from experience_logic import get_experience_level
from question_generator import generate_question

# Test experience mapping
assert get_experience_level(3) == "3-5"

# Test question generation
q = generate_question("JavaScript", "basic")
print("Sample Question:", q)

print("All tests passed")