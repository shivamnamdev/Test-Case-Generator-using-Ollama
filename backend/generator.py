import ollama

class TestGenerator:
    def __init__(self, model="llama3.2"):
        self.model = model

    def generate(self, code: str, language: str = "python", framework: str = "unittest") -> str:
        prompt = f"""
You are an expert QA Automation Engineer.
Your task is to write comprehensive unit tests for the following {language} code using the {framework} framework.

RULES:
1. Return ONLY the code. No markdown formatting (no ``` syntax), no explanations, no chat.
2. Include positive cases, negative cases, and edge cases.
3. Ensure the code is runnable (include imports).
4. If the input code is invalid or empty, return a comment explaining why.

INPUT CODE:
{code}
        """
        
        try:
            response = ollama.chat(model=self.model, messages=[
                {'role': 'user', 'content': prompt},
            ])
            content = response['message']['content']
            
            # Clean up if model breaks rule 1 slightly
            content = content.replace("```python", "").replace("```", "").strip()
            return content
            
        except Exception as e:
            return f"# Error generating tests: {str(e)}"
