# Lab 04 – Zadanie 4 (★): Zgadywanka
#
# Komputer losuje liczbę 1–100, a gracz zgaduje. Po każdej próbie program pisze:
#     Za mało!  /  Za dużo!
# a po trafieniu:
#     Brawo! Zgadłeś w 3 próbach.
#
# Jeśli gracz wpisze coś, co nie jest liczbą, wypisz "To nie jest liczba"
# i użyj continue (taka próba się nie liczy).
#
# Liczby nie zmieniaj – testy ustawiają ją przez zmienną środowiskową SEKRET:

import os
import random

SECRET = int(os.environ.get("SEKRET", random.randint(1, 100)))

# TODO: Twój kod poniżej (pętla while)
