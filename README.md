# SIEMLite

SIEMLite is a lightweight Security Information and Event Management (SIEM) system
written in Python. It parses various log formats, correlates events to detect
suspicious behavior, sends alerts, and provides a minimal web dashboard.

## Features

- Modular event parsers for Windows, Linux, web server, and firewall logs
- Correlation engine with brute force and port scan detectors
- Alerting via email, Slack, or log file
- Simple Flask dashboard to view alerts
- Utilities for timestamp conversion, IP geolocation, and log rotation
- Sample logs and configuration for testing
- Unit tests using pytest

## Setup

1. Clone the repository.
2. Create a virtual environment and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Adjust `config/config.yaml` to match your environment.

## Usage

Run the main script to start processing sample logs:

```bash
python main.py
```

Visit `http://localhost:5000` to view alerts on the dashboard.

## Project Structure

- `main.py` – entry point
- `event_parser/` – log parsers
- `correlation_engine/` – event correlation
- `alerts/` – alerting handlers
- `dashboard/` – Flask web interface
- `tests/` – unit tests
- `docs/` – documentation
- `config/` – YAML configuration
- `sample_logs/` – example logs
- `utils/` – helper utilities
- `logs/` – collected logs and alerts
