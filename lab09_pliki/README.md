# Lab 09 – Praca z plikami

📅 wtorek 08.12.2026, 08:30–11:45 · 📍 sala A/121 · ⏱ 4 h
**Sylabus:** treść nr 18 · **Efekty:** U1, U2, KS1 · **Slajdy:** [slajdy.md](slajdy.md)

## Cel zajęć

Po zajęciach potrafisz:
- otwierać pliki w odpowiednim trybie (`r`, `w`, `a`, `b`) z kodowaniem UTF-8,
- używać `with`, żeby plik zawsze został zamknięty,
- czytać i zapisywać pliki tekstowe linia po linii,
- obsługiwać brak pliku i błędne dane (`try` / `except`),
- zapisywać dane w formacie JSON (i wiedzieć, kiedy **nie** używać `pickle`).

## Na start: aktualizacja forka

Na GitHubie w swoim forku kliknij **Sync fork → Update branch**, a potem w terminalu: `git pull`.

## Zadania obowiązkowe ★

| Plik | Zadanie | Czas |
|---|---|---|
| `zad1_logger.py` | Logowanie zdarzeń z datą i godziną (tryb `a`) | 35 min |
| `zad2_suma_z_pliku.py` | Suma liczb z pliku z pomijaniem błędnych linii | 25 min |
| `zad3_edytor.py` | Prosty edytor: odczyt, dopisywanie, zamiana tekstu | 40 min |
| `zad4_json.py` | Książka adresowa z labu 06 zapisywana w JSON | 35 min |

## Zadania dodatkowe ☆

| Plik | Zadanie |
|---|---|
| `zad5_menedzer.py` | Menedżer plików: wyszukiwanie i porządkowanie według rozszerzeń (`pathlib`) |

## Jak sprawdzić rozwiązanie

W folderze `lab09_pliki`:

```bash
python -m unittest discover -s tests -v
python zad3_edytor.py        # edytor w terminalu
```

> Testy tworzą pliki w folderze tymczasowym i sprzątają po sobie – nie musisz niczego przygotowywać.

## Oddanie

Do **11:45**: `git add lab09_pliki`, `git commit -m "Lab 09"`, `git push`.

> ⏰ **Punkt za aktywność tylko za push przed 11:45** – liczy się godzina na GitHubie (zakładka Actions), nie data commita. Po zajęciach, nawet minutę później, punktu już nie ma. Nieobecność = brak punktu. Wymagane: wszystkie testy ★ zielone. [Zasady](../README.md#punkty-za-aktywność--tylko-za-pracę-na-zajęciach)

## Do poczytania

- E. Matthes, *Python. Instrukcje dla programisty* – rozdz. 10
- M. Dawson, *Python dla każdego* – rozdz. 7
