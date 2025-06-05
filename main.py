import yaml
from pathlib import Path
from event_parser import parse_event
from correlation_engine import correlate
from alerts import alert
from utils import rotate_log

CONFIG_FILE = Path("config/config.yaml")
LOG_DIR = Path("logs")


def load_config():
    with CONFIG_FILE.open() as f:
        return yaml.safe_load(f)


def load_logs():
    events = []
    log_sources = {
        "windows": "sample_logs/windows.log",
        "linux": "sample_logs/linux.log",
        "web": "sample_logs/web.log",
        "firewall": "sample_logs/firewall.log",
    }
    for log_type, path in log_sources.items():
        with open(path) as f:
            for line in f:
                evt = parse_event(log_type, line.strip())
                if evt:
                    events.append(evt)
    return events


def main():
    config = load_config()
    LOG_DIR.mkdir(exist_ok=True)
    rotate_log(Path(config["alerts"]["file"]["path"]))
    events = load_logs()
    alerts = correlate(events)
    for a in alerts:
        alert(str(a), config["alerts"])


if __name__ == "__main__":
    main()
