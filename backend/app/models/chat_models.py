from app.models.retrieval_models import RetrievalChunk
from pydantic import BaseModel
from typing import Literal

class ChatMessage(BaseModel):
    role: Literal["user", "assistant", "system"]
    content: str

class ChatRequest(BaseModel):
    query: str
    history: list[ChatMessage]

class ChatResponse(BaseModel):
    request: ChatRequest
    response: str
    sources: list[RetrievalChunk]