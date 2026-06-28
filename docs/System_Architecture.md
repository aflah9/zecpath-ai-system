ZECPATH-AI-SYSTEM

1-AI_CPRE
-----------------------------------------

1. CORE DECISION ENGINE (MOST IMPORTANT)
📄 decision_engine.py
🎯 Purpose

Makes the final hiring decision based on all AI scores.

📥 Input
{
  "ats_score": 80,
  "technical_score": 75,
  "hr_score": 70,
  "machine_test_score": 85,
  "behavior_risk": "Low",
  "integrity_risk": "Low"
}
📤 Output
{
  "final_score": 78.5,
  "decision": "Selected"
}
🧠 Role in system
Final authority module
Combines all AI outputs
Produces hiring decision

⭐ 2. MAIN PIPELINE ENGINE

📄 pipeline.py
🎯 Purpose

Runs the basic AI flow step-by-step

📥 Input
{
  "candidate_id": "C1",
  "resume": {}
}
📤 Output
{
  "parsed_resume": {},
  "scores": {},
  "decision": ""
}
🧠 Role
Orchestrates workflow
Calls multiple AI modules in sequence

📄 unified_pipeline.py
🎯 Purpose

New improved version of pipeline (central controller)

📥 Input

Candidate data (resume + interview + tests)

📤 Output

Full evaluation report

🧠 Role
Combines all pipelines into ONE system
Production-ready flow

📄 recommendation_pipeline.py
🎯 Purpose

Generates hiring recommendations

📥 Input
{
  "final_score": 78,
  "risk": "Low"
}
📤 Output
{
  "recommendation": "Hire"
}
🧠 Role
Converts score → decision label

⭐ 3. SCORING SYSTEM

📄 unified_scoring_engine.py
🎯 Purpose

Core scoring system for all evaluations

📥 Input
Resume data
Interview data
Skills
Experience
📤 Output
{
  "score": 82
}
🧠 Role
Base scoring logic engine
Used by multiple modules

📄 refined_scoring_logic.py
🎯 Purpose

Improved scoring with better accuracy

📥 Input

Candidate structured data

📤 Output

More accurate weighted score

🧠 Role
Replaces basic scoring
Better weighting system

📄 hiring_fit.py
🎯 Purpose

Checks if candidate is a good fit

📥 Input

Skills + role match data

📤 Output
{
  "fit_score": 0.85
}
🧠 Role
Role matching system

📄 hiring_fit_calculator.py
🎯 Purpose

Calculates numerical fit score

📥 Input

Skills, experience, job description

📤 Output

Fit percentage

🧠 Role
Supports hiring_fit.py

⭐ 4. REPORT GENERATION
📄 hiring_report_generator.py
🎯 Purpose

Generates final hiring report

📥 Input
{
  "candidate_id": "C1",
  "scores": {},
  "decision": "Selected"
}
📤 Output
{
  "report_pdf": "C1_report.pdf"
}
🧠 Role
Final output generator
Used by HR system
📄 report_formatter.py
🎯 Purpose

Formats report data into readable structure

📥 Input

Raw AI outputs

📤 Output

Formatted report JSON / text

📄 report_exporter.py
🎯 Purpose

Exports report (PDF/JSON)

📥 Input

Formatted report

📤 Output

File saved in /outputs

⭐ 5. BEHAVIOR + LOGIC MODULES

📄 conversation_logic.py
🎯 Purpose

Handles conversation flow in interviews

📥 Input

User responses

📤 Output

Next question / response evaluation

📄 cross_round_engine.py
🎯 Purpose

Combines multiple interview rounds

📥 Input

HR + Technical + Machine test results

📤 Output

Unified candidate evaluation

📄 explanation.py + explanations.py
🎯 Purpose

Generates reasoning for AI decisions

📥 Input

Scores + decision

📤 Output
{
  "explanation": "Candidate performed well in technical round..."
}
📄 confidence.py
🎯 Purpose

Calculates AI confidence level

📥 Input

Model outputs

📤 Output
{
  "confidence": 0.91
}
📄 normalizer.py
🎯 Purpose

Cleans and standardizes input data

📥 Input

Raw resume/interview data

📤 Output

Normalized structured JSON

⭐ 6. SYSTEM OPTIMIZATION MODULES

📄 optimized_ai_engine.py
🎯 Purpose

Faster version of AI engine

📥 Input

Same as main pipeline

📤 Output

Optimized prediction

📄 performance_optimized.py
🎯 Purpose

Improves speed and memory usage

📥 Input

AI tasks

📤 Output

Faster processed results

📄 memory_optimization.py
🎯 Purpose

Reduces memory usage in large processing

📥 Input

Large datasets

📤 Output

Compressed/optimized data flow

📄 stable_system.py
🎯 Purpose

Ensures system reliability

📥 Input

Any pipeline execution

📤 Output

Stable execution result (no crash)

⭐ 7. SUPPORT MODULES

📄 aggregation_pipeline.py
🎯 Purpose

Combines all AI module outputs

📥 Input

All scores + evaluations

📤 Output




🧠 HOW YOUR SYSTEM ACTUALLY WORKS (REAL FLOW)

This is the MOST important part for your documentation:

Resume / Interview Input
        ↓
normalizer.py
        ↓
pipeline.py / unified_pipeline.py
        ↓
scoring engines
        ↓
behavior + integrity modules
        ↓
aggregation_pipeline.py
        ↓
decision_engine.py
        ↓
recommendation_pipeline.py
        ↓
hiring_report_generator.py
        ↓
report_exporter.py


FINAL PURPOSE OF ai_core

Your ai_core folder is responsible for:

✔ Resume understanding
✔ Candidate scoring
✔ Interview evaluation
✔ Behavioral analysis
✔ Integrity detection
✔ Final hiring decision
✔ Report generation
✔ System optimization

2,AI-ENGIENS
------------------------------------------------

Role of ai_engines/

This folder is responsible for:

🔹 Resume understanding
🔹 Job description understanding
🔹 Skill extraction
🔹 Matching logic
🔹 ATS scoring
🔹 Candidate ranking
🔹 Eligibility checking
🔹 Fairness validation

👉 In simple words:

This is the intelligence + preprocessing layer before AI decision making

⭐ 1. CORE SCORING ENGINE
📄 ats_scorer.py
🎯 Purpose

Calculates ATS (Applicant Tracking System) score

This is the first major filtering layer.

📥 Input
{
  "resume": {},
  "job_description": {}
}
📤 Output
{
  "ats_score": 82
}
🧠 What it does
Matches resume with job description
Scores keyword relevance
Checks experience fit
Gives hiring relevance score

⭐ 2. CANDIDATE RANKING SYSTEM

📄 candidate_ranker.py
🎯 Purpose

Ranks multiple candidates for a job

📥 Input
[
  {"candidate_id": "C1", "score": 80},
  {"candidate_id": "C2", "score": 75}
]
📤 Output
[
  {"candidate_id": "C1", "rank": 1},
  {"candidate_id": "C2", "rank": 2}
]
🧠 Role
Sorting candidates
Selecting top applicants

⭐ 3. RESUME PROCESSING LAYER

📄 resume_processor.py
🎯 Purpose

Main pipeline for resume processing

📥 Input
PDF / Resume text
📤 Output
{
  "structured_resume": {}
}
🧠 Role
Orchestrates parsing + extraction
Main entry point for resume AI

⭐ 4. RESUME PARSER (CORE NLP MODULE)

📄 resume_parser.py
🎯 Purpose

Extract structured data from resume

📥 Input
Raw resume text / PDF text
📤 Output
{
  "name": "",
  "skills": [],
  "experience": [],
  "education": []
}
🧠 Role
Converts unstructured → structured data

⭐ 5. TEXT EXTRACTION

📄 resume_text_extractor.py
🎯 Purpose

Extract raw text from PDF or DOC

📥 Input
PDF file
📤 Output
Raw text string
🧠 Role
First step of pipeline
Feeds parser

⭐ 6. SKILL INTELLIGENCE SYSTEM

📄 skill_extractor.py
🎯 Purpose

