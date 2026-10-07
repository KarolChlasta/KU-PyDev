"""Lab 09 – Zadanie 3 (★): Prosty edytor tekstu."""


def read_text(path):
    """Zwraca całą zawartość pliku albo "" gdy plik nie istnieje."""
    raise NotImplementedError


def append_line(path, line):
    """Dopisuje linię na końcu pliku (ze znakiem nowej linii "\\n")."""
    raise NotImplementedError


def line_count(path):
    """Liczba linii w pliku (0 dla nieistniejącego)."""
    raise NotImplementedError


def replace_word(path, old, new):
    """Zamienia w pliku wszystkie wystąpienia tekstu old na new.

    Zapisuje plik z powrotem i zwraca liczbę dokonanych zamian.
    Wskazówka: text.count(old), text.replace(old, new)
    """
    raise NotImplementedError


def main():
    path = input("Plik: ")
    while True:
        command = input("[p]okaż, [d]opisz, [z]amień, [k]oniec: ").strip().lower()
        if command == "p":
            print(read_text(path))
        elif command == "d":
            append_line(path, input("Tekst: "))
        elif command == "z":
            count = replace_word(path, input("Co: "), input("Na co: "))
            print(f"Zamieniono: {count}")
        elif command == "k":
            break


if __name__ == "__main__":
    main()
