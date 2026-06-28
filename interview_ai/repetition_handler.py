def avoid_repetition(
    state,
    question_pool
):

    return [
        q
        for q in question_pool
        if not state.is_repeated(q)
    ]