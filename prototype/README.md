# AI Support Triage Prototype

A minimal executable prototype of the AI Support Triage workflow.

The prototype loads the reusable triage prompt from:

`../prompts/ai-support-triage.md`

It accepts a customer-reported issue, sends it through the configured AI model, and returns a structured support triage analysis.

## Requirements

* Python 3.9+
* An OpenAI API key
* Internet access

## Installation

From the repository root:

```bash
cd prototype
pip install -r requirements.txt
```

## Configure the API Key

Set the `OPENAI_API_KEY` environment variable.

### macOS / Linux

```bash
export OPENAI_API_KEY="your-api-key"
```

### Windows PowerShell

```powershell
$env:OPENAI_API_KEY="your-api-key"
```

Do not place API keys directly in the repository.

## Run

From the `prototype` directory:

```bash
python triage.py
```

Paste the customer's issue when prompted.

Type:

```text
END
```

on a new line when the customer message is complete.

The prototype will return:

* Issue summary
* Issue category
* Customer impact
* Priority
* Missing information
* Possible causes
* Troubleshooting plan
* Escalation decision
* Engineering context
* Customer response

## Example

Input:

```text
Our webhook events stopped reaching our fulfillment system. Orders are still completing, but our warehouse is no longer receiving the events. This started about two hours ago.

END
```

The resulting analysis should be reviewed by a support specialist against actual system data and logs.

## Important

This prototype is a support decision aid, not an autonomous support system.

The support specialist remains responsible for:

* Verifying information
* Checking system data and logs
* Confirming reproduction
* Deciding whether to escalate
* Communicating with the customer
* Making the final resolution decision
