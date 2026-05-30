from app.ingestion.document_loader import load_documents_from_directory
from pathlib import Path


def run_ingestion() -> None:
    # Load the documents
    documents = load_documents_from_directory(Path("../documents"), exclude=["README.md", "goals.md"]) # temporary exclusion for goals.md until it is completed
    for document in documents:
        frontmatter, markdown_content = document
        print(frontmatter.id)
    # Chunk the documents


if __name__ == "__main__":
    run_ingestion()