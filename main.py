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
# 🔹 STEP 4: SKILL EXTRACTION ENGINE (Day 9 🔥)
# ==============================
skill_extractor = SkillExtractor()

extracted_skills = skill_extractor.extract_skills(text)

# SAVE OUTPUT (IMPORTANT)
with open("outputs/skills.json", "w") as f:
    json.dump(extracted_skills, f, indent=4)

print("\n Extracted Skills:")
print(extracted_skills)
print("\n🧠 Extracted Skills (Readable Format):\n")

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

        print(f"\n📄 Processing: {file_name}")

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

        # 🔥 DEBUG EXPERIENCE SECTION
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
        print("❌ Resume file not found")
        return {}

    basic = data.get("basic_info", {})
    exp_data = data.get("experience_analysis", {})

    # ✅ Skills
    skills = basic.get("skills", [])

    # ✅ Education
    education = basic.get("education", "")

    # ✅ Experience text
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

    print("🚀 Running ATS Scoring System...\n")

    # Load data
    resume_data = load_resume_data()
    jd_data = load_jd_data()

    # Debug prints (optional)
    print("📄 Resume Skills:", resume_data["skills"])
    print("📄 Resume Education:", resume_data["education"])
    print("📄 Resume Experience:", resume_data["experience"][:100], "...\n")

    # Run ATS scoring
    result = ats_score_engine(resume_data, jd_data, nlp,role="credit_analyst")

    # Print result
    print("===== 🎯 ATS SCORE RESULT =====")
    print(json.dumps(result, indent=4))

    # Save result
    with open("outputs/ats_score.json", "w") as f:
        json.dump(result, f, indent=4)

    print("\n✅ ATS Score saved to outputs/ats_score.json")


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
                "name": f"{basic.get('name', 'Unknown')} ({file})",  # ✅ unique name
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
        print("❌ JD file not found")
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

    print("🚀 Running ATS Ranking System...\n")

    jd_data = load_jd_data()
    all_resumes = load_all_resumes()

    if not all_resumes:
        print("❌ No resumes found")
        return

    results = []

    # 🔹 Process each candidate
    for resume in all_resumes:

        print(f"📄 Processing: {resume['name']}")

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
            "status": get_status(score),  # ✅ shortlisting
            "breakdown": result["breakdown"],
            "explanation": result["explanation"]
        })

    # 🔥 SORT (Ranking)
    ranked = sorted(results, key=lambda x: x["score"], reverse=True)

    # ==============================
    # 🔹 PRINT RANKING
    # ==============================
    print("\n🏆 CANDIDATE RANKING:\n")

    for i, candidate in enumerate(ranked, start=1):
        print(f"{i}. {candidate['name']} → {candidate['score']}% ({candidate['status']})")

    # ==============================
    # 🔹 TOP CANDIDATE
    # ==============================
    top_candidate = ranked[0]
    print(f"\n⭐ Selected Candidate: {top_candidate['name']} ({top_candidate['score']}%)")

    # ==============================
    # 🔹 SAVE OUTPUT
    # ==============================
    with open("outputs/candidate_ranking.json", "w") as f:
        json.dump(ranked, f, indent=4)

    print("\n✅ Ranking saved to outputs/candidate_ranking.json")


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


# ✅ Load NLP model
nlp = spacy.load("en_core_web_md")


# ✅ Load all resumes
def load_all_resumes(folder="outputs"):
    resumes = []

    for file in os.listdir(folder):
        # ✅ Only load resume files
        if file.endswith(".json") and "credit_analyst" in file.lower():
            file_path = os.path.join(folder, file)

            with open(file_path, "r") as f:
                data = json.load(f)

                if isinstance(data, list):
                    resumes.extend(data)
                elif isinstance(data, dict):
                    resumes.append(data)

    return resumes


# ✅ Load JD
def load_jd_data():
    path = os.path.join("outputs", "jd_output.json")
    with open(path, "r") as f:
        return json.load(f)


# ✅ MAIN
if __name__ == "__main__":

    print("*********** DAY 15 + MULTI-RESUME ***********")

    # Load data
    all_resumes = load_all_resumes()
    jd_data = load_jd_data()

    # ✅ Create JD text for semantic scoring
    role = jd_data.get("role", "")
    skills = " ".join(jd_data.get("skills", []))
    experience = jd_data.get("experience", "")
    projects = jd_data.get("projects", "")
    education = jd_data.get("education", "")

    jd_data["text"] = f"{role} {skills} {experience} {projects} {education}".strip().lower()

    results = []

    # 🔁 PROCESS EACH RESUME
    for idx, resume_data in enumerate(all_resumes, start=1):

        print(f"\n📄 Processing Resume {idx}...")

        # ✅ Normalize
        clean_resume = normalize_resume(resume_data)

        # ✅ Convert experience → text (for ATS)
        if isinstance(clean_resume.get("experience"), list):
            exp_text = ""
            for exp in clean_resume["experience"]:
                if isinstance(exp, dict):
                    exp_text += f"{exp.get('role','')} {exp.get('company','')} "
            clean_resume["experience"] = exp_text.strip().lower()

        # ✅ Create text for semantic scoring
        skills_text = " ".join(clean_resume.get("skills", []))
        exp_text = clean_resume.get("experience", "")

        clean_resume["text"] = f"{skills_text} {exp_text}".strip()

        # ✅ ATS scoring
        result = ats_score_engine(clean_resume, jd_data, nlp)
        final_score = result["final_score"]

        # ✅ Fairness
        fair_output = fairness_pipeline(resume_data, final_score)

        # ✅ Append result
        results.append(fair_output)

    # ❌ If no results
    if not results:
        print("❌ No resumes processed")
        exit()

    # ✅ SORT (Ranking)
    results.sort(key=lambda x: x["final_score"], reverse=True)

    # ✅ ADD STATUS (Shortlisting)
    for r in results:
        score = r.get("final_score", 0)

        if score >= 60:
            r["status"] = "SHORTLISTED"
        elif score >= 45:
            r["status"] = "REVIEW"
        else:
            r["status"] = "REJECTED"

    # ✅ FINAL OUTPUT
    print("\n🎯 FINAL RANKED CANDIDATES:\n")

    for i, r in enumerate(results, 1):
        print(f"Rank {i}")
        print("Score:", r.get("final_score"))
        print("Status:", r.get("status"))
        print("Skills:", r["resume"].get("skills", []))
        print("Experience:", r["resume"].get("experience", []))
        print("Education:", r["resume"].get("education", ""))
        print("-" * 40)

    # ✅ Optional: Save results
    with open("outputs/final_results.json", "w") as f:
        json.dump(results, f, indent=4)

    print("\n✅ Results saved to outputs/final_results.json")


#----------DAY 15-------------
