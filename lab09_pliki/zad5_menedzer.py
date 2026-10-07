"""Lab 09 – Zadanie 5 (☆, dodatkowe): Menedżer plików (pathlib)."""
from pathlib import Path


def find_by_extension(folder, extension):
    """Posortowana lista NAZW plików z danym rozszerzeniem (bez względu na wielkość liter).

    Wskazówki: Path(folder).iterdir(), p.is_file(), p.suffix.lower(), p.name
    """
    raise NotImplementedError


def organize(folder):
    """Przenosi pliki do podfolderów nazwanych od rozszerzenia (małymi literami, bez kropki).

    Pliki bez rozszerzenia trafiają do folderu "inne".
    Zwraca słownik: nazwa_podfolderu -> liczba przeniesionych plików.
    Wskazówki: (folder / "txt").mkdir(exist_ok=True), p.rename(nowa_ścieżka)
    """
    raise NotImplementedError
