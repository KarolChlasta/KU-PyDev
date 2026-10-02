"""Testy zadań obowiązkowych (★) – Lab 02."""
from helpers import ScriptTestCase


class TestZad1Kalkulator(ScriptTestCase):
    def test_all_operations_8_and_2(self):
        output = self.run_script("zad1_kalkulator.py", "8\n2\n")
        for expected in (10, 6, 16, 4, 64):
            self.assertContainsNumber(output, expected)

    def test_all_operations_7_and_2(self):
        output = self.run_script("zad1_kalkulator.py", "7\n2\n")
        # +, -, *, /, //, %, **
        for expected in (9, 5, 14, 3.5, 3, 1, 49):
            self.assertContainsNumber(output, expected)


class TestZad2Temperatura(ScriptTestCase):
    def test_body_temperature_and_boiling_point(self):
        output = self.run_script("zad2_temperatura.py", "37\n212\n")
        self.assertContainsNumber(output, 98.6)
        self.assertContainsNumber(output, 100)

    def test_minus_forty_is_the_same(self):
        output = self.run_script("zad2_temperatura.py", "-40\n-40\n")
        self.assertContainsNumber(output, -40)


class TestZad3Waluty(ScriptTestCase):
    def test_425_pln(self):
        output = self.run_script("zad3_waluty.py", "425\n")
        self.assertContainsNumber(output, 100.00)
        self.assertContainsNumber(output, 111.84)

    def test_1000_pln(self):
        output = self.run_script("zad3_waluty.py", "1000\n")
        self.assertContainsNumber(output, 235.29)
        self.assertContainsNumber(output, 263.16)


class TestZad4Czas(ScriptTestCase):
    def test_3725_seconds(self):
        self.assertIn("1 h 2 min 5 s", self.run_script("zad4_czas.py", "3725\n"))

    def test_almost_a_day(self):
        self.assertIn("23 h 59 min 59 s", self.run_script("zad4_czas.py", "86399\n"))

    def test_less_than_a_minute(self):
        self.assertIn("0 h 0 min 59 s", self.run_script("zad4_czas.py", "59\n"))
