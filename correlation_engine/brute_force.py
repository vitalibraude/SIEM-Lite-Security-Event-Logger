from collections import defaultdict
from datetime import datetime, timedelta


def detect_brute_force(events, threshold=5, window_minutes=5):
    """Detect brute force attempts from failed login events."""
    failed_logins = defaultdict(list)
    for evt in events:
        if evt.get("event_id") == "FAILED_LOGIN":
            ip = evt.get("ip") or evt.get("src_ip")
            ts = evt.get("timestamp")
            failed_logins[ip].append(ts)
    alerts = []
    window = timedelta(minutes=window_minutes)
    for ip, times in failed_logins.items():
        times = sorted(times)
        for i in range(len(times)):
            if i + threshold - 1 < len(times) and times[i + threshold - 1] - times[i] <= window:
                alerts.append({"type": "brute_force", "ip": ip, "count": threshold})
                break
    return alerts
