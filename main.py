from utils.logger import log_info
from ai_engines.resume_text_extractor import ResumeTextExtractor
from ai_engines.jd_parser import parse_job_description
from ai_engines.resume_parser import ResumeParser
from ai_engines.skill_extractor import SkillExtractor

from models.candidate import Candidate
from models.skill import Skill
from models.experience import Experience

import os
import json

log_info("AI System Started")
print(" System Running...")

# ==============================
# 🔹 STEP 1: RESUME EXTRACTION
# ==============================
extractor = ResumeTextExtractor()
folder = "sample_resumes"

files = os.listdir(folder)
print(" Files found:", files)

for file in files:
    print(" Checking:", file)

    if file.lower().endswith((".pdf", ".docx")):

        path = os.path.join(folder, file)

        print("\n Processing:", file)

        cleaned_text = extractor.extract_text(path)

        output_path = f"outputs/{file}.txt"

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(cleaned_text)

        print(" Saved to:", output_path)

# Save latest resume separately
with open("outputs/cleaned_resume.txt", "w", encoding="utf-8") as f:
    f.write(cleaned_text)

print(" Resume processed successfully!")

# ==============================
# 🔹 STEP 2: JOB DESCRIPTION PARSING (Day 6)
# ==============================
jd_file = "sample_data/job_description.pdf"

jd_text = extractor.extract_text(jd_file)
jd_result = parse_job_description(jd_text)

print("\n JD Parsed Data:")
print(jd_result)
import json

with open("outputs/jd_output.json", "w") as f:
    json.dump(jd_result, f, indent=4)

print("JD saved to outputs/jd_output.json")

# ==============================
# 🔹 STEP 3: RESUME PARSING (Day 4)
# ==============================
with open("outputs/cleaned_resume.txt", "r", encoding="utf-8") as f:
    text = f.read()

parser = ResumeParser(text)
data = parser.parse()

print("\n Parsed Resume Data:\n", data)

# Create Candidate
c = Candidate(data.get("name", "Unknown"), "unknown@email.com")

# Add skills (basic parser skills)
for skill in data.get("skills", []):
    c.skills.append(Skill(skill, "technical", "intermediate"))

# Experience
duration = data.get("experience") or data.get("experience_years") or "Not Found"

c.experience.append(
    Experience(
        "Unknown Company",
        data.get("role", "Unknown Role"),
        duration
    )
)

c.education = data.get("education", "Not Found")

# ==============================
# 🔹 STEP 4: SKILL EXTRACTION ENGINE (Day 9 )
# ==============================
skill_extractor = SkillExtractor()

extracted_skills = skill_extractor.extract_skills(text)

# SAVE OUTPUT (IMPORTANT)
with open("outputs/skills.json", "w") as f:
    json.dump(extracted_skills, f, indent=4)

print("\n Extracted Skills:")
print(extracted_skills)
print("\n Extracted Skills (Readable Format):\n")

for skill, info in extracted_skills.items():
    print(f"{skill} → Category: {info['category']}, Confidence: {info['confidence']}")


print("\n Skills saved to outputs/skills.json")

# ==============================
# 🔹 FINAL OUTPUT
# ==============================
final_output = {
    "name": c.name,
    "education": c.education,
    "experience": [
        {
            "company": e.company_name,
            "role": e.designation,
            "duration": e.duration
        }
        for e in c.experience
    ],
    "parsed_skills": [s.skill_name for s in c.skills],
    "extracted_skills": extracted_skills
}


print("\n FINAL OUTPUT:\n")
print(final_output)

print("\n******** Day 1–9 Completed Successfully!********")


#------------
#   day 10
#esperince parser
#---------------

from ai_engines.resume_text_extractor import ResumeTextExtractor
from ai_engines.resume_parser import ResumeParser
from parser.section_segmenter import segment_sections
from ai_engines.experience_parser import parse_experience

RESUME_FOLDER = "sample_resumes"
OUTPUT_FOLDER = "outputs"


