def should_trigger_followup(answer):

    if not answer:
        return True

    if len(answer.split()) < 5:
        return True

    trigger_words = [
        "not sure",
        "don't know",
        "maybe",
        "can't remember"
    ]

    answer = answer.lower()

    for word in trigger_words:
        if word in answer:
            return True

    return False


def generate_followup(question):
    return (
        f"Could you please elaborate more on: "
        f"{question}?"
    )