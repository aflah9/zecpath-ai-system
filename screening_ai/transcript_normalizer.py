import re

def normalize_transcript(text):

    # Convert to lowercase
    text = text.lower()

    # Remove filler words
    fillers = ["um", "uh", "like", "you know"]

    for f in fillers:
        text = re.sub(rf"\b{f}\b", "", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    return text.strip()