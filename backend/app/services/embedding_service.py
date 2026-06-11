from openai import OpenAI
from app.core.config import Settings
from app.core.logging import get_logger
from app.models.chunk_models import ChunkModel, EmbeddingChunkModel
from app.builders.build_embedding_input import build_embedding_input

logger = get_logger(__name__)

# Example return format from OpenAI embeddings.create
# {
#   "object": "list",
#   "data": [
#     {
#       "object": "embedding",
#       "index": 0,
#       "embedding": [
#         -0.006929283495992422, -0.005336422007530928, -4.547132266452536e-5,
#         -0.024047505110502243
#       ]
#     }
#   ],
#   "model": "text-embedding-3-small",
#   "usage": {
#     "prompt_tokens": 5,
#     "total_tokens": 5
#   }
# }

class EmbeddingService:
    def __init__(self):
        """Initialize the embedding service
        """
        self.openai = OpenAI(api_key=Settings().OPENAI_API_KEY)
        self.model = Settings().EMBEDDING_MODEL

    def embed_text(self, text: str) -> list[float]:
        """Embed a string of text
        
        Args:
            text(str): The text to embed
        Returns:
            list[float]: The embedding of the text
        """
        embedding = self.openai.embeddings.create(
            input=text,
            model=self.model,
            encoding_format="float"
        )
        return embedding.data[0].embedding
    
    def embed_chunks(self, chunks: list[ChunkModel]) -> list[EmbeddingChunkModel]:
        """Embed a list of chunks

        Args:
            chunks(list[ChunkModel]): The chunks to embed
        Returns:
            list[EmbeddingChunkModel]: The list of embedded chunks
        """
        inputs = [build_embedding_input(chunk) for chunk in chunks]
        response = self.openai.embeddings.create(
            input=inputs,
            model=self.model,
            encoding_format="float"
        )
        
        embeddings = []
        for chunk, data in zip(chunks, response.data):
            embeddings.append(EmbeddingChunkModel(
                **chunk.model_dump(),
                embedding=data.embedding
            ))
        return embeddings

# Test the embedding service
if __name__ == "__main__":
    from app.ingestion.chunker import chunk_document
    from app.ingestion.document_loader import load_documents
    from pathlib import Path
    document = load_documents(Path("../documents/projects/airise.md"))
    frontmatter, markdown_content = document
    chunks = chunk_document((frontmatter, markdown_content))
    embedding_service = EmbeddingService()
    embedded_chunks = embedding_service.embed_chunks(chunks)
    for chunk in embedded_chunks:
        print(chunk.embedding)
        print("-"*100)