---
layout: agentic_pattern
author: Alex Serban
name: Verification-First Engineering
title: Verification-First Engineering
category: Verification
unique_id: verification_first
index: 10
phase: Continuous
comments: True
description: Make verification the dominant control loop around each agent step.
image: /assets/img/ver.png

intent: Make verification the dominant control loop around each agent step through executable checks, diff review, and scrutiny of unnecessary complexity.
problem: Agent output is often convincing before it is correct. Human intuition alone is not a sufficient filter, especially when defects are semantic rather than syntactic.
pattern: Make verification the dominant control loop around every agent step. This includes executable checks, review of the actual diff, and scrutiny of unnecessary complexity. The key question is not whether the agent claims the task is complete, but whether independent checks support that claim.
correct_use: Run the cheapest discriminating validation immediately after each edit, review the resulting changes, and reject outputs that cannot be explained clearly.
failure_mode: Plausible but wrong code enters the codebase because no stage in the workflow was designed to falsify it.
related: Self-Reflection & Critique, Incremental Execution
dependencies: Works with all execution patterns
---

## Rationale

Verification should be driven by explicit success criteria rather than trust in the initial output. The value lies in making the agent iterate against independent checks.

Common verification targets include:

- Syntactically correct but semantically wrong code
- Plausible-looking but incorrect solutions
- Code that works in isolation but breaks integration
- Hallucinated APIs or non-existent functions

The main issue is not only that agents can be wrong. It is that they are often wrong in ways that look locally plausible. Verification therefore needs to be designed as a mechanism for falsification rather than as a final sanity check.

## How to Apply the Pattern

Verification should be specified before trust is granted.

1. Define objective success criteria for the task.
2. Choose the cheapest checks that could disconfirm the current output.
3. Run those checks immediately after each edit or step.
4. Review the actual diff and resulting complexity, not only the command output.
5. Continue only when the current slice is independently supported.

In practice, this means verification is not a single late-stage activity. It is the main control loop around execution.

## Supporting Practices

### Use Layered Verification

Different checks catch different classes of failure.

| Layer | Mechanism | When | Catches |
|-------|-----------|------|---------|
| **Syntax** | Parse or compile | Every edit | Syntax errors |
| **Static** | Linting, type checking | Every edit | Type errors, style issues |
| **Unit** | Automated tests | After implementation | Logic errors |
| **Integration** | System tests | After integration | Interface errors |
| **Complexity** | Code review, metrics | After implementation | Abstraction bloat, over-engineering |
| **Cleanup** | Diff review, dead code analysis | After implementation | Leftover code, unintended changes |
| **Human** | Code review | Before merge | Design issues, edge cases |

### Design Verification to Catch Common Failure Modes

| Failure Mode | Description | Why It Happens |
|--------------|-------------|----------------|
| **Assumption Propagation** | Model misunderstands early, builds entire feature on faulty premises | You don't notice until 5 PRs deep and architecture is cemented |
| **Abstraction Bloat** | 1,000 lines where 100 would suffice | Agents optimise for looking comprehensive, not maintainability |
| **Dead Code Accumulation** | Old implementations linger, unrelated code altered | Agents don't clean up after themselves |
| **Sycophantic Agreement** | No pushback on incomplete requirements | Enthusiastic execution of whatever you described |

### Keep the Verification Loop Tight

```
Agent Output
     │
     ▼
┌────────────┐   fail   ┌──────────────┐
│   Parse    │────────▶   Fix Syntax   
└─────┬──────┘          └──────┬───────┘
     │ pass                    │ retry
     ▼                         └──────────↺
┌────────────┐   fail   ┌──────────────┐
│    Lint    │────────▶   Fix Issues  
└─────┬──────┘          └──────┬───────┘
     │ pass                    │ retry
     ▼                         └──────────↺
┌────────────┐   fail   ┌──────────────┐
│    Test    │────────▶   Fix Logic   
└─────┬──────┘          └──────┬───────┘
     │ pass                    │ retry
     ▼                         └──────────↺
 Verified
```

