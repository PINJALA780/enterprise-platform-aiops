# ADR-004: AIOps Safety

- Status: Accepted

## Decision
Build an AI-assisted incident analysis system.

## Capabilities
- Collect logs, metrics, traces and alerts.
- Correlate deployment and Kubernetes events.
- Suggest possible root causes.
- Recommend remediation.
- Record investigation history.

## Safety
Human approval is required for risky remediation.
AI must not perform unrestricted destructive production actions.
