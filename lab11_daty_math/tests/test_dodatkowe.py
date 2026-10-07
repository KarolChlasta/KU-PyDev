"""Testy zadań dodatkowych (☆) – Lab 11."""
import unittest
from datetime import date

from helpers import load


class TestZad5Kalendarz(unittest.TestCase):
    def setUp(self):
        self.m = load("zad5_kalendarz.py")

    def test_weekday_name(self):
        self.assertEqual(self.m.weekday_name(date(2026, 12, 22)), "wtorek")
        self.assertEqual(self.m.weekday_name(date(2027, 1, 8)), "piątek")

    def test_is_weekend(self):
        self.assertTrue(self.m.is_weekend(date(2026, 12, 26)))
        self.assertFalse(self.m.is_weekend(date(2026, 12, 22)))

    def test_working_days(self):
        self.assertEqual(self.m.working_days(date(2026, 12, 21), date(2026, 12, 27)), 5)
        self.assertEqual(self.m.working_days(date(2026, 12, 26), date(2026, 12, 26)), 0)
