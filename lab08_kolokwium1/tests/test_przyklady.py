"""Testy przykładowych zadań kolokwialnych – Kolokwium I."""
import unittest

from helpers import ScriptTestCase, load

stock = load("przyklad2_magazyn.py")
text = load("przyklad3_tekst.py")


class TestPrzyklad1Temperatury(ScriptTestCase):
    def test_statistics(self):
        output = self.run_script("przyklad1_temperatury.py", "-2.5\n3\n0\n-1\n5.5\n\n")
        self.assertIn("Min: -2.5", output)
        self.assertIn("Max: 5.5", output)
        self.assertIn("Średnia: 1.00", output)
        self.assertIn("Dni z mrozem: 2", output)

    def test_no_data(self):
        self.assertIn("brak danych", self.run_script("przyklad1_temperatury.py", "\n").lower())


class TestPrzyklad2Magazyn(unittest.TestCase):
    def test_add_stock(self):
        inventory = {"śruba": 10}
        stock.add_stock(inventory, "śruba", 5)
        stock.add_stock(inventory, "nakrętka", 3)
        self.assertEqual(inventory, {"śruba": 15, "nakrętka": 3})

    def test_remove_stock(self):
        inventory = {"śruba": 10}
        self.assertTrue(stock.remove_stock(inventory, "śruba", 4))
        self.assertFalse(stock.remove_stock(inventory, "śruba", 100))
        self.assertFalse(stock.remove_stock(inventory, "gwóźdź", 1))
        self.assertEqual(inventory, {"śruba": 6})

    def test_remove_all_deletes_item(self):
        inventory = {"śruba": 2}
        stock.remove_stock(inventory, "śruba", 2)
        self.assertEqual(inventory, {})

    def test_low_stock(self):
        inventory = {"c": 1, "a": 0, "b": 50, "d": 4}
        self.assertEqual(stock.low_stock(inventory, 5), ["a", "c", "d"])


class TestPrzyklad3Tekst(unittest.TestCase):
    def test_compress(self):
        self.assertEqual(text.compress("aaabcc"), "a3b1c2")
        self.assertEqual(text.compress(""), "")

    def test_decompress(self):
        self.assertEqual(text.decompress("a3b1c2"), "aaabcc")
        self.assertEqual(text.decompress("x12"), "x" * 12)

    def test_are_anagrams(self):
        self.assertTrue(text.are_anagrams("Kamil Ślimak", "kamil ślimak"))
        self.assertTrue(text.are_anagrams("listen", "Silent"))
        self.assertFalse(text.are_anagrams("abc", "abd"))
