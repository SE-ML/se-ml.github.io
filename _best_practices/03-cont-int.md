---
layout: practice
author: Alex Serban, Koen van der Blom, Joost Visser
name: Use Continuous Integration
title: Use Continuous Integration
category: Coding
unique_id: coding_build
index: 25
difficulty: "medium"
references: [CD4ML]
comments: True
description:
image: #
photocredit: #

intent: Catch any code integration problems as early as possible. #
motivation: Code changes and additions may introduce problems into the software system as a whole. This can be detected by running an automated build script each time that code is committed to the versioning repository.
applicability:  #
related: [coding_static, exp_tstfeature, coding_regr]
dependencies: [coding_automate] #
survey_question: Q55 #

labels: [agility, quality]

---

By running an automated build script at each commit, you achieve **Continuous Integration** (CI).

For this, you need to activate and configure a CI server in your development environment. Examples of CI servers include: TravisCI, CircleCI, and Appveyer. Some collaborative development environments include a built-in CI server.

To test not only possible **compilation errors** that may be introduced by code changes, but also possible **runtime defects** and **code quality problems**, the CI server must be configured to trigger one or more static analysis tools and your automated regression tests.
