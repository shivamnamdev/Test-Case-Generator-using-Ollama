# SOP: Generator Logic (Ollama)

## 1. Goal
Generate deterministic, high-quality test cases using the local Llama 3.2 model.

## 2. Inputs
- `code_snippet` (str)
- `language` (str)
- `framework` (str)

## 3. System Prompt Strategy
The system prompt must enforce:
1. **Role**: Senior QA Automation Engineer.
2. **Format**: Return ONLY the code, or valid JSON containing the code.
3. **Coverage**: Positive, negative, and edge cases.

## 4. Tool Logic
1. **Construct Prompt**:
   ```text
   System: You are an expert QA. Write {framework} tests for {language}. Output ONLY code.
   User: {code_snippet}
   ```
2. **Call Ollama**: `ollama.chat(model='llama3.2', messages=[...])`
3. **Post-Process**:
   - Strip Markdown backticks (```python ... ```).
   - Verify non-empty output.

## 5. Error Handling
- Use `try/except` for Ollama connection errors.
- Retry once on empty response.
