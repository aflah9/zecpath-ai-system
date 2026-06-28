"""
Example integration pipeline
"""


def parse_resume(data):

    return {
        "skills": ["Python", "SQL"]
    }


def ats_score(resume):

    return 82


def screening_ai(data):

    return 75


def interview_ai(data):

    return 88


def technical_ai(data):

    return 90


def machine_test(data):

    return 87


def decision_engine(scores):

    average = sum(scores.values()) / len(scores)

    return {
        "decision": "Selected",
        "final_score": average
    }


def full_integration_pipeline(data):

    resume = parse_resume(data)

    ats = ats_score(resume)

    screening = screening_ai(data)

    hr = interview_ai(data)

    tech = technical_ai(data)

    machine = machine_test(data)

    final = decision_engine({
        "ats": ats,
        "screening": screening,
        "hr": hr,
        "technical": tech,
        "machine": machine
    })

    return final


if __name__ == "__main__":

    result = full_integration_pipeline({})

    print(result)