# tests/test_hr_scoring.py

from interview_ai.hr_scoring_engine import (
    hr_scoring_pipeline
)


def test_hr_score():

    answers = [

        {
            "question_id": "Q1",
            "relevance_score": 0.9,
            "communication_score": 85,
            "confidence_score": 80,
            "contradiction": False,
            "is_vague": False
        }

    ]

    result = hr_scoring_pipeline(
        answers,
        "experienced"
    )

    print(result)


if __name__ == "__main__":
    test_hr_score()