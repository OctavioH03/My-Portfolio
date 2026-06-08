from app.models.document_model import DocumentModel
from app.models.frontmatter_model import FrontmatterModel, ExperienceFrontmatterModel, ProjectFrontmatterModel, GeneralFrontmatterModel
from app.models.document_model import ExperienceDocumentModel, ProjectDocumentModel, GeneralDocumentModel, DocumentModel
import re

SECTION_TO_MODEL: dict[str, tuple[type[FrontmatterModel], type[DocumentModel]]] = {
    "experience": (ExperienceFrontmatterModel, ExperienceDocumentModel),
    "project": (ProjectFrontmatterModel, ProjectDocumentModel),
    "bio": (GeneralFrontmatterModel, GeneralDocumentModel),
    "goals": (GeneralFrontmatterModel, GeneralDocumentModel),
    "contact": (GeneralFrontmatterModel, GeneralDocumentModel),
    "resume": (GeneralFrontmatterModel, GeneralDocumentModel),
    "faq": (GeneralFrontmatterModel, GeneralDocumentModel)
}

def create_document(content:str, raw_frontmatter: dict) -> DocumentModel:
    """Create a document model

    Args:
        content(str): The content of the document
        frontmatter(FrontmatterModel): The frontmatter model to create the document for
    Returns:
        DocumentModel: The document model
    """
    section = raw_frontmatter.get("section")
    if not section or section not in SECTION_TO_MODEL:
        raise ValueError(f"Invalid section: {section}")
    
    frontmatter_model, document_model = SECTION_TO_MODEL[section]
    frontmatter = frontmatter_model.model_validate(raw_frontmatter)
    return document_model(**frontmatter.model_dump(), content=content, id=_build_document_id(frontmatter.title, section))

def _build_document_id(title: str, section: str) -> str:
    """Build a document ID from the title and section

    Args:
        title(str): The title of the document
        section(str): The section of the document
    Returns:
        str: The document ID
    """
    slug = re.sub(r'[^a-zA-Z0-9]', '-', title)
    return f"{section}-{slug}" # example: experience-csu-ta