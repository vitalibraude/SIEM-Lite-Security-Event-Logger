from collections import defaultdict
from datetime import timedelta


def detect_port_scan(events, threshold=10, window_minutes=1):
    """Detect port scanning from connection events."""
    connections = defaultdict(list)
    for evt in events:
        if evt.get("event_id") == "CONNECTION":
            ip = evt.get("src_ip")
            ts = evt.get("timestamp")
            port = evt.get("dst_port")
            connections[ip].append((ts, port))
    alerts = []
    window = timedelta(minutes=window_minutes)
    for ip, entries in connections.items():
        entries = sorted(entries)
        ports = []
        times = []
        for ts, port in entries:
            while times and ts - times[0] > window:
                times.pop(0)
                ports.pop(0)
            if port not in ports:
                ports.append(port)
                times.append(ts)
            if len(ports) >= threshold:
                alerts.append({"type": "port_scan", "ip": ip, "count": len(ports)})
                break
    return alerts