Extract skills from resume/job description

📥 Input
Resume text
📤 Output
{
  "skills": ["Python", "SQL", "ML"]
}
📄 skill_matcher.py (EMPTY FILE ⚠️)
🎯 Purpose (INTENDED)

Matches resume skills vs job skills

📥 Input
{
  "resume_skills": [],
  "job_skills": []
}
📤 Output
{
  "match_score": 0.85
}
⭐ 7. JOB DESCRIPTION ENGINE

📄 jd_parser.py
🎯 Purpose

Extract structured data from job description

📥 Input
Job description text
📤 Output
{
  "required_skills": [],
  "experience_required": "",
  "role": ""
}
🧠 Role
Understand employer requirements

⭐ 8. EDUCATION ANALYSIS

📄 education_parser.py
🎯 Purpose

Extract education details

📥 Input

Resume text

📤 Output
{
  "degree": "B.Tech",
  "university": "",
  "year": ""
}
🧠 Role
Education scoring input

⭐ 9. EXPERIENCE ANALYSIS

📄 experience_parser.py
🎯 Purpose

Extract work experience

📥 Input

Resume text

📤 Output
{
  "companies": [],
  "years": 5
}
🧠 Role
Used in ATS scoring + eligibility

⭐ 10. SCORING CORE

📄 scorer.py
🎯 Purpose

Base scoring engine

📥 Input

All candidate features

📤 Output
{
  "score": 78
}
🧠 Role
Generic scoring system used by ATS + ranking

⭐ 11. SEMANTIC MATCHING (VERY IMPORTANT AI)

📄 semantic_matcher.py
🎯 Purpose

Find meaning-based similarity (NOT keyword only)

📥 Input
{
  "resume_text": "",
  "job_text": ""
}
📤 Output
{
  "similarity_score": 0.87
}
🧠 Role
AI-based understanding
Improves ATS accuracy

⭐ 12. ELIGIBILITY ENGINE

📄 eligibility_engine.py
🎯 Purpose

Checks if candidate qualifies for role

📥 Input
{
  "experience": 3,
  "skills": [],
  "job_requirements": {}
}
📤 Output
{
  "eligible": true
}
🧠 Role
Hard filter before scoring

⭐ 13. FAIRNESS ENGINE (VERY IMPORTANT)

📄 fairness_engine.py
🎯 Purpose

Ensures unbiased hiring decisions

📥 Input

Scores + candidate data

📤 Output
{
  "bias_check": "Passed",
  "adjusted_score": 81
}
🧠 Role
Removes bias in hiring
Ensures fairness compliance
🧠 OVERALL FLOW (REAL SYSTEM BEHAVIOR)
Resume PDF
   ↓
resume_text_extractor
   ↓
resume_parser
   ↓
skill_extractor + education_parser + experience_parser
   ↓
jd_parser
   ↓
semantic_matcher
   ↓
ats_scorer
   ↓
scorer
   ↓
fairness_engine
   ↓
candidate_ranker
   ↓
eligibility_engine
   ↓
AI Core Decision System
🎯 FINAL PURPOSE OF ai_engines

This folder is responsible for:

✔ Resume understanding
✔ Job description understanding
✔ Skill extraction
✔ Semantic matching
✔ ATS scoring
✔ Candidate ranking
✔ Eligibility filtering
✔ Fairness checking

3,API
-----------------------------------------------

API Layer (api/)
🧠 Role of this folder

This layer exposes your AI system to the outside world (frontend, apps, HR dashboards).

It handles:

Requests
Validation
Pipeline execution
Error handling
Response formatting

⭐ 1. MAIN ORCHESTRATION API

📄 integration_pipeline.py
🎯 Purpose

This is the core API orchestrator

It connects:

API → AI Engines → Decision System → Response

📥 Input
{
  "candidate_id": "C1",
  "resume": {},
  "job_description": {},
  "interview_data": {}
}
📤 Output
{
  "ats_score": 80,
  "technical_score": 75,
  "final_decision": "Selected"
}
🧠 Role in system
Calls AI pipeline
Coordinates all AI modules
Produces final API response

⭐ 2. OPTIMIZED API (FAST VERSION)

📄 optimized_api.py
🎯 Purpose

High-performance version of API

Used for:

Faster response
Production scaling
Reduced latency
📥 Input

Same as main API:

candidate data
📤 Output

Same structure but faster execution

🧠 Role
Performance optimized endpoint
Used in production traffic

⭐ 3. STABLE API (SAFE VERSION)

📄 stable_api.py
🎯 Purpose

Fault-tolerant API version

📥 Input

Candidate + job data

📤 Output
{
  "status": "success",
  "data": {}
}

OR fallback error-safe response

🧠 Role
Prevents system crashes
Ensures always-responding API

⭐ 4. ROUTES FILE (API ENDPOINT DEFINITIONS)

📄 routs.py ⚠️ (typo: should be routes.py)
🎯 Purpose

Defines all API endpoints

📥 Example endpoints
POST /resume/upload
POST /candidate/evaluate
POST /ats/score
GET /report/{id}
📤 Output

Routes → call internal pipeline

🧠 Role
Maps URL → function
Entry point for frontend

⭐ 5. SCHEMAS (DATA VALIDATION)

📄 schemas.py
🎯 Purpose

Defines request/response structure

📥 Input schema example
{
  "candidate_id": "string",
  "resume": "object",
  "job_description": "object"
}
📤 Output schema example
{
  "score": "float",
  "decision": "string"
}
🧠 Role
Ensures correct data format
Prevents invalid API calls

⭐ 6. ERROR HANDLING SYSTEM

📄 error_handling.py
🎯 Purpose

Handles API failures safely

📥 Input

Any API error (exception, timeout, invalid input)

📤 Output
{
  "error": "Invalid Resume Format",
  "status": 400
}
🧠 Role
Prevents system crashes
Returns clean error messages
Improves reliability
🧠 FULL API FLOW (REAL SYSTEM)
Frontend / User
      ↓
routes.py
      ↓
integration_pipeline.py
      ↓
ai_engines + ai_core
      ↓
decision_engine
      ↓
response formatting
      ↓
optimized_api / stable_api
      ↓
Final JSON Response

⚙️ WHAT EACH FILE DOES (SUMMARY TABLE)

File	Purpose

integration_pipeline.py	Main AI workflow controller
optimized_api.py	Fast production API
stable_api.py	Safe fallback API
routs.py	API endpoints
schemas.py	Input/output validation
error_handling.py	Error management

🎯 FINAL PURPOSE OF api/ FOLDER

This folder is responsible for:

✔ Receiving user requests
✔ Validating input
✔ Sending data to AI system
✔ Handling errors
✔ Returning structured responses
✔ Connecting frontend to backend AI

4,ATS_ENGIENE
---------------------------------------------

1. CORE FILE
📄 ats_scorer.py
🎯 Purpose

This is the main ATS intelligence module.

It calculates how well a candidate matches a job description based on:

Skills match
Experience match
Keywords relevance
Role compatibility
Semantic similarity (if integrated)
📥 INPUT

Typical input to this module:

{
  "candidate_resume": {
    "skills": ["Python", "SQL", "ML"],
    "experience_years": 3,
    "education": "B.Tech"
  },
  "job_description": {
    "required_skills": ["Python", "SQL"],
    "min_experience": 2,
    "role": "Data Analyst"
  }
}
📤 OUTPUT
{
  "ats_score": 82,
  "skill_match": 0.85,
  "experience_match": 0.75,
  "keyword_match": 0.80
}

OR simplified version:

{
  "ats_score": 82,
  "status": "Pass"
}
🧠 WHAT IT ACTUALLY DOES

Inside ats_scorer.py, logic typically includes:

1. Skill Matching
Compares resume skills vs job skills
Calculates overlap ratio
2. Experience Scoring
Checks years of experience
Matches required minimum
3. Keyword Matching
Finds important JD keywords in resume
4. Weighted Scoring

Example formula:

