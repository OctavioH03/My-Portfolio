from app.models.flexible_date_model import FlexibleDateModel
import pytest

def test_valid_flexible_date_format():
    date_string = "2026-04"
    date = FlexibleDateModel.from_string(date_string)
    assert date.year == 2026
    assert date.month == 4
    assert date.precision == "month"

def test_invalid_flexible_date_format():
    date_string = "2026-04-01-01"
    with pytest.raises(ValueError):
        FlexibleDateModel.from_string(date_string)