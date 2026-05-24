---
layout: agentic_pattern
author: Alex Serban
name: Human-in-the-Loop Checkpoints
title: Human-in-the-Loop Checkpoints
category: Coordination
unique_id: human_loop
index: 12
phase: Continuous
comments: True
description: Define explicit points where human review and approval is required before proceeding.

intent: Define explicit points where human review and approval is required before proceeding.
problem: Full automation risks compounding errors, some decisions require human judgment, costly mistakes need prevention gates, and compliance may require human approval.
solution: Establish checkpoint types including Approval Gates, Review Gates, Decision Gates, Escalation Gates, and Quality Gates with clear triggers and human actions.
related: Verification-First Engineering, Trust Boundaries
dependencies: Works with verification and safety patterns
---

## Problem

- Full automation risks compounding errors
- Some decisions require human judgment
- Costly mistakes need prevention gates
- Compliance may require human approval

## Solution

Establish checkpoint types:

| Checkpoint Type | Trigger | Human Action | Example |
|-----------------|---------|--------------|---------|
| **Approval Gate** | Before destructive/irreversible action | Approve/reject | Delete files, deploy to prod |
| **Review Gate** | After significant output | Review/revise | Architecture decisions |
| **Decision Gate** | Multiple valid options | Choose direction | Technology selection |
| **Escalation Gate** | Agent uncertainty | Provide guidance | Ambiguous requirements |
| **Quality Gate** | After milestone | Verify quality | End of feature |

## Checkpoint Definition Template

```markdown
## Checkpoint: [Name]

**Trigger:** [When this checkpoint activates]
**Presented to human:**
- [Information item 1]
- [Information item 2]

**Human options:**
- Approve: [What happens]
- Reject: [What happens]
- Modify: [What happens]

**Timeout behavior:** [What happens if no response]
```

## Checkpoint Frequency Guide

| Trust Level | Checkpoint Frequency |
|-------------|---------------------|
| **New agent/task** | Every step |
| **Familiar task** | Major milestones |
| **Proven workflow** | Critical points only |
| **Fully trusted** | Exceptions only |

## Adjusting Over Time

As you build trust with an agent on a specific type of task:
1. Start with frequent checkpoints
2. Track which checkpoints rarely catch issues
3. Reduce frequency for consistently passing checkpoints
4. Maintain checkpoints for high-risk operations regardless

## Practices

- Define checkpoints upfront in plans
- Make checkpoints cheap to execute (clear, focused)
- Log decisions made at checkpoints
- Adjust checkpoint frequency based on trust level
- Provide clear context at each checkpoint

## Anti-patterns

- ❌ No checkpoints (full autopilot)
- ❌ Too many checkpoints (defeats agent value)
- ❌ Checkpoints without clear criteria
- ❌ Approval without understanding
- ❌ Same checkpoint frequency for all trust levels
