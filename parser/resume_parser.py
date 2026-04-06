class ResumeParser:
    def parse(self, resume_text):
        skills = []
        experience = []

        # Simple keyword check (example logic)
        if "Python" in resume_text:
            skills.append("Python")
        if "Machine Learning" in resume_text:
            skills.append("Machine Learning")

        if "year" in resume_text.lower():
            experience.append("Experience Found")

        return {
            "skills": skills,
            "experience": experience
        }