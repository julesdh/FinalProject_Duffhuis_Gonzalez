import os
from dotenv import load_dotenv
import google.generativeai as genai
from backend.prompts import resume_prompt, cover_letter_prompt
from docx import Document

# Load environment variables
load_dotenv()

# Configure the Google API key
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

# Set the default model for Gemini
DEF_MODEL = "models/gemini-2.0-flash-exp"


def get_model(model_name=DEF_MODEL):
    return genai.GenerativeModel(model_name)


def save_text_to_docx(text, filename="output.docx"):
    doc = Document()
    for line in text.split('\n'):
        doc.add_paragraph(line)

    output_path = os.path.join("generated_docs", filename)
    os.makedirs("generated_docs", exist_ok=True)
    doc.save(output_path)
    print(f"Word document saved to {output_path}")
    return output_path


def generate_resume(name, experience, skills, job_desc, save_doc=True):
    # Format the resume prompt
    prompt = resume_prompt.format(name=name, experience=experience, skills=skills, job_desc=job_desc)

    # Get the Gemini model
    model = get_model()

    # Generate the response
    response = model.generate_content(prompt)
    resume_text = response.text

    if save_doc:
        filename = f"{name.replace(' ', '_')}_Resume.docx"
        save_text_to_docx(resume_text, filename)

    return resume_text


def generate_cover_letter(name, company, job_desc, save_doc=True):
    # Format the cover letter prompt
    prompt = cover_letter_prompt.format(name=name, company=company, job_desc=job_desc)

    # Get the Gemini model
    model = get_model()

    # Generate the response
    response = model.generate_content(prompt)
    cover_letter_text = response.text

    if save_doc:
        filename = f"{name.replace(' ', '_')}_CoverLetter.docx"
        save_text_to_docx(cover_letter_text, filename)

    return cover_letter_text

# Usage examples
if __name__ == '__main__':
    # Example for generating a resume
    name = "Jane Doe"
    experience = "5 years of experience as data scientist at Microsoft"
    skills = "Python, R, Machine Learning"
    job_desc = "Machine Learning engineer"
    print(generate_resume(name, experience, skills, job_desc))

    # Example for generating a cover letter
    name = "John Doe"
    company = "Microsoft"
    job_desc = "Data Base Engineer"
    print(generate_cover_letter(name, company, job_desc))

