# Transcript Metadata Standards – Zecpath AI

## Core Metadata Fields

| Field Name | Description |
|------------|-------------|
| transcript_id | Unique transcript identifier |
| candidate_id | Unique candidate ID |
| job_id | Associated job ID |
| question_id | Question reference |
| timestamp | Start & end time |
| duration_seconds | Answer duration |
| confidence_score | Speech-to-text accuracy |
| language | Spoken language |
| created_at | Record creation time |

---

## Metadata Design Principles

### Consistency
All transcripts follow the same structure

### Traceability
Each answer linked to question & candidate

### Auditability
Timestamps and confidence tracked

### Scalability
Supports multi-language and multi-round interviews