# Dayoff

Example usage of the package providing holiday calendars for multiple European countries.

```python
from dayoff import get_holidays, CountryCode

holidays_fr = get_holidays(2024, CountryCode.FR, department="75")
holidays_de = get_holidays(2024, CountryCode.DE)
```

`get_holidays` returns a list of `Holiday` objects for the requested country and year.
