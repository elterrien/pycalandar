from datetime import date, timedelta

from dayoff.domain.models import Holiday
from dayoff.domain.value_objects import HolidayType, HolidayName


class FranceHolidays:


    def __init__(self, year: int, department: str = "75"):
        self.year = year
        self.department = department

    @staticmethod
    def calculate_friday_before_easter(easter_day: date) -> Holiday:
        """
        Calculate the Friday before Easter date for the given year in France.
        """
        return Holiday(
            name=HolidayName.VENDREDI_SAINT,
            date=easter_day - timedelta(days=2),
            type=HolidayType.PUBLIC,
        )

    @staticmethod
    def calculate_easter_monday(easter_day: date) -> Holiday:
        """
        Calculate the Easter Monday date for the given year in France.
        """
        return Holiday(
            name=HolidayName.EASTER_MONDAY,
            date=easter_day + timedelta(days=1),
            type=HolidayType.PUBLIC,
        )

    @staticmethod
    def calculate_ascension(easter_day: date) -> Holiday:
        """
        Calculate the Ascension date for the given year in France.
        """
        return Holiday(
            name=HolidayName.ASCENSION,
            date=easter_day + timedelta(days=39),
            type=HolidayType.PUBLIC,
        )

    @staticmethod
    def calculate_pentecost(easter_day: date) -> Holiday:
        """
        Calculate the Pentecost date for the given year in France.
        """
        return Holiday(
            name=HolidayName.PENTECOST,
            date=easter_day + timedelta(days=50),
            type=HolidayType.PUBLIC,
        )

    def calculate_easter(self) -> date:
        """
        Calculate the Easter date for the given year in France.
        """
        # Using the Anonymous Gregorian algorithm to calculate Easter
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
        L = (2 * t + 2 * b -e -d + 32) % 7
        h = (n + 11 * e + 22 * L) // 451
        m = (e + L - 7 * h + 114) // 31
        j = (e + L - 7 * h + 114) % 31
        return date(self.year, m, j + 1)

    def map_abolition_slavery(self) -> Holiday:
        """
        Maps the abolition
        """
        abolition_day = {
            "971": date(self.year, 5, 27),  # Guadeloupe
            "972": date(self.year, 5, 22),  # Martinique
            "973": date(self.year, 6, 10),  # French Guiana
            "974": date(self.year, 12, 20),  # Réunion
            "976": date(self.year, 4, 27),  # Mayotte
            "977": date(self.year, 10, 9),  # Saint Barthélemy
            "978": date(self.year, 5, 27),  # Saint Martin

        }
        return Holiday(name=HolidayName.ABOLITION_SLAVERY, date=abolition_day[self.department], type=HolidayType.PUBLIC)

    def get_holidays(self) -> list[Holiday]:
        """
        Returns a list of holidays for the given year in France.
        """
        easter_day = self.calculate_easter()
        holidays = [Holiday(name=HolidayName.NEW_YEAR, date=date(self.year, 1, 1), type=HolidayType.PUBLIC),
                    Holiday(name=HolidayName.LABOR_DAY, date=date(self.year, 5, 1), type=HolidayType.PUBLIC),
                    Holiday(name=HolidayName.CHRISTMAS, date=date(self.year, 12, 25), type=HolidayType.PUBLIC),
                    Holiday(name=HolidayName.NATIONAL_DAY, date=date(self.year, 7, 14), type=HolidayType.PUBLIC),
                    Holiday(name=HolidayName.ARMISTICE, date=date(self.year, 11, 11), type=HolidayType.PUBLIC),
                    Holiday(name=HolidayName.ASSUMPTION, date=date(self.year, 8, 15), type=HolidayType.PUBLIC),
                    self.calculate_easter_monday(easter_day),
                    self.calculate_ascension(easter_day),
                    self.calculate_pentecost(easter_day),]
        if self.department in ["57", "67"]:
            holidays.append(Holiday(name=HolidayName.SAINT_ETIENNE, date=date(self.year, 12, 26), type=HolidayType.PUBLIC))
            holidays.append(
                Holiday(name=HolidayName.VENDREDI_SAINT, date=self.calculate_friday_before_easter(easter_day).date, type=HolidayType.PUBLIC)
            )
        if self.department in ["971", "972", "973", "974", "976", "977", "978"]:
            holidays.append(self.map_abolition_slavery())
        return holidays