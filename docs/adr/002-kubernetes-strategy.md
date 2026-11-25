# ADR-002: Kubernetes Strategy

- Status: Accepted

## Decision
- Use Minikube for local development.
- Use Amazon EKS for cloud deployment.
- Start with one EKS cluster.
- Use namespaces and RBAC for environment isolation.

## Trade-offs
EKS provides managed Kubernetes but introduces ongoing AWS costs.
