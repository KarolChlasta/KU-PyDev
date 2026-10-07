# Lab 04 – Pętle

📅 wtorek 27.10.2026, 08:30–11:45 · 📍 sala A/121 · ⏱ 4 h
**Sylabus:** treść nr 8 · **Efekty:** U1, U3, KS1 · **Slajdy:** [slajdy.md](slajdy.md)

## Cel zajęć

Po zajęciach potrafisz:
- powtarzać instrukcje pętlami `for` i `while`,
- korzystać z `range()`, `break` i `continue`,
- pisać pętle zagnieżdżone,
- stosować typowe wzorce: akumulator, licznik, wartownik (pusta linia kończy dane).

## Na start: aktualizacja forka

Na GitHubie w swoim forku kliknij **Sync fork → Update branch**, a potem w terminalu: `git pull`.

## Zadania obowiązkowe ★

| Plik | Zadanie | Czas |
|---|---|---|
| `zad1_srednia.py` | Średnia z ocen wpisywanych do pustej linii | 30 min |
| `zad2_tabliczka.py` | Tabliczka mnożenia n × n (pętle zagnieżdżone) | 30 min |
| `zad3_suma_cyfr.py` | Suma i liczba cyfr liczby – arytmetycznie | 30 min |
| `zad4_zgadywanka.py` | Gra „zgadnij liczbę” (`while`, `break`, `continue`) | 45 min |

## Zadania dodatkowe ☆

| Plik | Zadanie |
|---|---|
| `zad5_crawler.py` | Mini-crawler: linki i domeny z pliku `dane/strona.html` |

## Jak sprawdzić rozwiązanie

W folderze `lab04_petle`:

```bash
python -m unittest discover -s tests -v
```

> Program, który nie kończy pętli, zatrzymasz w terminalu skrótem **Ctrl+C**. Testy przerywają skrypt po 10 s.

## Oddanie

Do **11:45**: `git add lab04_petle`, `git commit -m "Lab 04"`, `git push`.

> ⏰ **Punkt za aktywność tylko za push przed 11:45** – liczy się godzina na GitHubie (zakładka Actions), nie data commita. Po zajęciach, nawet minutę później, punktu już nie ma. Nieobecność = brak punktu. Wymagane: wszystkie testy ★ zielone. [Zasady](../README.md#punkty-za-aktywność--tylko-za-pracę-na-zajęciach)

## Do poczytania

- E. Matthes, *Python. Instrukcje dla programisty* – rozdz. 4 (pętla `for`) i 7 (pętla `while`)
- M. Dawson, *Python dla każdego* – rozdz. 3–4
