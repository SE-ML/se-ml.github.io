# Data Practices Reference

All 8 practices from the SE-ML catalogue Data category (`01-*`).
Practices marked **[personal data]** are only loaded when scoping confirms
the application processes personal or individual data.
The practice `data_lbl` is only loaded for supervised/semi-supervised learning.

---

## data_sanity — Use Sanity Checks for All External Data Sources

**Difficulty:** medium | **Always applies**  
**Intent:** Avoid invalid or incomplete data being processed.  
**Motivation:** Data is at the heart of any ML model. Whenever external or
potentially incomplete data is used, verifying quality upfront prevents
production outages and inaccurate models.  
**Applicability:** Any ML application using external data sources.

**What to check (EVALUATE/DETECT):**
- Are there automated checks on data types, missing values, min/max ranges?
- Are histograms or distributions checked for continuous features?
- Are sanity check scripts reusable and integrated into the pipeline?

**Assist — minimal sanity check template (Python/pandas):**
```python
def sanity_check(df: pd.DataFrame, schema: dict) -> list[str]:
    issues = []
    for col, rules in schema.items():
        if col not in df.columns:
            issues.append(f"Missing column: {col}")
            continue
        if rules.get("dtype") and df[col].dtype != rules["dtype"]:
            issues.append(f"{col}: wrong dtype {df[col].dtype}")
        if "min" in rules and df[col].min() < rules["min"]:
            issues.append(f"{col}: value below min {rules['min']}")
        if "max" in rules and df[col].max() > rules["max"]:
            issues.append(f"{col}: value above max {rules['max']}")
        null_pct = df[col].isnull().mean()
        if null_pct > rules.get("max_null_pct", 0.0):
            issues.append(f"{col}: {null_pct:.0%} nulls exceeds threshold")
    return issues
```

**Related:** data_complete

---

## data_complete — Check that Input Data is Complete, Balanced and Well Distributed

**Difficulty:** basic | **Always applies**  
**Intent:** Avoid invalid or incomplete data being processed.  
**Motivation:** Data generation processes are not static. Distributions drift,
groups become over- or under-represented, and hidden feature dependencies emerge.
Continuous checks prevent models from being trained or served on degraded data.  
**Applicability:** Any ML application.

**What to check (EVALUATE/DETECT):**
- Are features checked for sufficient presence (not too sparse)?
- Is data distribution monitored over time (no silent drift)?
- Are training and test/production distributions compared?
- Are monitoring dashboards or alerts in place?

**Related:** data_sanity, deployment_distskew, social_bias

---

## data_reusable — Write Reusable Scripts for Data Cleaning and Merging

**Difficulty:** basic | **Applies when data preprocessing is needed**  
**Intent:** Avoid untidy data wrangling scripts; increase reproducibility.  
**Motivation:** Exploratory preprocessing code in notebooks is non-reproducible,
non-testable, and cannot be integrated into pipelines. Converting it to
parameterised, callable functions enables reuse, testing, and automation.  
**Applicability:** Any ML application that does not use raw or standard datasets.

**What to check (EVALUATE/DETECT):**
- Is preprocessing code in reusable functions/modules (not notebook-only)?
- Can preprocessing steps be called independently and tested?
- Are preprocessing scripts integrated into a pipeline (not run manually)?

**Typical gap:** Ad-hoc Jupyter notebook cells that depend on in-memory variables;
no way to reproduce the cleaning step from scratch.

**Related:** exp_tstfeature (Training)

---

## data_share — Make Datasets Available on Shared Infrastructure

**Difficulty:** basic | **Always applies**  
**Intent:** Avoid data duplication, bottlenecks, or unnecessary large transfers.  
**Motivation:** ML applications process large data volumes. Without shared,
versioned storage, teams duplicate data, lose traceability, and create access
control gaps. Shared infrastructure enables versioning, access logging, and
consistent naming conventions.  
**Applicability:** Any ML application.

