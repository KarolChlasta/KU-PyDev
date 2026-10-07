"""Lab 07 – Zadanie 2 (★): Funkcje przetwarzające napisy."""

VOWELS = "aąeęioóuy"


def normalize_spaces(text):
    """Usuwa spacje z brzegów i zamienia wielokrotne białe znaki na jedną spację.

    >>> normalize_spaces("  Ala   ma  kota ")
    'Ala ma kota'
    Wskazówka: text.split() bez argumentu dzieli po dowolnych białych znakach.
    """
    raise NotImplementedError


def normalize_name(text):
    """Porządkuje imię i nazwisko: zbędne spacje znikają, każde słowo z wielkiej litery.

    >>> normalize_name("  jAN   koWALski ")
    'Jan Kowalski'
    >>> normalize_name("anna-maria NOWAK")
    'Anna-Maria Nowak'
    Wskazówka: użyj normalize_spaces() i metody str.title().
    """
    raise NotImplementedError


def is_palindrome(text):
    """Czy tekst czytany wspak jest taki sam? Pomija wielkość liter i znaki niebędące literami.

    >>> is_palindrome("Kobyła ma mały bok")
    True
    Wskazówka: char.isalpha(), text[::-1]
    """
    raise NotImplementedError


def count_vowels(text):
    """Liczy samogłoski (także polskie: ą, ę, ó, y) bez względu na wielkość liter."""
    raise NotImplementedError
