import re

# -------------------------------
# Simulated STT Integration Layer
# -------------------------------

def speech_to_text(audio_input):
    """
    Simulated STT output
    Replace with Whisper / Google STT later
    """

    return {
        "text": audio_input,
        "confidence": 0.92
    }


# -------------------------------
# Filler Word Removal
# -------------------------------

FILLER_WORDS = ["um", "uh", "like", "you know", "hmm"]

def remove_fillers(text):

    for word in FILLER_WORDS:
        text = re.sub(
            rf"\b{word}\b",
            "",
            text,
            flags=re.IGNORECASE
        )

    return text


# -------------------------------
# Punctuation Correction
# -------------------------------

def fix_punctuation(text):

    text = text.strip()

    # Capitalize first letter
    if text:
        text = text[0].upper() + text[1:]

    # Add punctuation if missing
    if not text.endswith((".", "!", "?")):
        text += "."

    return text


# -------------------------------
# Normalize Case & Spacing
# -------------------------------

def normalize_text(text):

    text = text.lower()

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    return text.strip()


# -------------------------------
# Handle Interrupted Speech
# -------------------------------

def handle_interruptions(text):

    # Remove repeated letters
    text = re.sub(r"(.)\1{2,}", r"\1", text)

    return text


# -------------------------------
# Silence Detection
# -------------------------------

def detect_silence(text):

    if not text or len(text.strip()) < 2:
        return True

    return False


# -------------------------------
# Full Transcript Cleaning Pipeline
# -------------------------------

def clean_transcript(audio_input):

    stt_result = speech_to_text(audio_input)

    raw_text = stt_result["text"]

    confidence = stt_result["confidence"]

    # Silence check
    if detect_silence(raw_text):

        return {
            "clean_text": "",
            "confidence": confidence,
            "status": "silence_detected"
        }

    # Cleaning steps
    text = remove_fillers(raw_text)

    text = handle_interruptions(text)

    text = normalize_text(text)

    text = fix_punctuation(text)

    return {
        "clean_text": text,
        "confidence": confidence,
        "status": "processed"
    }