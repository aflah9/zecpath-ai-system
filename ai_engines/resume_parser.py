import re

import re
from parser.section_segmenter import segment_sections


class ResumeParser:

    def __init__(self, text):
        self.text = text.lower()
        self.sections = segment_sections(text)
        print(self.sections)

    def extract_name(self):
        lines = self.text.split("\n")

        for line in lines:
            line = line.strip()

            if (
                line
                and "email" not in line
                and "phone" not in line
                and len(line.split()) in [2, 3]
            ):
                return line.title()

        return "Not Found"

    def extract_skills(self):
        skills_list = [
            "financial analysis",
            "risk assessment",
            "credit scoring models",
            "excel",
            "financial tools",
            "data analysis",
            "communication skills",
            "risk management",
            "underwriting",
            "loan servicing",
            "research",
            "python",
            "mysql",
            "hadoop"
]

        skills_text = self.sections.get("skills", "").lower()

        found = []
        for skill in skills_list:
            if skill in skills_text:
                found.append(skill)

        return found

    import re

    def extract_experience(self):
        companies = []
        designations = []

        exp_text = self.sections.get("experience", "")

        # Find company followed by a year
        company_match = re.search(
            r'([A-Za-z &]+)\s+(20\d{2})',
            exp_text
        )

        if company_match:
            companies.append(company_match.group(1).strip())

        # Find designation
        role_match = re.search(
            r'(credit analyst|data analyst|software engineer|python developer)',
            exp_text.lower()
        )

        if role_match:
            designations.append(role_match.group(1).title())

        return companies, designations

   # print(parser.sections["experience"])

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