from interview_ai.final_hr_module import run_hr_interview


def test_final_system():

    result = run_hr_interview(
        candidate_id="C1001",

        answers=[
            {
                "question_id": "Q1",
                "relevance_score": 0.90,
                "communication_score": 82,
                "confidence_score": 78,
                "contradiction": False,
                "is_vague": False
            },
            {
                "question_id": "Q2",
                "relevance_score": 0.85,
                "communication_score": 80,
                "confidence_score": 77,
                "contradiction": False,
                "is_vague": False
            }
        ],

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

    print(result)

    assert "candidate_id" in result
    assert "final_score" in result
    assert "decision" in result
    assert "summary" in result


if __name__ == "__main__":
    test_final_system()