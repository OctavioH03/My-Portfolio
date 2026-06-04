from datetime import date
from pydantic import BaseModel, Field
from typing import Literal, Optional
from app.models.flexible_date_model import FlexibleDate
from uuid import UUID

class BaseDocumentModel(BaseModel):
    id: Optional[UUID] = None # None for new documents, UUID for existing documents
    title: str
    section: str
    content: str
    last_reviewed: date
    tags: list[str] = Field(default_factory=list)
    related: list[str] = Field(default_factory=list)
    summary: Optional[str] = None

class ExperienceDocumentModel(BaseDocumentModel):
    section: Literal["experience"]
    organization: str
    employment_type: str
    location: str
    date_start: FlexibleDate
    date_end: FlexibleDate
    stack: list[str] = Field(default_factory=list)
    skills: list[str] = Field(default_factory=list)

class ProjectDocumentModel(BaseDocumentModel):
    section: Literal["project"]
    status: str
    date_start: FlexibleDate
    date_end: FlexibleDate
    stack: list[str] = Field(default_factory=list)
    skills: list[str] = Field(default_factory=list)
    links: dict[str, str] = Field(default_factory=dict)

class GeneralDocumentModel(BaseDocumentModel):
    section: Literal["bio", "goals", "contact", "resume", "faq"]

DocumentModel = BaseDocumentModel