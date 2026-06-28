from ai_core.recommendation_pipeline import recommendation_pipeline


candidate_scores = {
    "technical": 88,
    "communication": 82,
    "behavior": 90,
    "integrity": 85,
    "final_score": 84
}


result = recommendation_pipeline(
    candidate_id="C10001",
    scores=candidate_scores,
    behavior_risk="Low Risk",
    integrity_risk="Moderate Risk"
)

print(result)

from ai_core.decision_engine import generate_decision


def test_decision():

    decision, score = generate_decision(85)

    assert decision == "Selected"

    print("Decision Test Passed")


test_decision()