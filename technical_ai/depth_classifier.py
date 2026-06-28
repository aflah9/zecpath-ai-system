def classify_answer_depth(text):

    word_count = len(text.split())

    if word_count > 20 and "because" in text.lower():
        return "deep"

    if word_count > 10:
        return "moderate"

    return "shallow"