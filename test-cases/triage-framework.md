# Support Triage Framework

This framework defines how a support specialist should evaluate a customer issue before deciding how to troubleshoot, resolve, or escalate it.

The goal is not to automatically solve every issue. The goal is to make the investigation structured, consistent, and actionable.

---

## 1. Understand the Issue

First identify what the customer is actually reporting.

### Questions to answer

* What is the customer trying to accomplish?
* What went wrong?
* What behavior did they expect?
* What behavior actually occurred?
* When did the issue start?
* Is the issue still happening?

### Output

**Issue summary:** A short description of the customer's problem in operational/technical terms.

---

## 2. Determine Customer Impact

Not every technical issue has the same urgency.

Evaluate:

* Number of affected users
* Number of affected transactions or records
* Whether the customer's business is blocked
* Whether there is a workaround
* Whether data may be lost or corrupted
* Whether the issue is intermittent or persistent
* Whether other customers may be affected

### Impact levels

**Low**

* Minor inconvenience
* Workaround available
* No significant business impact

**Medium**

* Important functionality affected
* Workaround may exist but is inefficient
* Limited number of users or workflows affected

**High**

* Important business workflow is blocked
* Multiple users or critical processes affected
* No practical workaround

**Critical**

* Widespread service disruption
* Significant data integrity concern
* Security or financial impact
* Large-scale customer impact

---

## 3. Assign Priority

Priority should consider both customer impact and urgency.

A useful principle is:

**Priority = Impact + Urgency**

A high-impact issue that is not immediately time-sensitive may require different handling from an issue that is actively preventing a customer from completing a critical business process.

The support specialist should also consider existing SLA requirements and internal escalation policies.

---

## 4. Identify Missing Information

Before troubleshooting, determine what information is missing.

Common examples include:

* Account or customer ID
* User affected
* Timestamp
* Error message
* Screenshot
* Transaction or record ID
* Browser/device information
* Steps to reproduce
* Expected behavior
* Actual behavior
* Recent configuration changes
* Scope of affected users or records

Avoid asking the customer for information that is not useful to the investigation.

Every question should have a reason.

---

## 5. Form Initial Hypotheses

Based on the available information, identify possible causes.

Examples:

* Configuration problem
* Account or permission issue
* User error
* Data issue
* Workflow issue
* Product defect
* Service degradation
* Integration problem
* Recent product change

These are hypotheses, not conclusions.

The purpose is to determine what should be tested next.

---

## 6. Troubleshoot Systematically

Troubleshooting should follow an evidence-based process.

### Recommended sequence

1. Confirm the issue
2. Review available information
3. Check for known incidents or changes
4. Reproduce the behavior when possible
5. Isolate the affected component or workflow
6. Test the most likely causes
7. Apply a safe resolution or workaround
8. Confirm the result
9. Document the outcome

Avoid making multiple unrelated changes at once because this makes the root cause harder to identify.

---

## 7. Decide Whether to Escalate

Escalation should happen when support has gathered enough information for another team to act.

### Escalate when:

* The issue is reproducible and appears to be a product defect
* Available evidence indicates a system-level problem
* The issue requires engineering access
* The problem affects multiple customers
* Data integrity may be affected
* A critical workflow is blocked
* The issue requires permissions or technical access unavailable to support

### Do not escalate simply because:

* The issue is difficult
* The customer is frustrated
* Initial troubleshooting did not immediately work
* The support specialist has not yet gathered enough information

A good escalation should reduce the amount of investigation the next team has to repeat.

---

## 8. Prepare the Engineering Escalation

When escalation is necessary, include:

**Customer / Account:**

**Issue summary:**

**Business impact:**

**When it started:**

**Affected users / records:**

**Expected behavior:**

**Actual behavior:**

**Steps to reproduce:**

**Troubleshooting already performed:**

**Relevant error messages:**

**Relevant logs / IDs / timestamps:**

**What support believes is happening:**

**What is still unknown:**

This structure gives Engineering enough context to begin investigating without starting from zero.

---

## 9. Communicate With the Customer

Technical accuracy is only part of good support.

The customer response should:

* Acknowledge the issue
* Clearly explain what has been confirmed
* Avoid unsupported assumptions
* Explain the next step
* Set expectations when appropriate
* Avoid unnecessary technical jargon
* Close the loop when the issue is resolved

Internal technical uncertainty should not become misleading customer communication.

---

## 10. Document the Outcome

After resolution, capture useful information for future cases.

Document:

* Root cause
* Resolution
* Workaround
* Relevant troubleshooting steps
* Known limitations
* Whether documentation should be updated
* Whether the issue should be reported to Product or Engineering

Repeated support issues should eventually become opportunities for:

**Documentation → Automation → Product improvement**

---

## Core Principle

The goal of support triage is not simply to move tickets faster.

The goal is to move the **right information** to the **right person** at the **right time**, while giving the customer a clear path toward resolution.
