import json
import os
from pathlib import Path

try:
from openai import OpenAI
except ImportError:
OpenAI = None

PROMPT_PATH = Path(**file**).resolve().parent.parent / "prompts" / "ai-support-triage.md"

def load_prompt():
return PROMPT_PATH.read_text(encoding="utf-8")

def build_prompt(customer_message):
prompt = load_prompt()
return prompt.replace("{{CUSTOMER_MESSAGE}}", customer_message)

def run_triage(customer_message):
if OpenAI is None:
raise RuntimeError(
"The OpenAI package is not installed. Run: pip install openai"
)

```
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise RuntimeError(
        "OPENAI_API_KEY is not set. Add your API key as an environment variable."
    )

client = OpenAI(api_key=api_key)

response = client.responses.create(
    model="gpt-5-mini",
    input=build_prompt(customer_message)
)

return response.output_text
```

def main():
print("=" * 60)
print("AI Support Triage Assistant")
print("=" * 60)
print()
print("Paste the customer issue below.")
print("Type END on a new line when finished.")
print()

```
lines = []

while True:
    line = input()

    if line.strip() == "END":
        break

    lines.append(line)

customer_message = "\n".join(lines).strip()

if not customer_message:
    print("No customer issue was provided.")
    return

print()
print("Running triage...")
print()

try:
    result = run_triage(customer_message)
    print(result)

except Exception as error:
    print(f"Error: {error}")
```

if **name** == "**main**":
main()
