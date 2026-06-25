from app.core.logging import get_logger
from app.core.config import Settings
from openai import OpenAI

# Example response from OpenAI responses.create
# https://developers.openai.com/api/reference/python/resources/responses/methods/create

class LLMService:
    def __init__(self):
        self._logger = get_logger(__name__)
        self._llm_client = OpenAI(api_key=Settings().OPENAI_API_KEY)
        self._chat_model = Settings().CHAT_MODEL
    
    async def generate(self, instructions: str, input: str) -> str:
        try:
            response = self._llm_client.responses.create(
                model=self._chat_model,
                instructions=instructions,
                input=input
            )
            return response.output_text
        except Exception as e:
            self._logger.error(f"Error generating response: {e}")
            raise
