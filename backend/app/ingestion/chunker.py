import app.core.logging as logging
from app.models.document_model import DocumentModel
from app.models.chunk_model import ChunkModel
from app.builders.chunk_factory import create_chunks
from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter
from langchain_core.documents import Document as LangchainDocument


logger = logging.get_logger(__name__)

HEADERS_TO_SPLIT_ON = [
    ("#", "h1"),
    ("##", "h2"),
    ("###", "h3"),
    ("####", "h4"),
    ("#####", "h5")
]
CHARACTERS_TO_SPLIT_ON = ["\n\n", "\n", ". ", ".", " ", ""]
ENCODING_NAME = "cl100k_base"


def chunk_document(document: DocumentModel) -> list[ChunkModel]:
    """Chunk a document
    Args:
        document(DocumentModel): The document to chunk
    Returns:
        list[ChunkModel]: The chunks
    """
    split_content = split_markdown_content(document.content)
    chunks = create_chunks(split_content, document)
    return chunks

def split_markdown_content(markdown_content: str) -> list[LangchainDocument]:
    """Split the markdown content into chunks using the MarkdownHeaderTextSplitter and RecursiveCharacterTextSplitter from LangChain

    Args:
        markdown_content(str): The markdown content to split
    Returns:
        list[LangchainDocument]: The split content
    """
    markdown_header_splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=HEADERS_TO_SPLIT_ON,
        strip_headers=False
    )
    recursive_character_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        encoding_name=ENCODING_NAME, 
        chunk_size=300, 
        chunk_overlap= 50, 
        separators=CHARACTERS_TO_SPLIT_ON
    )

    md_header_split_content = markdown_header_splitter.split_text(markdown_content)

    split_content = recursive_character_splitter.split_documents(md_header_split_content)

    return split_content

def chunk_documents(documents: list[DocumentModel]) -> list[ChunkModel]:
    """Chunk a list of documents

    Args:
        documents(list[DocumentModel]): The documents to chunk
    Returns:
        list[ChunkModel]: The chunks
    """
    chunks = []
    for document in documents:
        chunks.extend(chunk_document(document))
    return chunks

# Simple test to check if the chunker is working
# TODO: Remove this test before deploying
if __name__ == "__main__":
    from app.ingestion.document_loader import load_documents
    from pathlib import Path

    document = load_documents(Path("../documents/projects/airise.md"))
    chunks = chunk_document(document)
    for chunk in chunks:
        print(f"ID: {chunk.id}")
        print(f"Content: {chunk.content[:100]}...")
        print(f"Header Path: {chunk.header_path}")
        print("-"*100)
    print(f"FULL LAST CHUNK:\n{chunks[-1]}")