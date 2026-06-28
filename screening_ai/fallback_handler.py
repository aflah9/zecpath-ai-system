def fallback_strategy(issue, retry_count):

    if retry_count >= 3:
        return "skip_question"

    if issue in ["missing", "poor_audio"]:
        return "retry"

    if issue == "language_mix":
        return "switch_language"

    return "clarify"