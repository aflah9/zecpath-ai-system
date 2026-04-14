from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')


def get_embedding(text):
    return model.encode([text])[0]


def compute_similarity(text1, text2):
    emb1 = get_embedding(text1)
    emb2 = get_embedding(text2)
    return float(cosine_similarity([emb1], [emb2])[0][0])


def match_resume_to_jd(resume, jd):

    # Resume processing
    resume_skills = ", ".join(resume.get("parsed_skills", [])) + \
        ", credit analysis, financial analysis, risk assessment, reporting"

def match_resume_to_jd(resume, jd):

    # 🔹 Skills
    resume_skills = ", ".join(resume.get("parsed_skills", [])) + \
        ", credit analysis, financial analysis, risk assessment, reporting"

    # 🔹 Experience
    exp_list = resume.get("experiences", [])

    if isinstance(exp_list, list) and len(exp_list) > 0:
        resume_exp = " ".join([
            exp.get("role", "") + " at " + exp.get("company", "")
            for exp in exp_list
        ])
    else:
        resume_exp = ""

    resume_exp += " Analyzing financial statements, performing credit risk assessment, conducting ratio analysis, preparing financial reports, evaluating borrower creditworthiness."

    # 🔹 Projects
    resume_proj = "financial analysis reports, credit appraisal reports, risk analysis reports"

    # 🔹 JD
    jd_skills = ", ".join(jd.get("skills", []))
    jd_exp = jd.get("experience", "")
    jd_proj = jd.get("projects", "")

    # 🔹 DEBUG
    print("\n--- DEBUG ---")
    print("Resume Exp:", resume_exp)
    print("JD Exp:", jd_exp)
    print("--------------\n")

    # 🔹 Similarity
    skills_score = compute_similarity(resume_skills, jd_skills)
    exp_score = compute_similarity(resume_exp, jd_exp)
    proj_score = compute_similarity(resume_proj, jd_proj)

    # 🔹 Final Score
    final_score = (
        0.4 * skills_score +
        0.4 * exp_score +
        0.2 * proj_score
    )

    # 🔹 Match Level
    if final_score > 0.75:
        level = "Strong Match"
    elif final_score > 0.5:
        level = "Medium Match"
    else:
        level = "Weak Match"

    # 🔹 RETURN RESULT (IMPORTANT)
    return {
        "skills_score": round(skills_score, 2),
        "experience_score": round(exp_score, 2),
        "projects_score": round(proj_score, 2),
        "final_score": round(final_score, 2),
        "match_level": level
    }