# Fiks: seksjon-index-duplikat i Rettleiingar-menyen

## Bakgrunn

`specs/done/mkdocs-seksjon-index-sider/spec.md` la til fire landingssider
(`kom-i-gang.md`, `arkitektur.md`, `publisering.md`, `automasjon.md`) som
**flate filer** direkte i `mkdocs/docs/`, for å unngå å flytte dei 17
eksisterande søskensidene inn i undermapper.

Dette bryt føresetnaden for `navigation.indexes` (slått på i
`mkdocs/publish.sh` sin `features:`-blokk): MkDocs koplar berre ei
landingsside til sjølve seksjonsoverskrifta når fila er attkjend som
katalogen sin index-side — noko som i praksis krev at fila heiter
bokstaveleg `index.md`. Alle andre fungerande seksjonar i nav-treet
(`Rettleiingar` → `index.md`, `REFERANSE` → `referanse/index.md`,
`ap-no` → `ap-no/index.md`, osv.) følgjer dette mønsteret.

## Rot-årsak (verifisert empirisk)

Bygd `mkdocs/site/index.html` og inspisert nav-HTML-en direkte:

- **REFERANSE** (fungerer): seksjonsoverskrifta er ei ekte lenke
  (`<a href="referanse/">`), og det finst **ingen** duplikat-oppføring i
  lista under.
- **Kom i gang** (feilar): seksjonsoverskrifta er berre ein
  ekspander/kollaps-`<label>` **utan** `href` — ikkje klikkbar. Første
  element i lista under er `kom-i-gang/` med synleg tekst "Kom i gang",
  identisk med seksjonsnamnet → oppfattast som duplikat.

Same feil gjeld Arkitektur, Publisering og Automasjon.

## Løysing

Flytt **berre dei fire landingssidene** til eigne undermapper som
`index.md`, slik REFERANSE og domenesidene alt gjer. Dei 17 søskensidene
(`ny-org.md`, `arkitektur-oversikt.md`, `monitorering.md` osv.) vert
**ikkje** flytta — dei ligg framleis flatt i `mkdocs/docs/`, og
nav-stiane til dei (i `publish.sh`) er uendra.

## Steg

1. Flytt `mkdocs/docs/kom-i-gang.md` → `mkdocs/docs/kom-i-gang/index.md`
   (og tilsvarande for `arkitektur.md`, `publisering.md`,
   `automasjon.md`).
2. Rett interne relative lenkjer **inni** dei fire flytta filene:
   - Lenkjer til søskensider (t.d. `ny-org.md`) → `../ny-org.md`
   - Lenkjer til framsida (`index.md#kom-i-gang`) → `../index.md#kom-i-gang`
   - Kryss-lenkjer mellom dei fire landingssidene (t.d.
     `arkitektur.md` inni `kom-i-gang.md`) → `../arkitektur/` (peikar til
     den nye undermappa, ikkje fila direkte, sidan ho no er ei
     index-side)
3. Oppdater `mkdocs/publish.sh` sin `nav:`-heredoc (kring linje 514-543):
   - `kom-i-gang.md` → `kom-i-gang/index.md`
   - `arkitektur.md` → `arkitektur/index.md`
   - `publisering.md` → `publisering/index.md`
   - `automasjon.md` → `automasjon/index.md`
4. Verifiser med `make docs-publish` (steg 1 skal ikkje røre dei nye
   undermappene, sidan `kom-i-gang`/`arkitektur`/`publisering`/`automasjon`
   ikkje finst som domene i `generated/`) og `make docs-build`.
5. Inspiser generert `mkdocs/site/index.html`: seksjonsoverskriftene skal
   no rendrast som ekte `<a href="...">`-lenkjer, og det skal **ikkje**
   finnast duplikat-oppføringar med same tekst som seksjonsnamnet rett
   under.

## Handlingsliste

- [x] Flytt dei fire filene til `<seksjon>/index.md`
- [x] Rett relative lenkjer i alle fire filene
- [x] Oppdater `nav:`-heredoc i `publish.sh`
- [x] Køyr `make docs-publish` og `make docs-build`
- [x] Verifiser nav-HTML for alle fire seksjonar (ingen duplikat, klikkbar
      overskrift)

## Utført

- Flytta `kom-i-gang.md`, `arkitektur.md`, `publisering.md`, `automasjon.md`
  til `<seksjon>/index.md` og retta alle interne relative lenkjer (til
  søskensider, til framsida, og kryss-lenkjer mellom dei fire sidene)
- Oppdaterte `nav:`-heredoc i `mkdocs/publish.sh` til å peike på
  `<seksjon>/index.md`
- **Ekstra rot-årsak oppdaga under verifisering:** `publish.sh` sitt Steg 1
  har ei ryddesløyfe som slettar `mkdocs/docs/<mappe>/` for kvar mappe utan
  tilhøyrande `generated/<mappe>/` (unnateke ei kvitliste med
  `stylesheets`/`javascripts`). Denne sletta dei fire nye undermappene ved
  første `make docs-publish`. Lagt til `kom-i-gang|arkitektur|publisering|automasjon`
  i kvitlista i same sløyfe.
- Verifisert med `make docs-publish` (undermappene overlever no
  ryddesteget) og `make docs-build` (ingen nye WARNING/ERROR-linjer).
  Inspiserte generert `mkdocs/site/index.html` direkte: alle fire
  seksjonsoverskrifter rendrast no som ekte `<a href="...">`-lenkjer
  (identisk struktur til REFERANSE), og barnelista under kvar seksjon startar
  rett på første reelle søskenside — ingen duplikat-oppføring med
  seksjonsnamnet lenger
