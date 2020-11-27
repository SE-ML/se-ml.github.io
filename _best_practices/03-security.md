---
layout: practice
author: Alex Serban, Koen van der Blom, Joost Visser
name: Assure Application Security
category: Coding
index: 27
unique_id: security
difficulty: na
references: [TTAID]#
comments: True
description:
image: #
photocredit: #

intent: Prevent attackers from stealing or corrupting data, or from disrupting the availability of an application.  #
motivation: Security incidents can lead to public data leaks, financial losses, or disrupt the availability of an application. #
applicability: Security is important for any application with an external interface or which processes personal or sensitive data. #
related: [risk, gov_responsible] #
dependencies: Similarities, differences and connections to other practices #
survey_question: 1 #
survey_item: We use various methods to assure the security of our application under cyber attacks (e.g. code review, analysis tools, penetration tests, red teaming exercises).

---

For any application that exposes an external interface or uses personal or sensitive data, it is imperative to reflect and take actions for improving its security.
Security is known as an arms race, with attackers constantly improving their techniques, and defenders updating their systems in order to predict and prevent new threats.
Therefore, ensuring security is a continuous task.

Besides classical cyber threats that apply to software systems, machine learning adds new security risks both during training and deployment.
Training time attacks are known as data poisoning, and consist of attackers trying to alter the training data in order to induce malicious behaviour -- such as misclassifying certain examples.

Test time (or inference) attacks are more diverse, and consist of adding small perturbations to test data in order to induce malicious behaviour (adversarial attacks), reverse engineer the model or checking if some data was used for training (membership attacks). As other branches of machine learning, security is also a [growing](https://nicholas.carlini.com/writing/2019/all-adversarial-example-papers.html) field of study.

As mentioned earlier, security requires a proactive approach, with some mechanisms including security code reviews, using security analysis tools, penetration testing, and actively performing red teaming exercises.