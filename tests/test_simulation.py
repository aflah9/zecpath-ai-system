def test_simulation():
    from tests.full_simulation import run_full_simulation

    results = run_full_simulation(10)

    assert len(results) == 10