# Spesifikasjon: Multi-organisasjon modellkatalog og tverretatleg samarbeid

## Bakgrunn

Repoet er per i dag sett opp for éin organisasjon (Brønnøysundregistra) med ein einaste
modellkatalog (`brreg-modellkatalog`). `update-modellkatalog.py` har hardkoda sti til denne.

For at fleire offentlege verksemder skal kunne samarbeide om modellutvikling i same repo —
der kvar verksemd eig sine eigne domenemodeller og publiserer til sin eigen modellkatalog —
trengst det:

1. Eit maskinleseleg eigarskapsregister (`CODEOWNERS.md`)
2. Dynamisk katalogoppretting/-oppdatering per eigarorg i `update-modellkatalog.py`
3. Scaffold for ny org-katalog
4. Dokumentasjon for nye organisasjonar
5. Klare bidragsretningslinjer og styringsmodel

---

## Konsept og designval

### Korleis modell-eigarskap fungerer i dag

`annotations.utgiver` i kvart skjema peiker allereie på eigarorganisasjonen sin URI
(`https://data.norge.no/organizations/<orgnr>`). Dette er **autoritativ kjelde for
kva org som eig kva modell** — ikkje ein separat mappe-konvensjon.

`CODEOWNERS.md` treng difor **ikkje** liste individuelle modellar. Den inneheld
organisasjonsnivå-metadata som scriptet ikkje kan lese ut av skjemaet åleine:
katalognamn, kontaktpunkt-URI, GitHub-team-alias, osv.

### CODEOWNERS.md-format

`CODEOWNERS.md` ligg i repo-rota og nyttar YAML-frontmatter som maskinleseleg del.
Kroppen er vanleg Markdown med forklarande tekst og lenkje til `ny-org.md`.

```markdown
---
organizations:
  - alias: brreg
    name: Brønnøysundregistra
    org_uri: https://data.norge.no/organizations/974760673
    catalog_slug: brreg-modellkatalog
    catalog_title: "Brønnøysundregistra - Modellkatalog"
    contact_uri: https://brreg.no/kontakt/modellforvaltning
    github_team: "@brreg/modellforvaltning"
    path_patterns:
      - src/linkml/ngr/**
      - src/linkml/oreg/**
      - src/linkml/samt/**
      - src/linkml/fint/**
---

# Modelleigarskapar (CODEOWNERS)

...forklarande tekst...
```

- `alias` — kort nøkkel brukt i mappenamn (`<alias>-modellkatalog`)
- `org_uri` — `https://data.norge.no/organizations/<orgnr>` — matchar `annotations.utgiver`
- `catalog_slug` — mappenamn for modellkatalogskjema (`src/linkml/modellkatalog/<slug>/`)
- `path_patterns` — glob-mønster for `.github/CODEOWNERS`-generering og PR-routing
- `github_team` — GitHub-team som automatisk vert bedt om review på PR-ar til org sine modellar

Scriptet les frontmatter med `yaml.safe_load()` etter å ha splitta på `---`.

### Katalogstruktur per org

Kvar org som er registrert i `CODEOWNERS.md` og har minst eitt skjema med
`annotations.utgiver` matchande `org_uri`, skal ha:

```
src/linkml/modellkatalog/
  <alias>-modellkatalog/
    <alias>-modellkatalog-schema.yaml   ← LinkML-skjema (éin gong, manuelt/scaffolda)
    manifest.yaml                        ← publish_external: true, data_policy: felles-datakatalog
    examples/
      <alias>-modellkatalog-eksempel.yaml
    data/
      <alias>-modellkatalog/
        <alias>-modellkatalog.yaml       ← datafil (oppdatert av script)
        manifest.yaml
```

**Skjemafila er lik for alle orgar** — det er berre datafila som skil seg.
Scaffolden (tiltak 3) kopier og tilpassar brreg-skjemaet.

### Auto-oppretting av nye katalogelement

Noverande script oppdaterer berre eksisterande `informasjonsmodeller`-innslag og rapporterer
"legg til manuelt" for nye. Med multi-org-støtte bør scriptet **auto-opprette stubs**
for skjema som ikkje ligg i katalogen enno. Stubs har `TODO`-verdiar for felt scriptet
ikkje kan derivere (`tema`, `lisens`), men fyller inn det den kan:

```yaml
- id: https://data.norge.no/<alias>/modellkatalog/<schema_name>
  tittel:
    - <schema.title>
  beskrivelse:
    - <schema.description>
  utgiver: <annotations.utgiver>
  identifikator_literal: https://data.norge.no/<alias>/modellkatalog/<schema_name>
  informasjonsmodellidentifikator: https://brreg.github.io/linkml-datamodellering-no/<domain>/<schema_name>/
  kontaktpunkt:
    - <org.contact_uri>
  tema:
    - TODO
  lisens: TODO
```

---

## Tiltak

### Tiltak 1 — `CODEOWNERS.md` (nytt fil, repo-rota)

Opprett `CODEOWNERS.md` med YAML-frontmatter og Markdown-kropp.

