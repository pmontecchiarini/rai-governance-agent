import os
from google import genai
from dotenv import load_dotenv

# Import agents
from agents.architect import generate_spec
from agents.auditor import run_audit
from agents.reporter import generate_brief

load_dotenv()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
model_id = 'gemini-3.1-flash-lite-preview'

def main():
    print("--- 🛡️ Responsible AI Governance Orchestrator ---")
    
    # Get dynamic input from the terminal
    user_input = input("\n💡 Enter your AI business idea: ")
    
    if not user_input.strip():
        print("❌ No input provided. Exiting.")
        return
    
    # Step 1: Architect
    print("🚀 Architecting system...")
    spec = generate_spec(client, model_id, user_input)
    print(f"\n--- Technical Spec ---\n{spec}")
    
    # Step 2: Auditor
    print("\n🔍 Auditing for Responsible AI risks...")
    json_report = run_audit(client, model_id, spec)
    print(f"\n--- RAI JSON Report ---\n{json_report}")

    # Chain 3: Brief (Needs JSON)
    executive_brief = generate_brief(client, model_id, json_report)

    print(f"--- FINAL EXECUTIVE BRIEF ---\n{executive_brief}")

if __name__ == "__main__":
    main()