from datetime import date
from typing import Optional
from pydantic import BaseModel, ConfigDict
from uuid import UUID

class ChunkMetaData(BaseModel):
    # Common fields
    section: str
    title: str
    last_reviewed: date

    # Experience specific fields
    organization: Optional[str] = None
    employment_type: Optional[str] = None
    # Project specific fields
    status: Optional[str] = None
    links: Optional[dict[str, str]] = None
    # Extra fields
    stack: Optional[list[str]] = None
    skills: Optional[list[str]] = None

class ChunkModel(BaseModel):
    id: Optional[UUID] = None # None for new chunks, UUID for existing chunks
    content: str
    header_path: list[str]
    document_id: Optional[UUID] = None # None for new documents, UUID for existing documents
    chunk_index: int
    metadata: ChunkMetaData

class EmbeddingChunkModel(ChunkModel):
    embedding: list[float]