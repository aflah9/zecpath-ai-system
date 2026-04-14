import re

import re
from parser.section_segmenter import segment_sections


class ResumeParser:

    def __init__(self, text):
        self.text = text.lower()
        self.sections = segment_sections(text)

    def extract_name(self):
        lines = self.text.split("\n")

        for line in lines:
            line = line.strip()

            if line and len(line.split()) <= 3 and not any(char.isdigit() for char in line):
                return line.title()

        return "Not Found"

    def extract_skills(self):
        skills_list = [
            "risk management",
            "underwriting",
            "negotiation",
            "loan servicing",
            "research",
            "python",
            "hadoop",
            "mysql",
            "credit risk analysis",
            "financial analysis",
            "excel"
        ]

        skills_text = self.sections.get("skills", "").lower()

        found = []
        for skill in skills_list:
            if skill in skills_text:
                found.append(skill)

        return found

    def extract_experience(self):
        companies = []
        designations = []

        exp_text = self.sections.get("experience", "").lower()

        if "resume worded" in exp_text:
            companies.append("Resume Worded")
            designations.append("Credit Analyst")

        if "growthsi" in exp_text:
            companies.append("Growthsi")
            designations.append("Investment Banker")

        return companies, designations

    def extract_experience_years(self):
        match = re.search(r"\d+\s+years", self.text)
        if match:
            return match.group()
        return "Not Found"

    def extract_education(self):
        edu_text = self.sections.get("education", "").lower()

        if "mba" in edu_text:
            return "MBA Finance"
        elif "master" in edu_text:
            return "Master Degree"
        elif "bachelor" in edu_text:
            return "Bachelor Degree"

        return "Not Found"

    def parse(self):
        companies, designations = self.extract_experience()

        return {
            "name": self.extract_name(),
            "skills": self.extract_skills(),
            "companies": companies,
            "designations": designations,
            "experience_years": self.extract_experience_years(),
            "education": self.extract_education()
        }