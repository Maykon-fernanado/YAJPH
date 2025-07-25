# YAJPH: Statically Typed Prompts for Python

> 🔧 Write prompts like functions. Enforce structure like Pydantic.  
> 🧠 Finally, prompt engineering you can debug, test, and trust.

YAJPH (YAML + JSON + Prompt + Human) is a type-safe prompt engineering layer that lets you:

- ✅ Define strict input/output schemas for LLMs
- ✅ Validate prompt payloads like real software
- ✅ Debug LLM responses with explainable logs
- ✅ Build modular, testable, auditable AI workflows

Think: `TypedDict` + `Pydantic` + `LLM router` — all powered by YAML.

---

## 🚨 Problem

Prompt engineering is the new spaghetti code.

- Inputs are unvalidated
- Outputs are unpredictable
- Errors are silent
- Logic is hidden in natural language

You wouldn't ship an API like this. Why do it with AI?

---

## ✅ Solution

**YAJPH** brings type safety to AI logic.

```yaml
# Define inputs/outputs in YAML
inputs:
  name: { type: string, min_length: 1 }
  tone: { enum: ["friendly", "formal"] }

outputs:
  greeting: { type: string }

prompt: |
  Write a {{ tone }} greeting for {{ name }}.

At runtime:
json
{

  "inputs": { "name": "Alice", "tone": "friendly" },
  "output": { "greeting": "Hey Alice!" }
}
Invalid inputs or hallucinated outputs? YAJPH throws structured, explainable errors.
🔁 Built for Real AI Systems

    🛠️ Works with OpenAI, Anthropic, Local Models

    🧪 Testable, version-controlled YAML logic

    🔁 Swappable agents, clean logs, modular prompts

    📦 Use in CLI, backend services, notebooks, or agents

💡 Why It Matters

LLMs are too powerful to be unchecked.
YAJPH is your type system, debugger, and reasoning layer — in one.

    No more prompt soup

    No more JSON schema duct tape

    No more hallucinated pipelines

YAJPH lets you build cognitive software like real software.
🔮 What’s Next?

YAJPH is just the beginning.

    Coming soon:

        🧠 "Universal Reasoning Bus" mode for multi-agent coordination

        📊 Monte Carlo prompt simulations

        🔒 Permissioned cognitive graphs for critical decisions

🧠 Philosophy (Optional)

Under the hood, YAJPH is a new kind of reasoning infrastructure.
We treat YAML as the cognitive OS — and LLMs as modular workers.

It’s not just about prompts. It’s about trustable, auditable thinking at scale.

But you don’t need to believe that yet.
Just try typing your first prompt like it’s a function — and see what happens.
📦 Install

pip install yajph

🏁 Quickstart

▶️ Click here for a 1-minute example
📚 Full docs coming soon
🙌 Who’s It For?

    Engineers building serious LLM apps

    DevOps debugging brittle AI pipelines

    Agents routing AI logic with context

    Anyone tired of praying to the prompt gods

💬 Want More?

Follow progress, ideas, and drop in:
