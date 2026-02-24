# Cluster B: Training Code Quality

These four practices focus on the quality and maintainability of the code
used in the training pipeline. **All four are always relevant**, but three
(`exp_tstfeature`, `exp_archive`, `exp_owner`) are **conditional on manual
feature engineering** — skip them when features are learned end-to-end (e.g.
raw-input deep learning). `exp_peer` applies universally.

All are rated **basic–medium** difficulty.

---

## exp_peer — Peer Review Training Scripts

**Difficulty:** medium  
**Applicability:** Always — training scripts should always be peer reviewed.  
**Intent:** Avoid development errors and bugs.  
**Motivation:** Training scripts contain logic errors that are easy to miss in
isolation: data leakage, incorrect loss functions, silent NaN propagation,
wrong train/test splits. A second pair of eyes catches these before they
invalidate experiments or produce a flawed deployed model. Unlike production
software, ML bugs often produce plausible-looking outputs that mask the problem.

**What to look for (EVALUATE/DETECT):**
- Is there a pull request / code review process for training scripts?
- Are training scripts treated with the same rigour as production code?
- Is there a checklist used during review (data leakage, metric correctness,
  reproducibility)?

**Assist — checklist to use during review:**
- [ ] Is the train/validation/test split done *before* any preprocessing?
- [ ] Is there any possibility of data leakage (future data, label leakage)?
- [ ] Are random seeds set and documented?
- [ ] Does the loss function match the stated objective?
- [ ] Are metrics computed correctly (correct class weights, correct aggregation)?
- [ ] Are edge cases handled (empty batches, NaNs, class imbalance)?

**Typical gaps:** Training scripts treated as throwaway exploration code with no review;
review done informally in chat with no record.

---

## exp_tstfeature — Test All Feature Extraction Code

**Difficulty:** medium  
**Applicability:** When features are **manually engineered** (not auto-extracted).  
**Intent:** Avoid bugs in the feature extraction code.  
**Motivation:** Feature extraction code is often complex, data-dependent, and
changes frequently. Bugs here silently corrupt the training data: wrong
aggregations, off-by-one errors, incorrect joins. Because the model still
trains and produces outputs, these bugs can go undetected for a long time.
Unit tests on feature logic are the most cost-effective safety net available.

**What to look for (EVALUATE/DETECT):**
- Does feature extraction code have unit tests?
- Are edge cases tested (nulls, empty groups, boundary dates)?
- Are tests run automatically in CI?

**Assist — test structure template:**
```python
def test_feature_age_bucket():
    input_df = pd.DataFrame({"age": [0, 17, 18, 64, 65, None]})
    result = compute_age_bucket(input_df)
    assert result["age_bucket"].tolist() == ["minor", "minor", "adult", "adult", "senior", "unknown"]

def test_feature_no_data_leakage():
    # future_date should not be accessible at prediction time
    ...
```

**Typical gaps:** Feature code tested manually once when written, then never again;
no tests for null handling or boundary values.

---

## exp_archive — Actively Remove or Archive Features That Are Not Used

**Difficulty:** medium  
**Applicability:** When features are **manually engineered**.  
**Intent:** Avoid technical debt caused by unused features.  
**Motivation:** Feature sets accumulate over time. Unused features increase
training time and memory, add noise, complicate the codebase, and create
maintenance burden. They also confuse new team members. Actively archiving
features that do not contribute keeps the pipeline lean and interpretable.

**What to look for (EVALUATE/DETECT):**
- Is there a feature registry or documentation of active vs. archived features?
- Are features periodically reviewed for contribution (feature importance, ablation)?
- Is there a process for removing a feature (not just commenting out code)?

**Assist — archiving process:**
1. Run feature importance analysis (SHAP, permutation importance, ablation).
2. For features with near-zero importance over N consecutive runs, flag for review.
3. Move removed feature code to an `archived_features/` module (not deleted — for audit trail).
4. Update the feature registry and document the reason for archiving.
5. Bump a version number to signal the feature set changed.

**Related:** exp_owner, exp_versioning

---

## exp_owner — Assign an Owner to Each Feature and Document Its Rationale

**Difficulty:** medium  
**Applicability:** When features are **manually engineered**.  
**Intent:** Enhance feature development, understanding and maintenance.  
**Motivation:** Features without an owner decay silently. The original reasoning
is forgotten, nobody knows if a feature is still valid, and nobody is
accountable when it breaks. Documenting the rationale also enables newcomers
to understand *why* a feature exists — preventing the "cargo cult feature"
problem where features are kept because removing them feels risky.

**What to look for (EVALUATE/DETECT):**
- Is there a feature registry or feature documentation file?
- Does each feature have a named owner (person or team)?
- Is the business/domain rationale documented (not just the formula)?

**Assist — minimal feature registry entry:**
```yaml
- id: customer_days_since_last_purchase
  owner: alice@team.com
  created: 2024-03-01
  rationale: "Strong predictor of churn in prior cohort analysis (Q4 2023 study)"
  importance: high  # updated periodically
  status: active   # active | under-review | archived
  notes: "Sensitive to campaign timing — review before seasonal campaigns"
```

**Related:** exp_archive
