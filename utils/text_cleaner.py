import re

def clean_text(text):
    try:
        # Convert to lowercase
        text = text.lower()

        # Keep line breaks, normalize spaces within lines
        lines = text.splitlines()
        cleaned_lines = []

        for line in lines:
            line = line.strip()

            # Replace multiple spaces/tabs with a single space
            line = re.sub(r'[ \t]+', ' ', line)

            # Remove unwanted special characters but keep useful punctuation
            line = re.sub(r'[^a-z0-9.,()\-\/ ]', '', line)

            cleaned_lines.append(line)

        # Rejoin while preserving line structure
        return "\n".join(cleaned_lines).strip()

    except Exception as e:
        print(f"[Text Cleaning Error]: {e}")
        return text