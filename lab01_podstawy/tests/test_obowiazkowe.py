"""Testy zadań obowiązkowych (★) – Lab 01."""
from helpers import ScriptTestCase


class TestZad1Hello(ScriptTestCase):
    def test_prints_hello_world(self):
        output = self.run_script("zad1_hello.py")
        self.assertIn("Hello, World!", output)


class TestZad2Wizytowka(ScriptTestCase):
    def test_name_surname_and_age(self):
        output = self.run_script("zad2_wizytowka.py", "Anna\nKowalska\n2006\n")
        self.assertIn("Anna", output)
        self.assertIn("Kowalska", output)
        self.assertContainsNumber(output, 20)

    def test_other_birth_year(self):
        output = self.run_script("zad2_wizytowka.py", "Jan\nNowak\n1990\n")
        self.assertContainsNumber(output, 36)


class TestZad3BMI(ScriptTestCase):
    def test_bmi_70kg_175cm(self):
        output = self.run_script("zad3_bmi.py", "70\n1.75\n")
        self.assertContainsNumber(output, 22.86)

    def test_bmi_90kg_180cm(self):
        output = self.run_script("zad3_bmi.py", "90\n1.80\n")
        self.assertContainsNumber(output, 27.78)
