from pathlib import Path
from app.models.frontmatter_model import FrontmatterModel, parse_frontmatter
import yaml

def load_documents(path: Path) -> tuple[FrontmatterModel, str]:
    text = path.read_text(encoding="utf-8")
    _, yaml_frontmatter, markdown_content = text.split("---", 2)
    frontmatter = yaml.safe_load(yaml_frontmatter)
    return parse_frontmatter(frontmatter), markdown_content

def load_documents_from_directory(path: Path, exclude: list[str] = []) -> list[tuple[FrontmatterModel, str]]:
    documents = []
    for file in path.glob("**/*.md"):
        if file.name in exclude:
            continue
        documents.append(load_documents(file))
    return documents

