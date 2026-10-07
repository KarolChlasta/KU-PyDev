"""Testy zadań dodatkowych (☆) – Lab 12."""
import unittest
from datetime import date

from helpers import load


class TestZad5Pesel(unittest.TestCase):
    def setUp(self):
        self.m = load("zad5_pesel.py")

    def test_valid(self):
        self.assertTrue(self.m.validate("44051401359"))
        self.assertEqual(self.m.birth_date("44051401359"), date(1944, 5, 14))
        self.assertEqual(self.m.sex("44051401359"), "M")

    def test_born_in_2000s(self):
        self.assertEqual(self.m.birth_date("02291700007"), date(2002, 9, 17))
        self.assertEqual(self.m.sex("02291700007"), "K")

    def test_error_hierarchy(self):
        cases = (("123", self.m.PeselLengthError),
                 ("4405140135X", self.m.PeselDigitsError),
                 ("44051401358", self.m.PeselChecksumError))
        for pesel, error in cases:
            with self.assertRaises(error):
                self.m.validate(pesel)
            self.assertTrue(issubclass(error, self.m.PeselError))
