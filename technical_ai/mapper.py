import json

def load_role_skills():
    with open("technical_ai/question_hierarchy.json") as f:
        data = json.load(f)
    return data["role_mapping"]