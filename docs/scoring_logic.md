The ATS scoring engine evaluates how well a candidate’s resume matches a given job description using NLP and rule-based scoring.

The total score is calculated out of 100 points.

-Scoring Breakdown
 Total Score = 100

 Skills Match        → 40%
 Experience Match    → 20%
 Education Match     → 10%
 Keyword Matching    → 20%
 Projects/Relevance  → 10%

 1. Skills Matching (40%)


it works;

-Extract skills from resume using SpaCy NLP
-Extract required skills from Job Description
-Compare both lists

logic:


Skill Match % = (Matched Skills / Required Skills) × 100


scoring:

-≥ 80% match → Full score (40)
-50%–79% → Medium score (20–30)
-< 50% → Low score (0–15)


2. Experience Matching (20%)

it works:

-Extract years of experience from resume
-Compare with required experience in JD

logic;

-If experience ≥ required → Full score
-If slightly less → Partial score
-If no experience → Low score

3. Education Matching (10%)

it works;

-Extract degree (B.Tech, MBA, etc.)
-Match with JD requirements

scoring:

Exact match → 10
Related field → 5–8
No match → 0–3

4. Keyword Matching (20%)

it works:

-Use NLP to extract important keywords from JD
-Check frequency in resume

logic;
Keyword Score = (Matched Keywords / Total Keywords) × 20


5. Projects / Relevance (10%)

it works:


-Check if resume includes relevant projects
-Match project keywords with JD domain


scoring:
Highly relevant projects → 10
Some relevance → 5–8
No relevant projects → 0–3


Final Score Calculation:

Final Score =
Skills Score +
Experience Score +
Education Score +
Keyword Score +
Project Score


# NLP Usage (Important)

The system uses SpaCy (en_core_web_md) for:

Skill extraction
Keyword detection
Text similarity comparison
Entity recognition (education, experience)


# Threshold Logic

Category	 Threshold

Skills High 	≥ 80%
Skills Medium	50–79%
Skills Low	     < 50%
Final Shortlist	  ≥ 70