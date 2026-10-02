---
marp: true
theme: alk
paginate: true
footer: "Podstawy programowania w języku Python I · Lab 02 · 13.10.2026"
---

<!-- _class: tytul -->

# Lab 02
## Zmienne, typy danych i operacje arytmetyczne
dr Karol Chlasta · Akademia Leona Koźmińskiego

---

# Cel zajęć

- Typy `int`, `float`, `str` i konwersja między nimi
- Operatory arytmetyczne: `+ - * / // % **`
- Przeliczanie jednostek: temperatura, waluty, czas
- Efekty z sylabusa: **U1**, **U3** (proste algorytmy), **KS1**

---

# Z wykładu: typy i konwersje

```python
age = 20            # int
height = 1.75       # float
name = "Anna"       # str

int("42")      # 42
float("3.5")   # 3.5
str(7)         # "7"
type(height)   # <class 'float'>
```

---

# Operatory

| Operator | Przykład | Wynik |
|---|---|---|
| `/` | `7 / 2` | `3.5` |
| `//` | `7 // 2` | `3` (dzielenie całkowite) |
| `%` | `7 % 2` | `1` (reszta) |
| `**` | `2 ** 10` | `1024` |

```python
seconds = 3725
print(seconds // 3600, seconds % 3600 // 60, seconds % 60)   # 1 2 5
```

---

# Ciekawostki: liczby w komputerze 🤯

- `0.1 + 0.2 == 0.3` → **False**! Wynik to `0.30000000000000004` – ułamki dziesiętne zapisuje się w systemie dwójkowym w przybliżeniu
- `int` w Pythonie nie ma limitu: `2 ** 1000` to liczba z 302 cyframi
- `round(2.5)` → **2**, a `round(3.5)` → **4** – „zaokrąglanie bankierskie” (do parzystej)
- `-7 // 2` → **-4**, bo `//` zaokrągla w dół, nie „w stronę zera”

---

# Ciekawostki: jednostki i Fibonacci

- **Mars Climate Orbiter** (NASA, 23.09.1999) przepadł przy Marsie – oprogramowanie podawało impuls w funtach-sekundach, a system NASA oczekiwał niutonosekund (różnica 4,45×). Misja kosztowała **327,6 mln USD**
- Ciąg **Fibonacciego** wprowadził do matematyki europejskiej Leonardo z Pizy w *Liber Abaci* (1202) – jako zagadkę o rozmnażaniu królików
- −40 °C = −40 °F – jedyna temperatura równa w obu skalach

---

# Dzisiejsze zadania

| | Plik | Zadanie |
|---|---|---|
| ★ | `zad1_kalkulator.py` | 7 działań na dwóch liczbach |
| ★ | `zad2_temperatura.py` | °C ↔ °F |
| ★ | `zad3_waluty.py` | PLN → EUR, USD |
| ★ | `zad4_czas.py` | sekundy → `h min s` |
| ☆ | `zad5_fibonacci.py` | ciąg Fibonacciego |

---

# Sprawdzenie i oddanie

```bash
cd lab02_zmienne_typy
python -m unittest discover -s tests -v
git add .
git commit -m "Lab 02"
git push
```

- Punkt aktywności: **obecność + wszystkie testy ★ zielone + push na GitHub przed 11:45**
- Po zajęciach – **0 pkt**, bez wyjątków
- Pamiętaj: **Sync fork** na początku zajęć, żeby pobrać nowy lab
