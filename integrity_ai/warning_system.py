def generate_warning(events):

    warnings = []

    if events.get("tab_switch", 0) > 2:
        warnings.append(
            "Please stay on the interview screen"
        )

    if events.get("voice_detect", 0) > 1:
        warnings.append(
            "External voice detected. Please ensure you are alone"
        )

    if events.get("focus_loss", 0) > 3:
        warnings.append(
            "You seem distracted. Please focus on the interview"
        )

    return warnings