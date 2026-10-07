"""Testy zadań obowiązkowych (★) – Lab 14."""
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from helpers import LAB_DIR, load

SAMPLE = {
    "timezone": "Europe/Warsaw",
    "daily": {"time": ["2027-01-19", "2027-01-20", "2027-01-21"], "temperature_2m_max": [-2.5, 3.0, 1.5]},
}
FORECAST = [{"day": "2027-01-19", "temp": -2.5}, {"day": "2027-01-20", "temp": 3.0}, {"day": "2027-01-21", "temp": 1.5}]


class TestZad1Pogoda(unittest.TestCase):
    def setUp(self):
        self.m = load("zad1_pogoda.py")

    def test_celsius_to_fahrenheit(self):
        self.assertAlmostEqual(self.m.celsius_to_fahrenheit(0), 32)
        self.assertAlmostEqual(self.m.celsius_to_fahrenheit(-40), -40)

    def test_classify_boundaries(self):
        cases = {-0.1: "mróz", 0: "zimno", 9.9: "zimno", 10: "umiarkowanie",
                 19.9: "umiarkowanie", 20: "ciepło", 27.9: "ciepło", 28: "upał"}
        for temp, label in cases.items():
            self.assertEqual(self.m.classify(temp), label, f"classify({temp})")

    def test_parse_forecast(self):
        self.assertEqual(self.m.parse_forecast(SAMPLE), FORECAST)

    def test_average_and_warmest(self):
        self.assertAlmostEqual(self.m.average_temperature(FORECAST), 2 / 3)
        self.assertEqual(self.m.warmest_day(FORECAST), ("2027-01-20", 3.0))

    def test_empty_forecast_raises(self):
        with self.assertRaises(ValueError):
            self.m.warmest_day([])
        with self.assertRaises(ValueError):
            self.m.average_temperature([])

    def test_build_url(self):
        self.assertEqual(
            self.m.build_url(52.23, 21.01, 3),
            "https://api.open-meteo.com/v1/forecast?latitude=52.23&longitude=21.01"
            "&daily=temperature_2m_max&timezone=Europe%2FWarsaw&forecast_days=3",
        )

    def test_fetch_forecast_uses_mocked_http(self):
        with mock.patch.object(self.m, "get_json", return_value=SAMPLE) as fake:
            self.assertEqual(self.m.fetch_forecast(52.23, 21.01, 3), FORECAST)
        fake.assert_called_once_with(self.m.build_url(52.23, 21.01, 3))


class TestZad2MojeTesty(unittest.TestCase):
    """Uruchamia TWOJE testy z test_moje_arytmetyka.py na poprawnym module i na mutantach."""

    MUTANTS = Path(__file__).resolve().parent / "mutanty"
    STUDENT_FILE = LAB_DIR / "test_moje_arytmetyka.py"
    MIN_TESTS = 8

    def run_student_tests(self, implementation):
        with tempfile.TemporaryDirectory() as tmp:
            shutil.copy(self.STUDENT_FILE, Path(tmp) / "test_moje_arytmetyka.py")
            shutil.copy(self.MUTANTS / implementation / "arytmetyka.py", Path(tmp) / "arytmetyka.py")
            result = subprocess.run(
                [sys.executable, "-m", "unittest", "test_moje_arytmetyka"],
                cwd=tmp, capture_output=True, text=True, encoding="utf-8", timeout=60,
            )
        match = re.search(r"Ran (\d+) test", result.stderr)
        return result.returncode == 0, int(match.group(1)) if match else 0, result.stderr

    def require_enough_tests(self):
        self.assertTrue(self.STUDENT_FILE.exists(), "Brak pliku test_moje_arytmetyka.py")
        passed, count, report = self.run_student_tests("oryginal")
        self.assertGreaterEqual(count, self.MIN_TESTS, f"Napisz co najmniej {self.MIN_TESTS} testów (jest {count})")
        self.assertTrue(passed, f"Twoje testy muszą przechodzić na POPRAWNYM module:\n{report}")

    def check_mutant(self, name, hint):
        self.require_enough_tests()
        passed, _, _ = self.run_student_tests(name)
        self.assertFalse(passed, f"Mutant {name} przeżył – Twoje testy nie wykryły błędu. Podpowiedź: {hint}")

    def test_suite_passes_on_correct_module(self):
        self.require_enough_tests()

    def test_kills_m1(self):
        self.check_mutant("m1_gcd_zwraca_zero", "sprawdź wynik gcd")

    def test_kills_m2(self):
        self.check_mutant("m2_lcm_bez_gcd", "sprawdź lcm liczb, które mają wspólny dzielnik")

    def test_kills_m3(self):
        self.check_mutant("m3_jedynka_pierwsza", "czy 1 jest liczbą pierwszą?")

    def test_kills_m4(self):
        self.check_mutant("m4_kwadraty_pierwsze", "sprawdź kwadraty liczb pierwszych, np. 4, 9, 25")

    def test_kills_m5(self):
        self.check_mutant("m5_silnia_o_jeden_za_malo", "sprawdź silnię kilku liczb")

    def test_kills_m6(self):
        self.check_mutant("m6_silnia_ujemna_bez_bledu", "co ma się stać dla factorial(-1)? (assertRaises)")
