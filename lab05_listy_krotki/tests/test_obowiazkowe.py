"""Testy zadań obowiązkowych (★) – Lab 05."""
from helpers import ScriptTestCase


class TestZad1Zakupy(ScriptTestCase):
    def test_add_remove_sort_show(self):
        commands = "dodaj mleko\ndodaj chleb\ndodaj masło\nusuń chleb\nsortuj\npokaż\nkoniec\n"
        self.assertIn("masło, mleko", self.run_script("zad1_zakupy.py", commands))

    def test_show_keeps_insertion_order(self):
        commands = "dodaj jajka\ndodaj ser\npokaż\nkoniec\n"
        self.assertIn("jajka, ser", self.run_script("zad1_zakupy.py", commands))

    def test_remove_missing_item(self):
        output = self.run_script("zad1_zakupy.py", "usuń kawior\nkoniec\n").lower()
        self.assertIn("nie ma", output)

    def test_empty_list(self):
        output = self.run_script("zad1_zakupy.py", "pokaż\nkoniec\n").lower()
        self.assertIn("pusta", output)


class TestZad2Rezerwacje(ScriptTestCase):
    def test_full_session(self):
        commands = (
            "rezerwuj 2 5\n"
            "rezerwuj 1 1\n"
            "rezerwuj 2 5\n"
            "rezerwuj 9 9\n"
            "lista\n"
            "wolne\n"
            "koniec\n"
        )
        output = self.run_script("zad2_rezerwacje.py", commands)
        self.assertIn("(2, 5)", output)
        self.assertIn("zajęte", output.lower())
        self.assertIn("nie ma takiego miejsca", output.lower())
        self.assertIn("[(1, 1), (2, 5)]", output)
        self.assertIn("Wolne miejsca: 38", output)

    def test_cancel(self):
        commands = "rezerwuj 3 3\nanuluj 3 3\nlista\nwolne\nkoniec\n"
        output = self.run_script("zad2_rezerwacje.py", commands)
        self.assertIn("[]", output)
        self.assertIn("Wolne miejsca: 40", output)


class TestZad3Wycinki(ScriptTestCase):
    def test_all_operations(self):
        output = self.run_script("zad3_wycinki.py", "5 3 8 1 9 2\n")
        for expected in (
            "Pierwsze 3: [5, 3, 8]",
            "Ostatnie 3: [1, 9, 2]",
            "Co drugi: [5, 8, 9]",
            "Odwrócona: [2, 9, 1, 8, 3, 5]",
            "Posortowana: [1, 2, 3, 5, 8, 9]",
            "Min: 1, max: 9, suma: 28",
        ):
            self.assertIn(expected, output)
