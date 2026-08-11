# AI Support Triage Evaluation Matrix

## Purpose

This matrix summarizes how the AI Support Triage workflow responds to different customer-support scenarios.

The goal is not to determine whether the AI correctly identifies a single technical root cause.

Instead, the evaluation focuses on whether the workflow produces a proportionate support decision based on:

**Evidence + Customer Impact**

---

## Scenario Matrix

| Scenario                           | Evidence Level | Customer Impact | Priority | Triage Decision          |
| ---------------------------------- | -------------- | --------------- | -------- | ------------------------ |
| Transaction failure                | Limited        | Medium          | High     | Continue troubleshooting |
| Webhook delivery failure           | Moderate       | High            | High     | Continue investigation   |
| Webhook 500 failure                | Strong         | High            | High     | Escalate                 |
| Critical production webhook outage | Strong         | Critical        | Critical | Immediate escalation     |
| Expired API key                    | Strong         | Low             | Low      | Continue troubleshooting |

---

## Scenario Analysis

### 1. Transaction Failure

**Evidence:** Limited
**Customer Impact:** Medium
**Priority:** High
**Decision:** Continue troubleshooting

The customer reports repeated transaction failures but provides limited diagnostic information.

The workflow should not assume a platform-side defect.

It should first collect relevant information such as:

* Transaction ID
* Timestamp
* Exact error message
* Account information
* Transaction history
* Scope of the failure

**Expected support behavior:** Gather evidence before escalating.

---

### 2. Webhook Delivery Failure

**Evidence:** Moderate
**Customer Impact:** High
**Priority:** High
**Decision:** Continue investigation

Orders are completing successfully, but webhook events are no longer reaching the customer's internal system.

The integration is important to the customer's workflow, but the exact failure point has not yet been established.

The investigation should determine whether the problem is occurring in:

* Event generation
* Webhook delivery
* Routing or configuration
* Customer endpoint
* Downstream processing

**Expected support behavior:** Investigate the delivery path before assigning a confirmed root cause.

---

### 3. Webhook 500 Failure

**Evidence:** Strong
**Customer Impact:** High
**Priority:** High
**Decision:** Escalate

Webhook events are being generated and delivery attempts consistently return HTTP 500 responses while the customer's endpoint appears healthy.

The evidence provides a stronger indication that the failure may exist within the webhook delivery path.

However, the HTTP 500 source should still be independently verified through logs or system data.

**Expected support behavior:** Escalate with the available evidence while clearly identifying unverified information.

---

### 4. Critical Production Webhook Outage

**Evidence:** Strong
**Customer Impact:** Critical
**Priority:** Critical
**Decision:** Immediate escalation

A production fulfillment integration processing hundreds of orders per hour has stopped receiving webhook events.

The warehouse has stopped receiving new work and there is no workaround.

The business impact alone is sufficient to justify immediate escalation while Engineering investigates the technical cause.

The support team should preserve affected event IDs, timestamps, delivery information, and retry state for investigation and potential recovery.

**Expected support behavior:** Escalate immediately. Do not wait for complete root-cause certainty.

---

### 5. Expired API Key

**Evidence:** Strong
**Customer Impact:** Low
**Priority:** Low
**Decision:** Continue troubleshooting/documentation

API requests return HTTP 401 because the API key has expired.

The customer generates a new key and confirms that requests work normally.

There is no broader customer impact.

**Expected support behavior:** Resolve through normal support procedures and document the behavior if necessary rather than escalating unnecessarily.

---

## What the Matrix Demonstrates

The workflow should **not produce the same recommendation for every technical problem**.

A simple technical error does not automatically require Engineering involvement.

Likewise, a critical production incident should not remain in routine troubleshooting simply because the root cause has not yet been confirmed.

The decision should change as the evidence and business impact change.

### Evidence progression

**Limited evidence**

→ Gather information

**Moderate evidence**

→ Investigate and establish scope

**Strong evidence**

→ Escalate when the technical evidence supports it

**Critical business impact**

→ Escalate immediately when continued support investigation creates unacceptable operational risk

---

## Evaluation Criteria

Each scenario can be evaluated against the following criteria:

### Classification

Did the workflow identify the appropriate issue category?

### Customer Impact

Did it correctly assess how seriously the customer is affected?

### Priority

Was the recommended priority proportionate to urgency, scope, and business impact?

### Evidence Gathering

Did it request the information needed to investigate the issue?

### Hypothesis Quality

Did it distinguish possible causes from confirmed facts?

### Troubleshooting

Did it recommend safe, useful, and proportionate investigation steps?

### Escalation

Did it escalate when the evidence or customer impact justified escalation?

### Engineering Context

When escalation was appropriate, did it provide useful context without inventing information?

### Customer Communication

Did the response acknowledge the issue, avoid unsupported conclusions, and clearly explain the next step?

---

## Limitations

This is a qualitative evaluation rather than a formal statistical benchmark.

The scenarios are representative support cases based on realistic SaaS troubleshooting patterns.

They do not establish production accuracy or guarantee that the AI will make the correct decision in every situation.

The output must still be verified against:

* System data
* Logs
* Customer information
* Product behavior
* Applicable support procedures

The support specialist remains responsible for the final decision.