def main():
    extractor = ResumeTextExtractor()

    for file_name in os.listdir(RESUME_FOLDER):
        file_path = os.path.join(RESUME_FOLDER, file_name)

        print(f"\n Processing: {file_name}")

        # -----------------------------
        # STEP 1: Extract Text (Your Engine ✅)
        # -----------------------------
        try:
            resume_text = extractor.extract_text(file_path)
        except Exception as e:
            print(f" Skipping {file_name}: {e}")
            continue

        # -----------------------------
        # STEP 2: Resume Parser (Basic Info)
        # -----------------------------
        parser = ResumeParser(resume_text)
        basic_data = parser.parse()

        # -----------------------------
        # STEP 3: Section Segmentation (Day 9)
        # -----------------------------
        sections = segment_sections(resume_text)

        sections = segment_sections(resume_text)

        #  DEBUG EXPERIENCE SECTION
       # print("\n--- EXPERIENCE SECTION ---")
        #print(sections.get("experience", "NOT FOUND")[:500])

        # DEBUG (optional)
        # print(sections.keys())

        # -----------------------------
        # STEP 4: Experience Parsing (Day 10)
        # -----------------------------
        experience_data = parse_experience(sections)

        # -----------------------------
        # STEP 5: Combine Output
        # -----------------------------
        final_output = {
            "basic_info": basic_data,
            "experience_analysis": experience_data
        }

        # -----------------------------
        # STEP 6: Save Output
        # -----------------------------
        os.makedirs(OUTPUT_FOLDER, exist_ok=True)

        output_file = os.path.join(
            OUTPUT_FOLDER,
            f"{file_name}_final.json"
        )

        with open(output_file, "w") as f:
            json.dump(final_output, f, indent=4)


        print("\nOUTPUT:")
        print(json.dumps(experience_data, indent=4))

        print(f"Saved to: {output_file}")


if __name__ == "__main__":
    main()
print("********DAY 10 CMPLETED********")
    #-------day 10 over--------#
#-----------day 13---------------
print("*******day 13********")

# main.py

import json
import spacy
from ai_engines.ats_scorer import ats_score_engine

# 🔹 Load NLP model
nlp = spacy.load("en_core_web_md")


# 🔹 Load Resume Data (existing output)
def load_resume_data():
    import json

    try:
        with open("outputs/credit_analyst_sample2.pdf_final.json", "r") as f:
            data = json.load(f)
    except:
        print(" Resume file not found")
        return {}

    basic = data.get("basic_info", {})
    exp_data = data.get("experience_analysis", {})

    # Skills
    skills = basic.get("skills", [])

    #  Education
    education = basic.get("education", "")

    #  Experience text
    experiences = exp_data.get("experiences", [])
    experience_text = " ".join([exp.get("role", "") for exp in experiences])

    # fallback
    if not experience_text:
        experience_text = exp_data.get("total_experience", "")

    return {
        "skills": skills,
        "experience": experience_text,
        "education": education,
        "text": json.dumps(data)  # full text for semantic
    }


# 🔹 Load Job Description Data
def load_jd_data():
    import json

    with open("outputs/jd_output.json", "r") as f:
        jd = json.load(f)

    return {
        "role": jd.get("role", "credit analyst"),  # ✅ FIX HERE
        "skills": jd.get("skills", []),
        "keywords": jd.get("experience", "").split(),
        "education": jd.get("education", ""),
        "text": json.dumps(jd)
    }

# 🔹 MAIN FUNCTION
def main():

    print(" Running ATS Scoring System...\n")

    # Load data
    resume_data = load_resume_data()
    jd_data = load_jd_data()

    # Debug prints (optional)
    print(" Resume Skills:", resume_data["skills"])
    print(" Resume Education:", resume_data["education"])
    print(" Resume Experience:", resume_data["experience"][:100], "...\n")

    # Run ATS scoring
    result = ats_score_engine(resume_data, jd_data, nlp,role="credit_analyst")

    # Print result
    print("=====  ATS SCORE RESULT =====")
    print(json.dumps(result, indent=4))

    # Save result
    with open("outputs/ats_score.json", "w") as f:
        json.dump(result, f, indent=4)

    print("\n ATS Score saved to outputs/ats_score.json")


