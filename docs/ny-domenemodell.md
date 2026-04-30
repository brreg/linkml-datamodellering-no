# Veiledning: ny domenemodell

Denne veiledningen viser hvordan du utvikler en ny LinkML-domenemodell
ved å gjenbruke fellesmodellene i repoet og bruke MCP-validatoren underveis.

---

## Importhierarki

```
linkml:types          (alltid)
    ↓
common-ap-no          (bare AP-NO-profilene importerer denne direkte)
    ↓
dcat-ap-no / dqv-ap-no / skos-ap-no / …   (AP-NO-profiler)
    ↓
domenemodell          (importerer én eller flere AP-NO-profiler)

fint-common           (bare FINT-domenemodellene importerer denne)
    ↓
fint-administrasjon / fint-arkiv / …

fair-metadata         (kan importeres av alle domenemodeller)
```

Domenemodeller importerer **AP-NO-profilene** — ikke `common-ap-no` direkte.
De arver typer, subsets og slots fra AP-NO automatisk gjennom profilene.
`fint-common` er forbeholdt FINT-modellene.

---

## Hva importerer du?

| Du lager … | Importer |
|---|---|
| En AP-NO-profil | `linkml:types` + `../common/common-ap-no-schema` |
| En domenemodell (NGR, o.l.) | `linkml:types` + aktuelle AP-NO-profil(er) |
| En FINT-domenemodell | `linkml:types` + `../fint-common/fint-common-schema` |
| Modell med FAIR-dokumentasjon | + `../../fair/fair-metadata/fair-metadata-schema` |

---

## Katalogstruktur

```
src/linkml/<domene>/<modellnavn>/
    <modellnavn>-schema.yaml       ← selve skjemaet

examples/<domene>/
    <modellnavn>-eksempel.yaml     ← minst ett eksempel-datasett

tests/fixtures/                    ← bare nødvendig for AP-NO-profiler uten tree_root
    <modellnavn>-fixture.yaml
```

Legg til modellnavnet i `Makefile` i riktig liste
(`AP_NO_SCHEMAS`, `NGR_SCHEMAS`, `FINT_SCHEMAS`, o.l.) slik at
`make test`, `make gen-shacl` o.l. tar med den nye modellen automatisk.

---

## Steg for steg

### 1 — Opprett skjemafilen

Lag `src/linkml/<domene>/<modellnavn>/<modellnavn>-schema.yaml`.
Bruk malen nedenfor og tilpass:

```yaml
id: https://data.norge.no/linkml/<modellnavn>      # HTTP-URI, påkrevd (FAIR F1)
name: <modellnavn>
title: <Menneskelig tittel>
description: >
  Kort beskrivelse av hva domenemodellen dekker.
version: "1.0.0"                                   # Semantisk versjon (FAIR F4)

default_prefix: https://data.norge.no/linkml/<modellnavn>/
default_range: string

imports:
  - linkml:types
  - ../../ap-no/dcat-ap-no/dcat-ap-no-schema       # velg relevante AP-NO-profil(er)
  # - ../../fair/fair-metadata/fair-metadata-schema # legg til for FAIR-dokumentasjon

prefixes:
  linkml: https://w3id.org/linkml/
  dct:    http://purl.org/dc/terms/
  # legg til prefiks for vokabular du bruker

subsets:
  Obligatorisk:
    description: Obligatorisk egenskap.
  Anbefalt:
    description: Anbefalt egenskap.
  Valgfri:
    description: Valgfri egenskap.

classes:

  MinContainer:                                     # tree_root-klasse — trenger ikke class_uri
    tree_root: true
    description: Rotcontainer for <modellnavn>-instanser.
    slots:
      - mine_objekter

  MittObjekt:
    class_uri: ex:MittObjekt                        # eksplisitt class_uri (FAIR F3/I1)
    description: Beskrivelse av klassen.
    slots:
      - id
      - tittel                                      # fra dcat-ap-no via common-ap-no
      - <egne-slots>
    slot_usage:
      tittel:
        required: true
        in_subset:
          - Obligatorisk

slots:

  mine_objekter:
    slot_uri: ex:harObjekt
    range: MittObjekt
    multivalued: true
    inlined_as_list: true
    description: Liste av objekter i containeren.

  # Definer alle egenskaper som globale slots — aldri som attributes i klassen
  <eget-slot>:
    slot_uri: <prefix>:<lokal>                      # eksplisitt slot_uri (FAIR I1)
    range: string
    description: Hva egenskapen betyr.
```

### 2 — Legg til i Makefile

Åpne `Makefile` og legg til modellnavnet i riktig liste:

```makefile
NGR_SCHEMAS := ngr-adresse <modellnavn>
```

### 3 — Lag et eksempel-datasett

Lag `examples/<domene>/<modellnavn>-eksempel.yaml` med minst én instans:

```yaml
mine_objekter:
  - id: https://example.org/objekt/1
    tittel:
      - value: Eksempel-objekt
        language: nb
```

### 4 — Valider underveis med MCP-validatoren

Bruk MCP-validatoren aktivt mens du modellerer — den gir raskere
tilbakemelding enn `make test`:

```bash
# Standard validering (linting + obligatoriske felt)
make mcp-validate SCHEMA=src/linkml/<domene>/<modellnavn>/<modellnavn>-schema.yaml

# FAIR-validering (sjekker F1–R1.3)
make mcp-validate SCHEMA=src/linkml/<domene>/<modellnavn>/<modellnavn>-schema.yaml POLICY=fair
```

