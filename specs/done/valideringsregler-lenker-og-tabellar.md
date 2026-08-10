# Interne lenker og tabellkonsolidering i valideringsregler.md

**Kjelde:** `src/mcp-linkml-validator/policies/README.md` (genererer `mkdocs/docs/arkitektur/valideringsregler.md` verbatim via `mkdocs/publish.sh::generate_validation_docs()`)

---

## Bakgrunn

Brukaren ba om tre relaterte endringar i `arkitektur/valideringsregler.md`:

1. "Nivå for skjemakvalitet"-tabellen skal lenke kvar rad til tilhøyrande overskrift
   (`### bronze`, `### silver`, `### gold`) i same dokument.
2. Publiseringspolicyer (`felles-datakatalog`, `felles-begrepskatalog`) manglar ein
   tilsvarande oversiktstabell — legg til éin under `## Publiseringspolicyer` som listar
   alle publiseringspolicyane, med lenker til overskriftene deira.
3. Kvar publiseringspolicy skal dokumenterast som **éin** tabell, tilsvarande måten
   bronze/silver/gold har éin samla tabell kvar — i dag er kvar publiseringspolicy delt
   opp i fleire småtabellar (Import og prefiks, Containerklasse, `Begrep`-krav,
   Tospråkskrav, Instanssjekk osv.).

Sidan `valideringsregler.md` vert generert direkte frå `policies/README.md` (kun med
sed-justering av relative lenker til GitHub-URI-ar), skjer alle endringane i README.md —
ikkje i den genererte fila.

**Avklart med brukar:** Den samanslåtte publiseringspolicy-tabellen skal ha ein
`Kategori`-kolonne som tek vare på grupperinga (Import og prefiks, Containerklasse,
Begrep-krav, Tospråkskrav, Instanssjekk) som elles ville gått tapt ved samanslåing.
Kolonnerekkjefølgje: `Kategori | Krav | Alvor | Kode`.

## Steg

1. Legg lenker i "Nivå for skjemakvalitet"-tabellen (`Nivå`-kolonnen) til `#bronze`,
   `#silver`, `#gold`-ankera.
2. Legg til ny tabell under `## Publiseringspolicyer` som listar `felles-begrepskatalog`
   og `felles-datakatalog` med lenker til sine `###`-overskrifter, tilsvarande struktur
   som "Nivå for skjemakvalitet".
3. Konsolider `### felles-begrepskatalog` til éin tabell (`Kategori | Krav | Alvor | Kode`)
   — behald prose-merknadar (avgrensing, tospråk-forklaring) som tekst under tabellen.
4. Konsolider `### felles-datakatalog` til éin tabell på same måte.
5. Verifiser at ankera README.md genererer (GitHub-stil slugs) stemmer med
   mkdocs-material sin slug-algoritme (begge brukar lowercase + bindestrek), slik at
   lenkene fungerer både på GitHub og i mkdocs-portalen.

## Handlingsliste

- [x] Steg 1 — lenker i Nivå-tabellen
- [x] Steg 2 — ny oversiktstabell for publiseringspolicyer
- [x] Steg 3 — konsolider felles-begrepskatalog
- [x] Steg 4 — konsolider felles-datakatalog
- [x] Steg 5 — verifiser ankerlenker

## Utført

Alle fire endringar gjort i `src/mcp-linkml-validator/policies/README.md`:

1. "Nivå for skjemakvalitet"-tabellen lenkar no `bronze`/`silver`/`gold` til `#bronze`/`#silver`/`#gold`.
2. Ny tabell under `## Publiseringspolicyer` listar `felles-begrepskatalog` og
   `felles-datakatalog` med lenker til overskriftene sine.
3. `### felles-begrepskatalog` konsolidert frå 5 småtabellar til éin tabell
   (`Kategori | Krav | Alvor | Kode`) — prose-merknadar (avgrensing, tospråk) behaldne.
4. `### felles-datakatalog` konsolidert frå 5 småtabellar til éin tabell på same måte.

Verifisert at `mkdocs/publish.sh::generate_validation_docs()` sin sed-baserte
lenkerskriving (`.yaml`- og `specs/done/`-lenker → GitHub-URI-ar) framleis fungerer
korrekt på det oppdaterte innhaldet (simulert med same sed-kommandoar mot fila).
`valideringsregler.md` vert generert på nytt neste gong `make docs-publish` køyrer.
