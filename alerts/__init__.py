"""Alerting utilities."""

from pathlib import Path
from . import email_alerts, slack_alerts, file_alerts


def alert(message: str, config: dict):
    """Send alert via configured channels."""
    if "email" in config:
        email_alerts.send_email_alert("SIEMLite Alert", message, config["email"])
    if "slack" in config:
        slack_alerts.send_slack_alert(message, config["slack"]["webhook"])
    if "file" in config:
        alerts_path = Path(config["file"].get("path", "logs/alerts.log"))
        file_alerts.write_alert(message, alerts_path)
