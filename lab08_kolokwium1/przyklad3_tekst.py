"""Kolokwium I – PRZYKŁAD 3 (algorytm): Kompresja RLE i anagramy."""


def compress(text):
    """Kodowanie długości serii (Run-Length Encoding): "aaabcc" -> "a3b1c2"."""
    raise NotImplementedError


def decompress(code):
    """Odwrotność compress: "a3b1c2" -> "aaabcc". Liczba może mieć kilka cyfr: "x12"."""
    raise NotImplementedError


def are_anagrams(first, second):
    """Czy teksty składają się z tych samych liter? Pomija wielkość liter i spacje."""
    raise NotImplementedError
