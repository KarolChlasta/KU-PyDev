"""Lab 11 – Zadanie 1 (★): „Przypomnienie o wydarzeniach”.

Funkcje przyjmują dzisiejszą datę jako parametr `today` (zamiast wołać date.today()),
dzięki czemu da się je przetestować dla dowolnego dnia.
"""
from datetime import date, datetime


def parse_date(text):
    """Zamienia "24.12.2026" na date(2026, 12, 24).

    Wskazówka: datetime.strptime(text, "%d.%m.%Y").date()
    """
    raise NotImplementedError


def days_until(event, today):
    """Ile dni zostało do wydarzenia (ujemne – gdy już minęło). Odejmowanie dat daje timedelta."""
    raise NotImplementedError


def describe(name, event, today):
    """Opis wydarzenia:
        "Wigilia: za 2 dni"   |   "Lab 11: dziś!"   |   "Lab 10: 7 dni temu"
    """
    raise NotImplementedError


def upcoming(events, today):
    """Ze słownika nazwa -> data zwraca listę (nazwa, dni) dla wydarzeń dzisiaj i w przyszłości,
    posortowaną od najbliższego.
    """
    raise NotImplementedError


def main():
    events = {"Wigilia": date(2026, 12, 24), "Kolokwium II": date(2027, 1, 26)}
    for name, days in upcoming(events, date.today()):
        print(describe(name, events[name], date.today()))


if __name__ == "__main__":
    main()
