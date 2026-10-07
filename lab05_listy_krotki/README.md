# Lab 05 – Struktury danych I: listy i krotki

📅 wtorek 03.11.2026, 08:30–11:45 · 📍 sala A/121 · ⏱ 4 h
**Sylabus:** treść nr 10 · **Efekty:** U1, U3, KS1 · **Slajdy:** [slajdy.md](slajdy.md)

## Cel zajęć

Po zajęciach potrafisz:
- tworzyć i modyfikować listy (`append`, `remove`, `sort`, `pop`, `insert`),
- korzystać z indeksów i wycinków (*slicing*),
- rozumieć różnicę między listą (zmienną) a krotką (niezmienną),
- używać krotek do reprezentowania rekordów, np. miejsca `(rząd, miejsce)`.

## Na start: aktualizacja forka

Na GitHubie w swoim forku kliknij **Sync fork → Update branch**, a potem w terminalu: `git pull`.

## Zadania obowiązkowe ★

| Plik | Zadanie | Czas |
|---|---|---|
| `zad1_zakupy.py` | Lista zakupów sterowana poleceniami | 45 min |
| `zad2_rezerwacje.py` | System rezerwacji miejsc – krotki `(rząd, miejsce)` | 60 min |
| `zad3_wycinki.py` | Wycinki i funkcje `sorted`, `min`, `max`, `sum` | 30 min |

## Zadania dodatkowe ☆

| Plik | Zadanie |
|---|---|
| `zad4_znajdz_pare.py` | Gra „znajdź parę” (memory) |

## Jak sprawdzić rozwiązanie

W folderze `lab05_listy_krotki`:

```bash
python -m unittest discover -s tests -v
```

> Programy z poleceniami testujesz ręcznie, wpisując polecenia jedno po drugim. Test podaje je wszystkie naraz i kończy poleceniem `koniec`.

## Oddanie

Do **11:45**: `git add lab05_listy_krotki`, `git commit -m "Lab 05"`, `git push`.

> ⏰ **Punkt za aktywność tylko za push przed 11:45** – liczy się godzina na GitHubie (zakładka Actions), nie data commita. Po zajęciach, nawet minutę później, punktu już nie ma. Nieobecność = brak punktu. Wymagane: wszystkie testy ★ zielone. [Zasady](../README.md#punkty-za-aktywność--tylko-za-pracę-na-zajęciach)

## Do poczytania

- E. Matthes, *Python. Instrukcje dla programisty* – rozdz. 3–4
- M. Dawson, *Python dla każdego* – rozdz. 5
