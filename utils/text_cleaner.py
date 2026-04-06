import re

def clean_text(text):
    # remove extra spaces BUT keep line breaks
    text = re.sub(r'[ \t]+', ' ', text)

    # remove unwanted characters (optional)
    text = re.sub(r'[^a-zA-Z0-9\n.,\- ]', '', text)

    # normalize multiple line breaks
    text = re.sub(r'\n+', '\n', text)

    return text.strip()
