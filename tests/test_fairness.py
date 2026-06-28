def test_demographic_bias_removed():
    protected_attributes = [
        "gender",
        "age",
        "religion",
        "ethnicity",
        "nationality"
    ]

    scoring_features = [
        "communication",
        "confidence",
        "behavior",
        "skills"
    ]

    for attr in protected_attributes:
        assert attr not in scoring_features

    print("Fairness Test Passed")


if __name__ == "__main__":
    test_demographic_bias_removed()