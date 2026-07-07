# common-ap-no vert ikkje publisert i nav-menyen

## Bakgrunn

`common-ap-no-schema.yaml` er eit basisskjema som definerer felles typar, subsets, klasser og slots for alle AP-NO-profilene (dcat-ap-no, dqv-ap-no, skos-ap-no, cpsv-ap-no, xkos-ap-no, modelldcat-ap-no). Det ligg i `src/linkml/ap-no/common/` og vert importert av alle AP-NO-profiler.

**Problem:** `common-ap-no` dukkar ikkje opp i navigasjonsmenyen i mkdocs-portalen.

## Funn

### Årsak

`src/linkml/ap-no/common/` **manglar `manifest.yaml`**. Alle andre AP-NO-profiler har `manifest.yaml` og vert bygde som sjølvstendige modellar:

```bash
$ find src/linkml/ap-no -name "manifest.yaml"
src/linkml/ap-no/cpsv-ap-no/manifest.yaml
src/linkml/ap-no/dcat-ap-no/manifest.yaml
src/linkml/ap-no/dqv-ap-no/manifest.yaml
src/linkml/ap-no/modelldcat-ap-no/manifest.yaml
src/linkml/ap-no/skos-ap-no/manifest.yaml
src/linkml/ap-no/xkos-ap-no/manifest.yaml
```

### Konsekvens

- Ingen artefaktar vert genererte for `common-ap-no` (ingen `generated/ap-no/common-ap-no/`)
- `mkdocs/publish.sh` finn ingen skjema-katalog under `generated/ap-no/common*`
- `common-ap-no` vert ikkje lagt til i nav-menyen i `mkdocs.yml`

### Noverande struktur

```
src/linkml/ap-no/
├── common/
│   ├── common-ap-no-schema.yaml       ← skjemaet
│   └── description.md                 ← portaltekst (Markdown)
│   [MANGLAR: manifest.yaml]
├── cpsv-ap-no/
│   ├── cpsv-ap-no-schema.yaml
│   ├── manifest.yaml                  ← finst
│   └── ...
├── dcat-ap-no/
│   ├── dcat-ap-no-schema.yaml
│   ├── manifest.yaml                  ← finst
│   └── ...
└── ...
```

### Importhierarki

```
linkml:types
    ↓
common-ap-no          ← importerast av alle AP-NO-profiler
    ↓
dcat-ap-no / dqv-ap-no / skos-ap-no / cpsv-ap-no / xkos-ap-no / modelldcat-ap-no
    ↓
domenemodeller
```

`common-ap-no` er ein **intern bibliotek-modell** som gir gjenbruk av:

- **Typar:** `LangString`, `NonNegativeInteger`
- **Subsets:** `Metadata`, `Obligatorisk`, `Anbefalt`, `Valgfri`
- **Felles klasser/slots** (dersom relevante) — per no mest typar og subsets

## Alternativ

### Alternativ A: Legg til manifest.yaml (gjer common-ap-no synleg)

**Fordel:**
- Brukarar kan sjå kva som finst i `common-ap-no` (typar, subsets, felles slots)
- Fullstendig dokumentasjon av heile AP-NO-økosystemet
- Konsistent struktur: alle skjema i `src/linkml/<domain>/<modell>/` har manifest og vert bygde

**Ulempe:**
- `common-ap-no` er ikkje ein "ferdig modell" i seg sjølv — det er eit bibliotek som andre importerer
- Kan forvirre brukarar som trur dei skal bruke `common-ap-no` direkte i staden for å importere via AP-NO-profilane
- Ekstra byggjobb (liten kostnad — ~10-20 sekund)

**Forslag til manifest:**

```yaml
# src/linkml/ap-no/common/manifest.yaml
publish_external: false
validation_policy: bronze

generators:
  jsonld_context: true
  shacl: false
  python: true
  json_schema: true
  owl: true
  rdf: true
  protobuf: false
  erdiagram: true
  docs: true
  plantuml: true
  example_rdf: false
```

### Alternativ B: La common-ap-no forbli intern (ingen manifest)

**Fordel:**
- Beheld noverande design: `common-ap-no` er eit internt bibliotek, ikkje ein publisert modell
- Reduserer støy i portalen — brukarar ser berre "ferdigpakka" AP-NO-profiler
- Minimerer byggtid

**Ulempe:**
- Brukarar ser ikkje kva som finst i `common-ap-no` utan å lese kjeldekoden
- Inkonsistent med resten av strukturen (alle andre skjema har manifest)
- Vanskeleg å oppdage kva typar og subsets som er tilgjengelege

### Alternativ C: Dokumenter common-ap-no i mkdocs manuelt

**Fordel:**
- Full kontroll på korleis `common-ap-no` presenteras
- Kan skrive ein portaltekst som forklarar at dette er ein intern bibliotek-modell
- Slepp å bygge fullstendige artefaktar (shacl, rdf, protobuf osv.)