ATS Score =
(Skills Match × 40%)
+ (Experience × 30%)
+ (Keyword Match × 30%)
🔄 ROLE IN FULL SYSTEM
Resume Parser
      ↓
Skill Extractor
      ↓
JD Parser
      ↓
ATS Scorer  ← THIS MODULE
      ↓
Decision Engine
🎯 PURPOSE IN PROJECT

This module is used for:

✔ First-level filtering
✔ Shortlisting candidates
✔ Reducing workload for AI core
✔ Pre-scoring before interview AI



5,behavior_ai
----------------------------------------------

1. CORE FILE

📄 ats_scorer.py
🎯 Purpose

This is the main ATS intelligence module.

It calculates how well a candidate matches a job description based on:

Skills match
Experience match
Keywords relevance
Role compatibility
Semantic similarity (if integrated)
📥 INPUT

Typical input to this module:

{
  "candidate_resume": {
    "skills": ["Python", "SQL", "ML"],
    "experience_years": 3,
    "education": "B.Tech"
  },
  "job_description": {
    "required_skills": ["Python", "SQL"],
    "min_experience": 2,
    "role": "Data Analyst"
  }
}
📤 OUTPUT
{
  "ats_score": 82,
  "skill_match": 0.85,
  "experience_match": 0.75,
  "keyword_match": 0.80
}

OR simplified version:

{
  "ats_score": 82,
  "status": "Pass"
}
🧠 WHAT IT ACTUALLY DOES

Inside ats_scorer.py, logic typically includes:

1. Skill Matching
Compares resume skills vs job skills
Calculates overlap ratio
2. Experience Scoring
Checks years of experience
Matches required minimum
3. Keyword Matching
Finds important JD keywords in resume
4. Weighted Scoring

Example formula:

ATS Score =
(Skills Match × 40%)
+ (Experience × 30%)
+ (Keyword Match × 30%)
🔄 ROLE IN FULL SYSTEM
Resume Parser
      ↓
Skill Extractor
      ↓
JD Parser
      ↓
ATS Scorer  ← THIS MODULE
      ↓
Decision Engine
🎯 PURPOSE IN PROJECT

This module is used for:

✔ First-level filtering
✔ Shortlisting candidates
✔ Reducing workload for AI core
✔ Pre-scoring before interview AI


⚡ FINAL SUMMARY
File	Purpose
ats_scorer.py	Calculates ATS score for resume-job match
init.py	Makes folder a Python module
🚀 WHERE IT FITS IN YOUR SYSTEM
Resume Upload
   ↓
ai_engines (parsing)
   ↓
ATS Engine (THIS FOLDER)
   ↓
ai_core (decision making)
   ↓
API (response)

6,cache
-------------------------------------

here all the parsed and json formated structerd resumes are here


7,config
-----------------------------------------------

eligibility rules is in here

8,data
------------------------------------------------

Data Layer (data/)
📌 Role in system

This folder contains datasets, templates, mappings, schemas, and sample data used by all AI modules.

It is used for:

Training AI logic
Testing pipelines
Standardizing inputs/outputs
Mapping skills, questions, and scoring logic
⭐ 1. CORE DATASETS (MOST IMPORTANT)
📄 hr_screening_dataset.json
🎯 Purpose

Training dataset for HR screening AI

📥 INPUT
{
  "candidate": "C1",
  "answers": [],
  "labels": {
    "hire": true
  }
}
📤 OUTPUT (used for training)
HR scoring patterns
Behavioral labels
🧠 ROLE
Trains HR scoring engine
Improves interview AI accuracy
⭐ 2. SKILL DICTIONARY (VERY IMPORTANT)
📄 skill_dictionary.json
🎯 Purpose

Defines:

Skills
Categories
Synonyms
📥 INPUT

Used by skill extractor & ATS

📤 OUTPUT
{
  "python": ["python", "py", "python3"],
  "data_analysis": ["analytics", "data science"]
}
🧠 ROLE
Normalizes skill matching
Improves ATS accuracy
⭐ 3. QUESTION CATEGORY MAPPING
📄 question_category_mapping.json
🎯 Purpose

Maps interview questions into categories:

Technical
HR
Behavioral
📥 INPUT
"Explain SQL joins"
📤 OUTPUT
"Technical"
🧠 ROLE
Helps interview_ai classify questions
Used in scoring logic
⭐ 4. VOICE TRANSCRIPT SCHEMA
📄 voice_transcript_schema.json
🎯 Purpose

Defines structure for voice-based interview AI

📥 INPUT

Speech-to-text interview data

📤 OUTPUT
{
  "speaker": "candidate",
  "text": "",
  "sentiment": "",
  "timestamp": ""
}
🧠 ROLE
Future voice interview system
Supports AI coaching & analysis
⭐ 5. API MAPPING FILE
📄 api_mapping.txt
🎯 Purpose

Maps API endpoints → internal modules

Example:

POST /resume → resume_parser
POST /ats → ats_scorer
POST /interview → interview_ai
🧠 ROLE
Connects API layer to AI engines
Documentation + routing reference
⭐ 6. QUESTION SYSTEM (SCREENING AI)
📁 screening_ai/
📄 dataset_loader.py
🎯 Purpose

Loads screening datasets

📥 Input

JSON files

📤 Output

Structured dataset objects

📄 question_objects.json
🎯 Purpose

Stores structured interview questions

📄 question_templates.py
🎯 Purpose

Generates dynamic questions

📄 screening_flow.json
🎯 Purpose

Defines screening process steps

🧠 ROLE OF SCREENING_AI

✔ Builds interview questions
✔ Controls screening flow
✔ Feeds interview_ai module

⭐ 7. SAMPLE DATA FILES (TESTING ONLY)
📄 sample_answers.py
Fake candidate answers for testing
📄 sample_behavior.py
Behavioral test cases
📄 sample_scores.py
Expected scoring outputs
🧠 ROLE
Used for unit testing
Helps validate AI modules
⭐ 8. TEST DATA
📄 test_candidates.json
🎯 Purpose

Real-like candidate data for testing pipeline

📥 INPUT
{
  "name": "Test Candidate",
  "skills": ["Python"]
}
📤 OUTPUT

Used to simulate full system

⭐ 9. METADATA STANDARDS
📄 metadata_standards.md
🎯 Purpose

Defines:

JSON formats
naming conventions
data rules
🧠 ROLE
Ensures consistency across AI modules
⭐ 10. EMPTY DATA FOLDERS (STRUCTURE ONLY)

These are placeholders:

resumes/
parsed_profiles/
interview_results/
screening_reports/
training_datasets/
🧠 PURPOSE
Future storage
Pipeline outputs
Training expansion
🧠 OVERALL ROLE OF data/
Data Layer
   ↓
AI Engines
   ↓
AI Core
   ↓
Interview AI
   ↓
ATS Engine
   ↓
Decision System

9,demo
-----------------------------------------------
Demo Module (demo/)
📌 Role in system

This folder is used to run sample executions of the entire AI hiring system

It is NOT production logic.

It is used for:
✔ showcasing system
✔ testing workflows
✔ demo to clients / HR
✔ debugging pipeline

⭐ 1. MAIN DEMO SCRIPT
📄 run_demo.py
🎯 Purpose

This is the main entry point for running the full AI system demo

It simulates:

resume processing
ATS scoring
interview evaluation
final decision
📥 INPUT
{
  "candidate": "sample_user",
  "resume": {},
  "job_description": {}
}

OR loads from dataset:

hr_demo_dataset.json
📤 OUTPUT
{
  "ats_score": 82,
  "interview_score": 78,
  "final_score": 80,
  "decision": "Selected"
}
🧠 ROLE IN PROJECT
Runs full pipeline in one click
Used for testing system end-to-end
Used for presentations / demos
⭐ 2. DEMO DATASET
📄 hr_demo_dataset.json
🎯 PURPOSE

Contains sample candidate data for testing system behavior

📥 INPUT FORMAT
{
  "candidate_id": "C1",
  "skills": ["Python", "SQL"],
  "experience": 3,
  "answers": []
}
📤 OUTPUT (used by system)
ATS score
Interview score
Final decision
🧠 ROLE
Feeds demo pipeline
Simulates real hiring data
⭐ 3. INIT FILE
📄 __init__.py
🎯 PURPOSE

