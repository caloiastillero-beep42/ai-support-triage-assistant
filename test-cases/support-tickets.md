# Support Ticket Test Cases

These fictional test cases represent common issues encountered in SaaS, fintech, and enterprise support environments.

The purpose is to test whether an AI-assisted triage workflow can identify customer impact, gather the right diagnostic information, recommend appropriate troubleshooting steps, and determine when an issue should be escalated.

---

## Test Case 1 — Transaction / Payment Failure

**Customer message:**

> I tried to complete a transaction several times, but it keeps failing. The amount hasn't been deducted from my account, but I'm not sure why the transaction won't go through.

**Known information:**

* Customer cannot complete the transaction
* No successful transaction has been recorded
* Customer is unsure whether the issue is account-related or platform-related

**Expected support investigation:**

* Confirm the exact error message
* Identify the affected transaction
* Check transaction status and timestamps
* Review available transaction or platform logs
* Determine whether the issue is isolated to the customer or affects other users
* Check account status and relevant configuration
* Attempt to reproduce the issue when possible

**Potential escalation:**

Escalate to Engineering or the appropriate technical team when the transaction appears valid but the platform is failing to process it correctly, or when available logs indicate a system-level issue.

---

## Test Case 2 — Incorrect or Missing Data

**Customer message:**

> Some information that I entered yesterday isn't showing up correctly today. I've checked the details several times and I'm sure I submitted them correctly.

**Known information:**

* Customer reports missing or incorrect data
* Customer believes the information was submitted correctly
* The issue appears to affect recently submitted information

**Expected support investigation:**

* Identify the affected records
* Confirm when the information was submitted
* Compare the customer's submitted information with what appears in the platform
* Check account and workflow configuration
* Review available logs or system history
* Determine whether the issue affects one record or multiple records
* Attempt to reproduce the behavior when possible

**Potential escalation:**

Escalate when the submitted information is valid but is not being stored, displayed, or processed correctly by the platform.

---

## Test Case 3 — Billing Discrepancy

**Customer message:**

> Our invoice is higher than expected this month. We were charged for more usage than what we see in the dashboard.

**Known information:**

* Customer disputes the invoice amount
* Dashboard usage does not appear to match the invoice

**Expected support investigation:**

* Confirm invoice number and billing period
* Compare invoice line items against reported usage
* Check account plan and pricing
* Look for credits, adjustments, or additional charges
* Verify whether usage is being reported correctly
* Escalate to Billing or Finance when necessary

**Potential escalation:**

Escalate when the discrepancy cannot be explained by documented pricing, usage, credits, or adjustments.

---

## Test Case 4 — Account Access Issue

**Customer message:**

> I can't log into my account anymore. I reset my password twice but I'm still getting an error.

**Known information:**

* Password reset has already been attempted
* Customer still cannot access the account

**Expected support investigation:**

* Confirm exact error message
* Confirm whether the issue affects one user or multiple users
* Verify account status
* Check authentication method
* Confirm whether the customer can access password reset successfully
* Check for known authentication incidents

**Potential escalation:**

Escalate if the account is active, credentials are valid, and the issue can be reproduced or appears to be platform-related.

---

## Test Case 5 — Data Synchronization Issue

**Customer message:**

> The data in our dashboard is different from what we see in our internal system. Some records from yesterday are missing.

**Known information:**

* Data discrepancy affects recent records
* Customer's internal system contains records missing from the platform

**Expected support investigation:**

* Identify affected records
* Confirm timestamps
* Determine synchronization method
* Check whether the missing records were successfully submitted
* Review processing or integration logs
* Determine whether the issue is isolated or widespread

**Potential escalation:**

Escalate if records were successfully submitted but were not processed or stored correctly.

---

## Test Case 6 — Suspected Product Bug

**Customer message:**

> Every time I try to save this configuration, the page says it was saved but when I refresh, the settings are gone.

**Known information:**

* UI reports successful save
* Configuration does not persist
* Issue occurs repeatedly

**Expected support investigation:**

* Confirm affected configuration
* Reproduce the issue
* Identify browser/device/environment
* Check whether the issue affects other users
* Capture timestamps and relevant IDs
* Check for known incidents or recent releases

**Potential escalation:**

Engineering escalation is appropriate if the issue is reproducible and configuration data is not being persisted correctly.

---

## Test Case 7 — Performance Issue

**Customer message:**

> The dashboard has become extremely slow today. Pages that normally load in a few seconds are taking almost a minute.

**Known information:**

* Performance degraded significantly
* Issue appears to have started recently

**Expected support investigation:**

* Confirm affected pages
* Determine whether all users are affected
* Identify approximate start time
* Check whether the issue is intermittent
* Check for known incidents or service degradation
* Collect timestamps and account information

**Potential escalation:**

Escalate when the issue appears widespread or evidence suggests a service-level performance problem.

---

## Test Case 8 — Configuration / Workflow Problem

**Customer message:**

> We changed our workflow configuration yesterday and now some orders aren't being processed automatically. Can you tell us what went wrong?

**Known information:**

* Workflow configuration was recently changed
* Automation is no longer processing some orders

**Expected support investigation:**

* Identify the configuration changes
* Compare previous and current settings
* Identify affected orders
* Determine whether the issue affects all orders or specific conditions
* Check workflow execution history
* Reproduce with a test case if possible

**Potential escalation:**

Escalate when the configuration appears correct but the workflow is not behaving as expected.
