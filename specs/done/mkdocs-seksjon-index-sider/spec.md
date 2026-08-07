# Seksjons-index-sider for mkdocs-portalen

## Bakgrunn

`mkdocs/publish.sh` sin `nav:`-heredoc (§ omkring linje 514-538) definerer tre
undergrupper i "Rettleiingar"-menyen — **Kom i gang**, **Arkitektur og
publisering** og **Korleis artefaktar vert generert** — som kvar inneheld
fleire enkeltsider. `mkdocs.yml` har `navigation.indexes` slått på
(`mkdocs/publish.sh` § `features:`), som lèt sjølve gruppenamnet vere ei
klikkbar side dersom første oppføring i lista er ei side (typisk `index.md`
i ein undermappe). I dag manglar denne landingssida for alle tre gruppene —
klikk på gruppenamnet gjer difor ingenting anna enn å ekspandere/kollapse
lista i sidemenyen.

**Oppdatert etter tilbakemelding (1):** brukaren ønskjer at "Arkitektur og
publisering" vert splitta i to sjølvstendige nav-grupper — **Arkitektur** og
**Publisering** — kvar med si eiga landingsside, i staden for éin kombinert
gruppe.

**Oppdatert etter tilbakemelding (2):** "Korleis artefaktar vert generert"
vert omdøypt til **Automasjon**, og det tidlegare frittståande toppnivå-
menypunktet **Monitorering av automasjon** (`monitorering.md`) vert flytta inn
som ei side under Automasjon-gruppa i staden for å stå åleine i "Rettleiingar"-
menyen.

Menyen får dermed fire grupper totalt under "Rettleiingar": Kom i gang,
Arkitektur, Publisering, Automasjon.

Denne specen dekkjer **berre utkast til innhald** for dei fire landingssidene.
Utkasta ligg i denne mappa, klare for gjennomsyn, før dei vert kopierte inn i
`mkdocs/docs/` og kopla inn i `publish.sh` sin `nav:`-heredoc.

## Avklaring: filplassering

mkdocs-material sin vanlege konvensjon for seksjons-index er
`mkdocs/docs/<seksjon>/index.md` (undermappe). Denne vart **ikkje** brukt:
alle eksisterande søskensider (`ny-org.md`, `arkitektur-oversikt.md`,
`monitorering.md` osv.) ligg flatt direkte under `mkdocs/docs/`, ikkje i
undermapper. Ei undermappe-plassering ville krevd anten å flytte alle 17
eksisterande sider inn i sine respektive undermapper (stor, unødvendig
omrokkering), eller å skrive `../`-relative lenkjer i landingssidene som
ville brote dei enkle same-mappe-lenkjene til søskensidene.

Landingssidene vart difor lagt som **flate filer** direkte i
`mkdocs/docs/`: `kom-i-gang.md`, `arkitektur.md`, `publisering.md`,
`automasjon.md`. Dette har òg ein praktisk fordel: `publish.sh` sitt steg 1
ryddar vekk `mkdocs/docs/<mappe>/` for mapper som ikkje finst i
`generated/<domain>/` — flate filer vert aldri råka av denne opprydjinga,
så ingen endring var nødvendig i sjølve rydjelogikken.

## Utført

- Fire nye landingssider oppretta i `mkdocs/docs/`: `kom-i-gang.md`,
  `arkitektur.md`, `publisering.md`, `automasjon.md` (kopiert frå utkasta i
  denne mappa, med kryssreferansane retta til flate sti-referansar)
- `automasjon.md` inneheld no `monitorering.md` som siste rad i tabellen
- `mkdocs/publish.sh` sin `nav:`-heredoc oppdatert:
  - "Arkitektur og publisering" splitta til to grupper: **Arkitektur** og
    **Publisering**
  - "Korleis artefaktar vert generert" omdøypt til **Automasjon**
  - `Monitorering av automasjon: monitorering.md` flytta frå eige
    toppnivå-menypunkt til siste rad i Automasjon-gruppa
  - Kvar av dei fire gruppene har no si eiga landingsside (`kom-i-gang.md`,
    `arkitektur.md`, `publisering.md`, `automasjon.md`) som første oppføring
- Verifisert med `make docs-publish` (steg 1-4 fullførte utan feil, dei fire
  flate filene overlevde rydjesteget) og `make docs-build` (ingen nye
  `WARNING`/`ERROR`-linjer knytt til endringane — dei einaste `INFO`-linjene
  i output var førehandseksisterande, urelaterte lenkje-hint for
  `ap-no`-delmodellar og eitt manglande anker i `index.md`)
- Bygd site sjekka manuelt: `mkdocs/site/kom-i-gang/index.html`,
  `arkitektur/index.html`, `publisering/index.html`, `automasjon/index.html`
  finst, og nav-titlane "Arkitektur", "Publisering", "Automasjon" er
  til stades i søkeindeksen
