from abc import ABC, abstractmethod
from agent.models.anomaly import Anomaly


class BaseWriter(ABC):
    """
    Base class for anomaly writers.
    """

    @abstractmethod
    def write(self, anomaly: Anomaly) -> None:
        """
        Persist anomaly record.
        """
        pass