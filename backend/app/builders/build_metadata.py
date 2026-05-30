from app.models.frontmatter_model import SECTION_MODELS, FrontmatterModel
from app.models.chunk_model import ChunkMetaData
from app.models.frontmatter_model import ExperienceFrontmatterModel, ProjectFrontmatterModel
from app.core.logging import get_logger

logger = get_logger(__name__)
# Helper functions to build metadata for each section
def _build_experience_metadata(base: dict, frontmatter: ExperienceFrontmatterModel) -> ChunkMetaData:
    """Helper function to build metadata for an experience frontmatter model
    Args:
        base: The base metadata
        frontmatter: The experience frontmatter model to build metadata for
    Returns:
        The metadata for the experience frontmatter model
    """
    metadata = {
        **base,
        "organization": frontmatter.organization,
        "employment_type": frontmatter.employment_type,
        "stack": frontmatter.stack,
        "skills": frontmatter.skills
    }
    return ChunkMetaData(**metadata)

def _build_project_metadata(base: dict, frontmatter: ProjectFrontmatterModel) -> ChunkMetaData:
    """Helper function to build metadata for a project frontmatter model
    Args:
        base: The base metadata
        frontmatter: The project frontmatter model to build metadata for
    Returns:
        The metadata for the project frontmatter model
    """
    metadata = {
        **base,
        "status": frontmatter.status,
        "stack": frontmatter.stack,
        "skills": frontmatter.skills,
        "links": frontmatter.links
    }
    return ChunkMetaData(**metadata)

BUILDERS = {
    "experience": _build_experience_metadata,
    "project": _build_project_metadata
}

# Main function to build metadata for a frontmatter model
def build_metadata(frontmatter: FrontmatterModel) -> ChunkMetaData:
    """Build metadata for a frontmatter model
    Args:
        frontmatter: The frontmatter model to build metadata for
    Returns:
        The metadata for the frontmatter model
    """
    base = {
        "section": frontmatter.section,
        "title": frontmatter.title,
        "last_reviewed": frontmatter.last_reviewed
    }
    builder = BUILDERS.get(frontmatter.section)
    # All sections without a builder will use the base metadata
    # At this point, we have validated the section and frontmatter model
    if not builder:
        return ChunkMetaData(**base)
    return builder(base, frontmatter)