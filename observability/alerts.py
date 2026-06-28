def check_alerts(metrics):

    alerts=[]

    if metrics["avg_latency"] > 2:
        alerts.append("High latency detected")

    if metrics["success_rate"] < 0.9:
        alerts.append("Low success rate")

    return alerts