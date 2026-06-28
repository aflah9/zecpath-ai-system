# tests/test_summary_generator.py

def test_summary():

    from interview_ai.summary_generator import (
        generate_interview_summary
    )

    result = generate_interview_summary(
        "C1",
        [],
        {"communication_score": 50},
        {
            "confidence": {
                "confidence_score": 50
            },
            "behavioral_score": 50,
            "contradiction": False
        },
        []
    )

    assert "overall_score" in result