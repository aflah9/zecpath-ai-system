from ai_core.optimized_ai_engine import adjust_decision


def test_optimization():

    decision = adjust_decision(
        score=85,
        technical=90,
        integrity_risk="High Risk"
    )

    assert decision == "Hold / Review"

    print("TEST PASSED")


if __name__ == "__main__":
    test_optimization()