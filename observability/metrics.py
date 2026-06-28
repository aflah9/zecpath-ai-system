def calculate_metrics(success, total, response_times):

    success_rate = success / total if total else 0

    avg_latency = (
        sum(response_times) / len(response_times)
        if response_times else 0
    )

    return {
        "success_rate": round(success_rate,2),
        "avg_latency": round(avg_latency,2)
    }