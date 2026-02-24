# Governance Practices Reference

All 7 practices from the SE-ML catalogue Governance category (`06-*`).
All apply to any ML application; urgency and depth scale with stakes level.
All practices are **process and policy-based** — assessment relies on
self-report and documentation review.

**Priority order by stakes level:**

| Stakes | Priority order |
|--------|---------------|
| Low (internal tooling) | code_conduct → risk → audit_trails |
| Medium (affects users) | + alert → explainable → concerns |
| High (regulated / automated decisions) | all as critical, + audits |

---

## code_conduct — Establish Responsible AI Values

**Difficulty:** advanced  
**Intent:** Explicitly align all stakeholders on the ethical values and
constraints of the ML application.  
**Motivation:** ML applications can severely impact human lives even without
malicious intent. Shared, explicit values give all team members a framework
for making consistent decisions — especially in ambiguous situations not
covered by specific rules.  
**Applicability:** Any ML application.

**What to check (EVALUATE/DETECT):**
- Has the team subscribed to or formulated a Responsible AI code of conduct?
- Is it documented and accessible to all team members?
- Are values operationalised (linked to concrete practices, not just aspirational)?
- Are values reviewed when the application's scope or risk profile changes?

**Assist — starting points:**
- EU High-Level Expert Group: [Ethics Guidelines for Trustworthy AI](https://ec.europa.eu/digital-single-market/en/news/ethics-guidelines-trustworthy-ai)
- Google Responsible AI Practices
- Microsoft AI Principles
- IEEE Ethically Aligned Design

**Related:** tradeoff (Team), audits, interpretable (Training)

---

## risk — Perform Risk Assessments

**Difficulty:** advanced  
**Intent:** Identify and mitigate possible unintended negative impact of the
ML application.  
**Motivation:** Negative impacts should not wait to be discovered in production or
in a third-party audit. Internal risk assessments leverage team expertise to
surface risks early, when mitigation is cheapest.  
**Applicability:** At least one assessment before go-live; more frequent and
thorough for high-stakes applications.

**Risk assessment phases:**
1. **Scoping** — define which artefacts, use cases, and criteria are assessed
2. **Discovery** — probe artefacts, documentation, and conduct interviews
3. **Analysis** — surface risks, estimate severity × likelihood, propose mitigations
4. **Reporting** — document findings, share with stakeholders, track remediation

**What to check (EVALUATE/DETECT):**
- Has a risk assessment been conducted before deployment?
- Was the assessment team diverse (not just the core dev team)?
- Are risks tracked with severity, likelihood, and mitigation owner?
- Is there a schedule for re-assessment (e.g. quarterly, after major changes)?

**Assist — minimal risk register entry:**
```
Risk: [Short description]
Category: [Fairness / Privacy / Safety / Security / Reliability / Legal]
Likelihood: [High / Medium / Low]
Severity: [Critical / High / Medium / Low]
Affected parties: [Users / Organisation / Society]
Current mitigation: [What is already in place]
Proposed mitigation: [What needs to be done]
Owner: [Name / Team]
Review date: YYYY-MM-DD
```

**Related:** audits, security (Coding)

---

## alert — Inform Users on Machine Learning Usage

**Difficulty:** advanced  
**Intent:** Make users aware that ML is used, what it is used for, and what
its limitations are.  
**Motivation:** Users have the right to know they are interacting with an ML
system. Failure to disclose can violate human rights and regulations (EU AI Act,
GDPR). Informed users can make better decisions, provide better feedback, and
raise concerns more effectively.  
**Applicability:** Any ML application with user-facing outputs or decisions.

**What to check (EVALUATE/DETECT):**
- Is there in-product disclosure that ML is used?
- Is the intended use and scope of the ML system described to users?
- Are limitations and known failure modes communicated?
- Is a model card or equivalent public documentation published?

**Assist — model card essentials:**
```markdown
## Model Card: [Model Name]

**Intended use:** [What the model is designed to do]
**Out-of-scope uses:** [What it should NOT be used for]
**Training data:** [Source, size, date range — no PII details]
**Performance:** [Key metrics, on which evaluation sets]
**Known limitations:** [Edge cases, failure modes, biases identified]
**Fairness considerations:** [Subgroup analysis results if applicable]
**Contact / feedback:** [How users can raise concerns]
```

**Related:** explainable, concerns

---

## explainable — Explain Results and Decisions to Users

**Difficulty:** advanced  
**Intent:** Allow users to critically assess ML results so they can accept
them on an informed basis — or catch errors.  
**Motivation:** GDPR and US credit scoring law require the *right to explanation*
for automated decisions. Beyond legal compliance, explained decisions build
user trust, enable error correction, and improve the system over time.  
**Applicability:** Any ML application making decisions that affect users.

**What to check (EVALUATE/DETECT):**
- Does each decision or result come with a human-readable explanation?
- Is the explanation meaningful to the target user (not just ML jargon)?
- Can users challenge or query an explanation?
- Are explanation methods validated (not just presented)?

**Explanation approaches by model type:**
| Model | Approach |
|-------|----------|
| Logistic regression, linear | Coefficient-based explanation |
| Decision tree | Rule-based path explanation |
| Gradient boosted trees | SHAP values |
| Neural networks | LIME, Integrated Gradients, attention (with caveats) |
| Any | Counterfactual explanations ("if X had been Y, the decision would have been Z") |

**Related:** alert, audit_trails (Deployment), interpretable (Training)

---

## concerns — Provide Safe Channels to Raise Concerns

**Difficulty:** advanced  
**Intent:** Obtain honest feedback enabling timely remediation.  
**Motivation:** Users can identify bias, errors, and ethical issues that the
development team cannot see from the inside. Without a safe, accessible channel,
concerns go unvoiced — until they escalate into public incidents or legal action.  
**Applicability:** Any ML application with users or affected individuals.

**What to check (EVALUATE/DETECT):**
- Is there a documented channel for users to raise concerns (email, form, chat)?
- Is anonymous reporting possible to protect user privacy?
- Is there a defined response process (who reviews, in what timeframe)?
- Are concerns logged and used to improve the application?

**Assist — concerns channel checklist:**
- [ ] Contact method published in product UI and documentation
- [ ] Anonymous submission option available
- [ ] Acknowledgement sent within 48h
- [ ] Concerns categorised (bias / privacy / safety / other)
- [ ] Triaged to responsible team member
- [ ] Resolution communicated back where appropriate

**Related:** alert, explainable

---

## audits — Have Your Application Audited

**Difficulty:** advanced  
**Intent:** Obtain an independent assessment of the application's strengths
and weaknesses.  
**Motivation:** Internal risk assessments are limited by organisational familiarity
and potential bias toward favourable findings. External audits provide
independent, credible assessment — building trust with regulators, partners,
and users.  
**Applicability:** Any ML application; mandatory for high-risk applications
under the EU AI Act and similar regulations.

**What to check (EVALUATE/DETECT):**
- Has a third-party audit been conducted or scheduled?
- Are audit outcomes documented and shared appropriately?
- Is a remediation plan in place for findings?
- Is there a regular audit cadence (not just once before launch)?

**Assist — preparing for an audit:**
1. Ensure `audit_trails` (Deployment) are complete and accessible
2. Prepare documentation: model card, risk assessment, training data lineage
3. Identify audit scope: which systems, use cases, and criteria
4. Select an auditor with relevant domain expertise and independence
5. Define what "sharing the outcome" means for your stakeholders

**Regulatory context:**
- **EU AI Act** requires conformity assessments for high-risk AI systems
- **GDPR** requires Data Protection Impact Assessments (DPIA) for high-risk processing
- **Financial services**: Model Risk Management (SR 11-7) requires model validation

**Related:** audit_trails (Deployment), risk, code_conduct
