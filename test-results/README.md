Triage Evaluation

This directory contains the results of testing the AI Support Triage workflow against different technical SaaS support scenarios.

The purpose of these tests is not to measure whether the AI correctly identifies a single root cause.

Instead, the tests evaluate whether the workflow:

Identifies the appropriate issue category
Assesses customer impact appropriately
Assigns a reasonable priority
Requests relevant missing information
Distinguishes evidence from hypotheses
Recommends proportionate troubleshooting
Escalates when the evidence or business impact justifies it
Avoids unnecessary escalation when the issue can remain with support
Produces useful engineering context when escalation is appropriate
Produces a clear customer-facing response
Test Scenarios
Scenario	Evidence Level	Customer Impact	Triage Decision
Transaction failure	Limited	Medium	Continue troubleshooting
Webhook delivery failure	Moderate	High	Continue investigation
Webhook 500 failure	Strong	High	Escalate
Critical production webhook outage	Strong	Critical	Immediate escalation
Expired API key	Strong	Low	Continue troubleshooting
What the Tests Demonstrate
1. Limited evidence should lead to investigation

The transaction failure scenario contains very little diagnostic information.

The workflow avoids assuming a platform defect and instead identifies the information needed to investigate the failure.

Expected behavior: Gather evidence before escalating.

2. Technical severity and business impact both matter

The webhook delivery scenario shows a production integration problem affecting completed orders.

The issue is treated as high priority, but the workflow does not immediately declare a platform defect because the failure point has not yet been established.

Expected behavior: Investigate the delivery path and establish where the failure occurs.

3. Stronger evidence can justify escalation

In the webhook 500 scenario, events are being generated and delivery attempts consistently fail with HTTP 500 responses while the customer's endpoint appears healthy.

This provides substantially stronger evidence of a potential failure in the webhook delivery path.

Expected behavior: Escalate with the available evidence while clearly labeling unverified information as customer-reported.

4. Critical business impact can justify immediate escalation

The critical webhook outage affects a production fulfillment workflow processing hundreds of orders per hour.

The warehouse has stopped receiving new orders and there is no workaround.

Even without confirmed root cause, the business impact is sufficient to justify immediate escalation.

Expected behavior: Escalate immediately while Engineering investigates the technical cause.

5. Resolved authentication issues do not require unnecessary escalation

The expired API key scenario demonstrates the opposite case.

The customer generated a new key, confirmed that requests work normally, and reported no customer impact.

The remaining question is whether the expiration behavior was expected.

Expected behavior: Continue troubleshooting or documentation rather than escalating unnecessarily.

Evaluation Principle

The central evaluation principle is:

Evidence + Customer Impact → Support Decision

The workflow should not produce the same escalation recommendation for every technical issue.

As evidence becomes stronger or customer impact increases, the appropriate support action may change.

This is the behavior the test cases are intended to demonstrate.

Limitations

These tests are qualitative rather than a formal benchmark.

The scenarios are representative support cases based on realistic SaaS troubleshooting patterns, but they do not establish statistical performance or guarantee correct decisions in production.

A support specialist must still verify the AI's output against actual system data, logs, customer information, and applicable support procedures.
