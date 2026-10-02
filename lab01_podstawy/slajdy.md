---
marp: true
theme: alk
paginate: true
footer: "Podstawy programowania w języku Python I · Lab 01 · 06.10.2026"
---

<!-- _class: tytul -->

# Lab 01
## Podstawy Pythona: Hello, World! i BMI
dr Karol Chlasta · Akademia Leona Koźmińskiego

---

# Cel zajęć

- Skonfigurować środowisko: **Python, VS Code, Git, GitHub**
- Napisać i uruchomić pierwsze skrypty
- Poznać zmienne, `input()`, `print()`, f-stringi
- Efekty z sylabusa: **U1** (skrypty w Pythonie), **KS1** (samodzielna praca)

---

# Z wykładu: algorytm → program → skrypt

- **Algorytm** – przepis krok po kroku, jak rozwiązać problem
- **Program** – algorytm zapisany w języku programowania
- **Interpreter** Pythona wykonuje kod instrukcja po instrukcji
- **Typowanie dynamiczne** – typ ma wartość, a nie zmienna

```python
x = 5        # int
x = "pięć"   # teraz str – Python na to pozwala
```

---

# Pierwszy program

```python
print("Hello, World!")
```

```python
name = input("Jak masz na imię? ")
print(f"Cześć, {name}!")
```

`input()` **zawsze** zwraca tekst → do obliczeń użyj `int(...)` lub `float(...)`

---

# BMI w trzech liniach

```python
weight = float(input("Masa [kg]: "))
height = float(input("Wzrost [m]: "))
print(f"BMI = {weight / height ** 2:.2f}")
```

- `**` – potęgowanie
- `:.2f` – 2 miejsca po przecinku
- liczby dziesiętne wpisujemy z **kropką**: `1.75`

---

# Ciekawostki 🐍

- Nazwa **Python** pochodzi od serialu *Latający Cyrk Monty Pythona*, nie od węża
- Guido van Rossum zaczął pisać Pythona w **grudniu 1989** jako „projekt na święta”; pierwsza publiczna wersja (0.9.0) – **luty 1991**
- Wpisz w Pythonie:
  - `import this` → *Zen Pythona* (Tim Peters)
  - `import antigravity` → komiks xkcd o Pythonie

---

# Ciekawostki: BMI

- Podstawy wskaźnika opracował belgijski astronom i statystyk **Adolphe Quetelet** w latach **1830–1850** – stąd dawna nazwa „wskaźnik Queteleta”
- Nazwę *Body Mass Index* wprowadził **Ancel Keys** w artykule z 1972 r.
- BMI nie odróżnia mięśni od tłuszczu – kulturysta może mieć „nadwagę”

---

# Dzisiejsze zadania

| | Plik | Zadanie |
|---|---|---|
| ★ | — | Konfiguracja: fork, clone, pierwszy commit |
| ★ | `zad1_hello.py` | Hello, World! |
| ★ | `zad2_wizytowka.py` | Wizytówka z f-stringiem |
| ★ | `zad3_bmi.py` | Kalkulator BMI |
| ☆ | `zad4_bmi_kategoria.py` | Kategoria BMI (zapowiedź `if`) |

---

# Sprawdzenie i oddanie

```bash
cd lab01_podstawy
python -m unittest discover -s tests -v
git add .
git commit -m "Lab 01"
git push
```

- Punkt aktywności: **obecność + wszystkie testy ★ zielone + push na GitHub przed 11:45**
- Liczy się czas na GitHubie, nie data commita. Po zajęciach – **0 pkt**, bez wyjątków
- Zaliczenie: **Kolokwium I (50) + Kolokwium II (50) + bonus do 20** (obecność + aktywność)
