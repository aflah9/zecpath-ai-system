# tests/test_system.py

import sys
import os

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from screening_ai.report_generator import generate_screening_report


def test_system():

    report = generate_screening_report(
        "C1",
        "J1",
        [],
        [],
        []
    )

    assert report is not None

    print("System Test Passed")