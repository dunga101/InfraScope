from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class Snapshot:
    """
    Represents telemetry collected from a system component.
    """

    timestamp: str
    hostname: str
    collector: str
    metrics: Dict[str, Any]