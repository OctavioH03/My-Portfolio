from app.services.embedding_service import EmbeddingService
from app.models.chunk_model import ChunkModel, EmbeddingChunkModel
from app.core.logging import get_logger

logger = get_logger(__name__)

class Embedder:
    def __init__(self):
        """Initialize the embedder
        """
        self.embedding_service = EmbeddingService()

    def embed_chunks(self, chunks: list[ChunkModel]) -> list[EmbeddingChunkModel]:
        """Embed a list of chunks
        Args:
            chunks(list[ChunkModel]): The chunks to embed
        Returns:
            list[EmbeddingChunkModel]: The list of embedded chunks
        """
        return self.embedding_service.embed_chunks(chunks)