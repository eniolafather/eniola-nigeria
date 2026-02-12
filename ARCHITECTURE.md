# ARCHITECTURE.md

## Eniola Agent Rebuild

This file documents the core architecture for the newly built Eniola agent.

### Components
1.  **`bot.py`**: Contains the primary execution logic, including the agent's decision-making loop and tool orchestration capabilities.
2.  **`eniola_agent.json`**: The configuration file defining the agent's metadata, name, role, and the specific tools it has access to (per policy).
3.  **`MEMORY.md`**: Long-term memory store for distilled context and critical lessons.

### Workflow
The agent initializes by loading `eniola_agent.json`, then enters a loop to process user input, leveraging the defined tools to interact with the environment. The repository state is kept clean and up-to-date via scheduled commits.
