Zecpath AI System – Technical Handbook
1. System Overview

Zecpath AI is an AI-powered hiring system that automates the full recruitment lifecycle:

Resume parsing
ATS scoring
Screening interviews
HR interviews
Technical evaluation
Machine test evaluation
Integrity detection
Final hiring decision
Automated reporting
2. System Architecture (FROM YOUR CODE)
Resume Upload
    ↓
resume_parser.py
    ↓
ATS Scorer (ats_engine)
    ↓
screening_ai (screening_engine.py)
    ↓
interview_ai (hr_scoring_engine.py)
    ↓
technical_ai (technical_scoring_engine.py)
    ↓
machine_test (evaluation_logic.py)
    ↓
integrity_ai (risk_engine.py)
    ↓
ai_core/decision_engine.py
    ↓
ai_core/hiring_report_generator.py
    ↓
api/optimized_api.py
3. MODULE DOCUMENTATION (IMPORTANT)
📌 Example Format (YOU MUST FOLLOW FOR ALL MODULES)
📄 Resume Parser (ai_engines/resume_parser.py)
Purpose

Extract structured data from resumes.

Input
PDF / Text Resume
Output
{
  "name": "",
  "skills": [],
  "experience": [],
  "education": []
}
Used By
ATS Engine
Screening AI
Scoring Engine
📄 ATS Scorer (ats_engine/ats_scorer.py)
Purpose

Matches resume with job description.

Input
{
  "resume": {},
  "job_description": {}
}
Output
{
  "ats_score": 82
}
📄 Decision Engine (ai_core/decision_engine.py)
Purpose

Final hiring decision system.

Input
{
  "ats_score": 80,
  "interview_score": 75,
  "technical_score": 85,
  "behavior_score": 70,
  "integrity_risk": "low"
}
Output
{
  "final_decision": "Selected",
  "final_score": 81
}
4. SCORING LOGIC (FROM YOUR SYSTEM)

Based on your architecture:

Final Score =
ATS (20%)
Screening (15%)
HR Interview (20%)
Technical (25%)
Machine Test (20%)
Behavior Adjustment
Integrity Penalty
5. API DOCUMENTATION (FROM /api)
📄 POST /resume/parse

Input:

PDF Resume

Output:

{
  "parsed_resume": {}
}
📄 POST /decision/final

Input:

{
  "candidate_id": "C101"
}

Output:

{
  "decision": "Selected"
}
6. DATA MODELS (FROM my REAL JSON FILES)
Candidate Model
{
  "candidate_id": "C1",
  "resume": {},
  "ats_score": 0,
  "interview_scores": {},
  "final_decision": ""
}
Report Model
{
  "candidate_id": "C1",
  "final_score": 80,
  "decision": "Selected",
  "risk_flags": []
}
7. SYSTEM WORKFLOW
Resume Upload
    ↓
Parsing
    ↓
ATS Scoring
    ↓
Screening AI
    ↓
HR Interview AI
    ↓
Technical AI
    ↓
Machine Test
    ↓
Integrity Check
    ↓
Decision Engine
    ↓
Report Generator

7. System Architecture
Resume Upload
    ↓
resume_parser.py
    ↓
ATS Scorer (ats_engine)
    ↓
screening_ai (screening_engine.py)
    ↓
interview_ai (hr_scoring_engine.py)
    ↓
technical_ai (technical_scoring_engine.py)
    ↓
machine_test (evaluation_logic.py)
    ↓
integrity_ai (risk_engine.py)
    ↓
ai_core/decision_engine.py
    ↓
ai_core/hiring_report_generator.py
    ↓
api/optimized_api.py

8. SETUP GUIDE
git clone <repo>

cd zecpath-ai-system

python -m venv venv

pip install -r requirements.txt

python api/optimized_api.py
9. DEPLOYMENT GUIDE

Recommended architecture:

Docker containers for each AI service
API Gateway for routing
Load balancer for scaling
Logging system for monitoring
10. DEVELOPER ONBOARDING
Step 1

Understand folder structure

Step 2

Start with:

ai_engines/resume_parser.py
Step 3

Trace full pipeline:

Parser → ATS → Screening → Interview → Decision
Step 4

Run tests:

python -m tests.full_simulation