# ai_engines/ats_scorer.py

def skill_match_score(resume_skills, jd_skills):
    if not jd_skills:
        return 0

    matched = 0

    for jd_skill in jd_skills:
        jd_words = jd_skill.lower().split()

        for res_skill in resume_skills:
            res = res_skill.lower()

            # match ANY word
            if any(word in res for word in jd_words):
                matched += 1
                break

    return matched / len(jd_skills)

def experience_score(resume_exp, jd_role):
    resume_exp = resume_exp.lower()
    jd_role = jd_role.lower()

    score = 0

    # Role match (VERY IMPORTANT)
    if jd_role in resume_exp:
        score += 0.6

    # Domain keywords
    keywords = ["credit", "risk", "analysis", "finance"]

    keyword_match = sum(1 for word in keywords if word in resume_exp)

    score += (keyword_match / len(keywords)) * 0.4

    return min(score, 1.0)


def education_score(resume_edu, jd_required_edu):
    resume_edu = resume_edu.lower()
    jd_required_edu = jd_required_edu.lower()

    if jd_required_edu in resume_edu:
        return 1

    # fallback: general match
    if "degree" in resume_edu:
        return 0.7

    return 0.5


def semantic_score(resume_text, jd_text, nlp):
    doc1 = nlp(resume_text)
    doc2 = nlp(jd_text)
    return doc1.similarity(doc2)


# 🔹 Weight System
WEIGHTS = {
    "default": {
        "skills": 0.4,
        "experience": 0.3,
        "education": 0.1,
        "semantic": 0.2
    },
    "CREDIT_ANALYST": {
        "skills": 0.5,
        "experience": 0.2,
        "education": 0.1,
        "semantic": 0.2
    }
}


def safe_score(value):
    return value if value is not None else 0


def calculate_final_score(scores, weights):
    return (
        scores["skills"] * weights["skills"] +
        scores["experience"] * weights["experience"] +
        scores["education"] * weights["education"] +
        scores["semantic"] * weights["semantic"]
    )


def generate_explanation(scores):
    return {
        "Skill Match": f"{scores['skills']*100:.1f}%",
        "Experience Relevance": f"{scores['experience']*100:.1f}%",
        "Education Alignment": f"{scores['education']*100:.1f}%",
        "Semantic Similarity": f"{scores['semantic']*100:.1f}%"
    }


def ats_score_engine(resume_data, jd_data, nlp, role="default"):

    weights = WEIGHTS.get(role, WEIGHTS["default"])

    # Calculate scores
    skill_score = skill_match_score(resume_data["skills"], jd_data["skills"])
    exp_score = experience_score(resume_data["experience"], jd_data.get("role", ""))
    edu_score = education_score(resume_data["education"], jd_data["education"])
    sem_score = semantic_score(resume_data["text"], jd_data["text"], nlp)

    scores = {
        "skills": safe_score(skill_score),
        "experience": safe_score(exp_score),
        "education": safe_score(edu_score),
        "semantic": safe_score(sem_score)
    }

    final_score = calculate_final_score(scores, weights)
    explanation = generate_explanation(scores)

    return {
        "final_score": round(final_score * 100, 2),
        "breakdown": scores,
        "explanation": explanation
    }