from abc import ABC, abstractmethod
from typing import List
from agent.models.snapshot import Snapshot
from agent.models.anomaly import Anomaly


class BaseDetector(ABC):
    """
    Base class for anomaly detectors.
    """

    @abstractmethod
    def evaluate(self, snapshot: Snapshot) -> List[Anomaly]:
        """
        Evaluate telemetry and return anomalies if detected.
        """
        pass