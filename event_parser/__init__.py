"""Event parser package."""

from . import windows_parser, linux_parser, webserver_parser, firewall_parser

PARSERS = {
    "windows": windows_parser.parse_line,
    "linux": linux_parser.parse_line,
    "web": webserver_parser.parse_line,
    "firewall": firewall_parser.parse_line,
}

def parse_event(log_type: str, line: str) -> dict:
    """Dispatch line to appropriate parser."""
    parser = PARSERS.get(log_type)
    if parser:
        return parser(line)
    raise ValueError(f"Unknown log type: {log_type}")
