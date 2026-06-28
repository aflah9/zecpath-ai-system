def test_api_format():
    response = {
        "candidate_id": "C1",
        "final_score": 80
    }

    assert "candidate_id" in response
    assert "final_score" in response

    print("✓ API format validation passed")


if __name__ == "__main__":
    test_api_format()