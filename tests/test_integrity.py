from integrity_ai.main import evaluate_integrity


def test_integrity():

    result = evaluate_integrity(
        "C4001",
        {
            "tab_switch": 4,
            "focus_loss": 2,
            "voice_detect": 0,
            "gaze_off": 7
        }
    )

    print(result)

    assert result["integrity_score"] > 0


if __name__ == "__main__":
    test_integrity()