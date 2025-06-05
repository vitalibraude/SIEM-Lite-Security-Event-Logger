from event_parser import parse_event


def test_parse_windows_event():
    line = "2023-01-01T00:00:01 4625 FAILED_LOGIN"
    evt = parse_event("windows", line)
    assert evt["event_id"] == "4625"
