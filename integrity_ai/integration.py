def combined_risk(
    behavior_score,
    integrity_score
):

    final = (
        behavior_score * 0.4 +
        integrity_score * 0.6
    )

    return round(final, 2)


