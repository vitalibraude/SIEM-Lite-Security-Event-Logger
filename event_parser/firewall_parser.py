import re
from datetime import datetime

def parse_line(line: str) -> dict:
    """Parse a firewall log line."""
    match = re.match(r"(?P<timestamp>\S+)\s+(?P<action>\S+)\s+(?P<src_ip>\S+)\s+(?P<dst_ip>\S+)\s+(?P<dst_port>\d+)", line)
    if match:
        data = match.groupdict()
        data["timestamp"] = datetime.fromisoformat(data["timestamp"])  # naive example
        data["event_id"] = data.get("action")
        return data
    return {}