Marks folder as Python package

📥 INPUT

None

📤 OUTPUT

None

🧠 ROLE
Allows imports like:
from demo.run_demo import run
🧠 FULL DEMO FLOW
hr_demo_dataset.json
        ↓
run_demo.py
        ↓
AI Engines (ATS + Interview + Integrity)
        ↓
AI Core Decision Engine
        ↓
Final Result Output
🎯 PURPOSE OF demo/

This module is used for:

✔ End-to-end system testing
✔ Showing working AI pipeline
✔ Debugging AI outputs
✔ Client / recruiter demonstrations
✔ Validating system behavior

10,docs
-----------------------------------------------
all the documnets of the project is in this folder,most of the daiy tasks docs is here that whatvwe done where we done why we done...



9,future
------------------------------------------------

Future Module (future/)
📌 Role of this folder

This folder defines future upgrades, system evolution, and next-generation AI features

It is NOT used in scoring directly.

It is used for:

Roadmap planning
System scaling design
AI innovation ideas
AI coaching system
Architecture evolution


10,integrity_ai
--------------------------------------------------

⭐ 1. CORE FILE

📄 ai_coach.py
🎯 Purpose

This is a future AI assistant module that helps:

Improve candidate performance
Suggest interview answers
Guide hiring decisions
Provide feedback on weak areas

👉 Think of it as:

“AI mentor for candidates or recruiters”

📥 INPUT
{
  "candidate_profile": {
    "skills": ["Python", "SQL"],
    "interview_answers": []
  },
  "feedback_type": "improvement"
}
📤 OUTPUT
{
  "suggestions": [
    "Improve system design knowledge",
    "Practice SQL joins",
    "Work on communication clarity"
  ]
}
🧠 ROLE IN PROJECT
Future interview assistant
AI learning coach
Feedback generator

⭐ 2. ARCHITECTURE DOCUMENT

📄 architecture.md
🎯 Purpose

Describes future system design improvements

Includes:

Microservices scaling
AI pipeline evolution
Distributed architecture ideas
📥 INPUT

Not runtime based (documentation file)

📤 OUTPUT

System design blueprint

🧠 ROLE
Guides future engineers
Helps scaling decisions
Defines system evolution

⭐ 3. FUTURE FEATURES

📄 future_features.md
🎯 Purpose

Lists upcoming enhancements like:

Voice interview AI
Emotion detection
Video analysis
Real-time scoring
AI recruiter chatbot
📥 INPUT

None (planning document)

📤 OUTPUT

Feature roadmap list

🧠 ROLE
Product innovation planning
Feature backlog

⭐ 4. INNOVATION PROPOSAL

📄 innovation_proposal.md
🎯 Purpose

Contains advanced AI ideas such as:

Multi-modal hiring AI
Behavioral prediction models
AI-based fraud detection
Adaptive interview systems
🧠 ROLE
R&D thinking
Startup pitch material
System evolution ideas

⭐ 5. ROADMAP

📄 roadmap.md
🎯 Purpose

Defines timeline of system growth

Example:

Phase 1 → Core AI system
Phase 2 → Optimization
Phase 3 → Scaling
Phase 4 → AI intelligence upgrades
🧠 ROLE
Project planning
Development roadmap
Version evolution

⭐ 6. SCALING STRATEGY

📄 scaling_strategy.md
🎯 Purpose

Explains how system will handle:

Large number of users
High API traffic
Distributed AI processing
Cloud scaling

🧠 ROLE
DevOps planning
Production scaling design
Infrastructure strategy

🧠 OVERALL ROLE OF future/
Current AI System
        ↓
future/
        ↓
Next Version Design
        ↓
Scalable AI Hiring Platform

Integrity AI Module (integrity_ai/)
📌 Role in system

This module detects fake, risky, inconsistent, or suspicious candidate behavior

It acts as a trust & safety layer before final hiring decision.

⭐ 1. CORE ORCHESTRATOR
📄 main.py
🎯 Purpose

Main entry point for integrity checking system.

It coordinates:

pattern detection
risk scoring
warnings
final integrity decision
📥 INPUT
{
  "resume": {},
  "interview_answers": {},
  "behavior_data": {}
}
📤 OUTPUT
{
  "integrity_status": "Low Risk",
  "risk_score": 0.15
}
🧠 ROLE
Central controller
Runs full integrity pipeline
⭐ 2. RISK ENGINE (CORE LOGIC)
📄 risk_engine.py
🎯 Purpose

Calculates risk score of candidate

📥 INPUT
{
  "behavior_flags": [],
  "resume_inconsistencies": [],
  "pattern_anomalies": []
}
📤 OUTPUT
{
  "risk_score": 0.72,
  "risk_level": "High"
}
🧠 ROLE
Converts signals → risk score
Core decision factor for integrity
⭐ 3. PATTERN DETECTION
📄 pattern_detection.py
🎯 PURPOSE

Detects suspicious patterns like:

Repeated fake skills
Over-exaggerated experience
Copy-paste resumes
AI-generated answers
📥 INPUT
Resume + interview text
📤 OUTPUT
{
  "anomalies": [
    "Overstated experience",
    "Keyword stuffing detected"
  ]
}
🧠 ROLE
Fraud detection logic
Pattern anomaly finder
⭐ 4. DETECTION LOGIC
📄 detection_logic.py
🎯 PURPOSE

Applies rules + AI heuristics for integrity checks

📥 INPUT
Resume data
Interview answers
📤 OUTPUT
{
  "flags": [
    "Inconsistent job history",
    "Skill mismatch detected"
  ]
}
🧠 ROLE
Rule-based validation engine
Feeds risk engine
⭐ 5. WARNING SYSTEM
📄 warning_system.py
🎯 PURPOSE

Generates warnings based on detected risk

📥 INPUT
{
  "risk_level": "High",
  "flags": []
}
📤 OUTPUT
{
  "warnings": [
    "Candidate shows inconsistent experience",
    "Manual review required"
  ]
}
🧠 ROLE
Alerts HR system
Marks candidates for review
⭐ 6. INTEGRATION FILE
📄 integration.py
🎯 PURPOSE

Connects integrity system with:

AI Core
ATS Engine
Decision Engine
📥 INPUT

Candidate full profile

📤 OUTPUT

Merged integrity result:

{
  "risk_score": 0.25,
  "status": "Safe"
}
🧠 ROLE
Bridge between modules
Sends results to main system
🧠 OVERALL FLOW (REAL SYSTEM)
Resume + Interview Data
          ↓
pattern_detection
          ↓
detection_logic
          ↓
risk_engine
          ↓
warning_system
          ↓
main.py (controller)
          ↓
integration.py
          ↓
AI Core Decision Engine
🎯 PURPOSE OF integrity_ai

This module ensures:

✔ No fake resumes
✔ No skill manipulation
✔ No inconsistent experience
✔ No AI-generated cheating ignored
✔ Risk-based filtering


11,interview_ai
----------------------------------------------
Interview AI Module (interview_ai/)
📌 Role in system

This module simulates and evaluates real interviews (HR + technical + behavioral) using AI.

It handles:

Interview question generation
Candidate responses analysis
Behavioral scoring
HR scoring
Communication analysis
Stress detection
Final interview decision
⭐ 1. CORE PIPELINE
📄 pipeline.py
🎯 Purpose

Main controller of the interview system.

It runs:

Questions → Answers → Evaluation → Scoring

📥 INPUT
{
  "candidate_id": "C1",
  "questions": [],
  "answers": []
}
📤 OUTPUT
{
  "hr_score": 78,
  "behavior_score": 82,
  "technical_score": 75,
  "final_interview_score": 79
}
🧠 ROLE
Orchestrates full interview flow
Calls all sub-engines
⭐ 2. HR SCORING SYSTEM
📄 hr_scoring_engine.py (VERY IMPORTANT)
🎯 Purpose

Calculates HR interview performance:

