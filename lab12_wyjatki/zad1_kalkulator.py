"""Lab 12 – Zadanie 1 (★): „Bezpieczny kalkulator”.

Kalkulator nigdy się nie wysypuje: każdy błąd zamienia na czytelny komunikat.
"""


def calculate(a_text, op, b_text):
    """Liczy a op b dla argumentów podanych jako TEKST i zwraca wynik jako tekst, np. "3.5".

    Obsługiwane operatory: + - * / **
    Zamiast wyjątku zwraca komunikat:
        ZeroDivisionError  -> "Błąd: dzielenie przez zero"
        ValueError         -> "Błąd: to nie jest liczba"      (float("abc"))
        nieznany operator  -> "Błąd: nieznany operator"
        OverflowError      -> "Błąd: wynik za duży"           (np. 10.0 ** 1000)

    Wskazówka: jeden blok try i kilka klauzul except.
    """
    raise NotImplementedError


if __name__ == "__main__":
    while True:
        line = input("Działanie (np. 2 ** 10) albo Enter: ").split()
        if not line:
            break
        if len(line) != 3:
            print("Podaj: liczba operator liczba")
            continue
        print(calculate(line[0], line[1], line[2]))
