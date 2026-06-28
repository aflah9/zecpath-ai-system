from interview_ai.hr_scoring_engine import hr_scoring_pipeline
from interview_ai.summary_generator import generate_interview_summary
from ai_core.unified_scoring_engine import calculate_unified_score


def run_hr_interview(
    candidate_id,
    answers,
    communication,
    behavior
):
    hr_result = hr_scoring_pipeline(
    answers=answers,
    candidate_type="fresher"
)

    final_score = calculate_unified_score(
        ats_score=70,
        screening_score=75,
        hr_score=hr_result["hr_score"],
        weights={
            "ats": 0.30,
            "screening": 0.30,
            "hr": 0.40
        }
    )

    summary = generate_interview_summary(
        candidate_id,
        hr_result["details"],
        communication,
        behavior,
        answers
    )

    return {
        "candidate_id": candidate_id,
        "scores": {
            "communication": communication.get(
                "communication_score", 0
            ),
            "confidence": behavior.get(
                "confidence", {}
            ).get(
                "confidence_score", 0
            ),
            "hr": hr_result["hr_score"]
        },
        "final_score": final_score,
        "decision": summary.get(
            "decision",
            "Consider"
        ),
        "summary": summary
    }