Communication
Confidence
Clarity
Behavioral signals
📥 INPUT
{
  "answers": [],
  "communication_data": {}
}
📤 OUTPUT
{
  "hr_score": 80
}
🧠 ROLE
Core HR evaluation engine
Used in final hiring decision
⭐ 3. BEHAVIOR ANALYSIS
📄 behavior_analyzer.py
🎯 Purpose

Analyzes candidate behavior during interview

📥 INPUT
Answers
Tone
Response style
📤 OUTPUT
{
  "behavior_score": 85
}
🧠 ROLE
Measures soft skills
Emotional intelligence estimation
⭐ 4. COMMUNICATION ENGINE
📄 communication_engine.py
🎯 Purpose

Evaluates:

clarity
grammar
fluency
articulation
📥 INPUT
Interview answers text
📤 OUTPUT
{
  "communication_score": 78
}
⭐ 5. CONFIDENCE ANALYZER
📄 confidence_analyzer.py
🎯 Purpose

Detects confidence level from answers

📥 INPUT

Interview responses

📤 OUTPUT
{
  "confidence_score": 0.82
}
⭐ 6. CONTRADICTION DETECTOR
📄 contradiction_detector.py
🎯 Purpose

Finds inconsistencies in answers

📥 INPUT

Multiple answers

📤 OUTPUT
{
  "contradictions": [
    "Conflicting experience timeline"
  ]
}
⭐ 7. FOLLOW-UP ENGINE (VERY IMPORTANT)
📄 followup_engine.py
🎯 Purpose

Generates follow-up questions dynamically

📥 INPUT

Candidate answer

📤 OUTPUT
{
  "next_question": "Can you explain your project architecture?"
}
⭐ 8. QUESTION SYSTEM
📄 question_generator.py
🎯 Purpose

Generates interview questions

📥 INPUT
{
  "role": "Data Analyst"
}
📤 OUTPUT
{
  "questions": [
    "Explain SQL joins",
    "What is data cleaning?"
  ]
}
⭐ 9. QUESTION BANK
📄 question_bank.json
🎯 Purpose

Predefined interview questions storage

📥 INPUT

None (static file)

📤 OUTPUT

Question list

⭐ 10. FINAL HR MODULE
📄 final_hr_module.py
🎯 Purpose

Combines ALL interview signals into final HR decision

📥 INPUT
{
  "hr_score": 80,
  "behavior_score": 85,
  "communication_score": 78,
  "confidence": 0.82
}
📤 OUTPUT
{
  "final_hr_decision": "Strong Hire"
}
⭐ 11. STABLE HR SYSTEM
📄 stable_hr_ai.py
🎯 Purpose

Production-safe version of HR AI system

prevents crashes
fallback logic
⭐ 12. SCORING ENGINE
📄 refined_scoring.py
🎯 Purpose

Improved scoring system for interview results

📥 INPUT

All interview signals

📤 OUTPUT

Final normalized score

⭐ 13. SUMMARY GENERATOR (VERY IMPORTANT)
📄 summary_generator.py
🎯 Purpose

Generates interview summary report

📥 INPUT

All scores + answers

📤 OUTPUT
{
  "summary": "Candidate performed well in technical but weak in communication"
}
⭐ 14. SUPPORT SYSTEMS
📄 state_tracker.py

Tracks interview progress

📄 stress_detector.py

Detects nervousness / pressure

📄 sentiment_engine.py

Analyzes emotional tone of answers

📄 scenario_evaluator.py

Evaluates real-world problem solving

📄 normalization.py

Cleans interview input

📄 repetition_handler.py

Detects repeated answers

📄 followup_logic.py

Logic behind follow-up decisions

📄 followup_stability.py

Ensures follow-up system stability

📄 hr_weights.py

Defines scoring weights

Example:

HR = 30%
Behavior = 25%
Communication = 25%
Confidence = 20%
🧠 OVERALL FLOW
Candidate Interview
        ↓
question_generator
        ↓
pipeline
        ↓
communication_engine
        ↓
behavior_analyzer
        ↓
confidence_analyzer
        ↓
contradiction_detector
        ↓
hr_scoring_engine
        ↓
refined_scoring
        ↓
final_hr_module
        ↓
summary_generator
        ↓
stable_hr_ai
🎯 PURPOSE OF interview_ai

This module is responsible for:

✔ AI-powered interview simulation
✔ HR evaluation automation
✔ Behavioral analysis
✔ Communication scoring
✔ Confidence detection
✔ Dynamic follow-up questions
✔ Final interview decision


12,logs
------------------------------------------------
Logs Module (logs/)
📌 Role in system

This folder records everything happening inside your AI system for debugging, monitoring, and auditing

It helps you answer:

What happened?
When did it happen?
Why did it fail?
Which module caused the issue?
⭐ 1. CORE LOG FILE
📄 ai_system.log
🎯 Purpose

This is the central log file of the entire Zecpath AI system

It records:

API requests
AI pipeline execution
Errors
Scores generated
Decision outputs
Performance timing
📥 INPUT

Automatically generated from:

API layer
AI engines
Core decision system
Interview system
ATS system

Example events:

Resume received
ATS scoring started
Interview AI executed
Decision generated
📤 OUTPUT

Log entries like:

[INFO] Resume parsed successfully
[INFO] ATS Score = 82
[INFO] Interview Score = 78
[INFO] Final Decision = Selected
[ERROR] Missing skill field in resume
🧠 ROLE IN PROJECT
Tracks system behavior
Helps debugging errors
Monitors performance
Stores execution history
Helps auditing hiring decisions


HOW LOGGING WORKS IN YOUR SYSTEM
User Request
     ↓
API Layer
     ↓
AI Engines
     ↓
AI Core Decision
     ↓
Every Step → logs/ai_system.log
🎯 PURPOSE OF logs/

This module is responsible for:

✔ Tracking system activity
✔ Debugging AI pipeline issues
✔ Monitoring performance
✔ Storing execution history
✔ Audit trail for hiring decisions

13,machine_test
----------------------------------------------
Machine Test Module (machine_test/)
📌 Role in system

This module evaluates candidate performance on hands-on tasks, coding tests, and practical assignments

It focuses on:

coding ability
problem solving
task completion
time efficiency
⭐ 1. CORE PIPELINE
📄 pipeline.py
🎯 Purpose

This is the main controller for machine test evaluation.

It manages:

test execution flow
scoring
time tracking
result aggregation
📥 INPUT
{
  "candidate_id": "C1",
  "test_cases": [],
  "code_submission": ""
}
📤 OUTPUT
{
  "code_score": 78,
  "accuracy": 85,
  "final_test_score": 80
}
🧠 ROLE
Orchestrates full machine test evaluation
Connects logic + scoring modules
⭐ 2. EVALUATION LOGIC (MAIN ENGINE)
📄 evaluation_logic.py
🎯 Purpose

Core evaluation system for submitted tasks.

It checks:

correctness
logic quality
output validation
edge cases
📥 INPUT
{
  "solution_code": "",
  "expected_output": "",
  "test_cases": []
}
📤 OUTPUT
{
  "passed_tests": 8,
  "failed_tests": 2,
  "accuracy": 80
}
🧠 ROLE
Core grading engine
Determines correctness of solution
⭐ 3. TIME SCORING SYSTEM
📄 time_scoring.py
🎯 Purpose

Evaluates how fast candidate completed the test.

📥 INPUT
{
  "start_time": "10:00",
  "end_time": "10:30",
  "expected_time_limit": 45
}
📤 OUTPUT
{
  "time_taken": 30,
  "time_score": 90
}
🧠 ROLE
Rewards efficiency
Penalizes slow execution
🧠 OVERALL MACHINE TEST FLOW
Code Submission
        ↓
pipeline.py
        ↓
evaluation_logic.py (correctness check)
        ↓
time_scoring.py (speed check)
        ↓
Final Score Calculation
        ↓
AI Core Decision Engine
🎯 PURPOSE OF machine_test/

This module evaluates:

