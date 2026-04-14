import re

# 🎯 Degree patterns (more flexible)
DEGREE_PATTERNS = [
    r"B\.?Com",
    r"M\.?Com",
    r"MBA",
    r"BBA",
    r"Bachelor of Commerce",
    r"Master of Commerce",
    r"Bachelor",
    r"Master",
    r"Finance",
    r"Accounting",
    r"Economics"
]

# 🎯 Credit Analyst certifications
CERTIFICATION_KEYWORDS = [
    "CFA",
    "FRM",
    "CPA",
    "Credit Risk",
    "Financial Modeling",
    "Banking",
    "Risk Management"
]

# 🎯 Certification categories
CERT_CATEGORIES = {
    "CFA": "Finance",
    "FRM": "Risk",
    "CPA": "Accounting",
    "Financial Modeling": "Finance",
    "Credit Risk": "Risk",
    "Banking": "Finance",
    "Risk Management": "Risk"
}


# 🔹 Extract Field of Study
def extract_field(text):
    text = text.lower()

    if "finance" in text:
        return "Finance"
    elif "commerce" in text:
        return "Commerce"
    elif "economics" in text:
        return "Economics"
    elif "accounting" in text:
        return "Accounting"

    return "General"


# 🔹 Normalize Degree Names
def normalize_degree(text):
    text = text.lower()

    if "bcom" in text or "b.com" in text:
        return "B.Com"
    elif "mcom" in text or "m.com" in text:
        return "M.Com"
    elif "mba" in text:
        return "MBA"
    elif "bba" in text:
        return "BBA"
    elif "bachelor" in text:
        return "Bachelor's Degree"
    elif "master" in text:
        return "Master's Degree"

    return text.title()


# 🔹 Parse Education Section
def parse_education(text):
    education_list = []
    lines = text.split("\n")

    for i in range(len(lines)):
        line = lines[i].strip()

        # 🔍 Detect if line contains any degree pattern
        if any(re.search(pattern, line, re.IGNORECASE) for pattern in DEGREE_PATTERNS):

            degree = normalize_degree(line)

            # 📅 Extract year (check current + next line)
            combined_text = line
            if i + 1 < len(lines):
                combined_text += " " + lines[i + 1]

            year_match = re.search(r"(20\d{2})", combined_text)
            year = year_match.group() if year_match else None

            # 🏫 Extract institution (next line cleaned)
            institution = ""
            if i + 1 < len(lines):
                institution_line = lines[i + 1]

                institution = re.sub(r"(20\d{2})", "", institution_line)
                institution = re.sub(r"[|,]", "", institution)
                institution = institution.strip()

            # 📚 Extract field
            field = extract_field(line)

            education_list.append({
                "degree": degree,
                "field": field,
                "institution": institution,
                "year": year
            })

    return education_list


# 🔹 Extract Certifications
def extract_certifications(text):
    certifications = []

    for cert in CERTIFICATION_KEYWORDS:
        if cert.lower() in text.lower():
            certifications.append({
                "name": cert,
                "category": tag_certification(cert)
            })

    return certifications


# 🔹 Tag Certification Category
def tag_certification(cert):
    return CERT_CATEGORIES.get(cert, "General")


# 🔹 Final Output Builder
def build_education_output(education, certifications):
    return {
        "education": education,
        "certifications": certifications
    }