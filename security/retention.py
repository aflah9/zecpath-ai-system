# security/retention.py

RETENTION_POLICY = {
    "resume": 90,
    "transcript": 60,
    "report": 120,
    "audit_log": 180
}
from security.retention import RETENTION_POLICY

print(RETENTION_POLICY)