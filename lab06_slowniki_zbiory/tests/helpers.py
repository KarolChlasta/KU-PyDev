"""Narzędzia do testowania skryptów (laby 01–06).

Testy uruchamiają Twój skrypt jak zwykły program: podają dane na wejście
(tak, jakbyś wpisywał je z klawiatury) i sprawdzają, co skrypt wypisał.
Nie musisz tego pliku zmieniać ani rozumieć – wystarczy uruchomić testy.
"""
import os
import re
import subprocess
import sys
import unittest
from pathlib import Path

# Folder z plikami zadań: domyślnie folder labu (rodzic folderu tests/).
# Prowadzący może wskazać inny folder zmienną środowiskową LAB_DIR.
LAB_DIR = Path(os.environ.get("LAB_DIR", Path(__file__).resolve().parent.parent))

NUMBER_PATTERN = re.compile(r"-?\d+(?:\.\d+)?")


def numbers(text):
    """Zwraca listę wszystkich liczb występujących w tekście."""
    return [float(n) for n in NUMBER_PATTERN.findall(text)]


class ScriptTestCase(unittest.TestCase):
    def run_script(self, script, stdin="", env=None):
        path = LAB_DIR / script
        self.assertTrue(path.exists(), f"Brak pliku {script}")
        env = {**os.environ, "PYTHONIOENCODING": "utf-8", **(env or {})}
        try:
            result = subprocess.run(
                [sys.executable, str(path)],
                input=stdin, capture_output=True, text=True,
                encoding="utf-8", timeout=10, env=env, cwd=LAB_DIR,
            )
        except subprocess.TimeoutExpired:
            self.fail(f"{script} działa dłużej niż 10 s – czeka na dodatkowe dane albo ma nieskończoną pętlę?")
        self.assertEqual(result.returncode, 0, f"{script} zakończył się błędem:\n{result.stderr}")
        return result.stdout

    def assertContainsNumber(self, text, expected, tolerance=0.01):
        found = numbers(text)
        self.assertTrue(
            any(abs(n - expected) <= tolerance for n in found),
            f"Oczekiwano liczby {expected} w wyjściu programu:\n---\n{text}---",
        )
