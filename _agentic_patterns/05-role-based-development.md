---
layout: agentic_pattern
author: Alex Serban
name: Role-Based Development & Subagents
title: Role-Based Development & Subagents
category: Execution
unique_id: role_based
index: 5
phase: Implementation
comments: True
description: Distribute work across roles with isolated context and clear handoff.
image: /assets/img/role.png

intent: Distribute work across agents or sessions with distinct roles, scoped context, and structured handoff rather than relying on one overloaded conversation.
problem: Single long-running sessions mix exploration, design, implementation, and review into one context stream. This creates context pollution and weakens specialization.
pattern: Separate roles across fresh agents or subagents with scoped context. Typical roles include explorer, implementer, spec reviewer, and code reviewer. The key principle is isolation with structured handoff.
correct_use: Delegate non-overlapping tasks, pass concise summaries rather than whole transcripts, and sequence review roles explicitly.
failure_mode: The same agent both creates and legitimizes a solution while operating under stale or overloaded context.
related: Plan-Driven Task Decomposition, Incremental Execution, Workflow Orchestration Patterns, Memory & Context Management
dependencies: Works with planning, execution, orchestration, and context patterns
---

## Rationale

Agent performance depends strongly on context quality. When one session is asked to explore the codebase, interpret the specification, implement changes, justify its own choices, and review the result, these activities compete with one another in a single context stream. The result is often a mixture of stale assumptions, weak specialization, and shallow self-review.

Subagents or separate sessions help because they introduce context isolation. Each role can operate with a narrower objective, a smaller relevant context, and a clearer output format. This does not guarantee correctness, but it reduces the tendency for one overloaded session to accumulate too many responsibilities at once.

This pattern is not primarily about task decomposition or execution cadence. It is about who does the work, who reviews it, and how information moves between those roles.

Common pressures that motivate this pattern include:

- Mixed concerns within one long session
- Declining context quality over time
- Difficulty parallelizing non-overlapping work
- Weak separation between production and review
- Tasks that exceed what one session can handle cleanly

## How to Apply the Pattern

Role-based development starts by separating activities that should not share the same working context.

1. Identify which roles are needed for the task.
2. Give each role a narrow objective and only the context it needs.
3. Define what each role should return, usually as a summary or decision artefact.
4. Sequence roles explicitly when one depends on the output of another.
5. Keep review roles independent from implementation roles wherever possible.

The main objective is not to maximize the number of agents. It is to prevent context overload and role confusion.

Pattern 4 governs how an approved task is executed step by step. Pattern 5 governs how responsibility for that task is distributed across agents or sessions.

## Typical Roles

| Role | Responsibility | Context Needs |
|------|----------------|---------------|
| **Architect** | High-level design, component boundaries | System overview, requirements |
| **Implementer** | Write code for specific components | Component specs, interfaces |
| **Reviewer** | Critique and improve code quality | Code, style guides, patterns |
| **Tester** | Write and run tests | Code, requirements, test frameworks |
| **Documenter** | Write documentation | Code, user stories, API specs |
| **Researcher** | Gather information, explore options | Problem description, constraints |

## Typical Subagent Types

| Subagent | Purpose | Typical Tools |
|----------|---------|---------------|
| **Explore** | Fast, read-only codebase analysis | Read, Grep, Glob |
| **Plan** | Research and context gathering before planning | Read, Search |
| **General-purpose** | Complex multi-step tasks requiring action | Read, Write, Edit, Execute |

## Supporting Practices

### Define the Handoff Explicitly

Role separation works only if the interface between roles is clear. A good handoff states what was done, what remains unresolved, which artefacts matter, and what the next role should evaluate or produce.

Subagents are useful because they provide isolated context for complex tasks. Each subagent receives a fresh context window and communicates through delegation and summary rather than shared conversational state.

#### Subagent Communication Pattern

1. Main agent identifies delegatable task.
2. Main agent invokes a subagent with a specific scope and expected output.
3. Subagent executes in isolated context.
4. Subagent returns a concise summary rather than its full internal context.
5. Main agent incorporates the summary and decides the next step.

