import json
def norm(x):
    return x / 100

def load_data(file_path):
    with open(file_path, "r") as f:
        return json.load(f)


def run_demo_pipeline(candidate_id):
    ats = load_data("demo/data/ats_results.json")
    screening = load_data("demo/data/screening_outputs.json")
    interview = load_data("demo/data/interview_responses.json")
    technical = load_data("demo/data/technical_results.json")
    behavior = load_data("demo/data/behavior_signals.json")

    def find(data, key):
        return next((x for x in data if x["candidate_id"] == key), {})

    ats_data = find(ats, candidate_id)
    screening_data = find(screening, candidate_id)
    interview_data = find(interview, candidate_id)
    tech_data = find(technical, candidate_id)
    behavior_data = find(behavior, candidate_id)

    # FINAL SCORE LOGIC (simple weighted model)
    final_score = (
        ats_data.get("ats_score", 0) * 0.35 +
        screening_data.get("screening_score", 0) * 0.20 +
        interview_data.get("hr_score", 0) * 0.20 +
        tech_data.get("technical_score", 0) * 0.20 +
        tech_data.get("machine_test_score", 0) * 0.05
    )

    final_score = round(final_score , 2)

    # Decision logic
    if final_score >= 50:
        decision = "Selected"
    elif final_score >= 44:
        decision = "Hold / Review"
    else:
        decision = "Rejected"

    return {
        "candidate_id": candidate_id,
        "final_score": round(final_score, 2),
        "decision": decision,
        "behavior_risk": behavior_data.get("behavior_risk"),
        "integrity_risk": behavior_data.get("integrity_risk")
    }


if __name__ == "__main__":
    for cid in ["C001", "C002", "C003"]:
        print(run_demo_pipeline(cid))