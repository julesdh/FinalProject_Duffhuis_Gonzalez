from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI
import os
from backend.prompts import resume_prompt, cover_letter_prompt

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_resume(name, experience, skills, job_desc):
    prompt = resume_prompt.format(name=name, experience=experience, skills=skills, job_desc=job_desc)
    response = client.chat.completions.create(
        model="gemini-2.0-flash",
        messages=[{"role": "system", "content": prompt}]
    )
    return response.choices[0].message.content

def generate_cover_letter(name, company, job_desc):
    prompt = cover_letter_prompt.format(name=name, company=company, job_desc=job_desc)
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "system", "content": prompt}]
    )
    return response.choices[0].message.content
# credit

# usage examples
if __name__ == '__main__':
    name="Jane Doe"
    experience="5 years of experience as data scientist at Microsoft"
    skills="Python, R, Machine Learning"
    job_desc="Machine Learning engineer"
    prompt = resume_prompt.format(name=name, experience=experience, skills=skills, job_desc=job_desc)
    print(prompt)

if __name__ == '__main__':
    name="John Doe"
    company="Microsoft"
    job_desc="Data Base Engineer"
    prompt = cover_letter_prompt.format(name=name, company=company, job_desc=job_desc)
    print(prompt)
