"""Lab 11 – Zadanie 3 (★): Statystyka opisowa z modułem math.

Napisz funkcje SAMODZIELNIE (bez modułu statistics) – testy porównają je ze statistics.
"""
import math


def mean(values):
    """Średnia arytmetyczna."""
    raise NotImplementedError


def median(values):
    """Mediana: środkowy element posortowanych danych, a dla parzystej liczby – średnia dwóch środkowych.

    NIE zmieniaj listy wejściowej (użyj sorted, nie sort).
    """
    raise NotImplementedError


def std_dev(values):
    """Odchylenie standardowe z PRÓBY:  sqrt( Σ(x - średnia)² / (n - 1) ).  Użyj math.sqrt."""
    raise NotImplementedError
