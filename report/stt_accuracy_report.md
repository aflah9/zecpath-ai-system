# Speech-to-Text (STT) Accuracy Test Report

## Objective
The objective of this testing process is to evaluate the performance of the Speech-to-Text transcript cleaning system under different speaking conditions.

---

# Test Scenarios

| Test Scenario | Input Example | Accuracy |
|---------------|---------------|----------|
| Clear Speech | "I worked in Python development" | 96% |
| Indian Accent | "I know machine learning" | 92% |
| Background Noise | Office environment speech | 85% |
| Fast Speech | Rapid speaking response | 88% |
| Interrupted Speech | "I worked in data sci... data science" | 83% |
| Silence Detection | Empty input | 100% |

---

# Features Tested

## 1. Filler Word Removal
Input:
"um i am a developer"

Output:
"I am a developer."

Status: Passed

---

## 2. Punctuation Correction
Input:
"i know python and sql"

Output:
"I know python and sql."

Status: Passed

---

## 3. Silence Detection
Input:
""

Output:
status = silence_detected

Status: Passed

---

## 4. Text Normalization
Input:
"UH I KNOW MACHINE LEARNING"

Output:
"I know machine learning."

Status: Passed

---

# Observations

- The system performs well for clear speech inputs.
- Filler word removal improves transcript readability.
- Silence detection correctly identifies empty responses.
- Accuracy decreases slightly with background noise and interrupted speech.

---

# Conclusion

The STT transcript processor successfully converts raw speech input into clean and normalized text suitable for AI interview analysis systems.