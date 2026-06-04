from pathlib import Path
from app.models.document_model import DocumentModel
from app.builders.document_factory import create_document
import yaml

def load_documents(path: Path) -> DocumentModel:
    text = path.read_text(encoding="utf-8")
    _, yaml_frontmatter, markdown_content = text.split("---", 2)
    frontmatter = yaml.safe_load(yaml_frontmatter)
    return create_document(markdown_content, frontmatter)

def load_documents_from_directory(path: Path, exclude: list[str] = []) -> DocumentModel:
    documents = []
    for file in path.glob("**/*.md"):
        if file.name in exclude:
            continue
        documents.append(load_documents(file))
    return documents

