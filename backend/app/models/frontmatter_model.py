from datetime import date
from app.utils.validation import validate_daterange
from app.models.flexible_date_model import FlexibleDate
from pydantic import BaseModel, Field, model_validator
from typing import Literal, Optional, Union

class BaseFrontmatterModel(BaseModel):
    id: str
    section: str
    title: str
    last_reviewed: date
    tags: list[str] = Field(default_factory=list)
    related: list[str] = Field(default_factory=list)
    summary: Optional[str] = None

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

SECTION_MODELS = {
    "experience": ExperienceFrontmatterModel,
    "project": ProjectFrontmatterModel,
    "bio": GeneralFrontmatterModel,
    "goals": GeneralFrontmatterModel,
    "contact": GeneralFrontmatterModel,
    "resume": GeneralFrontmatterModel,
    "faq": GeneralFrontmatterModel
}

def parse_frontmatter(raw_content: dict) -> FrontmatterModel:
    section = raw_content.get("section")
    if not section or section not in SECTION_MODELS:
        raise ValueError(f"Invalid section: {section}")
    model = SECTION_MODELS[section]
    return model.model_validate(raw_content)