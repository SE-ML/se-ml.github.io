---
layout: practice
author: Joost Visser, Alex Serban, Koen van der Blom
name: Perform Risk Assessments
category: Governance
index: 40
unique_id: risk
difficulty: "advanced"
references: [TTAID,AIHLEG,CAIAG] #
comments: True
description:
image: #
photocredit: #

intent: Identify and mitigate possible unintended negative impact of your machine learning application. #
motivation: Machine learning applications could have unintended negative impact on your users, the organisation, other organisations, or society at large. A risk assessment is a deliberate, structured process to identify such risks before they occur, so mitigating measures can be designed and implemented.  #
applicability: At least one risk assessment should be conducted for any machine learning application before it goes live. When the stakes are higher (e.g. safety-relevant, vulnerable users, use of personal information), risk assessments should be conducted more frequently and more thoroughly. #
related: [audits]  #
dependencies: #
survey_question: Q97 #
survey_item: We perform regular risk assessments on our ML applications, addressing impact on users, organisations, and society.

labels: [robustness]

---

Unintended negative effects of an machine learning application should not be detected after they have happened in production, nor should we  wait for a (rare and expensive) third-party audit to detect them in a late stage of development.

By conducting an internal risk assessment, the expertise of your organisation is leveraged to identify and mitigate negative impacts as early as possible.

* **Who?** A risk assessment can be conducted by an internal team. Some members may be part of the team that develops the application, but to ensure a fresh and diverse perspective, they should be supplemented with people with different skills, backgrounds, and relative independence.
* **When?** Some form of risk assessment should already be conducted before development of the ML application starts, or in early phases of its development. Depending on the severity and likelihood of risks identified in the initial assessment, further risk assessments should be conducted with appropriate frequency and rigour, to monitor the effectiveness of mitigation steps and shifts in the risk profile due to design changes.
* **How?** A risk assessment should follow a pre-determined process, typically involving (1) a scoping phase to establish which artefacts (applications, data, models, etc.) and associated use cases are assessed against which criteria, (2) a discovery phase where artefacts, documentation, and interviewees are probed and observations are collected, (3) an analysis phase where risks are surfaced, their severity and likelihood are estimated, and possible mitigating steps are formulated, and (4) a reporting phase where all findings are documented and shared with appropriate stakeholders.

To ensure the effectiveness of risks assessments, several issues need to be kept in mind:

* Risk assessments are a type of internal audit, where the scope, process, rigour, and criteria are chosen by the organisation itself. There should be a **clear mandate and desire** by the organisation to keep its own risk assessments honest, and not use them as a mere ritual or act of reputation management.
* Risk assessments are carried out by an internal team. Their familiarity with the organisation, its goals, and the application being assessed allows them to leverage their expertise both for identifying risks and designing mitigation actions. To avoid that this familiarity compromises independence and diversity of perspectives, great care must be taken in the **formation of the assessment team**.

To alleviate these issues, a **third-party audit** can be commissioned in addition to internal risks assessments.

A **red team exercise** is a specific way of conducting a risk assessment on your machine learning application, where a separate team is tasked to take an adversarial perspective to detect vulnerabilities or, in this case, unintended negative impacts of the machine learning application.
