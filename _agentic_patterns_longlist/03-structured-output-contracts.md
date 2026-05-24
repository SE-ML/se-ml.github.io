---
layout: agentic_pattern
author: Alex Serban
name: Structured Output Contracts
title: Structured Output Contracts
category: Specification
unique_id: structured_output
index: 3
phase: Planning
comments: True
description: Enforce predictable output formats through schemas to enable reliable parsing, type safety, and clear interfaces between agents.

intent: Enforce predictable output formats through schemas to enable reliable parsing, type safety, and clear interfaces between agents.
problem: Free-form agent outputs require complex parsing logic, vary unpredictably between invocations, break downstream processes, and make verification difficult.
solution: Define explicit schemas for agent outputs using Pydantic, JSON Schema, or TypeScript interfaces.
related: Specification-Driven Development, Workflow Orchestration Patterns
dependencies: Works in conjunction with specification patterns
---

Free-form agent outputs:
- Require complex parsing logic
- Vary unpredictably between invocations
- Break downstream processes
- Make verification difficult

## Solution

Define explicit schemas for agent outputs:

```python
from pydantic import BaseModel, Field
from typing import Literal

class CodeChange(BaseModel):
    file_path: str = Field(description="Path to file to modify")
    action: Literal["create", "modify", "delete"]
    description: str = Field(description="What the change does")
    code: str = Field(description="The code to add or modify")

class TaskResult(BaseModel):
    status: Literal["success", "failure", "needs_clarification"]
    summary: str = Field(description="What was accomplished")
    changes: list[CodeChange] = Field(default_factory=list)
    next_steps: list[str] | None = None
```

## Practices

- Use Pydantic, JSON Schema, or TypeScript interfaces
- Validate outputs against schema before processing
- Include `Literal` types for routing decisions
- Document schema expectations in prompts
- Version schemas when they change

## Anti-patterns

- ❌ Parsing free-form text with regex
- ❌ Assuming consistent formatting without enforcement
- ❌ No validation before using outputs

## Benefits

| Benefit | Description |
|---------|-------------|
| **Predictability** | Same structure every time |
| **Type Safety** | Compile-time checks possible |
| **Tooling** | IDE autocompletion, validation |
| **Integration** | Easy to chain with other systems |
| **Testing** | Clear contract to test against |
