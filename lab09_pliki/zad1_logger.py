"""Lab 09 – Zadanie 1 (★): Logowanie zdarzeń do pliku.

Każdy wpis to jedna linia:  2026-12-08 09:15:02 | treść komunikatu
"""
from datetime import datetime


def log(message, path):
    """Dopisuje na KOŃCU pliku linię "RRRR-MM-DD GG:MM:SS | message".

    Wskazówki:
      - tryb "a" (append) dopisuje, "w" by nadpisał plik!
      - datetime.now().strftime("%Y-%m-%d %H:%M:%S")
      - zawsze podawaj encoding="utf-8"
    """
    raise NotImplementedError


def read_log(path):
    """Zwraca listę wpisów (bez znaków końca linii). Brak pliku -> pusta lista.

    Wskazówka: pathlib.Path(path).exists() albo try/except FileNotFoundError.
    """
    raise NotImplementedError


def count_entries(path):
    """Liczba wpisów w logu."""
    raise NotImplementedError
