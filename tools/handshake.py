import ollama
import sys

def check_connection():
    print("🔄 Checking Ollama connection...")
    try:
        # Check if the model exists
        models = ollama.list()
        print(f"Debug Raw Models: {models}")
        # ollama.list returns a dict with 'models' key which is a list of objects
        model_names = [m['model'] for m in models['models']] # 'model' might be the key instead of 'name'
        
        target_model = "llama3.2:latest"
        if target_model not in model_names:
            print(f"⚠️  Model '{target_model}' not found in list: {model_names}")
            print("Attempting to use generic 'llama3.2'...")
            # Sometimes tags vary, strict check might fail if user pulled differently
        
        print(f"✅ Ollama is reachable. Found {len(model_names)} models.")
        
        print(f"🧪 Sending test prompt to '{target_model}'...")
        response = ollama.chat(model='llama3.2', messages=[
          {
            'role': 'user',
            'content': 'Say "Hello, BLAST Protocol!" if you can hear me.',
          },
        ])
        
        content = response['message']['content']
        print(f"🤖 Response: {content}")
        
        if "BLAST Protocol" in content:
            print("✅ Handshake Successful!")
            return True
        else:
            print("⚠️  Response received but content unexpected.")
            return True # Still technically a success connection-wise

    except Exception as e:
        print(f"❌ Connection Failed: {e}")
        return False

if __name__ == "__main__":
    success = check_connection()
    sys.exit(0 if success else 1)
