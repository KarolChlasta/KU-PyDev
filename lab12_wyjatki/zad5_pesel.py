"""Lab 12 – Zadanie 5 (☆, dodatkowe): Walidator numeru PESEL z hierarchią wyjątków.

PESEL: RRMMDDPPPPK
  - cyfra kontrolna K = (10 - (Σ cyfra_i · waga_i) mod 10) mod 10, wagi 1,3,7,9,1,3,7,9,1,3
  - miesiąc koduje stulecie: 1–12 -> 1900, 21–32 -> 2000, 41–52 -> 2100, 61–72 -> 2200, 81–92 -> 1800
  - 10. cyfra: parzysta -> kobieta ("K"), nieparzysta -> mężczyzna ("M")
"""
from datetime import date

WEIGHTS = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]


class PeselError(ValueError):
    """Bazowy wyjątek dla błędnego numeru PESEL."""


# TODO: zdefiniuj PeselLengthError, PeselDigitsError, PeselChecksumError dziedziczące po PeselError


def validate(pesel):
    """Zwraca True albo zgłasza odpowiedni wyjątek (długość, cyfry, suma kontrolna)."""
    raise NotImplementedError


def birth_date(pesel):
    """Data urodzenia zakodowana w numerze."""
    raise NotImplementedError


def sex(pesel):
    """ "K" albo "M"."""
    raise NotImplementedError
