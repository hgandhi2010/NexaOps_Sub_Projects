# Security Policy

## Supported Versions

Because `NexaOps_SysMon` hooks directly into hardware abstraction layers, we prioritize security patches on the latest active release branches to ensure system stability and telemetry integrity.

| Version | Supported          | Notes |
| ------- | ------------------ | ----- |
| Main    | :white_check_mark: | Active development, receives all security updates. |
| 1.0.x   | :white_check_mark: | Current stable release branch. |
| < 1.0   | :x:                | Legacy experimental versions are no longer supported. |

## Reporting a Vulnerability

We value the security of our edge telemetry pipeline. If you discover a security vulnerability—such as memory leaks, privilege escalation via OS hooks, or telemetry data injection—**please do not open a public GitHub issue.** Instead, please report it responsibly using one of the following methods:

### Method 1: GitHub Private Vulnerability Reporting (Preferred)
If this repository is public, please navigate to the **Security** tab of this repository, select **Vulnerabilities** under the
