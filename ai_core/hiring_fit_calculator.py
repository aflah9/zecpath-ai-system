def calculate_hiring_fit(score):

    if score >= 85:
        category = "Excellent Fit"

    elif score >= 70:
        category = "Strong Fit"

    elif score >= 55:
        category = "Moderate Fit"

    else:
        category = "Low Fit"

    return {
        "hiring_fit_percentage": score,
        "fit_category": category
    }
def generate_explanation():

    return {

        "ats":
        "Good resume-job match",

        "screening":
        "Clear responses with minor gaps",

        "hr":
        "Strong communication and confidence",

        "technical":
        "High technical depth",

        "machine_test":
        "Good practical coding performance"
    }


