from fastapi import FastAPI, UploadFile, File, HTTPException
import shutil
import os
import spacy
import logging

# =========================
# 🚀 INIT APP
# =========================
app = FastAPI()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# =========================
# 🧠 LOAD MODELS
# =========================
nlp = spacy.load("en_core_web_md")

# =========================
# 📜 LOGGING SETUP
# =========================
logging.basicConfig(level=logging.INFO)

# =========================
# 🧵 SIMPLE ASYNC JOB STORE
# =========================
jobs = {}

# =========================
# 🏠 HOME ROUTE
# =========================
@app.get("/")
def home():
    return {"message": "ATS API is running successfully 🚀"}

# =========================
# 🧵 START JOB API (ASYNC STYLE)
# =========================
@app.post("/start-job")
def start_job():
    job_id = "job_" + str(len(jobs) + 1)

    jobs[job_id] = {
        "status": "processing",
        "result": None
    }

    logging.info(f"Job started: {job_id}")

    return {
        "job_id": job_id,
        "status": "processing"
    }

# =========================
# 📊 GET JOB STATUS (ERROR HANDLING)
# =========================
@app.get("/get-job/{job_id}")
def get_job(job_id: str):

    logging.info(f"Checking job: {job_id}")

    if job_id not in jobs:
        logging.error(f"Job not found: {job_id}")
        raise HTTPException(status_code=404, detail="Job not found")

    return jobs[job_id]

# =========================
# 📦 MAIN ATS PROCESSING API
# =========================
@app.post("/process-resume")
async def process_resume(
    file: UploadFile = File(...),
    jd_file: UploadFile = File(...)
):
    try:
        # =========================
        # 📁 SAVE FILES
        # =========================
        resume_path = os.path.join(UPLOAD_FOLDER, file.filename)
        jd_path = os.path.join(UPLOAD_FOLDER, "jd_" + jd_file.filename)

        with open(resume_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        with open(jd_path, "wb") as buffer:
            shutil.copyfileobj(jd_file.file, buffer)

        logging.info(f"Resume saved: {resume_path}")
        logging.info(f"JD saved: {jd_path}")

        # =========================
        # 📦 IMPORT YOUR MODULES
        # =========================
        from ai_engines.resume_text_extractor import ResumeTextExtractor
        from ai_engines.skill_extractor import SkillExtractor
        from ai_engines.ats_scorer import ats_score_engine
        from ai_engines.jd_parser import parse_job_description
        from ai_engines.experience_parser import extract_experience
        from ai_engines.education_parser import parse_education, extract_certifications

        # =========================
        # 🧠 TEXT EXTRACTION
        # =========================
        extractor = ResumeTextExtractor()

        resume_text = extractor.extract_text(resume_path)
        jd_text = extractor.extract_text(jd_path)

        logging.info("Text extraction completed")

        # =========================
        # 🧠 EXPERIENCE
        # =========================
        experience = extract_experience(resume_text)

        if experience is None:
            experience = ""
        elif isinstance(experience, list):
            experience = " ".join(map(str, experience))
        elif isinstance(experience, dict):
            experience = str(experience)
        else:
            experience = str(experience)

        # =========================
        # 🎓 EDUCATION + CERTS
        # =========================
        education_list = parse_education(resume_text)
        certifications = extract_certifications(resume_text)

        if education_list:
            education = " ".join([
                f"{edu.get('degree','')} {edu.get('field','')}"
                for edu in education_list
            ]).strip()
        else:
            education = "not specified"

        # =========================
        # 🧠 SKILL EXTRACTION
        # =========================
        try:
            skill_extractor = SkillExtractor()
            skills_result = skill_extractor.extract_skills(resume_text)

            if isinstance(skills_result, dict):
                skills = list(skills_result.keys())
            elif isinstance(skills_result, list):
                skills = skills_result
            else:
                skills = []

            skills = [str(s) for s in skills]

        except Exception as e:
            logging.error(f"Skill extraction failed: {e}")
            skills = []

        logging.info(f"Skills extracted: {skills}")

        # =========================
        # 📊 RESUME + JD DATA
        # =========================
        resume_data = {
            "skills": skills,
            "experience": experience,
            "education": education,
            "text": resume_text
        }

        jd_data = parse_job_description(jd_text)
        jd_data["text"] = jd_text

        # =========================
        # 🧠 ATS SCORING
        # =========================
        score = ats_score_engine(resume_data, jd_data, nlp)

        logging.info(f"ATS Score generated: {score}")

        # =========================
        # 🧵 CREATE JOB RESULT
        # =========================
        job_id = "job_" + str(len(jobs) + 1)

        jobs[job_id] = {
            "status": "completed",
            "result": {
                "skills": skills,
                "experience": experience,
                "education": education,
                "jd_data": jd_data,
                "score": score
            }
        }

        logging.info(f"Job completed: {job_id}")

        # =========================
        # 📤 RESPONSE
        # =========================
        return {
            "status": "success",
            "job_id": job_id
        }

    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return {
            "status": "error",
            "message": str(e)
        }