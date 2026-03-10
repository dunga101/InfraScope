from abc import ABC, abstractmethod
from agent.models.snapshot import Snapshot


class BaseCollector(ABC):
    """
    Base class for all telemetry collectors.
    """

    @abstractmethod
    def collect(self) -> Snapshot:
        """
        Collect telemetry and return a Snapshot.
        """
        pass