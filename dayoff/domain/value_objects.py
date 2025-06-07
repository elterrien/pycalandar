from enum import Enum

class HolidayType(Enum):
    PUBLIC = "public"
    BANK = "bank"
    COMPANY = "company"

class HolidayName(Enum):
    VENDREDI_SAINT = "Vendredi Saint"
    EASTER = "Easter"
    EASTER_MONDAY = "Easter Monday"
    ASCENSION = "Ascension"
    PENTECOST = "Pentecost"
    ASSUMPTION = "Assumption"
    ARMISTICE = "Armistice"
    CHRISTMAS = "Christmas"
    SAINT_ETIENNE = "Saint Etienne"
    NEW_YEAR = "New Year"
    LABOR_DAY = "Labor Day"
    VICTORY_1945 = "Victory 1945"
    NATIONAL_DAY = "National Day"
    ABOLITION_SLAVERY = "Abolition of Slavery"