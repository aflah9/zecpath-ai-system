def calculate_score(candidate_data, jd_skills, jd_experience=3):

    try:
        candidate_skills = set(candidate_data.get("skills", []))
        jd_skills_set = set(jd_skills)

        # 🔹 1. Skill Score (50%)
        matched = candidate_skills.intersection(jd_skills_set)
        skill_score = (len(matched) / len(jd_skills_set)) * 50 if jd_skills_set else 0

        # 🔹 2. Experience Score (30%)
        candidate_exp = candidate_data.get("experience", 0)

        if candidate_exp >= jd_experience:
            exp_score = 30
        else:
            exp_score = (candidate_exp / jd_experience) * 30

        # 🔹 3. Category Score (20%)
        categories = candidate_data.get("categories", {})
        category_count = sum(len(v) for v in categories.values())

        if category_count >= 3:
            cat_score = 20
        else:
            cat_score = (category_count / 3) * 20

        total_score = skill_score + exp_score + cat_score

        return round(total_score, 2)

    except Exception as e:
        print(f"[Scoring Error]: {e}")
        return 0