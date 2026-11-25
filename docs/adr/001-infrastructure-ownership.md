# ADR-001: Infrastructure Ownership

- Status: Accepted

## Decision
- Terraform manages foundational AWS infrastructure.
- Crossplane manages approved self-service cloud resources.
- Backstage provides the developer interface.
- Argo CD manages Kubernetes application deployments.

## Rule
Terraform and Crossplane must never independently manage the same resource.
