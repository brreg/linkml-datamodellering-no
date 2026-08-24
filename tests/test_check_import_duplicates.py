#!/usr/bin/env python3
"""Automatiske testar for check-import-duplicates.py.

Køyr frå repo-rot (krev linkml, sjå make check-import-duplicates-test):
  python3 -m pytest tests/test_check_import_duplicates.py -v

Testfixturane ligg i tests/fixtures/check-import-duplicates-*.yaml og dannar
eit lite, sjølvstendig import-hierarki (base → middle/no-collision/
direct-collision → transitive-collision) — ingen nettverkstilgang kravd,
i motsetnad til dei faktiske oreg-skjemaa scriptet vart skrive for å
beskytte (sjå specs/backlog/new-modell-dublettsjekk-mot-imports.md).
"""

import subprocess
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPT = REPO_ROOT / "src" / "assets" / "scripts" / "makefile" / "check-import-duplicates.py"
FIXTURES = REPO_ROOT / "tests" / "fixtures"


def run_check(*schema_names: str) -> subprocess.CompletedProcess:
    schema_paths = [str(FIXTURES / name) for name in schema_names]
    return subprocess.run(
        [sys.executable, str(SCRIPT), *schema_paths],
        capture_output=True,
        text=True,
    )


class TestCheckImportDuplicates(unittest.TestCase):
    def test_no_collision_passes(self):
        """Eit skjema som berre attgjenbruker eit importert slot/klasse-navn (utan lokal
        redefinisjon) skal ikkje reknast som ein kollisjon."""
        result = run_check("check-import-duplicates-no-collision-fixture.yaml")
        self.assertEqual(result.returncode, 0, msg=result.stderr)
        self.assertNotIn("[ERROR]", result.stderr)

    def test_direct_collision_fails(self):
        """Eit lokalt redefinert slot med same navn som eit direkte (førstenivå) import
        skal fangast."""
        result = run_check("check-import-duplicates-direct-collision-fixture.yaml")
        self.assertEqual(result.returncode, 1)
        self.assertIn("dublett-navn 'felles_slot'", result.stderr)
        self.assertIn("check-import-duplicates-direct-collision-fixture.yaml", result.stderr)

    def test_transitive_collision_fails(self):
        """Ein kollisjon som berre finst via ei transitiv importkjede (A importerer B,
        B importerer C, A kolliderer med noko definert i C) skal òg fangast."""
        result = run_check("check-import-duplicates-transitive-collision-fixture.yaml")
        self.assertEqual(result.returncode, 1)
        self.assertIn("dublett-navn 'felles_slot'", result.stderr)

    def test_linkml_types_not_false_positive(self):
        """linkml:types (brukt av alle fixture-skjemaa via `range: string` osv.) skal
        aldri sjølv trigge ein rapportert kollisjon."""
        result = run_check("check-import-duplicates-base-fixture.yaml")
        self.assertEqual(result.returncode, 0, msg=result.stderr)

    def test_multiple_schemas_batched_in_one_invocation(self):
        """Fleire skjema i éitt kall skal rapportere kvart for seg — eitt kolliderande
        skjema skal ikkje stoppe sjekken av dei andre (per-skjema-isolasjon, jf.
        batch-lint.py sitt mønster)."""
        result = run_check(
            "check-import-duplicates-no-collision-fixture.yaml",
            "check-import-duplicates-direct-collision-fixture.yaml",
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("check-import-duplicates-direct-collision-fixture.yaml", result.stderr)
        self.assertNotIn("check-import-duplicates-no-collision-fixture.yaml", result.stderr)


if __name__ == "__main__":
    unittest.main()
