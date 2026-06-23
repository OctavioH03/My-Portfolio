from app.ingestion.document_loader import load_documents_from_directory
from app.ingestion.chunker import chunk_documents
from app.services.ingestion_service import IngestionService
from pathlib import Path


def run_ingestion() -> None:
    # Load the documents
    documents = load_documents_from_directory(Path("../documents"), exclude=["README.md", "goals.md"]) # temporary exclusion for goals.md until it is completed
    
    # Chunk the documents
    documents_to_chunks = chunk_documents(documents)

    # Ingest the documents and chunks: upserts the documents and chunks into the database
    ingestion_service = IngestionService()
    ingestion_service.ingest_chunked_documents(documents_to_chunks)

if __name__ == "__main__":
    run_ingestion()