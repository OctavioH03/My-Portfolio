from app.db.supabase_client import get_supabase_client
from app.models.chunk_model import EmbeddingChunkModel
from app.core.logging import get_logger
from uuid import UUID

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

    def get_chunks_by_document_id(self, document_id: UUID) -> list[EmbeddingChunkModel]:
        """Get all chunks for a document

        Args:
            document_id(UUID): The document ID
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

    def get_chunk_by_id(self, id: UUID) -> EmbeddingChunkModel:
        """Get a chunk by its ID

        Args:
            id(UUID): The ID of the chunk
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

    def delete_chunk_by_id(self, id: UUID) -> None:
        """Delete a chunk by its ID

        Args:
            id(UUID): The ID of the chunk
        Returns:
            None
        """
        try:
            self._client.table(self.TABLE_NAME).delete().eq("id", id).execute()
            return None
        except Exception as e:
            self._logger.error(f"Error deleting chunk by ID: {e}")
            raise
    
    def delete_chunks_by_document_id(self, document_id: UUID) -> None:
        """Delete all chunks for a document

        Args:
            document_id(UUID): The document ID
        Returns:
            None
        """
        try:
            self._client.table(self.TABLE_NAME).delete().eq("document_id", document_id).execute()
            return None
        except Exception as e:
            self._logger.error(f"Error deleting chunks by document ID: {e}")
            raise