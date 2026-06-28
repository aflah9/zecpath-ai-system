from interview_ai.followup_engine import (
    detect_answer_quality,
    generate_followup
)

from interview_ai.adaptive_engine import (
    adapt_question_level,
    generate_adaptive_question
)


def followup_pipeline(
    question,
    answer,
    confidence_score
):

    quality = detect_answer_quality(answer)

    followup = generate_followup(
        question,
        quality
    )

    mode = adapt_question_level(
        quality,
        confidence_score
    )

    adaptive_question = generate_adaptive_question(
        question,
        mode
    )

    return {
        "quality": quality,
        "followup": followup,
        "next_question": adaptive_question
    }