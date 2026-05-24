---
layout: post
title: "Towards a Pattern Language for Agentic Coding"
author: Alex Serban
date: 2026-05-23 00:00:00-0000
comments: True
description: "Agentic coding is now an engineering practice rather than a novelty. This article studies its recurrent failure modes and proposes nine foundational patterns for disciplined human-AI software development."
image: https://www.reddit.com/media?url=https%3A%2F%2Fpreview.redd.it%2F18-months-of-agentic-coding-no-vibes-or-slop-allowed-v0-7aw1pfvnfoig1.jpg%3Fwidth%3D5504%26format%3Dpjpg%26auto%3Dwebp%26s%3D30e0a68b70416acc2e5fc929d5269f3d5c63a4d4
image:  /assets/img/18-months.webp
photocredit: "Image from 18 Months of Agentic Coding: No Vibes or Slop Allowed "
---

Agentic coding is no longer a tooling novelty. It has become an engineering practice in which developers delegate substantial parts of specification, implementation, and verification to AI agents. Agents can draft and revise code, inspect documentation and repositories, run commands and tests, and update their outputs in response to tool and human feedback. The relevant issue is therefore not only what these systems can produce, but how teams should organise, supervise, and constrain their use in real development settings.

This article examines this issue. It focuses on recurrent difficulties that arise when coding agents are used on non-trivial, long-lived codebases, and argues that these difficulties create demand for more explicit process structure. The argument is not that such structure eliminates the risks introduced by agentic coding. Rather that it provides a way to make delegation more deliberate, reviewable, and reversible. 
This need follows from a broader shift in the bottleneck of software development: code generation is becoming cheaper, while supervision, verification, review, and recovery remain costly. When software can be produced faster than it can be understood or rolled back, the engineering problem shifts from generation to control.

Against this background, the article introduces an initial set of nine patterns for agentic coding. The patterns are organised around the lifecycle of human-AI collaborative development, and are intended as a compact vocabulary for describing how teams can structure work around coding agents, not as a fixed method or a validated guarantee of improvement.

A more compact version of the argument is also available in the presentation [Agentic Coding](/assets/pdf/agentic_coding.pdf).


### From Vibe Coding to Agentic Coding

