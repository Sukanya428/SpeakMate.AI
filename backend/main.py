from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from chatbot import get_response

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
class ChatRequest(BaseModel):
    message:str

@app.post("/chat")
def chat(data: ChatRequest):
    reply=get_response(data.message)
    return {"reply":reply}

