def next_state(state):
    if len(state["questions_asked"]) < 2:
        return "conceptual"

    if len(state["questions_asked"]) < 4:
        return "problem_solving"

    if len(state["questions_asked"]) < 6:
        return "scenario"

    return "system_design"