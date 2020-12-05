---
layout: practice
author: Alex Serban, Koen van der Blom, Joost Visser
name: Run Automated Regression Tests
title: Run Automated Regression Tests
category: Coding
unique_id: coding_regr
index: 24
difficulty: "advanced"
references: [MLPROD]
comments: True
description:
image: #
photocredit: #

intent: Avoid the introduction of bugs in code. #
motivation: When making changes, new defects can easily be introduced in existing code. A suite of automated regression tests helps to spot such defects as early as possible. #
applicability: Regression testing can be applied to any type of code. #
related: [exp_tstfeature] #
dependencies: [coding_build] #
survey_question: Q53 #

---

When adding or changing code, new defects can be introduced, not only in the code that has just been worked on, but also in the code that existed before. Regression testing aims to spot those bugs and hence prevent the quality of the software to deteriorate (regress).

By automating your regression tests, spotting newly introduced bugs after each change becomes effortless. Thus, automated regression tests allows you to focus on experimenting with new functionality rather than worrying about not breaking existing functionality.

Testing frameworks are available to help writing, organizing, running, and reporting on the outcome of regression tests. The most widely used from of regression testing is **unit testing**. For many programming languages, unit testing frameworks are available, such as [JUnit](https://junit.org/) (for Java), [test that](https://testthat.r-lib.org/) for R, or [unittest](http://docs.python.org/library/unittest.html) for Python.

When adding new code, also new regression tests should be written, to ensure that regression testing may find bugs there as well in the future. The style of programming called **test-driven development** goes one step further and advocates for first writing a test for new functionality and only then writing the code that provides that functionality.

When running automated regression tests, it is important to make sure your test suite provides good **coverage**. For this, test coverage tooling can be used such as [Codecov](https://codecov.io/).

An advanced method for measuring test suite quality is mutation testing, where small perturbations (mutants) are injected into the code to see if the test suite detects them.


