# -------------------------------
# Depth Detection
# -------------------------------

def detect_depth(text):
    keywords = [
        "because",
        "architecture",
        "optimize",
        "scalable",
        "tradeoff"
    ]

    count = sum(word in text.lower() for word in keywords)

    if count >= 3:
        return 1.0
    elif count >= 1:
        return 0.7

    return 0.4


# -------------------------------
# Logical Reasoning
# -------------------------------

def logical_score(text):
    text = text.lower()

    if "first" in text and "then" in text:
        return 1.0

    elif len(text.split()) > 10:
        return 0.7

    return 0.4


# -------------------------------
# Real World Applicability
# -------------------------------

def real_world_score(text):
    text = text.lower()

    if "production" in text or "real-world" in text:
        return 1.0

    elif "example" in text:
        return 0.7

    return 0.4


# -------------------------------
# Accuracy
# -------------------------------

def accuracy_score(is_correct):
    return 1.0 if is_correct else 0.4


# -------------------------------
# Technical Score
# -------------------------------

def calculate_technical_score(
    answer,
    is_correct=True
):
    depth = detect_depth(answer)

    logic = logical_score(answer)

    real_world = real_world_score(answer)

    accuracy = accuracy_score(is_correct)

    final = (
        accuracy * 0.35 +
        depth * 0.25 +
        logic * 0.20 +
        real_world * 0.20
    )

    return {
        "technical_score": round(final * 100, 2),
        "breakdown": {
            "accuracy": round(accuracy, 2),
            "depth": round(depth, 2),
            "logic": round(logic, 2),
            "real_world": round(real_world, 2)
        }
    }

#----------new last added line or code#####



# ADD THIS to the SAME FILE that already has:
#   detect_depth, logical_score, real_world_score, accuracy_score, calculate_technical_score
#
# Your calculate_technical_score() only scores ONE answer. This adds a
# pipeline that scores a whole list of answers and produces one aggregate
# technical_score + decision, the same way hr_scoring_pipeline() does for HR.

def technical_scoring_pipeline(answers):
    """
    answers: list of dicts like:
        {"answer_text": "...", "is_correct": True}
    """

    scored = []

    for idx, ans in enumerate(answers, start=1):
        text = ans.get("answer_text", "")
        is_correct = ans.get("is_correct", True)

        result = calculate_technical_score(text, is_correct)
        result["question_no"] = idx
        scored.append(result)

    if not scored:
        return {
            "technical_score": 0,
            "decision": "Reject",
            "details": []
        }

    avg = sum(item["technical_score"] for item in scored) / len(scored)

    decision = (
        "Strong Hire" if avg >= 75
        else "Consider" if avg >= 55
        else "Reject"
    )

    return {
        "technical_score": round(avg, 2),
        "decision": decision,
        "details": scored
    }
