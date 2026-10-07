# Lab 14 – Testy jednostkowe i TDD 🤖

📅 wtorek 19.01.2027, 08:30–11:45 · 📍 **sala A/111** · ⏱ 4 h
**Sylabus:** treść nr 28 · **Efekty:** U1, U3, KS1 · **Slajdy:** [slajdy.md](slajdy.md)

## Cel zajęć

Po zajęciach potrafisz:
- pisać testy jednostkowe w `unittest` (klasy, asercje, `setUp`, `assertRaises`),
- pracować w cyklu TDD: **red → green → refactor**,
- odcinać testy od internetu atrapami (`unittest.mock`),
- ocenić jakość testów: pokrycie (*coverage*) i testowanie mutacyjne.

## Na start: aktualizacja forka

Na GitHubie w swoim forku kliknij **Sync fork → Update branch**, a potem w terminalu: `git pull`.

## Zadania obowiązkowe ★

| Plik | Zadanie | Czas |
|---|---|---|
| `zad1_pogoda.py` | „Aplikacja pogodowa” w TDD – funkcje rozwijane test po teście, pobieranie danych zastąpione mockiem | 70 min |
| `test_moje_arytmetyka.py` | **Twoje** testy modułu `arytmetyka.py` – muszą wykryć 6 mutantów | 60 min |

### Jak działa zadanie 2 (testowanie mutacyjne)

W `tests/mutanty/` jest 6 kopii `arytmetyka.py`, każda z **jednym celowo wprowadzonym błędem**. Test sprawdzający uruchamia Twoje testy:
- na poprawnym module – muszą **przejść**,
- na każdym mutancie – co najmniej jeden musi **nie przejść** (mutant „zabity”).

```bash
python -m unittest test_moje_arytmetyka -v      # Twoje testy
python -m unittest discover -s tests -v         # sprawdzenie (czy zabijasz mutanty)
```

Nie zaglądaj od razu do mutantów – najpierw pomyśl o przypadkach brzegowych (0, 1, liczby ujemne, wyjątki).

## Blok AI 🤖 (~1 h, po zadaniach ★)

Wypełnij [AI.md](AI.md): Ty piszesz testy → AI implementuje; AI pisze testy → Ty oceniasz; AI wyjaśnia mocki.

## Zadania dodatkowe ☆

- **Pokrycie testami:**

  ```bash
  python -m pip install coverage
  coverage run -m unittest discover -s tests
  coverage report -m          # które linie nie są wykonywane przez testy?
  coverage html               # raport w htmlcov/index.html (folder jest w .gitignore)
  ```

- Dopisz do `test_moje_arytmetyka.py` własny test z `unittest.mock.patch` dla `fetch_forecast` z `zad1_pogoda.py`.

## Oddanie

Do **11:45**: `git add lab14_testy_tdd`, `git commit -m "Lab 14"`, `git push` (razem z `AI.md`).

> ⏰ **Punkt za aktywność tylko za push przed 11:45** – liczy się godzina na GitHubie (zakładka Actions), nie data commita. Po zajęciach, nawet minutę później, punktu już nie ma. Nieobecność = brak punktu. Wymagane: wszystkie testy ★ zielone. [Zasady](../README.md#punkty-za-aktywność--tylko-za-pracę-na-zajęciach)

> 📝 **Kolokwium II – wtorek 26.01.2027, 08:30–11:45, sala A/111.** Zakres: laby 09–14. Szczegóły w [lab15_kolokwium2](../lab15_kolokwium2/).

## Do poczytania

- E. Matthes, *Python. Instrukcje dla programisty* – rozdz. 11 (testowanie)
- K. Beck, *TDD. Sztuka tworzenia dobrego kodu*, Helion
- Dokumentacja: `unittest`, `unittest.mock`
