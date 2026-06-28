# -------------------------------
# Scoring Weights
# -------------------------------

WEIGHTS = {
    "clarity": 0.25,
    "relevance": 0.30,
    "completeness": 0.25,
    "consistency": 0.20
}

# -------------------------------
# Clarity Score
# -------------------------------

def score_clarity(answer):

    text = answer.get("original_text", "")
    length = len(text.split())

    if length > 8:
        return 1.0
    elif length > 4:
        return 0.7
    elif length > 1:
        return 0.4

    return 0.0


# -------------------------------
# Relevance Score
# -------------------------------

def score_relevance(answer, expected_intent):

    return 1.0 if answer.get("intent") == expected_intent else 0.3


# -------------------------------
# Completeness Score
# -------------------------------

def score_completeness(answer):

    score = 0

    if answer.get("skills"):
        score += 0.4

    if answer.get("experience_years") > 0:
        score += 0.3

    if answer.get("availability") != "Unknown":
        score += 0.3

    return min(score, 1.0)


# -------------------------------
# Consistency Score
# -------------------------------

def score_consistency(answer):

    if answer.get("is_vague"):
        return 0.3

    if answer.get("off_topic"):
        return 0.2

    return 1.0


# -------------------------------
# Per Question Score
# -------------------------------

def score_answer(answer, expected_intent):

    clarity = score_clarity(answer)

    relevance = score_relevance(answer, expected_intent)

    completeness = score_completeness(answer)

    consistency = score_consistency(answer)

    final = (
        clarity * WEIGHTS["clarity"] +
        relevance * WEIGHTS["relevance"] +
        completeness * WEIGHTS["completeness"] +
        consistency * WEIGHTS["consistency"]
    )

    return {
        "question_id": answer["question_id"],
        "scores": {
            "clarity": round(clarity, 2),
            "relevance": round(relevance, 2),
            "completeness": round(completeness, 2),
            "consistency": round(consistency, 2)
        },
        "final_score": round(final * 100, 2)
    }

def generate_explanation(answer):

    return {

        "question_id": answer["question_id"],

        "explanation": {

            "clarity":
                "Answer is detailed and well-structured"
                if len(answer.get("original_text", "").split()) > 5
                else "Answer is too short",

            "relevance":
                "Matches expected intent"
                if not answer.get("off_topic")
                else "Answer appears off-topic",

            "completeness":
                "Includes skills and experience"
                if answer.get("skills")
                and answer.get("experience_years") > 0
                else "Missing important details",

            "consistency":
                "No vague or off-topic indicators"
                if not answer.get("is_vague")
                else "Answer appears vague"
        }
    }


# -------------------------------
# Aggregate Screening Score
# -------------------------------

def aggregate_scores(scored_answers):

    if not scored_answers:
        return 0

    total = sum(a["final_score"] for a in scored_answers)

    avg = total / len(scored_answers)

    return round(avg, 2)


# -------------------------------
# Score Normalization
# -------------------------------

def normalize_score(score, max_score=100):

    return round((score / max_score) * 100, 2)


# -------------------------------
# Screening Pipeline Function
# -------------------------------

def screening_scoring_pipeline(
    candidate_id,
    answers,
    intent_map
):

    scored_answers = []

    total_clarity = 0
    total_relevance = 0
    total_completeness = 0
    total_consistency = 0

    for ans in answers:

        expected_intent = intent_map.get(
            ans["question_id"],
            "unknown"
        )

        scored = score_answer(ans, expected_intent)

        scored_answers.append(scored)

        total_clarity += scored["scores"]["clarity"]
        total_relevance += scored["scores"]["relevance"]
        total_completeness += scored["scores"]["completeness"]
        total_consistency += scored["scores"]["consistency"]

    final_score = aggregate_scores(scored_answers)

    decision = (
        "Pass" if final_score >= 70
        else "Review" if final_score >= 50
        else "Reject"
    )

    count = len(scored_answers)

    return {

        "candidate_id": candidate_id,

        "screening_score": final_score,

        "decision": decision,

        "breakdown": [
            {
                "question_id": s["question_id"],
                "final_score": s["final_score"]
            }
            for s in scored_answers
        ],

        "summary": {

            "avg_clarity": round(total_clarity / count, 2),

            "avg_relevance": round(total_relevance / count, 2),

            "avg_completeness": round(total_completeness / count, 2),

            "avg_consistency": round(total_consistency / count, 2)
        },

        "details": scored_answers
    }

####--------day 30-----------
DECISION_THRESHOLDS = {
    "pass": 65,
    "review": 45
}

def get_decision(score):

    if score >= DECISION_THRESHOLDS["pass"]:
        return "Pass"

    elif score >= DECISION_THRESHOLDS["review"]:
        return "Review"

    return "Reject"


def screening_scoring_pipeline(sample_answers, intent_map):

    total_score = 0

    for answer in sample_answers:

        score = 50

        # Intent match bonus
        if answer["intent"] == intent_map.get(answer["question_id"]):
            score += 20

        # Experience bonus
        if answer.get("experience_years", 0) > 0:
            score += 10

        # Clarity bonus
        if not answer.get("is_vague"):
            score += 10

        # Off-topic penalty
        if answer.get("off_topic"):
            score -= 20

        total_score += score

    final_score = total_score / len(sample_answers)

    decision = get_decision(final_score)

    return {
        "final_score": final_score,
        "decision": decision
    }