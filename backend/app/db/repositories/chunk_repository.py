from app.db.supabase_client import get_supabase_client
from app.models.chunk_models import EmbeddingChunkModel
from app.core.logging import get_logger
from app.models.retrieval_models import RetrievalChunk
from app.core.config import Settings

class ChunkRepository:

    TABLE_NAME = "chunks"
    EXCLUDE_MODEL_FIELDS = ["metadata"]
    
    def __init__(self):
        self._client = get_supabase_client()
        self._logger = get_logger(__name__)

    def upsert_chunks(self, chunks: list[EmbeddingChunkModel]) -> list[EmbeddingChunkModel]:
        """Upsert a list of chunks

        Args:
            chunks(list[EmbeddingChunkModel]): The chunks to upsert
        Returns:
            list[EmbeddingChunkModel]: The upserted chunks
        """
        try:
            response = self._client.table("chunks").upsert([chunk.model_dump(mode="json", exclude=self.EXCLUDE_MODEL_FIELDS) for chunk in chunks]).execute()
            return [EmbeddingChunkModel(**chunk) for chunk in response.data]
        except Exception as e:
            self._logger.error(f"Error upserting chunks: {e}")
            raise

    def get_chunks_by_document_id(self, document_id: str) -> list[EmbeddingChunkModel]:
        """Get all chunks for a document

        Args:
            document_id(str): The document ID
        Returns:
            list[EmbeddingChunkModel]: The chunks
        """
        try:
            response = self._client.table(self.TABLE_NAME).select("*").eq("document_id", document_id).execute()
            if not response.data:
                self._logger.warning(f"No chunks found for document ID: {document_id}")
                raise ValueError(f"No chunks found for document ID: {document_id}")
            return [EmbeddingChunkModel(**chunk) for chunk in response.data]
        except Exception as e:
            self._logger.error(f"Error getting chunks by document ID: {e}")
            raise

    def get_chunk_by_id(self, id: str) -> EmbeddingChunkModel:
        """Get a chunk by its ID

        Args:
            id(str): The ID of the chunk
        Returns:
            EmbeddingChunkModel: The chunk
        """
        try:
            response = self._client.table(self.TABLE_NAME).select("*").eq("id", id).execute()
            if not response.data:
                self._logger.warning(f"No chunk found for ID: {id}")
                raise ValueError(f"No chunk found for ID: {id}")
            return EmbeddingChunkModel(**response.data[0])
        except Exception as e:
            self._logger.error(f"Error getting chunk by ID: {e}")
            raise

    def delete_chunk_by_id(self, id: str) -> None:
        """Delete a chunk by its ID

        Args:
            id(str): The ID of the chunk
        Returns:
            None
        """
        try:
            self._client.table(self.TABLE_NAME).delete().eq("id", id).execute()
            return None
        except Exception as e:
            self._logger.error(f"Error deleting chunk by ID: {e}")
            raise
    
    def delete_chunks_by_document_id(self, document_id: str) -> None:
        """Delete all chunks for a document

        Args:
            document_id(str): The document ID
        Returns:
            None
        """
        try:
            self._client.table(self.TABLE_NAME).delete().eq("document_id", document_id).execute()
            return None
        except Exception as e:
            self._logger.error(f"Error deleting chunks by document ID: {e}")
            raise
    
    def get_chunks_by_query(self, query_embedding: list[float], match_count: int = 5) -> list[RetrievalChunk]:
        """Get chunks based on an embedded query

        Args:
            query_embedding(list[float]): The embedded query
            match_count(int): The number of chunks to match
        Returns:
            list[RetrievalChunk]: The chunks
        """
        try:
            response = self._client.rpc("match_chunks", {
                "query_embedding": query_embedding,
                "match_count": match_count
            }).execute()
            if not response.data:
                self._logger.warning(f"No chunks found for query embedding: {query_embedding[:5]}...")
                return []
            return [RetrievalChunk.model_validate(chunk) for chunk in response.data if chunk["score"] > Settings().MIN_VECTOR_SIMILARITY_SCORE]
        except Exception as e:
            self._logger.error(f"Error getting chunks by query: {e}")
            raise