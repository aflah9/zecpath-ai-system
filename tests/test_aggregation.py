def test_aggregation():

    from ai_core.cross_round_engine import calculate_final_score

    score = calculate_final_score(
        {
            "ats": 70,
            "screening": 70,
            "hr": 70,
            "technical": 70,
            "machine_test": 70
        },
        {
            "ats": 0.2,
            "screening": 0.2,
            "hr": 0.2,
            "technical": 0.2,
            "machine_test": 0.2
        }
    )

    assert score == 70

    print("Aggregation Test Passed")


if __name__ == "__main__":
    test_aggregation()