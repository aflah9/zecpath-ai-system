from integrity_ai.risk_engine import (
    calculate_integrity_score,
    risk_flagging
)

events = {
    "tab_switch": 2,
    "focus_loss": 1,
    "voice_detect": 0,
    "gaze_off": 2
}

score = calculate_integrity_score(events)

print(score)
print(risk_flagging(score))