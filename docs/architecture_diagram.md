# InfraScope Runtime Architecture

```
 Windows System
       │
       │
       ▼
+--------------------+
| InfraScope Service |
+--------------------+
         │
         │ starts
         ▼
+--------------------+
| Scheduler Engine   |
+--------------------+
         │
         │ triggers
         ▼
+--------------------+
| Collectors         |
|--------------------|
| CPU Collector      |
| Memory Collector   |
| Disk Collector     |
| Network Collector  |
| EventLog Collector |
+--------------------+
         │
         │ produce
         ▼
+--------------------+
| Snapshots          |
+--------------------+
         │
         │ evaluated by
         ▼
+--------------------+
| Detectors          |
|--------------------|
| Threshold Detector |
| Event Detector     |
+--------------------+
         │
         │ generate
         ▼
+--------------------+
| Anomaly Records    |
+--------------------+
         │
         │ written by
         ▼
+--------------------+
| Writers            |
|--------------------|
| JSONL Writer       |
+--------------------+
         │
         │ output
         ▼
C:\ProgramData\InfraScope\logs
```