import fitz  # PyMuPDF
import json
import re

# Load skill dictionary
with open("data/skill_dictionary.json") as f:
    SKILL_DICT = json.load(f)


def extract_text(file_path):
    try:
        doc = fitz.open(file_path)
        text = ""

        for page in doc:
            text += page.get_text()

        return text

    except Exception as e:
        print(f"[Text Extraction Error]: {e}")
        return ""


def extract_skills(text):
    text = text.lower()

    found_skills = []
    found_categories = {}

    for category, skills in SKILL_DICT.items():
        for skill_name, synonyms in skills.items():

            for word in synonyms:
                # safer matching

                if re.search(rf'\b{word}\b', text):
                    found_skills.append(skill_name)

                    if category not in found_categories:
                        found_categories[category] = []

                    found_categories[category].append(skill_name)
                    break

    return list(set(found_skills)), found_categories


def extract_experience(text):
    try:
        matches = re.findall(r'(\d+)\+?\s*years', text.lower())
        return max(map(int, matches)) if matches else 0

    except Exception:
        return 0


def process_resume(file_path, clean_text_func):
    text = extract_text(file_path)
    clean = clean_text_func(text)

    skills, categories = extract_skills(clean)
    experience = extract_experience(clean)

    return {
        "skills": skills,
        "categories": categories,
        "experience": experience
    }