# AI Support Triage Workflow Architecture

## Overview

The AI Support Triage Assistant is designed as a structured decision-support workflow for technical SaaS support teams.

The workflow takes a customer-reported issue and progressively converts an unstructured support request into:

* A clear issue classification
* A customer-impact assessment
* A priority recommendation
* A list of missing evidence
* Ranked troubleshooting hypotheses
* A proportionate investigation plan
* An escalation recommendation
* Structured engineering context
* A customer-facing response

The AI is used to improve consistency and reduce repetitive triage work.

The support specialist remains responsible for verification, judgment, escalation, and final customer communication.

---

## Workflow

The core workflow is:

**Understand → Investigate → Troubleshoot → Resolve → Document**

### 1. Customer Report

The workflow begins with the customer's original report.

The system should preserve the customer's reported facts without adding assumptions.

Example:

> "Our orders are completing, but none of the webhook events are reaching our fulfillment system."

At this stage, the cause is unknown.

---

### 2. Issue Classification

The reported problem is categorized into the most appropriate support domain.

Examples include:

* Account / Access
* Billing
* Transaction / Payment
* API
* Authentication
* Data
* Integration
* Configuration / Workflow
* Product Bug
* Performance
* Other

Classification provides structure for the investigation but does not determine the root cause.

---

### 3. Customer Impact

The workflow evaluates how seriously the issue affects the customer.

Impact levels:

**Low**

Minor inconvenience with little or no business disruption.

**Medium**

A meaningful problem affecting a customer workflow but with limited operational impact.

**High**

A significant workflow is blocked or materially degraded.

**Critical**

A production workflow is severely disrupted, there is substantial business impact, or there is no reasonable workaround.

Customer impact is considered independently from the technical symptom.

---

### 4. Priority

Priority combines urgency, scope, and business impact.

A technical error does not automatically require a critical priority.

Conversely, a relatively simple technical failure may require immediate escalation when the business impact is critical.

Priority should be reassessed as new evidence becomes available.

---

### 5. Evidence Gathering

Before making strong conclusions, the workflow identifies the evidence required to investigate the problem.

Examples include:

* Customer or account ID
* Transaction ID
* Order or event ID
* Timestamp and timezone
* Exact error message
* HTTP status code
* Request or response information
* Relevant logs
* Reproduction steps
* Scope of affected users or records
* Recent configuration changes

The workflow should request only information that is relevant to the reported issue.

---

### 6. Hypothesis Generation

Once the available evidence is understood, the workflow identifies possible causes.

Hypotheses are ranked based on the available evidence.

For example:

1. Platform-side processing failure
2. Integration delivery failure
3. Configuration issue
4. Customer endpoint issue

The workflow must clearly distinguish hypotheses from confirmed root causes.

---

### 7. Troubleshooting

Troubleshooting should begin with the lowest-risk and highest-value checks.

A typical investigation may include:

1. Confirm the reported behavior.
2. Establish the scope of the issue.
3. Review relevant account or transaction records.
4. Review system or delivery logs.
5. Attempt safe reproduction when appropriate.
6. Compare behavior with expected system behavior.
7. Identify the failure point.
8. Determine whether the issue can be resolved through support.

Customer-side changes should not be recommended without sufficient evidence that they are relevant and safe.

---

### 8. Escalation Decision

The workflow determines whether support should continue troubleshooting or escalate.

Possible outcomes:

**Continue troubleshooting**

Use when available evidence is insufficient or the issue can reasonably remain within support.

**Escalate**

Use when:

* A platform-side failure is suspected based on evidence.
* The issue cannot be resolved through available support procedures.
* Reproduction confirms a product or system problem.
* Multiple customers or records are affected.
* Engineering access or investigation is required.
* Business impact justifies immediate engineering involvement.

Escalation does not require complete root-cause certainty.

---

### 9. Engineering Context

When escalation is appropriate, the workflow converts the investigation into structured engineering context.

The escalation should include:

* Customer / Account
* Issue summary
* Business impact
* Time started
* Affected users or records
* Expected behavior
* Actual behavior
* Steps to reproduce
* Troubleshooting performed
* Error messages
* Relevant IDs and timestamps
* Current hypothesis
* Remaining unknowns

Missing information should be explicitly marked as **Not provided** rather than invented.

---

### 10. Customer Communication

The workflow produces a customer-facing response based only on verified or clearly identified customer-reported information.

The response should:

* Acknowledge the issue
* Explain what is currently known
* Ask only necessary questions
* Explain the next step
* Avoid unsupported conclusions
* Avoid unnecessary technical jargon
* Avoid exposing internal reasoning

The response should remain useful even when the technical root cause has not yet been established.

---

## Decision Model

The central decision principle is:

**Evidence + Customer Impact → Support Decision**

The same technical symptom can result in different support actions.

For example:

### Limited evidence + Medium impact

A transaction fails but the customer provides no transaction ID, error message, or timestamp.

**Decision:** Continue gathering evidence.

### Strong evidence + High impact

Webhook delivery consistently returns HTTP 500 while the customer's endpoint appears healthy.

**Decision:** Escalate with the available evidence.

### Strong evidence + Critical impact

A production fulfillment integration processing hundreds of orders per hour stops receiving events and there is no workaround.

**Decision:** Immediate escalation.

This prevents the workflow from treating every technical error as an Engineering incident.

---

## Guardrails

The workflow is designed around several safety and quality principles.

### Do not invent information

Never fabricate:

* Customer IDs
* Transaction IDs
* Logs
* Error messages
* Timestamps
* System behavior
* Reproduction results

### Separate evidence from hypotheses

Customer-reported information should remain clearly identified as customer-reported until independently verified.

### Avoid false certainty

A possible cause should never be presented as a confirmed root cause without supporting evidence.

### Protect production systems

Avoid unnecessary production retries or customer-side changes when they could create duplicate processing, data changes, or other unintended consequences.

### Protect sensitive information

Never expose:

* API keys
* Passwords
* Credentials
* Tokens
* Secrets
* Other sensitive customer information

### Preserve human judgment

The AI provides structure and recommendations.

The support specialist remains responsible for:

* Verification
* Investigation
* Escalation
* Customer communication
* Final resolution

---

## Testing Strategy

The workflow is evaluated using representative support scenarios with different evidence levels and customer-impact levels.

The goal is to determine whether the recommendation changes appropriately as the available information changes.

Example test progression:

**Limited evidence → Gather information**

**Moderate evidence → Investigate**

**Strong evidence → Escalate when justified**

**Critical business impact → Escalate immediately**

This makes the test cases useful for evaluating decision quality rather than simply checking whether the AI identifies a particular technical root cause.

---

## Future Development

Future iterations may extend the workflow with:

* Automated ticket classification
* Structured support-quality scoring
* Larger scenario test suites
* Regression testing for prompt changes
* AI-assisted help-center generation
* Automated escalation templates
* Support analytics
* AI agent evaluation
* Workflow automation
* Integration with ticketing systems
* Human-versus-AI triage comparisons

The long-term goal is to explore how AI can augment experienced support specialists without removing human ownership from technical support decisions.
