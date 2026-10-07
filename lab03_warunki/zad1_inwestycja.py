# Lab 03 – Zadanie 1 (★): „Jak zainwestować?” – prosty system decyzyjny
#
# Program pyta kolejno o:
#   1. kwotę w zł (float),
#   2. horyzont inwestycji w latach (int),
#   3. profil ryzyka: niskie / średnie / wysokie (tekst),
# i wypisuje JEDNĄ rekomendację według reguł (sprawdzaj w tej kolejności!):
#
#   kwota < 1000                       -> "Najpierw zbuduj poduszkę finansową"
#   horyzont < 2                       -> "Lokata lub konto oszczędnościowe"
#   ryzyko niskie                      -> "Obligacje skarbowe"
#   ryzyko średnie                     -> "Fundusz mieszany"
#   ryzyko wysokie i horyzont >= 5     -> "Fundusz akcji (ETF)"
#   ryzyko wysokie i horyzont < 5      -> "Fundusz mieszany"
#   inny tekst                         -> "Nieznany profil ryzyka"
#
# Profil ryzyka porównuj bez względu na wielkość liter i spacje:
#   risk = input(...).strip().lower()
#
# To ćwiczenie z instrukcji warunkowych, a nie porada inwestycyjna. :)

# TODO: Twój kod poniżej
