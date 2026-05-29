from datetime import date
from app.models.frontmatter_model import ExperienceFrontmatterModel, GeneralFrontmatterModel, parse_frontmatter, ProjectFrontmatterModel
from app.tests.factories.frontmatter_factory import general_frontmatter_factory, experience_frontmatter_factory, project_frontmatter_factory
import pytest
from pydantic import ValidationError

@pytest.mark.parametrize("raw_content, expected_type", [
    (general_frontmatter_factory(), GeneralFrontmatterModel),
    (experience_frontmatter_factory(), ExperienceFrontmatterModel),
    (project_frontmatter_factory(), ProjectFrontmatterModel),
])
def test_mapping_frontmatter_data_to_model(raw_content, expected_type):
    model = parse_frontmatter(raw_content)
    assert isinstance(model, expected_type)

def test_project_not_returned_as_experience():
    raw_content = project_frontmatter_factory()
    model = parse_frontmatter(raw_content)
    assert isinstance(model, ProjectFrontmatterModel)
    assert not isinstance(model, ExperienceFrontmatterModel)

@pytest.mark.parametrize("raw_content", [
    general_frontmatter_factory(),
    experience_frontmatter_factory(),
    project_frontmatter_factory(),
])
def test_all_fields(raw_content):
    model = parse_frontmatter(raw_content)
    assert model.model_dump() == raw_content

def test_invalid_section():
    raw_content = general_frontmatter_factory(section="invalid")
    with pytest.raises(ValueError):
        parse_frontmatter(raw_content)

def test_missing_required_field():
    raw_content = general_frontmatter_factory()
    del raw_content["title"]
    with pytest.raises(ValidationError):
        parse_frontmatter(raw_content)

def test_missing_optional_field():
    raw_content = general_frontmatter_factory()
    del raw_content["summary"]
    del raw_content["related"]
    del raw_content["tags"]
    model = parse_frontmatter(raw_content)
    assert model.summary is None
    assert model.tags == []
    assert model.related == []

def test_extra_fields_are_ignored():
    raw_content = general_frontmatter_factory()
    raw_content["extra_field"] = "extra_value"
    model = parse_frontmatter(raw_content)
    assert "extra_field" not in model.model_dump()

def test_missing_experience_specific_field():
    raw_content = experience_frontmatter_factory()
    del raw_content["organization"]
    with pytest.raises(ValidationError):
        parse_frontmatter(raw_content)

def test_missing_project_specific_field():
    raw_content = project_frontmatter_factory()
    del raw_content["status"]
    with pytest.raises(ValidationError):
        parse_frontmatter(raw_content)

def test_valid_date_format():
    raw_content = general_frontmatter_factory(last_reviewed="2026-05-25")
    model = parse_frontmatter(raw_content)
    assert model.last_reviewed == date(2026, 5, 25)

def test_invalid_date_format():
    raw_content = general_frontmatter_factory(last_reviewed="May 25, 2026")
    with pytest.raises(ValidationError):
        parse_frontmatter(raw_content)

def test_invalid_date_range():
    raw_content = experience_frontmatter_factory(date_start=date(2026, 5, 26), date_end=date(2026, 5, 25))
    with pytest.raises(ValueError):
        parse_frontmatter(raw_content)