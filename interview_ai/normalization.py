def normalize_score(
        score,
        min_val=0,
        max_val=100):

    normalized = (
        score - min_val
    ) / (
        max_val - min_val
    )

    return round(
        normalized * 100,
        2
    )