**Innhald i frontmatter:**

```yaml
organizations:
  - alias: brreg
    name: Brønnøysundregistra
    org_uri: https://data.norge.no/organizations/974760673
    catalog_slug: brreg-modellkatalog
    catalog_title: "Brønnøysundregistra - Modellkatalog"
    contact_uri: https://brreg.no/kontakt/modellforvaltning
    github_team: "@brreg/modellforvaltning"
    path_patterns:
      - src/linkml/ngr/**
      - src/linkml/oreg/**
      - src/linkml/samt/**
      - src/linkml/fint/**
```

**Innhald i kroppen:**

- Forklaring av eigarskapsmodellen (org eig modell via `annotations.utgiver`)
- Lenkje til `mkdocs/docs/ny-org.md` for nye organisasjonar
- Merk at `.github/CODEOWNERS` er generert frå `path_patterns` her
- Tabell med gjeldande organisasjonar (alias, namn, org-URI)

**Merk:** AP-NO-profilar (`src/linkml/ap-no/`), `src/linkml/fair/` og
`src/linkml/referanse/` er ikkje knytte til ein enkelt org — dei er felles infrastruktur
forvalta av repo-eigaren. Dei inngår ikkje i nokon per-org-katalog.

---

### Tiltak 2 — `update-modellkatalog.py` (refaktorering + multi-org)

Erstatt hardkoda `DEFAULT_CATALOG`-sti med dynamisk multi-org-logikk.

**Endringsoversikt:**

1. **`load_org_registry(codeowners_path)`**  
   Les `CODEOWNERS.md`, splitter på `---`, `yaml.safe_load()` frontmatter.
   Returnerer dict keya på `org_uri`.

2. **`load_annotated_schemas(root)`**  
   Uendra frå dagens versjon.

3. **`group_schemas_by_org(schemas, org_registry)`**  
   Grupperer schemas på `annotations.utgiver`. Skjema med utgiver som ikkje finst
   i `org_registry` vert samla i ei "ukjend org"-liste og rapportert som åtvarslar.

4. **`find_or_create_catalog_data(org, dry_run)`**  
   - Finn `src/linkml/modellkatalog/<catalog_slug>/data/<catalog_slug>/<catalog_slug>.yaml`
   - Viss fila ikkje finst: åtvarslar og hoppar over (datafila må scaffoldast med tiltak 3)
   - Returnerer katalog-dict

5. **`update_or_add_entry(catalog, schema, org)`**  
   - Eksisterande innslag: oppdater annotasjonsfelter (som i dag)
   - Nytt innslag: legg til stub med `TODO`-verdiar

6. **`main()`**  
   - Ny `--codeowners`-parameter (default `CODEOWNERS.md`)
   - Ny `--org`-parameter for å køyre for berre éin org
   - Itererer over alle org-ar i registry
   - Rapporterer per-org: oppdaterte, nye stubs, ukjende skjema

**Bakoverkompatibilitet:**  
Eksisterande `brreg-modellkatalog.yaml`-datafil vert oppdatert som før — berre
`--catalog`-parameteren og hardkoda default vert fjerna.

**Ny Makefile-target:**
```makefile
update-modellkatalog:
    podman run ... python3 src/assets/scripts/update-modellkatalog.py
```
(Uendra frå i dag, men scriptet les no `CODEOWNERS.md` automatisk.)

---

### Tiltak 3 — `new-org-catalog.sh` (nytt scaffold-script)

Nytt script `src/assets/scripts/new-org-catalog.sh` som set opp katalogstruktur
for ein ny org. Legg til `make new-org-catalog ORG=<alias>`-target.

**Steg:**
1. Les org-metadata frå `CODEOWNERS.md` (krev at org er registrert i frontmatter)
2. Kopier `brreg-modellkatalog-schema.yaml` → `<alias>-modellkatalog-schema.yaml`
   og erstatt `brreg` med `<alias>`, og juster `id`, `title`, `default_prefix`
3. Opprett `manifest.yaml` med `publish_external: true`, `data_policy: felles-datakatalog`
4. Opprett tom datafil `data/<alias>-modellkatalog/<alias>-modellkatalog.yaml` med
   minimal modellkatalog-instans (basert på org-metadata frå CODEOWNERS.md)
5. Opprett `examples/<alias>-modellkatalog-eksempel.yaml`

---

### Tiltak 4 — `mkdocs/docs/ny-org.md` (ny rettleiing)

Ny rettleiingsside som forklarer korleis ein ny organisasjon tek i bruk repoet.

**Innhald:**

1. **Føresetnader** — same som `ny-domenemodell.md` (Podman, Make, Git)
2. **Steg 1 — Registrer organisasjonen**  
   Legg til org i frontmatter i `CODEOWNERS.md` + send PR + godkjenning frå repo-administrator
3. **Steg 2 — Scaffold katalog**  
   `make new-org-catalog ORG=<alias>` — genererer katalogskjema og datafil
4. **Steg 3 — Opprett domenemodeller**  
   `make new-model NAME=<modell> DOMAIN=<domain>` med rett `annotations.utgiver`
