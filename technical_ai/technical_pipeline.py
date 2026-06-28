from technical_ai.technical_scoring_engine import (
    calculate_technical_score
)

from technical_ai.difficulty_engine import (
    normalize_difficulty
)


def technical_pipeline(
    answer,
    difficulty,
    is_correct=True
):

    base_score = calculate_technical_score(
        answer,
        is_correct
    )

    normalized_score = normalize_difficulty(
        base_score["technical_score"],
        difficulty
    )

    return {
        "final_score": normalized_score,
        "details": base_score
    }