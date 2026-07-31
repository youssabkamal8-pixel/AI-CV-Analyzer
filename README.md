# 🚀 [Tips Hindawi](https://www.tipshindawi.com/) Challenge (June–July) 2026

> 🏆 This repository is my official submission for the **Tips Hindawi Challenge (June–July 2026).**

## 👤 Participant

| Field | Value |
|--------|-------|
| **Full Name** | Youssab  Kamal Kamel |
| **Project Name** | AI CV Analyzer |
| **GitHub Username** | https://github.com/youssabkamal8-pixel/AI-CV-Analyzer |
| **Challenge Batch** | June–July 2026 |
| **Training Program** | Large Language Models (LLMs) Program |
| **Organization** | Edrak for AI |

---

# 📖 Project Overview

**AI CV Analyzer** is an AI-powered application that evaluates resumes against job descriptions using **Retrieval-Augmented Generation (RAG)**.

The system extracts text from uploaded PDF files, retrieves the most relevant information using semantic search, and generates an intelligent analysis that helps candidates understand how well their CV matches a specific job.

---

# ✨ Features

- 📄 Upload CV (PDF)
- 💼 Upload Job Description (PDF)
- 📊 Calculate CV Match Score
- ✅ Identify Matching Skills
- ❌ Detect Missing Skills
- 💡 Generate Personalized Recommendations
- 🔍 Semantic Search using FAISS
- 🤖 Retrieval-Augmented Generation (RAG)
- ⚡ FastAPI REST API
- 💻 Interactive Streamlit Interface

---

# 🛠️ Technologies Used

- Python
- LangChain
- Hugging Face Transformers
- Hugging Face Embeddings
- Sentence Transformers
- FAISS Vector Database
- PyTorch
- FastAPI
- Streamlit
- PyPDF
- RecursiveCharacterTextSplitter
- Prompt Engineering
- JSON Output
- RAG (Retrieval-Augmented Generation)

---

# ⚙️ Installation

```bash
pip install -r requirements.txt
```

Run the FastAPI server

```bash
uvicorn fastapi_app:app --reload
```

Run the Streamlit application

```bash
streamlit run streamlit_app.py
```

---

# 🚀 Usage

1. Upload a CV in PDF format.
2. Upload a Job Description in PDF format.
3. The system extracts the text from both documents.
4. Relevant information is retrieved using the RAG pipeline.
5. The AI generates an analysis including:

- Match Score
- Matching Skills
- Missing Skills
- Strengths
- Weaknesses
- Recommendations

---

# 📸 Demo

_Add screenshots or a demo GIF here._

---

# 📈 Results

- Built a complete RAG pipeline for resume analysis.
- Developed a semantic search engine using FAISS.
- Extracted and processed PDF documents.
- Built a FastAPI backend.
- Designed an interactive Streamlit interface.
- Generated AI-powered CV evaluation and recommendations.

---

# 🔮 Future Improvements

- 🌍 Arabic & English support
- 📊 ATS Resume Score
- 🤖 Interview Question Generator
- 📝 Cover Letter Generator
- 💼 Job Recommendation System
- 📈 Skill Gap Analysis

---

# 📚 About the Challenge

This project was developed as part of the **Tips Hindawi Challenge (June–July 2026).**

**Tips Hindawi** is the internships department of **Edrak for AI**, and the challenge encourages participants to build real-world AI applications, apply practical skills, and showcase their work through GitHub.

For more information, visit:

- https://www.tipshindawi.com/
- https://edrak4ai.com/en

---

# 📄 License

This project is shared for educational and portfolio purposes.