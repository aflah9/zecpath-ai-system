import copy
import json


# ✅ 1. NORMALIZE RESUME
import copy


# ✅ 1. NORMALIZE RESUME (FIXED FOR YOUR STRUCTURE)
def normalize_resume(resume_data):
    normalized = copy.deepcopy(resume_data)

    # -----------------------------
    # ✅ Extract correct sections
    # -----------------------------
    basic_info = normalized.get("basic_info", {})
    exp_info = normalized.get("experience_analysis", {})

    # -----------------------------
    # ✅ Skills
    # -----------------------------
    skills = basic_info.get("skills", [])

    normalized["skills"] = list(set([
        s.strip().lower() for s in skills if isinstance(s, str)
    ]))

    # -----------------------------
    # ✅ Education
    # -----------------------------
    edu = basic_info.get("education", "")
    normalized["education"] = edu.lower() if isinstance(edu, str) else ""

    # -----------------------------
    # ✅ Experience
    # -----------------------------
    experiences = exp_info.get("experiences", [])

    cleaned_experience = []
    for exp in experiences:
        if isinstance(exp, dict):
            cleaned_experience.append({
                "role": exp.get("role", "").lower(),
                "company": exp.get("company", "").lower()
            })

    normalized["experience"] = cleaned_experience

    return normalized


# ✅ 2. MASK PERSONAL INFO
def mask_personal_info(resume_data):
    masked = copy.deepcopy(resume_data)

    for field in ["name", "email", "phone", "dob", "gender", "location"]:
        if field in masked:
            masked[field] = "REDACTED"

    return masked


# ✅ 3. REDUCE KEYWORD BIAS
def reduce_keyword_bias(skills):
    seen = {}
    filtered = []

    for skill in skills:
        if skill not in seen:
            seen[skill] = 1
            filtered.append(skill)
        elif seen[skill] < 2:
            seen[skill] += 1
            filtered.append(skill)

    return list(set(filtered))


# ✅ 4. BIAS CHECK
def check_bias(resume_data):
    bias_flags = {
        "keyword_bias": False,
        "experience_bias": False,
        "education_bias": False
    }

    if len(resume_data.get("skills", [])) > 15:
        bias_flags["keyword_bias"] = True

    if len(resume_data.get("experience", [])) == 0:
        bias_flags["experience_bias"] = True

    if not resume_data.get("education"):
        bias_flags["education_bias"] = True

    return bias_flags


# ✅ 5. FINAL FAIRNESS PIPELINE
def fairness_pipeline(resume_data, final_score):

    # Step 1: Normalize (FIXED)
    normalized = normalize_resume(resume_data)

    # Step 2: Reduce keyword bias
    normalized["skills"] = reduce_keyword_bias(normalized.get("skills", []))

    # Step 3: Mask personal info
    masked = mask_personal_info(normalized)

    # Step 4: Bias check
    bias_flags = check_bias(masked)

    return {
        "resume": masked,
        "final_score": final_score,
        "bias_flags": bias_flags
    }