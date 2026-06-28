from screening_ai.language_detector import detect_language_mix

def detect_edge_case(answer, confidence=1.0):

    if not answer or len(answer.strip()) == 0:
        return "missing"

    if confidence < 0.6:
        return "poor_audio"

    if any(word in answer.lower() for word in ["um", "uh", "hmm"]) and len(answer.split()) < 3:
        return "unclear"

    if detect_language_mix(answer):
        return "language_mix"

    if len(answer.split()) < 2:
        return "incomplete"

    return "valid"


def handle_edge_case(answer, confidence, retry_count):

    issue = detect_edge_case(answer, confidence)

    if issue == "missing":
        return "retry"

    elif issue == "poor_audio":
        return "ask_repeat_audio"

    elif issue == "unclear":
        return "simplify_question"

    elif issue == "language_mix":
        return "switch_language"

    elif issue == "incomplete":
        return "ask_detail"

    return "next"