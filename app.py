from fastapi import FastAPI

from schemas import ChatRequest
from rag.chatbot import ask_question

app = FastAPI()

@app.get("/")
def home():
    return {"message": "RAG Chatbot Running"}

@app.post("/chat")
def chat(request: ChatRequest):
    answer = ask_question(request.question)
    return {"answer": answer}