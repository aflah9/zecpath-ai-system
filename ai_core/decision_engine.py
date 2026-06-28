# decision_engine/final_recommendation.py

from ai_core.optimized_ai_engine import adjust_decision
from ai_core.optimized_ai_engine import adjust_decision

from observability.logging import log_event
from observability.audit import audit_log

# -------------------------------
# Risk Weight Adjustment
# -------------------------------

def adjust_for_risk(
        score,
        behavior_risk,
        integrity_risk):
    """
    Apply penalties based on behavior
    and integrity risks.
    """

    penalty = 0

    # Behavior Risk Penalty
    if behavior_risk == "High Risk":
        penalty += 10

    elif behavior_risk == "Moderate Risk":
        penalty += 5

    # Integrity Risk Penalty
    if integrity_risk == "High Risk":
        penalty += 15

    elif integrity_risk == "Moderate Risk":
        penalty += 7

    return max(score - penalty, 0)


# -------------------------------
# Final Decision Engine
# -------------------------------

def generate_decision(
        final_score,
        technical_score,
        behavior_risk="Low Risk",
        integrity_risk="Low Risk",
        candidate_id="Unknown"):
    """
    Generate final hiring decision.

    Steps:
    1. Apply risk penalties.
    2. Apply Day 54 optimization logic.
    3. Log the AI decision.
    4. Create an audit record.
    """

    adjusted_score = adjust_for_risk(
        final_score,
        behavior_risk,
        integrity_risk
    )

    decision = adjust_decision(
        score=adjusted_score,
        technical=technical_score,
        integrity_risk=integrity_risk
    )

    # -------------------------------
    # Decision Log
    # -------------------------------
    decision_log = log_event(
        service="Decision Engine",
        event_type="decision_generated",
        data={
            "candidate_id": candidate_id,
            "final_score": final_score,
            "adjusted_score": adjusted_score,
            "technical_score": technical_score,
            "decision": decision
        }
    )

    # -------------------------------
    # Audit Log
    # -------------------------------
    audit = audit_log(
        action=decision,
        user="Decision Engine",
        candidate_id=candidate_id
    )

    return {
        "final_score": final_score,
        "adjusted_score": adjusted_score,
        "technical_score": technical_score,
        "behavior_risk": behavior_risk,
        "integrity_risk": integrity_risk,
        "decision": decision,
        "decision_log": decision_log,
        "audit_log": audit
    }


if __name__ == "__main__":

    result = generate_decision(
        candidate_id="C101",
        final_score=85,
        technical_score=90,
        behavior_risk="Low Risk",
        integrity_risk="High Risk"
    )

    print(result)