from screening_ai.improved_intent import improved_intent_classification

def test_intent():

    text = "I worked as a developer for 2 years"

    result = improved_intent_classification(text)

    print("Detected Intent:", result)


if __name__ == "__main__":
    test_intent()