import re

def clean_noise(text):

    text = re.sub(r"\[.*?\]", "", text)

    text = re.sub(r"(.)\1{2,}", r"\1", text)

    return text.strip()