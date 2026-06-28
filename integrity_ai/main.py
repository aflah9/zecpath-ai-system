from integrity_ai.detection_logic import detect_malpractice
from integrity_ai.risk_engine import (
    calculate_integrity_score,
    risk_flagging
)
from integrity_ai.warning_system import generate_warning


def evaluate_integrity(
    candidate_id,
    events
):

    score = calculate_integrity_score(events)

    risk = risk_flagging(score)

    flags = detect_malpractice(events)

    warnings = generate_warning(events)

    return {
        "candidate_id": candidate_id,
        "integrity_score": score,
        "risk_level": risk,
        "flags": flags,
        "warnings": warnings
    }