"""Moduł do przetestowania w zadaniu 2 – NIE zmieniaj go.

Twoim zadaniem jest napisać testy (test_moje_arytmetyka.py), które wykryją
każdy błąd, jaki ktoś mógłby tu kiedyś wprowadzić.
"""


def gcd(a, b):
    """Największy wspólny dzielnik (dla liczb całkowitych, także ujemnych i zera)."""
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return b


def lcm(a, b):
    """Najmniejsza wspólna wielokrotność; lcm(x, 0) == 0."""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)


def is_prime(n):
    """Czy n jest liczbą pierwszą?"""
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def factorial(n):
    """n! dla n >= 0; dla n < 0 zgłasza ValueError."""
    if n < 0:
        raise ValueError("Silnia z liczby ujemnej")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
