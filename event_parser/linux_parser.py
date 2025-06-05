import re
from datetime import datetime

def parse_line(line: str) -> dict:
    """Parse a Linux syslog line."""
    match = re.match(r"(?P<timestamp>\w+\s+\d+\s+\S+)\s+(?P<message>.+)", line)
    if match:
        data = match.groupdict()
        data["timestamp"] = datetime.strptime(data["timestamp"], "%b %d %H:%M:%S")
        data["event_id"] = None
        return data
    return {}
