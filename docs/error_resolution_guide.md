# HR Interview AI – Error Resolution & Debugging Guide

## Overview

This document provides troubleshooting procedures, debugging recommendations, and issue resolution strategies for the Zecpath HR Interview AI system.

It helps developers and system administrators quickly identify and resolve common operational problems.

---

# Common Issues and Resolutions

| Issue                            | Possible Cause                    | Recommended Solution                                    |
| -------------------------------- | --------------------------------- | ------------------------------------------------------- |
| No response detected             | Speech-to-Text failure            | Retry STT processing and verify microphone input        |
| Low score anomaly                | Score normalization issue         | Verify scoring weights and normalization logic          |
| API timeout                      | Network delay or server overload  | Increase timeout limits and implement retry logic       |
| Wrong intent detection           | NLP keyword mismatch              | Improve keyword mapping and intent classification rules |
| Missing report data              | Incomplete processing pipeline    | Verify report generation workflow                       |
| Session not found                | Invalid session identifier        | Confirm session creation before report retrieval        |
| Follow-up question not generated | Low-quality answer parsing        | Review Follow-Up Engine thresholds                      |
| Confidence score inconsistency   | Behavioral signal detection error | Validate confidence scoring configuration               |

---

# Debugging Workflow

When an issue occurs, follow the steps below:

### Step 1: Verify API Logs

Check:

* Request logs
* Response logs
* Error logs
* Exception traces

Example:

```text
POST /answer

Status: 200 OK

Response Time: 120 ms
```

---

### Step 2: Validate Input Data

Verify:

* Candidate ID exists
* Session ID is valid
* Question ID is valid
* Answer text is not empty

Example Validation:

```json
{
  "candidate_id": "C101",
  "session_id": "S123",
  "answer": "I have worked on backend systems."
}
```

---

### Step 3: Verify AI Module Outputs

Check outputs from:

* Communication Analyzer
* Confidence Analyzer
* Aptitude Engine
* HR Scoring Engine
* Summary Generator

Ensure values are returned correctly.

Example:

```json
{
  "communication_score": 86.0
}
```

---

### Step 4: Verify Score Ranges

Expected score ranges:

| Module        | Expected Range |
| ------------- | -------------- |
| Communication | 0 – 100        |
| Confidence    | 0 – 100        |
| Aptitude      | 0 – 100        |
| HR Score      | 0 – 100        |
| Final Score   | 0 – 100        |

Investigate values outside these limits.

---

### Step 5: Verify Report Generation

Ensure final report contains:

* Candidate ID
* Individual scores
* Final score
* Hiring decision
* Summary

Example:

```json
{
  "candidate_id": "C101",
  "final_score": 78,
  "decision": "Strong Hire"
}
```

---

# Error Handling Examples

## Invalid Input

```json
{
  "error_code": "INVALID_INPUT",
  "message": "Missing candidate_id",
  "status": 400
}
```

---

## Session Not Found

```json
{
  "error_code": "SESSION_NOT_FOUND",
  "message": "Interview session not found",
  "status": 404
}
```

---

## Internal Server Error

```json
{
  "error_code": "INTERNAL_SERVER_ERROR",
  "message": "Unexpected server error",
  "status": 500
}
```

---

# System Verification Checklist

Before deployment or troubleshooting completion, confirm:

✓ API logs verified

✓ Input data validated

✓ Model outputs checked

✓ Scores normalized

✓ No missing fields

✓ Session creation successful

✓ Report generation successful

✓ Error responses handled correctly

---

# Maintenance Recommendations

* Monitor API response times.
* Maintain detailed application logs.
* Review scoring weights periodically.
* Update NLP keyword dictionaries.
* Validate database backups regularly.
* Perform regression testing after updates.

---

# Conclusion

This guide provides a structured approach to diagnosing and resolving issues within the HR Interview AI system, ensuring reliable operation and easier maintenance.
