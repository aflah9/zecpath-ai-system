# utils/bias_check.py

PROTECTED_FIELDS = [
    "gender",
    "age",
    "religion",
    "ethnicity",
    "nationality",
    "race"
]

def check_bias_usage(scoring_input):
    for field in PROTECTED_FIELDS:
        if field in scoring_input:
            print(f"Warning: {field} detected")