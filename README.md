# Podstawy programowania w języku Python I

Materiały do **laboratorium** z przedmiotu *Podstawy programowania w języku Python I*
(Informatyka, I stopień, rok 1, semestr zimowy 2026/2027, Akademia Leona Koźmińskiego).

- **Prowadzący laboratorium (grupa lab02/INF – I):** dr Karol Chlasta
- **Wykład:** E. Kot
- **Platforma e-learningowa:** [CyberSkiller](https://alk.cyberskiller.com) · informacje organizacyjne: Blackboard

Zajęcia to praktyczne wprowadzenie do Pythona: podstawy programowania, struktury danych,
algorytmy oraz dobre praktyki i standardy pisania kodu.

## Jak zacząć

1. Przejdź przez [SETUP.md](SETUP.md): instalacja Pythona, VS Code i Git, fork repozytorium.
2. Na każdych zajęciach: **Sync fork**, `git pull` i otwórz folder bieżącego labu.
3. Pracuj w plikach `zadN_*.py`, sprawdzaj testami, oddawaj przez `git push`.

## Harmonogram

| Lab | Data | Temat |
|---|---|---|
| [01](lab01_podstawy/) | wt 06.10.2026 | Podstawy Pythona, Hello World, BMI |
| [02](lab02_zmienne_typy/) | wt 13.10.2026 | Zmienne, typy danych, operacje arytmetyczne |
| 03 | wt 20.10.2026 | Instrukcje warunkowe |
| 04 | wt 27.10.2026 | Pętle |
| 05 | wt 03.11.2026 | Listy i krotki |
| 06 | wt 24.11.2026 | Słowniki i zbiory |
| 07 | wt 01.12.2026 | Funkcje 🤖 |
| 08 | **śr 02.12.2026, 14:00–17:15, A/136** | **Kolokwium I** |
| 09 | wt 08.12.2026 | Praca z plikami |
| 10 | wt 15.12.2026 | Moduły i pakiety |
| 11 | wt 22.12.2026 | Biblioteka standardowa: daty, czas, math |
| 12 | **pt 08.01.2027, 14:00–17:15, A/124** | Obsługa wyjątków |
| 13 | wt 12.01.2027 | Sortowanie, wyszukiwanie, notacja Big O 🤖 |
| 14 | wt 19.01.2027, **A/111** | Testy jednostkowe i TDD 🤖 |
| 15 | wt 26.01.2027, **A/111** | **Kolokwium II** |

Jeśli nie zaznaczono inaczej: wtorek 08:30–11:45, sala A/121. 🤖 – zajęcia z blokiem pracy z AI.
Kolejne laby pojawiają się w repozytorium przed zajęciami.

## Struktura labu

```
labNN_temat/
├── README.md              cele, zadania ★ i ☆, oddanie
├── slajdy.md              wprowadzenie do zajęć
├── zadN_*.py              pliki do uzupełnienia
└── tests/
    ├── test_obowiazkowe.py   testy zadań ★
    └── test_dodatkowe.py     testy zadań ☆
```

- **★ obowiązkowe** – ścieżka na ok. 3 h, którą oddajesz na zajęciach
- **☆ dodatkowe** – dla chętnych, rozwijające

Testy uruchamiasz w folderze labu: `python -m unittest discover -s tests -v`.

## Zaliczenie

| Składnik | Punkty |
|---|---|
| Kolokwium I (pisemne – pisanie programów i algorytmów na żywo) | 50 |
| Kolokwium II (jw.) | 50 |
| **Bonus:** obecność | do 10 |
| **Bonus:** aktywność | do 10 |
| **Razem** | maks. 120 |

- **Obecność:** 15 spotkań, 2 nieobecności bez utraty punktów, każda kolejna −1 pkt (minimum 0).
- **Aktywność:** 13 labów (bez kolokwiów) × 10/13 pkt – zasady poniżej.
- **Ocena** liczona od 100 pkt (bonus pomaga osiągnąć próg):

| Punkty | Ocena |
|---|---|
| > 91 | bardzo dobry (5) |
| > 83 – 91 | dobry plus (4,5) |
| > 75 – 83 | dobry (4) |
| > 67 – 75 | dostateczny plus (3,5) |
| > 60 – 67 | dostateczny (3) |
| ≤ 60 | niedostateczny (2) |

- **Termin drugi:** jedno kolokwium za 100 pkt (pisanie programów i algorytmów na żywo). Zdobyty bonus jest doliczany.
- Wykład zaliczany jest osobno, zgodnie z zasadami prowadzącej wykład.

### Punkty za aktywność – tylko za pracę na zajęciach

Punkt za lab dostajesz **wyłącznie**, gdy spełnisz wszystkie trzy warunki:

1. **jesteś obecny** na tych zajęciach,
2. **wszystkie testy obowiązkowe (★)** przechodzą,
3. Twój `git push` **dotarł na GitHub przed końcem zajęć** (godzina końca jest w harmonogramie).

- Liczy się **czas pushu na GitHubie** – godzina uruchomienia testów w zakładce **Actions** Twojego forka.
  **Data commita się nie liczy**, bo można ją zmienić na własnym komputerze.
- Praca wysłana **po zajęciach – nawet minutę później – nie dostaje punktu.** Nie ma późniejszego oddawania,
  dosyłania poprawek ani zaliczania labu zdalnie.
- **Nieobecność = 0 pkt aktywności** za ten lab. Zadania możesz zrobić w domu dla siebie (i warto), ale punktów za nie nie ma.
- Dlatego na Lab 01 włączasz GitHub Actions w forku – bez tego nie da się potwierdzić czasu oddania.
- Jedyny wyjątek: awaria po stronie uczelni lub GitHuba, zgłoszona prowadzącemu **w trakcie zajęć**.

## Zasady korzystania z AI

- AI (ChatGPT, GitHub Copilot, Claude itp.) służy do **nauki i wyjaśniania**, nie do oddawania gotowych rozwiązań.
- **AI nie zastępuje myślenia.** Każdy oddany kod musisz umieć wyjaśnić. Prowadzący może poprosić o to na zajęciach.
- Na labach 07, 13 i 14 są **bloki pracy z AI 🤖**. Tam AI używamy celowo, według instrukcji w README labu.
- Na **kolokwiach AI jest zakazane**.

## Uczciwość akademicka

Przywłaszczenie cudzego kodu lub jego fragmentów, w tym ukrycie źródła, jest plagiatem.
Praca nosząca znamiona plagiatu otrzymuje 0 pkt, a sprawa może trafić do postępowania dyscyplinarnego,
zgodnie z polityką Akademii Leona Koźmińskiego.

## Literatura

**Obowiązkowa**
- E. Matthes, *Python. Instrukcje dla programisty*, Helion, 2023
- M. Dawson, *Python dla każdego. Podstawy programowania*, Helion, 2015
- L. Ramalho, *Zaawansowany Python. Jasne, zwięzłe i efektywne programowanie*, Promise, 2020

**Uzupełniająca**
- I. Kalb, *Python zorientowany obiektowo. Programowanie gier i graficznych interfejsów użytkownika*, 2022

## Slajdy

Slajdy (`slajdy.md`) są w formacie [Marp](https://marp.app). Podgląd w VS Code daje rozszerzenie
*Marp for VS Code*: otwórz plik i kliknij ikonę podglądu. Motyw ładuje się automatycznie z `.vscode/settings.json`.
