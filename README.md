# Dayoff

Dayoff is a minimal library for computing French public holidays by year and department. It can be used to build small tools that manage days off or to simply check whether a given date is a holiday.

## Installation

Install the project using `pip`. The package metadata is defined in `pyproject.toml` so you can install it directly from the repository:

```bash
pip install .
```

or install the published package:

```bash
pip install dayoff
```

## Usage

The example below fetches holidays for a given year and département (Paris is `75`).

```python
from dayoff.countries.fr import FranceHolidays

holidays = FranceHolidays(2024, department="75").get_holidays()
for h in holidays:
    print(h.name.value, h.date)
```
