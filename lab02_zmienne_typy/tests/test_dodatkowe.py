"""Testy zadań dodatkowych (☆) – Lab 02."""
from helpers import ScriptTestCase, numbers


def contains_sequence(values, sequence):
    n = len(sequence)
    return any(values[i:i + n] == sequence for i in range(len(values) - n + 1))


class TestZad5Fibonacci(ScriptTestCase):
    def test_first_10(self):
        values = numbers(self.run_script("zad5_fibonacci.py", "10\n"))
        self.assertTrue(contains_sequence(values, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]),
                        f"Oczekiwano 10 pierwszych wyrazów ciągu, otrzymano: {values}")

    def test_first_15(self):
        values = numbers(self.run_script("zad5_fibonacci.py", "15\n"))
        self.assertTrue(contains_sequence(values, [144, 233, 377]),
                        f"Brak końcówki 144 233 377, otrzymano: {values}")
