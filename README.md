## YAJPH: The Anti-Black-Box Engine

# "Every 'no' comes with a roadmap to 'yes'"

🔍 Why Transparency Matters

In an AI-driven world, opaque decisions cost you:

    Trust when users can't understand rejections

    Time debugging mysterious failures

    Money when bad logic goes undetected

YAJPH solves this by making every decision:
✅ Explainable - Know exactly why something failed
✅ Actionable - Get specific improvement steps
✅ Auditable - Full trace of all rule checks
⚡ How It Works

    Define rules in simple YAML:

yaml

    # loan_rules.yaml
    requirements:
      credit_score: 620  # Minimum score
      dti: "36%"        # Max debt-to-income
    must_have: 
      - employment_status

Get clear JSON decisions:

json

    {
      "passed": false,
      "reason": "DTI too high",
      "your_score": "42%",
      "threshold": "36%",
      "fix": "Reduce debt-to-income ratio",
      "audit_trail": [
        "Checked credit_score: 650 (passed)",
        "Checked dti: 42% (failed)"
      ]
    }

🚀 Key Features
Feature	Benefit
🚦 Rule-based routing	Enforce business logic consistently
📝 Self-documenting rejects	Every "no" explains why + how to fix
🔍 Full audit trails	Compliance-ready decision logs
🛠 CLI + Python APIs	Fits any workflow
💡 Why YAJPH is Different

    Clear YAML rules → Humans and machines can read them

    No silent failures → Every rejection includes:

        Exact failure point

        Current vs required values

        Actionable fixes

    Hybrid-ready → Works with LLMs or traditional systems

    DevOps-friendly → Batch process files via CLI

🛠️ Get Started
bash

    pip install yajph
    yajph --rules loan_rules.yaml --input applicant.json

or in Python:
python

    from yajph import Router
    router = Router('loan_rules.yaml')
    decision = router.evaluate(applicant_data)
    print(decision.fix)  # "Reduce debt-to-income ratio"

🌟 Perfect For Developers Who Need To:

    Give constructive rejections in apps

    Maintain compliance trails for auditors

    Build stable rules that outlive LLM hype cycles

Because in production, "why?" matters as much as "what?"
