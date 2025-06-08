"""Public API for dayoff package."""

from .countries import (
    CountryCode,
    CountryHolidaysFactory,
)


def get_holidays(year: int, country: CountryCode, **kwargs):
    """Return list of :class:`Holiday` objects for given country and year."""
    provider = CountryHolidaysFactory.create(country, year, **kwargs)
    return provider.get_holidays()

__all__ = ["CountryCode", "get_holidays"]
