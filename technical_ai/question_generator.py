import random

QUESTION_BANK = {
    "Excel": {
        "basic": [
            "What is Excel used for in credit analysis?",
            "Explain basic formulas like SUM and AVERAGE."
        ],
        "intermediate": [
            "How would you use VLOOKUP or XLOOKUP in credit risk reporting?",
            "How do pivot tables help in financial analysis?"
        ],
        "advanced": [
            "Design an automated Excel model for credit scoring and risk classification."
        ]
    },

    "Financial_Analysis": {
        "basic": [
            "What is credit analysis?",
            "What is a credit score?"
        ],
        "intermediate": [
            "How do you analyze a company's financial statements for lending decisions?",
            "What ratios are important in credit risk assessment?"
        ],
        "advanced": [
            "How would you build a credit risk evaluation model for enterprise lending?"
        ]
    },

    "Risk_Assessment": {
        "basic": [
            "What is credit risk?",
            "What is default risk?"
        ],
        "intermediate": [
            "How do banks reduce credit risk?",
            "What is probability of default (PD)?"
        ],
        "advanced": [
            "Design a risk scoring system for loan approval in a fintech platform."
        ]
    },

    "Data_Analysis": {
        "basic": [
            "What is data analysis in finance?",
            "What is a dataset?"
        ],
        "intermediate": [
            "How do you clean financial data before credit evaluation?",
            "What metrics do you use for borrower profiling?"
        ],
        "advanced": [
            "How would you build a predictive model for loan default prediction?"
        ]
    },

    "Accounting": {
        "basic": [
            "What is an asset and liability?",
            "What is a balance sheet?"
        ],
        "intermediate": [
            "How does cash flow affect credit decisions?",
            "What is EBITDA?"
        ],
        "advanced": [
            "How would you evaluate financial health of a company using accounting data?"
        ]
    },

    "Excel_Modeling": {
        "basic": [
            "What is a spreadsheet model?"
        ],
        "intermediate": [
            "How do you structure a financial model for credit analysis?"
        ],
        "advanced": [
            "Design a dynamic credit underwriting model using Excel + automation."
        ]
    }
}


def generate_question(skill, difficulty):
    return random.choice(
        QUESTION_BANK.get(skill, {}).get(
            difficulty,
            ["No question available for this skill and difficulty level"]
        )
    )