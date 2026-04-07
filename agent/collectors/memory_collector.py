import psutil
from .base_collector import BaseCollector


class MemoryCollector(BaseCollector):
    def collect(self):
        memory = psutil.virtual_memory()

        return {
            "memory_percent": memory.percent,
            "total_memory": memory.total,
            "available_memory": memory.available
        }