The earliest widely discussed form of AI-assisted programming was what Karpathy described as *vibe coding*: a style in which the developer states an outcome, accepts generated code with little inspection, and uses execution feedback rather than code reading to steer the next step [[1]](#ref1). For prototypes, disposable scripts, and exploratory work, this can be effective.

The same compression becomes a liability once the artefact must be maintained, reviewed, or trusted. Vibe coding treats code as disposable output. Engineering cannot. Long-lived systems require traceability, comprehensibility, and controlled change. The question is not only whether the model can produce plausible code, but whether a team can verify, explain, and maintain it over time.

We use the term *agentic coding* here for the more disciplined form of this practice. The developer still scopes the task, curates context, sets constraints, validates outputs, and preserves reversibility. The agent is productive, but not authoritative. Its outputs remain drafts under engineering control.

| Aspect | Vibe Coding | Agentic Coding |
|---|---|---|
| Primary goal | Speed of generation | Reliability of supervised generation |
| Role of developer | Prompt and inspect outcomes | Specify, constrain, verify, and maintain |
| Suitable scope | Disposable or bounded work | Long-lived, shared codebases |
| Failure handling | Regenerate | Diagnose, verify, rollback, retry |
| Knowledge requirement | Low | Sufficient to review and explain |

The distinction is not stylistic. It is organisational. Agentic coding, in this more disciplined sense, adds explicit controls because the cost of silent error is higher than the cost of slower generation.


### Why Existing Practice Breaks Down

The need for patterns becomes clearer once we look at how current agentic practice fails. The evidence is heterogeneous, but the failure signals are recurrent. They do not simply reflect immature models. Many also reflect weak workflow controls, oversized task scopes, and insufficient verification.

- **Process distortion.** AI assistance can increase the rate of code generation without increasing the rate of review or integration. Faros AI and Google's DORA reporting, for example, associates high AI adoption with more merged pull requests, but also with larger change sets and longer review times [[3]](#ref3). The likely effect is not a uniformly faster process, but a shifted bottleneck. Review absorbs the saved effort.

- **Quality and security deficits.** Generated code often fails in a specifically dangerous way: it is plausible before it is correct. Veracode reports that about 45% of AI-generated code contains security flaws [[4]](#ref4). Comparative evidence also suggests higher rates of logic errors and cross-site scripting vulnerabilities than in human-written code [[5]](#ref5). These issues are hard to detect through superficial reading because the output is usually syntactically valid and coherent.

- **Agent-specific failure modes.** Practitioners also report failure modes that are distinctive to agentic workflows:
	- **Assumption propagation.** An early misunderstanding is carried forward through many locally consistent steps.
	- **Abstraction bloat.** The agent overproduces structure, dependencies, or indirection relative to the problem.
	- **Dead code accumulation.** Discarded approaches, debug traces, and stale documentation remain in place.
	- **Sycophantic execution.** The agent proceeds confidently through ambiguity instead of surfacing it.
	- **Context drift.** Long sessions accumulate stale facts and lose the operative constraints.

Taken together, these issues suggest that the main engineering challenge is not code generation itself, but the design of more reliable supervisory workflows around it. This does not mean that better process design removes these issues. It means process design is one of the few levers teams can actively control.

### Why a Pattern Language?

Patterns are useful when a field is neither fully ad hoc nor fully formalised. In the sense introduced by Alexander [[6]](#ref6) and adapted to software design by Gamma et al. [[7]](#ref7), a pattern names a recurring problem in context together with a proven direction of solution. Patterns do not replace judgment. They structure it.

Agentic coding is now at that stage. Tooling changes quickly. Model behaviour remains unstable. No single workflow generalises cleanly across domains. Yet the same pressures recur often enough to justify named responses, even if the effects of those responses are not yet well established.

Framing these responses as patterns has three advantages. It shifts attention from tool-specific features to workflow-level invariants. It supports comparison and refinement across teams. And it provides a vocabulary that is concise enough for practice while abstract enough to survive changes in models, editors, and orchestration frameworks.

The nine patterns below should therefore be read as a first organising layer for the engineering of agent-based software development, not as a complete method and not as evidence-backed guarantees of improvement.

### The Pattern Set

The patterns presented here align with a simple iterative workflow:

```
SPECIFY -> VALIDATE -> PLAN -> VALIDATE -> IMPLEMENT -> VALIDATE
```

This loop is intentionally narrow. Each stage produces an artefact that should be checked before the next stage begins. Not all patterns belong to a single linear phase, however. Some are tied to a particular point in the workflow, while others operate across the whole process. The table below therefore indicates typical placement rather than a strict phase taxonomy.

| # | Pattern | Typical Placement |
|---|---|---|
| 1 | Agent-Assisted Discovery | Before implementation |
| 2 | Specification-Driven Development | Before implementation |
| 3 | Plan-Driven Task Decomposition | Before implementation |
| 4 | Incremental Execution | During implementation |
| 5 | Role-Based Development & Subagents | During implementation |
| 6 | Memory & Context Management | Throughout the workflow |
| 7 | Verification-First Engineering | Throughout the workflow |
| 8 | Rollback & Reversibility | Throughout the workflow |
| 9 | Cleanup & Hygiene | After each step and after task completion |

---
#### Pattern 1 - Agent-Assisted Discovery

*Problem.* Developers often start with only partial understanding of the codebase, architecture, or domain constraints. In agentic workflows, skipping this step is costly because the agent will fill gaps with inference.

*Pattern.* Use the agent first as an exploratory instrument, not as an implementer. Map the local decision surface before changing code: which component owns the behaviour, which dependencies may be affected, and which assumptions matter.

*Correct use.* Ask for explanations, dependency traces, and alternatives before requesting implementation. Validate the findings against code and documents. Record durable discoveries for reuse.

*Failure mode if skipped.* The task starts from a false local model of the system. The resulting errors appear later as implementation defects rather than comprehension defects.

*Full pattern specification:* [Agent-Assisted Discovery](/agentic_patterns/01-agent-assisted-discovery/)

---
#### Pattern 2 - Specification-Driven Development

*Problem.* Agents execute literal instructions well, but they do not reliably resolve ambiguity or infer unstated constraints. Imperative prompts therefore tend to produce brittle output.

*Pattern.* State the task declaratively in terms of goals, constraints, context, and acceptance criteria. Emphasize what must be true at completion, not a rigid script for how to get there [[8]](#ref8).

*Correct use.* Specify the task boundaries explicitly, list prohibitions, and write acceptance criteria that are testable. Use the agent to refine the specification before using it to implement.

*Failure mode if skipped.* The agent solves the prompt it received rather than the problem the developer intended.

*Full pattern specification:* [Specification-Driven Development](/agentic_patterns/02-specification-driven-dev/)

---
#### Pattern 3 - Plan-Driven Task Decomposition

*Problem.* A specification can state what should be achieved without yet defining how the work should be decomposed. Without an intermediate planning step, execution tends to drift or absorb too much scope at once.

*Pattern.* Translate the specification into an ordered plan of atomic tasks. Each task should have a narrow objective, explicit dependencies, scoped context, and a clear verification point.

*Correct use.* Ask the agent to draft the plan, but review and refine it before implementation begins. The plan should define the execution order and task boundaries rather than leaving those choices implicit.

*Failure mode if skipped.* Execution begins directly from the specification, so decomposition happens implicitly during implementation. The result is usually drift, scope inflation, or poorly bounded tasks.

*Full pattern specification:* [Plan-Driven Task Decomposition](/agentic_patterns/03-plan-driven-task-decomposition/)

---
#### Pattern 4 - Incremental Execution

*Problem.* Large agent-issued changes are hard to inspect, validate, and unwind. Errors introduced early are often discovered only after later steps depend on them.

*Pattern.* Execute in small, independently verifiable units. Each step should have a narrow scope, an explicit validation action, and a clear stopping point. Reliability tends to decay as edit breadth increases.

*Correct use.* Prefer one coherent slice at a time, validate immediately, and move forward only from a known-good state.

*Failure mode if skipped.* A single session creates an entangled change set whose internal assumptions cannot be isolated or tested cheaply.

*Full pattern specification:* [Incremental Execution](/agentic_patterns/04-incremental-execution/)

---
#### Pattern 5 - Role-Based Development & Subagents

*Problem.* Single long-running sessions mix exploration, design, implementation, and review into one context stream. This creates context pollution and weakens specialization.

*Pattern.* Separate roles across fresh agents or subagents with scoped context. Typical roles include explorer, implementer, spec reviewer, and code reviewer. The key principle is isolation with structured handoff.

*Correct use.* Delegate non-overlapping tasks, pass concise summaries rather than whole transcripts, and sequence review roles explicitly.

*Failure mode if skipped.* The same agent both creates and legitimizes a solution while operating under stale or overloaded context.

*Full pattern specification:* [Role-Based Development & Subagents](/agentic_patterns/05-role-based-development/)

---
#### Pattern 6 - Memory & Context Management

*Problem.* Agents do not retain stable project memory across sessions, and large contexts degrade rather than simply accumulate. Without explicit memory artefacts, teams either reload context repeatedly or let the model guess.

*Pattern.* Treat context as a controlled input. Package only the relevant code, constraints, examples, and decisions for the current task. Externalize durable state into files such as decision logs, plan documents, or reusable skills [[9]](#ref9).

*Correct use.* Start new sessions often, summarize completed work, and curate both inclusions and exclusions.

*Failure mode if skipped.* The agent operates on partial, stale, or polluted context and compensates through hallucinated continuity.

*Full pattern specification:* [Memory & Context Management](/agentic_patterns/06-memory-context-management/)

---
#### Pattern 7 - Verification-First Engineering

*Problem.* Agent output is often convincing before it is correct. Human intuition alone is not a sufficient filter, especially when defects are semantic rather than syntactic.

*Pattern.* Make verification the dominant control loop around every agent step. This includes executable checks, review of the actual diff, and scrutiny of unnecessary complexity. The key question is not whether the agent claims the task is complete, but whether independent checks support that claim.

*Correct use.* Run the cheapest discriminating validation immediately after each edit, review the resulting changes, and reject outputs that cannot be explained clearly [[10]](#ref10).

*Failure mode if skipped.* Plausible but wrong code enters the codebase because no stage in the workflow was designed to falsify it.

*Full pattern specification:* [Verification-First Engineering](/agentic_patterns/07-verification-first/)

---
#### Pattern 8 - Rollback & Reversibility

*Problem.* Agentic sessions can create many dependent edits in a short time. Without checkpoints, recovery often means abandoning the whole session rather than undoing the faulty step.

*Pattern.* Build recovery into the workflow through checkpoint commits, isolated branches, or worktrees. Reversibility should be treated as a design property of the process, not as an emergency measure.

*Correct use.* Commit after each verified unit of work and keep rollback targets semantically meaningful, not merely chronological.

*Failure mode if skipped.* Recovery becomes so expensive that teams tolerate bad intermediate states or discard useful work wholesale.

*Full pattern specification:* [Rollback & Reversibility](/agentic_patterns/08-rollback-reversibility/)

---
#### Pattern 9 - Cleanup & Hygiene

*Problem.* Agents optimise for apparent task completion, not for leaving the repository in a clean long-term state. Residue accumulates easily: temporary files, unused imports, commented-out code, outdated text, and debugging artefacts.

*Pattern.* Make cleanup an explicit phase of the workflow at three levels: after each step, after each task, and periodically across the codebase. Hygiene is part of the definition of done.

*Correct use.* Remove scaffolding and leftovers immediately, update affected documentation, and use automation where possible to detect common residue.

*Failure mode if skipped.* The apparent gains of agentic speed are repaid as maintenance debt.

*Full pattern specification:* [Cleanup & Hygiene](/agentic_patterns/09-cleanup-hygiene/)

---
### Discussion

These patterns are meant to compose. Discovery improves specification quality. Specification supports planning. Planning makes incremental execution more reliable. Role separation determines how execution and review are distributed across agents or sessions. Verification is stronger when rollback points exist. Memory practices determine whether each role receives the right context. Cleanup prevents each task from leaving hidden liabilities for the next one.

The patterns are also intentionally conservative. They do not assume that better models will remove the need for engineering discipline. More capable agents may increase that need because they increase the speed at which wrong assumptions can spread.

One limitation should be stated directly: patterns do not substitute for technical judgment, and we do not claim that they independently resolve the failure modes discussed earlier. Their value depends on the developer's ability to review diffs, decompose tasks, write specifications, design useful checks, and decide when an agent should stop. Agentic workflows amplify engineering competence; they do not replace it.

### Conclusion

Agentic coding should now be studied as an engineering practice, not only as a model capability demonstration. The central question is not whether agents can generate code, but how developers can use them in ways that remain understandable, verifiable, and maintainable over time.

The case for a pattern language follows from this need. When teams repeatedly encounter the same failures and converge on similar countermeasures, naming those countermeasures becomes useful. It enables comparison, reuse, critique, and refinement. It does not by itself show that the countermeasures solve the underlying problems.

The nine patterns presented here offer a compact vocabulary for that purpose. They do not form a complete method. They provide an initial structure for supervised generation: discovery before action, specification before planning, planning before execution, verification before trust, rollback before regret, and cleanup before closure. Their strongest claim is practical and organisational, not causal.

The evidence behind this argument is still uneven. Some claims rest on empirical studies, others on industry reports or practitioner accounts. This is a limitation of the present moment, but also part of the point: practice is moving faster than formalisation. A pattern language is useful precisely in that interval.

If vibe coding asks only whether something appears to work, agentic coding, in this more disciplined sense, asks a stricter question: can the result be justified, checked, and maintained over time?

---

## References

The sources below mix empirical studies, industry reports, and practitioner accounts. They are used differently in the article: empirical studies support claims about quality and process effects; industry reports illustrate current adoption and workflow impact; practitioner sources mainly help define emerging terms and practices.

<a name="ref1"></a>[1] Karpathy, A. (2025). Twitter/X post introducing "vibe coding". Practitioner source. February 2, 2025. [https://x.com/karpathy/status/1886192184808149238](https://x.com/karpathy/status/1886192184808149238)

<a name="ref2"></a>[2] Ronacher, A. [@mitsuhiko]. (2026). Poll: "How much code do you still write yourself?" Twitter/X poll. Practitioner signal. January 11, 2026.

<a name="ref3"></a>[3] Faros AI / Google DORA Report. (2025). AI Adoption in Software Engineering: Impact on Development Workflows. Industry report.

<a name="ref4"></a>[4] Veracode. (2024). AI-Generated Code Security Risks. Industry study. [https://www.veracode.com/blog/ai-generated-code-security-risks/](https://www.veracode.com/blog/ai-generated-code-security-risks/)

<a name="ref5"></a>[5] Hamer, J., et al. (2024). An empirical study of code quality in AI-generated vs. human-written code. Empirical study. *ACM Digital Library*. [https://dl.acm.org/doi/10.1145/3716848](https://dl.acm.org/doi/10.1145/3716848)

<a name="ref6"></a>[6] Alexander, C., Ishikawa, S., & Silverstein, M. (1977). *A Pattern Language: Towns, Buildings, Construction*. Foundational theory.

<a name="ref7"></a>[7] Gamma, E., Helm, R., Johnson, R., & Vlissides, J. (1994). *Design Patterns: Elements of Reusable Object-Oriented Software*. Foundational theory.

<a name="ref8"></a>[8] Addyo. (2025). How to write a good spec for AI agents. Practitioner essay. [https://addyo.substack.com/p/how-to-write-a-good-spec-for-ai-agents](https://addyo.substack.com/p/how-to-write-a-good-spec-for-ai-agents)

<a name="ref9"></a>[9] Anthropic. (2025). *The Complete Guide to Building Skills for Claude*. Vendor documentation.

<a name="ref10"></a>[10] Addyo. (2025). My LLM coding workflow. Practitioner essay. [https://addyo.substack.com/p/my-llm-coding-workflow-going-into](https://addyo.substack.com/p/my-llm-coding-workflow-going-into)
