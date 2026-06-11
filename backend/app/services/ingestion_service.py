from app.db.repositories.document_repository import DocumentRepository
from app.db.repositories.chunk_repository import ChunkRepository
from app.services.embedding_service import EmbeddingService
from app.core.logging import get_logger
from app.models.document_models import DocumentModel
from app.models.chunk_models import ChunkMetaData, ChunkModel, EmbeddingChunkModel

class IngestionService:

    def __init__(self):
        self._documents_repository = DocumentRepository()
        self._chunks_repository = ChunkRepository()
        self._embedding_service = EmbeddingService()
        self._logger = get_logger(__name__)
    
    def ingest_chunked_document(self, document_to_chunks: tuple[DocumentModel, list[ChunkModel]]) -> tuple[DocumentModel, list[EmbeddingChunkModel]]:
        try:
            document, chunks = document_to_chunks
            upserted_document = self._documents_repository.upsert_document(document)
            # Use the document ID to upsert the chunks
            for chunk in chunks:
                chunk.document_id = upserted_document.id
            embedded_chunks = self._embedding_service.embed_chunks(chunks)
            upserted_chunks = self._chunks_repository.upsert_chunks(embedded_chunks)
            # for chunk in upserted_chunks:
            #     chunk.metadata = ChunkMetaData(**document.model_dump())
            return (upserted_document, upserted_chunks)
        except Exception as e:
            self._logger.error(f"Error ingesting chunked documents: {e}")
            raise
    
    def ingest_chunked_documents(self, documents_to_chunks: list[tuple[DocumentModel, list[ChunkModel]]]) -> list[tuple[DocumentModel, list[EmbeddingChunkModel]]]:
        """Ingest a list of chunked documents
        
        Args:
            documents_to_chunks(list[tuple[DocumentModel, list[ChunkModel]]]): The documents to chunks mapping
        Returns:
            list[tuple[DocumentModel, list[EmbeddingChunkModel]]]: The ingested documents and chunks
        """
        return [self.ingest_chunked_document(document_to_chunks) for document_to_chunks in documents_to_chunks]