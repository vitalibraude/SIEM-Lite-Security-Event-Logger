import re
from datetime import datetime

def parse_line(line: str) -> dict:
    """Parse a web server log line (combined log format)."""
    pattern = (
        r"(?P<ip>\S+)\s+-\s+-\s+\[(?P<timestamp>[^\]]+)\]\s+\"\S+\s+"
        r"(?P<url>\S+)\s+\S+\"\s+(?P<status>\d+)\s+(?P<size>\d+)"
    )
    match = re.match(pattern, line)
    if match:
        data = match.groupdict()
        data["timestamp"] = datetime.strptime(data["timestamp"], "%d/%b/%Y:%H:%M:%S %z")
        data["event_id"] = data.get("status")
        return data
    return {}
