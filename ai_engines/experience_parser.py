import re
from datetime import datetime

# -----------------------------
# Credit Analyst Keywords
# -----------------------------
CREDIT_ANALYST_KEYWORDS = {
    "credit analyst", "credit risk", "risk analyst", "financial analyst",
    "loan officer", "banking", "underwriting", "credit assessment",
    "risk management", "finance", "accounting", "loan processing",
    "credit evaluation", "financial modeling"
}


# -----------------------------
# Helper: Parse date
# -----------------------------
def parse_date(date_str):
    if not date_str:
        return None

    date_str = date_str.strip()

    formats = ["%b %Y", "%B %Y", "%Y"]

    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt)
        except:
            continue

    return None


# -----------------------------
# Extract Experience Entries (FINAL FIXED)
# -----------------------------
def extract_experience(experience_text):
    experiences = []
    lines = experience_text.split("\n")

    for line in lines:
        line = line.strip()

        # -----------------------------
        # FORMAT 1:
        # Credit Analyst  ABC Bank  2022 - Present
        # -----------------------------
        match1 = re.search(
            r"([A-Za-z\s]+?)\s{2,}([A-Za-z\s]+?)\s{2,}(\d{4})\s*-\s*(Present|\d{4})",
            line
        )

        if match1:
            role = match1.group(1).strip()
            company = match1.group(2).strip()
            start = match1.group(3).strip()
            end = match1.group(4).strip()

        else:
            # -----------------------------
            # FORMAT 2:
            # Credit Analyst - ABC Bank 2022 - Present
            # -----------------------------
            match2 = re.search(
                r"(.+?)\s*-\s*(.+?)\s+(\d{4})\s*-\s*(Present|\d{4})",
                line
            )

            if match2:
                role = match2.group(1).strip()
                company = match2.group(2).strip()
                start = match2.group(3).strip()
                end = match2.group(4).strip()
            else:
                continue

        # -----------------------------
        # Convert dates
        # -----------------------------
        start_date = parse_date(start)
        end_date = datetime.now() if end.lower() == "present" else parse_date(end)

        duration = calculate_duration(start_date, end_date)

        experiences.append({
            "role": role,
            "company": company,
            "start_date": start,
            "end_date": end,
            "duration_months": duration
        })

    return experiences


# -----------------------------
# Calculate Duration
# -----------------------------
def calculate_duration(start_date, end_date):
    if not start_date or not end_date:
        return 0

    return (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)


# -----------------------------
# Total Experience
# -----------------------------
def calculate_total_experience(experiences):
    total_months = sum(exp["duration_months"] for exp in experiences)

    years = total_months // 12
    months = total_months % 12

    return f"{years} years {months} months"


# -----------------------------
# Detect Gaps
# -----------------------------
def detect_gaps(experiences):
    gaps = []

    sorted_exp = sorted(
        experiences,
        key=lambda x: parse_date(x["start_date"]) or datetime.min
    )

    for i in range(len(sorted_exp) - 1):
        current_end = parse_date(sorted_exp[i]["end_date"])
        next_start = parse_date(sorted_exp[i + 1]["start_date"])

        if current_end and next_start and next_start > current_end:
            gaps.append(f"{sorted_exp[i]['end_date']} to {sorted_exp[i+1]['start_date']}")

    return gaps


# -----------------------------
# Detect Overlaps
# -----------------------------
def detect_overlaps(experiences):
    overlaps = []

    sorted_exp = sorted(
        experiences,
        key=lambda x: parse_date(x["start_date"]) or datetime.min
    )

    for i in range(len(sorted_exp) - 1):
        current_end = parse_date(sorted_exp[i]["end_date"])
        next_start = parse_date(sorted_exp[i + 1]["start_date"])

        if current_end and next_start and next_start < current_end:
            overlaps.append(
                f"{sorted_exp[i]['role']} overlaps with {sorted_exp[i+1]['role']}"
            )

    return overlaps


# -----------------------------
# Relevance Scoring
# -----------------------------
def relevance_score(role):
    role_lower = role.lower()

    if "credit analyst" in role_lower:
        return 1.0

    score = sum(1 for keyword in CREDIT_ANALYST_KEYWORDS if keyword in role_lower)

    if score >= 2:
        return 0.9
    elif score == 1:
        return 0.7
    else:
        return 0.3


# -----------------------------
# Add Relevance Scores
# -----------------------------
def add_relevance_scores(experiences):
    for exp in experiences:
        exp["relevance_score"] = relevance_score(exp["role"])
    return experiences


# -----------------------------
# MAIN FUNCTION
# -----------------------------
def parse_experience(sections):
    experience_text = sections.get("experience", "")

    experiences = extract_experience(experience_text)
    experiences = add_relevance_scores(experiences)

    total_exp = calculate_total_experience(experiences)
    gaps = detect_gaps(experiences)
    overlaps = detect_overlaps(experiences)

    return {
        "experiences": experiences,
        "total_experience": total_exp,
        "gaps": gaps,
        "overlaps": overlaps,
        "target_role": "Credit Analyst"
    }