import json

def export_report(report, filename="report.json"):

    export_data = {
        "candidate_id": report["candidate_id"],
        "final_score": (
            report["scores"]["ats"] +
            report["scores"]["screening"] +
            report["scores"]["hr"] +
            report["scores"]["technical"] +
            report["scores"]["machine_test"]
        ) / 5,
        "decision": report["final_recommendation"],
        "report": report
    }

    with open(filename, "w") as f:
        json.dump(export_data, f, indent=4)

    return filename