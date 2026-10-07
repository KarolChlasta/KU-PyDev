"""Lab 11 – Zadanie 2 (★): Konwersja stref czasowych.

Strefy z bazy IANA, np. "Europe/Warsaw", "America/New_York", "Asia/Tokyo", "UTC".
Na Windows najpierw:  python -m pip install tzdata
"""
from datetime import datetime
from zoneinfo import ZoneInfo

FORMAT = "%Y-%m-%d %H:%M"


def convert(text, from_zone, to_zone):
    """Przelicza czas "RRRR-MM-DD GG:MM" ze strefy from_zone na to_zone i zwraca go w tym samym formacie.

    Wskazówki:
        dt = datetime.strptime(text, FORMAT).replace(tzinfo=ZoneInfo(from_zone))
        dt.astimezone(ZoneInfo(to_zone)).strftime(FORMAT)
    """
    raise NotImplementedError


def utc_offset(zone, text):
    """Przesunięcie strefy względem UTC w godzinach (float) w danej chwili, np. 1, 2 albo 5.5.

    Wskazówka: dt.utcoffset() zwraca timedelta; .total_seconds() / 3600
    """
    raise NotImplementedError
