from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from backend.chatbot import QAChatbot
from typing import List, Dict

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

bot = QAChatbot()

# In-memory session (for simplicity in this local tool, we'll trust the client to send history or keep it simple)
# For a robust app, we'd store session IDs. 
# Here, we will accept the full history from the frontend to keep the backend stateless.

class ChatMessage(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    history: List[ChatMessage]

class ChatResponse(BaseModel):
    response: str

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    if not request.history:
        raise HTTPException(status_code=400, detail="History cannot be empty")
    
    # Convert Pydantic models to dicts
    history_dicts = [{"role": msg.role, "content": msg.content} for msg in request.history]
    
    response_text = bot.chat(history_dicts)
    return {"response": response_text}

@app.get("/health")
async def health_check():
    return {"status": "ok"}
