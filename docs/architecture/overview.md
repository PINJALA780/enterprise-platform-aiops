# Enterprise Platform Architecture

## 1. Project Vision

Build an enterprise Internal Developer Platform that enables developers
to create, deploy, secure and observe applications through self-service
workflows.

## 2. Core Architecture

Developer
  |
  v
Backstage Developer Portal
  |
  v
GitHub Repository
  |
  v
GitHub Actions CI/CD
  |
  +--> SonarQube
  +--> Gitleaks
  +--> Trivy
  |
  v
Docker Image
  |
  v
Amazon ECR
  |
  v
Argo CD
  |
  v
Amazon EKS
  |
  +--> Istio
  +--> Kyverno
  +--> HPA / KEDA / Karpenter
  |
  v
OpenTelemetry Collector
  |
  +--> Datadog
  +--> Prometheus / Grafana
  |
  v
AIOps Incident Analysis
  |
  v
Human-approved Remediation

## 3. Infrastructure Ownership

- Terraform: foundational AWS infrastructure.
- Crossplane: approved self-service cloud resources.
- Argo CD: Kubernetes application deployment.
- Kyverno: Kubernetes policy enforcement.

No two controllers should independently manage the same resource.

## 4. Security Principles

- Least-privilege IAM.
- GitHub Actions using AWS OIDC.
- Secrets stored outside source control.
- Container image scanning.
- Kubernetes admission policies.
- Human approval for risky remediation.

## 5. Operational Principles

- Observable services.
- Defined SLOs and error budgets.
- Documented incident runbooks.
- Tested backup and recovery.
- Cost-aware infrastructure.
