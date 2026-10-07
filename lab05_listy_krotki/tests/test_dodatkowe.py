"""Testy zadań dodatkowych (☆) – Lab 05."""
from helpers import ScriptTestCase


class TestZad4ZnajdzPare(ScriptTestCase):
    def test_full_game(self):
        moves = "0 1\n0 4\n1 5\n2 6\n3 7\n"
        output = self.run_script("zad4_znajdz_pare.py", moves, env={"BEZ_TASOWANIA": "1"}).lower()
        self.assertIn("pudło", output)
        self.assertIn("para", output)
        self.assertIn("5 ruch", output)

    def test_same_card_twice_is_rejected(self):
        moves = "0 0\n0 4\n1 5\n2 6\n3 7\n"
        output = self.run_script("zad4_znajdz_pare.py", moves, env={"BEZ_TASOWANIA": "1"}).lower()
        self.assertIn("dwie różne", output)
