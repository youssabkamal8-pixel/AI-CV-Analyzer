import streamlit as st
import requests
import json

st.set_page_config(page_title="AI CV Analyzer", layout="wide")

st.title("📄 AI CV Analyzer")

API_URL = "http://127.0.0.1:8000/analyze"

cv_file = st.file_uploader("Upload CV (PDF)", type="pdf")
job_file = st.file_uploader("Upload Job Description (PDF)", type="pdf")

if st.button("Analyze"):

    if cv_file is None or job_file is None:
        st.warning("Please upload both PDF files.")
        st.stop()

    files = {
        "cv": (
            cv_file.name,
            cv_file.getvalue(),
            "application/pdf"
        ),
        "job_description": (
            job_file.name,
            job_file.getvalue(),
            "application/pdf"
        )
    }

    with st.spinner("Analyzing..."):
        response = requests.post(API_URL, files=files)

    if response.status_code != 200:
        st.error(response.text)
        st.stop()

    data = response.json()

    analysis = data["analysis"]

    if isinstance(analysis, str):
        analysis = json.loads(analysis)

    st.success("Analysis Completed")

    st.metric("Match Score", f"{analysis['match_score']*100:.0f}%")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("✅ Matching Skills")
        st.write(analysis["matching_skills"])

        st.subheader("💪 Strengths")
        st.write(analysis["strengths"])

    with col2:
        st.subheader("❌ Missing Skills")
        st.write(analysis["missing_skills"])

        st.subheader("⚠ Weaknesses")
        st.write(analysis["weaknesses"])

    st.subheader("📚 Recommendations")
    st.write(analysis["recommendations"])

    st.subheader("📝 Final Decision")
    st.info(analysis["final_decision"])