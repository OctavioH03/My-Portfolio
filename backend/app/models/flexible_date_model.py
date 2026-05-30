from typing import Annotated, Any, Literal, Optional

from pydantic import BaseModel, BeforeValidator


class FlexibleDateModel(BaseModel):
    year: int
    month: Optional[int] = None
    day: Optional[int] = None
    precision: Literal["year", "month", "day"] = "year"

    @classmethod
    def from_string(cls, date_string: str) -> "FlexibleDateModel":
        parts = date_string.split("-")
        if len(parts) == 1:
            return cls(year=int(parts[0]), precision="year")
        if len(parts) == 2:
            return cls(year=int(parts[0]), month=int(parts[1]), precision="month")
        if len(parts) == 3:
            return cls(
                year=int(parts[0]),
                month=int(parts[1]),
                day=int(parts[2]),
                precision="day",
            )
        raise ValueError(f"Invalid date string: {date_string}")

    def _key(self) -> tuple[int, int, int]:
        return (
            self.year,
            self.month or 0,
            self.day or 0,
        )

    def __lt__(self, other: "FlexibleDateModel") -> bool:
        return self._key() < other._key()

    def __le__(self, other: "FlexibleDateModel") -> bool:
        return self._key() <= other._key()

    def __gt__(self, other: "FlexibleDateModel") -> bool:
        return self._key() > other._key()

    def __ge__(self, other: "FlexibleDateModel") -> bool:
        return self._key() >= other._key()

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, FlexibleDateModel):
            return NotImplemented
        return self._key() == other._key()

    def __ne__(self, other: object) -> bool:
        if not isinstance(other, FlexibleDateModel):
            return NotImplemented
        return self._key() != other._key()


def coerce_flexible_date(value: Any) -> FlexibleDateModel:
    if isinstance(value, FlexibleDateModel):
        return value
    if isinstance(value, str):
        return FlexibleDateModel.from_string(value)
    if isinstance(value, dict):
        return FlexibleDateModel.model_validate(value)
    raise ValueError(f"Invalid flexible date input: {value!r}")


FlexibleDate = Annotated[FlexibleDateModel, BeforeValidator(coerce_flexible_date)]
