# Cluster A: Training Foundations

These six practices are **always applicable** regardless of feature engineering
approach, domain, or team maturity. They are the baseline from which everything
else builds. All are rated **basic** difficulty — if any are missing, recommend
them before anything else.

---

## exp_trainingobjective — Share a Clearly Defined Training Objective

**Difficulty:** basic  
**Intent:** Avoid misunderstandings between multi-disciplinary team members.  
**Motivation:** A shared, explicit training objective ensures that data scientists,
engineers, and domain experts are optimising for the same thing. Without it,
team members may pursue conflicting directions without realising it.  
**Applicability:** Any machine learning team should share a clear training objective.

**What to look for (EVALUATE/DETECT):**
- Is the training objective documented in a README, model card, or project doc?
- Is it accessible to all team members, not just the person who ran the first experiment?
- Is it stated in terms understandable to non-ML stakeholders?

**Typical gaps:** Objective exists in someone's head or a notebook comment but
is never formally written down; objective changes mid-project without team alignment.

---

## exp_trainingmetric — Capture the Training Objective in a Metric

**Difficulty:** basic  
**Intent:** Ensure the machine learning objective is easy to measure and is a
good proxy for the *true* objective.  
**Motivation:** If the metric is hard to compute, poorly understood, or a poor
proxy for what you actually care about (e.g. optimising accuracy on imbalanced
data when you care about recall), the whole experimentation loop is optimising
for the wrong thing.  
**Applicability:** All training objectives should be captured in an easy-to-comprehend metric.

**What to look for (EVALUATE/DETECT):**
- Is there an agreed primary metric logged in every experiment?
- Is the metric aligned with the business or product objective?
- Are secondary metrics tracked (e.g. fairness, latency, calibration)?

**Typical gaps:** Multiple competing metrics with no agreed primary; metric
tracked in code but not communicated to stakeholders.

---

## exp_versioning — Use Versioning for Data, Model, Configurations and Training Scripts

**Difficulty:** basic  
**Intent:** Improve reproducibility, traceability and compliance.  
**Motivation:** Without versioning, it is impossible to reproduce a past result,
trace a deployed model back to its training data, or understand what changed
between two experiments. This is a prerequisite for debugging, auditing, and
certification in regulated domains.  
**Applicability:** Versioning should be used in any machine learning application or experiment.

**What to look for (EVALUATE/DETECT):**
- Are training scripts in version control (git)?
- Are datasets versioned (DVC, Delta Lake, MLflow, or equivalent)?
- Are model artefacts versioned and linked to the training run that produced them?
- Are hyperparameter configs stored alongside model artefacts?

**Typical gaps:** Code versioned but data is not; model files stored with
non-descriptive names like `model_final_v3b.pkl`.

---

## exp_quality — Continuously Measure Model Quality and Performance

**Difficulty:** basic  
**Intent:** Detect errors early and improve experimentation agility.  
**Motivation:** Measuring quality only at the end of training wastes compute and
delays feedback. Continuous measurement (per epoch, per fold, per data slice)
catches bugs and degradation early and enables fast iteration.  
**Applicability:** Quality monitoring should be used in any training experiment.

**What to look for (EVALUATE/DETECT):**
- Are training and validation metrics logged at regular intervals (not just final)?
- Is there a tool in use (MLflow, W&B, TensorBoard, Neptune, etc.)?
- Are quality regressions surfaced automatically (threshold alerts)?

**Related:** exp_trainingmetric, exp_status

**Typical gaps:** Metrics only logged at the end of training; no tooling —
quality tracked via print statements and manual notes.

---

## exp_parallel — Enable Parallel Training Experiments

**Difficulty:** basic  
**Intent:** Avoid deadlocks during experimentation.  
**Motivation:** When experiments are run sequentially on shared infrastructure
or with shared configs, one failing or slow run blocks the whole team.
Parallelisation decouples experiments, speeds up iteration, and forces
proper isolation of configs and artefacts.  
**Applicability:** Parallelisation should be considered in any machine learning application.

**What to look for (EVALUATE/DETECT):**
- Can multiple experiments run simultaneously without interfering?
- Are run configs and output directories isolated per experiment?
- Is there a job scheduler or experiment tracking tool managing runs?

**Typical gaps:** Experiments share a config file that gets overwritten; output
directories are not namespaced per run.

---

## exp_status — Share Status and Outcomes of Experiments Within the Team

**Difficulty:** basic  
**Intent:** Facilitate knowledge transfer, peer review and model assessment.  
**Motivation:** Experiments whose results are not shared generate duplicated
effort (others repeat the same failed approach) and stall peer review. A shared
experiment log is also the foundation for model governance and audit trails.  
**Applicability:** Experiment tracking and sharing should be used for any training experiment.

**Related:** exp_versioning, exp_quality, exp_peer

**What to look for (EVALUATE/DETECT):**
- Are experiment results accessible to the whole team (not just in one person's notebook)?
- Is there a shared tracking tool or at minimum a shared log/wiki page?
- When an experiment is concluded (pass or fail), is the outcome communicated?

**Typical gaps:** Results live in personal notebooks; only successes are shared,
failures are silently forgotten.
