from ai_core.optimized_ai_engine import adjust_decision

decision = adjust_decision(
    score=82,
    technical=91,
    integrity_risk="High Risk"
)

print({
    "candidate_id": "C1001",
    "score": 82,
    "technical": 91,
    "integrity": "High Risk",
    "decision": decision
})