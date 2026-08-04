# Skil ut policy-variantane av referansemodellen i eigne mapper

## Bakgrunn

`src/linkml/referanse/referansemodell/` inneheld i dag fire skjemafiler i same mappe:
`referansemodell-schema.yaml` (hovudskjemaet) og tre validator-demofiler
(`referansemodell-schema-bronze.yaml`, `-silver.yaml`, `-gold.yaml`) som viser
minstekrava for kvart policy-nivå.

Dette bryt med katalogkonvensjonen `src/linkml/<domain>/<modell>/<modell>-schema.yaml`
(éin skjemafil pr. mappe). `make/02-schema-discovery.mk` avleier `schema_outdir` og
`schema_key` frå **mappenamnet**, ikkje filnamnet — så alle fire filene ville fått
identisk output-katalog (`generated/referanse/referansemodell/`) og identisk
build.yaml-manifest (`dirname($$s)/build.yaml`) dersom dei nokon gong vart plukka opp
av den automatiske pipelinen. I tillegg matchar ikkje noverande filnamn
(`referansemodell-schema-bronze.yaml` osv.) glob-mønsteret `*-schema.yaml` som
`SCHEMAS`-oppdaginga i `make/02-schema-discovery.mk` brukar (krev filnamn som
sluttar på `-schema.yaml`), så dei er i dag usynlege for automatisk `make`-oppdaging.

Brukaren har bede om å flytte dei tre policy-variantane til eigne søskenmapper,
slik at kvar får sin eigen `build.yaml` og sitt eige output-namnerom, i tråd med
standard `<domain>/<modell>/`-struktur (jf. `specs/done/referanse-katalogstruktur.md`
som etablerte same mønster for hovudskjemaet).

Avklart med brukaren:
- Filene vert omdøypte til å følgje konvensjonen `<mappenamn>-schema.yaml`.
- Kvar ny mappe får full generator-konfigurasjon (same `generators:`-blokk som
  hovudskjemaet), med `validation_policy` sett til høvesvis bronze/silver/gold.

## Mål

```
src/linkml/referanse/
  referansemodell/                          (uendra — hovudskjemaet blir liggande)
    referansemodell-schema.yaml
    build.yaml
    CHANGELOG.md
    description.md
  referansemodell-bronze/                   (ny)
    referansemodell-bronze-schema.yaml
    build.yaml
  referansemodell-silver/                   (ny)
    referansemodell-silver-schema.yaml
    build.yaml
  referansemodell-gold/                     (ny)
    referansemodell-gold-schema.yaml
    build.yaml
```

## Nummererte steg

### 1. Opprett nye mapper

```bash
mkdir -p src/linkml/referanse/referansemodell-bronze
mkdir -p src/linkml/referanse/referansemodell-silver
mkdir -p src/linkml/referanse/referansemodell-gold
```

### 2. Flytt og omdøyp skjemafilene

```bash
git mv src/linkml/referanse/referansemodell/referansemodell-schema-bronze.yaml \
       src/linkml/referanse/referansemodell-bronze/referansemodell-bronze-schema.yaml
git mv src/linkml/referanse/referansemodell/referansemodell-schema-silver.yaml \
       src/linkml/referanse/referansemodell-silver/referansemodell-silver-schema.yaml
git mv src/linkml/referanse/referansemodell/referansemodell-schema-gold.yaml \
       src/linkml/referanse/referansemodell-gold/referansemodell-gold-schema.yaml
```

(Bruk `mv` dersom filene ikkje er sporte i git enno — dei skal ikkje committast av LLM uansett, sjå CLAUDE.md.)

### 3. Oppdater metadata og filstig-kommentarar i kvar flytta fil

I kvar av dei tre filene:
- `name:` → endre til å matche nytt filnamn utan `-schema.yaml`-suffiks
  (`referansemodell-bronze`, `referansemodell-silver`, `referansemodell-gold`)
- Header-kommentaren `## Run: make mcp-validate SCHEMA=...` → oppdater stien til ny plassering

`id`, `title`, `default_prefix` treng **ikkje** endrast — dei er allereie
namngjevne per policy-nivå (t.d. `id: https://data.norge.no/linkml/referansemodell-bronze`)
og påverkast ikkje av mappeflyttinga. `imports: [linkml:types]` er absolutt/alias-basert
og påverkast heller ikkje av mappedjupn.

### 4. Opprett `build.yaml` i kvar ny mappe

Same `generators:`-blokk som `src/linkml/referanse/referansemodell/build.yaml`,
med `validation_policy` justert per nivå:

```yaml
publish_external: false
validation_policy: bronze   # silver / gold i respektive mapper

generators:
  jsonld_context: true
  shacl: true
  shacl_flags: ""
  python: true
  json_schema: true
  owl: true
  owl_flags: ""
  rdf: true
  protobuf: true
  erdiagram: true
  docs: true
  plantuml: true
  example_rdf: false
```

### 5. Verifiser tom `referansemodell/`-mappe for policy-filer

