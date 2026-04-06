from utils.logger import log_info
from ai_engines.resume_text_extractor import ResumeTextExtractor


log_info("AI System Started")
print("System Running...")

# Resume Extraction Engine
extractor = ResumeTextExtractor()

import os

folder = "sample_resumes"

for file in os.listdir(folder):

    if file.endswith(".pdf") or file.endswith(".docx"):

        path = os.path.join(folder, file)

        print("\nProcessing:", file)

        cleaned_text = extractor.extract_text(path)

        output_path = f"outputs/{file}.txt"

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(cleaned_text)

        print("Saved to:", output_path)

output_path = "outputs/cleaned_resume.txt"

with open(output_path, "w", encoding="utf-8") as f:
    f.write(cleaned_text)

print("Resume processed successfully!")
print("Output saved at:", output_path)

#---------------------------#day 6 task
from ai_engines.resume_text_extractor import ResumeTextExtractor
from ai_engines.jd_parser import parse_job_description

jd_file = "sample_data/job_description.pdf"

extractor = ResumeTextExtractor()
jd_text = extractor.extract_text(jd_file)

result = parse_job_description(jd_text)

print(result)


#----day 4 code---#
from ai_engines.resume_parser import ResumeParser
from models.candidate import Candidate
from models.skill import Skill
from models.experience import Experience

print("System Running...")

# Load resume text
with open("outputs/cleaned_resume.txt", "r", encoding="utf-8") as f:
    text = f.read()

print("Resume processed successfully!")

# Parse resume
parser = ResumeParser(text)
data = parser.parse()

# Debug: see what parser returns
print("\nParsed Data:\n", data)

# Create candidate
c = Candidate(data.get("name", "Unknown"), "unknown@email.com")

# Add skills
for skill in data.get("skills", []):
    c.skills.append(Skill(skill, "technical", "intermediate"))

# Add experience (SAFE VERSION - no errors)
duration = data.get("experience") or data.get("experience_years") or "Not Found"

c.experience.append(
    Experience(
        "Unknown Company",
        data.get("role", "Unknown Role"),
        duration
    )
)

# Add education
c.education = data.get("education", "Not Found")

# Final structured output
output = {
    "name": c.name,
    "skills": [s.skill_name for s in c.skills],
    "education": c.education,
    "experience": [
        {
            "company": e.company_name,
            "role": e.designation,
            "duration": e.duration
        }
        for e in c.experience
    ]
}

print("\n✅ Structured Output:\n")
print(output)

print("\n🎉 Day 4 Completed Successfully!")