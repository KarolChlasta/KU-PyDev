# Lab 05 – Zadanie 4 (☆, dodatkowe): Gra „znajdź parę” (memory)
#
# Na stole leży 8 zakrytych kart (pozycje 0–7), po dwie z każdej litery.
# Gracz podaje dwie pozycje oddzielone spacją, np.  0 4
#   - jeśli karty są takie same: "Para!"  (karty zostają odkryte)
#   - jeśli różne: "Pudło"
#   - jeśli podał dwa razy tę samą pozycję: "Podaj dwie różne karty" (ruch się nie liczy)
# Po odkryciu wszystkich par: "Koniec gry w 5 ruchach"
#
# Przed każdym ruchem wypisz stół, np.:  ? ? A ? ? ? A ?
#
# Testy ustawiają BEZ_TASOWANIA, żeby układ kart był znany:

import os
import random

cards = ["A", "B", "C", "D", "A", "B", "C", "D"]
if "BEZ_TASOWANIA" not in os.environ:
    random.shuffle(cards)
revealed = [False] * len(cards)

# TODO: Twój kod poniżej
