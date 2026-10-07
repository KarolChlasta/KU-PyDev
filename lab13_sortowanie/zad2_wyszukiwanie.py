"""Lab 13 – Zadanie 2 (★): Wyszukiwanie liniowe i binarne."""


def linear_search(values, target):
    """Indeks PIERWSZEGO wystąpienia target albo -1. Przeglądaj elementy po kolei (bez index())."""
    raise NotImplementedError


def binary_search(sorted_values, target):
    """Indeks target w POSORTOWANEJ liście albo -1 – wyszukiwanie binarne w pętli while.

        low, high = 0, len(sorted_values) - 1
        while low <= high:
            middle = (low + high) // 2
            ...
    Nie używaj index() ani in – testy liczą, ile elementów odczytasz (dla miliona: najwyżej 25).
    """
    raise NotImplementedError


def binary_search_steps(sorted_values, target):
    """Ile obrotów pętli wykonało wyszukiwanie binarne (niezależnie od tego, czy znalazło)."""
    raise NotImplementedError
