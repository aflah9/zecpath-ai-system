from interview_ai.communication_engine import (
    calculate_communication_score
)

text = (
    "I have experience in Python "
    "because I worked on backend systems."
)

result = calculate_communication_score(text)

print(result)