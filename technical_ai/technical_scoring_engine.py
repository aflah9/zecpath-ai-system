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