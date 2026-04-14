import os
import fitz  # PyMuPDF
import json

from ai_engines.education_parser import (
    parse_education,
    extract_certifications,
    build_education_output
)

# 📁 Folder path
RESUME_FOLDER = "sample_resumes"


# 🔹 Extract text from PDF
def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""

    for page in doc:
        text += page.get_text()

    return text


def main():
    all_outputs = []

    for file in os.listdir(RESUME_FOLDER):
        if file.endswith(".pdf"):
            path = os.path.join(RESUME_FOLDER, file)

            print(f"Processing: {file}")

            text = extract_text_from_pdf(path)

            education = parse_education(text)
            certifications = extract_certifications(text)

            output = build_education_output(education, certifications)

            all_outputs.append({
                "file": file,
                "data": output
            })

    # Save output
    with open("outputs/education_output.json", "w") as f:
        json.dump(all_outputs, f, indent=4)

    print("✅ Output saved to outputs/education_output.json")


if __name__ == "__main__":
    main()