# 🔹 Run
if __name__ == "__main__":
    main()


#-------over day 13-----------


print("******DAY 14******")
#-------day 14--------------
# main.py

# main.py

import json
import os
import spacy
from ai_engines.ats_scorer import ats_score_engine

# 🔹 Load NLP model
nlp = spacy.load("en_core_web_md")


# ==============================
# 🔹 SHORTLISTING LOGIC
# ==============================
def get_status(score):
    if score >= 65:
        return "Shortlisted"
    elif score >= 50:
        return "Review"
    else:
        return "Rejected"


# ==============================
# 🔹 LOAD ALL RESUMES
# ==============================
def load_all_resumes(folder_path="outputs"):
    resumes = []

    for file in os.listdir(folder_path):
        if file.endswith("_final.json"):
            try:
                with open(os.path.join(folder_path, file), "r") as f:
                    data = json.load(f)
            except:
                continue

            basic = data.get("basic_info", {})
            exp_data = data.get("experience_analysis", {})

            skills = basic.get("skills", [])
            education = basic.get("education", "")

            experiences = exp_data.get("experiences", [])
            experience_text = " ".join([exp.get("role", "") for exp in experiences])

            if not experience_text:
                experience_text = exp_data.get("total_experience", "")

            resumes.append({
                "name": f"{basic.get('name', 'Unknown')} ({file})",  #  unique name
                "skills": skills,
                "education": education,
                "experience": experience_text,
                "text": json.dumps(data)
            })

    return resumes


# ==============================
# 🔹 LOAD JOB DESCRIPTION
# ==============================
def load_jd_data():
    try:
        with open("outputs/jd_output.json", "r") as f:
            jd = json.load(f)
    except:
        print(" JD file not found")
        return {}

    return {
        "role": jd.get("role", "credit analyst"),
        "skills": jd.get("skills", []),
        "keywords": jd.get("experience", "").split(),
        "education": jd.get("education", ""),
        "text": json.dumps(jd)
    }


# ==============================
# 🔹 MAIN FUNCTION
# ==============================
def main():

    print(" Running ATS Ranking System...\n")

    jd_data = load_jd_data()
    all_resumes = load_all_resumes()

    if not all_resumes:
        print(" No resumes found")
        return

    results = []

    # 🔹 Process each candidate
    for resume in all_resumes:

        print(f" Processing: {resume['name']}")

        result = ats_score_engine(
            resume,
            jd_data,
            nlp,
            role="credit_analyst"
        )

        score = result["final_score"]

        results.append({
            "name": resume["name"],
            "score": score,
            "status": get_status(score),  # shortlisting
            "breakdown": result["breakdown"],
            "explanation": result["explanation"]
        })

    #  SORT (Ranking)
    ranked = sorted(results, key=lambda x: x["score"], reverse=True)

    # ==============================
    # 🔹 PRINT RANKING
    # ==============================
    print("\n CANDIDATE RANKING:\n")

    for i, candidate in enumerate(ranked, start=1):
        print(f"{i}. {candidate['name']} → {candidate['score']}% ({candidate['status']})")

    # ==============================
    # 🔹 TOP CANDIDATE
    # ==============================
    top_candidate = ranked[0]
    print(f"\n Selected Candidate: {top_candidate['name']} ({top_candidate['score']}%)")

    # ==============================
    # 🔹 SAVE OUTPUT
    # ==============================
    with open("outputs/candidate_ranking.json", "w") as f:
        json.dump(ranked, f, indent=4)

    print("\n Ranking saved to outputs/candidate_ranking.json")


# ==============================
# 🔹 RUN
# ==============================
if __name__ == "__main__":
    main()


print("***********day 15***********")
#-------------day 15---------
import os
import json
import spacy

from ai_engines.ats_scorer import ats_score_engine
from ai_engines.fairness_engine import fairness_pipeline, normalize_resume


#  Load NLP model
nlp = spacy.load("en_core_web_sm")