**What to check (EVALUATE/DETECT):**
- Are datasets stored in shared infrastructure (S3, GCS, Azure Blob, NFS, etc.)?
- Is access controlled (not publicly writable, not on personal machines)?
- Are naming conventions applied (version info in paths/names)?
- Is a data access log maintained?

---

## data_lbl — Ensure Data Labelling is Performed in a Strictly Controlled Process

**Difficulty:** basic | **Applies for supervised / semi-supervised learning only**  
**Intent:** Avoid invalid or incomplete labels.  
**Motivation:** Labels are the ground truth signal for supervised learning.
Noisy or inconsistent labels degrade model quality in ways that are hard to
diagnose. A controlled process — including peer review of labels — is the
most effective safeguard.  
**Applicability:** Any application using labels.

**What to check (EVALUATE/DETECT):**
- Is there a documented labelling process?
- Are labels peer-reviewed by a second team member?
- Is label quality monitored (inter-annotator agreement, spot checks)?
- Are labelling issues documented and communicated when quality is sub-optimal?

**Assist — mature labelling process checklist:**
- [ ] Labelling guidelines documented and version-controlled
- [ ] Labels stored with annotator ID and timestamp
- [ ] At least 5–10% of labels peer-reviewed
- [ ] Inter-annotator agreement (Cohen's kappa or Fleiss) computed and tracked
- [ ] Label quality issues logged and communicated to the model team

---

## social_bias — Test for Social Bias in Training Data

**Difficulty:** advanced | **[personal data] — applies when data concerns individuals**  
**Intent:** Identify instances of social bias in training data to counteract
unfairness in trained and deployed models.  
**Motivation:** Bias in data is a primary source of unfairness. Seemingly
neutral attributes (location, name, hobbies) can encode sensitive social
traits via proxy effects — *failure through unawareness*.  
**Applicability:** Applications processing personal data or data about users.

**What to check (EVALUATE/DETECT):**
- Are distributions of social factors (gender, age, geography, etc.) analysed?
- Is over- or under-representation of groups detected and documented?
- Are latent proxy attributes identified (e.g. zip code as proxy for race)?
- Does the team include diverse perspectives in data review?

**Related:** discriminatory_attributes, subgroup_bias (Training), risk (Governance)

---

## discriminatory_attributes — Prevent Discriminatory Attributes Used as Features

**Difficulty:** advanced | **[personal data] — applies in applications affecting individuals**  
**Intent:** Avoid building discriminatory practices into ML applications.  
**Motivation:** Using protected attributes (gender, ethnicity, religion) as
features leads to discriminatory models. Simply removing them is insufficient —
latent proxies can reconstruct them. A hybrid approach is required.  
**Applicability:** Applications with direct or indirect impact on human lives.

**What to check (EVALUATE/DETECT):**
- Is there a list of protected/sensitive attributes for this application?
- Are those attributes removed from the feature set?
- Are latent proxy tests conducted to detect reconstruction of sensitive attributes?
- Is ongoing testing for subgroup bias (`subgroup_bias`) in place?

**Important:** Removing sensitive attributes alone can *worsen* fairness if
done improperly. Always complement removal with active bias testing.

**Related:** social_bias, subgroup_bias (Training), risk (Governance)

---

## privacy_preserving — Use Privacy-Preserving Machine Learning Techniques

**Difficulty:** advanced | **[personal data] — applies when processing PII**  
**Intent:** Protect the privacy of individuals whose data is used in ML.  
**Motivation:** ML models can leak information about training data (membership
attacks). When processing personal data, privacy-preserving techniques reduce
the risk of privacy violations and aid GDPR/regulatory compliance.  
**Applicability:** Any application using personally identifiable information.

**Techniques to consider:**
| Technique | Use case |
|-----------|----------|
| Differential privacy | Add calibrated noise during training |
| Federated learning | Train on device without centralising data |
| Anonymisation / pseudonymisation | Remove or mask identifiers in datasets |
| Homomorphic encryption | Compute on encrypted data |

**Tools:** Opacus (PyTorch differential privacy), PySyft (federated learning),
CrypTen (secure multi-party computation).

**Related:** gov_responsible (Governance)
