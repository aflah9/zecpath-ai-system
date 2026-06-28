# ai_core/stable_system.py

# -------------------------------
# Safe Score Normalization
# -------------------------------

def safe_score(value):
    try:
        value = float(value)
    except:
        return 0

    return max(min(value, 100), 0)


# -------------------------------
# Stable Aggregation
# -------------------------------

def stable_aggregate(scores):

    cleaned = {
        k: safe_score(v)
        for k, v in scores.items()
    }

    avg = (
        sum(cleaned.values()) /
        len(cleaned)
        if cleaned else 0
    )

    return round(avg, 2)


# -------------------------------
# Stable Decision Logic
# -------------------------------

def stable_decision(score):

    if score >= 75:
        return "Selected"

    elif score >= 55:
        return "Hold / Review"

    return "Rejected"


# -------------------------------
# Final Stable Pipeline
# -------------------------------

def stable_pipeline(candidate_id, scores):

    final_score = stable_aggregate(scores)

    decision = stable_decision(final_score)

    return {

        "candidate_id": candidate_id,

        "final_score": final_score,

        "decision": decision,

        "status": "stable"

    }
def handle_edge_cases(answer):

    if not answer:

        return "empty"

    if len(answer.strip()) == 0:

        return "empty"

    if len(answer.split()) < 3:

        return "too_short"

    if len(answer) > 1000:

        return "too_long"

    return "valid"