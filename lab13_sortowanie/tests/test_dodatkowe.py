"""Testy zadań dodatkowych (☆) – Lab 13."""
import random
import unittest
from unittest import mock

from helpers import load


class TestZad5Szybsze(unittest.TestCase):
    def setUp(self):
        self.m = load("zad5_szybsze.py")

    def check(self, sort):
        rng = random.Random(5)
        cases = [[], [1], [2, 1], [3, 1, 2, 3, 1]] + [[rng.randint(-1000, 1000) for _ in range(300)] for _ in range(5)]
        expected = [sorted(values) for values in cases]
        with mock.patch("builtins.sorted", side_effect=AssertionError("Nie używaj sorted()")):
            for values, want in zip(cases, expected):
                original = list(values)
                self.assertEqual(sort(values), want)
                self.assertEqual(values, original)

    def test_insertion_sort(self):
        self.check(self.m.insertion_sort)

    def test_merge_sort(self):
        self.check(self.m.merge_sort)
