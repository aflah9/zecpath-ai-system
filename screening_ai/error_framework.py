ERROR_RESPONSES = {
    "missing": "I didn't receive your response. Could you answer again?",
    "poor_audio": "Your audio wasn't clear. Could you repeat?",
    "unclear": "Can you explain that more clearly?",
    "language_mix": "Would you like to continue in another language?",
    "incomplete": "Could you provide more details?",
    "fallback": "Let's move to the next question."
}


def get_error_response(issue):
    return ERROR_RESPONSES.get(issue, ERROR_RESPONSES["fallback"])