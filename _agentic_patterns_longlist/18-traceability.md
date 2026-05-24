---
layout: agentic_pattern
author: Alex Serban
name: Traceability
title: Traceability
category: Maintenance
unique_id: traceability
index: 18
phase: Continuous
comments: True
description: Maintain clear records of what agents did, why, and with what results.

intent: Maintain clear records of what agents did, why, and with what results.
problem: Without traceability you cannot debug why something is wrong, reproduce agent work, audit for compliance, improve prompts, or learn from failures.
solution: Log prompts, outputs, decisions, verification results, human overrides, and time/cost metrics systematically.
related: Cleanup & Hygiene, Memory & Context Management
dependencies: Works with cleanup and memory patterns
---

## Problem

Without traceability:
- Cannot debug why something is wrong
- Cannot reproduce agent work
- Cannot audit for compliance
- Cannot improve prompts
- Cannot learn from failures

## Solution

Log the following:

| What to Log | Why | Where |
|-------------|-----|-------|
| **Prompts given** | Reproduce, improve | Session logs |
| **Outputs received** | Debug, audit | Session logs |
| **Decisions made** | Understand rationale | DECISIONS.md |
| **Verification results** | Track quality | CI/CD logs |
| **Human overrides** | Understand corrections | Session logs |
| **Time/cost** | Optimize | Metrics system |

## Traceability Artifacts

### CHANGELOG.md

```markdown
## [Date] - Task Description

### Added
- Feature X (agent-assisted)

### Changed
- Refactored Y (agent-assisted)

### Agent Session
- Model: Claude Opus 4.5
- Prompts: 12
- Duration: 45 min
- Human overrides: 2
```

### DECISIONS.md

```markdown
## Decision: Use PostgreSQL over MongoDB

**Date:** 2026-02-01
**Context:** Need database for user data
**Decision:** PostgreSQL
**Rationale:** 
- Structured data fits relational model
- Team expertise
- Agent recommendation with verification

**Alternatives Considered:**
- MongoDB: Better for unstructured, but our data is structured
```

### Session Log Structure

```json
{
  "session_id": "abc123",
  "timestamp": "2026-02-01T10:30:00Z",
  "model": "claude-opus-4-5-20260215",
  "task": "Implement user preferences API",
  "prompts": [
    {"role": "user", "content": "..."},
    {"role": "assistant", "content": "..."}
  ],
  "verification_results": {
    "tests_passed": true,
    "lint_errors": 0
  },
  "files_changed": ["src/auth.ts", "tests/auth.test.ts"]
}
```

## Practices

- Use version control commit messages meaningfully
- Document non-obvious decisions
- Keep prompt templates under version control
- Review logs when debugging
- Aggregate metrics for improvement
- Automate log collection where possible

## Anti-patterns

- ❌ No record of agent interactions
- ❌ Vague commit messages ("fixed stuff")
- ❌ Undocumented architectural decisions
- ❌ Losing session context between days
- ❌ Not reviewing logs for improvement opportunities
