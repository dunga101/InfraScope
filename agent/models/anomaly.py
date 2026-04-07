from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class Anomaly:
    """
    Represents an anomaly detected from telemetry.
    """

    timestamp: str
    hostname: str
    category: str
    severity: str
    source: str
    evidence: Dict[str, Any]
    threshold: Any
    message: str