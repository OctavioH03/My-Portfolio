import app.core.logging as logging
from app.models.frontmatter_model import FrontmatterModel
from app.builders.chunk_factory import create_chunks

logger = logging.getLogger(__name__)

def chunk_document(document: tuple[FrontmatterModel, str]) -> list[str]:
    #1. Parse the document into a list of reasonably sized chunks
    frontmatter, markdown_content = document
    split_content = split_markdown_content(markdown_content)
    chunks = create_chunks(split_content, frontmatter)
    return chunks

def split_markdown_content(markdown_content: str) -> list[tuple[list[str], str]]:
    # Split the markdown content using headers keeping track of the header path
    # Each chunk should be a tuple of the header path and the content
    # TODO: 
    # - Select a method to split the markdown content
        # - Use LangChain's MarkdownHeaderTextSplitter?
        # - Use a custom regex to split the markdown content?
    # - Implement the method to split the markdown content
    # - Return the list of tuples of the header path and the content
    return []