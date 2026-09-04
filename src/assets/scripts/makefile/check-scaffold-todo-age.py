#!/usr/bin/env python3
"""
Finn skjema med uendra scaffold-TODO frå `new-modell.sh` sitt standard-
import (`# TODO: endre/legg til imports etter behov`), og flagg dei som
er eldre enn ein terskel — ein uendra TODO kort tid etter oppretting er
normalt (skjemaet er under aktiv utvikling), men éin som står uendra
månadsvis er ofte gløymd importgjeld (jf.
specs/done/evaluering-gjentakande-monster-backlog.md, P4).

Alder vert rekna frå første commit som la til fila (`git log
--diff-filter=A --follow`), ikkje siste endring — ei fil som er redigert
mykje av andre grunnar, men der akkurat denne TODO-linja aldri er rørt,
skal framleis reknast som gammal.

Feilar aldri (ikkje ein valideringspolicy — informativ rapport, same
mønster som resten av analyse-*-familien, sjå COMMANDS.md § "Modell-analyse").

Ingen eksterne avhengigheiter (rein `git log` + tekstsøk).

Bruk:
    python3 check-scaffold-todo-age.py [--threshold-days 90]
"""

import argparse
import subprocess
from datetime import datetime, timezone
from pathlib import Path

SCHEMA_DIR = Path("src/linkml")
TODO_MARKER = "# TODO: endre/legg til imports etter behov"
DEFAULT_THRESHOLD_DAYS = 90


def discover_schemas() -> list[Path]:
    return sorted(SCHEMA_DIR.glob("*/*/*-schema.yaml"))


def find_todo_line(path: Path) -> int | None:
    for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if TODO_MARKER in line:
            return lineno
    return None


def creation_date(path: Path) -> datetime | None:
    """Datoen fila fyrst vart lagt til i git-historikken, eller None dersom
    fila ikkje er spora (t.d. nyleg oppretta, ikkje committa enno)."""
    result = subprocess.run(
        ["git", "log", "--diff-filter=A", "--follow", "--format=%cI", "--", str(path)],
        capture_output=True, text=True, check=False,
    )
    lines = [line for line in result.stdout.splitlines() if line.strip()]
    if not lines:
        return None
    return datetime.fromisoformat(lines[-1])


def find_stale_todos(threshold_days: int) -> list[tuple[Path, int, int]]:
    """Returnerer (sti, linjenummer, alder_i_dagar) for skjema med uendra
    TODO eldre enn terskelen."""
    now = datetime.now(timezone.utc)
    stale = []
    for path in discover_schemas():
        lineno = find_todo_line(path)
        if lineno is None:
            continue
        created = creation_date(path)
        if created is None:
            continue
        age_days = (now - created).days
        if age_days >= threshold_days:
            stale.append((path, lineno, age_days))
    return stale


def build_report(stale: list[tuple[Path, int, int]], threshold_days: int, total_checked: int) -> str:
    lines = [f"# Uendra scaffold-TODO (importgjeld) eldre enn {threshold_days} dagar", ""]
    if not stale:
        lines.append(
            f"Ingen skjema med uendra scaffold-TODO eldre enn {threshold_days} dagar "
            f"({total_checked} skjema sjekka)."
        )
        return "\n".join(lines)

    lines.append(f"**{len(stale)} av {total_checked} skjema har uendra scaffold-TODO:**")
    lines.append("")
    lines.append("| Skjema | Linje | Alder (dagar) |")
    lines.append("|---|---|---|")
    for path, lineno, age_days in sorted(stale, key=lambda x: -x[2]):
        lines.append(f"| `{path}` | {lineno} | {age_days} |")
    lines.append("")
    lines.append(
        "Vurder om importen frå `new-modell.sh` sitt scaffold framleis er "
        "nødvendig (sjå kva klassar/slots skjemaet faktisk brukar), eller "
        "om han bør fjernast/erstattast — og fjern TODO-kommentaren når "
        "importen er vurdert, uansett utfall."
    )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--threshold-days", type=int, default=DEFAULT_THRESHOLD_DAYS)
    args = parser.parse_args()

    schemas = discover_schemas()
    stale = find_stale_todos(args.threshold_days)
    print(build_report(stale, args.threshold_days, len(schemas)))


if __name__ == "__main__":
    main()
