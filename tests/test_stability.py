# tests/test_stability.py

from interview_ai.stable_hr_ai import (
    stable_hr_evaluation
)

from interview_ai.refined_scoring import (
    refined_score_pipeline
)

from interview_ai.followup_stability import (
    stable_followup
)

from screening_ai.optimized_cleaner import (
    advanced_clean
)


def test_stability():

    result = stable_hr_evaluation(
        [50, 60, 90, 30]
    )

    print(result)

    scores = refined_score_pipeline(
        [50, 60, 90, 30],
        [80, 75, 90, 70]
    )

    print(scores)

    print(
        stable_followup(
            "too_short",
            1
        )
    )

    print(
        advanced_clean(
            "Um um I like like coding!!!"
        )
    )

    assert result["stable_score"] > 0


if __name__ == "__main__":
    test_stability()