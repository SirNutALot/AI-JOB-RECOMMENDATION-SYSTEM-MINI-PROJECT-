from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from job_roles import JOB_ROLES

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

def calculate_job_match(
    resume_text,
    job_description
):

    resume_embedding = model.encode(
        [resume_text]
    )

    job_embedding = model.encode(
        [job_description]
    )

    similarity = cosine_similarity(
        resume_embedding,
        job_embedding
    )

    match_score = round(
        float(similarity[0][0]) * 100,
        2
    )

    return match_score

def get_top_job_matches(
    resume_text
):

    results = []

    resume_embedding = model.encode(
        [resume_text]
    )

    for role, description in JOB_ROLES.items():

        job_embedding = model.encode(
            [description]
        )

        similarity = cosine_similarity(
            resume_embedding,
            job_embedding
        )

        score = round(
            float(similarity[0][0]) * 100,
            2
        )

        results.append({

            "role": role,
            "score": score
        })

    results = sorted(
        results,
        key=lambda x: x["score"],
        reverse=True
    )

    return results[:5]