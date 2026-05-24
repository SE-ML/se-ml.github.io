---
layout: agentic_pattern
author: Alex Serban
name: Error Handling & Recovery
title: Error Handling & Recovery
category: Safety & Recovery
unique_id: error_handling
index: 15
phase: Implementation
comments: True
description: Define how to handle agent failures, hallucinations, and stuck states.

intent: Define how to handle agent failures, hallucinations, and stuck states.
problem: Agents fail by producing incorrect output, getting stuck in loops, hallucinating APIs or syntax, misunderstanding requirements, or exceeding resource limits.
solution: Implement recovery strategies for each failure mode with detection mechanisms and appropriate recovery actions.
related: Rollback & Reversibility, Graceful Degradation
dependencies: Works with rollback and degradation patterns
---

## Problem

Agents fail by:
- Producing incorrect output
- Getting stuck in loops
- Hallucinating APIs or syntax
- Misunderstanding requirements
- Exceeding resource limits

## Solution

Implement recovery strategies for each failure mode:

| Failure Mode | Detection | Recovery Strategy |
|--------------|-----------|-------------------|
| **Wrong output** | Verification fails | Rollback → clarify spec → retry |
| **Stuck/looping** | Timeout, repetition | Interrupt → decompose problem → retry |
| **Hallucination** | Non-existent APIs/syntax | Provide correct info → constrain |
| **Scope creep** | Changes to unrelated files | Rollback → tighten constraints |
| **Resource exhaustion** | Token/time limits | Summarize → continue fresh |
| **Repeated failure** | N failures on same task | Escalate → try different approach |

## Recovery Configuration

```yaml
error_handling:
  max_retries: 3
  retry_delay: exponential
  on_max_retries: escalate_to_human
  
  strategies:
    verification_failure:
      action: rollback_and_retry
      provide_feedback: true
      
    loop_detection:
      threshold: 3_similar_actions
      action: interrupt_and_decompose
      
    hallucination:
      action: provide_correct_context
      constrain_tools: true
      
    timeout:
      threshold: 5_minutes
      action: checkpoint_and_summarize
```

## Recovery Workflow

```
Error Detected
     │
     ▼
┌─────────────┐
│ Identify    │
│ Failure     │
│ Mode        │
└──────┬──────┘
       │
       ▼
┌─────────────┐    ┌─────────────┐
│ Apply       │───▶│ Log for     │
│ Recovery    │    │ Analysis    │
│ Strategy    │    └─────────────┘
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Retry or    │
│ Escalate    │
└─────────────┘
```

## Practices

- Set timeout expectations for tasks
- Define retry limits (not infinite)
- Have fallback approaches ready
- Document failure patterns for future reference
- Log all failures for analysis
- Provide clear feedback on why failure occurred

## Anti-patterns

- ❌ Infinite retry loops
- ❌ No timeout boundaries
- ❌ Accepting degraded output without noting it
- ❌ Same approach after repeated failures
- ❌ Not logging failures for pattern analysis
