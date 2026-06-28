def evaluate_answer(answer, question=""):

    answer = answer.lower()

    finance_keywords = [
        "risk", "credit", "loan", "borrower",
        "repayment", "default", "score", "bank"
    ]

    keyword_hits = sum(1 for k in finance_keywords if k in answer)

    if keyword_hits >= 3:
        return "good"
    elif keyword_hits == 2:
        return "average"
    else:
        return "poor"