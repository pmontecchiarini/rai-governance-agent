# 🛡️ AI Governance Orchestrator (v1)

**An automated, multi-agent pipeline designed to integrate responsible AI into the development lifecycle.**

This project demonstrates a **Linear Multi-Agent Workflow** that converts a high-level business idea into a governed technical roadmap and executive risk brief in seconds. By using specialized agents, the system bridges the gap between high-level ethical principles and technical implementation.

---

## Architecture: The 3-Agent Chain

The orchestrator utilizes a decoupled, modular architecture with three distinct agents, each governed by a specific system prompt:

1.  **Agent A: The System Architect**
    * **Function:** Decomposes a business idea into a structured technical specification.
    * **Outputs:** Data Inputs, Model Objectives, Automated Decisions, and Target Audience impact.

2.  **Agent B: The Governance Auditor**
    * **Function:** Performs a "zero-trust" audit against global RAI principles: **Fairness, Reliability, Privacy, Inclusiveness, Transparency, and Accountability.**
    * **Lifecycle Tagging:** Identifies exactly where a risk originates (e.g., Data Collection, Model Training, or Deployment).

3.  **Agent C: The Strategic Reporter**
    * **Function:** Synthesizes technical JSON data into a neutral, non-technical **Executive Responsibility Brief**.
    * **Tone:** Professional and third-person, designed for organizational stakeholders and C-level decision-makers.

---

## Technical Stack

* **Language:** Python 3.13
* **Design Pattern:** Linear Multi-Agent Orchestration
* **LLM:** Gemini 3.1 Flash Lite (Google GenAI SDK)
* **Security:** Environment-based secret management using `python-dotenv`.

---

## Installation & Usage

### 1. Clone the Repository
```bash
git clone [https://github.com/your-username/rai-governance-agent.git](https://github.com/your-username/rai-governance-agent.git)
cd rai-governance-agent