#  Load all resumes
def load_all_resumes(folder="outputs"):
    resumes = []

    for file in os.listdir(folder):
        #  Only load resume files
        if file.endswith(".json") and "credit_analyst" in file.lower():
            file_path = os.path.join(folder, file)

            with open(file_path, "r") as f:
                data = json.load(f)

                if isinstance(data, list):
                    resumes.extend(data)
                elif isinstance(data, dict):
                    resumes.append(data)

    return resumes


#  Load JD
def load_jd_data():
    path = os.path.join("outputs", "jd_output.json")
    with open(path, "r") as f:
        return json.load(f)


#  MAIN
if __name__ == "__main__":

    print("*********** DAY 15 + MULTI-RESUME ***********")

    # Load data
    all_resumes = load_all_resumes()
    jd_data = load_jd_data()

    #  Create JD text for semantic scoring
    role = jd_data.get("role", "")
    skills = " ".join(jd_data.get("skills", []))
    experience = jd_data.get("experience", "")
    projects = jd_data.get("projects", "")
    education = jd_data.get("education", "")

    jd_data["text"] = f"{role} {skills} {experience} {projects} {education}".strip().lower()

    results = []

    #  PROCESS EACH RESUME
    for idx, resume_data in enumerate(all_resumes, start=1):

        print(f"\n📄 Processing Resume {idx}...")

        #  Normalize
        clean_resume = normalize_resume(resume_data)

        #  Convert experience → text (for ATS)
        if isinstance(clean_resume.get("experience"), list):
            exp_text = ""
            for exp in clean_resume["experience"]:
                if isinstance(exp, dict):
                    exp_text += f"{exp.get('role','')} {exp.get('company','')} "
            clean_resume["experience"] = exp_text.strip().lower()

        #  Create text for semantic scoring
        skills_text = " ".join(clean_resume.get("skills", []))
        exp_text = clean_resume.get("experience", "")

        clean_resume["text"] = f"{skills_text} {exp_text}".strip()

        # ATS scoring
        result = ats_score_engine(clean_resume, jd_data, nlp)
        final_score = result["final_score"]

        #  Fairness
        fair_output = fairness_pipeline(resume_data, final_score)

        #  Append result
        results.append(fair_output)

    #  If no results
    if not results:
        print(" No resumes processed")
        exit()

    #  SORT (Ranking)
    results.sort(key=lambda x: x["final_score"], reverse=True)

    #  ADD STATUS (Shortlisting)
    for r in results:
        score = r.get("final_score", 0)

        if score >= 60:
            r["status"] = "SHORTLISTED"
        elif score >= 45:
            r["status"] = "REVIEW"
        else:
            r["status"] = "REJECTED"

    #  FINAL OUTPUT
    print("\n🎯 FINAL RANKED CANDIDATES:\n")

    for i, r in enumerate(results, 1):
        print(f"Rank {i}")
        print("Score:", r.get("final_score"))
        print("Status:", r.get("status"))
        print("Skills:", r["resume"].get("skills", []))
        print("Experience:", r["resume"].get("experience", []))
        print("Education:", r["resume"].get("education", ""))
        print("-" * 40)

    #  Optional: Save results
    with open("outputs/final_results.json", "w") as f:
        json.dump(results, f, indent=4)

    print("\n Results saved to outputs/final_results.json")


#----------DAY 15-------------
#-----------day 18--------
print("************day 18************")
import os
import time
import json
import logging

from utils.cache_handler import load_from_cache, save_to_cache
from utils.text_cleaner import clean_text
from ai_engines.resume_processor import process_resume
from ai_engines.scorer import calculate_score

# Logging setup
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

# Example JD Skills (replace with parsed JD later)
JD_SKILLS = ["excel", "sql", "financial analysis", "communication"
             "financial statement analysis",
    "risk assessment",
    "excel",
    "reporting",
    "analytical thinking",
    "ratio analysis",
    "cash flow",
    "credit appraisal",
    "collateral",
    "debt equity",
    "interest coverage",
    "dscr"
]


