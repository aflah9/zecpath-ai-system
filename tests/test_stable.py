from ai_core.stable_system import stable_pipeline


def test_stable_pipeline():

    result = stable_pipeline(

        "C1",

        {

            "ats":120,

            "hr":-10

        }

    )

    assert result["final_score"] <= 100

    assert result["status"] == "stable"

    print("TEST PASSED")


if __name__ == "__main__":

    test_stable_pipeline()