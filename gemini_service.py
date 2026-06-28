import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load variables from the .env file
load_dotenv()

# Read the API key
api_key = os.getenv("GEMINI_API_KEY")

# Tell Google's library which API key to use
genai.configure(api_key=api_key)

# Create a Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")


def analyze_resume(resume_text, job_description):
    prompt = f"""
You are an expert ATS Resume Reviewer.

Here is the resume:

{resume_text}

Here is the job description:

{job_description}

Please provide:

1. ATS Score out of 100
2. Missing Skills
3. Strengths
4. Weaknesses
5. Suggestions to improve the resume
"""

    response = model.generate_content(prompt)

    return response.text