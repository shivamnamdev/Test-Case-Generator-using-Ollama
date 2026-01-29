import ollama
from typing import List, Dict

class QAChatbot:
    def __init__(self, model="llama3.2"):
        self.model = model
        self.system_prompt = """
You are an expert QA Automation Lead and Test Architect.
Your goal is to help the user create high-quality "Proper Test Cases" and Automation Scripts.

BEHAVIOR:
1. **Chatbot Mode**: You are a conversational assistant, not just a code generator. Remember context.
2. **Clarify First**: If the user provides code/requirements, ask if they want:
   - Manual Test Cases (English texts with scenarios, steps, expected results).
   - Automated Unit Tests (Python/JS code).
3. **Proper Test Cases**: When asked for "Test Cases", defaults to a tabular/structured format:
   - Test Case ID
   - Scenario / Description
   - Pre-conditions
   - Steps
   - Expected Result
   - Type (Positive/Negative/Edge)
4. **Automation**: Only provide code if explicitly asked for "Automation Code" or "Script".

Maintain a professional, premium tone.
"""

    def chat(self, history: List[Dict[str, str]]) -> str:
        """
        history: List of messages [{'role': 'user', 'content': '...'}, {'role': 'assistant', 'content': '...'}]
        """
        # Prepend system prompt to the history for the model call
        messages = [{'role': 'system', 'content': self.system_prompt}] + history
        
        try:
            response = ollama.chat(model=self.model, messages=messages)
            content = response['message']['content']
            return content
        except Exception as e:
            return f"❌ **Error**: {str(e)}"
