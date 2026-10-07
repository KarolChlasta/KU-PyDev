---
marp: true
theme: warsawiq
paginate: true
header: "Podstawy programowania w języku Python I · Kolokwium II"
footer: "dr inż. Karol Chlasta · WarsawIQ · Akademia Leona Koźmińskiego · 26.01.2027"
---

<!-- _class: tytul -->

<p class="eyebrow">Akademia Leona Koźmińskiego · Informatyka, I rok · 26.01.2027</p>

# Kolokwium II
## Laby 09–14 · 50 pkt · 120 minut
**dr inż. Karol Chlasta** · WarsawIQ

---

# Zasady

- ✅ VS Code, terminal, dokumentacja Pythona (*docs.python.org*), notatki na papierze
- ❌ **AI**, komunikatory, internet poza dokumentacją, cudzy kod, telefon
- Naruszenie zasad = **0 pkt** z kolokwium
- Telefony wyciszone i schowane

---

# Przebieg

| Zadanie | Typ | Punkty |
|---|---|---|
| 1 | pliki + wyjątki | 15 |
| 2 | sortowanie i wyszukiwanie binarne (bez `sorted()`) | 20 |
| 3 | Twoje testy do gotowego modułu | 15 |

- Zadanie 3: punkty za **wykryte błędy** w ukrytych wersjach modułu – testuj wartości graniczne i wyjątki
- Ocenę wyznaczają testy sprawdzające + przegląd kodu

---

# Strategia

1. **Przeczytaj wszystkie zadania** (5 min)
2. Zadanie 3 nie wymaga pisania logiki – dobre na rozgrzewkę albo na koniec
3. Uruchamiaj testy po każdym kroku:

```bash
python -m unittest discover -s tests -v
python -m unittest test_moje_... -v
```

4. Nie zmieniaj **nazw plików, funkcji ani parametrów**; nie zmieniaj modułu z zadania 3
5. 10 minut przed końcem: sprawdź, czy wszystko się uruchamia, i oddaj

---

# Po kolokwium

- Wyniki i oceny końcowe: Teams
- Ocena z laboratorium = Kolokwium I + Kolokwium II + bonus (obecność, aktywność), progi od 100 pkt
- Termin drugi: jedno kolokwium za 100 pkt

# Dziękuję za semestr i powodzenia! 🍀
