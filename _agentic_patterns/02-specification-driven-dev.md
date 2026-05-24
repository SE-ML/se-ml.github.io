---
layout: agentic_pattern
author: Alex Serban
name: Specification-Driven Development
title: Specification-Driven Development
category: Specification
unique_id: spec_driven
index: 2
phase: Planning
comments: True
description: Define tasks declaratively before implementation begins.
image: /assets/img/specs.png

intent: State the task declaratively in terms of goals, constraints, context, and acceptance criteria rather than relying on imperative prompts.
problem: Agents execute literal instructions well, but they do not reliably resolve ambiguity or infer unstated constraints. Imperative prompts therefore tend to produce brittle output.
pattern: State the task declaratively in terms of goals, constraints, context, and acceptance criteria. Emphasize what must be true at completion, not a rigid script for how to get there.
correct_use: Specify the task boundaries explicitly, list prohibitions, and write acceptance criteria that are testable. Use the agent to refine the specification before using it to implement.
failure_mode: The agent solves the prompt it received rather than the problem the developer intended.
related: Agent-Assisted Discovery, Structured Output Contracts
dependencies: Should follow discovery phase
---

## Rationale

Coding agents are strong at executing instructions but weaker at reconstructing missing intent. If requirements remain implicit, ambiguous, or mixed with low-level directions, the agent often follows the wording literally while missing the underlying objective.

This makes the main problem different from ordinary programming. In conventional development, the same person usually writes both the instructions and the code. In agentic workflows, intent is delegated. This delegation creates a gap between what the developer means and what the agent implements. A specification helps narrow that gap.

Common consequences of imperative prompting include:

- Brittle, over-specified prompts
- Literal execution of underspecified instructions
- Missed intent when edge cases arise
- Difficulty adapting when circumstances change

## How to Apply the Pattern

Write the specification before asking the agent to implement. A useful specification usually has five parts:

| Component | Purpose | Example |
|-----------|---------|---------|
| **Goal** | States the desired end condition | "Users can authenticate with OAuth" |
| **Constraints** | Defines boundaries and prohibitions | "Do not modify the database schema" |
| **Context** | Supplies relevant technical or business background | "This is a legacy Python 2.7 system" |
| **Acceptance Criteria** | Defines verifiable completion conditions | "All existing tests pass" |
| **Out of Scope** | States what should not be attempted | "No redesign of the navigation flow" |

The practical aim is to specify what must be true, what must be avoided, and how completion will be checked.

## Specification Template

```markdown
## Task: [Brief Description]

### Goal
[What should be true when this is complete]

### Constraints
- MUST NOT: [Critical prohibitions]
- MUST: [Critical requirements]
- PREFER: [Soft preferences]

### Context
- [Relevant technical context]
- [Business context if applicable]
- [Related previous work]

### Acceptance Criteria
- [ ] [Verifiable criterion 1]
- [ ] [Verifiable criterion 2]
- [ ] [Verifiable criterion 3]

### Out of Scope
- [Explicitly excluded items]
```

## Supporting Practices

### Refine the Specification Before Implementation

Agents can help develop specifications, not only consume them.

1. Start from a rough task description.
2. Ask the agent to draft a specification.
3. Ask the agent to identify ambiguity, omissions, and edge cases.
4. Review and revise the specification.
5. Use the approved version to guide implementation.

Useful critique prompts include:

- "Review this specification. What is ambiguous or underspecified?"
- "What edge cases are not covered?"
- "What could go wrong if an agent implements this literally?"
- "Which acceptance criteria are missing?"

### Use LLMs to Write Better Specifications

LLMs can be useful during specification writing, but their role should be bounded. They are effective at turning a rough idea into a more explicit task description, surfacing missing constraints, proposing edge cases, and reformatting the result into a stable template. They are less reliable as arbiters of product intent or project truth. The developer still needs to decide what the task is, what trade-offs are acceptable, and which constraints are real.

A practical workflow is:

1. Start with a short statement of the task in plain language.
2. Ask the LLM to convert it into a structured specification with goals, constraints, context, acceptance criteria, and explicit task boundaries.
3. Ask the LLM to critique that draft for ambiguity, omissions, conflicting constraints, and missing edge cases.
4. Revise the specification manually.
5. Use the revised version as the implementation artefact.

Useful prompts include:

- "Turn this rough task description into a specification with goals, constraints, context, acceptance criteria, and out-of-scope items."
- "What in this specification is ambiguous or likely to be interpreted too literally?"
- "Which constraints are missing if I want to keep the change narrowly scoped?"
- "Which acceptance criteria would let me verify this task objectively?"

The key discipline is that the LLM may help draft and critique the specification, but it should not silently define the task on the developer's behalf.

### Prefer Declarative Framing

The relevant distinction is between describing *what* should hold at the end of the task and prescribing *how* the agent should proceed step by step. Declarative framing usually gives the agent enough flexibility to adapt while still constraining the result through goals and checks.

This does not remove the need for oversight. It means that effective use of coding agents depends heavily on specifying intent precisely, stating exclusions explicitly, and verifying that the output matches the intended result.

### Treat Specifications as Reusable Artefacts

Specifications are stronger than one-off prompts because they can be reviewed, revised, and reused across sessions.

| | Prompts | Specifications |
|---|---|---|
| **Persistence** | Ephemeral and session-bound | Persistent and reusable |
| **Reviewability** | Difficult to inspect collaboratively | Reviewable as project artefacts |
| **Rationale** | Often implicit | Can record why options were chosen or excluded |
| **Reusability** | Usually limited to one exchange | Reusable across sessions and contributors |

### Use the Double-Spec Pattern in Legacy Systems

When the current system behaviour is unclear, write two specifications before making changes:

1. A specification of what the system currently does
2. A specification of what it should do after the change

The gap between these two specifications defines the change surface more clearly and reduces the risk of accidental regressions.

## Anti-patterns

- Step-by-step instructions that over-constrain the solution
- Ambiguous goals such as "make it better"
- Missing constraints that allow unrelated changes
- Missing acceptance criteria
- Specifications that describe how rather than what
- One-off prompts instead of persistent specification files

## Indicators

- Amount of rework caused by misunderstood requirements
- Frequency of scope drift during implementation
- Share of tasks with explicit acceptance criteria before implementation

## Example

**Less effective:**

```text
Add a login button to the header that calls the auth API when clicked
and shows a loading spinner and handles errors with a toast message.
```

**More effective:**

```markdown
## Goal
Users can initiate authentication from any page in the application.

## Constraints
- MUST NOT modify existing header layout
- MUST use existing Button component from design system
- MUST follow current error handling patterns

## Acceptance Criteria
- [ ] Login button visible in header
- [ ] Clicking button initiates OAuth flow
- [ ] Loading state shown during authentication
- [ ] Errors displayed using existing toast system
- [ ] All existing tests pass
```
