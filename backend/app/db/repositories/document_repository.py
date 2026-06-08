from app.db.supabase_client import get_supabase_client
from app.models.document_model import DocumentModel
from app.core.logging import get_logger
from uuid import UUID

class DocumentRepository:
    TABLE_NAME = "documents"
    EXCLUDE_MODEL_FIELDS = ["summary", "date_end", "date_start", "location"]

    def __init__(self):
        self._client = get_supabase_client()
        self._logger = get_logger(__name__)

    def upsert_documents(self, documents: list[DocumentModel]) -> list[DocumentModel]:
        """Upsert a list of documents

        Args:
            documents(list[DocumentModel]): The documents to upsert
        Returns:
            list[DocumentModel]: The upserted documents
        """
        try:
            response = self._client.table(self.TABLE_NAME).upsert([document.model_dump(mode="json", exclude=self.EXCLUDE_MODEL_FIELDS) for document in documents]).execute()
            return [DocumentModel(**document) for document in response.data]
        except Exception as e:
            self._logger.error(f"Error upserting documents: {e}")
            raise
    
    def upsert_document(self, document: DocumentModel) -> DocumentModel:
        """Upsert a document

        Args:
            document(DocumentModel): The document to upsert
        Returns:
            DocumentModel: The upserted document
        """
        try:
            response = self._client.table(self.TABLE_NAME).upsert([document.model_dump(mode="json", exclude=self.EXCLUDE_MODEL_FIELDS)]).execute()
            return DocumentModel(**response.data[0])
        except Exception as e:
            self._logger.error(f"Error upserting document: {e}")
            raise

    def get_document_by_id(self, id: UUID) -> DocumentModel:
        """Get a document by its ID

        Args:
            id(UUID): The ID of the document
        Returns:
            DocumentModel: The document
        """
        try:
            response = self._client.table(self.TABLE_NAME).select("*").eq("id", id).execute()
            return DocumentModel(**response.data[0])
        except Exception as e:
            self._logger.error(f"Error getting document by ID: {e}")
            raise
    
    def get_documents(self) -> list[DocumentModel]:
        """Get all documents

        Returns:
            list[DocumentModel]: The documents
        """
        try:
            response = self._client.table(self.TABLE_NAME).select("*").execute()
            if not response.data:
                self._logger.warning(f"No documents found")
                raise ValueError(f"No documents found")
            return [DocumentModel(**document) for document in response.data]
        except Exception as e:
            self._logger.error(f"Error getting documents: {e}")
            raise
    
    def get_documents_by_section(self, section: str) -> list[DocumentModel]:
        """Get all documents in a section

        Args:
            section(str): The section of the documents
        Returns:
            list[DocumentModel]: The documents
        """
        try:
            response = self._client.table(self.TABLE_NAME).select("*").eq("section", section).execute()
            if not response.data:
                self._logger.warning(f"No documents found for section: {section}")
                raise ValueError(f"No documents found for section: {section}")
            return [DocumentModel(**document) for document in response.data]
        except Exception as e:
            self._logger.error(f"Error getting documents by section: {e}")
            raise    

    def delete_document_by_id(self, id: UUID) -> None:
        """Delete a document by its ID

        Args:
            id(UUID): The ID of the document
        Returns:
            None
        """
        try:
            self._client.table(self.TABLE_NAME).delete().eq("id", id).execute()
            return None
        except Exception as e:
            self._logger.error(f"Error deleting document by ID: {e}")
            raise
