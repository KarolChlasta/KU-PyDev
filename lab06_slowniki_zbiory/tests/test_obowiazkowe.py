"""Testy zadań obowiązkowych (★) – Lab 06."""
from helpers import ScriptTestCase


class TestZad1KsiazkaAdresowa(ScriptTestCase):
    def test_add_find_list(self):
        commands = (
            "dodaj Ola 600100200\n"
            "dodaj Adam 500600700\n"
            "szukaj Ola\n"
            "lista\n"
            "koniec\n"
        )
        output = self.run_script("zad1_ksiazka_adresowa.py", commands)
        self.assertIn("600100200", output)
        self.assertLess(output.index("Adam: 500600700"), output.index("Ola: 600100200"),
                        "Lista ma być posortowana alfabetycznie")

    def test_update_and_remove(self):
        commands = "dodaj Ola 1\ndodaj Ola 2\nusuń Ola\nszukaj Ola\nkoniec\n"
        output = self.run_script("zad1_ksiazka_adresowa.py", commands).lower()
        self.assertIn("brak kontaktu", output)

    def test_missing_contact(self):
        output = self.run_script("zad1_ksiazka_adresowa.py", "szukaj Zenon\nkoniec\n").lower()
        self.assertIn("brak kontaktu", output)


class TestZad2Duplikaty(ScriptTestCase):
    def test_keeps_first_occurrence_order(self):
        output = self.run_script("zad2_duplikaty.py", "a b a c b a\n")
        self.assertIn("Bez duplikatów: a b c", output)
        self.assertIn("Usunięto: 3", output)
        self.assertIn("Unikalne (alfabetycznie): a b c", output)

    def test_no_duplicates(self):
        output = self.run_script("zad2_duplikaty.py", "kot pies\n")
        self.assertIn("Usunięto: 0", output)


class TestZad3Szyfr(ScriptTestCase):
    def test_encrypt(self):
        self.assertIn("dod pd nrwd", self.run_script("zad3_szyfr.py", "s\nAla ma kota\n"))

    def test_decrypt(self):
        self.assertIn("ala ma kota", self.run_script("zad3_szyfr.py", "d\ndod pd nrwd\n"))

    def test_wraps_around_and_keeps_other_chars(self):
        self.assertIn("abc, 123!", self.run_script("zad3_szyfr.py", "s\nxyz, 123!\n"))


class TestZad4Czestosc(ScriptTestCase):
    def test_counts_words(self):
        output = self.run_script("zad4_czestosc.py", "to jest to co to jest\n")
        self.assertIn("to: 3", output)
        self.assertIn("jest: 2", output)
        self.assertIn("co: 1", output)

    def test_most_common_first(self):
        output = self.run_script("zad4_czestosc.py", "b a b c b a\n")
        self.assertLess(output.index("b: 3"), output.index("a: 2"))
        self.assertLess(output.index("a: 2"), output.index("c: 1"))
