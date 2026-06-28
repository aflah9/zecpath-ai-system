THRESHOLDS = {
    "tab_switch": 3,
    "focus_loss": 5,
    "voice_detect": 2,
    "gaze_off": 5
}


def detect_malpractice(events):

    flags = []

    if events["tab_switch"] > THRESHOLDS["tab_switch"]:
        flags.append("High Tab Switching")

    if events["focus_loss"] > THRESHOLDS["focus_loss"]:
        flags.append("Screen Focus Loss")

    if events["voice_detect"] > THRESHOLDS["voice_detect"]:
        flags.append("Multiple Voices Detected")

    if events["gaze_off"] > THRESHOLDS["gaze_off"]:
        flags.append("Frequent Gaze Deviation")

    return flags