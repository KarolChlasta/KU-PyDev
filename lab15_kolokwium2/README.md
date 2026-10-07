# Lab 15 – 📝 Kolokwium II

📅 **wtorek 26.01.2027, 08:30–11:45** · 📍 **sala A/111** · ⏱ 120 min pisania
**Sylabus:** treść nr 30 · **Efekty:** U1, U2, U3, KS1 · **Waga:** 50 pkt (połowa oceny z laboratorium) · **Slajdy:** [slajdy.md](slajdy.md)

## Zakres

Laby **09–14** (z wiedzą z labów 01–07 jako bazą):

| Lab | Temat |
|---|---|
| 09 | pliki tekstowe, `with`, JSON |
| 10 | moduły i pakiety |
| 11 | `datetime`, `math`, `statistics` |
| 12 | wyjątki: `try` / `except` / `finally`, `raise`, własne klasy wyjątków |
| 13 | sortowanie, wyszukiwanie binarne, Big O |
| 14 | testy jednostkowe `unittest` |

## Przebieg

- **3 zadania, razem 50 pkt**:
  1. **pliki i wyjątki** (ok. 15 pkt) – wczytanie danych, pomijanie błędnych linii, własny wyjątek,
  2. **algorytm** (ok. 20 pkt) – własne sortowanie (bez `sorted()`) i wyszukiwanie binarne,
  3. **testy** (ok. 15 pkt) – piszesz testy do gotowego modułu; punkty za wykryte błędy (jak mutanty w labie 14).
- Dwie grupy (A i B) z różnymi zadaniami. Zasady, oddawanie i ocenianie – jak na [Kolokwium I](../lab08_kolokwium1/).

## Zasady

- ✅ Wolno: VS Code, terminal, dokumentacja Pythona (*docs.python.org*), notatki **na papierze**.
- ❌ Nie wolno: **AI**, komunikatory, internet poza dokumentacją, cudzy kod, telefon.

## Jak się przygotować

| Plik | Temat |
|---|---|
| `przyklad1_wyniki.py` | wczytywanie wyników z CSV, błędne linie, własny wyjątek |
| `przyklad2_ranking.py` | sortowanie przez wstawianie z dwoma kryteriami, wyszukiwanie binarne |

```bash
cd lab15_kolokwium2
python -m unittest discover -s tests -v
```

Do zadania 3 poćwicz na labie 14: czy Twoje `test_moje_arytmetyka.py` zabija wszystkie mutanty?

## Termin drugi

Jedno kolokwium za 100 pkt z zakresu całego laboratorium – termin poda prowadzący.
