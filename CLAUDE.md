# CLAUDE.md

Dette filen gir veiledning til Claude Code (claude.ai/code) ved arbeid i dette repoet.

## Formål

Dette repoet modellerer norske W3C-applikasjonsprofiler fra [data.norge.no/showroom](https://data.norge.no/showroom/overview) i [LinkML-format](https://linkml.io/linkml-model/latest/docs/specification/).

Profiler som skal modelleres:
- **DCAT-AP-NO** – Datakataloger (`src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml`) ✅
- **SKOS-AP-NO** – Begrepssamlinger ✅
- **CPSV-AP-NO** – Offentlige tjenester ✅
- **DQV-AP-NO** – Datakvalitet ✅
- **ModelldCAT-AP-NO** – Informasjonsmodeller
- **XKOS-AP-NO** – Utvidet klassifikasjon ✅

Egenskaper som går igjen i flere profiler samles i `common-ap-no-schema.yaml`.

## Importhierarki

```
linkml:types
    ↓
common-ap-no          ← bare AP-NO-profilene importerer denne direkte
    ↓
dcat-ap-no / dqv-ap-no / skos-ap-no / …
    ↓
domenemodeller        ← importerer AP-NO-profilene, ikke common-ap-no direkte

fint-common           ← bare FINT-domenemodellene importerer denne
    ↓
fint-administrasjon / fint-arkiv / …

fair-metadata         ← kan importeres av alle domenemodeller
```

## Kommandoer

LinkML kjøres via Podman med imaget `docker.io/linkml/linkml:latest`. Ingen lokal installasjon nødvendig.

```bash
make validate               # Valider alle skjemaer mot LinkML-metaskjemaet
make gen-jsonld             # Generer JSON-LD kontekst
make gen-shacl              # Generer SHACL shapes
make gen-jsonschema         # Generer JSON Schema
make gen-owl                # Generer OWL/Turtle-ontologi
make docs                   # Generer HTML-dokumentasjon

# Enkelt skjema direkte:
podman run --rm -v "$(pwd):/work" -w /work docker.io/linkml/linkml:latest \
  gen-linkml --validate src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml

# MCP-validator (raskere tilbakemelding under utvikling):
make mcp-validate SCHEMA=src/linkml/<domene>/<modell>/<modell>-schema.yaml
make mcp-validate SCHEMA=src/linkml/<domene>/<modell>/<modell>-schema.yaml POLICY=fair
```

## Katalogstruktur

```
src/linkml/
  ap-no/<profil>/           – AP-NO-profiler (importerer common-ap-no)
  fair/fair-metadata/       – FAIR-metadataoverbygning
  fint/<domene>/            – FINT-domenemodeller (importerer fint-common)
  ngr/<domene>/             – NGR-domenemodeller

examples/<domene>/          – Eksempeldata (YAML)
tests/                      – Testskript og fixtures
generated/                  – Genererte artefakter (ikke innsjekket)
docs/                       – Utviklerveiledninger
```

## Modelleringsprinsipper

### Modelleringsspråk
Standard modelleringsspråk er **norsk bokmål** — klasse- og slotnavn, beskrivelser og kommentarer skrives på bokmål. Unntaket er tekniske begreper som er fastsatt i en spesifikasjon (f.eks. `dcat:Dataset` → `Datasett`).

### Slots, ikke attributes
Alle egenskaper modelleres som globale slots under `slots:` på toppnivå i skjemaet — aldri som `attributes:` inne i en klasse. Klasser refererer til slots via `slots:`-listen. Klassespesifikke innskrenkninger (`required`, `in_subset` o.l.) legges i `slot_usage` på klassen.

```yaml
# Riktig
slots:
  tittel:
    slot_uri: dct:title
    range: string

classes:
  Datasett:
    slots:
      - tittel
    slot_usage:
      tittel:
        required: true

# Feil
classes:
  Datasett:
    attributes:
      tittel:
        slot_uri: dct:title
        range: string
        required: true
```

### Lenking fremfor inlining
Alle klasser som kan opptre selvstendig får et `id`-slot med `identifier: true` og `range: uriorcurie`. Referanser til andre klasser har **ikke** `inlined: true` (som er standard når målklassen har en identifikator). Dette sikrer at instanser refereres med URI i stedet for å bygges inn.

### Klassenavn
Norske bokmålsnavn brukes for alle klasser (f.eks. `Datasett`, `Katalog`, `Distribusjon`). Hjelpeklasser for W3C-vokabulartermer kan bruke kortere engelske navn (`Begrep`, `Spraak`, `Mediatype`).

### Slot-uri og class-uri
Alle klasser og slots har eksplisitt `class_uri` / `slot_uri` som mapper til de korrekte RDF-vokabularene (dcat:, dct:, foaf:, vcard: osv.). `tree_root`-containerklasser er unntatt fra kravet om `class_uri`.

### Obligatorisk/anbefalt/valgfri
`slot_usage` med `in_subset` brukes for å markere om en egenskap er `Obligatorisk`, `Anbefalt` eller `Valgfri` i henhold til spesifikasjonen. `required: true` settes kun på obligatoriske egenskaper.

### Flerspråklige strenger
`LangString` (type `rdf:langString`) brukes for alle egenskaper som er definert som `rdf:langString` i spesifikasjonen (tittel, beskrivelse, nøkkelord osv.).

### Endringer i koderepoet
Forsøk alltid å utføre minimale endringer som kun løser den spesifikke oppgava.

### Ny profil eller domenemodell
Se `docs/ny-domenemodell.md` for steg-for-steg-veiledning. Kortversjon:
1. Opprett `src/linkml/<domene>/<modellnavn>/<modellnavn>-schema.yaml`
2. Legg til modellnavnet i riktig liste i `Makefile`
3. Opprett `examples/<domene>/` med minst ett eksempel-datasett
