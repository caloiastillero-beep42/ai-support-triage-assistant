# Example — Transaction / Payment Failure

## Customer Report

> I tried to complete a transaction several times, but it keeps failing. The amount hasn't been deducted from my account, but I'm not sure why the transaction won't go through.

---

## 1. Issue Summary

The customer is unable to complete a transaction. No successful transaction has been recorded, and the customer does not know whether the failure is related to their account or the platform.

**Initial classification:** Transaction processing issue

---

## 2. Customer Impact

**Impact:** High

The customer is currently unable to complete an important transaction.

At this stage, the scope of the issue is unknown, so it should not automatically be treated as a widespread incident.

---

## 3. Initial Priority

**Priority:** High

The issue is blocking the customer's intended transaction and has no confirmed workaround.

Priority should be reassessed if additional information shows that multiple customers or transactions are affected.

---

## 4. Missing Information

Before escalating, support should collect:

* Customer/account ID
* Transaction ID, if available
* Approximate time of the failed transaction
* Exact error message
* Number of failed attempts
* Whether other transaction types work
* Whether the customer has successfully completed transactions previously
* Any relevant account or configuration changes

---

## 5. Initial Hypotheses

Possible causes include:

1. Account or permission issue
2. Invalid or incomplete transaction information
3. Temporary platform issue
4. Transaction processing failure
5. Configuration problem
6. Issue affecting a specific transaction type

These are hypotheses and should be tested rather than presented as confirmed causes.

---

## 6. Troubleshooting Plan

### Step 1 — Confirm the failure

Verify the exact error message and identify the affected transaction.

### Step 2 — Check transaction history

Determine whether the transaction was rejected, failed, cancelled, or never entered the processing system.

### Step 3 — Check scope

Determine whether:

* Only this customer is affected
* Multiple transactions are affected
* Other customers are reporting similar failures

### Step 4 — Review available logs

Use the transaction ID and timestamp to locate relevant system activity.

Look for:

* Processing errors
* Validation failures
* Service errors
* Repeated failures
* Unexpected system responses

### Step 5 — Attempt reproduction

If possible, reproduce the same transaction using a safe test environment or approved support procedure.

---

## 7. Escalation Decision

**Escalation:** Not immediately.

Support should first collect the missing information and determine whether the problem can be reproduced.

Escalation becomes appropriate if:

* The transaction appears valid but consistently fails
* Logs indicate a platform-side failure
* The issue can be reproduced
* Multiple customers or transactions are affected
* The problem requires engineering access

---

## 8. Engineering Escalation Example

If escalation becomes necessary:

**Customer / Account:** [Account ID]

**Issue:** Transaction repeatedly fails

**Business impact:** Customer is unable to complete transaction

**Started:** [Timestamp]

**Transaction ID:** [Transaction ID]

**Expected behavior:** Transaction should complete successfully

**Actual behavior:** Transaction fails without completing

**Steps to reproduce:**

1. Attempt transaction
2. Submit transaction
3. Transaction fails
4. Repeat attempt
5. Same failure occurs

**Troubleshooting performed:**

* Confirmed customer/account status
* Verified transaction details
* Reviewed transaction history
* Reviewed available logs
* Attempted reproduction

**Relevant errors:** [Error message / log information]

**Support assessment:**

Evidence suggests the transaction may be failing during platform-side processing. Engineering assistance is requested to investigate the underlying failure.

---

## 9. Customer Communication

> Thanks for reporting this. I've reviewed the information available so far and can see that the transaction isn't completing successfully.
>
> I'd like to gather a few additional details so we can narrow down where the failure is occurring. Could you provide the transaction ID, the approximate time of your most recent attempt, and the exact error message you received?
>
> Once we have those details, we can continue investigating and determine the appropriate next step.

---

## 10. What This Example Demonstrates

This example shows the difference between:

**Customer complaint → Investigation → Evidence → Hypothesis → Troubleshooting → Escalation**

rather than:

**Customer complaint → Send to Engineering**

The goal is to make escalation more useful by giving the next team enough context to continue the investigation without repeating the initial troubleshooting.
