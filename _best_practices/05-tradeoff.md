---
layout: practice
author: Alex Serban, Koen van der Blom, Joost Visser
name: Decide Trade-Offs through Defined Team Process
category: Team
index: 38
unique_id: tradeoff
difficulty: na
references: [SEDS, GDMMA, MOIEA] #
comments: True
description:
image: #
photocredit: #

intent: Define methodology for generation, evaluation, prioritisation and selection of solution alternatives. #
motivation:  Software development is characterised by multiple objectives and constraints, uncertainty and incomplete information. Moreover, the problem parameters change very often. #
applicability: This practice applies to all applications involving software. #
related: [interpretable] #
dependencies: Similarities, differences and connections to other practices #
survey_question: Q86 #
survey_item: Our team has a clearly defined decision process to make trade-offs between competing quality attributes (e.g. between accuracy, explainability, resource consumption).
---

Software development can be seen as a multiple objective optimisation problem, where trade-offs between quality attributes of a system have to be made and recorded.
In most cases, decisions have to be made under uncertainty and incomplete information.
In order to enhance a teams ability to make the right decisions at the right time, it is imperative to define and enforce a standard process across team members.

ML adds more uncertainty to a system, and increases the importance of this practice.
Besides software relate trade-offs -- such as selecting the right architectural style or prioritising the maintenance cycle for certain components -- new trade-offs regarding ML quality attributes must be considered.

For example, a team process can include the prioritisation of interpretable models over black-box models, or a procedure to roll-back production systems when the accuracy drops significantly.
A team process can empower team members to take action even though other members responsible for decisions are not present.
Large companies, with vast experience in software development, adopt company wide policies that are followed by all teams (e.g. Amazon's 14 leadership principles).
Defining a process that can be adopted by multiple teams in the organisation enhances collaboration and communication between teams.
