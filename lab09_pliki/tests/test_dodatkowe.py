"""Testy zadań dodatkowych (☆) – Lab 09."""
import tempfile
import unittest
from pathlib import Path

from helpers import load


class TestZad5Menedzer(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self._tmp.name)
        for name in ("a.txt", "b.TXT", "foto.jpg", "raport.pdf", "README"):
            (self.dir / name).write_text("x", encoding="utf-8")
        self.m = load("zad5_menedzer.py")

    def tearDown(self):
        self._tmp.cleanup()

    def test_find_by_extension_ignores_case(self):
        self.assertEqual(self.m.find_by_extension(self.dir, ".txt"), ["a.txt", "b.TXT"])

    def test_organize(self):
        summary = self.m.organize(self.dir)
        self.assertEqual(summary, {"txt": 2, "jpg": 1, "pdf": 1, "inne": 1})
        self.assertTrue((self.dir / "txt" / "a.txt").exists())
        self.assertTrue((self.dir / "inne" / "README").exists())
        self.assertFalse((self.dir / "foto.jpg").exists())
