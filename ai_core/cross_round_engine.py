from ai_core.refined_scoring_logic import refined_final_scoreD # day 54

EFAULT_WEIGHTS = {
    "ats": 0.20,
    "screening": 0.15,
    "hr": 0.20,
    "technical": 0.25,
    "machine_test": 0.20
}

ROLE_WEIGHTS = {
    "fresher": {
        "ats": 0.20,
        "screening": 0.20,
        "hr": 0.25,
        "technical": 0.20,
        "machine_test": 0.15
    },
    "experienced": {
        "ats": 0.25,
        "screening": 0.10,
        "hr": 0.20,
        "technical": 0.25,
        "machine_test": 0.20
    },
    "technical": {
        "ats": 0.15,
        "screening": 0.10,
        "hr": 0.15,
        "technical": 0.35,
        "machine_test": 0.25
    },
    "non_technical": {
        "ats": 0.25,
        "screening": 0.20,
        "hr": 0.35,
        "technical": 0.10,
        "machine_test": 0.10
    }
}

def get_weights(role_type=None):
    return ROLE_WEIGHTS.get(role_type, DEFAULT_WEIGHTS)



def calculate_final_score(scores, weights):
    """
    scores = {
        "ats": 75,
        "screening": 70,
        "hr": 80,
        "technical": 85,
        "machine_test": 78
    }

    weights = {
        "ats": 0.15,
        "screening": 0.10,
        "hr": 0.15,
        "technical": 0.35,
        "machine_test": 0.25
    }
    """

    final = 0

    for key in weights:
        final += scores.get(key, 0) * weights[key]

    return round(final, 2)

#######day 54#######333

def calculate_optimized_final_score(scores, role_type=None):

    weights = get_weights(role_type)

    base_score = calculate_final_score(scores, weights)

    final_score = refined_final_score(
        scores,
        base_score
    )

    return round(final_score, 2)