✔ Coding ability
✔ Problem-solving skills
✔ Execution correctness
✔ Time efficiency
✔ Practical job readiness


14,models
------------------------------------------------
Models Layer (models/)
📌 Role in system

This folder defines the data structure (blueprints) used across ALL AI modules.

It ensures every system uses the same format for:

candidates
job descriptions
skills
experience
⭐ 1. CANDIDATE MODEL
📄 candidate.py
🎯 Purpose

Defines the structure of a candidate in the system.

📥 INPUT

Raw candidate data:

{
  "name": "John",
  "skills": ["Python", "SQL"],
  "experience_years": 3
}
📤 OUTPUT (structured model)
{
  "candidate_id": "auto_generated",
  "skills": [],
  "experience": {},
  "profile_score": 0
}
🧠 ROLE
Standardizes candidate format
Used by ATS, Interview AI, Decision Engine
⭐ 2. EXPERIENCE MODEL
📄 experience.py
🎯 PURPOSE

Defines how experience is stored and interpreted.

📥 INPUT
{
  "company": "ABC Corp",
  "role": "Data Analyst",
  "years": 2
}
📤 OUTPUT
{
  "total_experience": 2,
  "relevance_score": 0.8
}
🧠 ROLE
Used in ATS scoring
Used in interview evaluation
Helps eligibility engine
⭐ 3. JOB MODEL
📄 job.py
🎯 PURPOSE

Defines job structure (Job Description model)

📥 INPUT
{
  "title": "Data Analyst",
  "required_skills": ["Python", "SQL"],
  "min_experience": 2
}
📤 OUTPUT

Structured job object:

{
  "role": "Data Analyst",
  "skills": [],
  "requirements": {}
}
🧠 ROLE
Used by ATS Engine
Used by eligibility engine
Used for interview question generation
⭐ 4. SKILL MODEL
📄 skill.py
🎯 PURPOSE

Defines skill structure and classification

📥 INPUT
"Python"
📤 OUTPUT
{
  "skill": "Python",
  "category": "Programming",
  "weight": 0.9
}
🧠 ROLE
Used in ATS scoring
Used in skill matching
Used in recommendation engine
🧠 OVERALL ROLE OF models/
Raw Data
   ↓
models/
   ↓
Standardized AI Objects
   ↓
AI Engines + Core System
🎯 PURPOSE OF models/

This layer ensures:

✔ Consistent data structure
✔ Clean AI input/output format
✔ Reusable objects across system
✔ Better scoring accuracy
✔ Reduced system confusion

15,nlp
-----------------------------------------------
NLP Module (nlp/)
📌 Role in system

This module processes human language intent and meaning refinement

It sits between:

raw text input (resume/interview answers)
AI engines (scoring, decision, interview AI)
⭐ 1. CORE FILE
📄 intent_refinement.py
🎯 Purpose

This is the main NLP intelligence module.

It improves and clarifies user intent by:

detecting meaning behind text
refining unclear sentences
extracting intent from responses
normalizing candidate answers
📥 INPUT

Example input text:

"I kinda worked with data stuff and Python a bit in my last job"
📤 OUTPUT

Refined structured intent:

{
  "intent": "data analysis",
  "skills_detected": ["Python", "Data Handling"],
  "confidence": 0.72
}
🧠 WHAT IT ACTUALLY DOES

Inside this file, logic usually includes:

1. Intent Detection

Finds what user really means

2. Sentence Cleaning

Removes:

filler words
ambiguity
informal language
3. Skill Extraction

Extracts hidden skills from text

4. Normalization

Converts messy input → structured format

🧠 ROLE IN FULL SYSTEM
Raw Text (Resume / Interview Answer)
            ↓
nlp/intent_refinement.py
            ↓
Clean Structured Intent
            ↓
AI Engines (ATS / Interview AI / Core Decision)
🎯 PURPOSE OF NLP MODULE

This module is used for:

✔ Understanding human language
✔ Cleaning interview answers
✔ Extracting hidden skills
✔ Improving ATS accuracy
✔ Feeding structured data to AI engines


16,observability
------------------------------------------------

Observability Module (observability/)
📌 Role in system

This module tracks what the system is doing in real-time, how well it is performing, and when something goes wrong.

It provides:

logs (what happened)
metrics (how well it performs)
alerts (when something breaks)
audit trail (who did what)
⭐ 1. LOGGING SYSTEM
📄 logging.py
🎯 Purpose

Central logging system for the whole AI platform.

It records:

API calls
AI decisions
errors
pipeline execution steps
📥 INPUT
Events from all modules

Example:

ATS score generated
Interview completed
Decision created
📤 OUTPUT
[INFO] ATS completed
[INFO] Candidate evaluated
[ERROR] Missing resume field
🧠 ROLE
System activity tracking
Debugging support
Execution history
⭐ 2. METRICS SYSTEM
📄 metrics.py
🎯 Purpose

Tracks system performance:

response time
API latency
scoring speed
system load
📥 INPUT

Performance events:

{
  "api_latency": 120,
  "pipeline_time": 3.4
}
📤 OUTPUT
{
  "avg_latency": 110,
  "throughput": 45
}
🧠 ROLE
Performance monitoring
Optimization insights
Scalability tracking
⭐ 3. ALERT SYSTEM
📄 alerts.py
🎯 PURPOSE

Detects system issues and sends alerts.

📥 INPUT

Errors or anomalies:

high latency
pipeline failure
missing data
system crash risk
📤 OUTPUT
{
  "alert": "HIGH_LATENCY",
  "severity": "critical"
}
🧠 ROLE
Real-time system monitoring
Failure detection
Auto-warning system
⭐ 4. AUDIT SYSTEM
📄 audit.py
🎯 PURPOSE

Tracks who did what and when inside system.

Used for compliance + traceability.

📥 INPUT
{
  "user": "admin",
  "action": "final_decision_generated",
  "candidate_id": "C1"
}
📤 OUTPUT
{
  "recorded": true,
  "timestamp": "2026-06-28T12:00:00"
}
🧠 ROLE
Security tracking
Decision traceability
Compliance logging
🧠 OVERALL FLOW
AI System Events
      ↓
logging.py → record everything
      ↓
metrics.py → measure performance
      ↓
alerts.py → detect issues
      ↓
audit.py → track actions
🎯 PURPOSE OF observability/

This module ensures:

✔ System monitoring
✔ Performance tracking
✔ Error detection
✔ Security auditing
✔ Production reliability
✔ Debugging support

17,outputs
-----------------------------------------------
inhere is the ooutputs of prsed resumesand jd,json formated resuesand jad also here,


18,parser
-------------------------------------------------
Parser Module (parser/)
📌 Role in system

This module converts unstructured resume text → structured JSON data

It is the first intelligence layer in your pipeline.

⭐ 1. CORE FILE – RESUME PARSER
📄 resume_parser.py
🎯 Purpose

Extracts structured data from raw resumes.

It identifies:

name
skills
experience
education
companies
📥 INPUT
Raw resume text / PDF text

Example:

John worked at Google as a Data Analyst for 3 years. Skilled in Python and SQL.
📤 OUTPUT
{
  "name": "John",
  "skills": ["Python", "SQL"],
  "experience_years": 3,
  "company": "Google"
}
🧠 ROLE
Converts messy resume → structured AI data
Used by ATS + Interview + Decision engine
⭐ 2. SECTION SEGMENTER (VERY IMPORTANT)
📄 section_segmenter.py
🎯 Purpose

Splits resume into logical sections:

Experience
Skills
Education
Projects
📥 INPUT
Full resume text
📤 OUTPUT
{
  "experience_section": "...",
  "skills_section": "...",
  "education_section": "..."
}
🧠 ROLE
Pre-processing step before parsing
Improves accuracy of resume extraction
Helps NLP understand structure
🧠 FULL FLOW OF PARSER MODULE
Raw Resume Text
        ↓
section_segmenter.py
        ↓
resume_parser.py
        ↓
Structured Candidate JSON
        ↓
AI Engines (ATS / Interview / Core AI)
🎯 PURPOSE OF parser/

This module is used for:

