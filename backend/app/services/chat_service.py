from app.models.chat_models import ChatRequest, ChatResponse
from app.services.retrieval_service import RetrievalService
from app.core.logging import get_logger
from app.services.prompt_service import PromptService
from app.services.llm_service import LLMService
from app.models.chat_models import ChatMessage

class ChatService:
    def __init__(self): 
        self._logger = get_logger(__name__)
        self._retrieval_service = RetrievalService()
        self._prompt_service = PromptService()
        self._llm_service = LLMService()
    
    async def chat(self, request: ChatRequest) -> ChatResponse:
        retrieval_result = self._retrieval_service.retrieve(request.query)

        # Refusal handling
        if not retrieval_result.chunks:
            return ChatResponse(
                request=request,
                response=self._prompt_service.get_refusal_prompt(),
                sources=[]
            )
        
        instructions = self._prompt_service.get_system_instructions()
        user_input = self._prompt_service.build_user_input(request.query, retrieval_result.chunks)

        response_text = await self._llm_service.generate(instructions, user_input)
        response = ChatResponse(
            request=request,
            response=response_text,
            sources=retrieval_result.chunks,
        )
        return response

if __name__ == "__main__":
    chat_service = ChatService()
    request = ChatRequest(query="What is Octavio's full-stack development experience?", history=[])
    response = chat_service.chat(request)
    print(response)