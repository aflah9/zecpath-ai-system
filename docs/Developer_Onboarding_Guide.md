1. PROJECT OVERVIEW
# Zecpath AI System – Developer Onboarding Guide

Zecpath AI is an end-to-end AI-powered hiring system that automates:
- Resume parsing
- ATS scoring
- Candidate screening
- HR interviews
- Technical evaluation
- Machine test evaluation
- Integrity analysis
- Final hiring decision
📁 2. PROJECT STRUCTURE (VERY IMPORTANT)

Use YOUR real folders:

## Project Structure

ai_engines/        → Core AI processing (resume parsing, scoring)
ai_core/           → Decision engine + optimization layer
screening_ai/      → HR screening + conversation AI
interview_ai/      → HR + behavioral interviews
technical_ai/      → Technical assessment engine
machine_test/      → Practical coding evaluation
integrity_ai/      → Fraud / cheating detection
api/               → FastAPI/REST endpoints
models/            → Data models
parser/            → Resume + section parsing
scoring/           → Ranking logic
security/          → Access control + encryption
observability/     → Logging, metrics, alerts
tests/             → Full system testing
data/              → Training + sample datasets
logs/              → System logs
🧠 3. SYSTEM ARCHITECTURE SUMMARY
## Architecture Flow

Resume Upload
→ Resume Parser (ai_engines)
→ ATS Scorer
→ Screening AI
→ Interview AI
→ Technical AI
→ Machine Test AI
→ Integrity AI
→ Decision Engine (ai_core)
→ Report Generator
⚙️ 4. HOW TO SETUP PROJECT
## Setup Instructions

1. Clone repository
git clone <repo-url>

2. Create virtual environment
python -m venv venv

3. Activate environment
venv\Scripts\activate   (Windows)

4. Install dependencies
pip install -r requirements.txt
▶️ 5. HOW TO RUN SYSTEM
## Run Full System

python -m tests.full_simulation

OR

## Run API Server

python api/routs.py
🧪 6. HOW TO RUN TESTS
## Run All Tests

python -m pytest tests/

OR specific test:

python -m tests.test_full_system
🔄 7. HOW AI PIPELINE WORKS (VERY IMPORTANT)
## AI Pipeline Flow

1. Resume uploaded
2. Resume parsed → structured JSON
3. ATS engine scores resume
4. Screening AI evaluates candidate answers
5. Interview AI analyzes behavior + communication
6. Technical AI evaluates skills
7. Machine test evaluates practical coding
8. Integrity AI detects fraud or cheating
9. Decision engine combines all scores
10. Final hiring report generated
🧩 8. HOW TO ADD NEW MODULE (MOST IMPORTANT FOR DEVELOPERS)
## Adding a New AI Module

Step 1: Create new file in appropriate folder
Example:
ai_engines/new_model.py

Step 2: Define input/output format

Step 3: Integrate into pipeline
(ai_core or decision_engine)

Step 4: Add API endpoint if needed

Step 5: Write test case in tests/
⚠️ 9. COMMON ISSUES
## Common Issues

1. Import errors
→ Check virtual environment

2. Module not found
→ Ensure correct folder structure

3. API failure
→ Check api/routs.py logs

4. Wrong scoring
→ Validate scoring engine inputs
🟢 STEP 4 — FINAL FILE YOU WILL SUBMIT

You will submit:

docs/Developer_Onboarding_Guide.md