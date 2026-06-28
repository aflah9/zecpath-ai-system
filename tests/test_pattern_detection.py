from integrity_ai.pattern_detection import detect_patterns

events = {
    "tab_switch": 5,
    "focus_loss": 6,
    "voice_detect": 0,
    "gaze_off": 7,
    "long_pause": True,
    "response_delay": True
}

print(detect_patterns(events))