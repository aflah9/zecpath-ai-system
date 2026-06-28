from interview_ai.aptitude_pipeline import (
    aptitude_pipeline
)


def test_aptitude():

    text = """
    First I analyze the problem,
    then I plan a solution,
    finally I execute it.
    """

    result = aptitude_pipeline(
        text,
        "deadline_pressure"
    )

    print(result)


if __name__ == "__main__":
    test_aptitude()