5. **Steg 4 — Synk modellkatalog**  
   `make update-modellkatalog` — auto-oppdaterer datafila med nye modellar
6. **Steg 5 — Valider og publiser**  
   `make mcp-validate SCHEMA=... POLICY=felles-datakatalog INSTANCE=...`
7. **GitHub-tilgang** — kven ein kontaktar for å få write-tilgang til repoet
   (sjå GOVERNANCE.md)
8. **Tverretatleg samarbeid** — korleis importere ein annan org sin AP-NO-profil,
   korleis sende PR på delt infrastruktur, korleis foreslå endringar i common-ap-no

Sida skal leggast til i `mkdocs/publish.sh` under `- Rettleiingar:`.

---

### Tiltak 5 — `.github/CODEOWNERS` (nytt eller oppdatert)

Opprett `.github/CODEOWNERS` med path-mønster basert på `path_patterns` i `CODEOWNERS.md`.

Standard GitHub CODEOWNERS-format:
```
# Generert frå CODEOWNERS.md — ikkje rediger direkte
src/linkml/ngr/               @brreg/modellforvaltning
src/linkml/oreg/              @brreg/modellforvaltning
src/linkml/samt/              @brreg/modellforvaltning
src/linkml/fint/              @brreg/modellforvaltning

# Felles infrastruktur — alltid repo-admin-review
src/linkml/ap-no/             @brreg/modellforvaltning
src/assets/                   @brreg/modellforvaltning
.github/                      @brreg/modellforvaltning
Makefile                      @brreg/modellforvaltning
```

Kan genererast automatisk frå `CODEOWNERS.md` av eit script, eller vedlikehalast manuelt
(lettast for no). Vurder å generere `.github/CODEOWNERS` som del av `make update-modellkatalog`.

---

## Avhengigheiter

- Tiltak 1 må gjerast først (CODEOWNERS.md er input til alt anna)
- Tiltak 2 avheng av tiltak 1 (scriptet les frontmatter)
- Tiltak 3 avheng av tiltak 1 (scaffold-scriptet les org-metadata)
- Tiltak 4 kan gjerast parallelt med tiltak 2-3
- Tiltak 5 kan gjerast sist (GitHub-funksjonalitet, ikkje blokkerer anna)

## Prioritet

Høg — konseptuelt viktig for at repoet skal vere genuint flereigarleg.
Tiltak 1-2-4 er kjernen; tiltak 3 og 5 er komfort/automatisering.

Anbefalt rekkjefølge:
1. Tiltak 1 (CODEOWNERS.md) + tiltak 4 (ny-org.md) + tiltak 5 (governance-contributing-spec)
2. Tiltak 2 (script)
3. Tiltak 3 (scaffold)
4. Tiltak 5 (.github/CODEOWNERS)

## Utført

Utført 2026-06-10.

- **Tiltak 1** — `CODEOWNERS.md` oppretta med YAML-frontmatter (brreg som einaste registrerte org)
  og Markdown-kropp med eigarskapsforklaring, tabell og lenkje til `ny-org.md`.

- **Tiltak 2** — `update-modellkatalog.py` refaktorert:
  - `load_org_registry()` les YAML-frontmatter frå `CODEOWNERS.md`
  - `group_schemas_by_org()` grupperer etter `annotations.utgiver`
  - `process_org()` itererer per org og oppdaterer kvar sin katalogdatafil
  - Ny `--codeowners`- og `--org`-parameter; `--catalog` og hardkoda default er fjerna
  - **Avvik frå spec:** Scriptet auto-oppretter **ikkje** stubs for nye skjema. Grunnen:
    mange skjema med `annotations.utgiver` (AP-NO-profilar, FINT-skjema) er infrastruktur
    som ikkje høyrer til i ein offentleg modellkatalog. I staden rapporterer scriptet
    "Ikkje i katalogen (legg til manuelt om ønskjeleg)" med ein foreslått stub-ID.
    `make_stub()`-funksjonen er tilgjengeleg for manuell bruk via scriptutdata.

- **Tiltak 3** — `src/assets/scripts/new-org-catalog.sh` oppretta. Les org-metadata frå
  `CODEOWNERS.md`-frontmatter via Python, scaffoldar katalogskjema (kopi av brreg-malen),
  manifest, datafil med `TODO`-verdiar og eksempelfil.
  `make new-org-catalog ORG=<alias>`-target lagt til i Makefile.

- **Tiltak 4** — `mkdocs/docs/ny-org.md` oppretta med steg-for-steg-rettleiing (6 steg +
  tverretatleg samarbeid-seksjon). Lagt til i `mkdocs/publish.sh` nav øvst under Rettleiingar.

- **Tiltak 5** — `.github/CODEOWNERS` oppdatert med kommentar om at mapper er avleia frå
  `CODEOWNERS.md path_patterns`, og med eksplisitte linjer for `src/mcp-linkml-validator/`,
  `src/mcp-linkml-modell-utkast/` og `CODEOWNERS.md` sjølv.
