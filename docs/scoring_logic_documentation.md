# HR Interview AI – Scoring Logic Documentation

## Overview

This document describes the scoring mechanisms used by the Zecpath HR Interview AI system. The scoring engine combines communication analysis, confidence assessment, HR evaluation, aptitude assessment, and unified hiring calculations to generate final candidate recommendations.

---

# 1. Communication Score

## Purpose

Evaluate the quality of candidate communication during interview responses.

### Factors Evaluated

| Factor     | Weight |
| ---------- | ------ |
| Fluency    | 25%    |
| Grammar    | 20%    |
| Vocabulary | 20%    |
| Clarity    | 20%    |
| Structure  | 15%    |

### Formula

Communication Score =
(Fluency × 25) +
(Grammar × 20) +
(Vocabulary × 20) +
(Clarity × 20) +
(Structure × 15)

### Sample Output


Compliance Test Passed                               python -m tests.run_communicatione>
{'communication_score': 86.0, 'breakdown': {'fluency': 0.6, 'grammar': 1.0, 'vocabulary': 1.0, 'clarity': 0.7, 'structure': 1.0, 'penalty': 0.0}}
(venv) PS C:\Users\safeer\Desktop\zecpath-ai-system> 
---

# 2. Confidence Score

## Purpose

Measure candidate confidence and behavioral signals.

### Factors Evaluated

| Factor      | Weight |
| ----------- | ------ |
| Hesitation  | 40%    |
| Repetition  | 20%    |
| Uncertainty | 20%    |
| Sentiment   | 20%    |

### Formula

Confidence Score =
(Hesitation × 40) +
(Repetition × 20) +
(Uncertainty × 20) +
(Sentiment × 20)

### Sample Output

```json
(venv) PS C:\Users\safeer\Desktop\zecpath-ai-system> python -m tests.test_confidence
{'confidence': {'confidence_score': 75.0, 'signals': {'repeat': 0.7, 'hesitation': 1.0, 'uncertainty': 0.3, 'pause': 1.0}}, 'sentiment': {'sentiment': 'Positive', 'sentiment_score': 0.2}, 'stress_score': 0.7, 'contradiction': True, 'behavioral_score': 62.5}
(venv) PS C:\Users\safeer\Desktop\zecpath-ai-system> 
---

# 3. HR Interview Score

## Purpose

Evaluate candidate suitability from HR interview responses.

### Formula

HR Score =
(Relevance × Weight) +
(Communication × Weight) +
(Confidence × Weight) +
(Consistency × Weight)

### Evaluation Factors

* Relevance of answer
* Communication quality
* Confidence level
* Consistency across responses

### Sample Output


```(venv) PS C:\Users\safeer\Desktop\zecpath-ai-system> python -m tests.test_hr_scoring
{'hr_score': 88.5, 'decision': 'Strong Hire', 'details': [{'question_id': 'Q1', 'scores': {'relevance': 0.9, 'communication': 0.85, 'confidence': 0.8, 'consistency': 1.0}, 'final_score': 88.5}], 'summary': {'avg_relevance': 0.9, 'avg_communication': 0.85, 'avg_confidence': 0.8, 'avg_consistency': 1.0}}
(venv) PS C:\Users\safeer\Desktop\zecpath-ai-system> 

---

# 4. Aptitude Score

## Purpose

Evaluate logical reasoning and problem-solving abilities.

### Evaluation Areas

* Logical Reasoning
* Problem Solving
* Decision Making

### Sample Output

```json
(venv) PS C:\Users\safeer\Desktop\zecpath-ai-system> python -m tests.test_aptitude
{'aptitude_score': 91.0, 'details': {'aptitude_score': 100.0, 'breakdown': {'structure': 1.0, 'problem_solving': 1.0, 'decision_making': 1.0}}, 'scenario_score': 0.7}
(venv) PS C:\Users\safeer\Desktop\zecpath-ai-system> 
```

---

# 5. Unified Hiring Score

## Purpose

Generate a final hiring recommendation using all evaluation stages.

### Formula

Final Score =
(ATS × 0.30) +
(Screening × 0.30) +
(HR × 0.40)

### Weight Distribution

| Component       | Weight |
| --------------- | ------ |
| ATS Score       | 30%    |
| Screening Score | 30%    |
| HR Score        | 40%    |

### Sample Output

```json
python -m tests.test_unified

====================================================================== 
UNIFIED SCORING ENGINE TEST
====================================================================== 

Candidate ID: C101
--------------------------------------------------
Final Score : 88.3
Decision    : Hire
Fit         : Excellent Fit
Fit %       : 88.3
Weights     : {'ats': 0.4, 'screening': 0.3, 'hr': 0.3}

Candidate ID: C102
--------------------------------------------------
Final Score : 62.05
Decision    : Consider
Fit         : Moderate Fit
Fit %       : 62.05
Weights     : {'ats': 0.25, 'screening': 0.35, 'hr': 0.4}

Candidate ID: C103
--------------------------------------------------
Final Score : 45.0
Decision    : Reject
Fit         : Low Fit
Fit %       : 45.0
Weights     : {'ats': 0.2, 'screening': 0.3, 'hr': 0.5}

====================================================================== 
ALL TESTS PASSED
====================================================================== 
(venv) PS C:\Users\safeer\Desktop\zecpath-ai-system> 
```

---

# Hiring Decision Thresholds

| Score Range | Decision    |
| ----------- | ----------- |
| 85 - 100    | Strong Hire |
| 70 - 84     | Hire        |
| 55 - 69     | Consider    |
| Below 55    | Reject      |

---

# Conclusion

The scoring framework ensures consistent candidate evaluation by combining communication quality, behavioral analysis, aptitude assessment, and HR interview performance into a unified hiring score.
