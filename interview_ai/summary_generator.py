# interview_ai/summary_generator.py


def generate_natural_summary(
    strengths,
    weaknesses,
    risks,
    culture_fit,
    decision
):
    """
    Generate recruiter-friendly natural language summary.
    """

    strengths_text = (
        ", ".join(strengths[:2])
        if strengths
        else "some strengths"
    )

    weaknesses_text = (
        ", ".join(weaknesses[:2])
        if weaknesses
        else "minor weaknesses"
    )

    risks_text = (
        ", ".join(risks)
        if risks
        else "no major risks"
    )

    return f"""
The candidate demonstrates {strengths_text}.

However, there are concerns such as {weaknesses_text}.

Risk factors include {risks_text}.

Cultural fit is assessed as {culture_fit}.

Final Recommendation: {decision}.
""".strip()


def generate_interview_summary(
    candidate_id,
    hr_scores,
    communication,
    behavior,
    answers
):
    """
    Generate complete interview summary report.
    """

    strengths = []
    weaknesses = []
    risks = []
    inconsistencies = []

    # ---------------------------------
    # Analyze HR Scores
    # ---------------------------------

    for item in hr_scores:

        if item["final_score"] >= 80:
            strengths.append(
                f"Strong performance in {item['question_id']}"
            )

        elif item["final_score"] < 50:
            weaknesses.append(
                f"Weak response in {item['question_id']}"
            )

    # ---------------------------------
    # Communication Analysis
    # ---------------------------------

    communication_score = communication.get(
        "communication_score",
        0
    )

    if communication_score >= 80:
        strengths.append(
            "Excellent communication skills"
        )

    elif communication_score < 50:
        weaknesses.append(
            "Poor communication clarity"
        )

    # ---------------------------------
    # Behavior Analysis
    # ---------------------------------

    confidence_score = behavior.get(
        "confidence",
        {}
    ).get(
        "confidence_score",
        0
    )

    if confidence_score < 60:
        risks.append(
            "Low confidence detected"
        )

    if behavior.get("contradiction", False):
        inconsistencies.append(
            "Contradictory statements observed"
        )

    # ---------------------------------
    # Cultural Fit Indicators
    # ---------------------------------

    culture_fit = "Good"

    answers_text = " ".join(
        [str(answer) for answer in answers]
    ).lower()

    if "team" in answers_text:
        strengths.append(
            "Shows teamwork orientation"
        )
    else:
        culture_fit = "Moderate"

    # ---------------------------------
    # Calculate Average HR Score
    # ---------------------------------

    if len(hr_scores) > 0:
        avg_hr_score = (
            sum(
                item["final_score"]
                for item in hr_scores
            )
            / len(hr_scores)
        )
    else:
        avg_hr_score = 0

    # ---------------------------------
    # Overall Score Calculation
    # ---------------------------------

    overall_score = (
        communication_score * 0.3
        + behavior.get("behavioral_score", 0) * 0.3
        + avg_hr_score * 0.4
    )

    overall_score = round(
        overall_score,
        2
    )

    # ---------------------------------
    # Hiring Decision
    # ---------------------------------

    if overall_score >= 75:
        decision = "Strong Hire"

    elif overall_score >= 55:
        decision = "Consider"

    else:
        decision = "Reject"

    # ---------------------------------
    # Final Report
    # ---------------------------------

    report = {
        "candidate_id": candidate_id,
        "overall_score": overall_score,
        "decision": decision,
        "summary": {
            "strengths": strengths,
            "weaknesses": weaknesses,
            "risks": risks,
            "inconsistencies": inconsistencies,
            "cultural_fit": culture_fit
        },
        "natural_language_summary":
        generate_natural_summary(
            strengths,
            weaknesses,
            risks,
            culture_fit,
            decision
        )
    }

    return report