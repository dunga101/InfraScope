# InfraScope — Codex Project Plan

## Objective

Build an open-source, lightweight Windows background service that collects local hardware/software telemetry, detects anomalies using simple rules first, and writes structured local logs for later review.

## Product principles

* Lightweight and low overhead
* Local-first, no cloud dependency in v1
* Transparent and auditable
* Safe-by-default, read-only telemetry in v1
* Modular collectors and rules engine
* Open-source friendly and contributor-friendly

## Proposed v1 scope

* Run as a Windows service
* Collect CPU, memory, disk, network, uptime, top processes
* Read selected Windows Event Logs (System, Application)
* Evaluate simple anomaly rules
* Write JSONL logs locally under ProgramData
* Rotate logs safely
* Provide YAML config
* Provide installer/uninstaller scripts
* No remote command execution
* No kernel hooks
* No persistence beyond standard service install

## Suggested stack

* Language: Python
* Service framework: pywin32
* Metrics: psutil
* Config: pydantic or plain YAML parsing
* Logging: JSON lines
* Packaging: PyInstaller later
* CI: GitHub Actions

## Initial repository layout

* agent/

  * service.py
  * main.py
  * collectors/
  * detectors/
  * writers/
  * config/
  * utils/
* installer/
* tests/
* docs/
* examples/

## Recommended module boundaries

### Collectors

Return normalized snapshots only.

* cpu_collector
* memory_collector
* disk_collector
* network_collector
* process_collector
* eventlog_collector

### Detectors

Receive snapshots/events and emit anomaly records.

* threshold_detector
* event_severity_detector
* burst_detector

### Writers

Persist outputs.

* jsonl_writer
* rotating_file_writer

### Core

* scheduler loop
* config loader
* health heartbeat
* self-log

## Example anomaly categories

* sustained_high_cpu
* sustained_high_memory
* low_disk_space
* disk_error_event
* app_crash_event
* service_failure_event
* network_spike

## Data contract direction

### Snapshot

* timestamp
* hostname
* collector
* metrics

### Anomaly

* timestamp
* hostname
* category
* severity
* source
* evidence
* threshold
* message
* recommended_next_step

## Roadmap

### Milestone 1

Project skeleton, config, logging, service wrapper

### Milestone 2

CPU/memory/disk collectors and threshold detector

### Milestone 3

Windows Event Log collector and anomaly mapping

### Milestone 4

Installer, tests, documentation, GitHub Actions

### Milestone 5

Performance tuning and packaging

## Open-source readiness

* MIT or Apache-2.0 license
* CONTRIBUTING.md
* CODE_OF_CONDUCT.md
* SECURITY.md
* issue templates
* architecture decision records in docs/adr/

## Guardrails for Codex

* Prefer small, reviewable commits
* Keep functions short and typed
* Add docstrings
* Add tests for every new detector
* Do not introduce remote telemetry by default
* Do not add auto-remediation in v1
* Keep Windows compatibility explicit

## First Codex tasks

1. Create repository skeleton and Python package structure
2. Add config model and JSONL logger
3. Add Windows service wrapper with clean start/stop
4. Add CPU/memory/disk collectors
5. Add threshold detector and anomaly record schema
6. Add unit tests
7. Add installer PowerShell scripts
8. Add README and architecture docs

## Definition of done for v1

* Service starts and stops cleanly on Windows
* Configurable interval
* JSONL logs written to ProgramData
* At least 3 collectors and 3 anomaly rules working
* Basic Event Log ingestion working
* Unit tests passing in CI
* README sufficient for outside contributors

---

# Architecture Specification (v1)

## System Purpose

InfraScope is a lightweight Windows endpoint observability agent designed to collect local system telemetry, evaluate anomaly conditions, and persist structured diagnostic records locally for later analysis.

The system prioritizes:

* minimal system overhead
* transparency of operation
* deterministic rule‑based anomaly detection
* modular architecture enabling community extensions

InfraScope v1 intentionally avoids remote telemetry transmission and automated remediation actions.

---

# Runtime Architecture

Runtime flow:

Service Start
→ Load configuration
→ Initialize collectors
→ Scheduler loop
→ Collect telemetry snapshots
→ Pass snapshots to detectors
→ Generate anomaly records
→ Write structured JSON logs
→ Sleep interval
→ Repeat

This design ensures a predictable control loop and simplifies debugging.

---

# Core Components

## 1. Service Layer

Responsible for:

* Windows Service lifecycle
* Start / Stop management
* launching the scheduler

Location:

agent/service/

Key responsibilities:

* register service
* gracefully stop loops
* ensure logging available early

---

## 2. Scheduler (Core Engine)

Location:

agent/core/

Responsibilities:

* execute collectors on interval
* pass snapshots to detectors
* manage execution order

Pseudo flow:

collectors → snapshot → detectors → anomalies → writers

The scheduler does **not implement business logic**.

---

## 3. Collectors

Location:

agent/collectors/

Collectors gather telemetry only.

Collectors must:

* be read‑only
* execute quickly
* return structured snapshots

Example collectors:

cpu_collector
memory_collector
disk_collector
network_collector
process_collector
eventlog_collector

Collector interface concept:

collect() -> Snapshot

---

## 4. Snapshot Data Model

Snapshots represent raw telemetry collected during a cycle.

Fields:

* timestamp
* hostname
* collector
* metrics

Example snapshot:

{
"collector": "cpu",
"metrics": {
"cpu_usage": 84
}
}

Snapshots are ephemeral and only used by detectors.

---

## 5. Detectors

Location:

agent/detectors/

Detectors evaluate snapshots and determine whether anomalies exist.

Detectors must:

* contain deterministic rules
* produce structured anomaly records
* never perform IO operations

Examples:

threshold_detector
burst_detector
event_severity_detector

Detector interface concept:

evaluate(snapshot) -> list[Anomaly]

---

## 6. Anomaly Data Model

An anomaly is a structured diagnostic signal.

Fields:

* timestamp
* hostname
* category
* severity
* source
* evidence
* threshold
* message

Example anomaly:

{
"category": "sustained_high_cpu",
"severity": "warning",
"evidence": {
"cpu_usage": 96
},
"threshold": 90
}

---

## 7. Writers

Location:

agent/writers/

Writers persist anomalies.

Primary writer in v1:

JSONL writer

Responsibilities:

* write anomalies to disk
* rotate logs safely

Example output location:

C:\ProgramData\InfraScope\logs

Format:

JSON Lines

Each anomaly = one line.

---

## 8. Configuration System

Location:

agent/config/

Configuration file format:

YAML

Example:

interval: 30

thresholds:
cpu: 90
memory: 95
disk: 90

logs:
path: ProgramData/InfraScope/logs

Responsibilities:

* load config
* validate schema

---

# Performance Principles

InfraScope must maintain:

* low CPU usage (<1–2%)
* low memory footprint
* minimal disk writes

Collectors should execute within milliseconds whenever possible.

---

# Security Model

InfraScope v1 must NOT:

* execute remote commands
* alter system configuration
* transmit telemetry externally

The agent operates strictly in read‑only diagnostic mode.

---

# Extension Model

Future contributors should be able to add:

* new collectors
* new detectors

without modifying core components.

This is achieved through the collector and detector interfaces.

---

# Future Evolution

Potential future capabilities:

* baseline anomaly detection
* fleet aggregation service
* OpenTelemetry export
* performance dashboards
* security anomaly modules

These will remain optional extensions to preserve the lightweight core philosophy.
