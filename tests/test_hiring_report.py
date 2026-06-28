from ai_core.hiring_report_generator import generate_hiring_report


def test_report():

    result = generate_hiring_report(
        "C1",
        70, 70, 70, 70, 70,
        {"risk_level": "Low Risk", "integrity": "Low Risk"},
        "Selected"
    )

    assert "candidate_id" in result
    print("TEST PASSED")
    print(result)


# ✅ THIS IS REQUIRED (RUN THE TEST)
if __name__ == "__main__":
    test_report()