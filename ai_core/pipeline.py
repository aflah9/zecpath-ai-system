from ai_core.hiring_report_generator import generate_hiring_report


def hiring_report_pipeline(data):

    report = generate_hiring_report(
        data["candidate_id"],
        data["ats"],
        data["screening"],
        data["hr"],
        data["technical"],
        data["machine_test"],
        data["behavior"],
        data["decision"]
    )

    return report