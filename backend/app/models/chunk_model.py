from datetime import date
from typing import Optional
from pydantic import BaseModel, ConfigDict, field_validator
from uuid import UUID
import json

class ChunkMetaData(BaseModel):
    model_config = ConfigDict(extra="ignore")
    # Common fields
    section: str
    title: str
    last_reviewed: date
    source_path: str
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
    document_id: str
    chunk_index: int
    metadata: Optional[ChunkMetaData] = None
    @field_validator("header_path", mode="before")
    @classmethod
    def parse_header_path(cls, value: str) -> list[str]:
        if isinstance(value, str):
            return json.loads(value)
        return value

class EmbeddingChunkModel(ChunkModel):
    embedding: list[float]

    @field_validator("embedding", mode="before")
    @classmethod
    def parse_embedding(cls, value: str) -> list[float]:
        if isinstance(value, str):
            return json.loads(value)
        return value