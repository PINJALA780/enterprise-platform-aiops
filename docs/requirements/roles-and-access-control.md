# Platform Roles and Access Control

## 1. Platform Roles

- Developer
- Platform Engineer
- DevOps Engineer
- Security Engineer
- SRE Engineer
- Platform Administrator

## 2. Responsibilities

### Developer
Creates, tests and deploys owned applications.

### Platform Engineer
Maintains Backstage, platform services and infrastructure automation.

### DevOps Engineer
Maintains CI/CD pipelines, GitOps and deployment workflows.

### Security Engineer
Maintains security policies, vulnerability controls and compliance.

### SRE Engineer
Monitors service health, SLOs, incidents and recovery.

### Platform Administrator
Manages platform-wide identities, permissions and governance.

## 3. Access Control Design

- Use role-based access control.
- Apply least-privilege permissions.
- Restrict production access.
- Separate application and platform administration.
- Audit sensitive operations.

## 4. Identity and Authorization

- Backstage: user authentication and plugin permissions.
- GitHub: repository and environment permissions.
- AWS IAM: cloud resource permissions.
- Kubernetes RBAC: cluster and namespace permissions.
- Kyverno: admission and workload policy enforcement.

## 5. Production Approval

Production deployment must follow protected
branch and environment approval policies.

## 6. AIOps Security

- Use a dedicated service identity.
- Restrict access to necessary telemetry.
- Require human approval for risky remediation.
- Maintain an audit trail.

## 7. Security Principle

No user or service receives administrative
permissions unless explicitly required.
