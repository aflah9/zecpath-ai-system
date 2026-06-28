from tests.candidate_profiles import CANDIDATES

for candidate in CANDIDATES:

    print("\n===================")
    print("Name:", candidate["name"])
    print("Type:", candidate["type"])

    for answer in candidate["answers"]:
        print("-", answer)


from tests.candidate_profiles import CANDIDATES

from behavior_ai.signal_mapping import calculate_behavior_score
from behavior_ai.behavioral_engine import analyze_behavior


#----------day 48------

for candidate in CANDIDATES:

    print("\n===================")
    print("Name:", candidate["name"])
    print("Type:", candidate["type"])

    for answer in candidate["answers"]:
        print("-", answer)

    # Mock behavioral signals for testing
    if candidate["type"] == "Confident":
        signals = {
            "eye_focus": 0.90,
            "head_stability": 0.85,
            "engagement": 0.90,
            "distraction": 0.10
        }

    elif candidate["type"] == "Average":
        signals = {
            "eye_focus": 0.70,
            "head_stability": 0.70,
            "engagement": 0.75,
            "distraction": 0.30
        }

    else:  # Nervous candidate
        signals = {
            "eye_focus": 0.55,
            "head_stability": 0.50,
            "engagement": 0.60,
            "distraction": 0.45
        }

    score = calculate_behavior_score(signals)
    result = analyze_behavior(signals)

    print("\nBehavior Signals:")
    print(signals)

    print("\nBehavior Score:")
    print(score)

    print("\nBehavior Analysis:")
    print(result)