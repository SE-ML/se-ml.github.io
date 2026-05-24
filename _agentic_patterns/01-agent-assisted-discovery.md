---
layout: agentic_pattern
author: Alex Serban
name: Agent-Assisted Discovery
title: Agent-Assisted Discovery
category: Discovery
unique_id: agent_discovery
index: 1
phase: Pre-development
comments: True
description: Use agents to build understanding before implementation begins.

intent: Use agents as exploratory instruments before implementation to build a reliable local model of the codebase, domain, and task constraints.
problem: Both the developer and the agent often begin with an incomplete local model of the codebase, architecture, and domain constraints. In agentic workflows, that missing understanding is costly because the agent will often fill gaps with plausible inference unless the relevant context is surfaced and checked.
pattern: "Use an agent first as an exploratory instrument rather than as an implementer. Map the local decision surface before changing code: which component owns the behaviour, which dependencies may be affected, and which assumptions matter."
correct_use: Ask for explanations, dependency traces, and alternatives before requesting implementation. Validate the findings against code and documents. Record durable discoveries for reuse.
failure_mode: The task begins from a false local model of the system. Resulting errors then appear later as implementation defects rather than comprehension defects.
related: Specification-Driven Development, Memory & Context Management
dependencies: Should be performed before specification writing
---

## Rationale

Discovery is not only a navigation activity. It is also a learning activity. The immediate problem is not simply that the developer lacks information. It is that both the developer and the agent begin with only partial context, but the agent will often continue by inferring what is missing. The developer therefore needs enough understanding to validate, debug, and extend the result. Discovery reduces this avoidable uncertainty before specification and implementation begin.

This is especially important in unfamiliar or poorly documented environments. Common discovery tasks include:

- Navigating undocumented legacy systems
- Understanding domain-specific terminology
- Mapping architecture and dependencies
- Finding relevant code locations
- Learning new frameworks or libraries

## How to Apply the Pattern

Discovery should proceed from broad orientation to narrow verification.

1. Start by locating the relevant subsystem, files, and ownership boundaries.
2. Ask the agent to explain behaviour, dependencies, terminology, and likely side effects.
3. Request alternatives and trade-offs before accepting any proposed direction.
4. Verify the explanation against the codebase and available documentation.
5. Record the resulting understanding in a durable form when it is likely to be needed again in later sessions.

The guiding principle is simple: code or reasoning that cannot be explained clearly is difficult to validate, debug, or extend.

## Useful Question Types

| Discovery Type | Purpose | Example Prompts |
|----------------|---------|-----------------|
| **Codebase exploration** | Identify structure and ownership | "Explain the architecture of this subsystem" |
| **Domain translation** | Clarify local terminology and concepts | "What does this term mean in this project?" |
| **Dependency mapping** | Surface side effects and affected components | "What would break if I change this function?" |
| **Alternative analysis** | Compare plausible approaches | "Show me 2-3 ways to solve this and their trade-offs" |
| **Assumption checking** | Expose uncertainty that needs verification | "What assumptions did you make that I should verify?" |

Useful follow-up prompts include:

- "Why was this approach used here rather than a simpler alternative?"
- "Can you explain this control flow step by step?"
- "Which parts of this answer come from the codebase, and which are inferences?"
- "What should I inspect directly before trusting this explanation?"

## Supporting Practices

### Review Discovery Outputs

Discovery often produces explanations, summaries, and early code suggestions. These should still be reviewed critically.

| Area | Questions to ask |
|---|---|
| **Code Quality** | Is the explanation consistent with the actual code structure and behaviour? |
| **Architecture** | Does the agent identify the correct component boundaries and dependencies? |
| **Testing** | Are relevant tests or verification points identified? |
| **Requirements** | Does the explanation remain aligned with the task rather than drifting into unrelated areas? |

Useful review principles are:

- Classify issues by actual severity
- Refer to specific locations and behaviours
- Explain why an issue matters
- State a clear review outcome

### Use Discovery to Support Brainstorming

When discovery is used to turn an idea into a design or specification, keep the conversation structured.

1. Check the current project state first.
2. Refine the idea one question at a time.
3. Prefer focused or multiple-choice questions where possible.
4. Summarize the resulting design in short sections and validate each section.
5. Write the validated design to a reusable project artefact.

The one-question-per-message discipline is useful because models often answer multiple questions superficially rather than addressing any of them in depth.

### Maintain a Project Brief

For existing codebases, a short project brief can provide targeted context without loading the full repository. A useful brief typically includes:

- Goals and a short architecture overview
- Key technical constraints, stack, and versions in use
- Recently completed work
- Explicit task boundaries or areas that should not be touched
- Pointers to key files, modules, or directories

Update the brief at the end of each session so it can serve as a handover artefact for later work. This is a supporting practice rather than the core of the pattern: Pattern 1 is about surfacing the missing understanding, while Memory and Context Management is about preserving it effectively.

## Anti-patterns

- Trusting agent explanations without verification
- Skipping discovery and moving directly to implementation
- Accepting vague explanations without follow-up questions
- Assuming the agent knows facts it cannot observe
- Accepting code or explanations that cannot be stated clearly

## Indicators

- Time to first meaningful contribution during onboarding or handoff
- Accuracy of agent-provided explanations under spot-checking
- Number of false assumptions identified before implementation

## Example Workflow

```text
1. Initial exploration
   -> "Give me a high-level overview of this codebase structure"

2. Focused investigation
   -> "How does authentication work in this system?"

3. Verification
   -> Read the relevant authentication code to confirm the explanation

4. Documentation
   -> Record findings in a reusable context or project brief
```
