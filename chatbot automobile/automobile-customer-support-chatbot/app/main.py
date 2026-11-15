
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse

from app.api.chat import router as chat_router


app = FastAPI(
    title="Automobile Customer Support Chatbot",
    description=(
        "AI-powered automobile customer support chatbot "
        "using LangChain, RAG and Intent Recognition."
    ),
    version="1.0.0"
)

app.include_router(chat_router)

FRONTEND_FILE = (
    Path(__file__).resolve().parent / "static" / "index.html"
)


@app.get("/")
def home():
    if FRONTEND_FILE.exists():
        return FileResponse(FRONTEND_FILE)

    return {
        "message": "Automobile Customer Support Chatbot API is running.",
        "documentation": "/docs"
    }


@app.get("/health")
def health():
    return {
        "status": "running",
        "application": "Automobile Customer Support Chatbot"
    }
