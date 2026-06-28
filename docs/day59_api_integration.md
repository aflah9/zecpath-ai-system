Zecpath AI Integration Architecture
Objective

Define how every AI module communicates with backend services, databases and external systems.

Overall Architecture
Frontend (React/Web)

        │

        ▼

Backend (FastAPI / Django)

        │

──────────────────────────────────────

Resume Parser API

ATS Scoring API

Screening AI API

Interview AI API

Technical AI API

Machine Test API

Decision AI API

──────────────────────────────────────

        │

        ▼

Database

(PostgreSQL / MongoDB)

        │

        ▼

Logs

Reports

PDF Storage
Backend Flow
Resume Upload

↓

Resume Parser

↓

ATS Scoring

↓

Screening AI

↓

Interview AI

↓

Technical AI

↓

Machine Test

↓

Decision Engine

↓

Database

↓

Report Generator

↓

Frontend
Why this architecture?
Independent AI modules
Easy maintenance
Easy deployment
Better scalability
Reusable APIs


#--------------------------------------------



Async

Used for

Resume Parsing
ATS Scoring
Report Generation

Flow

Request

↓

Queue

↓

Worker

↓

Database

↓

Callback
Sync

Used for

Interview AI
Technical Interview
Live Feedback

Flow

Request

↓

AI

↓

Immediate Response


#----------------------------------

Authentication Section

Add

JWT Authentication

OAuth

HTTPS

Rate Limiting

Role Based Access

Input Validation

Audit Logging