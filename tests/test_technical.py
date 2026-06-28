from technical_ai.technical_scoring_engine import (
    calculate_technical_score
)

from technical_ai.technical_pipeline import (
    technical_pipeline
)


def test_technical():

    text = """
    First I design architecture,
    then optimize for scalability
    because real-world systems
    need performance in production.
    """

    result = calculate_technical_score(
        text,
        True
    )

    print(result)

    pipeline_result = technical_pipeline(
        text,
        "advanced",
        True
    )

    print(pipeline_result)


if __name__ == "__main__":
    test_technical()