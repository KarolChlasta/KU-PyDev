"""Testy zadań obowiązkowych (★) – Lab 11."""
import statistics
import unittest
from datetime import date

from helpers import load


class TestZad1Wydarzenia(unittest.TestCase):
    def setUp(self):
        self.m = load("zad1_wydarzenia.py")
        self.today = date(2026, 12, 22)

    def test_parse_date(self):
        self.assertEqual(self.m.parse_date("24.12.2026"), date(2026, 12, 24))

    def test_days_until(self):
        self.assertEqual(self.m.days_until(date(2026, 12, 24), self.today), 2)
        self.assertEqual(self.m.days_until(date(2027, 1, 26), self.today), 35)
        self.assertEqual(self.m.days_until(date(2026, 12, 20), self.today), -2)

    def test_describe(self):
        self.assertEqual(self.m.describe("Wigilia", date(2026, 12, 24), self.today), "Wigilia: za 2 dni")
        self.assertEqual(self.m.describe("Lab 11", self.today, self.today), "Lab 11: dziś!")
        self.assertEqual(self.m.describe("Lab 10", date(2026, 12, 15), self.today), "Lab 10: 7 dni temu")

    def test_upcoming_sorted_without_past(self):
        events = {"Kolokwium II": date(2027, 1, 26), "Wigilia": date(2026, 12, 24),
                  "Lab 10": date(2026, 12, 15), "Lab 11": date(2026, 12, 22)}
        self.assertEqual(self.m.upcoming(events, self.today),
                         [("Lab 11", 0), ("Wigilia", 2), ("Kolokwium II", 35)])


class TestZad2Strefy(unittest.TestCase):
    def setUp(self):
        self.m = load("zad2_strefy.py")

    def test_winter(self):
        self.assertEqual(self.m.convert("2026-12-22 10:00", "Europe/Warsaw", "America/New_York"), "2026-12-22 04:00")
        self.assertEqual(self.m.convert("2026-12-22 10:00", "Europe/Warsaw", "Asia/Tokyo"), "2026-12-22 18:00")

    def test_summer_time(self):
        self.assertEqual(self.m.convert("2026-07-01 10:00", "Europe/Warsaw", "UTC"), "2026-07-01 08:00")

    def test_date_change(self):
        self.assertEqual(self.m.convert("2026-12-31 20:00", "Europe/Warsaw", "Australia/Sydney"), "2027-01-01 06:00")

    def test_utc_offset(self):
        self.assertEqual(self.m.utc_offset("Europe/Warsaw", "2026-12-22 10:00"), 1)
        self.assertEqual(self.m.utc_offset("Europe/Warsaw", "2026-07-01 10:00"), 2)
        self.assertEqual(self.m.utc_offset("Asia/Kolkata", "2026-07-01 10:00"), 5.5)


class TestZad3Statystyka(unittest.TestCase):
    DATA = [2, 4, 4, 4, 5, 5, 7, 9]

    def setUp(self):
        self.m = load("zad3_statystyka.py")

    def test_mean(self):
        self.assertAlmostEqual(self.m.mean(self.DATA), statistics.mean(self.DATA))

    def test_median_even_and_odd(self):
        self.assertAlmostEqual(self.m.median(self.DATA), statistics.median(self.DATA))
        self.assertEqual(self.m.median([3, 1, 2]), 2)

    def test_median_does_not_modify_input(self):
        data = [3, 1, 2]
        self.m.median(data)
        self.assertEqual(data, [3, 1, 2])

    def test_std_dev_sample(self):
        self.assertAlmostEqual(self.m.std_dev(self.DATA), statistics.stdev(self.DATA))


class TestZad4Pomiar(unittest.TestCase):
    def setUp(self):
        self.m = load("zad4_pomiar.py")

    def test_sums_agree(self):
        for n in (0, 1, 10, 1000):
            self.assertEqual(self.m.sum_loop(n), n * (n + 1) // 2)
            self.assertEqual(self.m.sum_formula(n), n * (n + 1) // 2)

    def test_measure_returns_result_and_time(self):
        result, seconds = self.m.measure(self.m.sum_loop, 10000)
        self.assertEqual(result, 50005000)
        self.assertIsInstance(seconds, float)
        self.assertGreaterEqual(seconds, 0)
