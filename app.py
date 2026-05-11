import streamlit as st
import requests
import PyPDF2

st.set_page_config(
    page_title="AI Resume Matcher",
    layout="wide"
)

st.title("AI Job Recommendation System")

def extract_text_from_pdf(pdf_file):

    text = ""

    pdf_reader = PyPDF2.PdfReader(pdf_file)

    for page in pdf_reader.pages:

        extracted = page.extract_text()

        if extracted:
            text += extracted

    return text


uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf", "txt"]
)

resume_text = ""

if uploaded_file is not None:

    file_type = uploaded_file.name.split(".")[-1].lower()

    if file_type == "pdf":

        resume_text = extract_text_from_pdf(
            uploaded_file
        )

    elif file_type == "txt":

        resume_text = uploaded_file.read().decode(
            "latin-1"
        )

    st.subheader("📄 Resume Preview")

    st.text(resume_text[:1500])

if st.button("Analyze Resume", key="analyze_btn"):

    if resume_text:

        url = "http://127.0.0.1:8000/top_jobs"

        payload = {

            "resume_text": resume_text,
            "job_description": ""
        }

        try:

            response = requests.post(
                url,
                json=payload
            )

            if response.status_code == 200:

                result = response.json()

                st.subheader("🎯 Top Career Matches")

                for job in result["top_matches"]:

                    role = job["role"]
                    score = job["score"]

                    st.write(
                        f"✅ {role} — {score}%"
                    )

                st.subheader("🛠 Extracted Skills")

                for skill in result["skills"]:

                    st.write(f"✅ {skill}")

            else:

                st.error("Backend API Error")

                st.text(response.text)

        except Exception as e:

            st.error("Could not connect to backend.")

            st.text(str(e))

    else:

        st.warning(
            "Please upload a resume."
        )