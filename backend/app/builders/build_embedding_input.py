from app.models.chunk_models import ChunkModel

def build_embedding_input(chunk: ChunkModel) -> str:
    """Build the embedding input for a chunk
    Args:
        chunk(ChunkModel): The chunk to build the embedding input for
    Returns:
        str: The embedding input
    """
    headers = " > ".join(chunk.header_path)
    keywords = ", ".join(chunk.metadata.stack) if chunk.metadata.stack else "None"
    keywords += ", " + ", ".join(chunk.metadata.skills) if chunk.metadata.skills else "None"
    return f"{headers}\n\n{keywords}\n\n{chunk.content}".strip()

# Test the build_embedding_input function
if __name__ == "__main__":
    from app.ingestion.chunker import chunk_document
    from app.ingestion.document_loader import load_documents
    from pathlib import Path
    document = load_documents(Path("../documents/projects/airise.md"))
    frontmatter, markdown_content = document
    chunks = chunk_document((frontmatter, markdown_content))
    for chunk in chunks:
        print(build_embedding_input(chunk))
        print("-"*100)
    