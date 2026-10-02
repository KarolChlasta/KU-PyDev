# Przygotowanie środowiska

Zrób to raz, najlepiej przed pierwszymi zajęciami (06.10.2026). W razie problemów zrobimy to razem na Lab 01.

## 1. Python 3.12 lub nowszy

- Pobierz z [python.org/downloads](https://www.python.org/downloads/).
- **Windows:** w instalatorze zaznacz **„Add python.exe to PATH”**.
- Sprawdź w terminalu:

```bash
python --version      # Windows
python3 --version     # macOS / Linux
```

> Na macOS/Linux w poleceniach z instrukcji wpisuj `python3` zamiast `python`. Na Windows działa też `py`.

## 2. Visual Studio Code

- Pobierz z [code.visualstudio.com](https://code.visualstudio.com).
- Zainstaluj rozszerzenia (Ctrl+Shift+X):
  - **Python** (Microsoft),
  - **Marp for VS Code** – podgląd slajdów (opcjonalnie).

## 3. Git i konto GitHub

- Zainstaluj Git: [git-scm.com](https://git-scm.com/downloads). Na Windows zostaw domyślne opcje.
- Załóż konto na [github.com](https://github.com). Możesz użyć adresu uczelnianego.
- Skonfiguruj Git (raz):

```bash
git config --global user.name "Imię Nazwisko"
git config --global user.email "twoj@email"
```

- Polecane: [GitHub Education](https://education.github.com) (darmowy GitHub Copilot dla studentów, przyda się na labach z AI).

## 4. Fork i klonowanie repozytorium

1. Wejdź na [github.com/KarolChlasta/KU-PyDev](https://github.com/KarolChlasta/KU-PyDev) i kliknij **Fork** → **Create fork**.
2. W swoim forku otwórz zakładkę **Actions** i włącz workflowy (przycisk „I understand my workflows, go ahead and enable them”). Dzięki temu po każdym `git push` zobaczysz ✅ lub ❌ przy testach obowiązkowych.
3. Sklonuj **swój** fork:

```bash
git clone https://github.com/TWOJ_LOGIN/KU-PyDev.git
cd KU-PyDev
code .
```

Przy pierwszym `git push` przeglądarka poprosi o zalogowanie do GitHuba.

## 5. Praca na zajęciach

```bash
# na początku zajęć – pobierz nowy lab
#   (GitHub → Twój fork → Sync fork → Update branch)
git pull

# praca
cd lab01_podstawy
python zad1_hello.py                       # uruchom swój program
python -m unittest discover -s tests -v    # sprawdź testami

# oddanie (z folderu labu)
git add .
git commit -m "Lab 01"
git push
```

## 6. Najczęstsze problemy

| Problem | Rozwiązanie |
|---|---|
| `python: command not found` / `'python' is not recognized` | Windows: zainstaluj ponownie z „Add to PATH” albo użyj `py`. macOS/Linux: `python3` |
| Testy zawieszają się | Program czeka na więcej danych (`input()`), niż podaje test, albo ma nieskończoną pętlę |
| `ValueError: could not convert string to float: '1,75'` | Liczby dziesiętne wpisuj z kropką: `1.75` |
| `git push` odrzucony (`rejected`) | Najpierw `git pull`, potem ponownie `git push` |
| Lab 11, Windows: `ZoneInfoNotFoundError` | `python -m pip install tzdata` |
