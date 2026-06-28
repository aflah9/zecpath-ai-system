from ai_core.unified_pipeline import unified_scoring_pipeline


def test_unified():

    candidates = [

        # Strong Candidate
        {
            "candidate_id": "C101",
            "ats": 88,
            "screening": 85,
            "hr": 92,
            "candidate_type": "technical"
        },

        # Average Candidate
        {
            "candidate_id": "C102",
            "ats": 65,
            "screening": 60,
            "hr": 62,
            "candidate_type": "fresher"
        },

        # Weak Candidate
        {
            "candidate_id": "C103",
            "ats": 45,
            "screening": 50,
            "hr": 42,
            "candidate_type": "non_technical"
        }

    ]

    print("\n" + "=" * 70)
    print("UNIFIED SCORING ENGINE TEST")
    print("=" * 70)

    for candidate in candidates:

        result = unified_scoring_pipeline(
            candidate_id=candidate["candidate_id"],
            ats=candidate["ats"],
            screening=candidate["screening"],
            hr=candidate["hr"],
            candidate_type=candidate["candidate_type"]
        )

        print("\nCandidate ID:", result["candidate_id"])
        print("-" * 50)
        print("Final Score :", result["final_score"])
        print("Decision    :", result["decision"])
        print("Fit         :", result["fit"]["fit_category"])
        print("Fit %       :", result["fit"]["hiring_fit_percentage"])
        print("Weights     :", result["weights_used"])

        assert result["final_score"] > 0

    print("\n" + "=" * 70)
    print("ALL TESTS PASSED")
    print("=" * 70)


if __name__ == "__main__":
    test_unified()