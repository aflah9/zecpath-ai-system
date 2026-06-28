from interview_ai.question_generator import generate_questions

questions = generate_questions(
    role_type="technical",
    experience_level="experienced"
)

print("\n=== HR Interview Questions ===\n")

for i, q in enumerate(questions, start=1):
    print(f"Q{i}: {q}")