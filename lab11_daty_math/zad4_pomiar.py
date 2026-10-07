"""Lab 11 – Zadanie 4 (★): Pomiar czasu wykonania (moduł time)."""
import time


def sum_loop(n):
    """Suma 1 + 2 + ... + n liczona pętlą."""
    raise NotImplementedError


def sum_formula(n):
    """Ta sama suma ze wzoru Gaussa: n(n+1)/2 – wynik jako int (użyj //)."""
    raise NotImplementedError


def measure(func, *args):
    """Wywołuje func(*args) i zwraca krotkę (wynik, czas_w_sekundach).

    Do pomiaru użyj time.perf_counter() przed i po wywołaniu.
    """
    raise NotImplementedError


if __name__ == "__main__":
    for n in (10_000, 100_000, 1_000_000):
        _, t_loop = measure(sum_loop, n)
        _, t_formula = measure(sum_formula, n)
        print(f"n = {n:>9}: pętla {t_loop:.6f} s, wzór {t_formula:.6f} s")
