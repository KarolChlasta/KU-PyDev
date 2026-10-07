"""Lab 09 – Zadanie 4 (★): Książka adresowa zapisywana w JSON.

Kontynuacja labu 06: słownik imię -> telefon przeżywa teraz zamknięcie programu.
"""
import json


def save_contacts(contacts, path):
    """Zapisuje słownik do pliku JSON.

    Użyj json.dump(..., ensure_ascii=False, indent=2), żeby polskie litery były czytelne.
    """
    raise NotImplementedError


def load_contacts(path):
    """Wczytuje słownik z pliku JSON; gdy pliku nie ma – zwraca {}."""
    raise NotImplementedError


def add_contact(path, name, phone):
    """Wczytuje kontakty, dodaje/nadpisuje jeden i zapisuje z powrotem."""
    raise NotImplementedError