def process_resume_file(file_path):
    file_name = os.path.basename(file_path)

    # 🔹 Cache check
    USE_CACHE = False  # turn on/off easily

    cached = load_from_cache(file_name)

    if cached and USE_CACHE:
        return cached

    try:
        print("Processing:", file_name)

        data = process_resume(file_path, clean_text)

        print("DEBUG DATA:", data)  # IMPORTANT

        #  If extraction failed
        if not data:
            print(" No data extracted")
            return None

        score = calculate_score(data, JD_SKILLS, jd_experience=3)

        result = {
            "file": file_name,
            "skills": data.get("skills", []),
            "categories": data.get("categories", {}),
            "experience": data.get("experience", 0),
            "score": score
        }

        save_to_cache(file_name, result)

        return result

    except Exception as e:
        print(f" ERROR in {file_name}:", e)
        return None


def process_all_resumes(folder_path):
    results = []

    print(" Files found:", os.listdir(folder_path))  # DEBUG

    for file in os.listdir(folder_path):
        print(" Checking:", file)  # DEBUG

        if file.endswith(".pdf"):
            print(" Processing PDF:", file)  # DEBUG

            path = os.path.join(folder_path, file)

            result = process_resume_file(path)
            print("DEBUG RESULT:", result)

            if result:
                results.append(result)

    return results


def rank_candidates(results):
    return sorted(results, key=lambda x: x["score"], reverse=True)


if __name__ == "__main__":
    folder = "sample_resumes"  # put your PDF resumes here

    if not os.path.exists(folder):
        print(" 'resumes' folder not found!")
        exit()

    results = process_all_resumes(folder)

    ranked = rank_candidates(results)

    os.makedirs("outputs", exist_ok=True)

    # Save output
    with open("outputs/final_results.json", "w") as f:
        json.dump(ranked, f, indent=4)

    print("\n FINAL RANKED CANDIDATES:\n")

    for r in ranked:
        print(r)

    print("\n Processing Complete!")

#--------------day 21---------------------------------

    print("----------day 21----------")
# ==============================
# 🔥 DAY 18 + DAY 21 FINAL MAIN.PY
# ==============================

print("************ DAY 18 + DAY 21 ************")

import os
import json
import logging

from utils.cache_handler import load_from_cache, save_to_cache
from utils.text_cleaner import clean_text
from ai_engines.resume_processor import process_resume
from ai_engines.scorer import calculate_score
from ai_engines.eligibility_engine import evaluate_candidate

# ==============================
# 🔹 LOGGING SETUP
# ==============================
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


# ==============================
# 🔹 JOB DESCRIPTION SKILLS
# ==============================
JD_SKILLS = [
    "excel",
    "sql",
    "financial analysis",
    "communication",
    "financial statement analysis",
    "risk assessment",
    "reporting",
    "analytical thinking",
    "ratio analysis",
    "cash flow",
    "credit appraisal",
    "collateral",
    "debt equity",
    "interest coverage",
    "dscr"
]


# ==============================
# 🔹 PROCESS SINGLE RESUME
# ==============================
def process_resume_file(file_path):

    file_name = os.path.basename(file_path)

    # 🔹 CACHE CHECK
    USE_CACHE = False

    cached = load_from_cache(file_name)

    if cached and USE_CACHE:
        return cached

    try:

        print(f"\n📄 Processing: {file_name}")

        # 🔹 RESUME PROCESSING
        data = process_resume(file_path, clean_text)

        print("DEBUG DATA:", data)

        # 🔹 EXTRACTION FAILED
        if not data:
            print("❌ No data extracted")
            return None

        # 🔹 CALCULATE ATS SCORE
        score = calculate_score(
            data,
            JD_SKILLS,
            jd_experience=3
        )

        # 🔹 FINAL RESULT
        result = {
            "file": file_name,
            "skills": data.get("skills", []),
            "categories": data.get("categories", {}),
            "experience": data.get("experience", 0),
            "score": score
        }

        print("DEBUG RESULT:", result)

        # 🔹 SAVE CACHE
        save_to_cache(file_name, result)

        return result

    except Exception as e:

        print(f"❌ ERROR in {file_name}: {e}")

        return None


