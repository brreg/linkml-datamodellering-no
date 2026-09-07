# Rein vurderings-/kartleggings-spec skal bli i backlog, ikkje flyttast til done

## Bakgrunn

Ei nyleg spec (`vscode-plugin-linkml-modellering.md`) vart oppretta på
brukaren sin instruks om å **evaluere** ein idé og skrive resultatet til
`specs/`, utan at noko konkret skulle utførast utover sjølve evalueringa.
Specen vart likevel flytta til `specs/done/` ved avslutning, etter same
mønster som specar der faktiske tiltak (kodeendringar, konfigurasjon) er
utførte. Brukaren peika på at dette er feil: når instruksen berre er å få
laga sjølve specen — utan at noko i han skal utførast — skal specen bli
verande i `specs/backlog/`. `specs/done/` skal reserverast for specar der
konkrete tiltak faktisk er gjennomførte.

## Steg

1. Utvid CLAUDE.md § "Arbeidsflyt", steg 5, delsteg (d): legg til eit
   unntak — dersom brukaren sin instruks berre var å få laga sjølve
   specen, utan at noko i han skal utførast (t.d. ei rein
   kartlegging/vurdering der specen sjølv er heile leveransen), skal
   specen bli verande i `specs/backlog/` i staden for å flyttast til
   `specs/done/`.
2. Rett den feilaktige plasseringa av `vscode-plugin-linkml-modellering.md`
   — flytt han attende frå `specs/done/` til `specs/backlog/`, sidan han
   er nettopp eit slikt reint vurderingsoppdrag.

## Prioritert handlingsliste

| # | Steg | Fil | Merknad |
|---|---|---|---|
| 1 | Legg til unntak i Avslutning-steget | `CLAUDE.md` (Arbeidsflyt, steg 5d) | |
| 2 | Flytt feilplassert spec attende til backlog | `specs/done/vscode-plugin-linkml-modellering.md` → `specs/backlog/` | Korrigering av førre økt sin feil |

## Avgjerder

- **Retta den konkrete feilplasseringa av `vscode-plugin-linkml-modellering.md`
  same økt, utan å spørje først.** Grunngjeving: brukaren sin instruks var
  generell (oppdater CLAUDE.md-regelen), men peika direkte på ein feil eg
  nettopp hadde gjort — å la den feilaktige plasseringa stå att medan
  regelen vart retta ville vore inkonsekvent, og flytting av ein fil
  mellom to spec-mapper er ei låg-risiko, reversibel handling.
- **Denne specen sjølv går til `specs/done/`, ikkje `specs/backlog/`,**
  sjølv om han handlar om nett dette skiljet. Grunngjeving: i motsetnad
  til `vscode-plugin-linkml-modellering.md` inneheld denne specen eit
  konkret utført tiltak (redigering av `CLAUDE.md` + filflytting), ikkje
  berre ei vurdering — han fell difor utanfor unntaket han sjølv
  innfører, og skal følgje hovudregelen i steg 5.

## Utført

- `CLAUDE.md` § "Arbeidsflyt", steg 5(d): lagt til unntak for spec-typar
  utan utføring — dei skal bli verande i `specs/backlog/`.
- `specs/done/vscode-plugin-linkml-modellering.md` flytta attende til
  `specs/backlog/vscode-plugin-linkml-modellering.md`.
