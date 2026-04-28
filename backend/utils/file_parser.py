import fitz  # PyMuPDF for PDFs
import docx
from fastapi import UploadFile

async def extract_text(file: UploadFile) -> str:
    ext = file.filename.split(".")[-1].lower()
    content = await file.read()
    
    if ext == "pdf":
        return extract_pdf(content)
    elif ext in "docx":
        return extract_docx(content)
    elif ext == "txt":
        return content.decode("utf-8")
    elif ext == "doc":
        return "Unsupported format (.doc). Please upload .docx or PDF."
    else:
        return ""

def extract_pdf(content: bytes) -> str:
    doc = fitz.open(stream=content, filetype="pdf")
    return "\n".join([page.get_text() for page in doc])

def extract_docx(content: bytes) -> str:
    from io import BytesIO
    doc = docx.Document(BytesIO(content))
    return "\n".join([para.text for para in doc.paragraphs])
