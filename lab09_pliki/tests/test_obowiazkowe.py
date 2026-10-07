"""Testy zadań obowiązkowych (★) – Lab 09."""
import json
import re
import tempfile
import unittest
from pathlib import Path

from helpers import load


class TempDirTestCase(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self._tmp.name)

    def tearDown(self):
        self._tmp.cleanup()


class TestZad1Logger(TempDirTestCase):
    def setUp(self):
        super().setUp()
        self.m = load("zad1_logger.py")
        self.path = self.dir / "app.log"

    def test_appends_lines_with_timestamp(self):
        self.m.log("start", self.path)
        self.m.log("koniec", self.path)
        lines = self.path.read_text(encoding="utf-8").splitlines()
        self.assertEqual(len(lines), 2)
        self.assertRegex(lines[0], r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} \| start$")
        self.assertTrue(lines[1].endswith("| koniec"))

    def test_read_log_and_count(self):
        for message in ("a", "b", "c"):
            self.m.log(message, self.path)
        entries = self.m.read_log(self.path)
        self.assertEqual(len(entries), 3)
        self.assertTrue(entries[2].endswith("| c"))
        self.assertFalse(entries[0].endswith("\n"))
        self.assertEqual(self.m.count_entries(self.path), 3)

    def test_missing_log_is_empty(self):
        self.assertEqual(self.m.read_log(self.dir / "brak.log"), [])
        self.assertEqual(self.m.count_entries(self.dir / "brak.log"), 0)


class TestZad2SumaZPliku(TempDirTestCase):
    def test_sums_numbers_and_counts_skipped(self):
        m = load("zad2_suma_z_pliku.py")
        path = self.dir / "liczby.txt"
        path.write_text("10\n2.5\n\nabc\n-3\n4,5\n", encoding="utf-8")
        self.assertEqual(m.sum_numbers(path), (9.5, 2))


class TestZad3Edytor(TempDirTestCase):
    def setUp(self):
        super().setUp()
        self.m = load("zad3_edytor.py")
        self.path = self.dir / "notatka.txt"

    def test_read_missing_file_returns_empty_text(self):
        self.assertEqual(self.m.read_text(self.path), "")

    def test_append_and_count_lines(self):
        self.m.append_line(self.path, "pierwsza")
        self.m.append_line(self.path, "druga")
        self.assertEqual(self.m.read_text(self.path), "pierwsza\ndruga\n")
        self.assertEqual(self.m.line_count(self.path), 2)

    def test_replace_word(self):
        self.path.write_text("kot i kot\npies\nkotlet\n", encoding="utf-8")
        self.assertEqual(self.m.replace_word(self.path, "kot", "pies"), 3)
        self.assertEqual(self.m.read_text(self.path), "pies i pies\npies\npieslet\n")


class TestZad4Json(TempDirTestCase):
    def setUp(self):
        super().setUp()
        self.m = load("zad4_json.py")
        self.path = self.dir / "kontakty.json"

    def test_save_and_load(self):
        contacts = {"Ola": "600100200", "Łukasz": "500600700"}
        self.m.save_contacts(contacts, self.path)
        self.assertEqual(json.loads(self.path.read_text(encoding="utf-8")), contacts)
        self.assertIn("Łukasz", self.path.read_text(encoding="utf-8"), "Użyj ensure_ascii=False")
        self.assertEqual(self.m.load_contacts(self.path), contacts)

    def test_load_missing_file(self):
        self.assertEqual(self.m.load_contacts(self.path), {})

    def test_add_contact_persists(self):
        self.m.add_contact(self.path, "Ola", "1")
        self.m.add_contact(self.path, "Adam", "2")
        self.assertEqual(self.m.load_contacts(self.path), {"Ola": "1", "Adam": "2"})
