"""Lab 13 – Zadanie 1 (★): Sortowanie bąbelkowe i przez wybieranie.

Obie funkcje zwracają NOWĄ, posortowaną rosnąco listę i nie zmieniają listy wejściowej
(zacznij od kopii: result = list(values)). Nie używaj sorted() ani list.sort() – testy to sprawdzają.
"""


def bubble_sort(values):
    """Sortowanie bąbelkowe: porównuj sąsiadów i zamieniaj je, aż w całym przebiegu nie będzie zamiany.

    Zamiana:  a[i], a[i + 1] = a[i + 1], a[i]
    """
    raise NotImplementedError


def selection_sort(values):
    """Sortowanie przez wybieranie: dla każdej pozycji i znajdź minimum w części a[i:] i zamień je z a[i]."""
    raise NotImplementedError