Validatoren bygger containeren automatisk første gang. Deretter
trengs ikke rebuild — endringer i `server.py` og `policies/` tar
effekt umiddelbart.

### 5 — Kjør full testsuite

```bash
make test
```

Linter alle skjemaer og validerer alle eksempel-datasett.

---

## Hva får du fra AP-NO-profilene

Ved å importere en AP-NO-profil arver du automatisk alt fra `common-ap-no`
(via profilen) — du trenger ikke importere `common-ap-no` direkte.

**Typer fra `common-ap-no`** (tilgjengelige via profilene)

| Navn | RDF-type | Bruk |
|---|---|---|
| `LangString` | `rdf:langString` | Flerspråklige strenger (tittel, beskrivelse …) |
| `Duration` | `xsd:duration` | Varighet, f.eks. `PT15M` |
| `GYear` | `xsd:gYear` | Årstall, f.eks. `2024` |
| `NonNegativeInteger` | `xsd:nonNegativeInteger` | Telling, størrelse |

**Gjenbrukbare slots** (eksempler fra `common-ap-no`, tilgjengelige via profilene)

```yaml
classes:
  MittObjekt:
    slots:
      - id          # identifier: true, range: uriorcurie
      - tittel      # slot_uri: dct:title, range: LangString
      - beskrivelse # slot_uri: dct:description, range: LangString
      - utgiver     # slot_uri: dct:publisher, range: uriorcurie
      - lisens      # slot_uri: dct:license, range: uriorcurie
```

Se `src/linkml/ap-no/common/common-ap-no-schema.yaml` for full liste
over tilgjengelige typer og slots.

---

## FAIR-konformitet med fair-metadata

For å dokumentere eksplisitt at en ressurs er FAIR-konform,
importer `fair-metadata` og legg til en referanse til `FAIRMetadata`:

```yaml
imports:
  - linkml:types
  - ../../ap-no/dcat-ap-no/dcat-ap-no-schema
  - ../../fair/fair-metadata/fair-metadata-schema

classes:
  MittDatasett:
    class_uri: dcat:Dataset
    slots:
      - id
      - tittel
      - fair_metadata              # ← lenke til FAIR-vurdering

slots:
  fair_metadata:
    slot_uri: fair:harFAIRMetadata
    range: FAIRMetadata            # fra fair-metadata-schema
    description: FAIR-metadata for dette datasettet.
```

Eksempel-datasett med FAIR-metadata:

```yaml
datasett:
  - id: https://example.org/datasett/1
    tittel:
      - value: Mitt datasett
        language: nb
    fair_metadata:
      id: https://example.org/fair/datasett/1
      ressursIdentifikator: https://example.org/datasett/1
      ressurstype: dcat:Dataset
      tilgangsmetadata:
        tilgangsURL: https://example.org/api/datasett
        tilgangsrettar: http://publications.europa.eu/resource/authority/access-right/PUBLIC
      gjenbruksmetadata:
        lisens: https://creativecommons.org/licenses/by/4.0/
      proveniensmetadata:
        ansvarlegAktoer: https://organization-catalog.fellesdatakatalog.digdir.no/organizations/123456789
      katalogregistrering:
        registrertIKatalog: https://data.norge.no
```

Valider at modellen tilfredsstiller FAIR-kravene:

```bash
make mcp-validate SCHEMA=src/linkml/<domene>/<modellnavn>/<modellnavn>-schema.yaml POLICY=fair
```

En modell som bruker `fair-metadata` korrekt skal gi:

```json
{ "valid": true, "errorCount": 0, "warningCount": 0 }
```

---

## Modelleringsprinsipper (sammendrag)

Se `CLAUDE.md` for full oversikt. De viktigste reglene:

**Norsk bokmål**
Alle klassenavn, slotnavn og beskrivelser skrives på norsk bokmål.

**Slots, ikke attributes**
Alle egenskaper defineres som globale `slots:` på toppnivå — aldri som
`attributes:` inne i en klasse.

**Lenking fremfor inlining**
Klasser som kan opptre selvstendig får `id`-slot med `identifier: true`.
Referanser til slike klasser skal *ikke* ha `inlined: true`.

**Eksplisitte URI-er**
Alle klasser skal ha `class_uri` (unntatt `tree_root`-containerklasser).
Alle slots skal ha `slot_uri`. Begge deler er påkrevd av FAIR-policyen.

**`slot_usage` for klassespesifikke innskrenkninger**
`required: true` og `in_subset:` settes i `slot_usage` på klassen,
ikke i den globale slotdefinisjonen.

---

## Sjekkliste før innsjekking

```
[ ] id er en HTTPS-URI
[ ] title og description er satt på skjemanivå
[ ] version er satt (f.eks. "1.0.0")
[ ] Importerer AP-NO-profil(er) — ikke common-ap-no direkte
[ ] Klasse- og slotnavn er på norsk bokmål
[ ] Alle klasser (unntatt tree_root) har class_uri
[ ] Alle globale slots har slot_uri
[ ] Minst ett standard-vokabularprefiks (dct, dcat, skos, prov …)
[ ] make test kjører uten feil
[ ] make mcp-validate POLICY=fair gir 0 feil og akseptable advarsler
```