# ==============================
# 🔹 PROCESS ALL RESUMES
# ==============================
def process_all_resumes(folder_path):

    results = []

    print("\n📂 Files found:", os.listdir(folder_path))

    for file in os.listdir(folder_path):

        print("👉 Checking:", file)

        if file.endswith(".pdf"):

            print("✅ Processing PDF:", file)

            path = os.path.join(folder_path, file)

            result = process_resume_file(path)

            if result:
                results.append(result)

    return results


# ==============================
# 🔹 RANK CANDIDATES
# ==============================
def rank_candidates(results):

    return sorted(
        results,
        key=lambda x: x["score"],
        reverse=True
    )


# ==============================
# 🔹 MAIN
# ==============================
if __name__ == "__main__":

    folder = "sample_resumes"

    # 🔹 CHECK FOLDER
    if not os.path.exists(folder):

        print("❌ 'sample_resumes' folder not found!")

        exit()

    # ==============================
    # 🔹 STEP 1: PROCESS RESUMES
    # ==============================
    results = process_all_resumes(folder)

    # ==============================
    # 🔹 STEP 2: RANK CANDIDATES
    # ==============================
    ranked = rank_candidates(results)

    # 🔹 CREATE OUTPUT FOLDER
    os.makedirs("outputs", exist_ok=True)

    # ==============================
    # 🔹 SAVE RANKING OUTPUT
    # ==============================
    with open("outputs/final_results.json", "w") as f:

        json.dump(ranked, f, indent=4)

    print("\n🎯 FINAL RANKED CANDIDATES:\n")

    for r in ranked:
        print(r)

    # ==============================
    # 🔥 DAY 21 – ELIGIBILITY ENGINE
    # ==============================
    print("\n******** DAY 21 – ELIGIBILITY RESULTS ********\n")

    eligibility_results = []

    for candidate in ranked:

        result = evaluate_candidate(candidate)

        eligibility_results.append(result)

        print(result)

    # ==============================
    # 🔹 SAVE ELIGIBILITY OUTPUT
    # ==============================
    with open("outputs/eligibility_results.json", "w") as f:

        json.dump(eligibility_results, f, indent=4)

    print("\n✅ Eligibility results saved to outputs/eligibility_results.json")

    print("\n✅ Processing Complete!")

    #----------day 24----------


    print("**************day 24***********")

from screening_ai.transcript_cleaner import process_audio_answers


audio_inputs = [

    "um i worked in python development",

    "uh i know machine learning and sql",

    "",

    "hmm i am interested in ai"

]


results = process_audio_answers(audio_inputs)


for result in results:
    print(result)

#######-------day 26--------------------------------------------

print("*******************DAY 26***************")

from screening_ai.scoring_engine import (
    screening_scoring_pipeline,
    generate_explanation
)

# -----------------------------------
# Candidate Answers
# -----------------------------------

answers = [

    {
        "question_id": "Q1",
        "original_text": "I know fiinancial analysis excel SQl",
        "intent": "skills",
        "skills": ["excel","sql", "financial analysis"],
        "experience_years": 2,
        "availability": "Immediate",
        "off_topic": False,
        "is_vague": False
    },

    {
        "question_id": "Q3",
        "original_text": "I have 2 years experience in credit analyst",
        "intent": "experience",
        "skills": [],
        "experience_years": 2,
        "availability": "unknown",
        "off_topic": False,
        "is_vague": False
    }

]

# -----------------------------------
# Expected Intent Mapping
# -----------------------------------

intent_map = {

    "Q1": "skills",

    "Q3": "experience"
}

# -----------------------------------
# Run Screening Pipeline
# -----------------------------------

result = screening_scoring_pipeline(

    candidate_id="C123",

    answers=answers,

    intent_map=intent_map
)

# -----------------------------------
# Print Final Screening Result
# -----------------------------------

print("\n==============================")
print(" FINAL SCREENING RESULT ")
print("==============================\n")

print(result)

# -----------------------------------
# Print Per Question Breakdown
# -----------------------------------

print("\n==============================")
print(" PER QUESTION BREAKDOWN ")
print("==============================\n")