The summary is important. A well-designed subagent returns distilled findings rather than its entire internal context.

### Use Simple Orchestration Patterns

Different tasks justify different orchestration structures.

#### Orchestration Patterns

```
Sequential:     Role A ──▶ Role B ──▶ Role C

Parallel:       Role A ──┐
                Role B ──┼──▶ Aggregator
                Role C ──┘

Iterative:      Implementer ◀──▶ Reviewer (cycle until accepted)

Hierarchical:   Supervisor ──┬──▶ Team A Supervisor ──┬──▶ Worker
                             │                        └──▶ Worker
```

### Use Paired Sessions for Architecture and Implementation

#### Two-Session Architect and Implementer Pattern

A practical realization of role-based development with two separate agent sessions:

1. **Architect session** (Session A): Reviews the specification and approved plan, asks clarifying questions, and remains available to review the implementer's output.
2. **Implementer session** (Session B): Receives the approved task scope (for example, "execute tasks 1–3"). When done, the human copies the implementer's summary to the architect for review.
3. **Context reset between chunks**: After the architect signs off on a chunk, reset the implementer's context before starting the next chunk. This prevents context pollution across task boundaries.
4. **Architect checkpoint**: Before reviewing the next chunk, reset the architect to a previous checkpoint state to reduce accumulated context bloat.

This separation ensures that the implementer never accumulates context from previous tasks and that the architect always reviews from a position of architectural intent, not implementation detail.

### Separate Compliance Review from Quality Review

#### Two-Stage Review Pattern

For each implementation task, apply reviews in strict order:

1. **Spec compliance review** — does the implementation match the specification? Acceptance criteria met? Scope respected? No unintended changes?
2. **Code quality review** — does it meet quality and pattern standards? Clean structure? No abstraction bloat? Follows codebase conventions?

The order matters. Code quality review should not begin until spec compliance is confirmed. An implementation that is well-written but does not satisfy the specification is incomplete.

Issues found in either review → implementer fixes → the review stage with issues is repeated. Never proceed to the next task while either review has open issues.

### Define Specialized Subagents Only When Reuse Justifies It

For recurrent tasks, a specialized subagent definition can make delegation more consistent.

```markdown
---
name: security-reviewer
description: Reviews code for security vulnerabilities.
  Invoke when checking for auth issues, injection risks,
  or data exposure.
tools: Read, Grep, Glob
---

You are a security-focused code reviewer. When analyzing code:
1. Check for authentication and authorization gaps
2. Look for injection vulnerabilities (SQL, command, XSS)
3. Identify sensitive data exposure risks
4. Flag insecure dependencies
```

## Practices

- Explicitly state the role when starting a task
- Handoff context between roles cleanly
- Use different context windows for different roles
- Define done criteria for each role
- Log role transitions for traceability
- Delegate already-bounded tasks rather than asking roles to infer their own scope
- Specify the expected output format; subagents should return summaries, not dumps
- Limit tool access where possible
- Avoid unnecessary nesting of subagents
- Apply the two-stage review order consistently

## Anti-patterns

- Skipping either review stage
- Proceeding with unfixed issues from a review
- Dispatching multiple implementation subagents in parallel on overlapping files
- Making a subagent read the full plan file instead of providing only the relevant section
- Omitting scene-setting context
- Ignoring subagent questions
- Treating spec compliance as approximate
- Allowing implementer self-review to substitute for actual review
- Starting code quality review before spec compliance is confirmed
- Moving to the next task while review issues remain open
- Overloading one agent with all roles
- Unclear handoff between roles
- No defined interfaces between subagents
- Roles with overlapping responsibilities
- Subagents returning full context instead of summaries
- Not specifying tool permissions for subagents
- Tasks too large for a single subagent to complete
- Expecting subagents to share context directly
- Reversing the review order

## Indicators

- Frequency of handoff failures or rework caused by unclear delegation
- Number of roles combined into one session for complex tasks
- Rate at which review catches issues missed by the implementer
- Amount of overlapping file ownership across parallel agent tasks
