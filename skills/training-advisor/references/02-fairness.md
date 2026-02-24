# Cluster D: Fairness and Interpretability

These two practices are **conditional** — they apply primarily when the
application is deployed in a **regulated, fairness-sensitive, or high-stakes
domain** (healthcare, finance, HR decisions, credit scoring, law enforcement,
education, etc.). Both are rated **advanced**.

Even outside regulated domains, these practices are worth raising as a
**suggestion** when the model makes decisions that affect individuals.

---

## subgroup_bias — Assess and Manage Subgroup Bias

**Difficulty:** advanced  
**Applicability:** All applications that process data regarding groups and
subgroups of individuals — especially where automated decisions are made.  
**Intent:** Avoid bias and unfair decisions within subgroups.  
**Motivation:** A model with acceptable aggregate performance may perform very
differently across demographic subgroups (age, gender, race, geography, etc.).
This disparity can cause real harm in high-stakes decisions. Assessing subgroup
performance is not optional in regulated contexts — it is a legal and ethical
requirement in many jurisdictions (EU AI Act, EEOC guidelines, GDPR).

**What to look for (EVALUATE/DETECT):**
- Are performance metrics broken down by relevant subgroups?
- Are protected attributes identified and documented?
- Is there a threshold below which subgroup performance is considered unacceptable?
- Are subgroup disparities tracked over time in production?

**Assist — minimal subgroup evaluation:**
```python
from sklearn.metrics import classification_report

for group in df["subgroup"].unique():
    subset = df[df["subgroup"] == group]
    print(f"\n--- Subgroup: {group} ---")
    print(classification_report(subset["y_true"], subset["y_pred"]))
```

**Key fairness metrics to consider:**
- Demographic parity: equal positive prediction rates across groups
- Equalised odds: equal TPR and FPR across groups
- Calibration: predicted probabilities equally calibrated across groups

**Tools:** Fairlearn, IBM AI Fairness 360, What-If Tool, Aequitas.

**Important:** Bias assessment is not a one-time check. It must be part of
the continuous monitoring pipeline (`deployment_monitor`).

**Related:** gov_responsible, interpretable, deployment_monitor

---

## interpretable — Employ Interpretable Models When Possible

**Difficulty:** advanced  
**Applicability:** Non-interpretable models often only provide a marginal
performance gain. Whenever possible, prefer interpretable over black-box
models, even at a small performance cost.  
**Intent:** Help users, developers, and auditors understand and account for
the results of machine learning applications.  
**Motivation:** Black-box models create accountability gaps: when a model
makes a harmful or incorrect decision, there is no way to explain why or
to identify what to fix. Interpretable models (logistic regression, decision
trees, GAMs, rule lists) make debugging, auditing, and trust-building
significantly easier. In regulated domains, interpretability is often a
hard requirement.

**What to look for (EVALUATE/DETECT):**
- Has the team evaluated interpretable model alternatives before defaulting to
  complex models?
- If a complex model is used, are post-hoc explanation methods applied
  (SHAP, LIME, integrated gradients)?
- Are explanations validated — i.e., do they reflect the model's actual
  decision process, not just plausible-sounding stories?
- Are explanations provided to end users or decision-makers in a usable form?

**Assist — interpretability ladder:**

| Level | Approach | When to use |
|-------|----------|-------------|
| 1 | Logistic regression, decision tree, rule list | Tabular data, regulatory requirement |
| 2 | Generalised Additive Models (GAMs, EBMs) | Non-linear relationships, still interpretable |
| 3 | Gradient boosted trees + SHAP | Strong performance needed, post-hoc explanation acceptable |
| 4 | Deep learning + LIME/SHAP/Integrated Gradients | Large unstructured data; explanation quality varies |

**Caution:** Post-hoc explanations (SHAP, LIME) approximate model behaviour
and can be misleading. Intrinsically interpretable models are always
preferable when performance permits.

**Related:** subgroup_bias, gov_responsible, efficient_compression