for item in result["details"]:

    print(f"Question ID : {item['question_id']}")

    print(f"Scores       : {item['scores']}")

    print(f"Final Score  : {item['final_score']}")

    print("-----------------------------------")

# -----------------------------------
# Generate Explainable Outputs
# -----------------------------------

print("\n==============================")
print(" EXPLAINABLE SCORING OUTPUT ")
print("==============================\n")

for ans in answers:

    explanation = generate_explanation(ans)

    print(explanation)

    print("-----------------------------------")

####-------------------DAY27-------------



print('***********day 27***********')

from screening_ai.behavior_report import (
    generate_behavior_report
)

# Example Candidate Answer

text = (
    "I am confident in my Python skills "
    "and have strong experience"
)

duration = 5

# Generate Report

result = generate_behavior_report(
    text,
    duration
)

print(result)


##############---------------DAY 28-------------


print("*************DAY 28*********************")

from screening_ai.report_generator import generate_screening_report

from screening_ai.report_exporter import export_report_text

from data.sample_answers import answers
from data.sample_scores import scores
from data.sample_behavior import behavior_reports

# -----------------------------------
# Generate Report
# -----------------------------------

report = generate_screening_report(

    candidate_id="C123",

    job_id="J101",

    answers=answers,

    scores=scores,

    behavior_reports=behavior_reports
)

# -----------------------------------
# Print JSON Report
# -----------------------------------

print(report)

# -----------------------------------
# Export Recruiter Text Report
# -----------------------------------

text_report = export_report_text(report)

print(text_report)


######_________________DAY 29-------------------

######_________________DAY 29-------------------

print("***********DAY 29***********")

import json

from screening_ai.conversation_engine import ConversationStateMachine
from screening_ai.error_handling import detect_issue

# Load conversation flow
with open("screening_ai/conversation_flow.json") as f:
    flow = json.load(f)

# Create engine
engine = ConversationStateMachine(flow)

# Retry messages
RETRY_MESSAGES = {
    "silence": "Sorry, I didn’t hear anything. Could you please respond?",
    "confusion": "Let me clarify the question for you.",
    "repeat": "Could you provide more details?"
}

print("\n=== AI Interview Started ===")

while not engine.is_end():

    print("DEBUG CURRENT NODE:", engine.current_node)

    question = engine.get_question()
    print("\nAI:", question)

    answer = input("User: ").strip()

    # 🔥 IMPORTANT FIX: detect empty BEFORE processing
    if answer == "":
        issue = "silence"
    else:
        issue = detect_issue(answer)

    if issue == "silence":
        print("AI:", RETRY_MESSAGES["silence"])
        engine.handle_silence()
        continue   # 🔥 prevents double-processing

    elif issue == "confusion":
        print("AI:", RETRY_MESSAGES["confusion"])
        engine.handle_confusion()

    elif issue == "repeat":
        print("AI:", RETRY_MESSAGES["repeat"])
        engine.handle_repeat()

    else:
        engine.next()



print("***********day 53**********")

from ai_core.pipeline import hiring_report_pipeline
from ai_core.report_formatter import format_recruiter_report
from ai_core.report_exporter import export_report

# sample input
sample_data = {
    "candidate_id": "C12001",
    "ats": 78,
    "screening": 72,
    "hr": 80,
    "technical": 85,
    "machine_test": 76,
    "behavior": {
        "confidence": 82,
        "risk_level": "Low Risk",
        "integrity": "Moderate Risk"
    },
    "decision": "Selected"
}

# STEP 5: run pipeline
report = hiring_report_pipeline(sample_data)

print("RAW REPORT:\n", report)



from ai_core.pipeline import hiring_report_pipeline
from ai_core.report_formatter import format_recruiter_report

report = hiring_report_pipeline(sample_data)

formatted = format_recruiter_report(report)

print("\nFORMATTED REPORT:\n")
print(formatted)



from ai_core.pipeline import hiring_report_pipeline
from ai_core.report_formatter import format_recruiter_report
from ai_core.report_exporter import export_report

report = hiring_report_pipeline(sample_data)

print(format_recruiter_report(report))

file = export_report(report)

print("\nExported to:", file)