# Lab 03 – Instrukcje warunkowe

📅 wtorek 20.10.2026, 08:30–11:45 · 📍 sala A/121 · ⏱ 4 h
**Sylabus:** treść nr 6 · **Efekty:** U1, U3, KS1 · **Slajdy:** [slajdy.md](slajdy.md)

## Cel zajęć

Po zajęciach potrafisz:
- budować warunki z operatorów porównania i operatorów logicznych `and`, `or`, `not`,
- pisać rozgałęzienia `if` / `elif` / `else` i wyrażenia warunkowe,
- zaprojektować prosty system decyzyjny jako ciąg reguł,
- obsłużyć przypadki szczególne (dzielenie przez zero, błędne dane).

## Na start: aktualizacja forka

Na GitHubie w swoim forku kliknij **Sync fork → Update branch**, a potem w terminalu: `git pull`.

## Zadania obowiązkowe ★

| Plik | Zadanie | Czas |
|---|---|---|
| `zad1_inwestycja.py` | „Jak zainwestować?” – rekomendacja na podstawie kwoty, horyzontu i profilu ryzyka | 50 min |
| `zad2_kalkulator.py` | Kalkulator z wyborem działania i ochroną przed dzieleniem przez zero | 30 min |
| `zad3_przestepny.py` | Czy rok jest przestępny? | 20 min |
| `zad4_ocena.py` | Ocena z przedmiotu według progów z sylabusa | 30 min |

## Zadania dodatkowe ☆

| Plik | Zadanie |
|---|---|
| `zad5_trojkat.py` | Czy z trzech odcinków da się zbudować trójkąt i jaki to trójkąt? |

## Jak sprawdzić rozwiązanie

W folderze `lab03_warunki`:

```bash
python -m unittest discover -s tests -v
```

> W `zad1_inwestycja.py` kolejność warunków ma znaczenie – sprawdzaj reguły dokładnie w podanej kolejności.

## Oddanie

Do **11:45**: `git add lab03_warunki`, `git commit -m "Lab 03"`, `git push`.

> ⏰ **Punkt za aktywność tylko za push przed 11:45** – liczy się godzina na GitHubie (zakładka Actions), nie data commita. Po zajęciach, nawet minutę później, punktu już nie ma. Nieobecność = brak punktu. Wymagane: wszystkie testy ★ zielone. [Zasady](../README.md#punkty-za-aktywność--tylko-za-pracę-na-zajęciach)

## Do poczytania

- E. Matthes, *Python. Instrukcje dla programisty* – rozdz. 5
- M. Dawson, *Python dla każdego* – rozdz. 3
