# HR Interview AI Developer Handbook – Zecpath

## Overview

This handbook provides developers, integrators, and maintainers with the information required to understand, integrate, deploy, and troubleshoot the Zecpath HR Interview AI System.

The handbook serves as a central reference for architecture, APIs, data models, scoring logic, and integration procedures.

---

# 1. Architecture Overview

The HR Interview AI system is designed as a modular architecture where each AI component performs a specific responsibility.

## High-Level Architecture

```text
Frontend (Web/App)
        ↓
Backend API Layer
        ↓

Question Generator
Conversation Engine
Follow-Up Engine
Answer Understanding Engine
Communication Analyzer
Confidence & Behavior Analyzer
HR Scoring Engine
Aptitude Engine
Summary Generator

        ↓

Database / Storage
```

## Data Flow

```text
User Input (Voice/Text)
        ↓
Speech-to-Text
        ↓
Answer Processing
        ↓
AI Evaluation
(Communication + Confidence + Aptitude)
        ↓
HR Scoring
        ↓
Summary Generation
        ↓
Final Report
        ↓
Frontend Dashboard
```

For detailed architecture information, refer to:

```text
docs/architecture.md
```

---

# 2. API Reference

## Base URL

```text
https://api.zecpath.ai/v1/hr-interview
```

### Start Interview

```http
POST /start
```

Purpose:

Start a new interview session and generate questions.

---

### Submit Answer

```http
POST /answer
```

Purpose:

Submit candidate responses and receive follow-up questions.

---

### Get Final Report

```http
GET /report/{session_id}
```

Purpose:

Retrieve interview results and hiring recommendations.

For complete request and response examples, refer to:

```text
docs/api_specification.md
```

---

# 3. Data Models

The HR Interview AI uses standardized JSON objects across all modules.

## Candidate Object

```json
{
  "candidate_id": "C101",
  "name": "John Doe"
}
```

## Answer Object

```json
{
  "question_id": "Q1",
  "answer_text": "I worked on backend systems",
  "intent": "experience",
  "skills": ["Python"],
  "confidence_score": 80,
  "communication_score": 75
}
```

## Report Object

```json
{
  "candidate_id": "C101",
  "scores": {
    "ats": 75,
    "screening": 70,
    "hr": 80
  },
  "final_score": 77,
  "decision": "Hire"
}
```

For additional models and field descriptions, refer to:

```text
docs/data_formats.md
```

---

# 4. Scoring Logic

The HR Interview AI combines multiple evaluation engines to generate hiring recommendations.

## Communication Score

```text
Fluency      25%
Grammar      20%
Vocabulary   20%
Clarity      20%
Structure    15%
```

## Confidence Score

```text
Hesitation    40%
Repetition    20%
Uncertainty   20%
Sentiment     20%
```

## HR Score Formula

```text
HR Score =
(Relevance × Weight)
+
(Communication × Weight)
+
(Confidence × Weight)
+
(Consistency × Weight)
```

## Final Unified Score Formula

```text
Final Score =
(ATS × 0.3)
+
(Screening × 0.3)
+
(HR × 0.4)
```

For detailed formulas and sample outputs, refer to:

```text
docs/scoring_logic_documentation.md
```

---

# 5. Integration Steps

Follow these steps to integrate the HR Interview AI into external systems.

## Interview Workflow

### Step 1

Call:

```http
POST /start
```

Receive interview session information and questions.

---

### Step 2

Display questions to candidate.

---

### Step 3

Capture candidate responses using text or speech input.

---

### Step 4

Send responses using:

```http
POST /answer
```

---

### Step 5

Receive follow-up questions and continue interview flow.

---

### Step 6

When interview is complete, call:

```http
GET /report/{session_id}
```

---

### Step 7

Display final report and hiring recommendation in dashboard.

---

# 6. Tech Stack

## Backend

```text
Python
FastAPI
```

## Artificial Intelligence Layer

```text
Natural Language Processing (NLP)

Rule-Based Logic

Machine Learning Models
```

## Database Layer

```text
PostgreSQL

MongoDB
```

---

# Advantages

* Modular architecture
* Easy API integration
* Scalable design
* Consistent scoring framework
* Structured reporting

---

# Limitations

* Requires backend API deployment
* Some modules use rule-based evaluation
* Performance depends on transcript quality

---

# Future Improvements

* Developer SDK
* GraphQL APIs
* Real-time streaming interviews
* Advanced behavioral analytics
* Multi-language interview support

---

# Related Documentation

```text
docs/architecture.md

docs/api_specification.md

docs/data_formats.md

docs/scoring_logic_documentation.md

docs/troubleshooting.md
```

---

# Conclusion

The Zecpath HR Interview AI provides a complete framework for conducting automated interviews, evaluating candidates, generating reports, and supporting hiring decisions through a scalable API-driven architecture.
