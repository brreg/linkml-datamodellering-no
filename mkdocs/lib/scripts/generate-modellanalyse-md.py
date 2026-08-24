#!/usr/bin/env python3
"""
Genererer ein ## Modellanalyse-seksjon frå dei per-skjema
modellanalyse-rapportane (similar-classes/-slots/-types-domain-report.md,
ubrukte-slots/-enums/-types/-subsets-report.md,
isolerte-klasser-report.md) til stdout.

Rapportfilene vert skrivne av generate.yml sitt «Køyr modellanalyse per
skjema»-steg (make analyse-similar-classes-domain/-slots-domain/-types-domain
og make analyse-ubrukte-slots/-enums/-types/-subsets/analyse-isolerte-klasser
NAME=<skjema>/SCHEMA=<sti>) til generated/<domain>/<schema>/model-analyse/ —
sjå specs/done/modellanalyse-per-skjema-index-md.md,
specs/backlog/modellanalyse-liknande-typenamn.md og
specs/backlog/modellanalyse-ubrukte-lokale-definisjonar.md. Dei er
domene-scopa/per-skjema-scopa (ikkje cross-domain) og reint offline
(ingen IRI-/nettverkssjekkar) — sjå den fyrste spec-en for grunngjeving.

Kvar rapportfil startar med si eiga "# ..."-overskrift (frå
find-similar-names.py/find-unused-local-definitions.py) — denne vert
stroken og erstatta med ei eiga ###-underoverskrift her, sidan rapporten
vert nesta inn i denne sida sin eigen ## Modellanalyse-seksjon.

Cross-domain-fotnote: fram til no enda kvar underseksjon med ei fast
fotnote som peika til modell-analyse.yml-workflowen i GitHub Actions —
ikkje til noka konkret fil. Dei tre similar-*-domain-analysane har no ein
faktisk publisert cross-domain-motpart (--scope all, køyrd éin gong i
generate.yml sin publish-jobb og publisert som statiske sider under
mkdocs/docs/modellanalyse/ av mkdocs/publish.sh), så fotnota for desse
lenkar no direkte til den sida i staden. Dei fem ubrukt-lokalt/isolert-
analysane har inga meiningsfull cross-domain-form (dei er per definisjon
per-skjema) og får difor ingen fotnote i det heile — sjå
cross_domain_report_relpath=None per oppføring under.

Funntal i overskrifta: kvar underoverskrift viser talet på funn i
parentes ("### Liknande klassenavn (same domene) (3)"), etter same
mønster som ### Slots (13) lenger oppe på sida. Talet vert utleidd
generisk frå rapportkroppen (talet på `|`-tabellrader minus header-/
skiljerad) i staden for parsa frå kvar rapport sin eigen menneskelesbare
"Totalt: ..."-linje — sjå count_table_rows(). Manglande/uleseleg
rapportfil får ingen parentes (ikkje "(0)", som ville sett ut som eit
stadfesta nullfunn).

Bruk: python3 generate-modellanalyse-md.py <model-analyse-dir> <domain> <schema>
"""

import sys
from pathlib import Path

