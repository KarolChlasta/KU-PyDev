"""Lab 10 – Zadanie 4 (☆, dodatkowe): Kursy walut z API Narodowego Banku Polskiego.

Wymaga pakietu zewnętrznego:  pip install requests
API (bez klucza):  https://api.nbp.pl/api/exchangerates/rates/a/<kod>/?format=json
Odpowiedź, np.:
    {"table": "A", "currency": "euro", "code": "EUR",
     "rates": [{"no": "194/A/NBP/2026", "effectiveDate": "2026-10-06", "mid": 4.3699}]}
"""

URL = "https://api.nbp.pl/api/exchangerates/rates/a/{code}/?format=json"


def fetch_json(url):
    """Pobiera JSON spod adresu (requests.get(url, timeout=10).json())."""
    import requests  # import tutaj: testy nie wymagają zainstalowanego requests
    raise NotImplementedError


def parse_rate(data):
    """Z odpowiedzi API zwraca krotkę (kod, data, kurs_średni), np. ("EUR", "2026-10-06", 4.3699)."""
    raise NotImplementedError


def get_rate(code, fetch=fetch_json):
    """Pobiera i parsuje kurs waluty. Kod w adresie MAŁYMI literami.

    Parametr fetch pozwala testom podstawić atrapę zamiast prawdziwego internetu.
    """
    raise NotImplementedError


def convert_pln(amount_pln, rate):
    """Ile waluty kupisz za amount_pln złotych przy danym kursie."""
    raise NotImplementedError


if __name__ == "__main__":
    code, day, mid = get_rate(input("Kod waluty (np. EUR): "))
    print(f"1 {code} = {mid} PLN (kurs średni NBP z {day})")
