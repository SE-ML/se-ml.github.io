---
layout: practice
author: Alex Serban, Joost Visser
name: Use Static Analysis to Check Code Quality
title: Use Static Analysis to Check Code Quality
category: Coding
unique_id: coding_static
index: 19
difficulty: "advanced"
references: [BMS]
comments: True
description:
image: #
photocredit: #

intent: Avoid the introduction of code that is difficult to test, maintain, or extend. #
motivation: High-quality code is easier to understand, test, maintain, reuse, and extend. The most effective way of ensuring high code quality is to make use of static analysis tools. #
applicability: Code quality control should be applied to any type of code. #
related: [coding_build] # Static code analysis can be combined with Continuous Integration / Run Build at Each Commit #
dependencies: #
survey_question: Q57 #
---

By ensuring high code quality you can avoid the introduction of defects into the code, enable new team members to become productive more quickly, and more easily reason about the correctness of your code.

Static code analysis can be done in various ways:
- **Linters**: A linter is a tool that finds undesirable patterns in program code and reports these back to the programmer. Linters can be activated in a code editor, and integrated development environment, or they can be run on the commandline.
- **Quality gates**: You can integrate a static code quality analysis tool in automated build and testing script that runs every time a developer commits code changes to the versioning system. When quality issues are found, you can choose to have the commit rejected.
- **Quality dashboards**: You can display the results of static code quality analysis tools on a dashboard available to the entire development team or even the larger organisation. This allows quality trends to be shared and acted upon at a broader level than just the individual developer.

Apart from choosing and activating appropriate static analysis tools, it is important to embed the usage of the tools and their results in the way of work of the development team. This requires:
- Agreeing on what level of quality is expected
- Encouraging team members to act on quality issues in a meaningful way, i.e. by finding and eliminating the root causes
- Allowing the team to spend time on quality corrections before moving on to implementing more functonality

There are various pitfalls to look out for:
- Some static analysis tools produce many "false positives": findings that are not relevant in the context at hand, but absorb attention and time from developers
- When static analysis tools are not configured to look at all code (e.g. just program code, but not database scripts). This leads to a blind spot and false confidence in code quality.