
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import List
import traceback

from app.orchestrator.router import route_query

router = APIRouter()


class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1)


class ChatResponse(BaseModel):
    intent: str
    answer: str
    sources: List[str] = []


@router.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):

    try:
        message = request.message.strip()

        if not message:
            raise HTTPException(
                status_code=400,
                detail="Message cannot be empty."
            )

        result = route_query(message)

        return ChatResponse(
            intent=result["intent"],
            answer=result["answer"],
            sources=result.get("sources", [])
        )

    except HTTPException:
        raise

    except Exception as error:

        print("\n========== CHAT API ERROR ==========")
        print("ERROR:", repr(error))
        print("ERROR TYPE:", type(error).__name__)
        print("STATUS:", getattr(error, "status_code", None))
        print("BODY:", getattr(error, "body", None))
        traceback.print_exc()
        print("====================================\n")

        raise HTTPException(
            status_code=500,
            detail="Internal error while processing your message."
        )
