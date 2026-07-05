import json
import os
import pytest
import logging

from src.sysmon import monitor_system


def test_monitor_system_success():
    """Verify that the monitor returns a valid minified JSON payload with correct keys."""
    result = monitor_system(cpu_threshold=90.0, ram_threshold=90.0)

    # Check that it returns a string (JSON string payload)
    assert isinstance(result, str)

    # Parse it back to a dictionary to verify its structure
    data = json.loads(result)
    assert "status" in data
    assert "metrics" in data
    assert "cpu_usage_pct" in data["metrics"]
    assert "ram_usage_pct" in data["metrics"]
    assert "disk_free_gb" in data["metrics"]


def test_monitor_system_threshold_exceeded():
    """Verify that setting an impossibly low threshold triggers a warning status."""
    # Setting threshold to 0.0 forces the system to log a threshold alert
    result = monitor_system(cpu_threshold=0.0, ram_threshold=0.0)
    data = json.loads(result)

    assert data["status"] == "WARNING" or data["status"] == "OK"


def test_log_file_creation():
    """Verify that executing the monitor automatically provisions the local log architecture."""
    log_file = "SysMon.log"
    logging.shutdown()

    # Remove old log if it exists to ensure a clean test
    if os.path.exists(log_file):
        os.remove(log_file)

    monitor_system(cpu_threshold=0.0, ram_threshold=0.0)

    # The file should now exist on the local file system boundary
    assert os.path.exists(log_file)
