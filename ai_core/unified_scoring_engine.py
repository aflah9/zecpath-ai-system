# ai_core/unified_scoring_engine.py

DEFAULT_WEIGHTS = {
    "ats": 0.30,
    "screening": 0.30,
    "hr": 0.40
}

ROLE_BASED_WEIGHTS = {
    "fresher": {
        "ats": 0.25,
        "screening": 0.35,
        "hr": 0.40
    },
    "experienced": {
        "ats": 0.35,
        "screening": 0.25,
        "hr": 0.40
    },
    "technical": {
        "ats": 0.40,
        "screening": 0.30,
        "hr": 0.30
    },
    "non_technical": {
        "ats": 0.20,
        "screening": 0.30,
        "hr": 0.50
    }
}


def get_weights(candidate_type=None):
    return ROLE_BASED_WEIGHTS.get(
        candidate_type,
        DEFAULT_WEIGHTS
    )


def calculate_unified_score(
    ats_score,
    screening_score,
    hr_score,
    weights
):

    final_score = (
        ats_score * weights["ats"] +
        screening_score * weights["screening"] +
        hr_score * weights["hr"]
    )

    return round(final_score, 2)