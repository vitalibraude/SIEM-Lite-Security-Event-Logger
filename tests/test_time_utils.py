from datetime import datetime
from utils import to_iso


def test_to_iso():
    ts = datetime(2023, 1, 1, 0, 0, 0)
    assert to_iso(ts) == "2023-01-01T00:00:00"
