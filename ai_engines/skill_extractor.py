import json
import re

class SkillExtractor:
    def __init__(self, dictionary_path="data/skill_dictionary.json"):
        with open(dictionary_path, "r") as f:
            self.skills_db = json.load(f)

        self.skill_section_headers = [
            "skills", "technical skills", "key skills",
            "core skills", "key competencies",
            "technical competencies", "tools", "tools technologies"
        ]

    def normalize_text(self, text):
        return text.lower()

    # 🔹 Extract only SKILLS section
    def extract_skill_section(self, text):
        text = text.lower()

        for header in self.skill_section_headers:
            if header in text:
                parts = text.split(header)
                if len(parts) > 1:
                    return parts[1][:1000]  # take next portion
        return text  # fallback

    def extract_skills(self, text):
        text = self.normalize_text(text)

        # ✅ Focus on skills section
        skill_text = self.extract_skill_section(text)

        extracted = {}

        for category, skills in self.skills_db.items():
            for skill, variants in skills.items():
                for variant in variants:
                    if re.search(r"\b" + re.escape(variant) + r"\b", skill_text):
                        extracted[skill] = {
                            "category": category,
                            "confidence": self.calculate_confidence(variant, skill_text)
                        }

        return self.deduplicate(extracted)

    def calculate_confidence(self, skill, text):
        count = len(re.findall(skill, text))

        if count > 2:
            return 0.9
        elif count > 1:
            return 0.7
        else:
            return 0.6

    def deduplicate(self, skills):
        return dict(sorted(skills.items()))