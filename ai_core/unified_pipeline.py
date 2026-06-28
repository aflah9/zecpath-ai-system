# ai_core/unified_pipeline.py

from ai_core.unified_scoring_engine import (
    calculate_unified_score,
    get_weights
)

from ai_core.hiring_fit import (
    calculate_hiring_fit
)


def unified_scoring_pipeline(
    candidate_id,
    ats,
    screening,
    hr,
    candidate_type="fresher"
):

    weights = get_weights(candidate_type)

    final_score = calculate_unified_score(
        ats_score=ats,
        screening_score=screening,
        hr_score=hr,
        weights=weights
    )

    fit = calculate_hiring_fit(final_score)

    decision = (
        "Hire"
        if final_score >= 75
        else "Consider"
        if final_score >= 55
        else "Reject"
    )
    explanation = {
    "ats": "Strong resume match and skill alignment",
    "screening": "Good response quality but minor gaps",
    "hr": "Strong communication and confidence"
}
    return {
    "candidate_id": candidate_id,
    "final_score": final_score,
    "decision": decision,
    "weights_used": weights,
    "fit": fit,
    "explanation": explanation
}