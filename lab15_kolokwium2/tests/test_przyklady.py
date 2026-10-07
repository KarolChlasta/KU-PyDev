"""Testy przykładowych zadań kolokwialnych – Kolokwium II."""
import tempfile
import unittest
from pathlib import Path

from helpers import load


class CountingList(list):
    def __init__(self, *args):
        super().__init__(*args)
        self.reads = 0

    def __getitem__(self, index):
        self.reads += 1
        return super().__getitem__(index)


class TestPrzyklad1Wyniki(unittest.TestCase):
    def setUp(self):
        self.m = load("przyklad1_wyniki.py")
        self._tmp = tempfile.TemporaryDirectory()
        self.path = Path(self._tmp.name) / "wyniki.csv"

    def tearDown(self):
        self._tmp.cleanup()

    def test_load_skips_bad_lines(self):
        self.path.write_text("Ala;45\nJan;abc\n\nOla;38.5\nbez średnika\n", encoding="utf-8")
        self.assertEqual(self.m.load_scores(self.path), ({"Ala": 45.0, "Ola": 38.5}, 2))

    def test_missing_file_raises_custom_error(self):
        with self.assertRaises(self.m.ScoresFileError) as ctx:
            self.m.load_scores(self.path)
        self.assertIn("wyniki.csv", str(ctx.exception))


class TestPrzyklad2Ranking(unittest.TestCase):
    def setUp(self):
        self.m = load("przyklad2_ranking.py")

    def test_sort_by_score_then_name(self):
        results = [("Ola", 38), ("Ala", 45), ("Ewa", 45), ("Jan", 20)]
        self.assertEqual(self.m.rank(results), [("Ala", 45), ("Ewa", 45), ("Ola", 38), ("Jan", 20)])
        self.assertEqual(results[0], ("Ola", 38), "Nie zmieniaj listy wejściowej")

    def test_binary_search_names(self):
        names = CountingList(f"student{i:07d}" for i in range(1_000_000))
        self.assertEqual(self.m.find(names, "student0765432"), 765_432)
        self.assertEqual(self.m.find(names, "zzz"), -1)
        self.assertLessEqual(names.reads, 50)
        self.assertGreater(names.reads, 0)
