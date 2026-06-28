import random
import json


def load_question_bank():
    with open("interview_ai/question_bank.json", "r") as f:
        return json.load(f)


def generate_questions(role_type, experience_level):
    qb = load_question_bank()

    questions = []

    # Introduction
    questions += qb["categories"]["introduction"][experience_level]

    # Common HR Categories
    categories = [
        "career_journey",
        "strengths_weaknesses",
        "teamwork",
        "career_goals",
        "availability"
    ]

    for category in categories:
        questions += qb["categories"][category]["common"]

    # Role-Based Questions
    questions += qb["role_based"][role_type]

    return random.sample(
        questions,
        min(8, len(questions))
    )