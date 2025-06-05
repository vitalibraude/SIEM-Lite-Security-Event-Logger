import re
from datetime import datetime

def parse_line(line: str) -> dict:
    """Parse a Windows event log line."""
    match = re.match(r"(?P<timestamp>\S+)\s+(?P<event_id>\d+)\s+(?P<message>.+)", line)
    if match:
        data = match.groupdict()
        data["timestamp"] = datetime.fromisoformat(data["timestamp"])  # naive example
        return data
    return {}
