"""Testy zadań dodatkowych (☆) – Lab 07."""
import unittest

from helpers import load

fun = load("zad5_lambdy.py")


class TestZad5Lambdy(unittest.TestCase):
    def test_apply_to_all(self):
        self.assertEqual(fun.apply_to_all(abs, [-1, 2, -3]), [1, 2, 3])
        self.assertEqual(fun.apply_to_all(lambda x: x * x, [1, 2, 3]), [1, 4, 9])

    def test_sort_by_last_name(self):
        names = ["Jan Nowak", "Anna Kowalska", "Ewa Adamska"]
        self.assertEqual(fun.sort_by_last_name(names), ["Ewa Adamska", "Anna Kowalska", "Jan Nowak"])

    def test_filter_even(self):
        self.assertEqual(fun.filter_even([1, 2, 3, 4, 5, 6]), [2, 4, 6])

    def test_global_counter(self):
        fun.counter = 0
        fun.increment()
        fun.increment()
        self.assertEqual(fun.counter, 2)
