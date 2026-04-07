import psutil

from agent.collectors.base_collector import BaseCollector


class DiskCollector(BaseCollector):
    def collect(self):
        disk = psutil.disk_usage("/")

        return {
            "total_bytes": disk.total,
            "used_bytes": disk.used,
            "free_bytes": disk.free,
            "used_percent": disk.percent,
        }