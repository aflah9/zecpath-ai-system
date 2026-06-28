# tests/day55_demo.py

from security.access_control import has_access
from security.audit_log import log_event
from security.encryption import encrypt_data, decrypt_data

print("===== DAY 55 DEMO =====")

print("\nAccess Control")
print(has_access("admin", "delete"))

print("\nAudit Log")

log = log_event(
    "decision_generated",
    "C15001",
    {
        "decision": "Selected",
        "score": 82
    }
)

print(log)

print("\nEncryption")

encrypted = encrypt_data("Interview Transcript")
print(encrypted)

print(decrypt_data(encrypted))