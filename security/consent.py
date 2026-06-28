# security/consent.py

def has_consent(candidate):
    return candidate.get("consent", False)