from ai_engines.resume_parser import ResumeParser

with open("outputs/cleaned_resume.txt", "r", encoding="utf-8") as f:
    text = f.read()

parser = ResumeParser(text)

print("\n===== DETECTED SECTIONS =====")
print(parser.sections)

print("\n===== PARSED DATA =====")
print(parser.parse())