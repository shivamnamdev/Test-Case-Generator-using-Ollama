# Project Constitution (Gemini)

## 1. Data Schemas

### Input Payload (CLI/Function Call)
```json
{
  "source_code": "string",  // The code to generate tests for
  "language": "string",     // e.g., 'python', 'javascript'
  "framework": "string"     // e.g., 'pytest', 'jest', 'unittest'
}
```

### Output Payload (Generator Result)
```json
{
  "test_code": "string",      // The complete executable test code
  "filename": "string",       // Suggested filename (e.g., test_utils.py)
  "explanation": "string"     // Brief explanation of coverage
}
```

## 2. Behavioral Rules
- **Model**: Use `llama3.2` via Ollama.
- **Templating**: MUST use a strictly defined system prompt/template stored in the codebase.
- **Determinism**: Output should be code-only or structured JSON where possible to avoid parsing issues.
- **Protocol**: Follow BLAST.

## 3. Architectural Invariants
- **Protocol**: BLAST
- **Core**: HTML/JS Client <-> Python API (FastAPI) <-> Ollama Wrapper
- **Design**: Premium, responsive, glassmorphism UI.


