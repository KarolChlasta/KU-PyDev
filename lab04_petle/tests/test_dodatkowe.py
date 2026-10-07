"""Testy zadań dodatkowych (☆) – Lab 04."""
from helpers import ScriptTestCase


class TestZad5Crawler(ScriptTestCase):
    def test_counts_links_and_domains(self):
        output = self.run_script("zad5_crawler.py").lower()
        self.assertIn("liczba linków: 5", output)
        for domain in ("www.python.org", "docs.python.org", "pypi.org", "github.com"):
            self.assertIn(domain, output)
