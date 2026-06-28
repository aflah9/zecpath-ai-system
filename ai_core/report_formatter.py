def format_recruiter_report(report):

    s = report["scores"]
    b = report["behavior"]
    sumry = report["summary"]

    text = f"""
=============================
CANDIDATE HIRING REPORT
=============================

Candidate ID: {report['candidate_id']}

--- SCORE BREAKDOWN ---
ATS Score: {s['ats']}
Screening Score: {s['screening']}
HR Score: {s['hr']}
Technical Score: {s['technical']}
Machine Test Score: {s['machine_test']}

--- BEHAVIOR ---
Confidence: {b['confidence']}
Risk Level: {b['risk_level']}
Integrity: {b['integrity']}

--- STRENGTHS ---
{chr(10).join(sumry['strengths'])}

--- WEAKNESSES ---
{chr(10).join(sumry['weaknesses'])}

--- RISKS ---
{chr(10).join(sumry['risks'])}

--- FINAL DECISION ---
{report['final_recommendation']}
"""
    return text