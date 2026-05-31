from app.models.chunk_model import ChunkModel
from app.models.frontmatter_model import FrontmatterModel
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

def create_chunk(chunk_index: int, content: str, header_path: list[str], frontmatter: FrontmatterModel) -> ChunkModel:
    """Create a chunk model
    Args:
        chunk_index(int): The index of the chunk
        content(str): The content of the chunk
        header_path(list[str]): The header path of the chunk
        frontmatter(FrontmatterModel): The frontmatter model to create the chunk for
    Returns:
        ChunkModel: The chunk model
    """
    metadata = build_metadata(frontmatter)
    return ChunkModel(
        id=f"{frontmatter.id}-{header_path[-1].lower()}-{chunk_index:04d}",
        content=content,
        header_path=header_path,
        document_id=frontmatter.id,
        metadata=metadata
    )

def create_chunks(split_content: list[LangchainDocument], frontmatter: FrontmatterModel) -> list[ChunkModel]:
    """Create a list of chunk models
    Args:
        split_content(list[tuple[list[str], str]]): The split content with each index containing the header path and the content for the chunk
        frontmatter(FrontmatterModel): The frontmatter model to create the chunks for
    Returns:
        list[ChunkModel]: The list of chunk models
    Notes:
        - The chunk index is used to create a unique id for the chunk
        - The last header in the header path is used to create a unique id for the chunk
        - The document id is used to create a unique id for the chunk
        - The metadata is used to create the chunk model
    """
    chunks = []
    for chunk_index, document in enumerate(split_content):
        header_path = _build_header_path(document.metadata)
        chunks.append(create_chunk(
            chunk_index=chunk_index,
            content=document.page_content,
            header_path=header_path,
            frontmatter=frontmatter
        ))
    return chunks
