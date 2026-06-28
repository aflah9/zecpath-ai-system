from ai_core.decision_engine import generate_decision
from ai_core.confidence import calculate_decision_confidence
from ai_core.explanation import generate_explanation


def recommendation_pipeline(
        candidate_id,
        scores,
        behavior_risk,
        integrity_risk):

    final_score = scores.get(
        "final_score",
        0
    )

    decision, adjusted_score = generate_decision(
        final_score,
        behavior_risk,
        integrity_risk
    )

    confidence = calculate_decision_confidence(
        list(scores.values())
    )

    explanation = generate_explanation(
        scores,
        decision
    )

    return {
        "candidate_id": candidate_id,
        "final_score": final_score,
        "adjusted_score": adjusted_score,
        "decision": decision,
        "confidence_score": confidence,
        "risks": {
            "behavior": behavior_risk,
            "integrity": integrity_risk
        },
        "explanation": explanation
    }