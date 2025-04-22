from fastapi import FastAPI
from backend.generator import generate_resume, generate_cover_letter, save_markdown_like_text_to_docx

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Resume and Cover Letter Generator API"}

@app.post("/generate_resume/")
def resume(name: str, experience: str, skills: str, education: str, job_desc: str):
    return {"resume": generate_resume(name, experience, skills, education, job_desc)}


@app.post("/generate_cover_letter/")
def cover_letter(name: str, company: str, job_desc: str):
    return {"cover_letter": generate_cover_letter(name, company, job_desc)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) # Runs on http://127.0.0.1:8000/docs
    # uvicorn backend.main:app --reload




