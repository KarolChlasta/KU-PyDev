"""Testy zadań dodatkowych (☆) – Lab 01."""
from helpers import ScriptTestCase


class TestZad4KategoriaBMI(ScriptTestCase):
    def check_category(self, weight, height, category):
        output = self.run_script("zad4_bmi_kategoria.py", f"{weight}\n{height}\n").lower()
        self.assertIn(category, output)

    def test_underweight(self):
        self.check_category(50, 1.80, "niedowaga")      # BMI 15.43

    def test_normal(self):
        self.check_category(70, 1.75, "prawidłowa")     # BMI 22.86

    def test_overweight(self):
        self.check_category(90, 1.80, "nadwaga")        # BMI 27.78

    def test_obesity(self):
        self.check_category(110, 1.75, "otyłość")       # BMI 35.92
