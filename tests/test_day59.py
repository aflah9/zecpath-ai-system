from api.error_handling import retry_request
from api.integration_pipeline import full_integration_pipeline


def test_retry():

    result = retry_request(lambda: 1)

    assert result == 1


def test_pipeline():

    result = full_integration_pipeline({})

    assert result["decision"] == "Selected"

    print("TEST PASSED")


if __name__ == "__main__":

    test_retry()

    test_pipeline()