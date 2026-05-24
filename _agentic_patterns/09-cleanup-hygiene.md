---
layout: agentic_pattern
author: Alex Serban
name: Cleanup & Hygiene
title: Cleanup & Hygiene
category: Maintenance
unique_id: cleanup_hygiene
index: 9
phase: Post-task
comments: True
description: Leave repositories in a clean, reviewable, and maintainable state after agent work.
image: /assets/img/clean.png

intent: Make cleanup an explicit part of the workflow so repositories are left in a clean, reviewable, and maintainable state after agent work.
problem: "Agents optimise for apparent task completion, not for leaving the repository in a clean long-term state. Residue accumulates easily: temporary files, unused imports, commented-out code, outdated text, and debugging artefacts."
pattern: "Make cleanup an explicit phase of the workflow at three levels: after each step, after each task, and periodically across the codebase. Hygiene is part of the definition of done."
correct_use: Remove scaffolding and leftovers immediately, update affected documentation, and use automation where possible to detect common residue.
failure_mode: The apparent gains of agentic speed are repaid as maintenance debt.
related: Traceability, Verification-First Engineering
dependencies: Works with verification and traceability patterns
---

## Rationale

Agents are usually optimised to satisfy the explicit task, not to leave the repository in the cleanest possible long-term state. When no cleanup phase is defined, temporary fixes and leftover artefacts remain in place and gradually accumulate into maintenance burden.

Common cleanup targets include:

- Temporary files
- Debug code and print statements
- Commented-out code
- Incomplete implementations
- Outdated documentation
- Unused imports

The key issue is not only visible mess. Residue also makes future review, modification, and debugging harder by obscuring which parts of the repository are still active and intentional.

## How to Apply the Pattern

Cleanup should be treated as a normal part of task completion rather than as optional polish.

1. Remove local residue after each coherent implementation step.
2. Perform a broader cleanup pass after the task is complete.
3. Periodically remove accumulated repository-wide cruft.
4. Use automated checks where they are reliable.
5. Confirm that cleanup has not hidden real failures or removed important signals.

In practice, cleanup is strongest when it is anticipated in the plan rather than postponed until the end.

## Supporting Practices

### Use Multiple Cleanup Levels

| Level | When | What to Clean |
|-------|------|---------------|
| **Immediate** | After each step | Temp files, debug output |
| **Post-task** | After task completion | Debug code, comments, unused code |
| **Periodic** | After multiple tasks, on PR merge, or on a regular schedule | Accumulated cruft, outdated docs |

### Keep a Cleanup Checklist

```markdown
## Post-Task Cleanup

### Code Hygiene
- [ ] Remove temporary files
- [ ] Remove debug/print statements
- [ ] Remove commented-out code
- [ ] Remove unused imports
- [ ] Format code (prettier, black, etc.)

### Documentation
- [ ] Update README if needed
- [ ] Update API docs if changed
- [ ] Update CHANGELOG
- [ ] Remove outdated comments

### Tests
- [ ] Remove test debugging code
- [ ] Ensure all tests pass
- [ ] Remove skipped tests or document why skipped

### Git
- [ ] Squash WIP commits if appropriate
- [ ] Write clear commit message
- [ ] Remove merged branches
```

### Automate What Can Be Automated

```bash
# Post-agent cleanup script
npm run lint:fix          # Auto-fix linting issues
npm run format            # Format code
npm run test              # Verify tests pass
git diff --stat           # Review changes
```

### Review Common Cleanup Targets

| Target | Detection | Removal |
|--------|-----------|---------|
| **Debug statements** | `console.log`, `print(`, `debugger` | Linter rules |
| **Commented code** | Large comment blocks | Manual review |
| **Unused imports** | IDE/linter warnings | Auto-fix |
| **Temp files** | `.tmp`, `.bak`, `~` suffix | Gitignore + delete |
| **Dead code** | Unreachable code analysis | Linter rules |

## Practices

- Include cleanup as explicit step in plans
- Use linters to catch common hygiene issues
- Review agent output for cleanliness
- Automate what can be automated
- Make cleanup part of the definition of done
- Do not remove failing tests without explicit authorization; failing tests are diagnostic signals, not noise

## Anti-patterns

- Skipping cleanup for later
- Accumulating unresolved TODO comments
- Leaving dead code paths in place
- Merging with debug code
- Relying on manual cleanup for tasks that can be automated

## Indicators

- Number of cleanup-related issues found during review after a task is marked complete
- Frequency of residual debug code, temporary files, or dead code in merged changes
- Share of tasks that include an explicit cleanup step
- Amount of repository maintenance caused by leftover artefacts from prior agent work
