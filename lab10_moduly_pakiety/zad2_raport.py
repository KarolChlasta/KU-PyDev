"""Lab 10 – Zadanie 2 (★): Aplikacja korzystająca z własnego pakietu.

Zaimportuj funkcje z pakietu geometria (spróbuj różnych stylów importu!):
    import geometria
    from geometria import plaskie
    from geometria.plaskie import circle_area
"""


def total_area(shapes):
    """Suma pól figur z listy krotek:
        ("koło", r)
        ("prostokąt", a, b)
        ("trójkąt", a, b, c)
    Nieznane figury pomija.
    """
    raise NotImplementedError


if __name__ == "__main__":
    print(f"{total_area([('koło', 1), ('prostokąt', 2, 3)]):.2f}")
