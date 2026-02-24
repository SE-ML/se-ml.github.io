# Cluster C: Training Automation

These four practices reduce manual effort and systematic bias in the
experimentation loop through automation. They are rated **medium–advanced**
and should be recommended **after** the foundations cluster is in place.

`exp_auto_feat` is conditional on **manual feature engineering**. The others
apply broadly, but teams starting out should begin with `exp_hyperparam`
before tackling NAS or full AutoML.

---

## exp_hyperparam — Automate Hyper-Parameter Optimisation

**Difficulty:** medium  
**Applicability:** Any machine learning application.  
**Intent:** Enhance experimentation, performance and fair comparisons between
algorithms, by automating hyper-parameter search and model selection.  
**Motivation:** Manual hyperparameter tuning is slow, inconsistent, and unfair
when comparing algorithms (one may be better-tuned than another by coincidence
of the experimenter's time). Automated HPO also explores the search space more
systematically than human intuition and is reproducible.

**What to look for (EVALUATE/DETECT):**
- Is hyperparameter search done manually (try a few values by hand)?
- Is there a search tool in use (Optuna, Ray Tune, Hyperopt, W&B Sweeps, etc.)?
- Are search results logged and reproducible (seed, search space documented)?
- Are comparisons between models made at their respective optima?

**Assist — minimal Optuna example:**
```python
import optuna

def objective(trial):
    lr = trial.suggest_float("lr", 1e-5, 1e-1, log=True)
    depth = trial.suggest_int("max_depth", 3, 10)
    model = train_model(lr=lr, max_depth=depth)
    return evaluate(model)

study = optuna.create_study(direction="maximize")
study.optimize(objective, n_trials=50)
print(study.best_params)
```

**Recommended progression:** Start with random search or Optuna TPE before
moving to more expensive Bayesian or evolutionary methods.

**Related:** exp_auto_nas, exp_quality

---

## exp_auto_feat — Automate Feature Generation and Selection

**Difficulty:** advanced  
**Applicability:** When features are **manually engineered** and expertise to
assess generated features is available.  
**Intent:** Reduce human effort required to develop and select features
through automation.  
**Motivation:** Manual feature engineering is time-consuming and biased by domain
assumptions. Automated feature generation (via tools like Featuretools, TSFRESH,
autofeat) can discover features a human would not think of, while automated
selection (via RFECV, SHAP-based selection, Boruta) objectively identifies
which features contribute.

**What to look for (EVALUATE/DETECT):**
- Is feature generation entirely manual?
- Is feature selection done systematically (importance-based, wrapper, filter)?
- Are generated features validated against domain knowledge before use?

**Caution:** Auto-generated features can be hard to interpret and may capture
spurious correlations. Always validate against `exp_owner` (rationale
documentation) and the fairness cluster if applicable.

**Related:** exp_archive, exp_owner, subgroup_bias

---

## exp_auto_nas — Automate Configuration of Algorithms or Model Structure

**Difficulty:** advanced  
**Applicability:** Any machine learning application.  
**Intent:** Improve algorithm and model performance by automatically optimising
their structures.  
**Motivation:** Neural Architecture Search (NAS) and AutoML model selection
remove the need to manually design architecture choices (layer types, depth,
width, connectivity). This is particularly valuable when moving to a new
domain or data modality where human intuition about architecture is weak.

**What to look for (EVALUATE/DETECT):**
- Is model architecture chosen purely by convention or literature defaults?
- Has any automated search over architectures been attempted?
- Are search costs (compute, time) tracked and justified?

**Tools to consider:** AutoKeras, NNI, Ray Tune with architecture search,
SMAC, Ludwig.

**Note:** NAS is expensive. Recommend only when `exp_hyperparam` is already in
place and the team has budget for extended search. Start with hyperparameter
optimisation over architecture topology before full NAS.

**Related:** exp_hyperparam, efficient_compression

---

## efficient_compression — Use the Most Efficient Models

**Difficulty:** n/a (context-dependent)  
**Applicability:** Efficient models should be the first choice for any ML application.  
**Intent:** Avoid overparametrised or energy-inefficient models.  
**Motivation:** Larger models are not always better. Overparametrised models
consume more compute, cost more to serve, have larger carbon footprints, and
can be harder to interpret and audit. Starting with the simplest model that
achieves the objective is good engineering practice and often produces more
robust results.

**What to look for (EVALUATE/DETECT):**
- Is the model size justified relative to the task complexity?
- Have simpler baselines been tried and documented?
- Are model compression techniques considered for deployment (quantisation,
  pruning, distillation)?
- Is compute/energy cost tracked alongside model quality?

**Assist — efficiency checklist:**
- [ ] Establish a simple baseline first (linear model, shallow tree, rule-based)
- [ ] Only increase complexity if the baseline falls short on the defined metric
- [ ] For deployment: evaluate quantisation (INT8) before accepting full-precision serving
- [ ] Document the efficiency tradeoff decision explicitly

**Related:** exp_auto_nas, interpretable
