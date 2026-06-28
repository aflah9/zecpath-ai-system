# Zecpath AI System – Deployment Guide

This document explains how to deploy the Zecpath AI Hiring System based on the actual project architecture.

## 1. System Requirements

### Backend
- Python 3.10+
- FastAPI / Flask (API layer in `api/`)
- pip dependencies from requirements.txt

### AI Modules
- ai_engines/
- screening_ai/
- interview_ai/
- technical_ai/
- integrity_ai/
- ai_core/

### Storage
- Local JSON files (data/)
- Logs (logs/)

## 2. Project Structure

zecpath-ai-system/
│
├── ai_engines/ → Resume parsing, ATS, scoring
├── screening_ai/ → Screening + conversation AI
├── interview_ai/ → HR interview system
├── technical_ai/ → Technical evaluation system
├── integrity_ai/ → Fraud/risk detection
├── ai_core/ → Decision engine + pipelines
├── api/ → API endpoints
├── models/ → Data models
├── data/ → Datasets & JSON files
├── tests/ → System validation
├── logs/ → System logs

## 3. Local Setup Instructions

### Step 1: Clone Project
git clone <your-repo>
cd zecpath-ai-system


run

python -m venv venv

archident environment
venv\Scripts\activate



Install Dependencies
pip install -r requirements.txt



Run System Tests
python -m tests.test_full_system

# RUN API SERVER (FROM YOUR api/ FOLDER)


API layer is:

api/

So document like this:

## 4. Run API Server

The API layer is located in `api/`.

To start the API:

```bash
python api/optimized_api.py

or

python api/integration_pipeline.py

---

# 🟢 STEP 8 — HOW AI SYSTEM RUNS (BASED ON YOUR REAL PIPELINE)

```markdown
## 5. System Execution Flow

Resume Upload
↓
ai_engines/resume_parser.py
↓
ai_engines/ats_scorer.py
↓
screening_ai/scoring_engine.py
↓
interview_ai/hr_scoring_engine.py
↓
technical_ai/technical_scoring_engine.py
↓
integrity_ai/risk_engine.py
↓
ai_core/decision_engine.py
↓
hiring_report_generator


EPLOYMENT OPTIONS (REALISTIC)
## 6. Deployment Options

### Option 1: Local Deployment
- Run API using Python directly

### Option 2: Docker (if added later)
- Containerize API + AI services

### Option 3: Cloud Deployment
- AWS EC2 / Azure / GCP
- Run FastAPI server
- Expose API endpoints

### Option 4: Scalable Architecture (Future)
- Kubernetes for AI microservices
- Load balancer for API layer
- Redis caching for scoring



LOGGING & MONITORING (YOU ALREADY HAVE logs/)
## 7. Logging & Monitoring

Logs are stored in:


logs/ai_system.log


Modules using logging:
- api/
- ai_core/
- screening_ai/
- integrity_ai/

Purpose:
- Debug failures
- Track AI decisions
- Monitor performance


TESTING BEFORE DEPLOYMENT (IMPORTANT FROM YOUR PROJECT)
## 8. Pre-Deployment Testing

Run all system tests:

```bash
python -m tests.full_simulation
python -m tests.load_test
python -m tests.test_stable

Ensure:

All tests pass
No scoring errors
API responds correctly

---

# 🟢 STEP 12 — FINAL CHECK SECTION

```markdown
## 9. Deployment Checklist

✔ All modules working  
✔ API server running  
✔ Tests passed  
✔ Logs enabled  
✔ No runtime errors  
✔ AI pipeline stable  