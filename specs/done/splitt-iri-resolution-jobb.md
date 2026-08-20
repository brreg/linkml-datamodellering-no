# Plan: splitt iri-resolution-jobben i modell-analyse i to jobbar

## Bakgrunn og motivasjon

`modell-analyse`-workflowen sin `iri-resolution`-jobb gjer i dag to ulike ting
i eitt steg: testar IRI-dereferering (kan IRI-en hentast over HTTP i det heile)
og testar innhaldsforhandling (`Accept: text/turtle`, `Accept-Language: nb/en`
for IRI-ar repoet sjølv eig). Begge skriv til éin rapportfil
(`iri-resolution-report.md`) via éin make-target (`analyse-iri-resolution`)
som kallar éitt Python-script (`check-iri-resolution.py`) sitt `main()`, som
igjen kallar begge `print_*`-funksjonane etter kvarandre.

Brukaren ønskjer at desse to testane vert splitta i to separate GitHub
Actions-jobbar, slik at dei køyrer og rapporterer uavhengig av kvarandre
(eiga rapportfil, eige steg-summary, eige artifact).

**Namnekonvensjon (brukarval):** dei to nye jobbane/make-måla/rapportfilene
skal bruke norske namn som matchar overskriftene rapporten alt brukar
("IRI-dereferering" / "Innhaldsforhandling"), jf.
`specs/done/iri-dereferering-terminologi.md`:

| Konsept | Jobbnamn | Make-target | Rapportfil |
|---|---|---|---|
| IRI-dereferering | `iri-dereferering` | `analyse-iri-dereferering` | `iri-dereferering-report.md` |
| Innhaldsforhandling | `innhaldsforhandling` | `analyse-innhaldsforhandling` | `innhaldsforhandling-report.md` |

Det gamle jobbnamnet `iri-resolution`, targeten `analyse-iri-resolution` og
rapportfila `iri-resolution-report.md` vert fjerna til fordel for desse to.
Ingen andre filer i repoet refererer desse namna utanfor dei fem filene lista
i steg 1-5 (verifisert med grep), så dette er trygt å endre.

**Implementasjon av `check-iri-resolution.py`:** for å halde DRY (delt
skjema-oppdaging, IRI-innsamling, HTTP-sjekk-hjelparar) held scriptet fram
som éitt script, men får eit nytt `--check {dereferering,innhaldsforhandling}`
CLI-flagg som styrer kva for éin `print_*`-funksjon `main()` kallar. Filnamnet
`check-iri-resolution.py` er ein teknisk identifikator (ikkje norsk prosa) og
held fram uendra, jf. presedens i `specs/done/iri-dereferering-terminologi.md`.

## Steg

1. **`src/assets/scripts/makefile/check-iri-resolution.py`**
   - Legg til `--check {dereferering,innhaldsforhandling}` (`required=True`)
     i `argparse`
   - `main()`: kall berre `print_resolution_report(...)` når
     `--check dereferering`, berre `print_content_negotiation_report(...)`
     når `--check innhaldsforhandling`
   - Oppdater docstring til å nemne at scriptet no vert kalla separat for
     kvar av dei to testane (via `--check`)

2. **`make/91-modell-analyse.mk`**
   - Erstatt `analyse-iri-resolution`-targeten med to targets:
     `analyse-iri-dereferering` og `analyse-innhaldsforhandling`, kvar med
     sin eigen `--check`-verdi til scriptet
   - Oppdater `.PHONY`-lista
   - Oppdater header-kommentaren (linje 13-16, script-referanse-lista)

3. **`.github/workflows/modell-analyse.yml`**
   - Erstatt `iri-resolution`-jobben (linje 126-152) med to separate jobbar
     `iri-dereferering` og `innhaldsforhandling`, kvar strukturert som dei
     eksisterande `similar-*`-jobbane (checkout → bygg python-container →
     køyr make-target til eiga rapportfil + step summary → last opp eige
     artifact)
   - Oppdater `sammendrag`-jobben sin `needs:`-liste: byt ut `iri-resolution`
     med `iri-dereferering` og `innhaldsforhandling`
   - Oppdater header-kommentaren (linje 4-5) om det trengst

