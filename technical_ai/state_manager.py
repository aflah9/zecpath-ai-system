def create_session(candidate_id, role, exp_level):
    return {
        "candidate_id": candidate_id,
        "role": role,
        "experience_level": exp_level,
        "current_difficulty": "basic",
        "questions_asked": [],
        "scores": [],
        "status": "in_progress"
    }