"""Testy zadań obowiązkowych (★) – Lab 04."""
from helpers import ScriptTestCase, numbers


class TestZad1Srednia(ScriptTestCase):
    def test_three_grades(self):
        self.assertContainsNumber(self.run_script("zad1_srednia.py", "5\n4\n3\n\n"), 4.0)

    def test_half_grades(self):
        self.assertContainsNumber(self.run_script("zad1_srednia.py", "4.5\n5\n\n"), 4.75)

    def test_no_grades(self):
        self.assertIn("brak", self.run_script("zad1_srednia.py", "\n").lower())


class TestZad2Tabliczka(ScriptTestCase):
    def rows(self, n):
        output = self.run_script("zad2_tabliczka.py", f"{n}\n")
        return [numbers(line) for line in output.splitlines() if numbers(line)]

    def test_3x3(self):
        rows = self.rows(3)
        for expected in ([1, 2, 3], [2, 4, 6], [3, 6, 9]):
            self.assertIn(expected, rows, f"Brak wiersza {expected}, otrzymano: {rows}")

    def test_5x5_last_row(self):
        self.assertIn([5, 10, 15, 20, 25], self.rows(5))


class TestZad3SumaCyfr(ScriptTestCase):
    def test_12345(self):
        output = self.run_script("zad3_suma_cyfr.py", "12345\n")
        self.assertIn("Suma cyfr: 15", output)
        self.assertIn("Liczba cyfr: 5", output)

    def test_zero(self):
        output = self.run_script("zad3_suma_cyfr.py", "0\n")
        self.assertIn("Suma cyfr: 0", output)
        self.assertIn("Liczba cyfr: 1", output)

    def test_9009(self):
        output = self.run_script("zad3_suma_cyfr.py", "9009\n")
        self.assertIn("Suma cyfr: 18", output)
        self.assertIn("Liczba cyfr: 4", output)


class TestZad4Zgadywanka(ScriptTestCase):
    def play(self, guesses):
        return self.run_script("zad4_zgadywanka.py", guesses, env={"SEKRET": "42"}).lower()

    def test_hints_and_attempts(self):
        output = self.play("50\n25\n42\n")
        self.assertIn("za dużo", output)
        self.assertIn("za mało", output)
        self.assertIn("brawo", output)
        self.assertIn("3", output)

    def test_ignores_non_numbers(self):
        output = self.play("abc\n42\n")
        self.assertIn("nie jest liczb", output)
        self.assertIn("1 prób", output)
