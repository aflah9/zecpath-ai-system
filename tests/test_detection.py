from integrity_ai.detection_logic import detect_malpractice

events = {
    "tab_switch": 5,
    "focus_loss": 1,
    "voice_detect": 0,
    "gaze_off": 6
}

print(detect_malpractice(events))