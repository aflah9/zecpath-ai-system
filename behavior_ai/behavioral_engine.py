from behavior_ai.signal_mapping import calculate_behavior_score
from behavior_ai.risk_detection import detect_behavior_risk
from observability.logging import log_event


def analyze_behavior(signals):

    score = calculate_behavior_score(signals)

    if score >= 85:
        level = "Highly Focused"

    elif score >= 70:
        level = "Good Engagement"

    elif score >= 50:
        level = "Moderate"

    else:
        level = "Distracted"

    result = {
        "behavior_score": score,
        "behavior_level": level,
        "risk": detect_behavior_risk(score),
        "signals": signals
    }

    # Log AI behavior analysis
    log = log_event(
        service="Behavior AI",
        event_type="behavior_analysis_completed",
        data={
            "behavior_score": score,
            "behavior_level": level,
            "risk": result["risk"]
        }
    )

    # Optional: print the log for demonstration
    print(log)

    return result