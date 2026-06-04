from app.models.chunk_model import ChunkModel
from app.models.document_model import DocumentModel
from app.builders.build_metadata import build_metadata
from langchain_core.documents import Document as LangchainDocument



def _build_header_path(metadata: dict) -> list[str]:
    """Build the header path from the metadata given by LangChain's MarkdownHeaderTextSplitter
    Args:
        metadata(dict): The metadata given by LangChain's MarkdownHeaderTextSplitter
    Returns:
        list[str]: The header path
    """
    header_path = [value for key, value in sorted(metadata.items())]
    return header_path

def create_chunk(chunk_index: int, content: str, header_path: list[str], document: DocumentModel) -> ChunkModel:
    """Create a chunk model
    Args:
        chunk_index(int): The index of the chunk
        content(str): The content of the chunk
        header_path(list[str]): The header path of the chunk
        document(DocumentModel): The document to create the chunk for
    Returns:
        ChunkModel: The chunk model
    """
    metadata = build_metadata(document)
    return ChunkModel(
        content=content,
        header_path=header_path,
        document_id=document.id,
        chunk_index=chunk_index,
        metadata=metadata
    )

def create_chunks(split_content: list[LangchainDocument], document: DocumentModel) -> list[ChunkModel]:
    """Create a list of chunk models
    
    Args:
        split_content(list[LangchainDocument]): The split content to create the chunks for
        document(DocumentModel): The document to create the chunks for
    Returns:
        list[ChunkModel]: The list of chunk models
    """
    chunks = []
    for chunk_index, chunk_data in enumerate(split_content):
        header_path = _build_header_path(chunk_data.metadata)
        chunks.append(create_chunk(
            chunk_index=chunk_index,
            content=chunk_data.page_content,
            header_path=header_path,
            document=document
        ))
    return chunks