```bash
ls -la src/linkml/referanse/referansemodell/
```

Skal berre innehalde `referansemodell-schema.yaml`, `build.yaml`, `CHANGELOG.md`,
`description.md`.

### 6. Lint og valider alle fire skjema

```bash
make lint SCHEMA=src/linkml/referanse/referansemodell/referansemodell-schema.yaml
make lint SCHEMA=src/linkml/referanse/referansemodell-bronze/referansemodell-bronze-schema.yaml
make lint SCHEMA=src/linkml/referanse/referansemodell-silver/referansemodell-silver-schema.yaml
make lint SCHEMA=src/linkml/referanse/referansemodell-gold/referansemodell-gold-schema.yaml

make mcp-validate SCHEMA=src/linkml/referanse/referansemodell-bronze/referansemodell-bronze-schema.yaml POLICY=bronze
make mcp-validate SCHEMA=src/linkml/referanse/referansemodell-silver/referansemodell-silver-schema.yaml POLICY=silver
make mcp-validate SCHEMA=src/linkml/referanse/referansemodell-gold/referansemodell-gold-schema.yaml POLICY=gold
```

### 7. Sjekk om noko anna refererer til dei gamle stiane

Søk (allereie gjort under planlegging — berre treff var i `specs/done/` og filene
sjølve): `grep -rn "referansemodell-schema-silver\|referansemodell-schema-gold\|referansemodell-schema-bronze"`.
`specs/done/` skal **ikkje** endrast (arkivert, urørt per CLAUDE.md).
`mkdocs/mkdocs.yml` er autogenerert og treng ikkje manuell oppdatering.

## Handlingsliste

- [x] Steg 1: Opprett tre nye mapper
- [x] Steg 2: Flytt og omdøyp dei tre skjemafilene
- [x] Steg 3: Oppdater `name:` og Run-kommentar i kvar fil
- [x] Steg 4: Opprett `build.yaml` i kvar ny mappe (bronze/silver/gold)
- [x] Steg 5: Verifiser at `referansemodell/` berre inneheld hovudskjemaet
- [x] Steg 6: Lint og mcp-validate alle fire skjema
- [x] Steg 7: Verifiser at ingen andre filer refererer til gamle stiar

## Utført

Alle tiltak er utførte:

- ✅ `src/linkml/referanse/referansemodell-bronze/referansemodell-bronze-schema.yaml` + `build.yaml`
- ✅ `src/linkml/referanse/referansemodell-silver/referansemodell-silver-schema.yaml` + `build.yaml`
- ✅ `src/linkml/referanse/referansemodell-gold/referansemodell-gold-schema.yaml` + `build.yaml`
- ✅ `referansemodell/` inneheld no berre hovudskjemaet (`referansemodell-schema.yaml`, `build.yaml`, `CHANGELOG.md`, `description.md`)
- ✅ `name:`-felt og `## Run:`-kommentar oppdatert i alle tre flytta filer
- ✅ `make lint` — berre pre-eksisterande warnings (canonical_prefixes, recommended description), ingen errors, for alle fire skjema
- ✅ `make mcp-linkml-validate` (rett målnamn — CLAUDE.md sitt `mcp-validate` finst ikkje som eige target) — `valid: true, errorCount: 0` for bronze/silver/gold, POLICY korrekt auto-detektert frå kvar ny `build.yaml`
- ✅ `find src/linkml -mindepth 3 -maxdepth 3 -name '*-schema.yaml'` viser no fire distinkte skjema under `referanse/` utan katalog-/output-kollisjon (tidlegare delte alle fire same `schema_outdir`/`schema_key` via mappenamnet `referansemodell`)
- ✅ Ingen andre filer i repoet refererer til dei gamle stiane (kun `specs/done/` og denne specen sjølv, som er historiske/skildrande)

### Etterfølgjande feilretting: transliterasjon i silver/gold

Då `make domain-referanse` vart køyrt med full generator-konfigurasjon (jf. steg 4),
feila `gen-jsonld-context` for silver og gold med
`ValueError: Not a valid URI: https://data.norge.no/linkml/referansemodell-silver/aktørar`.
Årsak: attributtet `aktørar` (containerklassen) og klassen `Aktør` braut
CLAUDE.md-regelen om at særnorske bokstavar skal translittererast i identifikatorar
(klassenamn, slotnamn, attributtnamn) — `ø` er ikkje gyldig i ein URI utan
prosentkoding, og feilen var latent fordi desse skjemaa aldri hadde generators
aktivert før denne omorganiseringa.

Retta i begge filer:
- `aktørar` → `aktorar` (attributtnamn)
- `Aktør` → `Aktor` (klassenamn, `range:`-referanse)
- `ReferanseSølvContainer` → `ReferanseSolvContainer` (klassenamn, berre silver)

`description`-felt med `ø` (fritekst) er urørte — dei er unntatt frå kravet.
Verifisert med `make lint` (berre pre-eksisterande warnings) og
`make domain-referanse` (fullført med exit code 0 for alle fire skjema).
