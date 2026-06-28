# demo/run_demo.py
import sys
import os

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)


from screening_ai.report_generator import generate_screening_report

def run_demo():

    answers = [
        {
            "question_id": "Q1",
            "original_text": "I have 3 years experience in Python",
            "skills": ["Python"],
            "availability": "Immediate",
            "salary": "6 LPA",
            "is_vague": False,
            "off_topic": False
        }
    ]

    scores = [
        {
            "question_id": "Q1",
            "final_score": 85
        }
    ]

    behavior = [
        {
            "communication_strength": "Strong"
        }
    ]

    report = generate_screening_report(
        "C1001",
        "J2001",
        answers,
        scores,
        behavior
    )

    print(report)

run_demo()