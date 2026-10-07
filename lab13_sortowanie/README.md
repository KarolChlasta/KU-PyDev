# Lab 13 – Sortowanie, wyszukiwanie, notacja Big O 🤖

📅 wtorek 12.01.2027, 08:30–11:45 · 📍 sala A/121 · ⏱ 4 h
**Sylabus:** treść nr 26 · **Efekty:** U3, U1, KS1 · **Slajdy:** [slajdy.md](slajdy.md)

## Cel zajęć

Po zajęciach potrafisz:
- zaimplementować sortowanie bąbelkowe i przez wybieranie,
- zaimplementować wyszukiwanie liniowe i binarne,
- sortować złożone dane funkcją `sorted()` z parametrem `key`,
- oceniać złożoność algorytmów w notacji Big O i sprawdzać ją pomiarem,
- krytycznie oceniać kod algorytmów wygenerowany przez AI.

## Na start: aktualizacja forka

Na GitHubie w swoim forku kliknij **Sync fork → Update branch**, a potem w terminalu: `git pull`.

## Zadania obowiązkowe ★

| Plik | Zadanie | Czas |
|---|---|---|
| `zad1_sortowania.py` | Sortowanie bąbelkowe i przez wybieranie – bez `sorted()` | 40 min |
| `zad2_wyszukiwanie.py` | Wyszukiwanie liniowe i binarne + liczenie kroków | 35 min |
| `zad3_biblioteka.py` | „Sortowanie biblioteki” – `sorted` z `key`, sortowanie wielokryterialne | 25 min |
| `zad4_pomiar.py` | Eksperyment: jak rośnie czas sortowania? | 20 min |

> Testy sprawdzają, czy naprawdę piszesz algorytm: sortowanie nie może wywoływać `sorted()`, a wyszukiwanie binarne na liście miliona elementów może zajrzeć najwyżej do 25 z nich.

## Blok AI 🤖 (~1 h, po zadaniach ★)

Wypełnij [AI.md](AI.md):
1. Wpisz wyniki eksperymentu z `zad4_pomiar.py` i porównaj je z teorią.
2. Poproś AI o **quicksort**, przetestuj go na przypadkach brzegowych i znajdź słabe punkty.
3. Sprawdź **analizę złożoności** podaną przez AI – czy jest kompletna (najgorszy przypadek!)?

## Zadania dodatkowe ☆

| Plik | Zadanie |
|---|---|
| `zad5_szybsze.py` | Sortowanie przez wstawianie i przez scalanie (*merge sort*) |

## Jak sprawdzić rozwiązanie

```bash
python -m unittest discover -s tests -v
python zad4_pomiar.py
```

## Oddanie

Do **11:45**: `git add lab13_sortowanie`, `git commit -m "Lab 13"`, `git push` (razem z `AI.md`).

> ⏰ **Punkt za aktywność tylko za push przed 11:45** – liczy się godzina na GitHubie (zakładka Actions), nie data commita. Po zajęciach, nawet minutę później, punktu już nie ma. Nieobecność = brak punktu. Wymagane: wszystkie testy ★ zielone. [Zasady](../README.md#punkty-za-aktywność--tylko-za-pracę-na-zajęciach)

## Do poczytania

- T. H. Cormen i in., *Wprowadzenie do algorytmów* – rozdziały o sortowaniu
- J. Bentley, *Perełki oprogramowania* – rozdział o wyszukiwaniu binarnym
- Dokumentacja: *Sorting Techniques* (*docs.python.org/3/howto/sorting.html*), moduł `bisect`
