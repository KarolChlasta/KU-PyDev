"""Lab 11 – Zadanie 5 (☆, dodatkowe): Kalendarz."""
from datetime import date, timedelta

DAYS = ["poniedziałek", "wtorek", "środa", "czwartek", "piątek", "sobota", "niedziela"]


def weekday_name(day):
    """Polska nazwa dnia tygodnia. Wskazówka: day.weekday() zwraca 0 dla poniedziałku."""
    raise NotImplementedError


def is_weekend(day):
    """Czy to sobota albo niedziela?"""
    raise NotImplementedError


def working_days(start, end):
    """Liczba dni roboczych (pon–pt) od start do end WŁĄCZNIE (bez uwzględniania świąt)."""
    raise NotImplementedError
