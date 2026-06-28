import json


def load_questions(file_path):
    with open(file_path, "r") as f:
        return json.load(f)


questions = load_questions("data/hr_screening_dataset.json")

print(questions)