def adjust_difficulty(current_level, answer_quality):

    levels = ["basic", "intermediate", "advanced"]

    idx = levels.index(current_level)

    if answer_quality == "good" and idx < 2:
        return levels[idx + 1]

    if answer_quality == "poor" and idx > 0:
        return levels[idx - 1]

    return current_level

def normalize_difficulty(
    score,
    difficulty
):
    multipliers = {
        "basic": 1.0,
        "intermediate": 1.1,
        "advanced": 1.2
    }

    adjusted = score * multipliers.get(
        difficulty,
        1.0
    )

    return min(
        round(adjusted, 2),
        100
    )