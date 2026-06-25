from fastapi import APIRouter, HTTPException, Depends, status
from app.models.chat_models import ChatRequest, ChatResponse
from app.services.chat_service import ChatService

router = APIRouter()

def get_chat_service() -> ChatService:
    return ChatService()

@router.post("/", response_model=ChatResponse, status_code=status.HTTP_200_OK)
async def chat(request: ChatRequest, chat_service: ChatService = Depends(get_chat_service)) -> ChatResponse:
    """Answer a question from the user using the AI Chat Service"""
    try: 
        response = await chat_service.chat(request)
        return response
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))