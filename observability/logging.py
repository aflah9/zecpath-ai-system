from datetime import datetime

def log_event(service, event_type, data):
    return {
        "service": service,
        "event_type": event_type,
        "data": data,
        "timestamp": datetime.utcnow().isoformat()
    }
from observability.logging import log_event

log = log_event(
    service="Resume Parser",
    event_type="resume_parsed",
    data={
        "candidate": "C101",
        "status": "Success"
    }
)

print(log)