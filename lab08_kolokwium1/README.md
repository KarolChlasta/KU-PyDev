# Lab 08 – 📝 Kolokwium I

📅 **środa 02.12.2026, 14:00–17:15** · 📍 **sala A/136** · ⏱ 120 min pisania
**Sylabus:** treść nr 16 · **Efekty:** U1, U2, U3, KS1 · **Waga:** 50 pkt (połowa oceny z laboratorium) · **Slajdy:** [slajdy.md](slajdy.md)

## Zakres

Laby **01–07**:

| Lab | Temat |
|---|---|
| 01–02 | zmienne, typy, `input()`/`print()`, f-stringi, operatory, konwersje |
| 03 | `if` / `elif` / `else`, operatory logiczne |
| 04 | pętle `for` i `while`, `range`, `break`, `continue` |
| 05 | listy i krotki, indeksy, wycinki, metody list |
| 06 | słowniki i zbiory |
| 07 | funkcje, parametry, `return`, rekurencja, `lambda` |

## Przebieg

- **3 zadania, razem 50 pkt**, rosnąca trudność (ok. 10 + 15 + 25 pkt):
  1. **skrypt** z `input()` i `print()` (jak w labach 01–06),
  2. **funkcje** na słownikach / listach (jak w labie 07),
  3. **algorytm** zapisany jako funkcje (pętle, warunki, ewentualnie rekurencja).
- Dwie grupy (A i B) z różnymi zadaniami.
- Piszesz na komputerze w sali, w VS Code. Zadania i sposób oddania podaje prowadzący na początku kolokwium.
- Do każdego zadania dostajesz **testy jawne** – możesz je uruchamiać w trakcie.

## Zasady

- ✅ Wolno: VS Code, terminal, dokumentacja Pythona (*docs.python.org*), własne notatki **na papierze**.
- ❌ Nie wolno: **AI** (Copilot, ChatGPT itp.), komunikatory, internet poza dokumentacją, cudzy kod, telefon.
- Naruszenie zasad = 0 pkt z kolokwium (zgodnie z polityką plagiatu ALK).

## Ocenianie

- Punkty za zadanie są proporcjonalne do **zaliczonych testów sprawdzających** (prowadzący ma ich więcej niż testów jawnych).
- Prowadzący może skorygować wynik po przejrzeniu kodu, np. za rozwiązanie „pod testy” (wpisane na sztywno wyniki) albo za czytelność.
- Kod, który się nie uruchamia (błąd składni), nie zalicza testów **tego zadania** – pozostałe zadania liczą się normalnie.

## Jak się przygotować

Rozwiąż przykładowe zadania z tego folderu – mają testy jak na kolokwium:

| Plik | Typ | Temat |
|---|---|---|
| `przyklad1_temperatury.py` | skrypt | statystyka temperatur do pustej linii |
| `przyklad2_magazyn.py` | funkcje | stan magazynu w słowniku |
| `przyklad3_tekst.py` | algorytm | kompresja RLE, anagramy |

```bash
cd lab08_kolokwium1
python -m unittest discover -s tests -v
```

Powtórz też zadania ★ z labów 01–07 i spróbuj je napisać **od zera, bez podglądania**, w ograniczonym czasie.

## Termin drugi

Jedno kolokwium za 100 pkt z zakresu całego laboratorium (laby 01–14) – termin poda prowadzący.
