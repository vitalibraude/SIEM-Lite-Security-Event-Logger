from datetime import datetime
from correlation_engine.brute_force import detect_brute_force


def test_brute_force_detection():
    events = [
        {"event_id": "FAILED_LOGIN", "ip": "1.1.1.1", "timestamp": datetime(2023, 1, 1, 0, 0, i)}
        for i in range(5)
    ]
    alerts = detect_brute_force(events, threshold=5, window_minutes=5)
    assert alerts and alerts[0]["type"] == "brute_force"
