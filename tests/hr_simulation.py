import random

def simulate_candidate(candidate_type):

    base_scores = {
        "Confident": random.randint(80, 95),
        "Hesitant": random.randint(55, 70),
        "Inexperienced": random.randint(50, 65),
        "Overqualified": random.randint(75, 90)
    }

    ai_score = base_scores[candidate_type]
    human_score = ai_score + random.randint(-5, 5)

    return {
        "candidate_type": candidate_type,
        "ai_score": ai_score,
        "human_score": human_score
    }

def run_simulation():

    types = [
        "Confident",
        "Hesitant",
        "Inexperienced",
        "Overqualified"
    ]

    results = []

    for _ in range(40):
        candidate_type = random.choice(types)
        results.append(
            simulate_candidate(candidate_type)
        )

    return results

if __name__ == "__main__":
    print(run_simulation())