from datetime import date
from typing import Optional
from pydantic import BaseModel, model_validator
from app.models.frontmatter_model import FrontmatterModel

class ChunkMetaData(BaseModel):
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
    id: str 
    content: str
    header_path: list[str]
    document_id: str    # foreign key to the document
    metadata: ChunkMetaData

class EmbeddingChunkModel(ChunkModel):
    embedding: list[float]