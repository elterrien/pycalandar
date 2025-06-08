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


class TestFridayBeforeEasterFranceHolidays(unittest.TestCase):
    def test_friday_before_easter_2023(self):
        easter_day = date(2023, 4, 9)
        self.assertEqual(
            FranceHolidays(2023).calculate_friday_before_easter(easter_day),
            Holiday(
                name=HolidayName.VENDREDI_SAINT,
                date=date(2023, 4, 7),
                type=HolidayType.PUBLIC,
            ),
        )

class TestPentecostFranceHolidays(unittest.TestCase):
    def test_pentecost_2023(self):
        easter_day = date(2023, 4, 9)
        self.assertEqual(
            FranceHolidays(2023).calculate_pentecost(easter_day),
            Holiday(
                name=HolidayName.PENTECOST,
                date=date(2023, 5, 29),
                type=HolidayType.PUBLIC,
            ),
        )

class TestAbolitionSlaveryMappingFranceHolidays(unittest.TestCase):
    def test_map_all_departments(self):
        expected = {
            "971": date(2023, 5, 27),
            "972": date(2023, 5, 22),
            "973": date(2023, 6, 10),
            "974": date(2023, 12, 20),
            "976": date(2023, 4, 27),
            "977": date(2023, 10, 9),
            "978": date(2023, 5, 27),
        }
        for dep, dt in expected.items():
            with self.subTest(dep=dep):
                self.assertEqual(
                    FranceHolidays(2023, dep).map_abolition_slavery(),
                    Holiday(name=HolidayName.ABOLITION_SLAVERY, date=dt, type=HolidayType.PUBLIC),
                )

class TestFranceHolidaysList(unittest.TestCase):
    def test_get_holidays_2023_department_67(self):
        fh = FranceHolidays(2023, "67")
        easter = fh.calculate_easter()
        expected = [
            Holiday(name=HolidayName.NEW_YEAR, date=date(2023, 1, 1), type=HolidayType.PUBLIC),
            Holiday(name=HolidayName.LABOR_DAY, date=date(2023, 5, 1), type=HolidayType.PUBLIC),
            Holiday(name=HolidayName.CHRISTMAS, date=date(2023, 12, 25), type=HolidayType.PUBLIC),
            Holiday(name=HolidayName.NATIONAL_DAY, date=date(2023, 7, 14), type=HolidayType.PUBLIC),
            Holiday(name=HolidayName.ARMISTICE, date=date(2023, 11, 11), type=HolidayType.PUBLIC),
            Holiday(name=HolidayName.ASSUMPTION, date=date(2023, 8, 15), type=HolidayType.PUBLIC),
            fh.calculate_easter_monday(easter),
            fh.calculate_ascension(easter),
            fh.calculate_pentecost(easter),
            Holiday(name=HolidayName.SAINT_ETIENNE, date=date(2023, 12, 26), type=HolidayType.PUBLIC),
            Holiday(name=HolidayName.VENDREDI_SAINT, date=date(2023, 4, 7), type=HolidayType.PUBLIC),
        ]
        self.assertEqual(fh.get_holidays(), expected)
