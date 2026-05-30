from app.models.flexible_date_model import FlexibleDateModel


def validate_daterange(date_start: FlexibleDateModel, date_end: FlexibleDateModel) -> None:
    if date_start > date_end:
        raise ValueError("Date start cannot be after date end")