**Ulempe:**
- Ekstra manuelt arbeid: må vedlikehalde dokumentasjon utanfor publish.sh-flyten
- Risiko for at dokumentasjonen kjem ut av synk med kjeldekoden

## Anbefaling

**Alternativ A** er å føretrekke dersom målet er full transparens og konsistens.

**Valt løysing:** Alternativ A + omdøping av katalog til `common-ap-no/` for konsistent namngjeving.

## Beslutning

Vi skal:

1. **Omdøpe katalogen** frå `src/linkml/ap-no/common/` til `src/linkml/ap-no/common-ap-no/`
   - Konsistent med alle andre skjema: `<domain>/<modell>/<modell>-schema.yaml`
   - Eksplisitt at dette er `common-ap-no` (AP-NO-fellesbibliotek), ikkje generisk "common"
   - Unngår potensielle konfliktar med andre `common`-katalogar
2. **Legge til `manifest.yaml`** for `common-ap-no`
   - Gjer `common-ap-no` synleg i mkdocs-portalen
   - Konsistent med alle andre AP-NO-profiler

## Endringar som må gjerast

### 1. Omdøp katalog

```bash
git mv src/linkml/ap-no/common src/linkml/ap-no/common-ap-no
```

### 2. Oppdater import-referansar i seks AP-NO-profiler

Alle seks AP-NO-profiler importerer `common-ap-no-schema` — import-stien må oppdaterast:

| Fil | Gamal import | Ny import |
|-----|--------------|-----------|
| `cpsv-ap-no/cpsv-ap-no-schema.yaml` | `../common/common-ap-no-schema` | `../common-ap-no/common-ap-no-schema` |
| `dcat-ap-no/dcat-ap-no-schema.yaml` | `../common/common-ap-no-schema` | `../common-ap-no/common-ap-no-schema` |
| `dqv-ap-no/dqv-ap-no-schema.yaml` | `../common/common-ap-no-schema` | `../common-ap-no/common-ap-no-schema` |
| `modelldcat-ap-no/modelldcat-ap-no-schema.yaml` | `../common/common-ap-no-schema` | `../common-ap-no/common-ap-no-schema` |
| `skos-ap-no/skos-ap-no-schema.yaml` | `../common/common-ap-no-schema` | `../common-ap-no/common-ap-no-schema` |
| `xkos-ap-no/xkos-ap-no-schema.yaml` | `../common/common-ap-no-schema` | `../common-ap-no/common-ap-no-schema` |

### 3. Opprett manifest.yaml

`src/linkml/ap-no/common-ap-no/manifest.yaml`:

```yaml
publish_external: false
validation_policy: bronze

generators:
  jsonld_context: true
  shacl: false
  python: true
  json_schema: true
  owl: true
  rdf: true
  protobuf: false
  erdiagram: true
  docs: true
  plantuml: true
  example_rdf: false
```

### 4. Valider og bygg

```bash
# Valider common-ap-no
make mcp-validate SCHEMA=src/linkml/ap-no/common-ap-no/common-ap-no-schema.yaml

# Bygg alle AP-NO-profiler (verifiser at imports fungerer)
make ap-no

# Publiser til mkdocs
make docs-publish
```

## Utført

Alle tiltak vart gjennomførte 2026-07-07:

- [x] Omdøp katalog: `git mv src/linkml/ap-no/common src/linkml/ap-no/common-ap-no`
- [x] Oppdater import i `cpsv-ap-no-schema.yaml`
- [x] Oppdater import i `dcat-ap-no-schema.yaml`
- [x] Oppdater import i `dqv-ap-no-schema.yaml`
- [x] Oppdater import i `dqv-core-schema.yaml`
- [x] Oppdater import i `modelldcat-katalog-schema.yaml`
- [x] Oppdater import i `modelldcat-modell-schema.yaml`
- [x] Oppdater import i `skos-ap-no-schema.yaml`
- [x] Oppdater import i `xkos-ap-no-schema.yaml`
- [x] Opprett `manifest.yaml` for `common-ap-no`
- [x] Fjern `grep -v common` frå Makefile (linje 42-43)
- [x] Bygg alle AP-NO-profiler med `make domain-ap-no`
- [x] Publiser til mkdocs med `make docs-publish`
- [x] Verifiser at `common-ap-no` dukkar opp i nav-menyen

### Resultat

- `common-ap-no` er no synleg i nav-menyen: `mkdocs.yml` linje 74
- Genererte artefaktar i `generated/ap-no/common-ap-no/`
- Dokumentasjon i `mkdocs/docs/ap-no/common-ap-no/index.md`
- Alle AP-NO-profiler bygde utan feil med oppdaterte import-referansar

## Relatert

- `CLAUDE.md` (LinkML Importhierarki-seksjonen)
- `specs/done/ap-no-metadata-subset.md` (subset-definisjonar i common-ap-no)
- `mkdocs/publish.sh` (byggeprosess — Steg 2, linje 286-335)
