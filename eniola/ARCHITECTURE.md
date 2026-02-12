# ARCHITECTURE.md - Finalized Architecture
This file outlines the structure for the ENIOLA Agent rebuild.

## Core Components
1.  **Entry Point**: Must be structured around running `eniola_agent.json`.
2.  **Routing Logic**: Must contain the latest conversational LLM routing logic.
3.  **Data Schemas**: Defined in `database_schema.sql`.
4.  **Worker Definitions**: Onboarding prompts are in `prompts/worker_onboarding.txt`.