from interview_ai.pipeline import followup_pipeline
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from interview_ai.pipeline import followup_pipeline


def test_followup():

    result = followup_pipeline(
        question="Tell me about your teamwork experience",
        answer="I worked in a team",
        confidence_score=0.6
    )

    print(result)



    