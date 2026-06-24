from app.core.logging import get_logger
from app.prompts.prompts import SystemPrompt, RefusalPrompt
from app.models.retrieval_models import RetrievalChunk

class PromptService:
    def __init__(self):
        self._logger = get_logger(__name__)
        self._system_prompt = SystemPrompt()
        self._refusal_prompt = RefusalPrompt()
    
    def get_system_instructions(self) -> str:
        """ Get the system instructions for the chat model
        
        Returns:
            str: The system instructions
        """
        return f"{self._system_prompt}"
    
    def get_refusal_prompt(self) -> str:
        """ Get the refusal prompt for the chat model
        
        Returns:
            str: The refusal prompt
        """
        return f"{self._refusal_prompt}"
    
    def build_user_input(self, query: str, chunks: list[RetrievalChunk]) -> str:
        """ Build the user input for the chat model
        
        Args:
            query(str): The query to build the user input for
            chunks(list[RetrievalChunk]): The context chunks to build the user input for
        Returns:
            str: The user input
        """
        context = self._build_context(chunks)
        return f"User: {query}\n\nContext: {context}"


    def _build_context(self, chunks: list[RetrievalChunk]) -> str:
        """ Build the context based on the chunksfor the chat model
        
        Args:
            chunks(list[RetrievalChunk]): The context chunks to build the context for
        Returns:
            str: The context
        """
        context = ""
        for index, chunk in enumerate(chunks):
            document = chunk.document_id
            headers = ">".join(chunk.header_path)
            context += f"[Source {index+1}] {document} > {headers}\n{chunk.content}\n\n"
        return context