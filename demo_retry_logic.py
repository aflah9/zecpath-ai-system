from screening_ai.robust_flow import detect_edge_case
from screening_ai.error_framework import get_error_response
from screening_ai.fallback_handler import fallback_strategy

answer = "um"
confidence = 0.4
retry_count = 1

issue = detect_edge_case(answer, confidence)

print("Issue:", issue)

response = get_error_response(issue)

print("AI:", response)

action = fallback_strategy(issue, retry_count)

print("Next Action:", action)