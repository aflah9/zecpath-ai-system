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
print("🚀 System Running...")

# ==============================
# 🔹 STEP 1: RESUME EXTRACTION
# ==============================
extractor = ResumeTextExtractor()
folder = "sample_resumes"

files = os.listdir(folder)
print("📂 Files found:", files)

for file in files:
    print("🔍 Checking:", file)

    if file.lower().endswith((".pdf", ".docx")):

        path = os.path.join(folder, file)

        print("\n📄 Processing:", file)

        cleaned_text = extractor.extract_text(path)

        output_path = f"outputs/{file}.txt"

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(cleaned_text)

        print("✅ Saved to:", output_path)

# Save latest resume separately
with open("outputs/cleaned_resume.txt", "w", encoding="utf-8") as f:
    f.write(cleaned_text)

print("✅ Resume processed successfully!")

# ==============================
# 🔹 STEP 2: JOB DESCRIPTION PARSING (Day 6)
# ==============================
jd_file = "sample_data/job_description.pdf"

jd_text = extractor.extract_text(jd_file)
jd_result = parse_job_description(jd_text)

print("\n📌 JD Parsed Data:")
print(jd_result)

# ==============================
# 🔹 STEP 3: RESUME PARSING (Day 4)
# ==============================
with open("outputs/cleaned_resume.txt", "r", encoding="utf-8") as f:
    text = f.read()

parser = ResumeParser(text)
data = parser.parse()

print("\n📊 Parsed Resume Data:\n", data)

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

print("\n🧠 Extracted Skills:")
print(extracted_skills)

print("\n✅ Skills saved to outputs/skills.json")

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


print("\n🎯 FINAL OUTPUT:\n")
print(final_output)

print("\n🎉 Day 1–9 Completed Successfully!")