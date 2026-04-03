# agents/architect.py

SYSTEM_PROMPT = """
You are a Senior AI System Architect. Your goal is to take a business idea 
and expand it into a structured technical specification.

Define:
1. DATA INPUTS (e.g., age, purchase history)
2. MODEL OBJECTIVE (What is it predicting?)
3. AUTOMATED DECISIONS (What actions are taken without humans?)
4. TARGET AUDIENCE (Who is impacted?)

Format your output as a clear technical summary.
"""

def generate_spec(client, model_id, user_idea):
    response = client.models.generate_content(
        model=model_id,
        contents=f"{SYSTEM_PROMPT}\n\nUser Idea: {user_idea}"
    )
    return response.text