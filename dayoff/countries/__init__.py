from enum import Enum

from .fr import FranceHolidays
from .de import GermanyHolidays
from .es import SpainHolidays
from .it import ItalyHolidays

class CountryCode(Enum):
    FR = "FR"
    DE = "DE"
    ES = "ES"
    IT = "IT"


class CountryHolidaysFactory:
    """Return holiday provider classes based on country code."""

    _providers = {
        CountryCode.FR: FranceHolidays,
        CountryCode.DE: GermanyHolidays,
        CountryCode.ES: SpainHolidays,
        CountryCode.IT: ItalyHolidays,
    }

    @classmethod
    def register(cls, code: CountryCode, provider):
        cls._providers[code] = provider

    @classmethod
    def create(cls, code: CountryCode, year: int, **kwargs):
        provider_cls = cls._providers.get(code)
        if provider_cls is None:
            raise ValueError(f"Unsupported country: {code}")
        return provider_cls(year, **kwargs)
