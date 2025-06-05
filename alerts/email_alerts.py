import smtplib
from email.mime.text import MIMEText


def send_email_alert(subject: str, message: str, config: dict):
    """Send an email alert using SMTP."""
    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = config.get("from")
    msg["To"] = config.get("to")
    with smtplib.SMTP(config.get("server", "localhost")) as server:
        server.send_message(msg)
