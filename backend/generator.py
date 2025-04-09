import os
from dotenv import load_dotenv
import google.generativeai as genai
from backend.prompts import resume_prompt, cover_letter_prompt

# Load environment variables
load_dotenv()

# Configure the Google API key
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

# Set the default model for Gemini
DEF_MODEL = "models/gemini-2.0-flash-exp"  # You can change this model name to the desired Gemini version

def get_model(model_name=DEF_MODEL):
    return genai.GenerativeModel(model_name)

def generate_resume(name, experience, skills, job_desc):
    # Format the resume prompt
    prompt = resume_prompt.format(name=name, experience=experience, skills=skills, job_desc=job_desc)

    # Get the Gemini model
    model = get_model()

    # Invoke the model and get the response
    response = model.generate_content(prompt)
    return response.text  # Extract the text from the response

def generate_cover_letter(name, company, job_desc):
    # Format the cover letter prompt
    prompt = cover_letter_prompt.format(name=name, company=company, job_desc=job_desc)

    # Get the Gemini model
    model = get_model()

    # Invoke the model and get the response
    response = model.generate_content(prompt)
    return response.text  # Extract the text from the response

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

