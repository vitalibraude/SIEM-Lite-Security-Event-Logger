from datetime import datetime

def to_iso(ts: datetime) -> str:
    """Convert datetime to ISO8601 string."""
    return ts.isoformat()
