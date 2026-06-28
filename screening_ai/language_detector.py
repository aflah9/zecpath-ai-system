def detect_language_mix(text):

    local_words = [
        "hai",
        "enna",
        "chetta",
        "bhai",
        "macha"
    ]

    text = text.lower()

    for word in local_words:
        if word in text:
            return True

    return False