4. **`src/assets/scripts/makefile/summarise-modell-analyse.py`**
   - `CHECKS`-lista: begge rader (`"IRI-dereferering"` og
     `"Innhaldsforhandling"`) peikar i dag på same fil
     (`iri-resolution-report.md`) — oppdater til å peike på kvar si nye
     rapportfil (`iri-dereferering-report.md` / `innhaldsforhandling-report.md`)
   - Oppdater docstring (linje 3-10) sin omtale av kor mange rapportfiler som
     vert lest (no seks separate filer, ikkje fem — den eine gamle
     `iri-resolution-report.md` vert til to)

5. **`COMMANDS.md`**
   - Erstatt raden for `make analyse-iri-resolution` (linje 312) med to rader:
     éi for `make analyse-iri-dereferering` og éi for
     `make analyse-innhaldsforhandling`, kvar med si eiga skildring henta frå
     den noverande kombinerte skildringa

6. **Actionlint** — køyr
   `podman run --rm -v "$(pwd)":/repo:ro -w /repo docker.io/rhysd/actionlint:latest -color .github/workflows/modell-analyse.yml`
   etter steg 3, jf. CLAUDE.md § «Actionlint etter CI-endring»

7. **Verifiser** — køyr
   `make analyse-iri-dereferering DOMAIN=fair > /tmp/iri-dereferering-report.md`
   og `make analyse-innhaldsforhandling DOMAIN=fair > /tmp/innhaldsforhandling-report.md`,
   stadfest at kvar rapport berre inneheld sin eigen seksjon, og køyr deretter
   `make analyse-sammendrag` (etter å ha kopiert dei to filene til rett
   filnamn i arbeidskatalogen) for å stadfeste at dei oppdaterte regex-ane i
   steg 4 framleis parsar begge rapportane korrekt

## Handlingsliste

- [x] Steg 1: `check-iri-resolution.py`
- [x] Steg 2: `91-modell-analyse.mk`
- [x] Steg 3: `modell-analyse.yml`
- [x] Steg 4: `summarise-modell-analyse.py`
- [x] Steg 5: `COMMANDS.md`
- [x] Steg 6: actionlint
- [x] Steg 7: verifiser med `make analyse-iri-dereferering` + `make analyse-innhaldsforhandling` + `make analyse-sammendrag`

## Utført

Alle sju steg gjennomførte. `check-iri-resolution.py` fekk eit nytt
`--check {dereferering,innhaldsforhandling}`-flagg (`main()` kallar no berre
éin av dei to `print_*`-funksjonane per køyring); innhaldsforhandling-
rapporten sin overskrift vart heva frå `##` til `#` sidan han no er ein
sjølvstendig rapportfil. `91-modell-analyse.mk` fekk to nye targets
(`analyse-iri-dereferering`, `analyse-innhaldsforhandling`) i staden for
`analyse-iri-resolution`. `modell-analyse.yml` fekk to nye jobbar
(`iri-dereferering`, `innhaldsforhandling`) i staden for `iri-resolution`,
kvar med eiga rapportfil og artifact; `sammendrag`-jobben sin `needs:`-liste
oppdatert tilsvarande. Actionlint køyrt mot den endra workflow-fila —
ingen `[expression]`-feil. `summarise-modell-analyse.py` sin `CHECKS`-liste
oppdatert til å peike på dei to nye rapportfilnamna. `COMMANDS.md` fekk to
separate rader i staden for éi kombinert.

Verifisert med `make analyse-iri-dereferering DOMAIN=fair` og
`make analyse-innhaldsforhandling DOMAIN=fair`: kvar rapport inneheld no
berre sin eigen seksjon (høvesvis "IRI-dereferering (IRI resolution)" og
"Innhaldsforhandling (Content negotiation)"). Deretter verifisert at
`make analyse-sammendrag` framleis parsar begge dei nye rapportfilnamna
korrekt ("IRI-dereferering: 1/6", "Innhaldsforhandling: 6/6" for
fair-domenet).
