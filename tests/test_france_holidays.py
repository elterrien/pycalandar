import unittest
from datetime import date

from dayoff.countries.fr import FranceHolidays
from dayoff.domain.models import Holiday
from dayoff.domain.value_objects import HolidayType, HolidayName


class TestEasterFranceHolidays(unittest.TestCase):

    def test_easter_2000(self):
        self.assertEqual(FranceHolidays(2000).calculate_easter(), date(2000, 4, 23))

    def test_easter_2001(self):
        self.assertEqual(FranceHolidays(2001).calculate_easter(), date(2001, 4, 15))

    def test_easter_2003(self):
        self.assertEqual(FranceHolidays(2003).calculate_easter(), date(2003, 4, 20))

    def test_easter_2008(self):
        self.assertEqual(FranceHolidays(2008).calculate_easter(), date(2008, 3, 23))

    def test_easter_2010(self):
        self.assertEqual(FranceHolidays(2010).calculate_easter(), date(2010, 4, 4))

    def test_easter_2015(self):
        self.assertEqual(FranceHolidays(2015).calculate_easter(), date(2015, 4, 5))

    def test_easter_2018(self):
        self.assertEqual(FranceHolidays(2018).calculate_easter(), date(2018, 4, 1))

    def test_easter_2023(self):
        self.assertEqual(FranceHolidays(2023).calculate_easter(), date(2023, 4, 9))

    def test_easter_2025(self):
        self.assertEqual(FranceHolidays(2025).calculate_easter(), date(2025, 4, 20))

    def test_easter_2026(self):
        self.assertEqual(FranceHolidays(2026).calculate_easter(), date(2026, 4, 5))

    def test_easter_2027(self):
        self.assertEqual(FranceHolidays(2027).calculate_easter(), date(2027, 3, 28))

    def test_easter_2028(self):
        self.assertEqual(FranceHolidays(2028).calculate_easter(), date(2028, 4, 16))


class TestEasterMondayFranceHolidays(unittest.TestCase):

    def test_easter_monday_2000(self):
        self.assertEqual(FranceHolidays(2000).calculate_easter_monday(date(2000, 4, 23)), Holiday(
            name=HolidayName.EASTER_MONDAY,
            date=date(2000, 4, 24),
            type=HolidayType.PUBLIC,
        ))

    def test_easter_monday_2001(self):
        self.assertEqual(FranceHolidays(2001).calculate_easter_monday(date(2001, 4, 15)), Holiday(
            name=HolidayName.EASTER_MONDAY,
            date=date(2001, 4, 16),
            type=HolidayType.PUBLIC,
        ))

class TestAssumptionFranceHolidays(unittest.TestCase):

    def test_ascension_2000(self):
        self.assertEqual(FranceHolidays(2000).calculate_ascension(date(2000, 4, 23)), Holiday(
            name=HolidayName.ASCENSION,
            date=date(2000, 6, 1),
            type=HolidayType.PUBLIC,
        ))


class TestAlsaceMoselleAdditionalHolidays(unittest.TestCase):

    def test_department_68_includes_good_friday_and_st_etienne(self):
        holidays = FranceHolidays(2023, "68").get_holidays()
        self.assertIn(
            Holiday(
                name=HolidayName.VENDREDI_SAINT,
                date=date(2023, 4, 7),
                type=HolidayType.PUBLIC,
            ),
            holidays,
        )
        self.assertIn(
            Holiday(
                name=HolidayName.SAINT_ETIENNE,
                date=date(2023, 12, 26),
                type=HolidayType.PUBLIC,
            ),
            holidays,
        )
