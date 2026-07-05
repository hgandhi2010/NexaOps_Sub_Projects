# NexaOps_Sub_Projects
Side Projects for NexaOps-AI

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
        C1[sysmon.log File]
        C2[Minified JSON Payload]
    end

    %% Core Data Intercepts
    A1 -->|Raw Data Intercept / Error Catching Hooks| B1
    B2 -->|Append Persistent Track Trace| C1
    B2 -->|Return Clean Formatted Metrics String| C2

    style Data Ingestion Point fill:#1f1f1f,stroke:#333,stroke-width:2px;
    style Transformation Logic fill:#111,stroke:#007acc,stroke-width:2px;
    style System Boundary Lines fill:#1f1f1f,stroke:#333,stroke-width:2px;
    ``` 
    