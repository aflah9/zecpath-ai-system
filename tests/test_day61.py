from observability.logging import log_event
from observability.metrics import calculate_metrics
from observability.alerts import check_alerts
from observability.audit import audit_log


def test_day61():

    log = log_event(
        "ATS",
        "score_generated",
        {
            "candidate":"C101",
            "score":82
        }
    )

    metrics = calculate_metrics(
        success=9,
        total=10,
        response_times=[1.2,1.3,1.4]
    )

    alerts = check_alerts(metrics)

    audit = audit_log(
        "Selected",
        "Decision Engine",
        "C101"
    )

    print(log)
    print(metrics)
    print(alerts)
    print(audit)

    print("\nTEST PASSED")


if __name__ == "__main__":
    test_day61()