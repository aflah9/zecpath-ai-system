How to use this system:


# 1. Setup Instructions

1. Clone project
2. Create virtual environment
3. Install requirements:
   pip install -r requirements.txt
4. Run server:
   uvicorn main:app --reload

# 2. How to Use ATS API

POST /analyze_resume

Input:
- Resume file
- Job description

Output:
- Score
- Ranking
- Recommendation

# 3. How to Add New Features

• Add new scoring rule in ats_scorer.py
• Update API response format