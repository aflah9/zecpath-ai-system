import re

# -------------------------------
# Intent Keywords Mapping
# -------------------------------

INTENT_MAP = {

    "introduction": [
        "introduce",
        "about myself",
        "background"
    ],

    "experience": [
        "experience",
        "years",
        "worked",
        "analyst",
        "bank",
        "finance"
    ],

    "skills": [
        "excel",
        "financial analysis",
        "credit analysis",
        "risk assessment",
        "banking",
        "accounting",
        "loan processing",
        "communication",
        "customer handling",
        "reporting"
    ],

    "salary": [
        "salary",
        "ctc",
        "pay",
        "lpa"
    ],

    "availability": [
        "notice period",
        "available",
        "join",
        "immediately"
    ]
}

# -------------------------------
# Intent Classification
# -------------------------------

def classify_intent(text):

    text_lower = text.lower()

    for intent, keywords in INTENT_MAP.items():

        for word in keywords:

            if word in text_lower:
                return intent

    return "unknown"

# -------------------------------
# Skill Extraction
# -------------------------------

SKILL_DB = [

    "excel",

    "financial analysis",

    "credit analysis",

    "risk assessment",

    "banking",

    "accounting",

    "loan processing",

    "communication",

    "reporting",

    "customer handling"
]

def extract_skills(text):

    text = text.lower()

    return [skill for skill in SKILL_DB if skill in text]

# -------------------------------
# Experience Extraction
# -------------------------------

def extract_experience(text):

    match = re.search(r"(\d+)\s*(years|year)", text.lower())

    return int(match.group(1)) if match else 0

# -------------------------------
# Salary Extraction
# -------------------------------

def extract_salary(text):

    match = re.search(r"(\d+)\s*(lpa|lakhs|k)", text.lower())

    return match.group(0) if match else None

# -------------------------------
# Availability Detection
# -------------------------------

def extract_availability(text):

    if "immediate" in text.lower():
        return "Immediate"

    elif "notice" in text.lower():
        return "Notice Period"

    return "Unknown"

# -------------------------------
# Off-topic Detection
# -------------------------------

def is_off_topic(intent):

    return intent == "unknown"

# -------------------------------
# Vague Answer Detection
# -------------------------------

def is_vague(text):

    vague_words = ["maybe", "not sure", "don't know"]

    return any(word in text.lower() for word in vague_words)

# -------------------------------
# Missing Answer Detection
# -------------------------------

def detect_missing_answer(text):

    return not text or len(text.strip()) < 3

# -------------------------------
# Main Answer Processing
# -------------------------------

def process_answer(question_id, answer_text):

    intent = classify_intent(answer_text)

    structured = {

        "question_id": question_id,

        "original_text": answer_text,

        "intent": intent,

        "skills": extract_skills(answer_text),

        "experience_years": extract_experience(answer_text),

        "salary": extract_salary(answer_text),

        "availability": extract_availability(answer_text),

        "off_topic": is_off_topic(intent),

        "is_vague": is_vague(answer_text),

        "missing_answer": detect_missing_answer(answer_text)
    }

    return structured

# -------------------------------
# Batch Processing
# -------------------------------

def process_answers_batch(answers):

    results = []

    for ans in answers:

        result = process_answer(
            ans["question_id"],
            ans["text"]
        )

        results.append(result)

    return results