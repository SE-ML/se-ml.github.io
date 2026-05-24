---
layout: agentic_pattern
author: Alex Serban
name: Self-Reflection & Critique
title: Self-Reflection & Critique
category: Verification
unique_id: self_reflection
index: 11
phase: Implementation
comments: True
description: Enable agents to evaluate their own outputs and improve iteratively through self-criticism.

intent: Enable agents to evaluate their own outputs and improve iteratively through self-criticism.
problem: Single-pass generation often produces suboptimal results, agents don't naturally identify their own errors, and there's no learning from mistakes within a session.
solution: Implement reflection mechanisms including self-criticism, hindsight learning, heuristic detection, and memory-augmented reflection.
related: Verification-First Engineering, Human-in-the-Loop Checkpoints
dependencies: Works with verification and coordination patterns
---

## Problem

- Single-pass generation often produces suboptimal results
- Agents don't naturally identify their own errors
- No learning from mistakes within a session

## Solution

Implement reflection mechanisms:

| Mechanism | Description | Implementation |
|-----------|-------------|----------------|
| **Self-criticism** | Agent critiques its own work | "Review your solution for errors" |
| **Hindsight learning** | Learn from sequence of improving outputs | Show past attempts with feedback |
| **Heuristic detection** | Identify hallucination or inefficient planning | Check for repeated actions, verify API existence |
| **Memory-augmented reflection** | Store reflections for future reference | Log insights to persistent memory |

## Reflection Prompt Template

```markdown
You have just produced the following output:
[OUTPUT]

Please reflect on this output:
1. What are potential errors or issues?
2. Does this fully address the requirements?
3. What would you do differently?
4. Rate your confidence (1-10) and explain.

If confidence < 8, revise your output.
```

## ReAct Pattern

The ReAct (Reasoning + Acting) pattern interleaves reasoning with actions:

```
Thought: [What I'm thinking]
Action: [What I'll do]
Observation: [What happened]
... (repeat)
Thought: [Final reasoning]
Answer: [Final answer]
```

This pattern forces explicit reasoning at each step, making it easier to:
- Identify where the agent went wrong
- Understand the agent's decision process
- Intervene when reasoning goes off track

## Confidence Calibration

Use confidence scores to trigger appropriate actions:

| Confidence | Action |
|------------|--------|
| 9-10 | Proceed with minimal review |
| 7-8 | Quick human verification |
| 5-6 | Detailed human review required |
| < 5 | Request clarification or try different approach |

## Practices

- Build reflection into multi-step workflows
- Store reflections for debugging
- Use confidence scores to trigger human review
- Compare outputs against requirements explicitly
- Have agents explain their reasoning before acting

## Anti-patterns

- ❌ Single-pass generation for complex tasks
- ❌ No opportunity for self-correction
- ❌ Ignoring agent uncertainty signals
- ❌ Not logging reflections for debugging
