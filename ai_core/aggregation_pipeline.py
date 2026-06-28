from ai_core.cross_round_engine import (
    calculate_final_score,
    get_weights
)

from ai_core.hiring_fit_calculator import (
    calculate_hiring_fit
)

from ai_core.normalizer import (
    normalize_scores
)

from ai_core.explanations import (
    generate_explanation
)


def aggregation_pipeline(
    candidate_id,
    scores,
    role_type="technical"
):

    normalized_scores = normalize_scores(scores)

    weights = get_weights(role_type)

    final_score = calculate_final_score(
        normalized_scores,
        weights
    )

    hiring_fit = calculate_hiring_fit(
        final_score
    )

    explanation = generate_explanation()

    decision = (
        "Hire"
        if final_score >= 75
        else "Consider"
        if final_score >= 55
        else "Reject"
    )

    candidate_object = {

        "candidate_id": candidate_id,

        "scores": normalized_scores,

        "weights": weights,

        "final_score": final_score,

        "decision": decision,

        "hiring_fit": hiring_fit,

        "explanation": explanation
    }

    return candidate_object
