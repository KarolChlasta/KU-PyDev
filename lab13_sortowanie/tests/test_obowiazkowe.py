"""Testy zadań obowiązkowych (★) – Lab 13."""
import random
import unittest
from unittest import mock

from helpers import load

CASES = [[], [1], [2, 1], [5, 3, 8, 1, 9, 2], [3, 3, 1, 1, 2], [-4, 0, -10, 7], list(range(20, 0, -1))]


class CountingList(list):
    """Lista, która liczy odczyty elementów po indeksie."""

    def __init__(self, *args):
        super().__init__(*args)
        self.reads = 0

    def __getitem__(self, index):
        self.reads += 1
        return super().__getitem__(index)


class TestZad1Sortowania(unittest.TestCase):
    def setUp(self):
        self.m = load("zad1_sortowania.py")

    def test_bubble_sort(self):
        self._check_sort(self.m.bubble_sort)

    def test_selection_sort(self):
        self._check_sort(self.m.selection_sort)

    def _check_sort(self, sort):
        rng = random.Random(13)
        cases = CASES + [[rng.randint(-100, 100) for _ in range(50)] for _ in range(5)]
        expected = [sorted(values) for values in cases]
        with mock.patch("builtins.sorted", side_effect=AssertionError("Nie używaj sorted() – napisz algorytm!")):
            for values, want in zip(cases, expected):
                original = list(values)
                self.assertEqual(sort(values), want)
                self.assertEqual(values, original, "Funkcja nie może zmieniać listy wejściowej")


class TestZad2Wyszukiwanie(unittest.TestCase):
    def setUp(self):
        self.m = load("zad2_wyszukiwanie.py")

    def test_linear_search(self):
        values = [7, 3, 9, 3]
        self.assertEqual(self.m.linear_search(values, 3), 1)
        self.assertEqual(self.m.linear_search(values, 5), -1)
        self.assertEqual(self.m.linear_search([], 5), -1)

    def test_binary_search_finds_every_element(self):
        values = list(range(0, 100, 3))
        for i, value in enumerate(values):
            self.assertEqual(self.m.binary_search(values, value), i)
        for missing in (-1, 1, 100, 1000):
            self.assertEqual(self.m.binary_search(values, missing), -1)
        self.assertEqual(self.m.binary_search([], 1), -1)

    def test_binary_search_is_logarithmic(self):
        values = CountingList(range(1_000_000))
        self.assertEqual(self.m.binary_search(values, 765_432), 765_432)
        self.assertGreater(values.reads, 0, "Wyszukiwanie binarne ma czytać elementy po indeksie, nie używać index() ani in")
        self.assertLessEqual(values.reads, 25, f"Za dużo odczytów: {values.reads} – to nie jest wyszukiwanie binarne")

    def test_binary_search_steps(self):
        values = list(range(1_000_000))
        self.assertLessEqual(self.m.binary_search_steps(values, 765_432), 20)
        self.assertLessEqual(self.m.binary_search_steps(values, -5), 21)
        self.assertEqual(self.m.binary_search_steps([4], 4), 1)


class TestZad3Biblioteka(unittest.TestCase):
    def setUp(self):
        self.m = load("zad3_biblioteka.py")
        self.books = self.m.BOOKS

    def titles(self, books):
        return [book["title"] for book in books]

    def test_sort_by_year(self):
        result = self.m.sort_books(self.books, "year")
        years = [book["year"] for book in result]
        self.assertEqual(years, sorted(years))
        self.assertEqual(result[0]["title"], "Pan Tadeusz")

    def test_sort_descending_by_pages(self):
        pages = [book["pages"] for book in self.m.sort_books(self.books, "pages", descending=True)]
        self.assertEqual(pages, sorted(pages, reverse=True))

    def test_original_not_modified(self):
        before = list(self.books)
        self.m.sort_books(self.books, "title")
        self.assertEqual(self.books, before)

    def test_unknown_key(self):
        with self.assertRaises(ValueError):
            self.m.sort_books(self.books, "isbn")

    def test_author_then_year(self):
        lem = [b for b in self.m.sort_by_author_then_year(self.books) if b["author"] == "Stanisław Lem"]
        self.assertEqual(self.titles(lem), ["Solaris", "Cyberiada"])

    def test_newest(self):
        self.assertEqual(self.titles(self.m.newest(self.books, 2)),
                         ["Python. Instrukcje dla programisty", "Ostatnie życzenie"])


class TestZad4Pomiar(unittest.TestCase):
    def test_measurements(self):
        m = load("zad4_pomiar.py")
        seconds = m.time_function(m.bubble_sort, 200)
        self.assertIsInstance(seconds, float)
        self.assertGreater(seconds, 0)
        self.assertGreater(m.growth_ratio(m.bubble_sort, 200), 0)
