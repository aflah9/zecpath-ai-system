from ai_core.pipeline import hiring_report_pipeline

def test_sample_candidate():

    sample_data = {
        "candidate_id": "C12001",
        "ats": 78,
        "screening": 72,
        "hr": 80,
        "technical": 85,
        "machine_test": 76,
        "behavior": {
            "confidence": 82,
            "risk_level": "Low Risk",
            "integrity": "Moderate Risk"
        },
        "decision": "Selected"
    }

    report = hiring_report_pipeline(sample_data)

    print(report)
    assert "candidate_id" in report