# Deployment Practices Reference

All 7 practices from the SE-ML catalogue Deployment category (`04-*`).
All apply to production-level ML applications. For teams preparing for
deployment, use the dependency order below as a milestone roadmap.

**Dependency order:**
```
deployment_automate → deployment_shadow → deployment_distskew
    → deployment_monitor → deployment_rollback
    → deployment_log → audit_trails
```

---

## deployment_automate — Automate Model Deployment

**Difficulty:** medium  
**Intent:** Increase ability to deploy models on demand; increase availability
and scalability.  
**Motivation:** Manual deployment is slow, error-prone, and hard to scale.
Automated packaging and delivery eliminates human errors, enables on-demand
deployment, and is a prerequisite for shadow deployment, rollback, and
continuous monitoring.  
**Applicability:** Any production-level ML application.

**What to check (EVALUATE/DETECT):**
- Is there a CI/CD pipeline that builds and packages the model automatically?
- Is deployment triggered by a pipeline (not manual SSH + copy)?
- Are models containerised (Docker) with dependencies pinned?
- Can a new model version be deployed without manual intervention?

**Tools:** Docker, Kubernetes, MLflow Models, Seldon Core, BentoML, 
GitHub Actions, GitLab CI, Argo CD.

**Related:** deployment_shadow, deployment_rollback

---

## deployment_shadow — Enable Shadow Deployment

**Difficulty:** medium  
**Intent:** Test a model's behaviour on production data without impacting the
live service.  
**Motivation:** Training/test performance does not guarantee production
performance. Shadow deployment lets a candidate model process real traffic
in parallel with the live model — without making decisions — so its quality
can be assessed before promotion.  
**Applicability:** Any production-level ML application.

**What to check (EVALUATE/DETECT):**
- Is there a mechanism to route production traffic to a shadow model?
- Are shadow model outputs logged and compared with the live model?
- Is there a defined promotion criterion (metric threshold)?

**Pattern:**
```
Production traffic ──┬──► Live model ──► Final decision
                     └──► Shadow model ──► Logged only (no decision)
```
Compare shadow vs. live outputs. When shadow meets promotion criteria, swap.

**Related:** deployment_automate, deployment_distskew

---

## deployment_distskew — Perform Checks to Detect Skew Between Models

**Difficulty:** medium  
**Intent:** Avoid introducing errors in production pipelines.  
**Motivation:** Models that perform well in training can degrade in production
when the data distribution shifts. Continuous skew detection catches this
drift early, before users are affected.  
**Applicability:** Any production-level ML application.

**What to check (EVALUATE/DETECT):**
- Is performance skew between training and hold-out data checked before deployment?
- Is skew between recent production data and training data monitored?
- Are statistical distribution tests run on feature distributions?

**Skew checks to implement:**
- Train/validation performance gap (before deployment)
- Prediction distribution shift over time (PSI, KL divergence)
- Feature distribution drift (KS test, chi-square for categorical)
- Label drift (if ground truth feedback is available)

**Tools:** Evidently AI, WhyLabs, NannyML, Deepchecks.

**Related:** deployment_monitor, data_complete (Data)

---

## deployment_monitor — Continuously Monitor the Behaviour of Deployed Models

**Difficulty:** medium  
**Intent:** Avoid unintended behaviour in production models.  
**Motivation:** Production environments change: data drifts, user behaviour
shifts, infrastructure fluctuates. Without monitoring, degradation is invisible
until it causes visible failures or user complaints.  
**Applicability:** Any production-level ML application.

**Monitoring pipeline should include:**
- Performance and quality metrics (accuracy, F1, RMSE, etc.)
- Skew and drift metrics (feature distributions, prediction distributions)
- Fairness metrics (subgroup performance parity)
- Model interpretability outputs (LIME/SHAP on samples)
- Business-level metrics (user interaction, conversion, downstream effects)
- Alerting when metrics breach defined thresholds

**What to check (EVALUATE/DETECT):**
- Are model quality metrics logged in production?
- Is there a dashboard showing metric trends?
- Are alerts configured for metric degradation?
- Are fairness and drift metrics included (not just accuracy)?

**Related:** deployment_distskew, deployment_rollback, deployment_log

---

## deployment_rollback — Enable Automatic Rollbacks for Production Models

**Difficulty:** medium  
**Intent:** Avoid keeping sub-optimal models in production.  
**Motivation:** If a deployed model degrades — due to data drift, a bug in
a new version, or an undetected skew — it should be automatically reverted
to the last known good version. Manual rollback is slow and depends on
someone being available.  
**Applicability:** Any production-level ML application.

**What to check (EVALUATE/DETECT):**
- Is there an automated rollback mechanism triggered by monitoring alerts?
- Are previous model versions retained and deployable on demand?
- Has the rollback process been tested (not just designed)?
- Is the rollback time (RTO) documented and acceptable?

**Pattern:**
```
Monitor detects degradation
    → Alert fired
    → Rollback pipeline triggered automatically
    → Previous model version re-deployed
    → Team notified
```

**Related:** deployment_automate, deployment_monitor

---

## deployment_log — Log Production Predictions with Model Version and Input Data

**Difficulty:** medium  
**Intent:** Enhance debugging, traceability, reproducibility, compliance, and
incident management.  
**Motivation:** Without prediction logs, debugging a production failure is
nearly impossible. Logs linking each prediction to its model version and
input data enable full traceability, incident replay, and compliance
with right-to-explanation requirements.  
**Applicability:** Any production-level ML application.

**What to check (EVALUATE/DETECT):**
- Are predictions logged in production with timestamps?
- Are logs linked to model version (tag or hash)?
- Are input features (or a hash of them) stored alongside predictions?
- Is log retention policy defined and compliant with regulation?

**Minimal log record schema:**
```json
{
  "prediction_id": "uuid",
  "timestamp": "ISO8601",
  "model_version": "v1.3.2",
  "input_hash": "sha256:...",
  "input_features": { "feature_a": 0.5, "feature_b": "cat" },
  "prediction": 0.87,
  "confidence": 0.91
}
```

**Related:** exp_versioning (Training), audit_trails

---

## audit_trails — Provide Audit Trails

**Difficulty:** advanced  
**Intent:** Allow post-mortem behaviour analysis of the application.  
**Motivation:** Regulations (EU GDPR, EU AI Act, US credit scoring) require
the right to explanation for automated decisions. Without deliberate audit
trail design, post-mortem analysis and regulatory compliance become impossible.  
**Applicability:** Any ML application; critical for regulated/high-stakes domains.

**Audit trail strategy should cover:**
- Training data distribution snapshots at model training time
- Design decisions (why this model was chosen over alternatives)
- Known failure modes and limitations
- Production prediction logs (see `deployment_log`)
- Model performance over time (monitoring history)
- Incident records and remediation actions

**What to check (EVALUATE/DETECT):**
- Are audit artefacts generated automatically (not manually)?
- Is there a defined retention period for audit records?
- Can a specific past decision be traced back to model version + training data?
- Has an audit strategy been documented and reviewed?

**Related:** deployment_log, explainable (Governance), audits (Governance)
