from fastapi import FastAPI
from pydantic import BaseModel
from nlp_preprocessor import preprocess_text
from skill_extractor import extract_skills
from job_matcher import (
    calculate_job_match,
    get_top_job_matches
)


# CREATE FASTAPI APP
app = FastAPI()


# =========================
# REQUEST MODEL
# =========================
class JobMatchRequest(BaseModel):

    resume_text: str
    job_description: str


# =========================
# ROOT ROUTE
# =========================
@app.get("/")
def home():

    return {
        "message": "AI Resume Matcher API Running"
    }


# =========================
# JOB MATCH ROUTE
# =========================
@app.post("/match_job")
# =========================
# TOP JOB RECOMMENDATIONS
# =========================
@app.post("/top_jobs")

def top_jobs(request: JobMatchRequest):

    # PREPROCESS
    cleaned_resume = preprocess_text(
        request.resume_text
    )

    # EXTRACT SKILLS
    skills = extract_skills(
        cleaned_resume
    )

    # GET TOP JOBS
    top_matches = get_top_job_matches(
        cleaned_resume
    )

    return {

        "top_matches": top_matches,
        "skills": skills
    }
    
def match_job(request: JobMatchRequest):

    # PREPROCESS
    cleaned_resume = preprocess_text(
        request.resume_text
    )

    # SKILL EXTRACTION
    skills = extract_skills(cleaned_resume)

    # MATCH SCORE
    match_score = calculate_job_match(
        cleaned_resume,
        request.job_description
    )

    return {

        "match_score": match_score,
        "skills": skills
    }