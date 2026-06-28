# Zecpath HR Interview AI - API Specification

## Base URL

```text
https://api.zecpath.ai/v1/hr-interview
```

---

# 1. Start Interview

### Endpoint

```http
POST /start
```

### Description

Starts a new HR interview session and generates the initial interview questions.

### Request

```json
{
  "candidate_id": "C101",
  "job_id": "J501",
  "role_type": "technical",
  "experience_level": "fresher"
}
```

### Response

```json
{
  "session_id": "S123",
  "questions": [
    "Tell me about yourself",
    "What are your strengths?"
  ]
}
```

---

# 2. Submit Answer

### Endpoint

```http
POST /answer
```

### Description

Submits a candidate answer and returns a follow-up question and next interview question.

### Request

```json
{
  "session_id": "S123",
  "question_id": "Q1",
  "answer": "I have experience in Python...",
  "duration": 6
}
```

### Response

```json
{
  "follow_up": "Can you elaborate more?",
  "next_question": "Describe your teamwork experience"
}
```

---

# 3. Get Final Report

### Endpoint

```http
GET /report/{session_id}
```

### Description

Returns the final evaluation report for the completed interview.

### Response

```json
{
  "candidate_id": "C101",
  "final_score": 78,
  "decision": "Strong Hire",
  "summary": {
    "strengths": [
      "Good communication"
    ],
    "weaknesses": [
      "Minor hesitation"
    ]
  }
}
```

---

# Error Response Format

```json
{
  "error_code": "INVALID_INPUT",
  "message": "Missing candidate_id",
  "status": 400
}
```
# Error Handling

## Overview

The HR Interview AI API uses a standardized error response format to ensure consistent communication between clients and backend services.

### Standard Error Format

```json
{
  "error_code": "ERROR_IDENTIFIER",
  "message": "Human readable message",
  "status": 400
}
```

### Fields

| Field      | Type    | Description             |
| ---------- | ------- | ----------------------- |
| error_code | String  | Unique error identifier |
| message    | String  | Error description       |
| status     | Integer | HTTP status code        |

---

# Common Error Responses

## 1. Invalid Input

### Description

Returned when a required field is missing or invalid.

### Example

```json
{
  "error_code": "INVALID_INPUT",
  "message": "Missing candidate_id",
  "status": 400
}
```

### Possible Causes

* Missing candidate_id
* Missing session_id
* Empty answer field
* Invalid request payload

### Resolution

* Validate request body before submission.
* Ensure all mandatory fields are provided.

---

## 2. Session Not Found

### Description

Returned when the requested interview session does not exist.

### Example

```json
{
  "error_code": "SESSION_NOT_FOUND",
  "message": "Session not found",
  "status": 404
}
```

### Possible Causes

* Invalid session ID
* Expired interview session
* Session deleted from database

### Resolution

* Verify session ID.
* Create a new interview session if necessary.

---

## 3. Internal Server Error

### Description

Returned when an unexpected server-side error occurs.

### Example

```json
{
  "error_code": "INTERNAL_SERVER_ERROR",
  "message": "Unexpected server error",
  "status": 500
}
```

### Possible Causes

* Database connectivity issues
* AI processing failures
* Unhandled application exceptions

### Resolution

* Review application logs.
* Check database connectivity.
* Verify AI service availability.

---

# HTTP Status Codes Used

| Status Code | Meaning               |
| ----------- | --------------------- |
| 200         | Request successful    |
| 400         | Invalid request       |
| 404         | Resource not found    |
| 500         | Internal server error |

---

# Error Handling Best Practices

* Always validate input before API submission.
* Handle HTTP error responses gracefully.
* Log all failed API requests.
* Display meaningful error messages to users.
* Implement retry logic for temporary failures.
