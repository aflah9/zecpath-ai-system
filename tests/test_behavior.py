from tests.candidate_profiles import CANDIDATES

from behavior_ai.signal_mapping import calculate_behavior_score
from behavior_ai.behavioral_engine import analyze_behavior

print("=== BEHAVIOR AI TEST ===")

for candidate in CANDIDATES:

    print("\n===================")
    print("Name:", candidate["name"])
    print("Type:", candidate["type"])

    # Mock signals based on candidate type
    if candidate["type"] == "Confident":

        signals = {
            "eye_focus": 0.90,
            "head_stability": 0.85,
            "engagement": 0.90,
            "distraction": 0.10
        }

    elif candidate["type"] == "Average":

        signals = {
            "eye_focus": 0.75,
            "head_stability": 0.70,
            "engagement": 0.75,
            "distraction": 0.25
        }

    elif candidate["type"] == "Nervous":

        signals = {
            "eye_focus": 0.55,
            "head_stability": 0.50,
            "engagement": 0.60,
            "distraction": 0.45
        }

    else:

        signals = {
            "eye_focus": 0.65,
            "head_stability": 0.60,
            "engagement": 0.65,
            "distraction": 0.35
        }

    score = calculate_behavior_score(signals)

    result = analyze_behavior(signals)

    print("\nSignals:")
    print(signals)

    print("\nBehavior Score:")
    print(score)

    print("\nAnalysis:")
    print(result)