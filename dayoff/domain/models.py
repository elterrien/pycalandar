from dataclasses import dataclass
from datetime import date

from dayoff.domain.value_objects import HolidayType, HolidayName


@dataclass(frozen=True)
class Holiday:
    name: HolidayName
    date: date
    type: HolidayType
    department: str | None = None
    region: str | None = None



class Calendar:
    def __init__(self, holidays: list[Holiday]):
        self._holidays = holidays

    def is_holiday(self, d: date) -> bool:
        return any(h.date == d for h in self._holidays)

    def get_named_holiday(self, d: date) -> HolidayName | None:
        for h in self._holidays:
            if h.date == d:
                return h.name
        return None

    def all(self) -> list[Holiday]:
        return self._holidays