import re
from utils.text_cleaner import clean_text

SKILL_KEYWORDS = [
    "financial statement analysis",
    "risk assessment",
    "excel",
    "reporting",
    "analytical thinking",
    "ratio analysis",
    "cash flow",
    "credit appraisal",
    "collateral",
    "debt equity",
    "interest coverage",
    "dscr"
]
SKILL_SYNONYMS = {
    "dscr": "debt service coverage ratio",
    "debt-equity": "debt equity",
    "interest coverage": "interest coverage",
    "excel": "excel"
}
ROLE_KEYWORDS = [
    "credit analyst",
    "financial analyst",
    "risk analyst"
]

def extract_skills(text):
    skills = []

    for skill in SKILL_KEYWORDS:
        if skill in text:
            skills.append(skill)

    for syn in SKILL_SYNONYMS:
        if syn in text:
            skills.append(SKILL_SYNONYMS[syn])

    return list(set(skills))


def extract_role(text):
    for role in ROLE_KEYWORDS:
        if role in text:
            return role
    return "unknown"


def extract_experience_year(text):
    match = re.search(r'(\d+[-–]?\d*)\s+years', text)
    if match:
        return match.group()
    return "not specified"


def extract_education(text):
    if "mba" in text:
        return "mba finance"
    elif "ca" in text:
        return "ca inter"
    elif "cfa" in text:
        return "cfa level 1"
    return "not specified"

def extract_experience_description(text):
    keywords = [
        "analy", "evalu", "review", "prepare",
        "conduct", "monitor", "assess", "assist"
    ]

    sentences = re.split(r'[.\n•\-]', text)
    selected = []

    for sentence in sentences:
        sentence = sentence.strip()

        if len(sentence) < 25:
            continue

        for word in keywords:
            if word in sentence.lower():
                selected.append(sentence.capitalize())
                break

    return ". ".join(selected[:4]) + "."
def extract_projects(text):
    keywords = [
        "report", "analysis", "model", "dashboard",
        "prepare", "conduct", "evaluate"
    ]

    sentences = re.split(r'[.\n•\-]', text)
    selected = []

    for sentence in sentences:
        sentence = sentence.strip()

        if len(sentence) < 25:
            continue

        # Avoid "assist" to reduce overlap
        if "assist" in sentence.lower():
            continue

        for word in keywords:
            if word in sentence.lower():
                selected.append(sentence)
                break

    return ". ".join(selected[:3])

def parse_job_description(text):

    text = clean_text(text)

    job_data = {
        "role": extract_role(text),
        "skills": extract_skills(text),
        "experience_year": extract_experience_year(text),
        "education": extract_education(text),
        "experience":extract_experience_description(text),
        "projects":extract_projects(text)
    }

    return job_data

