---
layout: practice
author: Alex Serban, Joost Visser
name: Automate Model Deployment
category: Deployment
unique_id: deployment_automate
index: 20
difficulty: "medium"
references: [VML, MLArch, MLLG, OPML]
comments: True
description:
image: #
photocredit: #


intent: Increase the ability to deploy models on demand -- which increases availability and scalability. #
motivation: Deploying and orchestrating different components of an application can be a tedious task. Instead of manually packaging and delivering models and in order to avoid manual interventions or errors, one can automate this task. #
applicability: #
related: #
dependencies: #
survey_question: Q56
---

Automated deployment involves automatically packing the model together with its dependencies and 'shipping' it to a production server -- instead of manually connecting to a server and perform the deployment.

Automated model deployment brings several advantages. At first, it saves time and it increases reliability because the chances to introduce human errors are removed.
Secondly, it improves availability and scalability because one can repeat the process on demand for as many instances as it is needed, without manual intervention.
This means one can spin off many instances of the model whenever many users need access to a service and decrease the number of instances when the demand lowers.


In order to facilitate continuous deployment:
- use virtualization abstractions , e.g. Docker, Kubeflow,
- use CD tools, e.g. Gitlab CD/Shipyard, Travis, etc.