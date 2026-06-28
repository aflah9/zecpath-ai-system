# interview_ai/hr_scoring_engine.py

from interview_ai.hr_weights import get_weights
from nlp.intent_refinement import refined_intent_detection

# -------------------------------
# Default Weight Configuration
# -------------------------------

DEFAULT_WEIGHTS = {
    "relevance": 0.30,
    "communication": 0.25,
    "confidence": 0.25,
    "consistency": 0.20
}


# -------------------------------
# Consistency Score
# -------------------------------

def score_consistency(answer):
    """
    Calculate consistency score based on answer quality.
    """

    if answer.get("contradiction"):
        return 0.3

    if answer.get("is_vague"):
        return 0.6

    return 1.0


# -------------------------------
# Per-Answer Scoring
# -------------------------------

def score_hr_answer(answer, weights=DEFAULT_WEIGHTS):
    """
    Score a single HR interview answer.
    """

    relevance = answer.get(
        "relevance_score",
        0.7
    )

    communication = (
        answer.get(
            "communication_score",
            70
        ) / 100
    )

    confidence = (
        answer.get(
            "confidence_score",
            70
        ) / 100
    )

    consistency = score_consistency(answer)

    # -------------------------------
    # Day 54 Intent Detection
    # -------------------------------

    answer_text = answer.get(
        "answer_text",
        ""
    )

    intent = refined_intent_detection(
        answer_text
    )

    final = (
        relevance * weights["relevance"] +
        communication * weights["communication"] +
        confidence * weights["confidence"] +
        consistency * weights["consistency"]
    )

    return {
        "question_id": answer["question_id"],

        "intent": intent,

        "scores": {
            "relevance": round(relevance, 2),
            "communication": round(communication, 2),
            "confidence": round(confidence, 2),
            "consistency": round(consistency, 2)
        },

        "final_score": round(
            final * 100,
            2
        )
    }


# -------------------------------
# Aggregate HR Interview Score
# -------------------------------

def aggregate_hr_scores(scored_answers):
    """
    Calculate average HR interview score.
    """

    if not scored_answers:
        return 0

    total = sum(
        answer["final_score"]
        for answer in scored_answers
    )

    avg = total / len(scored_answers)

    return round(avg, 2)


# -------------------------------
# Normalize Interview Score
# -------------------------------

def normalize_interview_score(
    score,
    total_questions
):
    """
    Normalize score across interview lengths.
    """

    if total_questions == 0:
        return 0

    normalized = score / total_questions

    return round(
        normalized,
        2
    )


# -------------------------------
# Generate Summary Statistics
# -------------------------------

def generate_summary(scored_answers):
    """
    Generate average parameter scores.
    """

    if not scored_answers:
        return {
            "avg_relevance": 0,
            "avg_communication": 0,
            "avg_confidence": 0,
            "avg_consistency": 0
        }

    count = len(scored_answers)

    avg_relevance = (
        sum(
            a["scores"]["relevance"]
            for a in scored_answers
        ) / count
    )

    avg_communication = (
        sum(
            a["scores"]["communication"]
            for a in scored_answers
        ) / count
    )

    avg_confidence = (
        sum(
            a["scores"]["confidence"]
            for a in scored_answers
        ) / count
    )

    avg_consistency = (
        sum(
            a["scores"]["consistency"]
            for a in scored_answers
        ) / count
    )

    return {
        "avg_relevance": round(
            avg_relevance,
            2
        ),
        "avg_communication": round(
            avg_communication,
            2
        ),
        "avg_confidence": round(
            avg_confidence,
            2
        ),
        "avg_consistency": round(
            avg_consistency,
            2
        )
    }


# -------------------------------
# HR Scoring Pipeline
# -------------------------------

def hr_scoring_pipeline(
    answers,
    candidate_type="fresher"
):
    """
    Complete HR interview scoring pipeline.
    """

    weights = get_weights(
        candidate_type
    )

    scored = []

    for answer in answers:

        result = score_hr_answer(
            answer,
            weights
        )

        scored.append(
            result
        )

    final_score = aggregate_hr_scores(
        scored
    )

    decision = (
        "Strong Hire"
        if final_score >= 75
        else "Consider"
        if final_score >= 55
        else "Reject"
    )

    return {
        "hr_score": final_score,
        "decision": decision,
        "details": scored,
        "summary": generate_summary(
            scored
        )
    }


# -------------------------------
# Example Execution
# -------------------------------

if __name__ == "__main__":

    answers = [
        {
            "question_id": "Q1",
            "answer_text":
            "I developed a CRM application for our sales team.",

            "relevance_score": 0.9,
            "communication_score": 85,
            "confidence_score": 80,
            "contradiction": False,
            "is_vague": False
        },
        {
            "question_id": "Q2",
            "answer_text":
            "I studied machine learning through online courses.",

            "relevance_score": 0.8,
            "communication_score": 78,
            "confidence_score": 75,
            "contradiction": False,
            "is_vague": True
        }
    ]

    result = hr_scoring_pipeline(
        answers,
        "experienced"
    )

    print(result)