# Lab 07 – Funkcje 🤖

📅 wtorek 01.12.2026, 08:30–11:45 · 📍 sala A/121 · ⏱ 4 h
**Sylabus:** treść nr 14 · **Efekty:** U1, U2, U3, KS1 · **Slajdy:** [slajdy.md](slajdy.md)

## Cel zajęć

Po zajęciach potrafisz:
- definiować funkcje z parametrami, wartościami domyślnymi i `return`,
- rozumieć zasięg zmiennych (lokalne, globalne),
- przekazywać funkcje jako argumenty i używać `lambda`,
- pisać funkcje rekurencyjne z warunkiem stopu,
- świadomie korzystać z AI do wyjaśniania i refaktoryzacji kodu.

## Na start: aktualizacja forka

Na GitHubie w swoim forku kliknij **Sync fork → Update branch**, a potem w terminalu: `git pull`.

## Nowość: testy wywołują Twoje funkcje

Od tego labu testy **importują** Twój plik i wywołują funkcje, np. `add(2, 3)`.
Dlatego:
- uzupełniasz **ciała funkcji** – usuń `raise NotImplementedError` i napisz kod,
- **nie zmieniaj nazw funkcji ani parametrów**,
- `input()` i `print()` trzymaj w `main()` – kod pod `if __name__ == "__main__":` nie wykonuje się przy imporcie.

## Zadania obowiązkowe ★

| Plik | Zadanie | Czas |
|---|---|---|
| `zad1_kalkulator.py` | Kalkulator funkcyjny + słownik `operator → funkcja` | 30 min |
| `zad2_napisy.py` | Normalizacja napisów, palindromy, samogłoski | 35 min |
| `zad3_csv.py` | Analiza ocen z pliku `dane/oceny.csv` | 35 min |
| `zad4_rekurencja.py` | Silnia, Fibonacci, potęga, suma cyfr – rekurencyjnie | 30 min |

## Blok AI 🤖 (~1 h, po zadaniach ★)

Wypełnij [AI.md](AI.md):
1. Poproś AI o **wyjaśnienie** Twojej funkcji `is_palindrome` – sprawdź, czy wyjaśnienie jest prawdziwe.
2. Poproś o **refaktoryzację** `zad2_napisy.py`; każdą zmianę sprawdź testami.
3. Zapisz prompt, decyzje (co przyjąłeś, co odrzuciłeś) i co najmniej jeden błąd AI.

Zasady: AI **po** samodzielnym rozwiązaniu, nie zamiast. Kod, którego nie umiesz wyjaśnić, nie jest Twój. `AI.md` oddajesz razem z labem.

## Zadania dodatkowe ☆

| Plik | Zadanie |
|---|---|
| `zad5_lambdy.py` | Funkcje jako argumenty, `lambda`, `filter`, `global` |

## Jak sprawdzić rozwiązanie

W folderze `lab07_funkcje`:

```bash
python -m unittest discover -s tests -v
python zad3_csv.py        # uruchomienie main()
```

## Oddanie

Do **11:45**: `git add lab07_funkcje`, `git commit -m "Lab 07"`, `git push`.

> ⏰ **Punkt za aktywność tylko za push przed 11:45** – liczy się godzina na GitHubie (zakładka Actions), nie data commita. Po zajęciach, nawet minutę później, punktu już nie ma. Nieobecność = brak punktu. Wymagane: wszystkie testy ★ zielone. [Zasady](../README.md#punkty-za-aktywność--tylko-za-pracę-na-zajęciach)

> 📝 **Kolokwium I – jutro: środa 02.12.2026, 14:00–17:15, sala A/136.** Zakres: laby 01–07. Szczegóły w [lab08_kolokwium1](../lab08_kolokwium1/).

## Do poczytania

- E. Matthes, *Python. Instrukcje dla programisty* – rozdz. 8
- M. Dawson, *Python dla każdego* – rozdz. 6
