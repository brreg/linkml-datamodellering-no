# Plan: `validate-modellkatalog-instance` skal akseptere alias, ikkje catalog_slug

## Bakgrunn

Oppfølging av [[argumentnavn-avvik-revisjon]]. Brukaren peika på at
`validate-modellkatalog-instance (ORG=<org-slug>)` og
`new-modellkatalog (ORG=<alias>)` bruker `ORG` ulikt.

Undersøking synte at dette er meir enn eit visingsavvik — dei to (tre,
inkl. `gen-modelldcat-elements`) targeta forventar reelt **ulike
verdiformat** for same variabelnamn:

| Target | `ORG=`-verdi | Korleis han vert brukt |
|---|---|---|
| `new-modellkatalog` | Kort CODEOWNERS-alias (t.d. `digdir`) | Slått opp mot `organizations[].alias` i `CODEOWNERS.md`-frontmatter → `catalog_slug` (`digdir-modellkatalog`) + øvrig metadata (`org_uri`, `catalog_title`, `contact_uri`) |
| `gen-modelldcat-elements` | Kort CODEOWNERS-alias | `org["alias"] == args.org` — same oppslag (`update-modellkatalog.py`) |
| `validate-modellkatalog-instance` | Full `catalog_slug` (t.d. `digdir-modellkatalog`) | Brukt **direkte** som katalognamn: `src/linkml/modellkatalog/$(ORG)/...` — inga CODEOWNERS-oppslag |

Konsekvens: `make new-modellkatalog ORG=digdir` (fungerer) følgt av
`make validate-modellkatalog-instance ORG=digdir` (feilar — filene ligg
under `.../digdir-modellkatalog/`, ikkje `.../digdir/`) er ei brukarfelle.
2 av 3 ORG-target er alt konsistente (alias); det er
`validate-modellkatalog-instance` som avvik.

**Brukarval:** la `validate-modellkatalog-instance` akseptere alias, med
same CODEOWNERS-oppslag som dei to andre — ikkje berre rename
variabelnamnet, og ikkje behalde catalog_slug-forma.

## Tiltak

1. Ny delt script `src/assets/scripts/scaffolding/resolve-catalog-slug.sh
   <alias>` — slår opp `catalog_slug` for ein alias i
   `CODEOWNERS.md`-frontmatter (delmengde av oppslaget
   `new-modellkatalog.sh` alt gjer, men berre for `catalog_slug`-feltet).
   Skriv slug til stdout, feilar med melding til stderr + exit 1 dersom
   alias ikkje finst.
2. `make/30-instances.mk`: `validate-modellkatalog-instance` sitt
   `## `-kommentar endra til `(ORG=<alias>)`, oppskrifta kallar det nye
   scriptet og byggjer stiane frå resultatet i staden for `$(ORG)` direkte.
3. Oppdater `COMMANDS.md` og `mkdocs/docs/kom-i-gang/kommandoar.md` sine
   rader for `validate-modellkatalog-instance` til å vise `ORG=<alias>`
   (eksempel `ORG=digdir`, ikkje `ORG=digdir-modellkatalog`).
4. `new-modellkatalog.sh` sin eigen, rikare CODEOWNERS-oppslagslogikk vert
   **ikkje** endra eller omfaktorert til å bruke det nye scriptet — han
   treng fire andre felt i tillegg til `catalog_slug`, og er alt
   testa/fungerande. To ulike, ikkje-identiske oppslag er under CLAUDE.md
   sin DRY-terskel (3+ identiske tilfelle).

## Handlingsliste

1. [x] Opprett `resolve-catalog-slug.sh`
2. [x] Oppdater `validate-modellkatalog-instance` i `make/30-instances.mk`
3. [x] Oppdater `COMMANDS.md` og `mkdocs/docs/kom-i-gang/kommandoar.md`
4. [x] Verifiser: `make validate-modellkatalog-instance ORG=digdir`
   (gyldig alias) og `ORG=digdir-modellkatalog` (no ugyldig — skal feile
   med tydeleg feilmelding, ikkje stille feil)

## Utført

**Uventa funn undervegs:** `resolve-catalog-slug.sh` sitt fyrste utkast
kopierte CODEOWNERS-oppslagsmønsteret frå `new-modellkatalog.sh` — som synte
seg å vere **reelt øydelagt**. `new-modellkatalog.sh` sin inline
Python-parsar sjekka `content.startswith("---")`, men `CODEOWNERS.md` sitt
organisasjonsregister er pakka i ein ` ```yaml ` Markdown-kodeblokk, ikkje
`---`-frontmatter — nøyaktig same feilklasse som BUG-16
(`bugs/codeowners-frontmatter-format-mismatch.md`), men i ein fjerde,
ufiksa duplikat. `make new-modellkatalog ORG=<alias>` feila difor **alltid**
med "FEIL: Ingen YAML-frontmatter i CODEOWNERS.md" før denne endringa.

Retta ved å la både `resolve-catalog-slug.sh` og `new-modellkatalog.sh`
delegere til den delte, korrekte parsaren i
`src/assets/scripts/utils/codeowners.py::load_codeowners()` (same parsar
`update-modellkatalog.py` alt brukte etter BUG-16) i staden for å
implementere `---`-frontmatter-parsing sjølv. Verifisert org-oppslag
isolert (`digdir` → rett `catalog_slug`/`org_uri`/m.fl.) utan å køyre heile
scaffoldinga (som ville oppretta filer).

**Koda:**
- `src/assets/scripts/scaffolding/resolve-catalog-slug.sh`: ny, delegerer
  til `utils.codeowners.load_codeowners()`
- `src/assets/scripts/scaffolding/new-modellkatalog.sh`: broken inline
  `---`-parsar bytt ut med delegering til same delte parsar
- `make/30-instances.mk`: `validate-modellkatalog-instance` sitt argument
  endra til `(ORG=<alias>)`, byggjer no stiar frå
  `resolve-catalog-slug.sh` sitt resultat i staden for `$(ORG)` direkte
- `COMMANDS.md`, `mkdocs/docs/kom-i-gang/kommandoar.md`: rader oppdaterte
  til `ORG=<alias>` (eksempel `ORG=digdir`)

**Verifisert:**
- `make validate-modellkatalog-instance ORG=digdir` → validerer korrekt
  (`No issues found`)
- `make validate-modellkatalog-instance ORG=digdir-modellkatalog` (gammalt
  format) → feilar tydeleg: "Alias 'digdir-modellkatalog' ikkje funne...
  Gyldige aliasar: brreg, digdir, kartverket, ksdigital, novari,
  skatteetaten" — ikkje stille feil, i tråd med CLAUDE.md
- `new-modellkatalog.sh` sitt org-metadata-oppslag testa isolert for
  `digdir` — returnerer no korrekt `name`/`org_uri`/`catalog_slug`/
  `catalog_title`/`contact_uri` i staden for å feile
