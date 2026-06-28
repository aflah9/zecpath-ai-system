from machine_test.pipeline import machine_test_pipeline


def test_machine():

    candidate_data = {
        "candidate_id": "C5001",
        "task_id": "T101",

        "code_snapshot":
        "def add(a,b):\n    return a+b",

        "execution_results": {
            "passed": 8,
            "total": 10,
            "runtime": 1.2
        },

        "attempts": 2,
        "time_taken": 25
    }

    result = machine_test_pipeline(candidate_data)

    print(result)


if __name__ == "__main__":
    test_machine()