### Define Explicit Success Criteria

Use objective conditions to determine whether a task is complete.

```markdown
## Success Criteria for This Task

- [ ] All existing tests pass
- [ ] New tests cover the added functionality  
- [ ] No linting errors
- [ ] No type errors
- [ ] Diff shows only intended changes (no dead code)
- [ ] Solution uses ≤ N lines / ≤ N files (complexity gate)
```

The task is complete only when all criteria are satisfied.

### Guard Against Requirement Drift and Sycophantic Testing

AI agents often produce an initial result quickly, but the remaining work still includes edge cases, subtle bugs, security considerations, and architectural coherence. In some cases, the final portion of the task takes longer than expected because the developer must debug code they did not write and do not fully understand.

A related failure mode is **sycophantic testing**: agents write tests that match the implementation they just produced rather than tests that validate the requirements. The result may be a test suite with high coverage but low validation value.

Practical implications for verification:
- Write tests *before* asking the agent to implement (test-driven development prevents sycophantic tests)
- Build test suites that verify **behaviour**, not implementation (integration tests, property-based tests, scenario tests)
- When reviewing AI-generated tests, ask: does this test validate the requirement, or does it just confirm what the code currently does?

### Review Failure Modes Systematically

| Failure Mode | Likely Cause | Fix |
|---|---|---|
| Agent writes code ignoring project conventions | CLAUDE.md/config doesn't capture conventions, or agent didn't read it | Make config more explicit; start session with confirmation of conventions |
| Agent "solves" the problem unexpectedly | Underspecified task; agent optimised for a proxy metric | Add explicit constraints and negative requirements to the spec |
| Agent gets confused mid-session | Context window degradation; early context loses influence | Audit current context, start a fresh session, or re-inject key constraints |
| Agent breaks something unrelated | Insufficient test coverage; scope too broad | Run full test suite after every task; narrow task scope |

### Keep a Human Verification Checklist

Automated checks catch syntax and logic errors, but human review is the only mechanism that catches design issues, unintended scope changes, and the subtle failure modes listed above. Apply this checklist before accepting any non-trivial agent output:

| Check | How | Why |
|---|---|---|
| **Read the code** | Line by line, not just skim | Agents produce plausible-looking but semantically wrong code |
| **Run it yourself** | Execute, test edge cases | "It should work" ≠ it works |
| **Review the diff** | `git diff` — what actually changed? | Catch unintended modifications and dead code accumulation |
| **Understand the approach** | Can you explain it to someone else? | If you can't explain it, you can't maintain it |
| **Question complexity** | Could this be simpler? | Push back on abstraction bloat proactively |
| **Verify requirements met** | Check against the original specification | Agents solve what they understood, not necessarily what you meant |

Code that cannot be explained clearly should not be accepted without further review. Accepting code that is not understood creates a maintenance liability.

## Practices

- Run static checks automatically after each agent edit
- Write tests before asking agents to implement
- Ask agents to verify their own work ("check if this compiles")
- Use multiple verification methods in combination
- Automate verification in CI/CD
- Verify early so assumption propagation is caught before it compounds
- Check whether the solution could be simpler
- Review cleanup explicitly by checking the diff for unintended changes and dead code
- Use objective criteria such as tests and linters rather than subjective impressions

## Anti-patterns

- Accepting agent code without running it
- Skipping tests because the code appears plausible
- Verifying only at the end of a large change
- Trusting claims that code "should work" without independent checks
- Not reviewing diffs for unintended changes
- Accepting complex solutions without questioning whether they can be simplified
- Relying on agent self-assessment

## Indicators

- Share of tasks with explicit success criteria before implementation begins
- Time between an edit and its first independent verification step
- Frequency of defects caught by diff review, complexity review, or human review after tests pass
- Rate of regressions caused by changes that were never independently checked
