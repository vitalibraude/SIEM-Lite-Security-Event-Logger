from pathlib import Path
from datetime import datetime


def rotate_log(log_file: Path, max_size: int = 10_000):
    """Rotate log file if it exceeds max_size in bytes."""
    if log_file.exists() and log_file.stat().st_size > max_size:
        timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
        rotated = log_file.with_suffix(f".{timestamp}.log")
        log_file.rename(rotated)
        log_file.touch()
        return rotated
    return None
