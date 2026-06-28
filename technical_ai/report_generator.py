def generate_report(state):

    avg_score = (
        sum(state["scores"]) / len(state["scores"])
        if state["scores"]
        else 0
    )

    return {
        "candidate_id": state["candidate_id"],

        "technical_score": round(avg_score, 2),

        "decision":
            "Strong Technical Fit"
            if avg_score >= 80
            else "Consider",

        "questions_asked":
            len(state["questions_asked"]),

        "skills":
            state.get("skills", {}),

        "strengths":
            state.get("strengths", []),

        "weaknesses":
            state.get("weaknesses", []),

        "breakdown":
            state.get("breakdown", [])
    }