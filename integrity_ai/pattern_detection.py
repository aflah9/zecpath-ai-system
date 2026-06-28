def detect_patterns(events):

    patterns = []

    if events["tab_switch"] > 3:
        patterns.append(
            "Possible cheating via tab switching"
        )

    if events["voice_detect"] > 2:
        patterns.append(
            "Possible external assistance"
        )

    if (
        events["gaze_off"] > 5 and
        events.get("long_pause", False)
    ):
        patterns.append(
            "Looking at notes while answering"
        )

    if (
        events["focus_loss"] > 5 and
        events.get("response_delay", False)
    ):
        patterns.append(
            "Potential multitasking detected"
        )

    return patterns