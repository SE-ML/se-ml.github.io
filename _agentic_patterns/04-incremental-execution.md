---
layout: agentic_pattern
author: Alex Serban
name: Incremental Execution
title: Incremental Execution
category: Execution
unique_id: incremental_exec
index: 4
phase: Implementation
comments: True
description: Execute one approved task at a time with immediate verification.


intent: Carry out one approved task at a time with immediate verification and checkpointing rather than in large agent-issued batches.
problem: Large agent-issued changes are hard to inspect, validate, and unwind. Errors introduced early are often discovered only after later steps depend on them.
pattern: Execute in small, independently verifiable units. Each step should have a narrow scope, an explicit validation action, and a clear stopping point. Reliability tends to decay as edit breadth increases.
correct_use: Prefer one coherent slice at a time, validate immediately, and move forward only from a known-good state.
failure_mode: A single session creates an entangled change set whose internal assumptions cannot be isolated or tested cheaply.
related: Plan-Driven Task Decomposition, Role-Based Development & Subagents, Verification-First Engineering, Rollback & Reversibility
dependencies: Follows planning and works with verification and rollback patterns
---

## Rationale

Agents can produce many plausible edits quickly, but the ease of generation does not reduce the cost of inspection, validation, or recovery. When changes are issued in large batches, several problems tend to appear at once:

- Verification becomes slower and less discriminating
- Errors compound across multiple files and steps
- Rollback becomes more expensive
- The source of failure becomes harder to localize

The practical issue is not only that large changes contain more code. It is that later edits often depend on earlier ones. By the time a defect is noticed, the session may already have built additional assumptions on top of it.

This pattern assumes that task decomposition has already happened. Its concern is not how the work is partitioned into tasks, but how each approved task is carried out safely.

## How to Apply the Pattern

Execute the approved plan one logical step at a time. Each step should identify what is being changed, how success will be checked, and where execution should pause before continuing.

In practice, this usually means:

1. Select the next approved task from the plan.
2. Limit execution to that single slice of work.
3. Run the defined verification action immediately.
4. Commit or checkpoint the known-good state.
5. Continue only after the current step is verified.

The goal is not to maximize the number of steps. It is to make each step small enough that failure can be detected, explained, and reversed cheaply.

Pattern 4 governs execution cadence. Pattern 5 governs role separation and handoff. They often compose, but they answer different questions.

## Step Template

```markdown
STEP 1: [Action]
  Files: [affected files]
  Verify: [how to confirm success]
  Rollback: [how to undo if needed]

STEP 2: [Action]
  Files: [affected files]
  Verify: [how to confirm success]
  Rollback: [how to undo if needed]
```

## Supporting Practices

### Keep Verification Between Steps

#### Verification Cadence

```
┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐
│ Step 1   ───▶ Verify    ───▶ Commit   ───▶ Step 2   ───▶ ...
└─────────┘    └─────────┘    └─────────┘    └─────────┘
                   │
                   ▼ (if fail)
              ┌─────────┐
              │Rollback │
              └─────────┘
```

This cadence is the operational core of the pattern: execute, verify, and only then continue.

### Pair the Pattern with TDD When Appropriate

#### TDD Step Cadence

Incremental execution pairs naturally with test-driven development. Each implementation step follows this sequence:

```
1. Write the failing test
2. Run it to verify it fails (confirm the test is meaningful)
3. Implement the minimal code to make the test pass
4. Run the tests to verify they pass
5. Commit
```

As a rule of thumb, each step should be small enough to complete and verify quickly. If a step becomes large, split it further.

Where task decomposition, dependency order, or task-scoped context remain unclear, return to the planning step rather than improvising a broader execution step.

## Practices

- Ask for one coherent change at a time
- Verify after each change before proceeding
- Commit frequently at working states
- Keep each step small enough to review quickly
- Return to the plan when execution reveals that a task is too large or poorly bounded
- State clearly that execution should pause when the approved task boundary becomes unclear

## Anti-patterns

- Requests to implement an entire feature in one step
- Multiple unrelated changes in one request
- Skipping verification between steps
- Steps that modify many files at once
- Steps without a defined verification action
- Skipping the failing-test step

## Indicators

- Average size of each implementation step or diff
- Time between selecting a task and running its first verification step
- Time needed to identify the source of a regression
- Frequency of successful rollback to the previous known-good state
