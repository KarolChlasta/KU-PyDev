"""Lab 12 – Zadanie 3 (★): Wyjątki przy pracy z plikami; else i finally."""


def read_config(path):
    """Czyta plik konfiguracyjny z liniami  klucz = wartość  i zwraca słownik (klucze i wartości bez spacji).

    - puste linie i linie zaczynające się od # pomija,
    - gdy pliku nie ma, zwraca {},
    - gdy linia nie zawiera "=", zgłasza ValueError("Linia 2: brak znaku =")  (numer linii od 1).
    """
    raise NotImplementedError


def read_first_line(path, log):
    """Zwraca pierwszą linię pliku (bez "\\n").

    Na początku dopisuje do listy log "start", a w bloku finally – "koniec".
    Wyjątku FileNotFoundError NIE łap – ma polecieć dalej, ale finally i tak się wykona.
    """
    raise NotImplementedError
