# screening_ai/optimized_cleaner.py

import re


def advanced_clean(text):

    text = text.lower()

    text = re.sub(
        r"\b(um|uh|like|you know)\b",
        "",
        text
    )

    text = re.sub(
        r"\b(\w+)( \1\b)+",
        r"\1",
        text
    )

    text = re.sub(
        r"[^\w\s]",
        "",
        text
    )

    return re.sub(
        r"\s+",
        " ",
        text
    ).strip()