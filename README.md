# InfraScope

InfraScope is a lightweight Windows observability agent designed to collect local telemetry and detect system anomalies before they impact users.

The project focuses on proactive troubleshooting by collecting system metrics, evaluating them through anomaly detectors, and writing structured logs for analysis.

---

# Architecture Overview

InfraScope is designed as a modular observability pipeline.

```
Collectors → Detectors → Writers
```

Each stage of the pipeline has a clearly defined responsibility.

---

## High Level Flow

```
+-------------+
|  Collectors |
|-------------|
| CPU usage   |
| Memory use  |
| Disk stats  |
+-------------+
        |
        v
+-------------+
|  Detectors  |
|-------------|
| Thresholds  |
| Pattern     |
| Anomaly     |
+-------------+
        |
        v
+-------------+
|   Writers   |
|-------------|
| JSON logs   |
| File output |
| Future SIEM |
+-------------+
```

---

# Project Structure

```
InfraScope
│
├── agent
│   ├── collectors
│   ├── detectors
│   ├── writers
│   ├── models
│   ├── utils
│   └── core
│
├── docs
│   ├── architecture.md
│   ├── architecture_diagram.md
│   └── module_architecture.md
│
├── installer
│
├── tests
│
├── pyproject.toml
└── README.md
```

---

# Design Principles

InfraScope follows several key engineering principles:

**Modularity**

Each component operates independently.

**Observability-first design**

The system is built around telemetry collection and analysis.

**Structured logging**

Output is designed to integrate with log analysis platforms.

**Extensibility**

Future collectors and detectors can be added without changing the core runtime.

---

# Current Status

Project foundation and architecture documentation completed.

Next milestone:

Implement runtime execution engine.

```
agent/core/runtime.py
```

This module will orchestrate the telemetry pipeline.

---

# Future Goals

- Windows service integration
- Expanded telemetry collectors
- Advanced anomaly detection
- SIEM / log platform integration
- performance tuning

---

# Author

Dulanga Mudalige  
Mechanical Engineer → Systems / Cloud / Infrastructure Engineering