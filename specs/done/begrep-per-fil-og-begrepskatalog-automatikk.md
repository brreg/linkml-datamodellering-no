# Begrep per fil og begrepskatalog-automatikk

## Bakgrunn

I dag ligg alle begrep for ein organisasjon i éin stor YAML-fil under
`src/linkml/begrepskatalog/<organisasjon>-begrepskatalog/data/<organisasjon>-begrepskatalog/<organisasjon>-begrepskatalog.yaml`.

Dette gjer det vanskeleg å:
- Versjonere og spore endringar i einskilde begrep (git-diff viser heile fila)
- Organisere begrep i logiske domene eller temaområde
- Samarbeide om begrep utan merge-konflikt
- Gjenbruke enkeltstående begrep på tvers av organisasjonar

**Målet:**
1. Modellere kvart begrep som ei eiga fil
2. Innføre omgrepet "begrepssamling" — ein samling av begrep for eit domene
3. Automatisk aggregere alle begrepssamlingane til ein organisasjon til ein begrepskatalog
4. Leggje til tabell "Genererte begrepskatalogar" i README.md (før modellkatalog-tabellen)

## Omgrep

- **Begrep** — enkeltomgrep med definisjon og metadata (SKOS `Concept`)
- **Begrepssamling** — logisk samling av begrep for eit domene (t.d. "Begrep frå Foretaksregisteret", "Begrep frå Aksjonærregisteret")
- **Begrepskatalog** — automatisk generert oversikt over **alle** begrep frå **alle** begrepssamlingane til ein organisasjon (SKOS `Collection`)

Ein organisasjon kan ha fleire begrepssamlingar. Kvar begrepssamling inneheld fleire begrep. Begrepskatalogen aggregerer alle.

## Filstruktur (ny)

```
src/linkml/
  <domain>/
    <begrepssamling>/
      <begrepssamling>-schema.yaml       ← importerer skos-ap-no
      build.yaml                          ← manifestfil (sjå under)
      examples/
        <begrepssamling>-eksempel.yaml
      begrep/                             ← NYTT: éin fil per begrep
        <begrep-id>.yaml                  ← t.d. foretaksnavn.yaml, nestleder.yaml
        <begrep-id>.yaml
        ...

  begrepskatalog/                         ← automatisk generert (ikkje manuell redigering)
    <organisasjon>-begrepskatalog/
      <organisasjon>-begrepskatalog-schema.yaml
      build.yaml
      data/
        <organisasjon>-begrepskatalog/
          <organisasjon>-begrepskatalog.yaml  ← aggregert frå alle begrepssamlingane
          build.yaml
```

**Døme:**

```
src/linkml/
  oreg/
    brreg-begrepssamling-foretaksregisteret/
      brreg-begrepssamling-foretaksregisteret-schema.yaml
      build.yaml
      begrep/
        foretaksnavn.yaml
        nestleder.yaml
    brreg-begrepssamling-aksjonaerregisteret/
      brreg-begrepssamling-aksjonaerregisteret-schema.yaml
      build.yaml
      begrep/
        aksjeklasser.yaml

  begrepskatalog/
    brreg-begrepskatalog/
      brreg-begrepskatalog-schema.yaml
      data/
        brreg-begrepskatalog/
          brreg-begrepskatalog.yaml  ← aggregerer foretaksnavn, nestleder, aksjeklasser
```

## Manifestformat (`build.yaml` i begrepssamling)

```yaml
# Publisering og validering for begrepssamlinga
publish_external: false         # berre begrepskatalogen publiserer
validation_policy: bronze       # eller silver/gold

# Metadata for aggregering til begrepskatalog
aggregation:
  organization: "974760673"     # organisasjonsnummer (tilsv. Brønnøysundregistra)
  catalog_name: brreg-begrepskatalog

# Generatorkonfig (vanleg)
generators:
  jsonld_context: true
  shacl: true
  # osv.
```

**Avklaringsspørsmål til brukaren:**

1. **Skal begrepssamlinga ha eigen containerklasse** (`BegrepssamlingContainer`) eller berre vere ein mappe med YAML-filer?
   - Alternativ A: `BegrepssamlingContainer` (frå SKOS-AP-NO) brukas som `tree_root` i `<begrepssamling>-schema.yaml`
   - Alternativ B: Begrep ligg som frittstående filer, utan containerklasse (enklare, men mindre struktur)

2. **Skal begrepssamling-skjemaet importere skos-ap-no?**
   - Eg antek: Ja — `imports: [skos-ap-no-schema]`

3. **Skal begrepskatalogen vere read-only (automatisk generert)?**
   - Eg antek: Ja — `begrepskatalog/`-mappa skal **aldri** redigerast manuelt

4. **Skal vi støtte begrep som høyrer til fleire organisasjonar?**
   - Alternativ A: Nei — kvart begrep høyrer til éin organisasjon
   - Alternativ B: Ja — `aggregation.organization` kan vere ei liste

## Tiltak

### 1. Definer ny filstruktur og manifestformat

- [x] Oppdater `CONVENTIONS.md` med ny seksjon "Begrepssamlingar og begrepskatalogar"
- [x] Dokumenter `build.yaml`-feltet `aggregation.organization` og `aggregation.catalog_name`
- [x] Dokumenter at `begrep/`-mappa skal innehalde éin YAML-fil per begrep

