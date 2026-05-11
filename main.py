import pandas as pd

from nlp_preprocessor import preprocess_text
from skill_extractor import extract_skills
from job_matcher import calculate_job_match


# =========================
# LOAD DATASET
# =========================
DATASET_PATH = "../data/resume samples/resume_samples.txt"

data = []

with open(DATASET_PATH, "r", encoding="latin-1") as file:

    lines = file.readlines()

    # TAKE SMALL SAMPLE FOR SPEED
    for line in lines[:100]:

        parts = line.split(":::")

        if len(parts) == 3:

            resume_id = parts[0]
            occupations = parts[1]
            resume_text = parts[2]

            data.append({
                "resume_id": resume_id,
                "occupations": occupations,
                "resume_text": resume_text
            })


# CREATE DATAFRAME
df = pd.DataFrame(data)

print(df.head())


# =========================
# TAKE FIRST RESUME
# =========================
resume_text = df.iloc[0]["resume_text"]

print("\n===== RAW RESUME TEXT =====\n")
print(resume_text[:1000])


# =========================
# PREPROCESS TEXT
# =========================
cleaned_resume = preprocess_text(resume_text)

print("\n===== CLEANED RESUME =====\n")
print(cleaned_resume[:1000])


# =========================
# SKILL EXTRACTION
# =========================
skills = extract_skills(cleaned_resume)

print("\n===== EXTRACTED SKILLS =====")
print(skills)


# =========================
# SAMPLE JOB DESCRIPTION
# =========================
job_description = """
Looking for a Python developer with SQL,
Machine Learning, Docker, FastAPI,
and AWS experience.
"""


# =========================
# JOB MATCH SCORE
# =========================
match_score = calculate_job_match(
    cleaned_resume,
    job_description
)

print("\n===== JOB MATCH SCORE =====")
print(f"{match_score}%")