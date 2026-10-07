"""Kolokwium II – PRZYKŁAD 1: pliki i wyjątki.

Plik CSV z liniami  imię;punkty  (np. "Ala;45").
"""


class ScoresFileError(Exception):
    """Zgłaszany, gdy pliku z wynikami nie ma. Komunikat zawiera ścieżkę pliku."""


def load_scores(path):
    """Zwraca krotkę (słownik imię -> punkty jako float, liczba_błędnych_linii).

    Puste linie pomija bez liczenia; linie bez ";" albo z punktami, które nie są liczbą – liczy jako błędne.
    Brak pliku -> ScoresFileError(f"Brak pliku: {path}").
    """
    raise NotImplementedError
