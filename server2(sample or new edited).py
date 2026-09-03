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
    """Make sure jobs[job_id]['result'] is a usable dict, not None."""
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
# 📊 GET JOB STATUS
# =========================
@app.get("/get-job/{job_id}")
def get_job(job_id: str):
    logging.info(f"Checking job: {job_id}")
    require_job(job_id)
    return jobs[job_id]


# =========================
# 📦 MAIN ATS PROCESSING API (Resume + JD)
# =========================
@app.post("/process-resume")
async def process_resume(
    file: UploadFile = File(...),
    jd_file: UploadFile = File(...)
):
    try:
        resume_path = os.path.join(UPLOAD_FOLDER, file.filename)
        jd_path = os.path.join(UPLOAD_FOLDER, "jd_" + jd_file.filename)

        with open(resume_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        with open(jd_path, "wb") as buffer:
            shutil.copyfileobj(jd_file.file, buffer)

        logging.info(f"Resume saved: {resume_path}")
        logging.info(f"JD saved: {jd_path}")

        from ai_engines.resume_text_extractor import ResumeTextExtractor
        from ai_engines.skill_extractor import SkillExtractor
        from ai_engines.ats_scorer import ats_score_engine
        from ai_engines.jd_parser import parse_job_description
        from ai_engines.experience_parser import extract_experience
        from ai_engines.education_parser import parse_education, extract_certifications

        extractor = ResumeTextExtractor()
        resume_text = extractor.extract_text(resume_path)
        jd_text = extractor.extract_text(jd_path)

        logging.info("Text extraction completed")

        experience = extract_experience(resume_text)
        if experience is None:
            experience = ""
        elif isinstance(experience, (list, dict)):
            experience = " ".join(map(str, experience)) if isinstance(experience, list) else str(experience)
        else:
            experience = str(experience)

        education_list = parse_education(resume_text)
        certifications = extract_certifications(resume_text)

        if education_list:
            education = " ".join([
                f"{edu.get('degree','')} {edu.get('field','')}"
                for edu in education_list
            ]).strip()
        else:
            education = "not specified"

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

        resume_data = {
            "skills": skills,
            "experience": experience,
            "education": education,
            "text": resume_text
        }

        jd_data = parse_job_description(jd_text)
        jd_data["text"] = jd_text

        score = ats_score_engine(resume_data, jd_data, nlp)
        logging.info(f"ATS Score generated: {score}")

        job_id = "job_" + str(len(jobs) + 1)

        jobs[job_id] = {
            "status": "completed",
            "result": {
                "skills": skills,
                "experience": experience,
                "education": education,
                "certifications": certifications,
                "jd_data": jd_data,
                "score": score  # resume <-> JD match score
            }
        }

        logging.info(f"Job completed: {job_id}")

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


# =====================================================
# 🗣️ HR INTERVIEW SCORING
# =====================================================
class HRAnswerIn(BaseModel):
    question_id: str
    answer_text: str
    relevance_score: Optional[float] = 0.7
    communication_score: Optional[float] = 70
    confidence_score: Optional[float] = 70
    contradiction: Optional[bool] = False
    is_vague: Optional[bool] = False


class HRInterviewRequest(BaseModel):
    candidate_type: str = "fresher"   # "fresher" or "experienced" -> feeds hr_weights.get_weights
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


# =====================================================
# 💻 TECHNICAL INTERVIEW SCORING
# =====================================================
class TechnicalAnswerIn(BaseModel):
    answer_text: str
    is_correct: bool = True


class TechnicalInterviewRequest(BaseModel):
    answers: List[TechnicalAnswerIn]


@app.post("/technical-interview/{job_id}")
def technical_interview(job_id: str, payload: TechnicalInterviewRequest):
    require_job(job_id)

    # NOTE: adjust this import path to match where you saved the file
    # with calculate_technical_score() + the technical_scoring_pipeline()
    # helper (see technical_scoring_pipeline_addition.py)
    from technical_ai.technical_scoring_engine import technical_scoring_pipeline

    answers = [a.dict() for a in payload.answers]

    try:
        result = technical_scoring_pipeline(answers)
    except Exception as e:
        logging.error(f"Technical scoring failed: {e}")
        raise HTTPException(status_code=500, detail=f"Technical scoring failed: {e}")

    ensure_result(job_id)["technical_interview"] = result
    logging.info(f"Technical interview scored for {job_id}: {result['technical_score']}")

    return result


# =====================================================
# 🧪 MACHINE TEST SCORING
# =====================================================
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

    # NOTE: adjust this import path to wherever machine_test_pipeline()
    # actually lives in your machine_test/ folder
    from machine_test.pipeline import machine_test_pipeline

    data = {
        "candidate_id": payload.candidate_id,
        "execution_results": payload.execution_results.dict(),
        "code_snapshot": payload.code_snapshot,
        "attempts": payload.attempts,
        "time_taken": payload.time_taken,
    }

    try:
        result = machine_test_pipeline(data)
    except Exception as e:
        logging.error(f"Machine test scoring failed: {e}")
        raise HTTPException(status_code=500, detail=f"Machine test scoring failed: {e}")

    ensure_result(job_id)["machine_test"] = result
    logging.info(f"Machine test scored for {job_id}: {result['final_score']}")

    return result


# =====================================================
# 🏆 FINAL HIRING SCORE (combines all 4 stages)
# =====================================================
# Adjust these weights to whatever your hiring process wants to emphasize.
FINAL_WEIGHTS = {
    "resume_match": 0.20,
    "hr": 0.25,
    "technical": 0.30,
    "machine_test": 0.25,
}


@app.get("/final-score/{job_id}")
def final_score(job_id: str):
    require_job(job_id)
    result = jobs[job_id].get("result") or {}

    # Resume/JD ATS match score
    ats = result.get("score")
    if isinstance(ats, dict):
        resume_match_score = ats.get("final_score") or ats.get("score") or 0
    else:
        resume_match_score = ats or 0

    hr_score = result.get("hr_interview", {}).get("hr_score", 0)
    technical_score = result.get("technical_interview", {}).get("technical_score", 0)
    machine_score = result.get("machine_test", {}).get("final_score", 0)

    missing = []
    if "score" not in result:
        missing.append("resume/JD (call /process-resume)")
    if "hr_interview" not in result:
        missing.append("hr interview (call /hr-interview/{job_id})")
    if "technical_interview" not in result:
        missing.append("technical interview (call /technical-interview/{job_id})")
    if "machine_test" not in result:
        missing.append("machine test (call /machine-test/{job_id})")

    final = (
        resume_match_score * FINAL_WEIGHTS["resume_match"] +
        hr_score * FINAL_WEIGHTS["hr"] +
        technical_score * FINAL_WEIGHTS["technical"] +
        machine_score * FINAL_WEIGHTS["machine_test"]
    )

    decision = (
        "Strong Hire" if final >= 75
        else "Consider" if final >= 55
        else "Reject"
    )

    final_result = {
        "job_id": job_id,
        "resume_match_score": resume_match_score,
        "hr_score": hr_score,
        "technical_score": technical_score,
        "machine_test_score": machine_score,
        "final_hiring_score": round(final, 2),
        "decision": decision,
        "missing_stages": missing,   # non-empty means score is computed on incomplete data
    }

    ensure_result(job_id)["final"] = final_result
    return final_result
