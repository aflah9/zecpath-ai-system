import json

from interview_ai.final_hr_module import run_hr_interview


def convert_answers(raw_answers):
    """
    Convert dataset answers into HR scoring format.
    """

    converted = []

    for i, _ in enumerate(raw_answers, start=1):

        converted.append(
            {
                "question_id": f"Q{i}",
                "relevance_score": 0.85,
                "communication_score": 80,
                "confidence_score": 78,
                "contradiction": False,
                "is_vague": False
            }
        )

    return converted


with open("demo/hr_demo_dataset.json", "r") as f:
    candidates = json.load(f)

for candidate in candidates:

    result = run_hr_interview(
        candidate_id=candidate["candidate_id"],

        answers=convert_answers(
            candidate["answers"]
        ),

        communication={
            "communication_score": 82
        },

        behavior={
            "confidence": {
                "confidence_score": 78
            },
            "behavioral_score": 80,
            "contradiction": False
        }
    )

    print("\n" + "=" * 50)
    print("Candidate:", candidate["candidate_id"])
    print(result)