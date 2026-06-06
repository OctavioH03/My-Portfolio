from app.models.document_model import DocumentModel, ExperienceDocumentModel, ProjectDocumentModel
from app.models.chunk_model import ChunkMetaData
from app.core.logging import get_logger

logger = get_logger(__name__)
# Helper functions to build metadata for each section
def _build_experience_metadata(base: dict, document: ExperienceDocumentModel) -> ChunkMetaData:
    """Helper function to build metadata for an experience frontmatter model
    Args:
        base: The base metadata
        document: The experience document model to build metadata for
    Returns:
        The metadata for the experience frontmatter model
    """
    metadata = {
        **base,
        "organization": document.organization,
        "employment_type": document.employment_type,
        "stack": document.stack,
        "skills": document.skills
    }
    return ChunkMetaData(**metadata)

def _build_project_metadata(base: dict, document: ProjectDocumentModel) -> ChunkMetaData:
    """Helper function to build metadata for a project frontmatter model
    Args:
        base: The base metadata
        document: The project document model to build metadata for
    Returns:
        The metadata for the project frontmatter model
    """
    metadata = {
        **base,
        "status": document.status,
        "stack": document.stack,
        "skills": document.skills,
        "links": document.links
    }
    return ChunkMetaData(**metadata)

BUILDERS = {
    "experience": _build_experience_metadata,
    "project": _build_project_metadata
}

# Main function to build metadata for a frontmatter model
def build_metadata(document: DocumentModel) -> ChunkMetaData:
    """Build metadata for a frontmatter model
    Args:
        document: The document model to build metadata for
    Returns:
        The metadata for the frontmatter model
    """
    base = {
        "section": document.section,
        "title": document.title,
        "last_reviewed": document.last_reviewed,
        "source_path": document.source_path
    }
    builder = BUILDERS.get(document.section)
    # All sections without a builder will use the base metadata
    # At this point, we have validated the section and frontmatter model
    if not builder:
        return ChunkMetaData(**base)
    return builder(base, document)