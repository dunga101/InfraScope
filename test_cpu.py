from agent.collectors.cpu_collector import CPUCollector

collector = CPUCollector()
data = collector.collect()

print(data)