✔ Resume text cleaning
✔ Section identification
✔ Structured data extraction
✔ Feeding AI engines
✔ Converting PDFs/text into AI format


19,sample data
--------------------------------------
inside here i uploaded a jd,in pdf formate

20,sample_resumes
----------------------------------------
here i uploaded the resumes in pdf format


21,scoring
--------------------------------------------
Scoring Module (scoring/)
📌 Role in system

This module takes all AI outputs and converts them into a final ranked list of candidates

It answers:

“Who is the best candidate among all evaluated candidates?”

⭐ 1. CORE FILE
📄 ranker.py
🎯 Purpose

This is the final ranking engine.

It combines scores from:

ATS engine
Interview AI
Machine test
Integrity AI
Behavior scoring

Then produces a final ranking order.

📥 INPUT
[
  {
    "candidate_id": "C1",
    "ats_score": 80,
    "interview_score": 75,
    "machine_test_score": 78,
    "integrity_score": 90
  },
  {
    "candidate_id": "C2",
    "ats_score": 70,
    "interview_score": 85,
    "machine_test_score": 80,
    "integrity_score": 95
  }
]
📤 OUTPUT
[
  {
    "candidate_id": "C2",
    "final_rank": 1,
    "final_score": 83.5
  },
  {
    "candidate_id": "C1",
    "final_rank": 2,
    "final_score": 80.2
  }
]
🧠 WHAT IT DOES INTERNALLY

Typical logic inside ranker.py:

1. Weighted scoring

Example:

Final Score =
ATS (20%)
+ Interview (25%)
+ Machine Test (25%)
+ Integrity (15%)
+ Behavior (15%)
2. Sorting
Sort candidates by final score
Assign rank position
3. Tie handling
Break ties using integrity score or interview score
🧠 ROLE IN FULL SYSTEM
AI Engines Output
        ↓
ATS + Interview + Machine Test + Integrity
        ↓
scoring/ranker.py
        ↓
Final Ranked Candidate List
        ↓
Decision Engine
🎯 PURPOSE OF scoring/

This module is responsible for:

✔ Final candidate ranking
✔ Comparing multiple candidates
✔ Producing hiring order
✔ Feeding decision engine
✔ Generating shortlist


22,screening_ai
-------------------------------------------------


Screening Module (screening_ai/)
📌 Role in system

This module conducts AI-driven screening interviews, processes answers, and evaluates candidates in real time.

It handles:

chat-based screening
behavioral analysis
confidence scoring
intent understanding
response evaluation
report generation
⭐ 1. CORE CONVERSATION ENGINE
📄 conversation_engine.py
🎯 Purpose

Main chatbot-like engine that interacts with candidates.

It:

asks questions
processes answers
maintains conversation flow
📥 INPUT
{
  "candidate_id": "C1",
  "message": "I worked as a data analyst in banking sector"
}
📤 OUTPUT
{
  "next_question": "What tools did you use in banking analytics?",
  "context_updated": true
}
🧠 ROLE
Simulates real HR screening interview
Controls conversation flow
⭐ 2. SCORING ENGINE (CORE BRAIN)
📄 scoring_engine.py
🎯 Purpose

Evaluates candidate answers in real time.

It checks:

relevance
correctness
depth of answer
skill alignment
📥 INPUT
{
  "question": "Explain SQL joins",
  "answer": "I used joins to combine tables in projects"
}
📤 OUTPUT
{
  "score": 78,
  "confidence": 0.82,
  "feedback": "Good understanding but lacks depth"
}
🧠 ROLE
Core evaluation engine of screening AI
Feeds ATS + final scoring system
⭐ 3. BEHAVIOR ANALYSIS
📄 behavior_report.py + behavior_rules.py
🎯 PURPOSE

Analyzes candidate behavior:

communication style
hesitation
confidence
clarity
📥 INPUT
Transcript of conversation
📤 OUTPUT
{
  "confidence_level": "medium",
  "communication_score": 72,
  "behavior_risk": "low"
}
🧠 ROLE
Soft skills evaluation
HR personality insights
⭐ 4. CONFIDENCE ENGINE
📄 confidence_engine.py
🎯 PURPOSE

Measures how confident candidate sounds in answers.

📥 INPUT
Candidate response text
📤 OUTPUT
{
  "confidence_score": 0.75
}
🧠 ROLE
Detects hesitation
Speech/text confidence analysis
⭐ 5. INTENT + LANGUAGE PROCESSING
📄 intent_classifier.py + language_detector.py
🎯 PURPOSE

Understands:

what candidate actually means
language of response
📥 INPUT
"I kinda worked with SQL stuff"
📤 OUTPUT
{
  "intent": "SQL experience",
  "language": "en"
}
🧠 ROLE
Improves NLP understanding
Used by scoring engine
⭐ 6. SENTIMENT ENGINE
📄 sentiment_engine.py
🎯 PURPOSE

Detects emotional tone:

positive
neutral
negative
📥 INPUT
"I am not very confident about this topic"
📤 OUTPUT
{
  "sentiment": "negative",
  "stress_level": "high"
}
⭐ 7. SPEECH / TRANSCRIPT PIPELINE
Files:
stt_processor.py
transcript_cleaner.py
transcript_normalizer.py
transcript_processor.py
🎯 PURPOSE

Converts raw speech/text into clean structured format.

📥 INPUT
Messy interview transcript
📤 OUTPUT
{
  "clean_text": "Candidate explained SQL joins clearly"
}
⭐ 8. REPORT GENERATION
📄 report_generator.py + report_exporter.py
🎯 PURPOSE

Creates final screening report for each candidate.

📤 OUTPUT
{
  "candidate_id": "C1",
  "final_screening_score": 82,
  "strengths": ["SQL", "communication"],
  "weaknesses": ["depth in explanation"]
}
🧠 FULL SCREENING FLOW
Candidate Chat Input
        ↓
conversation_engine.py
        ↓
intent_classifier.py
        ↓
scoring_engine.py
        ↓
behavior + confidence + sentiment engines
        ↓
transcript processing
        ↓
report_generator.py
        ↓
Final Screening Report
🎯 PURPOSE OF screening_ai/

This module handles:

✔ AI interviewer simulation
✔ Real-time answer evaluation
✔ Behavioral analysis
✔ Confidence detection
✔ Conversation flow control
✔ Screening report generation

22,security
-----------------------------------------------


Security Module (security/)
📌 Role in system

This module protects sensitive candidate and system data from unauthorized access, misuse, and leaks.

It handles:

authentication / access control
encryption
consent management
audit tracking
data retention rules
⭐ 1. ACCESS CONTROL
📄 access_control.py
🎯 Purpose

Controls who can access what inside the system.

Example roles:

Admin
HR
AI system
Viewer
📥 INPUT
{
  "user_role": "HR",
  "action": "view_candidate_data"
}
📤 OUTPUT
{
  "allowed": true
}
🧠 ROLE
Prevents unauthorized access
Role-based permissions
⭐ 2. ENCRYPTION SYSTEM
📄 encryption.py
🎯 Purpose

Protects sensitive data like:

resumes
candidate info
interview transcripts
📥 INPUT
Sensitive candidate data
📤 OUTPUT
Encrypted string (ciphertext)
🧠 ROLE
Data privacy protection
Secure storage + transmission
⭐ 3. AUDIT LOG (SECURITY VERSION)
📄 audit_log.py
🎯 Purpose

Tracks all sensitive system actions for security compliance.

📥 INPUT
{
  "user": "admin",
  "action": "deleted_candidate_record"
}
📤 OUTPUT
{
  "logged": true,
  "timestamp": "2026-06-28T21:00:00"
}
🧠 ROLE
Security traceability
Compliance logging (GDPR-style tracking)
⭐ 4. CONSENT MANAGEMENT
📄 consent.py
🎯 PURPOSE

Checks if candidate has allowed data usage.

📥 INPUT
{
  "candidate_id": "C1"
}
📤 OUTPUT
{
  "consent_given": true
}
🧠 ROLE
Legal compliance (data usage permission)
Privacy protection
⭐ 5. DATA RETENTION POLICY
📄 retention.py
🎯 PURPOSE

