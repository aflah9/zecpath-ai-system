from screening_ai.answer_engine import process_answer
from screening_ai.answer_engine import process_answers_batch

# -----------------------
# Single Answer Test
# -----------------------

answer = "I have 3 years experience in Python and Django"

result = process_answer("Q3", answer)

print("Single Answer Result:")
print(result)

# -----------------------
# Batch Answer Test
# -----------------------

answers = [

    {
        "question_id": "Q1",
        "text": "I have 2 years experience in banking and finance"
    },

    {
        "question_id": "Q2",
        "text": "My skills are Excel, financial analysis and credit analysis"
    },

    {
        "question_id": "Q3",
        "text": "Expected salary is 5 LPA"
    },

    {
        "question_id": "Q4",
        "text": "I can join immediately"
    },

    {
        "question_id": "Q5",
        "text": "Maybe"
    }

]

batch_results = process_answers_batch(answers)

print("\nBatch Results:")

for item in batch_results:
    print(item)