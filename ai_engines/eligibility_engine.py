import json

from observability.logging import log_event
from observability.audit import audit_log


def load_rules():
    with open("config/eligibility_rules.json", "r") as f:
        return json.load(f)["Credit Analyst"]


def evaluate_candidate(candidate):

    rules = load_rules()

    missing_skills = []

    for skill in rules["mandatory_skills"]:
        if skill not in candidate["skills"]:
            missing_skills.append(skill)

    score_ok = candidate["score"] >= rules["min_score"]
    exp_ok = candidate["experience"] >= rules["min_experience"]

    # FINAL DECISION
    if score_ok and exp_ok and not missing_skills:
        status = "Eligible"

    elif score_ok:
        status = "Review"

    else:
        status = "Rejected"

    result = {
        "file": candidate["file"],
        "score": candidate["score"],
        "experience": candidate["experience"],
        "status": status,
        "missing_skills": missing_skills
    }

    # -----------------------------
    # Day 61 Observability Logging
    # -----------------------------
    log = log_event(
        service="Decision Engine",
        event_type="candidate_evaluated",
        data=result
    )

    audit = audit_log(
        action=status,
        user="Decision Engine",
        candidate_id=candidate["file"]
    )

    # (Optional) Print logs for demonstration
    print(log)
    print(audit)

    return result