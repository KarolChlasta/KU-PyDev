"""Testy zadań obowiązkowych (★) – Lab 03."""
from helpers import ScriptTestCase


class TestZad1Inwestycja(ScriptTestCase):
    def advice(self, amount, years, risk):
        return self.run_script("zad1_inwestycja.py", f"{amount}\n{years}\n{risk}\n").lower()

    def test_small_amount_needs_safety_cushion(self):
        self.assertIn("poduszk", self.advice(500, 10, "wysokie"))

    def test_short_horizon_means_deposit(self):
        self.assertIn("lokat", self.advice(10000, 1, "wysokie"))

    def test_low_risk_means_bonds(self):
        self.assertIn("obligacj", self.advice(10000, 5, "niskie"))

    def test_medium_risk_means_mixed_fund(self):
        self.assertIn("mieszany", self.advice(10000, 5, "średnie"))

    def test_high_risk_long_horizon_means_etf(self):
        self.assertIn("etf", self.advice(10000, 10, "wysokie"))

    def test_high_risk_short_horizon_means_mixed_fund(self):
        self.assertIn("mieszany", self.advice(10000, 3, "wysokie"))

    def test_risk_is_case_and_space_insensitive(self):
        self.assertIn("obligacj", self.advice(10000, 5, "  NISKIE "))

    def test_unknown_risk_profile(self):
        self.assertIn("nieznany", self.advice(10000, 5, "ogromne"))


class TestZad2Kalkulator(ScriptTestCase):
    def test_multiplication(self):
        self.assertContainsNumber(self.run_script("zad2_kalkulator.py", "8\n*\n2\n"), 16)

    def test_division(self):
        self.assertContainsNumber(self.run_script("zad2_kalkulator.py", "7\n/\n2\n"), 3.5)

    def test_division_by_zero(self):
        self.assertIn("zero", self.run_script("zad2_kalkulator.py", "1\n/\n0\n").lower())

    def test_unknown_operator(self):
        self.assertIn("nieznany", self.run_script("zad2_kalkulator.py", "1\n?\n2\n").lower())


class TestZad3RokPrzestepny(ScriptTestCase):
    def check(self, year, leap):
        output = self.run_script("zad3_przestepny.py", f"{year}\n").lower()
        self.assertIn("przestępny", output)
        if leap:
            self.assertNotIn("nie jest", output, f"Rok {year} JEST przestępny")
        else:
            self.assertIn("nie jest", output, f"Rok {year} NIE jest przestępny")

    def test_2024_leap(self):
        self.check(2024, True)

    def test_2023_not_leap(self):
        self.check(2023, False)

    def test_1900_not_leap(self):
        self.check(1900, False)

    def test_2000_leap(self):
        self.check(2000, True)


class TestZad4Ocena(ScriptTestCase):
    def check(self, points, grade):
        output = self.run_script("zad4_ocena.py", f"{points}\n")
        self.assertContainsNumber(output, grade)

    def test_92_is_5(self):
        self.check(92, 5)

    def test_91_is_4_5(self):
        self.check(91, 4.5)

    def test_80_is_4(self):
        self.check(80, 4)

    def test_70_is_3_5(self):
        self.check(70, 3.5)

    def test_61_is_3(self):
        self.check(61, 3)

    def test_60_is_2(self):
        self.check(60, 2)
