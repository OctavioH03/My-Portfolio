from datetime import date

def validate_daterange(date_start: date, date_end: date) -> None:
    if date_start > date_end:
        raise ValueError("Date start cannot be after date end")