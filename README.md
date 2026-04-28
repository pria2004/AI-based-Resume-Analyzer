
# AI Resume & Job Description Analyzer

This is an AI-powered web application that analyzes a candidate’s resume against a given job description and provides structured scoring along with actionable feedback. The system is built using FastAPI for the backend and a lightweight HTML, CSS, and JavaScript frontend, with integration of a local LLaMA model via Ollama for intelligent analysis.

#TECHNOLOGIES USED
Python (FastAPI) – backend API development
HTML, CSS, JavaScript – frontend interface
LLaMA (via Ollama) – AI-based analysis
PyMuPDF, python-docx – resume and document parsing

#FEATURES
Upload resume files (PDF, DOCX, TXT)
Upload or paste job descriptions
AI-based evaluation of resume relevance
Score generation for overall match, searchability, hard skills, and soft skills
Automated recruiter-style suggestions for improvement
Simple and user-friendly interface

#PROJECT STRUCTURE
ai-resume-analyzer/ │
├── backend/ │
│   ├── main.py → API entry point
│   ├── llama_handler.py → Handles AI interaction
│   ├── utils/ → File parsing logic
│   ├── prompts/ → AI prompt templates
│   └── requirements.txt → Dependencies
│
├── frontend/ │
│   ├── index.html → User interface
│   ├── script.js → API integration
│   └── style.css → Styling

#SETUP INSTRUCTIONS
Install Python and required dependencies using requirements.txt
Install Ollama and run the LLaMA model locally
Start the backend server using uvicorn
Open the frontend index.html file in a browser

#HOW TO RUN
Navigate to the backend folder and start the server
Ensure the server runs on http://localhost:8000
Open the frontend and upload resume and job description to analyze

#LICENSE
This project is intended for educational and demonstration purposes and can be modified for further enhancements.
