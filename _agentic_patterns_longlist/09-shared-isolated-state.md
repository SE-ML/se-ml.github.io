---
layout: agentic_pattern
author: Alex Serban
name: Shared vs. Isolated State
title: Shared vs. Isolated State
category: Context & State
unique_id: shared_isolated
index: 9
phase: Ongoing
comments: True
description: Decide whether agents share a common scratchpad or maintain isolated state, based on collaboration needs.

intent: Decide whether agents share a common scratchpad or maintain isolated state, based on collaboration needs.
problem: Choosing the wrong state management approach leads to either context pollution and privacy concerns (shared) or lost intermediate reasoning and coordination overhead (isolated).
solution: Choose state management approach based on specific criteria - use shared state when agents need to see each other's reasoning, use isolated state when only final results matter.
related: Memory & Context Management, Role-Based Development & Subagents
dependencies: Works with memory and role-based patterns
---

## Trade-offs

| Approach | Pros | Cons |
|----------|------|------|
| **Shared Scratchpad** | Full visibility, collaboration, can see reasoning | Verbose, context pollution, privacy concerns |
| **Isolated + Handoff** | Focused context, cleaner, parallel execution | May lose intermediate reasoning, coordination overhead |

## Selection Criteria

### Use Shared State when:
- Agents need to see each other's reasoning steps
- Debugging requires full trace
- Tasks are tightly coupled
- Sequential execution

### Use Isolated State when:
- Only final results matter
- Parallel execution needed
- Context is role-specific
- Privacy/security concerns

## Hybrid Approach

```
Isolated working memory ──▶ Publish final result ──▶ Shared results store
                                                          │
                                                          ▼
                                              Other agents can read
```

This approach gives you the best of both worlds:
- Each agent works in isolation without context pollution
- Final results are shared for coordination
- Intermediate reasoning can be logged for debugging if needed

## Practices

- Default to isolated state for most multi-agent scenarios
- Use shared state deliberately when collaboration is essential
- Log intermediate state for debugging even when isolated
- Define clear interfaces for state handoff

## Anti-patterns

- ❌ Sharing all state by default
- ❌ No state persistence between agent invocations
- ❌ Unclear boundaries on what's shared vs. private
