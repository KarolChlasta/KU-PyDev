"""Lab 13 – Zadanie 3 (★): „Sortowanie biblioteki”.

Tu już WOLNO (i należy) używać sorted() z parametrem key – w praktyce tak się sortuje.
"""

# Dane przykładowe (liczby stron zależą od wydania – przyjęto przykładowe wartości)
BOOKS = [
    {"title": "Solaris", "author": "Stanisław Lem", "year": 1961, "pages": 256},
    {"title": "Lalka", "author": "Bolesław Prus", "year": 1890, "pages": 696},
    {"title": "Pan Tadeusz", "author": "Adam Mickiewicz", "year": 1834, "pages": 384},
    {"title": "Cyberiada", "author": "Stanisław Lem", "year": 1965, "pages": 320},
    {"title": "Ostatnie życzenie", "author": "Andrzej Sapkowski", "year": 1993, "pages": 332},
    {"title": "Python. Instrukcje dla programisty", "author": "Eric Matthes", "year": 2023, "pages": 600},
]

KEYS = ("title", "author", "year", "pages")


def sort_books(books, key, descending=False):
    """Nowa lista książek posortowana po polu key (jedno z KEYS); dla innego klucza – ValueError.

    Wskazówka: sorted(books, key=lambda book: book[key], reverse=descending)
    """
    raise NotImplementedError


def sort_by_author_then_year(books):
    """Sortowanie po autorze, a w obrębie autora – po roku (klucz będący KROTKĄ)."""
    raise NotImplementedError


def newest(books, n):
    """n najnowszych książek, od najnowszej."""
    raise NotImplementedError
