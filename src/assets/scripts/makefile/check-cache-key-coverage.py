#!/usr/bin/env python3
"""
Sjekk at cache-nøklar med same namneprefiks er byte-for-byte identiske på
tvers av alle .github/workflows/*.yml-filer.

Løyser IKKJE det generelle "er dette hashFiles(...)-globet korrekt i det
heile"-spørsmålet (det krev kjennskap til kvar jobb sin faktiske kallgraf,
og må framleis vurderast manuelt når ein cache-nøkkel vert oppretta eller
endra). Fangar i staden éin spesifikk, faktisk observert regresjonsklasse:
to eller fleire cache-steg som er MEINT å dele cache-innslag på tvers av
workflowar (t.d. fordi GitHub Actions-cache ikkje er isolert per workflow —
sjå .github/workflows/lenkje-og-mermaid-sjekk.yml sin kommentar om
"v4-generated"), men som har drive frå kvarandre etter at berre éin stad
vart oppdatert.

Metode: for kvar `key:`-linje i alle workflow-filer, hent ut det statiske
namneprefikset (t.d. "v4-generated" frå "v4-generated-${{ matrix.domain
}}-..."). Grupper alle funne key-linjer etter dette prefikset. Innanfor
kvar gruppe med meir enn éi fil: samanlikn heile `hashFiles(...)`-innhaldet
(alle kall på linja, normalisert). Ulikt innhald for same prefiks på tvers
av filer vert rapportert som eit avvik.

Ingen eksterne avhengigheiter (rein regex — ingen YAML-parsing nødvendig,
sidan `${{ }}`-uttrykk ikkje er gyldig YAML-verdisyntaks i alle høve).

Bruk:
    python3 check-cache-key-coverage.py
"""

import re
from pathlib import Path

WORKFLOW_DIR = Path(".github/workflows")

KEY_LINE_RE = re.compile(r"^\s*key:\s*(.+)$")
PREFIX_RE = re.compile(r"^([A-Za-z0-9_.-]+?)-?\$\{\{")
HASHFILES_RE = re.compile(r"hashFiles\(([^)]*)\)")


def discover_workflows() -> list[Path]:
    return sorted(WORKFLOW_DIR.glob("*.yml"))


def extract_key_lines(path: Path) -> list[tuple[int, str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    return [
        (lineno, m.group(1).strip())
        for lineno, line in enumerate(lines, start=1)
        if (m := KEY_LINE_RE.match(line))
    ]


def key_prefix(key_value: str) -> str | None:
    m = PREFIX_RE.match(key_value)
    return m.group(1) if m else None


def normalized_hashfiles(key_value: str) -> tuple[str, ...]:
    """Sorterte, kvitteikn-normaliserte hashFiles(...)-kall-argument på linja."""
    return tuple(sorted(" ".join(arg.split()) for arg in HASHFILES_RE.findall(key_value)))


def collect_entries() -> dict[str, list[tuple[Path, int, str, tuple[str, ...]]]]:
    groups: dict[str, list[tuple[Path, int, str, tuple[str, ...]]]] = {}
    for path in discover_workflows():
        for lineno, key_value in extract_key_lines(path):
            prefix = key_prefix(key_value)
            if prefix is None:
                continue
            groups.setdefault(prefix, []).append(
                (path, lineno, key_value, normalized_hashfiles(key_value))
            )
    return groups


def find_divergent_groups(
    groups: dict[str, list[tuple[Path, int, str, tuple[str, ...]]]],
) -> dict[str, list[tuple[Path, int, str, tuple[str, ...]]]]:
    divergent = {}
    for prefix, entries in groups.items():
        if len(entries) < 2:
            continue
        distinct_hashfiles = {e[3] for e in entries}
        if len(distinct_hashfiles) > 1:
            divergent[prefix] = entries
    return divergent


def build_report(
    divergent: dict[str, list[tuple[Path, int, str, tuple[str, ...]]]],
    total_groups: int,
) -> str:
    lines = ["# Konsistens for delte cache-nøklar på tvers av workflow-filer", ""]
    if not divergent:
        lines.append(
            f"Ingen avvik funne ({total_groups} nøkkel-prefiks sjekka, "
            f"kvar med meir enn éi førekomst er byte-for-byte identiske)."
        )
        return "\n".join(lines)

    lines.append(
        f"**{len(divergent)} av {total_groups} nøkkel-prefiks har divergert "
        f"på tvers av workflow-filer.**"
    )
    lines.append("")
    for prefix in sorted(divergent):
        lines.append(f"## `{prefix}`")
        lines.append("")
        for path, lineno, key_value, _ in divergent[prefix]:
            lines.append(f"- `{path}:{lineno}`")
        lines.append("")
        lines.append(
            "`hashFiles(...)`-innhaldet skil seg mellom desse — dersom nøkkelen "
            "er meint å delast på tvers av workflow-filer (same cache-innslag), "
            "må fil-lista i `hashFiles(...)` vere identisk alle stader. Sjå "
            "specs/done/evaluering-gjentakande-monster-backlog.md (P3)."
        )
        lines.append("")
    return "\n".join(lines)


def main() -> None:
    groups = collect_entries()
    divergent = find_divergent_groups(groups)
    print(build_report(divergent, len(groups)))


if __name__ == "__main__":
    main()
