from screening_ai.robust_flow import detect_edge_case


def test_missing():
    assert detect_edge_case("", 1.0) == "missing"


def test_poor_audio():
    assert detect_edge_case("hello", 0.4) == "poor_audio"


def test_unclear():
    assert detect_edge_case("um", 1.0) == "unclear"


def test_language_mix():
    assert detect_edge_case("hai chetta", 1.0) == "language_mix"


def test_incomplete():
    assert detect_edge_case("python", 1.0) == "incomplete"


def test_valid():
    assert detect_edge_case(
        "I have 3 years experience in Python",
        1.0
    ) == "valid"