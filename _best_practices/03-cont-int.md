---
layout: practice
author: Alex Serban, Koen van der Blom, Joost Visser
name: Use Continuous Integration
title: Use Continuous Integration
category: Coding
unique_id: coding_build
index: 27
difficulty: "advanced"
references: [CD4ML, REMLRR]
comments: True
description:
image: #
photocredit: #

intent: Catch any code integration problems as early as possible. #
motivation: Code changes and additions may introduce problems into the software system as a whole. This can be detected by running an automated build script each time that code is committed to the versioning repository.
applicability:  #
related: [coding_static, exp_tstfeature, coding_regr, gov_rai_requirements, gov_fairness_lifecycle]
dependencies: [coding_automate] #
survey_question: Q55 #

labels: [agility, quality]

---

By running an automated build script at each commit, you achieve **Continuous Integration** (CI).

For this, you need to activate and configure a CI server in your development environment. Examples of CI servers include: TravisCI, CircleCI, and Appveyer. Some collaborative development environments include a built-in CI server.

To test not only possible **compilation errors** that may be introduced by code changes, but also possible **runtime defects** and **code quality problems**, the CI server must be configured to trigger one or more static analysis tools and your automated regression tests.

**Gate on fairness and ethics metrics**
Beyond functional correctness, the CI pipeline should also enforce Responsible AI requirements automatically.
Add automated checks that run on every commit or at minimum on every release candidate:
- evaluate fairness metrics (e.g. demographic parity, equalised odds) on a representative held-out slice dataset and fail the build if a metric drops below a defined threshold,
- run bias detection tools (e.g. Fairlearn, AI Fairness 360) as part of the regression suite,
- check that required explainability artefacts (e.g. feature importance reports) are produced and non-empty.

These gates encode RAI requirements as executable acceptance criteria, making ethical regressions as visible as functional ones.
