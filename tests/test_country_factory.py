import unittest
from datetime import date

from dayoff import get_holidays, CountryCode
from dayoff.countries import CountryHolidaysFactory, GermanyHolidays, SpainHolidays


class TestCountryHolidaysFactory(unittest.TestCase):
    def test_create_germany(self):
        provider = CountryHolidaysFactory.create(CountryCode.DE, 2024)
        self.assertIsInstance(provider, GermanyHolidays)

    def test_create_spain(self):
        provider = CountryHolidaysFactory.create(CountryCode.ES, 2024)
        self.assertIsInstance(provider, SpainHolidays)


class TestGetHolidays(unittest.TestCase):
    def test_germany_new_year(self):
        holidays = get_holidays(2024, CountryCode.DE)
        self.assertIn(date(2024, 1, 1), [h.date for h in holidays])

    def test_spain_national_day(self):
        holidays = get_holidays(2024, CountryCode.ES)
        self.assertIn(date(2024, 10, 12), [h.date for h in holidays])


if __name__ == "__main__":
    unittest.main()
