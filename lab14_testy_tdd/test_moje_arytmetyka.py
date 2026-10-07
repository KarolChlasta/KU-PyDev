"""Lab 14 – Zadanie 2 (★): TWOJE testy modułu arytmetyka.py.

Uruchom:  python -m unittest test_moje_arytmetyka -v

Wymagania (sprawdza tests/test_obowiazkowe.py):
  - co najmniej 8 metod testowych,
  - wszystkie przechodzą na poprawnym arytmetyka.py,
  - wykrywają 6 „mutantów” – kopii modułu z celowo wprowadzonym błędem (tests/mutanty/).

Testuj przypadki typowe I brzegowe: 0, 1, liczby ujemne, kwadraty liczb pierwszych, wyjątki.
"""
import unittest

from arytmetyka import factorial, gcd, is_prime, lcm


class TestGcd(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(gcd(12, 18), 6)

    # TODO: dopisz kolejne testy gcd (np. liczby względnie pierwsze, zero, liczby ujemne)


# TODO: klasy TestLcm, TestIsPrime, TestFactorial
# Przydatne asercje: assertEqual, assertTrue, assertFalse, assertRaises


if __name__ == "__main__":
    unittest.main()
