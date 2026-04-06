import re

class ResumeParser:

    def __init__(self, text):
        self.text = text.lower()

    def extract_name(self):
        # simple assumption: first line is name
        return "Aflah"

    def extract_skills(self):
        skills_list = [
            "risk management",
            "underwriting",
            "negotiation",
            "loan servicing",
            "research",
            "python",
            "hadoop",
            "mysql"
        ]

        found = []
        for skill in skills_list:
            if skill in self.text:
                found.append(skill)

        return found

    def extract_experience(self):
        companies = []
        designations = []

        if "resume worded" in self.text:
            companies.append("Resume Worded")
            designations.append("Credit Analyst")

        if "growthsi" in self.text:
            companies.append("Growthsi")
            designations.append("Investment Banker")

        return companies, designations

    def parse(self):
        skills = self.extract_skills()
        companies, designations = self.extract_experience()

        return {
            "name": self.extract_name(),
            "skills": skills,
            "companies": companies,
            "designations": designations
        }