# Lab 06 – Struktury danych II: słowniki i zbiory

📅 wtorek 24.11.2026, 08:30–11:45 · 📍 sala A/121 · ⏱ 4 h
**Sylabus:** treść nr 12 · **Efekty:** U1, U3, KS1 · **Slajdy:** [slajdy.md](slajdy.md)

## Cel zajęć

Po zajęciach potrafisz:
- tworzyć słowniki i korzystać z metod `get`, `keys`, `values`, `items`,
- używać słowników do mapowania (np. szyfr) i zliczania,
- wykonywać operacje na zbiorach: suma, część wspólna, różnica,
- wybrać właściwą strukturę danych: listę, krotkę, słownik albo zbiór.

## Na start: aktualizacja forka

Na GitHubie w swoim forku kliknij **Sync fork → Update branch**, a potem w terminalu: `git pull`.

## Zadania obowiązkowe ★

| Plik | Zadanie | Czas |
|---|---|---|
| `zad1_ksiazka_adresowa.py` | Książka adresowa na słowniku | 45 min |
| `zad2_duplikaty.py` | Usuwanie duplikatów z zachowaniem kolejności (zbiór `seen`) | 25 min |
| `zad3_szyfr.py` | Szyfr Cezara jako słownik: szyfrowanie i deszyfrowanie | 40 min |
| `zad4_czestosc.py` | Częstość słów w tekście | 30 min |

## Zadania dodatkowe ☆

| Plik | Zadanie |
|---|---|
| `zad5_znajomi.py` | Wspólni znajomi – operacje na zbiorach |

## Jak sprawdzić rozwiązanie

W folderze `lab06_slowniki_zbiory`:

```bash
python -m unittest discover -s tests -v
```

## Oddanie

Do **11:45**: `git add lab06_slowniki_zbiory`, `git commit -m "Lab 06"`, `git push`.

> ⏰ **Punkt za aktywność tylko za push przed 11:45** – liczy się godzina na GitHubie (zakładka Actions), nie data commita. Po zajęciach, nawet minutę później, punktu już nie ma. Nieobecność = brak punktu. Wymagane: wszystkie testy ★ zielone. [Zasady](../README.md#punkty-za-aktywność--tylko-za-pracę-na-zajęciach)

> 📝 **Kolokwium I – środa 02.12.2026, 14:00–17:15, sala A/136.** Zakres: laby 01–07. Szczegóły w [lab08_kolokwium1](../lab08_kolokwium1/).

## Do poczytania

- E. Matthes, *Python. Instrukcje dla programisty* – rozdz. 6
- M. Dawson, *Python dla każdego* – rozdz. 5
