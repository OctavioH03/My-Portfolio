from datetime import date
from app.utils.validation import validate_daterange
from app.models.flexible_date_model import FlexibleDate
from pydantic import BaseModel, Field, model_validator
from typing import Literal, Optional, Union

class BaseFrontmatterModel(BaseModel):
    section: str
    title: str
    last_reviewed: date
    tags: list[str] = Field(default_factory=list)
    related: list[str] = Field(default_factory=list)
    summary: Optional[str] = None
    source_path: str

class ExperienceFrontmatterModel(BaseFrontmatterModel):
    section: Literal["experience"]
    organization: str
    location: str
    employment_type: str
    date_start: FlexibleDate
    date_end: FlexibleDate
    stack: list[str] = Field(default_factory=list)
    skills: list[str] = Field(default_factory=list)

    @model_validator(mode="after")
    def validate_daterange(self) -> "ExperienceFrontmatterModel":
        validate_daterange(self.date_start, self.date_end)
        return self

class ProjectFrontmatterModel(BaseFrontmatterModel):
    section: Literal["project"]
    status: str
    date_start: FlexibleDate
    date_end: FlexibleDate
    stack: list[str] = Field(default_factory=list)
    skills: list[str] = Field(default_factory=list)
    links: dict[str, str] = Field(default_factory=dict)

    @model_validator(mode="after")
    def validate_daterange(self) -> "ProjectFrontmatterModel":
        validate_daterange(self.date_start, self.date_end)
        return self

class GeneralFrontmatterModel(BaseFrontmatterModel):
    section: Literal["bio", "goals", "contact", "resume", "faq"]

FrontmatterModel = Union[
    ExperienceFrontmatterModel, 
    ProjectFrontmatterModel, 
    GeneralFrontmatterModel
]