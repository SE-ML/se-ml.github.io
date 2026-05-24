---
layout: agentic_pattern
author: Alex Serban
name: Trust Boundaries
title: Trust Boundaries
category: Safety & Recovery
unique_id: trust_boundaries
index: 13
phase: Setup
comments: True
description: Define explicit boundaries for what agents can access, modify, and execute.

intent: Define explicit boundaries for what agents can access, modify, and execute.
problem: Unrestricted agents can modify production systems, expose credentials, delete important data, execute arbitrary code, and access unauthorized resources.
solution: Layer trust with explicit permissions for Read, Write, Execute, Network, and Secrets access across different trust levels from Minimal to Production.
related: Rollback & Reversibility, Error Handling & Recovery
dependencies: Foundational safety pattern
---

## Problem

Unrestricted agents can:
- Modify production systems
- Expose credentials
- Delete important data
- Execute arbitrary code
- Access unauthorized resources

## Solution

Layer trust with explicit permissions:

| Trust Level | Read | Write | Execute | Network | Secrets |
|-------------|------|-------|---------|---------|---------|
| **Minimal** | Specified files | None | None | None | None |
| **Sandboxed** | Project files | Temp directory | Sandboxed | None | None |
| **Development** | Project files | Project files | Local tests | Local only | Dev only |
| **Full** | All files | All files | Any command | Allowed | Accessible |
| **Production** | Restricted | Controlled | Approved only | Monitored | Vault only |

## Boundary Specification

```markdown
## Agent Permissions

### File Access
- READ: src/**, tests/**, docs/**
- WRITE: src/**, tests/**
- FORBIDDEN: .env, secrets/**, node_modules/**

### Execution
- ALLOWED: npm test, npm run lint, npm run build
- FORBIDDEN: npm publish, rm -rf, curl

### Network
- ALLOWED: localhost:*
- FORBIDDEN: external APIs (except approved list)
```

## Trust Escalation

When an agent needs higher permissions:
1. Agent requests elevated permissions with justification
2. Human reviews the request
3. If approved, grant temporarily scoped permissions
4. Log all actions taken with elevated permissions
5. Revoke elevated permissions when task completes

## Practices

- Start with minimal permissions
- Explicitly scope file/folder access
- Use sandboxed environments for testing
- Never expose production credentials to agents
- Audit agent actions regularly
- Use principle of least privilege
- Document permission boundaries in agent configuration

## Anti-patterns

- ❌ Giving agents access to production
- ❌ Storing secrets in agent-accessible locations
- ❌ No isolation between test and production
- ❌ Implicit trust based on task description
- ❌ Permanent elevated permissions
