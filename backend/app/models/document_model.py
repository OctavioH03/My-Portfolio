from datetime import date
from pydantic import BaseModel, Field
from typing import Literal, Optional
from app.models.flexible_date_model import FlexibleDate

class BaseDocumentModel(BaseModel):
    id: str
    title: str
    section: str
    content: str
    last_reviewed: date
    tags: list[str] = Field(default_factory=list)
    related: list[str] = Field(default_factory=list)
    summary: Optional[str] = None # not used in the database
    source_path: str

class ExperienceDocumentModel(BaseDocumentModel):
    section: Literal["experience"]
    organization: str
    employment_type: str
    location: str
    date_start: FlexibleDate # not used in the database
    date_end: FlexibleDate # not used in the database
    stack: list[str] = Field(default_factory=list)
    skills: list[str] = Field(default_factory=list)

class ProjectDocumentModel(BaseDocumentModel):
    section: Literal["project"]
    status: str
    date_start: FlexibleDate # not used in the database
    date_end: FlexibleDate # not used in the database
    stack: list[str] = Field(default_factory=list)
    skills: list[str] = Field(default_factory=list)
    links: dict[str, str] = Field(default_factory=dict)

class GeneralDocumentModel(BaseDocumentModel):
    section: Literal["bio", "goals", "contact", "resume", "faq"]

DocumentModel = BaseDocumentModel