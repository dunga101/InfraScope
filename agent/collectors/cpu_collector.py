"""CPU telemetry collector for InfraScope."""

from __future__ import annotations

import logging
import time
from typing import Any, Dict

import psutil


class CPUCollector:
    """Collects CPU telemetry snapshots."""

    def __init__(self) -> None:
        self._logger = logging.getLogger(__name__)

    def collect(self) -> Dict[str, Any]:
        """Collect current CPU metrics as a simple snapshot dictionary."""
        timestamp = time.time()

        try:
            cpu_percent = float(psutil.cpu_percent(interval=None))
            cpu_cores = psutil.cpu_count(logical=True) or 0

            return {
                "cpu_percent": cpu_percent,
                "cpu_cores": int(cpu_cores),
                "timestamp": timestamp,
            }
        except Exception as exc:  # pragma: no cover - defensive fallback
            self._logger.exception("CPU telemetry collection failed: %s", exc)
            return {
                "cpu_percent": 0.0,
                "cpu_cores": 0,
                "timestamp": timestamp,
            }
