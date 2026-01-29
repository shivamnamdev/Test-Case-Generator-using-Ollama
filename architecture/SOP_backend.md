# SOP: Backend API (FastAPI)

## 1. Goal
Provide a reliable REST API to bridge the Web Frontend and the Ollama Generator.

## 2. Inputs
- **Endpoint**: `POST /generate`
- **Payload**:
  ```json
  {
      "code_snippet": "string",
      "language": "string (default: python)",
      "framework": "string (default: unittest)"
  }
  ```

## 3. Logic Flow
1. **Receive Request**: Validate JSON payload.
2. **Sanitize**: Ensure input is not empty.
3. **Route**: Call `Generator.generate_test_case(code, language, framework)`.
4. **Respond**: Return JSON with generated code and status.

## 4. Edge Cases
- **Ollama Down**: Return 503 Service Unavailable.
- **Empty Input**: Return 400 Bad Request.
- **Timeouts**: Handle long generation times (set timeout to 60s).
