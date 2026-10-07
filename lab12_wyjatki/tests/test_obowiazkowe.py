"""Testy zadań obowiązkowych (★) – Lab 12."""
import tempfile
import unittest
from pathlib import Path

from helpers import load


class TestZad1BezpiecznyKalkulator(unittest.TestCase):
    def setUp(self):
        self.m = load("zad1_kalkulator.py")

    def test_results(self):
        self.assertEqual(self.m.calculate("7", "/", "2"), "3.5")
        self.assertEqual(self.m.calculate("2", "**", "10"), "1024.0")

    def test_errors_become_messages(self):
        self.assertEqual(self.m.calculate("1", "/", "0"), "Błąd: dzielenie przez zero")
        self.assertEqual(self.m.calculate("abc", "+", "1"), "Błąd: to nie jest liczba")
        self.assertEqual(self.m.calculate("1", "%%", "1"), "Błąd: nieznany operator")
        self.assertEqual(self.m.calculate("10", "**", "1000"), "Błąd: wynik za duży")


class TestZad2Walidacja(unittest.TestCase):
    def setUp(self):
        self.m = load("zad2_walidacja.py")

    def test_parse_age_ok(self):
        self.assertEqual(self.m.parse_age(" 20 "), 20)

    def test_parse_age_raises_value_error_with_message(self):
        for text, fragment in (("abc", "liczb"), ("-1", "ujemn"), ("151", "150")):
            with self.assertRaises(ValueError) as ctx:
                self.m.parse_age(text)
            self.assertIn(fragment, str(ctx.exception).lower())

    def test_read_int_repeats_until_valid(self):
        answers = iter(["dwa", "0", "11", "7"])
        messages = []
        value = self.m.read_int("Ocena: ", 1, 10, input_func=lambda prompt: next(answers), output=messages.append)
        self.assertEqual(value, 7)
        self.assertEqual(len(messages), 3)
        self.assertIn("liczbę całkowitą", messages[0])
        self.assertIn("1–10", messages[1])


class TestZad3Pliki(unittest.TestCase):
    def setUp(self):
        self.m = load("zad3_pliki.py")
        self._tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self._tmp.name)

    def tearDown(self):
        self._tmp.cleanup()

    def test_read_config(self):
        path = self.dir / "app.cfg"
        path.write_text("# komentarz\nhost = localhost\n\nport=8080\n", encoding="utf-8")
        self.assertEqual(self.m.read_config(path), {"host": "localhost", "port": "8080"})

    def test_read_config_missing_file(self):
        self.assertEqual(self.m.read_config(self.dir / "brak.cfg"), {})

    def test_read_config_bad_line(self):
        path = self.dir / "zly.cfg"
        path.write_text("host=localhost\nport 8080\n", encoding="utf-8")
        with self.assertRaises(ValueError) as ctx:
            self.m.read_config(path)
        self.assertIn("2", str(ctx.exception))

    def test_finally_runs_even_on_error(self):
        log = []
        with self.assertRaises(FileNotFoundError):
            self.m.read_first_line(self.dir / "brak.txt", log)
        self.assertEqual(log, ["start", "koniec"])

    def test_finally_runs_on_success(self):
        path = self.dir / "a.txt"
        path.write_text("pierwsza\ndruga\n", encoding="utf-8")
        log = []
        self.assertEqual(self.m.read_first_line(path, log), "pierwsza")
        self.assertEqual(log, ["start", "koniec"])


class TestZad4WlasneWyjatki(unittest.TestCase):
    def setUp(self):
        self.m = load("zad4_wyjatki.py")

    def test_withdraw_ok(self):
        self.assertEqual(self.m.withdraw(100, 30), 70)

    def test_insufficient_funds(self):
        with self.assertRaises(self.m.InsufficientFundsError) as ctx:
            self.m.withdraw(100, 150)
        error = ctx.exception
        self.assertIsInstance(error, Exception)
        self.assertEqual((error.balance, error.amount), (100, 150))
        self.assertIn("100", str(error))
        self.assertIn("150", str(error))

    def test_non_positive_amount(self):
        with self.assertRaises(ValueError):
            self.m.withdraw(100, 0)

    def test_percent_assertion(self):
        self.assertEqual(self.m.percent(1, 4), 25)
        with self.assertRaises(AssertionError):
            self.m.percent(1, 0)
