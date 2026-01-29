# Findings
## Research & Discoveries

- **Project**: Local LLM Test Case Generator
- **Tech Stack**: Ollama (specified by user)

## Constraints
- Local execution via Ollama.
- Must follow BLAST protocol.

## Research Findings (Phase 1)
- **Ollama Setup**: Requires running Ollama server (`ollama serve`) and pulling a model (e.g., `llama3`, `codellama`).
- **Python Integration**: Use `ollama` python library.
- **Workflow**: 
    1. Connect to local API (default `http://localhost:11434`).
    2. Send prompt with context/code.
    3. Receive generated test cases.

