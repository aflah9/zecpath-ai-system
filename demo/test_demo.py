from demo.full_pipeline_simulation import run_demo_pipeline

def test_demo():
    result = run_demo_pipeline("C001")

    assert "candidate_id" in result
    assert "final_score" in result
    assert result["decision"] in ["Selected", "Hold / Review", "Rejected"]

    print("TEST PASSED")


if __name__ == "__main__":
    test_demo()