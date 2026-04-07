from agent.collectors.cpu_collector import CPUCollector
from agent.collectors.memory_collector import MemoryCollector
from agent.collectors.disk_collector import DiskCollector

from agent.writers.json_writer import JsonWriter


def run_once():
    collectors = [
        CPUCollector(),
        MemoryCollector(),
        DiskCollector(),
    ]

    writer = JsonWriter()

    all_data = {}

    for collector in collectors:
        data = collector.collect()
        all_data[collector.__class__.__name__] = data

    writer.write(all_data)


if __name__ == "__main__":
    run_once()