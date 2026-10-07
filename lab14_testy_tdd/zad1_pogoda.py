"""Lab 14 – Zadanie 1 (★): „Aplikacja pogodowa” w podejściu TDD.

Pracuj w cyklu RED → GREEN → REFACTOR:
  1. uruchom testy i zobacz czerwony test (RED),
  2. napisz NAJPROSTSZY kod, który go spełnia (GREEN),
  3. popraw czytelność, nie psując testów (REFACTOR) – i weź kolejny czerwony test.

API Open-Meteo (bez klucza), odpowiedź m.in.:
  {"daily": {"time": ["2027-01-19", ...], "temperature_2m_max": [-2.5, ...]}}
"""
import json
import urllib.request

BASE_URL = "https://api.open-meteo.com/v1/forecast"


def celsius_to_fahrenheit(celsius):
    raise NotImplementedError


def classify(temp):
    """< 0 "mróz", < 10 "zimno", < 20 "umiarkowanie", < 28 "ciepło", w przeciwnym razie "upał"."""
    raise NotImplementedError


def parse_forecast(data):
    """Zamienia odpowiedź API na listę słowników [{"day": "2027-01-19", "temp": -2.5}, ...]."""
    raise NotImplementedError


def average_temperature(forecast):
    """Średnia z pól "temp"; dla pustej prognozy – ValueError."""
    raise NotImplementedError


def warmest_day(forecast):
    """Krotka (dzień, temperatura) dla najcieplejszego dnia; dla pustej prognozy – ValueError."""
    raise NotImplementedError


def build_url(latitude, longitude, days):
    """Adres zapytania – dokładnie w tej postaci (strefa czasowa zakodowana jako Europe%2FWarsaw):
    https://api.open-meteo.com/v1/forecast?latitude=52.23&longitude=21.01&daily=temperature_2m_max&timezone=Europe%2FWarsaw&forecast_days=3
    """
    raise NotImplementedError


def get_json(url):
    """Pobiera JSON z internetu (biblioteka standardowa – bez requests).

    Testy PODMIENIAJĄ tę funkcję atrapą (mock), żeby nie łączyć się z siecią.
    """
    with urllib.request.urlopen(url, timeout=10) as response:
        return json.load(response)


def fetch_forecast(latitude, longitude, days=3):
    """Pobiera (get_json) i parsuje (parse_forecast) prognozę."""
    raise NotImplementedError


if __name__ == "__main__":
    forecast = fetch_forecast(52.23, 21.01, 7)          # Warszawa
    for entry in forecast:
        print(f"{entry['day']}: {entry['temp']:5.1f} °C  {classify(entry['temp'])}")
    print(f"Średnio: {average_temperature(forecast):.1f} °C, najcieplej: {warmest_day(forecast)}")
