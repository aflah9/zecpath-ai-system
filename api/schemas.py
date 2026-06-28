"""
Day 59

API Request / Response Schemas

These schemas document how AI services communicate.
"""

resume_request = {
    "candidate_id": "C100",
    "file_url": "https://resume.pdf"
}

resume_response = {
    "candidate_id": "C100",
    "parsed_data": {
        "skills": ["Python", "SQL"],
        "experience": 5
    }
}


ats_request = {
    "candidate_profile": {},
    "job_description": {}
}

ats_response = {
    "ats_score": 82,
    "match_details": {}
}


screening_request = {
    "candidate_id": "C100",
    "answers": []
}

screening_response = {
    "screening_score": 76,
    "transcript": []
}


interview_request = {
    "session_id": "S101",
    "answers": []
}

interview_response = {
    "hr_score": 84,
    "summary": {}
}


decision_request = {
    "scores": {},
    "risk_flags": {}
}

decision_response = {
    "decision": "Selected",
    "confidence": 91
}