from app.ingestion.document_loader import load_documents_from_directory
from app.ingestion.chunker import chunk_documents
from app.services.embedding_service import EmbeddingService
from pathlib import Path


def run_ingestion() -> None:
    # Load the documents
    documents = load_documents_from_directory(Path("../documents"), exclude=["README.md", "goals.md"]) # temporary exclusion for goals.md until it is completed
    
    # Chunk the documents
    chunks = chunk_documents(documents)

    # Embed the chunks
    embedding_service = EmbeddingService()
    embedded_chunks = embedding_service.embed_chunks(chunks)

    # Store the chunks in the database
    #upsert_chunks(embedded_chunks)

if __name__ == "__main__":
    run_ingestion()