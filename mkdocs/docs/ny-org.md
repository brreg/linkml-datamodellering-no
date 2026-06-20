# Rettleiing: ny organisasjon

Denne rettleiinga forklarer korleis ein ny organisasjon tek i bruk repoet for å
publisere eigne informasjonsmodellar saman med Brønnøysundregistra og andre verksemder.

## Føresetnader

Same som for [ny domenemodell](ny-domenemodell.md):

```bash
make check-prereqs
make linkml-build-docker && make python-build-docker && make mcp-val-build
```

## Steg 1 — Registrer organisasjonen i CODEOWNERS.md

Legg til organisasjonen i YAML-frontmatter i `CODEOWNERS.md` (repo-rota).

```yaml
organizations:
  # ... eksisterande organisasjonar ...
  - alias: <alias>                          # kort nøkkel, t.d. digdir, ssb, kartverket
    name: <Organisasjonsnamn>
    org_uri: https://data.norge.no/organizations/<9-sifra orgnr>
    catalog_slug: <alias>-modellkatalog     # mappenamn, t.d. digdir-modellkatalog
    catalog_title: "<Org> – Modellkatalog"
    contact_uri: https://<org-domene>/kontakt/modellforvaltning
    github_team: "@<github-org>/<team>"
    path_patterns:
      - src/linkml/<domain>/**              # mappane org-en eig
```

Send **pull request** mot `main` med denne endringa. Repo-administratoren godkjenner
PR-en og gir GitHub-teamet write-tilgang til repoet (sjå `GOVERNANCE.md`).

## Steg 2 — Scaffold modellkatalog

Etter godkjent PR, opprett katalogstrukturen:

```bash
make new-org-catalog ORG=<alias>
```

Dette oppretter:
```
src/linkml/modellkatalog/<alias>-modellkatalog/
├── <alias>-modellkatalog-schema.yaml    ← LinkML-skjema for katalogen
├── manifest.yaml                         ← publish_external: true
├── examples/
│   └── <alias>-modellkatalog-eksempel.yaml
└── data/
    └── <alias>-modellkatalog/
        ├── <alias>-modellkatalog.yaml    ← katalogdatafil (med TODO-verdiar)
        └── manifest.yaml
```

Fyll inn `TODO`-verdiane i datafila manuelt:
- `tittel` og `beskrivelse` på katalogen
- `har_del`-lista (vert automatisk synkronisert seinare av `update-modellkatalog`)
- Namn på kontaktpunkt i `aktoerer`-lista

## Steg 3 — Opprett domenemodeller

```bash
make new-model NAME=<modell> DOMAIN=<domain>
```

Opne den genererte skjemafila og set `annotations.utgiver` til org-en sin URI:

```yaml
annotations:
  utgiver: https://data.norge.no/organizations/<orgnr>
  endringsdato: "YYYY-MM-DD"
  utgivelsesdato: "YYYY-MM-DD"
  status: http://purl.org/adms/status/UnderDevelopment
  oppdateringsfrekvens: http://publications.europa.eu/resource/authority/frequency/IRREG
```

Sjå [Ny domenemodell](ny-domenemodell.md) for full rettleiing om korleis ein modellerer.

## Steg 4 — Synkroniser modellkatalog

Etter at skjema har korrekt `annotations.utgiver`, synkroniser katalogdatafila:

```bash
make update-modellkatalog
```

Scriptet finn alle skjema med `annotations.utgiver` matchande org-URI, og
oppretter nye stub-innslag i katalogdatafila for skjema som ikkje er registrerte enno.
Stubs har `TODO`-verdiar for felt som `tema` og `lisens` — desse må fyllast inn manuelt.

**Konvensjon:** Modellkatalogen skal liste **alle** skjema org-en forvaltar — også
modellar som ikkje er ferdige enno. Sett `annotations.status` til
`http://purl.org/adms/status/UnderDevelopment` for utkast. Modellkatalogen er den
maskinlesbare oversikta rettleiaren *Veileder for tilgjengeliggjøring av åpne data*
krev (jf. punkt 12 — «òg for data som ikkje er tilgjengelege enno»), så ufullstendige
modellar skal vere synlege i katalogen med korrekt status, ikkje utelatne til dei er
klare.

For å køyre berre for éin org:
```bash
python3 src/assets/scripts/update-modellkatalog.py --org <alias>
```

## Steg 5 — Valider

Valider kvar enkelt domenemodell:
```bash
make mcp-validate SCHEMA=src/linkml/<domain>/<modell>/<modell>-schema.yaml POLICY=bronze
make mcp-validate SCHEMA=src/linkml/<domain>/<modell>/<modell>-schema.yaml POLICY=silver
```

Valider modellkatalogen mot publiseringspolicy:
```bash
make mcp-validate \
  SCHEMA=src/linkml/modellkatalog/<alias>-modellkatalog/<alias>-modellkatalog-schema.yaml \
  POLICY=felles-datakatalog \
  INSTANCE=src/linkml/modellkatalog/<alias>-modellkatalog/data/<alias>-modellkatalog/<alias>-modellkatalog.yaml
```

Sjå [Valideringsreglar](valideringregler.md) for fullstendig oversikt.

## Steg 6 — Send pull request

Lag ein PR mot `main` med:
- Nye domenemodeller i `src/linkml/<domain>/`
- Oppdatert `CODEOWNERS.md` (om ikkje gjort i steg 1)
- Ny katalogstruktur i `src/linkml/modellkatalog/<alias>-modellkatalog/`

CI køyrer lint, instansvalidering og policy-sjekkar automatisk. Alle sjekkar må passere
før PR-en kan mergast.

---

## Tverretatleg samarbeid

### Importere ap-no profil

Alle AP-NO-profilar i `src/linkml/ap-no/` er felles infrastruktur og kan importerast
av alle domenemodeller uavhengig av eigar-org:

```yaml
imports:
  - linkml:types
  - ../../ap-no/dcat-ap-no/dcat-ap-no-schema
```

### Foreslå endringar i felles infrastruktur

Endringar i `src/linkml/ap-no/`, `src/assets/` eller `Makefile` krev godkjenning frå
repo-administrator (sjå `GOVERNANCE.md`). Send ein PR og skriv tydeleg i PR-beskrivselen
kvifor endringa er nødvendig og om ho er bakoverkompatibel.

Breaking changes (fjerne/endre eksisterande slottar eller klasser) krev ein RFC-prosess
med 14 dagars diskusjonsperiode — sjå `GOVERNANCE.md` for detaljar.

### Referere til ein annan org sin modell

Alle modellar i dette repoet er offentlige og kan gjenbrukes i andre modellar.

Bruk `schema_id`-URIen frå den andre org sin modell som `slot_uri` eller `class_uri`:

```yaml
imports:
  - linkml:types
  - ../../dcat-ap-no/dcat-ap-no-schema
  # Importer ikkje direkte frå ein annan org sin domenemodell —
  # bruk heller eit felles AP-NO-importlag
```

---

## Tilgang og kontakt

For å få write-tilgang til repoet, kontakt repo-administrator via GitHub Issues.
Sjå `GOVERNANCE.md` for formelle krav og prosess.
