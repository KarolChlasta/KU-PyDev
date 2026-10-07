# Lab 10 – Moduły i pakiety

📅 wtorek 15.12.2026, 08:30–11:45 · 📍 sala A/121 · ⏱ 4 h
**Sylabus:** treść nr 20 · **Efekty:** U1, U2, KS1 · **Slajdy:** [slajdy.md](slajdy.md)

## Cel zajęć

Po zajęciach potrafisz:
- importować moduły na różne sposoby i rozumieć przestrzenie nazw,
- zbudować własny pakiet z kilkoma modułami (`__init__.py`),
- utworzyć środowisko wirtualne i instalować pakiety przez `pip`,
- zapisać zależności projektu w `requirements.txt`.

## Na start: aktualizacja forka

Na GitHubie w swoim forku kliknij **Sync fork → Update branch**, a potem w terminalu: `git pull`.

## Zadania obowiązkowe ★

| Plik | Zadanie | Czas |
|---|---|---|
| `geometria/` | Pakiet: `plaskie.py` (pola), `bryly.py` (objętości), `__init__.py` (wersja i eksport funkcji) | 60 min |
| `zad2_raport.py` | Aplikacja korzystająca z pakietu `geometria` | 30 min |
| `requirements.txt` | Środowisko wirtualne + `pip install requests` + plik zależności (instrukcja niżej) | 30 min |

### Środowisko wirtualne (zadanie 3)

W folderze `lab10_moduly_pakiety`:

```bash
python -m venv .venv                 # utwórz środowisko (folder .venv jest w .gitignore)

.venv\Scripts\activate               # Windows (PowerShell)
source .venv/bin/activate            # macOS / Linux

python -m pip install requests       # instalacja pakietu z PyPI
python -m pip freeze > requirements.txt
```

Otwórz `requirements.txt` – powinna w nim być linia `requests==…` (i zależności `requests`). W VS Code wybierz interpreter z `.venv`: `Ctrl+Shift+P` → **Python: Select Interpreter**.

> Na Windows, jeśli PowerShell blokuje `activate`: `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`.

## Zadania dodatkowe ☆

| Plik | Zadanie |
|---|---|
| `zad4_kursy.py` | Kursy walut z API NBP przez `requests` |

## Jak sprawdzić rozwiązanie

```bash
python -m unittest discover -s tests -v
python zad4_kursy.py         # wymaga requests i internetu
```

## Oddanie

Do **11:45**: `git add lab10_moduly_pakiety`, `git commit -m "Lab 10"`, `git push`. Folder `.venv` **nie** trafia do repo – tylko `requirements.txt`.

> ⏰ **Punkt za aktywność tylko za push przed 11:45** – liczy się godzina na GitHubie (zakładka Actions), nie data commita. Po zajęciach, nawet minutę później, punktu już nie ma. Nieobecność = brak punktu. Wymagane: wszystkie testy ★ zielone. [Zasady](../README.md#punkty-za-aktywność--tylko-za-pracę-na-zajęciach)

## Do poczytania

- E. Matthes, *Python. Instrukcje dla programisty* – rozdz. 8 (moduły) i dodatek o środowisku
- Dokumentacja: *Modules* (*docs.python.org/3/tutorial/modules.html*), *Virtual Environments and Packages* (*docs.python.org/3/tutorial/venv.html*)
