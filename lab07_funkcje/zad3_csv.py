"""Lab 07 – Zadanie 3 (★): Analiza danych z pliku CSV.

Plik dane/oceny.csv ma nagłówek:  imie,nazwisko,ocena
Ocena studenta to krotka ("Imię Nazwisko", ocena_float).
"""
import csv


def load_grades(path):
    """Wczytuje plik CSV i zwraca listę krotek, np. [("Anna Kowalska", 4.5), ...].

    Wskazówka:
        with open(path, encoding="utf-8", newline="") as f:
            for row in csv.DictReader(f):
                row["imie"], row["nazwisko"], row["ocena"]
    """
    raise NotImplementedError


def average(grades):
    """Średnia ocen; dla pustej listy zwraca 0.0."""
    raise NotImplementedError


def best(grades):
    """Zwraca krotkę studenta z najwyższą oceną (przy remisie – pierwszego z listy)."""
    raise NotImplementedError


def count_passing(grades, threshold=3.0):
    """Ile ocen jest >= threshold. Parametr ma wartość domyślną 3.0."""
    raise NotImplementedError


def main():
    grades = load_grades("dane/oceny.csv")
    print(f"Liczba studentów: {len(grades)}")
    print(f"Średnia: {average(grades):.2f}")
    print(f"Najlepszy wynik: {best(grades)}")
    print(f"Zaliczyło: {count_passing(grades)}")


if __name__ == "__main__":
    main()
