# Webhook Escalation Test

## Test Scenario

A customer reported that their webhook integration stopped delivering new order events around 10:30 AM UTC.

The customer reported that:

* Webhook events were being generated.
* Every delivery attempt since 10:30 AM UTC was failing with HTTP 500.
* Their webhook endpoint was healthy.
* The endpoint returned HTTP 200 when tested directly.
* The issue affected every new order received that day.

## Expected Triage Behavior

The assistant should:

1. Recognize the issue as a high-impact integration problem.
2. Avoid immediately assuming the platform is at fault.
3. Identify the evidence needed to determine where the failure occurs.
4. Recommend escalation once the available evidence supports a potential platform-side failure.
5. Clearly distinguish customer-reported information from independently verified information.

## Triage Result

**Category:** Integration

**Customer Impact:** High

**Priority:** High

**Escalation Decision:** Escalate

The available evidence supports escalation because webhook events are being generated successfully while delivery attempts consistently fail with HTTP 500 errors.

The customer's endpoint reportedly responds normally when tested independently, making a failure in the webhook delivery path a reasonable hypothesis.

The exact root cause remains unconfirmed and requires verification through platform logs and infrastructure data.

## Engineering Context

**Issue:** Webhook deliveries for new orders are failing with HTTP 500 errors.

**Start Time:** Approximately 10:30 AM UTC.

**Affected Records:** All new orders received by the customer that day, according to the customer.

**Expected Behavior:** Generated order webhook events should be successfully delivered to the customer's endpoint.

**Actual Behavior:** Events are generated, but delivery attempts fail with HTTP 500.

**Customer Troubleshooting:** The customer confirmed that their endpoint is healthy, receives traffic from other services, and returns HTTP 200 when tested directly.

**Known Error:** HTTP 500 from the webhook delivery service.

**Remaining Questions:**

* Do failed requests actually reach the customer's endpoint?
* What is generating the HTTP 500?
* Are other customers experiencing the same issue?
* Did a platform deployment or infrastructure change occur around 10:30 AM UTC?
* Is there a broader webhook delivery incident?

## Key Observation

The assistant correctly changed its recommendation as additional evidence became available.

The initial webhook scenario recommended continued investigation because the source of the failure was unclear.

After the customer provided evidence of consistent HTTP 500 responses from the webhook delivery service, the assistant recommended escalation.

This demonstrates an evidence-based triage workflow rather than automatic escalation.

## Support Principle Demonstrated

**Investigate first. Escalate when the evidence justifies it.**

Customer-reported information should remain clearly identified as customer-reported until independently verified through logs, system data, testing, or another reliable source.
