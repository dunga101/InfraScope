# InfraScope Runtime Pipeline

InfraScope operates as a deterministic monitoring loop.

The agent continuously collects system telemetry, evaluates anomaly rules, and writes structured records.

---

## Execution Flow

Service Start

→ Load configuration  
→ Initialize collectors  
→ Initialize detectors  
→ Initialize writers  

Scheduler Loop

1. Collect telemetry snapshots
2. Normalize snapshot data
3. Pass snapshots to detectors
4. Evaluate anomaly rules
5. Generate anomaly records
6. Persist anomalies using writers
7. Sleep until next interval

---

## Data Flow

Collectors → Snapshots → Detectors → Anomalies → Writers

---

## Components

### Collectors

Collectors gather system telemetry.

Examples:

- CPU usage
- Memory usage
- Disk usage
- Network metrics
- Windows Event Logs

Collectors return **Snapshots**.

---

### Snapshots

Snapshots represent raw telemetry data.

Example structure:

{
 "timestamp": "2026-03-10T12:00:00Z",
 "hostname": "HOST01",
 "collector": "cpu",
 "metrics": {
   "cpu_usage": 78
 }
}

Snapshots are passed to detectors.

---

### Detectors

Detectors evaluate telemetry snapshots and identify anomalies.

Example conditions:

- CPU usage > threshold
- memory usage > threshold
- disk free space below threshold
- event log critical error

Detectors return **Anomaly records**.

---

### Anomaly Records

Example:

{
 "timestamp": "2026-03-10T12:00:00Z",
 "hostname": "HOST01",
 "category": "sustained_high_cpu",
 "severity": "warning",
 "source": "cpu_detector",
 "evidence": {
   "cpu_usage": 96
 },
 "threshold": 90,
 "message": "CPU usage exceeded threshold"
}

---

### Writers

Writers persist anomaly records.

In v1:

- JSONL writer
- local file storage

Example output path:

ProgramData/InfraScope/logs

Each anomaly is written as a JSON line.