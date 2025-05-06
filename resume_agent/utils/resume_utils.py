
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()



client = OpenAI(base_url="https://api.groq.com/openai/v1", api_key=os.getenv("GROQ_API_KEY"))

def ats_score_feedback(resume_text, job_title):
    prompt = f"""
    You are an ATS (Applicant Tracking System) analyzer.
    Analyze this resume for the role of {job_title}.
    Provide:
    1. ATS Score (out of 100)
    2. Missing keywords
    3. Suggestions for improvement
    Resume:
    {resume_text}
    """
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def rewrite_resume(resume_text, job_title):
    prompt = f"""
    Rewrite the following resume to be tailored for the role of {job_title}.
    Keep formatting clean. Do not use any asterisks or markdown. Keep it professional.
    Resume:
    {resume_text}
    """
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
