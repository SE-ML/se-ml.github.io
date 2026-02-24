# Team Practices Reference

All 4 practices from the SE-ML catalogue Team category (`05-*`).
All practices are **process and culture-based** — assessment relies on
self-report. No artifact can fully confirm or deny adherence.

Recommended adoption order: **team_collab → team_communication → team_backlog → tradeoff**

---

## team_collab — Use a Collaborative Development Platform

**Difficulty:** basic  
**Intent:** Enable teams to work together more effectively through consistent
use of a shared platform.  
**Motivation:** Collaborative platforms provide shared access to code, data,
experiments, issues, and documentation. Without one, knowledge is siloed,
decisions are hard to trace back, and remote/async collaboration breaks down.
For ML teams specifically, platforms with experiment tracking and model registry
capabilities are particularly valuable.  
**Applicability:** Any ML team.

**What to check (EVALUATE/DETECT):**
- Is there a single agreed platform all team members use consistently?
- Does it support version control, issue tracking, and CI/CD at minimum?
- Are ML-specific capabilities in use: experiment tracking, model registry,
  dataset versioning?
- Are all team members using the platform (or is it mixed with personal drives,
  email, etc.)?

**Platform tiers to consider:**
| Need | Options |
|------|---------|
| Code + issues + CI | GitHub, GitLab, Azure DevOps |
| ML experiments | MLflow, Weights & Biases, Neptune, Comet |
| Data versioning | DVC, Delta Lake, LakeFS |
| All-in-one ML | Databricks, SageMaker Studio |

**Related:** team_backlog, exp_versioning (Training), exp_status (Training)

---

## team_communication — Communicate, Align, and Collaborate with Others

**Difficulty:** basic  
**Intent:** Ensure alignment with other teams, management, and external stakeholders.  
**Motivation:** ML systems integrate with infrastructure, business processes, and
other software systems. Siloed development leads to integration failures,
misaligned priorities, and missed requirements. Frequent communication with
stakeholders outside the team is not overhead — it is the mechanism by which
the team stays connected to actual goals.  
**Applicability:** Any ML team.

**What to check (EVALUATE/DETECT):**
- Does the team have regular touchpoints with adjacent teams (data engineering,
  platform/infra, product)?
- Are stakeholders kept informed of experiment outcomes and model status?
- Is there a shared way of working (tools, conventions) with adjacent teams?
- Are blockers or impediments communicated upward promptly?

**Assist — communication rhythm checklist:**
- [ ] Weekly sync with product owner / business stakeholder
- [ ] Bi-weekly or monthly demo of experiment progress
- [ ] Shared Slack/Teams channel with data engineering or infra
- [ ] Incident communication protocol defined (who to notify, when)

---

## team_backlog — Work Against a Shared Backlog

**Difficulty:** medium  
**Intent:** Avoid misunderstandings on the content, priority, and status of tasks.  
**Motivation:** A maintained backlog is the single source of truth for what the
team is working on and why. It enables external stakeholders to understand
priorities, supports async coordination, and creates a traceable record of
decisions and agreements.  
**Applicability:** Any ML team.

**What to check (EVALUATE/DETECT):**
- Is there an issue tracker actively used by the whole team?
- Does the backlog include both engineering and ML/experiment tasks (not just bugs)?
- Is the backlog regularly groomed (stale items removed or re-prioritised)?
- Does a product owner or equivalent maintain priorities with stakeholder input?

**Assist — ML-adapted backlog item template:**
```
Title: [Clear, action-oriented description]
Type: [Feature / Experiment / Bug / Technical Debt / Governance]
Priority: [Critical / High / Medium / Low]
Objective: [What we expect to learn or achieve]
Acceptance criteria: [How we know this is done]
Effort estimate: [S / M / L]
Dependencies: [Other items or external systems]
Notes: [Context, links to experiments, data sources]
```

**Related:** team_collab

---

## tradeoff — Decide Trade-offs Through a Defined Team Process

**Difficulty:** medium  
**Intent:** Define methodology for generating, evaluating, prioritising, and
selecting solution alternatives.  
**Motivation:** ML development is a multi-objective optimisation problem under
uncertainty: accuracy vs. interpretability, performance vs. cost, speed vs.
fairness. Without a shared decision process, these trade-offs are resolved
inconsistently, reversed later, or create team conflict. A defined process
empowers individuals to act without waiting for a decision-maker.  
**Applicability:** Any ML team — especially valuable for recurring trade-off
decisions (model choice, deployment strategy, fairness thresholds).

**What to check (EVALUATE/DETECT):**
- Does the team have a documented decision process for trade-offs?
- Are trade-off decisions recorded (not just made verbally and forgotten)?
- Are ML-specific quality dimensions included: accuracy, interpretability,
  latency, cost, fairness, privacy?
- Can team members make decisions in the absence of senior members?

**Assist — minimal trade-off decision record template:**
```markdown
## Decision: [Short title]
Date: YYYY-MM-DD | Owner: [name] | Status: [Decided / Under review]

### Problem
[What trade-off needed to be made and why]

### Options considered
| Option | Pros | Cons | Score |
|--------|------|------|-------|
| A | ... | ... | ... |
| B | ... | ... | ... |

### Decision
[Which option was chosen and why]

### Constraints and assumptions
[What assumptions this decision rests on; what would change it]

### Review trigger
[When or under what conditions this decision should be revisited]
```

**Related:** interpretable (Training), risk (Governance)
