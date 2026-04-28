from fastapi import FastAPI, UploadFile, Form, File
from fastapi.middleware.cors import CORSMiddleware
from utils.file_parser import extract_text
from llama_handler import analyze_resume_with_jd

app = FastAPI()



# CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
async def analyze(
    resume: UploadFile = File(...),
    jd_input_type: str = Form(...),  # 'upload' or 'paste'
    jd_file: UploadFile = File(None),
    jd_text: str = Form(None)
):
    # Extract resume text
    resume_text = await extract_text(resume)

    # Handle JD: upload or paste
    if jd_input_type == "upload" and jd_file:
        jd_text_final = await extract_text(jd_file)
    else:
        jd_text_final = jd_text

    # Send to LLaMA
    result = analyze_resume_with_jd(resume_text, jd_text_final)

    return result
