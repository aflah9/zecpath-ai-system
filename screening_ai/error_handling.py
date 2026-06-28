def detect_issue(answer):

    if not answer or len(answer.strip()) == 0:
        return "silence"

    text = answer.lower()

    confusion_words = ["huh", "what", "repeat", "pardon"]

    if text.strip() in confusion_words:
        return "confusion"

    words = text.split()

    if len(words) < 2:
        return "confusion"

    # ONLY detect repeat if same word repeated consecutively
    repeated_pattern = all(words[i] == words[i-1] for i in range(1, len(words)))

    if repeated_pattern:
        return "repeat"

    return "valid"