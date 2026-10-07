"""Testy zadań dodatkowych (☆) – Lab 06."""
from helpers import ScriptTestCase


class TestZad5Znajomi(ScriptTestCase):
    def test_set_operations(self):
        output = self.run_script("zad5_znajomi.py", "Ala Ola Jan Ewa\nJan Ewa Piotr\n")
        self.assertIn("Wspólni: Ewa, Jan", output)
        self.assertIn("Wszyscy: Ala, Ewa, Jan, Ola, Piotr", output)
        self.assertIn("Tylko pierwszej osoby: Ala, Ola", output)
        self.assertIn("Tylko jednej z osób: Ala, Ola, Piotr", output)
