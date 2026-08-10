Critical Webhook Outage Test
Test Scenario

A customer reported a production webhook outage lasting approximately two hours.

The customer reported that:

Orders were still being created successfully.
None of the webhook events were reaching the fulfillment system.
The customer processes hundreds of orders per hour.
The warehouse had stopped receiving new orders.
The customer's endpoint was online.
Webhook deliveries were failing with HTTP 500.
There was no available workaround.
Expected Triage Behavior

The assistant should:

Recognize the issue as a critical production incident.
Prioritize business impact alongside technical symptoms.
Recommend immediate escalation rather than prolonged first-line troubleshooting.
Identify the evidence needed for Engineering to investigate.
Avoid assuming the platform is definitely the root cause.
Warn against repeated manual retries when duplicate-delivery risk is unknown.
Clearly distinguish customer-reported information from independently verified information.
Triage Result

Category: Integration

Customer Impact: Critical

Priority: Critical

Escalation Decision: Escalate immediately

The reported issue affects a production fulfillment workflow processing hundreds of orders per hour.

The warehouse has stopped receiving new orders and there is no available workaround. The webhook delivery service is reportedly returning HTTP 500 for every delivery attempt.

The evidence supports immediate escalation based on the severity and business impact, while the exact technical root cause still requires verification.

Key Evidence
Production integration affected.
Incident ongoing for approximately two hours.
Every webhook delivery reportedly failing.
HTTP 500 responses reported.
Hundreds of orders per hour affected.
Fulfillment workflow interrupted.
Warehouse no longer receiving new orders.
No workaround available.
Engineering Investigation

Engineering should determine:

Where the HTTP 500 response is generated.
Whether requests reach the customer's endpoint.
Whether webhook events are being queued or retried.
Whether affected events can be recovered safely.
Whether other customers or integrations are affected.
Whether a deployment, configuration change, or infrastructure incident coincides with the start time.
Important Guardrail

The customer's report that the endpoint is online and that the webhook service returns HTTP 500 should remain identified as customer-reported until independently verified through logs, monitoring, testing, or other reliable system evidence.

The escalation decision is based on the reported severity and business impact, not on a confirmed root cause.

Support Principle Demonstrated

Escalation urgency should be based on evidence and customer impact, not only on root-cause certainty.

A support team should not wait for complete root-cause identification before escalating a critical production incident when the available evidence shows severe ongoing business impact.
