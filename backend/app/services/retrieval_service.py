from app.services.embedding_service import EmbeddingService
from app.db.repositories.chunk_repository import ChunkRepository
from app.core.logging import get_logger
from app.models.retrieval_models import RetrievalResult
import re
from app.core.config import Settings
from app.services.rerank_service import RerankService

class RetrievalService:
    def __init__(self):
        self._embedding_service = EmbeddingService()
        self._rerank_service = RerankService()
        self._chunks_repository = ChunkRepository()
        self._logger = get_logger(__name__)

    def retrieve(self, query: str) -> RetrievalResult:
        # Rewrite the query to improve the retrieval results
        query = self._rewrite_query(query)
        self._logger.info(f"Rewritten query: {query}")

        query_embedding = self._embedding_service.embed_text(query)

        # Retrieve the chunks from the database
        chunks = self._chunks_repository.get_chunks_by_query(query_embedding, Settings().RETRIEVAL_TOP_K)
        self._logger.info(
            "Retrieved %s chunks for query (top similarity: %s)",
            len(chunks),
            chunks[0].similarity if chunks else 0
        )
        if not chunks:
            self._logger.warning("No chunks found for query: %s", query)
            return RetrievalResult(
                query=query,
                chunks=[],
                match_count=0
            )

        # Rerank the chunks to improve the retrieval results
        reranked_chunks = self._rerank_service.rerank(query, chunks)
        self._logger.info(
            "Reranked %s chunks for query (top similarity: %s)",
            len(reranked_chunks),
            reranked_chunks[0].similarity if reranked_chunks else 0
        )
        
        return RetrievalResult(
            query=query,
            chunks=reranked_chunks,
            match_count=len(chunks)
        )
    
    def _rewrite_query(self, query: str) -> str:
        """Rewrite the query to improve the retrieval results

        Args:
            query(str): The query to rewrite
        Returns:
            str: The rewritten query
        """
        rewritten_query = query.strip()
        rewritten_query = re.sub(r"\b(you|yourself)\b", "Octavio", rewritten_query, flags=re.IGNORECASE)
        rewritten_query = re.sub(r"\b(your|his)\b", "Octavio's", rewritten_query, flags=re.IGNORECASE)
        # TODO: Implement context rewriting logic here
        return rewritten_query

# Test the retrieval service
if __name__ == "__main__":
    retrieval_service = RetrievalService()
    result = retrieval_service.retrieve("What experience do you have with full-stack development?")
    print(f"Query: {result.query}")
    print("-"*100)
    for chunk in result.chunks:
        print(chunk.content)
        print(f"Similarity: {chunk.similarity}")
        print("-"*100)