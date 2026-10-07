"""Lab 13 – Zadanie 4 (★): Eksperyment – jak rośnie czas sortowania?

Po uruchomieniu (python zad4_pomiar.py) uzupełnij w AI.md tabelę wyników i wnioski.
"""
import random
import time

from zad1_sortowania import bubble_sort, selection_sort


def time_function(sort_func, n, repeats=3):
    """NAJKRÓTSZY z `repeats` czasów sortowania losowej listy n liczb (time.perf_counter)."""
    raise NotImplementedError


def growth_ratio(sort_func, n):
    """Iloraz czasu dla 2n i dla n. Dla O(n²) spodziewaj się ok. 4, dla O(n log n) – nieco ponad 2."""
    raise NotImplementedError


if __name__ == "__main__":
    print(f"{'n':>6} {'bąbelkowe':>12} {'wybieranie':>12} {'sorted()':>12}")
    for n in (500, 1000, 2000, 4000):
        row = [time_function(f, n) for f in (bubble_sort, selection_sort, sorted)]
        print(f"{n:>6} " + " ".join(f"{t:>12.5f}" for t in row))
