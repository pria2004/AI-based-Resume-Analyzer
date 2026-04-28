# 🚀 AI Resume & Job Description Analyzer

An AI-powered web application that analyzes a candidate’s resume against a given job description and provides structured scoring along with actionable, recruiter-style feedback.

Built using FastAPI for the backend and a lightweight HTML, CSS, and JavaScript frontend, the system integrates a locally hosted LLaMA model via Ollama to deliver intelligent and context-aware analysis.

---

## 🛠️ Technologies Used

* **Python (FastAPI)** – Backend API development
* **HTML, CSS, JavaScript** – Frontend interface
* **LLaMA (via Ollama)** – AI-powered analysis
* **PyMuPDF, python-docx** – Resume and document parsing

---

## ✨ Features

* Upload resume files (PDF, DOCX, TXT)
* Upload or paste job descriptions
* AI-based evaluation of resume relevance
* Score generation:

  * Overall Score
  * Searchability Score
  * Hard Skills Match
  * Soft Skills Match
* Automated recruiter-style improvement suggestions
* Simple and user-friendly interface

---

## 📁 Project Structure

```
ai-resume-analyzer/
│
├── backend/
│   ├── main.py              → API entry point
│   ├── llama_handler.py     → AI processing logic
│   ├── utils/               → File parsing utilities
│   ├── prompts/             → AI prompt templates
│   └── requirements.txt     → Dependencies
│
├── frontend/
│   ├── index.html           → User interface
│   ├── script.js            → API integration
│   └── style.css            → Styling
```

---

## ⚙️ Setup Instructions

1. Install Python and required dependencies:

   ```
   pip install -r requirements.txt
   ```

2. Install Ollama and run the LLaMA model:

   ```
   ollama run llama3
   ```

3. Start the backend server:

   ```
   uvicorn main:app --reload
   ```

4. Open the frontend:

   ```
   frontend/index.html
   ```

---

## ▶️ How to Use

* Upload your resume
* Upload or paste the job description
* Click **Analyze**
* View scores and improvement suggestions instantly

---

## 📌 Notes

* Backend runs on: `http://localhost:8000`
* Requires Ollama to be installed and running locally
* Designed for demonstration and educational purposes

---

## 📄 License

This project is open for educational use and can be modified for further enhancements.