### 2. Skriv `collect-concepts.py` (CI-script)

- [x] Opprett `src/assets/scripts/collect-concepts.py` (Python i staden for bash)
- [x] Input: `src/linkml/<domain>/<begrepssamling>/build.yaml` (alle med `aggregation.organization`)
- [x] Logikk:
  - For kvar organisasjon `X`:
    - Finn alle begrepssamlingar med `aggregation.organization: X`
    - Samle alle begrep frå `begrep/*.yaml` i desse samlingane
    - Generer aggregert `begrepskatalog/<X>-begrepskatalog/data/<X>-begrepskatalog/<X>-begrepskatalog.yaml`

### 3. Integrer `collect-concepts.py` i CI

- [x] Legg til override for `domain-begrepskatalog` i Makefile som køyrer `collect-concepts` først
- [x] CI køyrer `make domain-begrepskatalog` som no kallar `collect-concepts` automatisk

### 4. Migrer eksisterande `brreg-begrepskatalog`

- [x] Flytt `brreg-begrepskatalog/data/brreg-begrepskatalog/brreg-begrepskatalog.yaml` til `oreg/begrepssamling-foretaksregisteret/begrep/`
- [x] Split opp i éin fil per begrep (`foretaksnavn.yaml`, `nestleder.yaml`, `aksjeklasser.yaml`)
- [x] Opprett `build.yaml` for begrepssamlinga med `aggregation.organization: 974760673`
- [x] Køyr `collect-concepts.py` og verifiser at `brreg-begrepskatalog.yaml` vert regenerert

### 5. Legg til tabell i README.md

- [x] Legg til seksjon "## Genererte begrepskatalogar" **før** "## Genererte modellkatalogar"
- [x] Legg til første rad i tabell manuelt (automatisering kjem seinare)
- [x] Marker tabellen med `<!-- BEGIN AUTO-GENERATED: BEGREPSKATALOG TABLE -->` og `<!-- END AUTO-GENERATED: BEGREPSKATALOG TABLE -->`

### 6. Oppdater dokumentasjon

- [ ] `mkdocs/docs/ny-begrepsmodell.md`: oppdater rettleiinga for å reflektere ny struktur (begrep per fil)
- [x] `COMMANDS.md`: legg til `make collect-concepts` for manuell køyring
- [x] `Makefile`: legg til `collect-concepts`-target

### 7. Test og validering

- [ ] Verifiser at `make mcp-linkml-validate` fungerer for begrepssamlingar
- [ ] Verifiser at `make docs-publish` viser begrepskatalogen korrekt
- [ ] Sjekk at `generated/begrepskatalog/brreg-begrepskatalog/` inneheld samlede artefaktar

## Valideringsresultat

Begrepskatalogen skal validerast med `felles-begrepskatalog`-policy (ihht dagens praksis). Begrepssamlingar skal validerast med `bronze`/`silver`/`gold` (konfigurerbart i `build.yaml`).

## Utført

**Dato:** 2026-07-11

### Gjennomførte tiltak

1. **Filstruktur og manifest:**
   - Oppdatert `CONVENTIONS.md` med ny seksjon om begrepssamlingar
   - Dokumentert `build.yaml`-format med `aggregation.organization` og `aggregation.catalog_name`

2. **Aggregeringscript:**
   - Oppretta `collect-concepts.py` (Python i staden for bash) for betre YAML-handtering
   - Scriptet samlar alle begrep frå `begrepssamling-*/begrep/*.yaml` og genererer aggregert begrepskatalog per organisasjon

3. **CI-integrasjon:**
   - Lagt til override for `domain-begrepskatalog` i Makefile som køyrer `collect-concepts` først
   - CI køyrer `make domain-begrepskatalog` som no kallar `collect-concepts` automatisk

4. **Migrering av eksisterande data:**
   - Migrert `brreg-begrepskatalog` til `oreg/begrepssamling-foretaksregisteret/begrep/`
   - Splita 3 begrep til eigne filer: `foretaksnavn.yaml`, `nestleder.yaml`, `aksjeklasser.yaml`
   - Oppretta `build.yaml` med aggregation-metadata

5. **Dokumentasjon:**
   - Lagt til tabell "Genererte begrepskatalogar" i README.md (før modellkatalog-tabellen)
   - Oppdatert `COMMANDS.md` med `make collect-concepts`
   - Lagt til `collect-concepts`-target i Makefile

### Gjenstående arbeid

- [ ] `mkdocs/docs/ny-begrepsmodell.md`: oppdater rettleiinga for å reflektere ny struktur (begrep per fil)
- [ ] Verifiser at `make docs-publish` viser begrepskatalogen korrekt
- [ ] Test at `make mcp-linkml-validate` fungerer for begrepssamlingar

### Verifisering

- ✓ `make collect-concepts` samlar 3 begrep frå `begrepssamling-foretaksregisteret`
- ✓ Generert `brreg-begrepskatalog.yaml` inneheld alle felt frå originale begrepsfiler
- ✓ `make domain-begrepskatalog` køyrer `collect-concepts` først, deretter alle generatorar
