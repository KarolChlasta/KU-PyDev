"""Narzędzia do testowania funkcji (laby 07–14).

Testy importują Twój plik jak moduł i wywołują jego funkcje.
Kod pod  if __name__ == "__main__":  NIE jest wtedy uruchamiany –
dlatego input() i print() trzymaj w funkcji main().
Nie musisz tego pliku zmieniać ani rozumieć – wystarczy uruchomić testy.
"""
import importlib.util
import os
import sys
from pathlib import Path

# Folder z plikami zadań: domyślnie folder labu (rodzic folderu tests/).
# Prowadzący może wskazać inny folder zmienną środowiskową LAB_DIR.
LAB_DIR = Path(os.environ.get("LAB_DIR", Path(__file__).resolve().parent.parent))
DATA_DIR = Path(__file__).resolve().parent.parent / "dane"

if str(LAB_DIR) not in sys.path:
    sys.path.insert(0, str(LAB_DIR))


def load(filename):
    """Importuje plik zadania (np. "zad1_kalkulator.py") i zwraca go jako moduł."""
    path = LAB_DIR / filename
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[path.stem] = module
    spec.loader.exec_module(module)
    return module
