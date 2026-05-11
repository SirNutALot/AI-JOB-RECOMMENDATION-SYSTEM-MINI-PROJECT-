import os
import pandas as pd
from resume_parser import extract_text_from_pdf

DATASET_PATH = "../data/resumes"

def process_resume_dataset():

    data = []
    for category in os.listdir(DATASET_PATH):

        category_path = os.path.join(DATASET_PATH, category)

        if os.path.isdir(category_path):

            for file_name in os.listdir(category_path):

                if file_name.endswith(".pdf"):

                    file_path = os.path.join(category_path, file_name)

                    print(f"Processing: {file_name}")

                    text = extract_text_from_pdf(file_path)

                    data.append({
                        "category": category,
                        "file_name": file_name,
                        "resume_text": text
                    })
                    
    df = pd.DataFrame(data)
    return df