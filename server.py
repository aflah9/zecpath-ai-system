from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
from typing import List, Optional
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
def ensure_result(job_id: str):
    if jobs[job_id].get("result") is None:
        jobs[job_id]["result"] = {}
    return jobs[job_id]["result"]


def require_job(job_id: str):
    if job_id not in jobs:
        raise HTTPException(status_code=404, detail="Job not found")
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
        "certifications": certifications,
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
    
class HRAnswerIn(BaseModel):
    question_id: str
    answer_text: str
    relevance_score: float = 0.7
    communication_score: float = 70
    confidence_score: float = 70
    contradiction: bool = False
    is_vague: bool = False


class HRInterviewRequest(BaseModel):
    candidate_type: str = "fresher"
    answers: List[HRAnswerIn]


@app.post("/hr-interview/{job_id}")
def hr_interview(job_id: str, payload: HRInterviewRequest):
    require_job(job_id)

    from interview_ai.hr_scoring_engine import hr_scoring_pipeline

    answers = [a.dict() for a in payload.answers]

    try:
        result = hr_scoring_pipeline(answers, payload.candidate_type)
    except Exception as e:
        logging.error(f"HR scoring failed: {e}")
        raise HTTPException(status_code=500, detail=f"HR scoring failed: {e}")

    ensure_result(job_id)["hr_interview"] = result
    logging.info(f"HR interview scored for {job_id}: {result['hr_score']}")

    return result


class TechnicalAnswerIn(BaseModel):
    answer_text: str
    is_correct: bool = True


class TechnicalInterviewRequest(BaseModel):
    answers: List[TechnicalAnswerIn]


@app.post("/technical-interview/{job_id}")
def technical_interview(job_id: str, payload: TechnicalInterviewRequest):

    require_job(job_id)

    from technical_ai.technical_scoring_engine import technical_scoring_pipeline

    result = technical_scoring_pipeline(
        [a.dict() for a in payload.answers]
    )

    ensure_result(job_id)["technical_interview"] = result

    return result

class ExecutionResults(BaseModel):
    passed: int
    total: int
    runtime: float


class MachineTestRequest(BaseModel):
    candidate_id: str
    execution_results: ExecutionResults
    code_snapshot: str
    attempts: int
    time_taken: float


@app.post("/machine-test/{job_id}")
def machine_test(job_id: str, payload: MachineTestRequest):

    require_job(job_id)

    from machine_test.pipeline import machine_test_pipeline

    result = machine_test_pipeline({
        "candidate_id": payload.candidate_id,
        "execution_results": payload.execution_results.dict(),
        "code_snapshot": payload.code_snapshot,
        "attempts": payload.attempts,
        "time_taken": payload.time_taken
    })

    ensure_result(job_id)["machine_test"] = result

    return result

FINAL_WEIGHTS = {
    "resume_match":0.20,
    "hr":0.25,
    "technical":0.30,
    "machine_test":0.25
}


@app.get("/final-score/{job_id}")
def final_score(job_id:str):

    require_job(job_id)

    result = jobs[job_id]["result"]

    ats = result["score"]

    resume_score = result.get("score", {}).get("final_score", 0)

    hr = result.get("hr_interview",{}).get("hr_score",0)

    technical = result.get("technical_interview",{}).get("technical_score",0)

    machine = result.get("machine_test",{}).get("final_score",0)

    final = (
    resume_score * FINAL_WEIGHTS["resume_match"] +
    hr * FINAL_WEIGHTS["hr"] +
    technical * FINAL_WEIGHTS["technical"] +
    machine * FINAL_WEIGHTS["machine_test"]
)
   

    decision = (
        "Strong Hire"
        if final>=75
        else
        "Consider"
        if final>=55
        else
        "Reject"
    )
    return {
        "resume_match":resume_score,
        "hr_score":hr,
        "technical_score":technical,
        "machine_test_score":machine,
        "final_score":round(final,2),
        "decision":decision
    }
        
    