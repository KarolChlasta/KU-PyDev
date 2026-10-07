"""Lab 07 – Zadanie 1 (★): Kalkulator funkcyjny.

Każde działanie to osobna funkcja. Słownik OPERATIONS przypisuje
symbolowi operatora FUNKCJĘ (nie wynik!) – funkcje w Pythonie są obiektami.
"""


def add(a, b):
    """Zwraca a + b."""
    raise NotImplementedError


def subtract(a, b):
    """Zwraca a - b."""
    raise NotImplementedError


def multiply(a, b):
    """Zwraca a * b."""
    raise NotImplementedError


def divide(a, b):
    """Zwraca a / b albo None, gdy b == 0."""
    raise NotImplementedError


# TODO: uzupełnij słownik:  "+" -> add, "-" -> subtract, "*" -> multiply, "/" -> divide
OPERATIONS = {}


def calculate(a, op, b):
    """Wykonuje działanie op na a i b, korzystając ze słownika OPERATIONS.

    Dla nieznanego operatora zwraca None.
    Wskazówka: func = OPERATIONS.get(op); potem func(a, b).
    """
    raise NotImplementedError


def main():
    a = float(input("Pierwsza liczba: "))
    op = input("Operator (+ - * /): ").strip()
    b = float(input("Druga liczba: "))
    result = calculate(a, op, b)
    print("Błąd: nieznany operator albo dzielenie przez zero" if result is None else f"Wynik: {result}")


if __name__ == "__main__":
    main()
