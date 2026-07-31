from fastapi import FastAPI, UploadFile, File
from pathlib import Path
import shutil

from pypdf import PdfReader

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import ChatOllama


# =========================
# App
# =========================

app = FastAPI(
    title="AI CV Analyzer API",
    version="1.0"
)


# =========================
# Paths
# =========================

BASE_DIR = Path.cwd()

UPLOAD_DIR = BASE_DIR / "uploads"
UPLOAD_DIR.mkdir(exist_ok=True)


# =========================
# PDF Extraction
# =========================

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    return text


def clean_text(text):
    return " ".join(text.split())


# =========================
# Documents
# =========================

def create_documents(text, source):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )

    chunks = splitter.split_text(text)

    documents = [
        Document(
            page_content=chunk,
            metadata={"source": source}
        )
        for chunk in chunks
    ]

    return documents


# =========================
# Models
# =========================

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={
        "device": "cpu"
    },
    encode_kwargs={
        "normalize_embeddings": True
    }
)

llm = ChatOllama(
    model="mistral",
    temperature=0
)


# =========================
# RAG Analysis
# =========================

def analyze_cv(cv_text, jd_text):

    cv_docs = create_documents(cv_text, "cv")
    jd_docs = create_documents(jd_text, "job_description")

    cv_store = FAISS.from_documents(
        cv_docs,
        embedding_model
    )

    jd_store = FAISS.from_documents(
        jd_docs,
        embedding_model
    )

    cv_retriever = cv_store.as_retriever(
        search_kwargs={"k": 5}
    )

    jd_retriever = jd_store.as_retriever(
        search_kwargs={"k": 5}
    )

    cv_context = "\n\n".join(
        doc.page_content
        for doc in cv_retriever.invoke(
            "candidate skills experience projects"
        )
    )

    jd_context = "\n\n".join(
        doc.page_content
        for doc in jd_retriever.invoke(
            "required skills qualifications"
        )
    )

    prompt = f"""
You are an AI HR assistant.

Compare the CV with the Job Description.

CV:
{cv_context}

Job Description:
{jd_context}

Return ONLY valid JSON.

{{
    "match_score": 0,
    "matching_skills": [],
    "missing_skills": [],
    "strengths": [],
    "weaknesses": [],
    "recommendations": [],
    "final_decision": ""
}}
"""

    response = llm.invoke(prompt)

    result = response.content.strip()

    result = result.replace("```json", "")
    result = result.replace("```", "")
    result = result.strip()

    return result


# =========================
# API Endpoint
# =========================

@app.post("/analyze")
async def analyze(
    cv: UploadFile = File(...),
    job_description: UploadFile = File(...)
):

    cv_path = UPLOAD_DIR / cv.filename
    jd_path = UPLOAD_DIR / job_description.filename

    with open(cv_path, "wb") as f:
        shutil.copyfileobj(cv.file, f)

    with open(jd_path, "wb") as f:
        shutil.copyfileobj(job_description.file, f)

    cv_text = clean_text(
        extract_text_from_pdf(cv_path)
    )

    jd_text = clean_text(
        extract_text_from_pdf(jd_path)
    )

    result = analyze_cv(
        cv_text,
        jd_text
    )

    return {
        "analysis": result
    }