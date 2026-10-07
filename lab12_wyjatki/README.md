# Lab 12 – Obsługa wyjątków

📅 **piątek 08.01.2027, 14:00–17:15** · 📍 **sala A/124** · ⏱ 4 h
**Sylabus:** treść nr 24 · **Efekty:** U1, KS1 · **Slajdy:** [slajdy.md](slajdy.md)

## Cel zajęć

Po zajęciach potrafisz:
- czytać komunikat błędu (*traceback*) i rozpoznawać typowe wyjątki,
- obsługiwać wyjątki blokami `try` / `except` / `else` / `finally`,
- zgłaszać wyjątki (`raise`) i tworzyć własne klasy wyjątków,
- odróżniać walidację danych użytkownika od asercji (`assert`).

## Na start: aktualizacja forka

Na GitHubie w swoim forku kliknij **Sync fork → Update branch**, a potem w terminalu: `git pull`.

## Zadania obowiązkowe ★

| Plik | Zadanie | Czas |
|---|---|---|
| `zad1_kalkulator.py` | „Bezpieczny kalkulator” – błędy zamienione na komunikaty | 35 min |
| `zad2_walidacja.py` | Walidacja wieku i bezpieczne wczytywanie liczby | 40 min |
| `zad3_pliki.py` | Plik konfiguracyjny, brak pliku, `finally` | 35 min |
| `zad4_wyjatki.py` | Własny wyjątek `InsufficientFundsError` i asercje | 30 min |

## Zadania dodatkowe ☆

| Plik | Zadanie |
|---|---|
| `zad5_pesel.py` | Walidator PESEL z hierarchią własnych wyjątków |

## Jak sprawdzić rozwiązanie

```bash
python -m unittest discover -s tests -v
python zad1_kalkulator.py
```

## Oddanie

Do **17:15**: `git add lab12_wyjatki`, `git commit -m "Lab 12"`, `git push`.

> ⏰ **Punkt za aktywność tylko za push przed 17:15** – liczy się godzina na GitHubie (zakładka Actions), nie data commita. Po zajęciach, nawet minutę później, punktu już nie ma. Nieobecność = brak punktu. Wymagane: wszystkie testy ★ zielone. [Zasady](../README.md#punkty-za-aktywność--tylko-za-pracę-na-zajęciach)

## Do poczytania

- E. Matthes, *Python. Instrukcje dla programisty* – rozdz. 10 (wyjątki)
- Dokumentacja: *Errors and Exceptions* (*docs.python.org/3/tutorial/errors.html*), *Built-in Exceptions*
