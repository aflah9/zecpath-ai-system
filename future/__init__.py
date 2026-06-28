from future.ai_coach import generate_feedback


def test_ai_coach():
    feedback = generate_feedback({
        "communication": 60,
        "technical": 80,
        "confidence": 50
    })

    assert len(feedback) > 0


if __name__ == "__main__":
    test_ai_coach()
    print("TEST PASSED")