# (rapportfil, ###-overskrift, objekttype brukt i fotnoteteksten,
#  relativ sti til cross-domain-sida frå mkdocs/docs/<domain>/<schema>/index.md
#  (None = ingen cross-domain-ekvivalent, ingen fotnote), fotnote-lenkjetekst)
REPORTS = [
    (
        "isolerte-klasser-report.md",
        "Isolerte klasser",
        "isolerte klasser",
        None,
        None,
    ),
    (
        "ubrukte-slots-report.md",
        "Ubrukte slots",
        "ubrukte slots",
        None,
        None,
    ),
    (
        "ubrukte-types-report.md",
        "Ubrukte types",
        "ubrukte types",
        None,
        None,
    ),
    (
        "ubrukte-enums-report.md",
        "Ubrukte enumerations",
        "ubrukte enumerations",
        None,
        None,
    ),
    (
        "ubrukte-subsets-report.md",
        "Ubrukte subsets",
        "ubrukte subsets",
        None,
        None,
    ),
    (
        "similar-classes-domain-report.md",
        "Liknande klassenavn",
        "klassenavn",
        "../../modellanalyse/liknande-klassenavn-alle-domene.md",
        "Analyse av klassenavn på tvers av alle domene",
    ),
    (
        "similar-slots-domain-report.md",
        "Liknande slotnavn",
        "slotnavn",
        "../../modellanalyse/liknande-slotnavn-alle-domene.md",
        "Analyse av slotnavn på tvers av alle domene",
    ),
    (
        "similar-types-domain-report.md",
        "Liknande typenavn",
        "typenavn",
        "../../modellanalyse/liknande-typenavn-alle-domene.md",
        "Analyse av typenavn på tvers av alle domene",
    ),
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


def count_table_rows(body: str) -> int:
    """Talet på funn i rapporten: talet på `|`-tabellrader i body, minus
    header- og skiljerad. 0 når rapporten ikkje har nokon tabell (ingen
    funn) — sjå moduldocstring § "Funntal i overskrifta"."""
    pipe_lines = [line for line in body.splitlines() if line.strip().startswith("|")]
    if len(pipe_lines) < 2:
        return 0
    return len(pipe_lines) - 2


def main() -> None:
    if len(sys.argv) < 4:
        print(
            "Bruk: generate-modellanalyse-md.py <model-analyse-dir> <domain> <schema>",
            file=sys.stderr,
        )
        sys.exit(1)

    analyse_dir = Path(sys.argv[1])
    # domain/schema er ikkje brukt i sjølve formateringa i dag (cross-domain-
    # relativstiane er faste — alle skjema-index.md ligg to nivå under
    # mkdocs/docs/), men tekne imot for symmetri med generate-validation-md.py
    # sitt grensesnitt og for framtidig bruk.
    _domain = sys.argv[2]
    _schema = sys.argv[3]

    lines = [
        "",
        "## Modellanalyse",
        "",
        "> Modellanalysen samanliknar dette skjemaet sine lokalt definerte "
        "klasse-, slot- og typenavn mot andre skjema i same domene, flaggar "
        "par med høg navnelikskap som eit mogleg duplikat- eller "
        "konsolideringssignal, og fangar lokalt definerte slots, "
        "enumerations, types, subsets og klassar som ikkje er i bruk lokalt "
        "i modellen. Analysen er informativ, ikkje ein valideringspolicy.",
        "",
        f"*For IRI-dereferering og innhaldsforhandling sjå "
        f"[Modell-analyse]({MODELL_ANALYSE_WORKFLOW_URL})-workflowen.*",
    ]

    any_report_found = False
    for filename, heading, objekttype, cross_domain_relpath, cross_domain_label in REPORTS:
        report_path = analyse_dir / filename
        body = None
        if not report_path.is_file():
            print(f"ÅTVARING: fann ikkje {report_path}", file=sys.stderr)
        else:
            any_report_found = True
            try:
                body = strip_own_heading(report_path.read_text(encoding="utf-8"))
            except Exception as e:
                print(f"ÅTVARING: klarte ikkje lese {report_path}: {e}", file=sys.stderr)

        if body is None:
            lines += ["", f"### {heading}", ""]
            lines.append("*Rapport ikkje tilgjengeleg for denne bygginga.*")
        else:
            lines += ["", f"### {heading} ({count_table_rows(body)})", ""]
            lines.append(body)

        if cross_domain_relpath:
            lines += [
                "",
                f"*For fullstendig analyse av {objekttype} på tvers av domene sjå "
                f"[{cross_domain_label}]({cross_domain_relpath}).*",
            ]

    if not any_report_found:
        print(f"ÅTVARING: ingen modellanalyse-rapportar funne i {analyse_dir}", file=sys.stderr)

    print("\n".join(lines))


if __name__ == "__main__":
    main()
