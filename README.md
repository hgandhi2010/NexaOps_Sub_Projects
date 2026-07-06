# NexaOps_SysMon

A lightweight, high-performance edge system telemetry monitoring engine built using Test-Driven Development (TDD) principles. This module hooks directly into core hardware abstraction layers to deliver fast, optimized telemetry logging and minified data handoffs.

---

 🚀 Installation & Local Execution
1. Environment Configuration
Clone the repository, initialize your isolated python virtual environment, and activate it:

Bash
# Initialize Environment
python -m venv .venv

# Activate Environment (Windows PowerShell)
.\.venv\Scripts\Activate.ps1
2. Dependency Management
Install the foundational testing framework and system performance monitoring hooks:

Bash
pip install pytest psutil
3. Running the Automated Verification Engine
Execute the pytest test matrix from the root folder to verify internal pipeline safety bounds and output accuracy:

Bash
pytest -v

## 🗺️ System Architecture

The following diagram maps out the multi-layered tracking pipeline, from raw operating system telemetry ingestion to localized log appending and automation payload generation:

```mermaid
graph TD
    %% Ingestion Layer
    subgraph Data Ingestion Point [1. System Hardware Layer]
        A1[OS Internal Metrics / Files]
    end

    %% Transformation Layer
    subgraph Transformation Logic [2. Processing Engine: sysmon.py]
        B1[Modular Metric Collectors]
        B2{Threshold Audit Validator}
        B3[Structured Logging Mechanism]
        
        B1 --> B2
        B2 -->|Metric Over Limit| B3
    end

    %% System Boundaries
    subgraph System Boundary Lines [3. Target Output Deliverables]
        C1[SysMon.log File]
        C2[Minified JSON Payload]
    end

    %% Core Data Intercepts
    A1 -->|Raw Data Intercept / Error Catching Hooks| B1
    B2 -->|Append Persistent Track Trace| C1
    B2 -->|Return Clean Formatted Metrics String| C2

    style Data Ingestion Point fill:#1f1f1f,stroke:#333,stroke-width:2px;
    style Transformation Logic fill:#111,stroke:#007acc,stroke-width:2px;
    style System Boundary Lines fill:#1f1f1f,stroke:#333,stroke-width:2px;


   



