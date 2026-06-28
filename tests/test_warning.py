
from integrity_ai.warning_system import generate_warning
events = {
    "tab_switch": 4,
    "focus_loss": 5,
    "voice_detect": 2
}

print(generate_warning(events))