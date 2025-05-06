
import streamlit as st
from dotenv import load_dotenv
import os

from utils.file_utils import extract_text_from_pdf, extract_text_from_docx
from utils.resume_utils import rewrite_resume, ats_score_feedback
from utils.pdf_utils import generate_pdf
from utils.pitch_utils import generate_pitch_deck, create_pptx

load_dotenv()
st.set_page_config(page_title="Resume & Pitch Deck Agent", layout="wide")
st.title("🤖 Resume & Pitch Deck Agent")

tab1, tab2 = st.tabs(["📄 Resume Assistant", "📊 Pitch Deck Generator"])

with tab1:
    st.header("Resume Tailoring & ATS Feedback")
    uploaded_file = st.file_uploader("Upload your resume (PDF or DOCX)", type=["pdf", "docx"])
    job_title = st.text_input("Target Job Title")

    if uploaded_file and job_title:
        if uploaded_file.name.endswith(".pdf"):
            resume_text = extract_text_from_pdf(uploaded_file)
        else:
            resume_text = extract_text_from_docx(uploaded_file)

        st.subheader("🎯 Tailored Resume")
        tailored = rewrite_resume(resume_text, job_title)
        st.text_area("Tailored Resume", tailored, height=300)
        pdf_data = generate_pdf(tailored)
        st.download_button("Download Tailored Resume (PDF)", pdf_data, file_name="Tailored_Resume.pdf")

        st.subheader("📊 ATS Score & Feedback")
        ats_results = ats_score_feedback(resume_text, job_title)
        st.text_area("ATS Feedback", ats_results, height=250)

with tab2:
    st.header("Startup Pitch Deck Generator")
    idea = st.text_area("Enter your startup idea or upload memo")
    if st.button("Generate Pitch Deck") and idea:
        slides = generate_pitch_deck(idea)
        pptx_file = create_pptx(slides)
        st.text_area("Pitch Deck Content", slides, height=300)
        st.download_button("Download Pitch Deck (PPTX)", pptx_file, file_name="Pitch_Deck.pptx")
