from pathlib import Path
from datetime import datetime


def write_alert(message: str, alerts_file: Path):
    """Append alert message to a file."""
    alerts_file.parent.mkdir(parents=True, exist_ok=True)
    with alerts_file.open("a") as f:
        f.write(f"{datetime.utcnow().isoformat()} {message}\n")
