Keep 2 terminals open in the relevant venv

1) Run: uvicorn api:app --reload
   Wait for application to startup

2) Then run: streamlit run app.py 


Main Directory:
---Docker composer 

---frontend (folder)
------app.py
------dockerfile (frontend)(rename file to just docker file)

---backend (folder)
remaining files

For Using Docker,
Change: [In app.py]

url = "http://127.0.0.1:8000/top_jobs"

TO the Docker version:

url = "http://backend:8000/top_jobs"
