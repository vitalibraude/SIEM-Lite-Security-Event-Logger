import requests


def send_slack_alert(message: str, webhook_url: str):
    """Send an alert message to Slack via webhook."""
    payload = {"text": message}
    requests.post(webhook_url, json=payload)
