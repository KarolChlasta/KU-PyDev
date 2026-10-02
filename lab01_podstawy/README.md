# Lab 01 – Podstawy Pythona: Hello, World! i BMI

📅 wtorek 06.10.2026, 08:30–11:45 · 📍 sala A/121 · ⏱ 4 h
**Sylabus:** treść nr 2 · **Efekty:** U1, KS1 · **Slajdy:** [slajdy.md](slajdy.md)

## Cel zajęć

Po zajęciach potrafisz:
- skonfigurować środowisko pracy (Python, VS Code, Git, GitHub),
- napisać i uruchomić skrypt w Pythonie,
- używać zmiennych, `input()`, `print()` i f-stringów,
- wykonać proste obliczenia i oddać pracę przez Git.

## Część 0 ★ – konfiguracja (~45 min)

Postępuj według [SETUP.md](../SETUP.md):

- [ ] Python 3.12+ działa: `python --version`
- [ ] VS Code z rozszerzeniem Python
- [ ] Fork repozytorium na swoim koncie GitHub i `git clone`
- [ ] Włączone GitHub Actions w forku
- [ ] Pierwszy commit i push (np. dopisz swoje imię w `lab01_podstawy/zad1_hello.py` w komentarzu)

## Zadania obowiązkowe ★

| Plik | Zadanie | Czas |
|---|---|---|
| `zad1_hello.py` | Wypisz `Hello, World!` | 10 min |
| `zad2_wizytowka.py` | Zapytaj o imię, nazwisko, rok urodzenia; wypisz zdanie z wiekiem | 30 min |
| `zad3_bmi.py` | Kalkulator BMI (2 miejsca po przecinku) | 40 min |

Szczegóły zadania są w komentarzu na początku każdego pliku.

## Zadania dodatkowe ☆

| Plik | Zadanie |
|---|---|
| `zad4_bmi_kategoria.py` | BMI + kategoria wg WHO (zapowiedź `if` z labu 03) |

## Jak sprawdzić rozwiązanie

W terminalu, w folderze `lab01_podstawy`:

```bash
python -m unittest discover -s tests -v                          # wszystkie testy
python -m unittest discover -s tests -p "test_obowiazkowe.py" -v # tylko ★
```

`OK` oznacza, że wszystko działa. `FAIL` pokazuje, czego test oczekiwał, a czego nie znalazł w wyjściu programu.

> Liczby dziesiętne wpisuj z **kropką** (`1.75`, nie `1,75`).

## Oddanie

Do **11:45**:

```bash
git add lab01_podstawy
git commit -m "Lab 01"
git push
```

Za ★ oddane w trakcie zajęć dostajesz punkt aktywności (szczegóły w [README](../README.md#zaliczenie)).

## Do poczytania

- E. Matthes, *Python. Instrukcje dla programisty* – rozdz. 1–2
- M. Dawson, *Python dla każdego* – rozdz. 1
