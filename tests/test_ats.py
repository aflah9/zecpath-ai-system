import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ats_engine.ats_scorer import ATSScorer

def test_ats_score():
    scorer = ATSScorer()
    score = scorer.calculate_score({}, {})
    assert score == 75