# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Formål

Dette repoet modellerer norske W3C-applikasjonsprofiler fra [data.norge.no/showroom](https://data.norge.no/showroom/overview) i [LinkML-format](https://linkml.io/linkml-model/latest/docs/specification/).

Profiler som skal modelleres:
- **DCAT-AP-NO** – Datakataloger (`src/linkml/dcat-ap-no/schema.yaml`) ✅
- **SKOS-AP-NO** – Begrepssamlinger
- **CPSV-AP-NO** – Offentlige tjenester
- **DQV-AP-NO** – Datakvalitet
- **ModelldCAT-AP-NO** – Informasjonsmodeller
- **XKOS-AP-NO** – Utvidet klassifikasjon

Attributter som går igjen i fleire profiler samles i common-ap-no-schema.yaml

## Kommandoer

LinkML kjøres via Podman med imaget `docker.io/linkml/linkml:latest`. Ingen lokal installasjon nødvendig.

```bash
make validate               # Valider alle skjemaer mot LinkML-metaskjemaet
make gen-jsonld             # Generer JSON-LD kontekst
make gen-shacl              # Generer SHACL shapes
make gen-jsonschema         # Generer JSON Schema
make gen-owl                # Generer OWL/Turtle ontologi
make docs                   # Generer HTML-dokumentasjon

# Enkelt skjema direkte:
podman run --rm -v "$(pwd):/work" -w /work docker.io/linkml/linkml:latest \
  gen-linkml --validate src/linkml/dcat-ap-no/schema.yaml
```

## Katalogstruktur

```
src/linkml/<profil>/schema.yaml   – LinkML-skjema for profilen
examples/<profil>/                – Eksempeldata (YAML/JSON-LD/Turtle)
tests/                            – Validering av eksempeldata
generated/<profil>/               – Genererte artefakter (ikke innsjekket)
generated/<profil>/docs/           – Generert HTML-dokumentasjon
```

## Modelleringsprinsipper

### Lenking fremfor inlining
Alle klasser som kan opptre selvstendig får et `id`-slot med `identifier: true` og `range: uriorcurie`. Referanser til andre klasser har **ikke** `inlined: true` (som er standard når målklassen har en identifikator). Dette sikrer at instanser refereres med URI i stedet for å bygges inn.

### Klassenavn
Norske navn brukes for alle DCAT-AP-NO-klasser (f.eks. `Datasett`, `Katalog`, `Distribusjon`). Hjelpeklasser for W3C-vokabulartermer brukes med kortere engelske navn (`Begrep`, `Spraak`, `Mediatype`).

### Slot-uri og class-uri
Alle klasser og slots har eksplisitt `class_uri` / `slot_uri` som mapper til de korrekte RDF-vokabularene (dcat:, dct:, foaf:, vcard: osv.).

### Obligatorisk/anbefalt/valgfri
`slot_usage` med `in_subset` brukes for å markere om en egenskap er `Obligatorisk`, `Anbefalt` eller `Valgfri` i henhold til spesifikasjonen. `required: true` settes kun på obligatoriske egenskaper.

### Flerspråklige strenger
`LangString` (type `rdf:langString`) brukes for alle egenskaper som er definert som `rdf:langString` i spesifikasjonen (tittel, beskrivelse, nøkkelord osv.).

### Ny profil
Når en ny profil legges til:
1. Opprett `src/linkml/<profil>/schema.yaml`
2. Legg til profilens kortnavn i `SCHEMAS`-variabelen i `Makefile`
3. Opprett `examples/<profil>/` for eksempeldata
