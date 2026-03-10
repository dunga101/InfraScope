# InfraScope Code Module Architecture

The InfraScope codebase is organized into clear modules to maintain separation of responsibilities.

Each module has a single purpose.

```
InfraScope
│
├── agent
│   │
│   ├── service
│   │     Windows service lifecycle
│   │
│   ├── core
│   │     scheduler
│   │     runtime orchestration
│   │
│   ├── collectors
│   │     gather telemetry from system components
│   │
│   ├── detectors
│   │     evaluate telemetry for anomalies
│   │
│   ├── writers
│   │     persist anomaly records
│   │
│   ├── models
│   │     shared data models
│   │
│   ├── config
│   │     configuration loading
│   │
│   └── utils
│         shared helper utilities
│
├── docs
│     architecture documentation
│
├── tests
│     unit tests
│
└── installer
      service installation scripts
```

---

## Module Responsibilities

### service

Handles Windows Service lifecycle:

- start
- stop
- restart
- integration with Windows Service Manager

---

### core

Contains the runtime engine:

- scheduler loop
- orchestration
- system initialization

---

### collectors

Collectors gather telemetry from the system.

Examples:

- CPU usage
- memory usage
- disk usage
- network metrics
- Windows Event Logs

Collectors return **Snapshots**.

---

### detectors

Detectors evaluate telemetry snapshots.

Examples:

- threshold detection
- event severity detection
- burst detection

Detectors generate **Anomaly records**.

---

### writers

Writers persist anomaly records.

Examples:

- JSONL writer
- log rotation

---

### models

Models define the shared data structures:

- Snapshot
- Anomaly

These ensure consistent communication between modules.

---

### config

Handles configuration loading and validation.

Expected configuration format:

YAML

---

### utils

Contains helper functions used across modules.

Examples:

- hostname retrieval
- timestamp helpers
- path utilities
