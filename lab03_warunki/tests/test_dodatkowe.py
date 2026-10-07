"""Testy zadań dodatkowych (☆) – Lab 03."""
from helpers import ScriptTestCase


class TestZad5Trojkat(ScriptTestCase):
    def kind(self, a, b, c):
        return self.run_script("zad5_trojkat.py", f"{a}\n{b}\n{c}\n").lower()

    def test_impossible(self):
        self.assertIn("nie da się", self.kind(1, 2, 10))

    def test_equilateral(self):
        self.assertIn("równoboczny", self.kind(3, 3, 3))

    def test_isosceles(self):
        self.assertIn("równoramienny", self.kind(5, 5, 8))

    def test_scalene_right(self):
        output = self.kind(3, 4, 5)
        self.assertIn("różnoboczny", output)
        self.assertIn("prostokątny", output)
