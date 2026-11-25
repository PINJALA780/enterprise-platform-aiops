# ADR-003: GitOps Strategy

- Status: Accepted

## Decision
Use Argo CD for Kubernetes GitOps.

## Workflow
1. Developer pushes code.
2. GitHub Actions tests and scans the application.
3. Docker image is published to Amazon ECR.
4. GitOps configuration is updated.
5. Argo CD reconciles the desired state into EKS.

## Principle
Git is the source of truth for deployment configuration.
