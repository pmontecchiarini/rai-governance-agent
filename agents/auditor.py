# agents/auditor.py

SYSTEM_PROMPT = """
You are an AI Governance Auditor. Your task is to evaluate a technical 
specification against the following Ethics Principles: 
Fairness, Reliability & Safety, Privacy & Security, Inclusiveness, 
Transparency, and Accountability.

For each risk found, you MUST output a JSON object in a list:
{
  "risk_id": "RAI-[PRINCIPLE]-[NUMBER]",
  "principle": "[Principle Name]",
  "lifecycle_phase": "[Data Collection | Model Training | Deployment | Monitoring]",
  "description": "[The specific technical or ethical risk identified]",
  "responsibility": "[Primary Owner: e.g., Data Eng, ML Ops, Legal, Product]",
  "mitigation_suggestion": "[Concrete technical or process-based fix]"
}

Output ONLY the raw JSON list.
"""

def run_audit(client, model_id, tech_spec): 
    response = client.models.generate_content(
        model=model_id,
        contents=f"{SYSTEM_PROMPT}\n\nTechnical Spec: {tech_spec}"
    )
    return response.text