Controls how long data is stored.

Example:

delete after 90 days
archive after interview
📥 INPUT
{
  "candidate_id": "C1",
  "created_at": "2026-01-01"
}
📤 OUTPUT
{
  "action": "archive"
}
🧠 ROLE
Data lifecycle management
Storage optimization
Legal compliance
🧠 OVERALL SECURITY FLOW
User Request
     ↓
access_control.py (permission check)
     ↓
consent.py (legal check)
     ↓
encryption.py (protect data)
     ↓
audit_log.py (track action)
     ↓
retention.py (data lifecycle)
🎯 PURPOSE OF security/

This module ensures:

✔ Role-based access control
✔ Data encryption
✔ Legal compliance (consent)
✔ Audit tracking
✔ Data lifecycle management
✔ Enterprise-grade security

23,technical_ai
-------------------------------------------


Technical Interview Module (technical_ai/)
📌 Role in system

This module generates technical questions, evaluates answers, adjusts difficulty, and produces final technical scores.

It simulates:

senior technical interviewer
exam question setter
grading system
⭐ 1. CORE PIPELINE
📄 technical_pipeline.py
🎯 Purpose

This is the main orchestrator of technical interviews.

It manages:

question selection
difficulty adjustment
scoring flow
result aggregation
📥 INPUT
{
  "candidate_id": "C1",
  "skill": "Python",
  "level": "intermediate"
}
📤 OUTPUT
{
  "question_set": ["Q1", "Q2"],
  "difficulty": "medium"
}
🧠 ROLE
Controls full technical interview flow
Connects all submodules
⭐ 2. QUESTION GENERATION ENGINE
📄 question_generator.py
🎯 PURPOSE

Creates technical questions based on:

skills
difficulty level
job role
📥 INPUT
{
  "skill": "SQL",
  "difficulty": "medium"
}
📤 OUTPUT
{
  "questions": [
    "Explain JOIN types in SQL",
    "What is normalization?"
  ]
}
🧠 ROLE
Dynamic question creation
Core interview content generator
⭐ 3. TECHNICAL SCORING ENGINE
📄 technical_scoring_engine.py
🎯 PURPOSE

Evaluates candidate answers technically.

It checks:

correctness
depth
logic quality
completeness
📥 INPUT
{
  "question": "What is normalization?",
  "answer": "It organizes database to reduce redundancy"
}
📤 OUTPUT
{
  "score": 82,
  "accuracy": 0.85,
  "feedback": "Good explanation but lacks examples"
}
🧠 ROLE
Core technical evaluation engine
Produces final technical score
⭐ 4. DIFFICULTY ENGINE
📄 difficulty_engine.py
🎯 PURPOSE

Adjusts question difficulty dynamically.

📥 INPUT
{
  "candidate_performance": 75
}
📤 OUTPUT
{
  "next_difficulty": "hard"
}
🧠 ROLE
Adaptive interview system
Makes interview dynamic
⭐ 5. QUESTION HIERARCHY
📄 question_hierarchy.json
🎯 PURPOSE

Defines structure of questions:

beginner
intermediate
advanced
🧠 ROLE
Organizes question complexity
Helps generator select correct level
⭐ 6. SKILL BREAKDOWN
📄 skill_breakdown.py
🎯 PURPOSE

Breaks skill into sub-skills.

Example:
Python →

syntax
OOP
data structures
📥 INPUT
Python
📤 OUTPUT
{
  "sub_skills": ["OOP", "DSA", "Syntax"]
}
⭐ 7. RUBRICS SYSTEM
📄 rubrics.py
🎯 PURPOSE

Defines scoring rules.

Example:

correctness = 40%
depth = 30%
clarity = 30%
🧠 ROLE
Standard scoring logic
Ensures fairness
⭐ 8. STATE MANAGER
📄 state_manager.py
🎯 PURPOSE

Tracks interview progress:

current question
answers given
score history
🧠 ROLE
Maintains session memory
Controls interview flow state
⭐ 9. REPORT GENERATOR
📄 report_generator.py
🎯 PURPOSE

Generates final technical interview report.

📤 OUTPUT
{
  "candidate_id": "C1",
  "technical_score": 85,
  "strengths": ["SQL", "Python"],
  "weaknesses": ["system design"]
}
🧠 FULL TECHNICAL FLOW
Candidate Skill Input
        ↓
technical_pipeline.py
        ↓
question_generator.py
        ↓
state_manager.py
        ↓
answer evaluation
        ↓
technical_scoring_engine.py
        ↓
difficulty_engine.py
        ↓
rubrics.py
        ↓
report_generator.py
🎯 PURPOSE OF technical_ai/

This module handles:

✔ Technical interview simulation
✔ Question generation
✔ Adaptive difficulty
✔ Answer evaluation
✔ Skill breakdown
✔ Final technical scoring


24,tests
-------------------------------------------
esting Module (tests/)
📌 Role in system

This module ensures every AI component works correctly, individually and together.

It is responsible for:

unit testing
integration testing
system simulation
load testing
validation of AI pipelines
⭐ 1. FULL SYSTEM SIMULATION
📄 full_simulation.py
🎯 Purpose

Runs the entire AI hiring pipeline end-to-end.

It simulates:

resume → ATS → screening → interview → decision
📥 INPUT
{
  "candidate_profile": "sample resume data"
}
📤 OUTPUT
{
  "final_decision": "Selected",
  "final_score": 84
}
🧠 ROLE
End-to-end system validation
Real-world flow testing
⭐ 2. LIVE DEMO SYSTEM
📄 live_demo.py
🎯 PURPOSE

Runs a real-time demo of the AI system.

📥 INPUT
Candidate resume
Interview responses
📤 OUTPUT
Live scoring
real-time decisions
🧠 ROLE
Showcase system for demo/interview/clients
⭐ 3. LOAD TESTING
📄 load_test.py
🎯 PURPOSE

Checks system performance under heavy usage.

📥 INPUT
1000+ candidate requests
📤 OUTPUT
{
  "avg_response_time": 120ms,
  "success_rate": 99.2%
}
🧠 ROLE
Scalability testing
Production readiness check
⭐ 4. MODULE TESTS (UNIT TESTS)

These test individual components:

Examples:

test_ats.py → ATS engine
test_parser.py → resume parsing
test_behavior.py → behavior analysis
test_integrity.py → fraud detection
test_decision.py → decision engine
📥 INPUT

Small controlled test data:

{
  "input": "sample resume text"
}
📤 OUTPUT
{
  "status": "PASS"
}
🧠 ROLE
Validate each AI module independently
⭐ 5. INTEGRATION TESTING

Examples:

test_integration.py
test_final_system.py
test_unified.py
🎯 PURPOSE

Checks if all modules work together:

Parser → AI Engines → Screening → Technical → Decision
📤 OUTPUT
{
  "system_status": "PASS"
}
⭐ 6. SCREENING & INTERVIEW TESTS

Examples:

test_screening_scoring.py
test_hr_interview.py
test_full_interview.py
🎯 PURPOSE

Validates:

conversation engine
HR AI
scoring engine
⭐ 7. SECURITY & COMPLIANCE TESTS

Examples:

test_security.py
test_compliance.py
🎯 PURPOSE

Checks:

access control
encryption
consent validation
⭐ 8. PERFORMANCE & OPTIMIZATION TESTS

Examples:

test_performance.py
test_memory_demo.py
🎯 PURPOSE

Checks:

speed
memory usage
optimization quality
🧠 FULL TESTING FLOW
Code Written
      ↓
Unit Tests (module level)
      ↓
Integration Tests (system level)
      ↓
Full Simulation (end-to-end)
      ↓
Load Testing (scalability)
      ↓
Live Demo (real-world usage)
🎯 PURPOSE OF tests/

This module ensures:

✔ Every AI module works correctly
✔ System works end-to-end
✔ Performance is stable
✔ Production readiness verified
✔ Bugs are detected early
✔ System reliability guaranteed


