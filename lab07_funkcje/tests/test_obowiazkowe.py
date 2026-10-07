"""Testy zadań obowiązkowych (★) – Lab 07."""
import unittest

from helpers import DATA_DIR, load

calc = load("zad1_kalkulator.py")
texts = load("zad2_napisy.py")
grades_csv = load("zad3_csv.py")
rec = load("zad4_rekurencja.py")


class TestZad1Kalkulator(unittest.TestCase):
    def test_basic_operations(self):
        self.assertEqual(calc.add(2, 3), 5)
        self.assertEqual(calc.subtract(2, 3), -1)
        self.assertEqual(calc.multiply(4, 2.5), 10)
        self.assertEqual(calc.divide(7, 2), 3.5)

    def test_divide_by_zero_returns_none(self):
        self.assertIsNone(calc.divide(1, 0))

    def test_calculate_dispatches_by_operator(self):
        self.assertEqual(calc.calculate(6, "*", 7), 42)
        self.assertEqual(calc.calculate(6, "-", 7), -1)
        self.assertIsNone(calc.calculate(6, "?", 7))

    def test_operations_dict_holds_functions(self):
        self.assertIs(calc.OPERATIONS["+"], calc.add)
        self.assertIs(calc.OPERATIONS["/"], calc.divide)


class TestZad2Napisy(unittest.TestCase):
    def test_normalize_spaces(self):
        self.assertEqual(texts.normalize_spaces("  Ala   ma \t kota  "), "Ala ma kota")

    def test_normalize_name(self):
        self.assertEqual(texts.normalize_name("  jAN   koWALski "), "Jan Kowalski")
        self.assertEqual(texts.normalize_name("anna-maria NOWAK"), "Anna-Maria Nowak")

    def test_is_palindrome(self):
        self.assertTrue(texts.is_palindrome("Kobyła ma mały bok"))
        self.assertTrue(texts.is_palindrome("Kajak"))
        self.assertFalse(texts.is_palindrome("Python"))

    def test_count_vowels(self):
        self.assertEqual(texts.count_vowels("Ćwiczenie z Pythona"), 7)
        self.assertEqual(texts.count_vowels("ŁĄKA"), 2)


class TestZad3Csv(unittest.TestCase):
    def setUp(self):
        self.grades = grades_csv.load_grades(DATA_DIR / "oceny.csv")

    def test_load_grades(self):
        self.assertEqual(len(self.grades), 6)
        self.assertEqual(self.grades[0], ("Anna Kowalska", 4.5))

    def test_average(self):
        self.assertAlmostEqual(grades_csv.average(self.grades), 23 / 6)

    def test_average_of_empty_list(self):
        self.assertEqual(grades_csv.average([]), 0.0)

    def test_best_returns_first_maximum(self):
        self.assertEqual(grades_csv.best(self.grades), ("Ewa Wiśniewska", 5.0))

    def test_count_passing(self):
        self.assertEqual(grades_csv.count_passing(self.grades), 5)
        self.assertEqual(grades_csv.count_passing(self.grades, threshold=4.5), 3)


class TestZad4Rekurencja(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(rec.factorial(0), 1)
        self.assertEqual(rec.factorial(5), 120)

    def test_fibonacci(self):
        self.assertEqual([rec.fibonacci(n) for n in range(10)], [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
        self.assertEqual(rec.fibonacci(20), 6765)

    def test_power(self):
        self.assertEqual(rec.power(2, 10), 1024)
        self.assertEqual(rec.power(7, 0), 1)

    def test_sum_digits(self):
        self.assertEqual(rec.sum_digits(12345), 15)
        self.assertEqual(rec.sum_digits(0), 0)
