# Coding Practices Reference

All 4 practices from the SE-ML catalogue Coding category (`03-*`).
All apply broadly; `security` is conditional on external interfaces or
sensitive data. `coding_build` (CI) is recommended for production projects.

Recommended adoption order: **coding_regr → coding_static → coding_build → security**

---

## coding_regr — Run Automated Regression Tests

**Difficulty:** medium | **Always applies**  
**Intent:** Avoid the introduction of bugs in code.  
**Motivation:** Changes to ML code introduce defects not just in new code but in
existing functionality. Automated regression tests catch these regressions early,
freeing the team to experiment without fear of silently breaking the pipeline.  
**Applicability:** Any type of code in the ML project.

**What to check (EVALUATE/DETECT):**
- Is there a test suite (pytest, unittest, or equivalent)?
- Are tests run automatically on each commit or PR?
- Is test coverage measured (codecov, pytest-cov)?
- Are ML-specific concerns tested: data leakage, metric correctness,
  preprocessing correctness (see `exp_tstfeature` in Training)?

**Assist — minimal pytest setup for ML code:**
```python
# tests/test_preprocessing.py
import pytest
import pandas as pd
from src.preprocessing import normalize_features

def test_normalize_output_range():
    df = pd.DataFrame({"a": [0.0, 10.0, 5.0]})
    result = normalize_features(df)
    assert result["a"].min() >= 0.0 and result["a"].max() <= 1.0

def test_normalize_handles_nulls():
    df = pd.DataFrame({"a": [1.0, None, 3.0]})
    result = normalize_features(df)
    assert result["a"].isnull().sum() == 0
```

**Related:** coding_build, exp_tstfeature (Training)

---

## coding_static — Use Static Analysis to Check Code Quality

**Difficulty:** medium | **Always applies**  
**Intent:** Avoid the introduction of code that is difficult to test, maintain,
or extend.  
**Motivation:** High-quality code reduces defects, accelerates onboarding,
and makes correctness easier to reason about. Static analysis is the most
cost-effective way to enforce quality — it runs in seconds and requires no
test data.  
**Applicability:** Any type of code.

**What to check (EVALUATE/DETECT):**
- Is a linter configured and in use (ruff, flake8, pylint)?
- Is a type checker in use (mypy, pyright)?
- Are quality issues surfaced at commit time (pre-commit hooks) or in CI?
- Is there an agreed quality threshold the team acts on?

**Assist — minimal pre-commit config:**
```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.3.0
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.8.0
    hooks:
      - id: mypy
```

**Related:** coding_build

---

## coding_build — Use Continuous Integration

**Difficulty:** advanced | **Recommended for production projects**  
**Intent:** Catch code integration problems as early as possible.  
**Motivation:** CI runs the test suite and static analysis on every commit,
making integration failures immediately visible to the whole team —
not discovered days later in a broken shared branch.  
**Applicability:** Any ML project integrating code changes from multiple contributors.

**What to check (EVALUATE/DETECT):**
- Is a CI server configured (GitHub Actions, GitLab CI, CircleCI, etc.)?
- Does CI run both static analysis and regression tests?
- Are failed builds blocking merge to main?
- Does CI run on PRs, not just after merge?

**Assist — minimal GitHub Actions workflow:**
```yaml
# .github/workflows/ci.yml
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: pip install -e ".[dev]"
      - run: ruff check .
      - run: mypy src/
      - run: pytest --cov=src tests/
```

**Related:** coding_static, coding_regr

---

## security — Assure Application Security

**Difficulty:** advanced | **Applies when: external interface or sensitive data**  
**Intent:** Prevent attackers from stealing/corrupting data or disrupting the application.  
**Motivation:** ML adds unique attack surfaces beyond classical software:
*data poisoning* (manipulating training data), *adversarial attacks*
(perturbing inputs at inference), and *membership attacks* (inferring
training data from the model). Proactive security is an ongoing requirement,
not a one-time fix.  
**Applicability:** Any application with an external interface or that processes
personal or sensitive data.

**ML-specific threats to address:**

| Threat | Description | Mitigation |
|--------|-------------|-----------|
| Data poisoning | Attacker alters training data | Input validation, data provenance tracking |
| Adversarial examples | Perturbed inputs cause misclassification | Adversarial training, input sanitisation |
| Membership attacks | Infer if a record was in training data | Differential privacy, model output restrictions |
| Model extraction | Reconstruct model via queries | Rate limiting, output perturbation |

**Security mechanisms to implement:**
- Security-focused code review (OWASP ML Security Top 10)
- Static security analysis (bandit for Python, semgrep)
- Penetration testing of API endpoints
- Red teaming exercises for high-stakes applications

**Assist — minimal bandit setup:**
```bash
pip install bandit
bandit -r src/ -ll  # report medium and high severity issues only
```

**Related:** risk (Governance), gov_responsible (Governance)
