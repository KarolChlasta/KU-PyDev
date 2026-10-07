# Lab 11 – Biblioteka standardowa: daty, czas, matematyka

📅 wtorek 22.12.2026, 08:30–11:45 · 📍 sala A/121 · ⏱ 4 h
**Sylabus:** treść nr 22 · **Efekty:** U1, U2, KS1 · **Slajdy:** [slajdy.md](slajdy.md)

## Cel zajęć

Po zajęciach potrafisz:
- liczyć na datach (`date`, `datetime`, `timedelta`) i zamieniać tekst na datę i z powrotem,
- przeliczać czas między strefami (`zoneinfo`) z uwzględnieniem czasu letniego,
- mierzyć czas wykonania kodu (`time.perf_counter`),
- liczyć statystyki opisowe z modułem `math` i porównać je z modułem `statistics`.

## Na start: aktualizacja forka

Na GitHubie w swoim forku kliknij **Sync fork → Update branch**, a potem w terminalu: `git pull`.

> **Windows:** moduł `zoneinfo` potrzebuje bazy stref: `python -m pip install tzdata` (raz).

## Zadania obowiązkowe ★

| Plik | Zadanie | Czas |
|---|---|---|
| `zad1_wydarzenia.py` | „Przypomnienie o wydarzeniach” – ile dni zostało | 40 min |
| `zad2_strefy.py` | Konwersja stref czasowych, przesunięcie względem UTC | 35 min |
| `zad3_statystyka.py` | Średnia, mediana, odchylenie standardowe z `math` | 35 min |
| `zad4_pomiar.py` | Pomiar czasu: pętla vs wzór Gaussa | 25 min |

## Zadania dodatkowe ☆

| Plik | Zadanie |
|---|---|
| `zad5_kalendarz.py` | Nazwy dni tygodnia, weekendy, dni robocze |

## Jak sprawdzić rozwiązanie

```bash
python -m unittest discover -s tests -v
python zad4_pomiar.py        # porównanie czasów
```

## Oddanie

Do **11:45**: `git add lab11_daty_math`, `git commit -m "Lab 11"`, `git push`.

> ⏰ **Punkt za aktywność tylko za push przed 11:45** – liczy się godzina na GitHubie (zakładka Actions), nie data commita. Po zajęciach, nawet minutę później, punktu już nie ma. Nieobecność = brak punktu. Wymagane: wszystkie testy ★ zielone. [Zasady](../README.md#punkty-za-aktywność--tylko-za-pracę-na-zajęciach)

> 📅 Następne zajęcia: **piątek 08.01.2027, 14:00–17:15, sala A/124** (wyjątkowo!).

## Do poczytania

- Dokumentacja modułów `datetime`, `zoneinfo`, `time`, `math`, `statistics` (*docs.python.org/3/library/*)
- L. Ramalho, *Zaawansowany Python* – fragmenty o liczbach i czasie
