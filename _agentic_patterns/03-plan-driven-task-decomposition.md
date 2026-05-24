---
layout: agentic_pattern
author: Alex Serban
name: Plan-Driven Task Decomposition
title: Plan-Driven Task Decomposition
category: Planning
unique_id: plan_driven_decomposition
index: 3
phase: Planning
comments: True
description: Turn a validated specification into a reviewed implementation plan.
image: /assets/img/plan.png

intent: Translate a validated specification into an ordered plan of atomic tasks, dependencies, scoped context, and verification points before implementation begins.
problem: A specification can state what should be achieved without yet defining how the work should be decomposed. Without an intermediate planning step, agents are more likely to drift, over-build, or work from an overloaded context.
pattern: Translate the specification into an ordered plan of atomic tasks. Each task should have a narrow objective, explicit dependencies, scoped context, and a clear verification point.
correct_use: Ask the agent to draft the plan, but review and refine it before implementation begins. Compress intent into what each task actually needs rather than passing the whole codebase or full specification into every step.
failure_mode: Execution begins directly from the specification, so decomposition happens implicitly and inconsistently during implementation. The result is usually drift, scope inflation, or poorly bounded tasks.
related: Specification-Driven Development, Incremental Execution, Memory & Context Management
dependencies: Follows specification writing and precedes execution
---

## Rationale

Specification and execution are distinct activities. A specification defines the intended outcome, constraints, and acceptance criteria. It does not automatically determine the right execution order, the correct task boundaries, or the smallest coherent units of work.

Coding agents are sensitive to how work is partitioned. If the next action is too large, the agent tends to improvise hidden substeps. If the context is too broad, irrelevant details compete with the actual task. If dependencies are implicit, the execution order becomes fragile.

Three recurrent failure modes motivate this pattern:

- **Drift.** The agent starts solving a slightly different problem than intended, and the deviation compounds over time.
- **Gold-plating.** The agent adds unnecessary structure because scope was never defined at task granularity.
- **Context pollution.** Long-running sessions accumulate stale or irrelevant context that influences later work.

## How to Apply the Pattern

The planning step should transform a validated specification into an executable sequence.

1. Start from an approved specification rather than a rough idea.
2. Decompose the work into the smallest coherent tasks that can be reviewed and verified.
3. State task dependencies explicitly.
4. For each task, identify the files, interfaces, or artefacts likely to be involved.
5. Define the verification action for each task or stage.
6. Review the resulting plan before any implementation begins.

The main objective is not simply to make a list of steps. It is to produce a plan that reduces ambiguity during execution.

## Plan Template

```markdown
# Implementation Plan: [Feature or Change]

Generated from: [specification file]
Status: Draft

## Stage 1: [Stage Name]
Goal: [What this stage achieves]
Verification: [How to confirm this stage is complete]

- [ ] Task 1: [Atomic task]
  - Depends on: [None or prior task]
  - Scope: [Files, modules, interfaces]
  - Context needed: [What the agent must know for this task]
  - Verification: [Command, test, or review action]

- [ ] Task 2: [Atomic task]
  - Depends on: Task 1
  - Scope: [Files, modules, interfaces]
   - Context needed: [Relevant constraints or artefacts]
  - Verification: [Command, test, or review action]
```

## Supporting Practices

### Use the Agent to Draft the Plan

LLMs can be useful in turning a specification into a first-pass plan. They are effective at proposing stages, identifying likely dependencies, and suggesting missing verification steps. They are less reliable at deciding whether the task boundaries are appropriate for the actual repository or team workflow.

A practical workflow is:

1. Provide the validated specification.
2. Ask the agent to propose stages and atomic tasks.
3. Ask the agent to justify the dependency order and identify missing checks.
4. Review the plan manually.
5. Use the reviewed plan as the execution artefact.

Useful prompts include:

- "Turn this specification into a staged implementation plan with atomic tasks."
- "Which tasks in this plan are too large and should be split further?"
- "What dependencies are implicit here and should be stated explicitly?"
- "What context does each task actually need?"

### Compress Context Per Task

Planning is also a context-management activity. Each task should carry only the code, constraints, and artefacts needed for that step. This is more reliable than giving every agent step the entire specification, full transcript, and broad repository context.

The question to ask is: what is the minimum context required for this task to be executed correctly?

### Review the Plan Before Execution

The plan should be treated as a reviewable artefact, not as a disposable prompt. Review should check at least four things:

| Area | Questions to ask |
|---|---|
| **Task Size** | Is each task small enough to execute and verify cheaply? |
| **Dependencies** | Is the order explicit and technically justified? |
| **Scope** | Does each task stay within a narrow surface area? |
| **Verification** | Is there a defined way to check each stage or task? |

## Practices

- Write the plan after the specification is validated and before implementation begins
- Decompose work into atomic, reviewable tasks
- State dependencies explicitly rather than assuming execution order
- Attach a verification action to each stage or task
- Limit the context passed to each task to what is actually needed
- Revise the plan when implementation reveals a genuine mismatch

## Anti-patterns

- Beginning implementation directly from the specification without a planning step
- Treating one large feature as a single task
- Passing the entire codebase or full transcript into every step
- Leaving dependencies implicit
- Starting execution from an unreviewed plan
- Using a plan that has no verification points

## Indicators

- Average number of files or interfaces touched per task
- Frequency with which tasks need to be split during execution
- Frequency of execution drift relative to the approved plan
- Share of tasks with explicit verification actions

## Example Workflow

```text
1. Validated specification
   -> Goals, constraints, context, and acceptance criteria are approved

2. Plan drafting
   -> Agent proposes stages and atomic tasks

3. Plan review
   -> Human refines task boundaries, dependencies, and checks

4. Verified plan
   -> The plan becomes the artefact that guides execution
```