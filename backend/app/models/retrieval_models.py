from app.models.chunk_models import ChunkMetaData, ChunkModel
from pydantic import BaseModel, field_validator
import json

class RetrievalChunk(BaseModel):
    chunk_id: str
    content: str
    header_path: list[str]
    chunk_index: int
    document_id: str
    metadata: ChunkMetaData
    score: float

    @field_validator("metadata", mode="before")
    @classmethod
    def parse_metadata(cls, value) -> ChunkMetaData:
        if isinstance(value, str):
            return json.loads(value)
        return value
    
    @field_validator("header_path", mode="before")
    @classmethod
    def parse_header_path(cls, value) -> list[str]:
        if isinstance(value, str):
            return json.loads(value)
        return value
    
    def to_chunk_model(self) -> ChunkModel:
        return ChunkModel(
            id=self.chunk_id,
            content=self.content,
            header_path=self.header_path,
            chunk_index=self.chunk_index,
            document_id=self.document_id,
            metadata=self.metadata
        )

class RetrievalResult(BaseModel):
    query: str
    chunks: list[RetrievalChunk]
    match_count: int