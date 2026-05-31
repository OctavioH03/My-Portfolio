import app.core.logging as logging
from app.models.frontmatter_model import FrontmatterModel
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


def chunk_document(document: tuple[FrontmatterModel, str]) -> list[str]:
    frontmatter, markdown_content = document
    split_content = split_markdown_content(markdown_content)
    chunks = create_chunks(split_content, frontmatter)
    return chunks

def split_markdown_content(markdown_content: str) -> list[LangchainDocument]:
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