# tests/test_full_interview.py

from tests.candidate_profiles import CANDIDATES

from interview_ai.communication_engine import (
    calculate_communication_score
)

from interview_ai.behavior_analyzer import (
    analyze_behavior
)

from interview_ai.hr_scoring_engine import (
    hr_scoring_pipeline
)

from interview_ai.summary_generator import (
    generate_interview_summary
)


def test_full_interview():

    for idx, candidate in enumerate(CANDIDATES, start=1):

        candidate_id = f"C{idx:03d}"

        answers = candidate["answers"]

        combined_text = " ".join(answers)

        print("\n" + "=" * 70)
        print(f"Candidate ID: {candidate_id}")
        print(f"Name: {candidate['name']}")
        print(f"Type: {candidate['type']}")

        # -------------------------
        # Communication Analysis
        # -------------------------

        communication = calculate_communication_score(
            combined_text
        )

        print("\n=== COMMUNICATION ===")
        print(communication)

        # -------------------------
        # Behavior Analysis
        # -------------------------

        behavior = analyze_behavior(
            combined_text,
            duration=10
        )

        print("\n=== BEHAVIOR ===")
        print(behavior)

        # -------------------------
        # HR Scoring
        # -------------------------

        hr_answers = [

            {
                "question_id": "Q1",
                "relevance_score": 0.9,
                "communication_score":
                    communication["communication_score"],
                "confidence_score":
                    behavior["confidence"]["confidence_score"],
                "contradiction": False,
                "is_vague": False
            }

        ]

        # Candidate experience level
        if candidate["type"] == "Inexperienced":
            experience_level = "fresher"
        else:
            experience_level = "experienced"

        hr_result = hr_scoring_pipeline(
            hr_answers,
            experience_level
        )

        print("\n=== HR SCORE ===")
        print(hr_result)

        # -------------------------
        # Summary Generation
        # -------------------------

        summary = generate_interview_summary(
            candidate_id=candidate_id,
            hr_scores=[
                {
                    "question_id": "Q1",
                    "final_score": hr_result["hr_score"]
                }
            ],
            communication=communication,
            behavior=behavior,
            answers=answers
        )

        print("\n=== FINAL SUMMARY ===")
        print(summary)

        print("\n=== FINAL DECISION ===")
        print(
            f"Candidate: {candidate['name']} | "
            f"Type: {candidate['type']} | "
            f"Overall Score: {summary['overall_score']} | "
            f"Decision: {summary['decision']}"
        )


if __name__ == "__main__":
    test_full_interview()