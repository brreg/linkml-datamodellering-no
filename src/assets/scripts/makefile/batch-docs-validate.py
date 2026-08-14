#!/usr/bin/env python3
"""
Batch-valider FLEIRE gen-docs-output-katalogar (.md-filer) i éin prosess,
med parallelle filopningar via ein trådpool.

Bakgrunn: `test_gen_docs()` i tests/test_make.sh sjekka tidlegare KVART
.md-fil ÅLEINE (find + [ -s ] + grep -q '^#') i ein bash-while-løkke —
gen-docs produserer 60-225+ .md-filer PER SKJEMA (éin per klasse/slot/
enum/type), så dette var 60-225 separate filopningar PER SKJEMA, 35
gonger. Målt på eitt skjema (enhetsregisteret-bvrinn, 225 filer): 4,8s
totalt, men berre ~1,15s var faktisk CPU-tid (user+sys) — resten var
I/O-VENTETID, venteleg forverra av at repoet ligg under WSL2 sin
Windows-filsystem-bru (/mnt/c), som har målbar per-fil-overhead for
MANGE SMÅ sekvensielle filoperasjonar. Summert over 35 skjema målt til
~221s i Fase B åleine. Sjå
specs/backlog/gjer-gen-docs-raskare-fase-b.md.

Denne batchen adresserer BEGGE kostnadskjeldene:
1. Amortiserer ikkje berre kontainar-oppstart (som dei andre batch-
   skripta), men også PROSESS-SPAWN-overhead: 225 separate `grep`-kall
   vart til 225 reine Python read()-kall i éin allereie-køyrande prosess.
2. Sjekkar FILENE PARALLELT via ThreadPoolExecutor (I/O-bunde arbeid —
   Python sin GIL vert sloppen under fil-I/O, så mange samstundes
   opningar overlappar VENTETIDA i staden for å stable ho sekvensielt).

Bruk:
  python3 batch-docs-validate.py --jobs-tsv <fil>

  jobs.tsv: éi jobb per linje, tab-separert:
    schema<TAB>docsdir

Skriv `::error file=<schema>::` til stderr for feila skjema (same
attribueringsformat som dei andre batch-skripta) — grep-bart av
phase_a_check() i tests/test_make.sh. Maks éi feillinje per skjema
(fyrste problemet funne), same granularitet som den opphavlege
test_gen_docs()-sjekken.
"""

from __future__ import annotations

import argparse
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path


def log_error(msg: str) -> None:
    print(f"[ERROR] {msg}", file=sys.stderr)


def log_info(msg: str) -> None:
    print(msg, file=sys.stderr)


def load_jobs(jobs_tsv: str) -> list[tuple[str, str]]:
    jobs = []
    for line in Path(jobs_tsv).read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        schema, docsdir = line.split("\t")
        jobs.append((schema, docsdir))
    return jobs


def check_file(f: Path) -> str | None:
    """Returnerer ei feilmelding, eller None dersom fila er OK."""
    try:
        text = f.read_text(encoding="utf-8", errors="replace")
    except OSError as exc:
        return f"Kunne ikkje lese {f}: {exc}"
    if not text:
        return f"Tom fil: {f}"
    if not any(line.startswith("#") for line in text.splitlines()):
        return f"Manglar #-overskrift: {f}"
    return None


def check_schema(docsdir: str, pool: ThreadPoolExecutor) -> str | None:
    d = Path(docsdir)
    if not d.is_dir():
        return f"Katalog manglar: {docsdir}"
    md_files = sorted(d.rglob("*.md"))
    if not md_files:
        return f"Ingen .md-filer i {docsdir}"
    for result in pool.map(check_file, md_files):
        if result is not None:
            return result
    return None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--jobs-tsv", required=True)
    args = parser.parse_args()

    jobs = load_jobs(args.jobs_tsv)

    failed = 0
    with ThreadPoolExecutor(max_workers=32) as pool:
        for schema, docsdir in jobs:
            error = check_schema(docsdir, pool)
            if error is not None:
                log_error(f"::error file={schema}::{error}")
                failed += 1
            else:
                log_info(f"→ docs-validity  {schema}")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
