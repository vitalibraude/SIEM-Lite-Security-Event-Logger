from flask import Flask, render_template_string
from pathlib import Path

app = Flask(__name__)
ALERTS_FILE = Path("logs/alerts.log")


@app.route("/")
def index():
    if ALERTS_FILE.exists():
        alerts = ALERTS_FILE.read_text().splitlines()
    else:
        alerts = []
    return render_template_string(
        """<h1>SIEMLite Alerts</h1><pre>{{ alerts|join('\n') }}</pre>""",
        alerts=alerts,
    )


if __name__ == "__main__":
    app.run(debug=True)
