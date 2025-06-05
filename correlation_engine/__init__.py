"""Correlation engine to detect suspicious behavior."""

from . import brute_force, port_scan

DETECTORS = [
    brute_force.detect_brute_force,
    port_scan.detect_port_scan,
]

def correlate(events):
    """Run all detectors on the list of events."""
    alerts = []
    for detector in DETECTORS:
        alerts.extend(detector(events))
    return alerts
