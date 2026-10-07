"""Testy zadań dodatkowych (☆) – Lab 10."""
import unittest

from helpers import load

SAMPLE = {"table": "A", "currency": "euro", "code": "EUR",
          "rates": [{"no": "194/A/NBP/2026", "effectiveDate": "2026-10-06", "mid": 4.3699}]}


class TestZad4Kursy(unittest.TestCase):
    def setUp(self):
        self.m = load("zad4_kursy.py")

    def test_parse_rate(self):
        self.assertEqual(self.m.parse_rate(SAMPLE), ("EUR", "2026-10-06", 4.3699))

    def test_get_rate_builds_url_and_parses(self):
        calls = []

        def fake_fetch(url):
            calls.append(url)
            return SAMPLE

        self.assertEqual(self.m.get_rate("eur", fetch=fake_fetch), ("EUR", "2026-10-06", 4.3699))
        self.assertEqual(calls, ["https://api.nbp.pl/api/exchangerates/rates/a/eur/?format=json"])

    def test_convert(self):
        self.assertAlmostEqual(self.m.convert_pln(437, 4.37), 100)
