"""Testy zadań obowiązkowych (★) – Lab 10."""
import importlib
import math
import unittest

from helpers import LAB_DIR, load


class TestZad1PakietGeometria(unittest.TestCase):
    def setUp(self):
        self.pkg = importlib.import_module("geometria")
        self.flat = importlib.import_module("geometria.plaskie")
        self.solid = importlib.import_module("geometria.bryly")

    def test_package_version(self):
        self.assertEqual(self.pkg.__version__, "1.0.0")

    def test_flat_shapes(self):
        self.assertAlmostEqual(self.flat.circle_area(1), math.pi)
        self.assertEqual(self.flat.rectangle_area(2, 3), 6)
        self.assertAlmostEqual(self.flat.triangle_area(3, 4, 5), 6)
        self.assertIsNone(self.flat.triangle_area(1, 2, 10))

    def test_solids(self):
        self.assertAlmostEqual(self.solid.sphere_volume(3), 36 * math.pi)
        self.assertEqual(self.solid.cuboid_volume(2, 3, 4), 24)
        self.assertAlmostEqual(self.solid.cylinder_volume(1, 2), 2 * math.pi)

    def test_package_reexports_functions(self):
        self.assertIs(self.pkg.circle_area, self.flat.circle_area)
        self.assertIs(self.pkg.sphere_volume, self.solid.sphere_volume)


class TestZad2Raport(unittest.TestCase):
    def test_total_area(self):
        report = load("zad2_raport.py")
        shapes = [("koło", 1), ("prostokąt", 2, 3), ("trójkąt", 3, 4, 5)]
        self.assertAlmostEqual(report.total_area(shapes), math.pi + 12)

    def test_unknown_shape_is_skipped(self):
        report = load("zad2_raport.py")
        self.assertEqual(report.total_area([("sześciokąt", 1), ("prostokąt", 1, 1)]), 1)


class TestZad3Requirements(unittest.TestCase):
    def test_requirements_file_lists_requests(self):
        path = LAB_DIR / "requirements.txt"
        self.assertTrue(path.exists(), "Brak pliku requirements.txt – zobacz README, część „Środowisko wirtualne”")
        names = [line.split("==")[0].strip().lower() for line in path.read_text(encoding="utf-8").splitlines()]
        self.assertIn("requests", names)
