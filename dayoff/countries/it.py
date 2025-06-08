from datetime import date, timedelta

from dayoff.domain.models import Holiday
from dayoff.domain.value_objects import HolidayType, HolidayName


class ItalyHolidays:
    def __init__(self, year: int):
        self.year = year

    def calculate_easter(self) -> date:
        n = self.year % 19
        c = self.year // 100
        u = self.year % 100
        s = c // 4
        t = c % 4
        p = (c + 8) // 25
        q = (c - p + 1) // 3
        e = (19 * n + c - s - q + 15) % 30
        b = u // 4
        d = u % 4
        L = (2 * t + 2 * b - e - d + 32) % 7
        h = (n + 11 * e + 22 * L) // 451
        m = (e + L - 7 * h + 114) // 31
        j = (e + L - 7 * h + 114) % 31
        return date(self.year, m, j + 1)

    @staticmethod
    def calculate_easter_monday(easter_day: date) -> Holiday:
        return Holiday(
            name=HolidayName.EASTER_MONDAY,
            date=easter_day + timedelta(days=1),
            type=HolidayType.PUBLIC,
        )

    def get_holidays(self) -> list[Holiday]:
        easter = self.calculate_easter()
        return [
            Holiday(name=HolidayName.NEW_YEAR, date=date(self.year, 1, 1), type=HolidayType.PUBLIC),
            Holiday(name=HolidayName.LABOR_DAY, date=date(self.year, 5, 1), type=HolidayType.PUBLIC),
            Holiday(name=HolidayName.NATIONAL_DAY, date=date(self.year, 6, 2), type=HolidayType.PUBLIC),
            Holiday(name=HolidayName.CHRISTMAS, date=date(self.year, 12, 25), type=HolidayType.PUBLIC),
            self.calculate_easter_monday(easter),
        ]
