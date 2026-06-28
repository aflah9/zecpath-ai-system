from screening_ai.report_generator import generate_screening_report

# -----------------------------------
# Test Report Generator
# -----------------------------------

def test_report():

    report = generate_screening_report(

        candidate_id="C1",

        job_id="J1",

        answers=[],

        scores=[],

        behavior_reports=[]
    )

    # -----------------------------------
    # Verify report keys exist
    # -----------------------------------

    assert "candidate_id" in report

    assert "job_id" in report

    assert "final_score" in report

    assert "decision" in report

    assert "summary" in report

    assert "highlights" in report

    assert "answers" in report