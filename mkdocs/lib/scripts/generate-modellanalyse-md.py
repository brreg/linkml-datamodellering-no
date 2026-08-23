#!/usr/bin/env python3
"""
Genererer ein ## Modellanalyse-seksjon frå dei to per-skjema
modellanalyse-rapportane (similar-classes-domain-report.md,
similar-slots-domain-report.md) til stdout.

Rapportfilene vert skrivne av generate.yml sitt «Køyr modellanalyse per
skjema»-steg (make analyse-similar-classes-domain/-slots-domain NAME=<skjema>)
til generated/<domain>/<schema>/model-analyse/ — sjå
specs/done/modellanalyse-per-skjema-index-md.md. Dei er domene-scopa
(ikkje cross-domain) og reint offline (ingen IRI-/nettverkssjekkar) — sjå
spec-en for grunngjeving. IRI-dereferering, innhaldsforhandling og
cross-domain-samanlikning køyrer framleis berre i den vekentlege
modell-analyse.yml-workflowen; denne seksjonen lenkar dit i staden for å
duplisere dei.

Kvar rapportfil startar med si eiga "# Liknande ..."-overskrift (frå
find-similar-names.py) — denne vert stroken og erstatta med ei eiga
###-underoverskrift her, sidan rapporten vert nesta inn i denne sida sin
eigen ## Modellanalyse-seksjon.

Bruk: python3 generate-modellanalyse-md.py <model-analyse-dir> <domain> <schema>
"""

import sys
from pathlib import Path

REPORTS = [
    ("similar-classes-domain-report.md", "Liknande klassenamn (same domene)"),
    ("similar-slots-domain-report.md", "Liknande slotnamn (same domene)"),
]

MODELL_ANALYSE_WORKFLOW_URL = (
    "https://github.com/brreg/linkml-datamodellering-no/actions/workflows/modell-analyse.yml"
)


def strip_own_heading(text: str) -> str:
    """Fjernar rapporten si eiga '# ...'-toppoverskrift (+ tom linje etter)."""
    lines = text.splitlines()
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
        if lines and lines[0].strip() == "":
            lines = lines[1:]
    return "\n".join(lines).rstrip("\n")


def main() -> None:
    if len(sys.argv) < 4:
        print(
            "Bruk: generate-modellanalyse-md.py <model-analyse-dir> <domain> <schema>",
            file=sys.stderr,
        )
        sys.exit(1)

    analyse_dir = Path(sys.argv[1])
    # domain/schema er ikkje brukt i sjølve formateringa i dag, men tekne imot
    # for symmetri med generate-validation-md.py sitt grensesnitt og for
    # framtidig bruk (t.d. lenkjer tilbake til skjemaet).
    _domain = sys.argv[2]
    _schema = sys.argv[3]

    lines = [
        "",
        "## Modellanalyse",
        "",
        "> Modellanalysen samanliknar dette skjemaet sine lokalt definerte "
        "klasse- og slotnamn mot andre skjema i same domene, og flaggar par "
        "med høg namnelikskap som eit mogleg duplikat- eller "
        "konsolideringssignal. Analysen er informativ, ikkje ein "
        "valideringspolicy — han feilar aldri bygget.",
    ]

    any_report_found = False
    for filename, heading in REPORTS:
        report_path = analyse_dir / filename
        lines += ["", f"### {heading}", ""]
        if not report_path.is_file():
            print(f"ÅTVARING: fann ikkje {report_path}", file=sys.stderr)
            lines.append("*Rapport ikkje tilgjengeleg for denne bygginga.*")
            continue
        any_report_found = True
        try:
            body = strip_own_heading(report_path.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"ÅTVARING: klarte ikkje lese {report_path}: {e}", file=sys.stderr)
            lines.append("*Rapport ikkje tilgjengeleg for denne bygginga.*")
            continue
        lines.append(body)

    lines += [
        "",
        f"> IRI-dereferering, innhaldsforhandling og samanlikning på tvers av "
        f"alle domene køyrer vekentleg i "
        f"[Modell-analyse]({MODELL_ANALYSE_WORKFLOW_URL})-workflowen, "
        f"ikkje her.",
    ]

    if not any_report_found:
        print(f"ÅTVARING: ingen modellanalyse-rapportar funne i {analyse_dir}", file=sys.stderr)

    print("\n".join(lines))


if __name__ == "__main__":
    main()
