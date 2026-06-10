# Plan: XML Schema (XSD)-generering frå LinkML-modellskjema

## Bakgrunn

Fleire domenemodeller i dette repoet skal eksporterast til XML Schema (XSD) for
bruk i systemintegrasjon, SOAP-tenester og verktøy som ikkje støttar JSON Schema
eller SHACL.

**Vurdering av native `gen-xsd`** (utført steg 1):
`gen-xsd` eksisterer ikkje i `linkml==1.11.1` — verken som kommando eller som
modul (`linkml.generators.xsdgen`). Generatoren vart fjerna frå `linkml`-pakken
i nyare versjonar.

**Konklusjon: avrotize er hovudvegen.**
[avrotize](https://github.com/clemensv/avrotize) konverterer JSON Schema til XSD
via Avro Schema som mellomformat: `gen-json-schema` → `avrotize j2a` → `avrotize a2x`.
`json_schema: true` er allereie aktivert for alle skjema, så mellomsteget krev
ingen nye generator-køyringar.

## Avklarte val

1. **Korrekt XSD-semantikk er krav** — brukstilfellet er systemintegrasjon der
   XSD-fila vert brukt til validering og kodegenerering.
2. **Publisering i portalen** — `.xsd`-filer skal visast som nedlastbar ressurs
   i dokumentasjonsportalen, same måte som `.shacl.ttl` og `.owl.ttl` i dag.
3. **Opt-in per modell** — `xsd: false` er standard i `manifest.yaml`-malen.
   Kvart skjema aktiverer eksplisitt med `xsd: true`.

---

## Steg 1 — Verifiser `gen-xsd` i eksisterande container ✓

```bash
podman run --rm -e HOME=/tmp --user root localhost/linkml-local:latest gen-xsd --help
# → Exit 127: gen-xsd not found

podman run --rm -e HOME=/tmp --user root localhost/linkml-local:latest \
    python3 -c 'from linkml.generators import xsdgen'
# → ImportError: cannot import name 'xsdgen'
```

`gen-xsd` finst ikkje i `linkml==1.11.1`. Avrotize-pipeline er aktivert som primærveg.

---

## Steg 2 — Bygg avrotize-container ✓

`src/assets/containers/Dockerfile.avrotize` oppretta, variablar og `avrotize-build-docker`-mål lagt til i `Makefile`. avrotize 3.5.11 installert i image `localhost/avrotize-local:latest`. Begge kommandoane `j2a` og `a2x` er tilgjengelege.

---

## Steg 3 — Test pipeline på eit enkelt skjema ✓

Køyrt på `samt-bu`. Output: `generated/samt/samt-bu/samt-bu.xsd` (2470 linjer).

**Resultat — kva fungerer:**
- Alle klasser er `xs:complexType` med riktige namn (`Datasett`, `Elev`, `Skole`, osv.)
- `xs:sequence` + `xs:documentation` (frå `description:`) er bevart på alle element
- Multivalued slots → `<xs:element name="item" minOccurs="0" maxOccurs="unbounded" type="xs:string"/>`
- Containerklassen `SamtBuContainer` har typerte referansar til korrekte `xs:complexType`-ar (t.d. `type="Basisgruppe"`)
- Velforma XML, rootelement er `{http://www.w3.org/2001/XMLSchema}schema`

**Kjende avvik — aksepterte:**
- Referanse-slots (`utgiver`, `produsent`, `har_skoleeier` o.l.) er `xs:string` (URI-streng), ikkje `xs:complexType`-referanse. Dette er korrekt for LinkML sitt lenkingsmønster (URI-baserte referansar), men gjev ikkje XSD-referanseintegritet.
- `document_wrapper*`-typar på slutten av fila er avrotize-intern boilerplate frå handtering av JSON Schema sin top-level union. Ikkje semantisk relevante.

**Kjende avvik — krev tiltak i steg 5 (Makefile):**

| Problem | Årsak | Kan løysast med flagg? | Tiltak |
|---|---|---|---|
| `targetNamespace="urn:"` | avrotize fallback-namespace | Ja — `a2x --namespace <uri>` | Les `id`-feltet frå YAML og send det som `--namespace` |
| Datofelt som `xs:integer` | `j2a` konverterer JSON Schema `"format": "date"` til Avro `"int"` (utan `"logicalType": "date"`) — ikkje ein avrotize-flagg-mangel, men ein `j2a`-konverteringsfeil | Nei | Post-prosessering av XSD-outputen: byt ut `xs:integer` med `xs:date`/`xs:dateTime` for felt med `"format": "date"`/`"date-time"` i JSON Schema |

**Undersøkt og dokumentert 2026-06-10:**
JSON Schema har korrekt `"format": "date", "type": ["string", "null"]` for alle datofelt.
`j2a` mappar dette til Avro `["null", "int"]` i staden for `["null", {"type": "int", "logicalType": "date"}]`.
`a2x` har ingen flagg for datobehandling. Korkje `j2a` eller `a2x` tilbyr flagg som løyser dette.

---

## Steg 4 — Legg til `xsd`-flagg i `manifest.yaml`-mal ✓

Oppdaterte alle 23 eksisterande `manifest.yaml`-filer (dei som har `generators:`-seksjon) med `xsd: false` som siste felt under `generators:`. Standard er `false` (opt-in).

Merk: ingen `xsd_flags` — avrotize-pipeline har ikkje flagg som er aktuelle per skjema.

---

## Steg 5 — Legg til `gen-xsd`-mål i `Makefile` ✓

Implementert:
- `define run_gen_xsd` — shell for-loop-makro, hoppar over skjema utan `xsd: true`
- `gen-xsd` — bulk-mål for alle skjema
- `domain-gen-xsd DOMAIN=<domene>` — per-domene-mål
- `schema-gen-xsd SCHEMA=<sti>` — per-skjema-mål
- Integrert i `domain_target`-makroen (køyrer automatisk ved `make <domene>`)

**Pipeline per skjema:**
1. `avrotize j2a` — JSON Schema → Avro Schema (`.avsc`, midlertidig)
2. `avrotize a2x --namespace <id>` — Avro Schema → XSD (løyser avvik 1: `targetNamespace`)
3. `fix-xsd-dates.py` — XSD post-prosessering: `xs:integer` → `xs:date`/`xs:dateTime` for datofelt (løyser avvik 2)
4. Slettar midlertidig `.avsc`

**Årsak til XSD post-prosessering i staden for AVSC-patching:**
`a2x` ignorerer Avro logical types (`logicalType: date`) fullstendig — konverterer alltid til `xs:integer`. `fix-xsd-dates.py` brukar JSON Schema som fasit og erstattar typane direkte i XSD-outputen.

**Verifisert på `samt-bu`:**
- `targetNamespace="https://data.norge.no/samt/samt-bu"` ✓
- `endringsdato`, `utgivelsesdato`, `startdato`, `sluttdato` → `xs:date` ✓
- `begynnelse`, `slutt` → `xs:dateTime` ✓

---

## Steg 6 — Publisering i portalen ✓

**`.github/workflows/generate.yml`:**
- `Dockerfile.avrotize` lagt til i `paths:`-trigger
- Avrotize image-blokk (cache/GHCR/bygg/last/push) lagt til i `ensure-images`-jobben
- `avrotize-local.tar.zst` lagt til i nøkkelen for genererte artefaktar
- `avrotize-local` gjenopprettings-steg lagt til i `generate`-jobben
- `podman load` for avrotize-image lagt til i image-innlastingssteget
- `xsd` lagt til i artefaktgenereringsløkka

**`mkdocs/publish.sh`:**
- `schema.xsd) echo "XML Schema (XSD)" ;;` lagt til i `artifact_label()`-funksjonen
- `schema.xsd` lagt til i `ARTIFACT_ORDER` (etter `schema.json`, før `ontology.ttl`)

XSD-filer vert kopiert automatisk via `find "$schema_dir" -maxdepth 1 -type f -exec cp {} "$out/" \;` som allereie fangar alle filer i skjemagenerert katalog.

---

## Prioritert handlingsliste

| # | Steg | Fil | Merknad |
|---|---|---|---|
| 1 | ✓ Verifiser container | — | `gen-xsd` finst ikkje i linkml 1.11.1 |
| 2 | ✓ Bygg avrotize-container | `src/assets/containers/Dockerfile.avrotize` | avrotize 3.5.11, j2a + a2x OK |
| 3 | ✓ Test pipeline | `generated/samt/samt-bu/samt-bu.xsd` | OK — 2 avvik krev tiltak i steg 5 |
| 4 | ✓ Manifest-mal | Alle `manifest.yaml` med `generators:` | `xsd: false` lagt til i 23 filer |
| 5 | ✓ Makefile-mål | `Makefile`, `src/assets/scripts/fix-xsd-dates.py` | `run_gen_xsd`, `gen-xsd`, `domain-gen-xsd`, `schema-gen-xsd`, XSD post-prosessering |
| 6 | ✓ CI + portal | `.github/workflows/generate.yml`, `mkdocs/publish.sh` | Artefaktar + nedlastingslenker |

---

## Avhengigheiter

- Nytt container-image `localhost/avrotize-local:latest` (bygd frå `Dockerfile.avrotize`)
- `json_schema: true` må vere sett i manifest for skjema som aktiverer `xsd: true` — det er det for alle skjema i dag
- `xmllint` (`libxml2-utils`) for manuell validering under utvikling — finst i podman-basert testkøyring
- Ingen endringar i CI-matrix nødvendig

---

## Utført

Utført 2026-06-10. Alle seks steg er fullførte.

**Kva som vart gjort:**
- Nytt container-image `localhost/avrotize-local:latest` (avrotize 3.5.11) oppretta med eigen `Dockerfile.avrotize`
- XSD-generering via pipeline: `gen-json-schema` → `avrotize j2a` → `avrotize a2x` → `fix-xsd-dates.py`
- `fix-xsd-dates.py` skriven for å korrigere dato-typar (`xs:integer` → `xs:date`/`xs:dateTime`) sidan avrotize ignorerer Avro logical types
- `Makefile` utvida med `run_gen_xsd`-makro og `gen-xsd`/`domain-gen-xsd`/`schema-gen-xsd`-mål
- `xsd: false` lagt til i alle 23 `manifest.yaml`-filer med `generators:`-seksjon (opt-in)
- GitHub Actions-workflow oppdatert med avrotize image-handtering og `xsd` i genereringsløkka
- `mkdocs/publish.sh` oppdatert med `schema.xsd`-etikett og plasseringsrekkjefølgje
- `CLAUDE.md` oppdatert med «Planen kjem først»-regelen

**Avvik frå opphavleg plan:**
- Opphavleg plan vurderte patching av `.avsc`-fila (Avro Schema) for å korrigere datotypar. Etter testing viste det seg at `a2x` ignorerer Avro `logicalType` fullstendig og alltid skriv `xs:integer`. Post-prosessering av XSD-outputen direkte vart difor valt i staden.
- `fix-avsc-dates.py` (mellombels script for AVSC-patching) vart oppretta og deretter sletta.
- `j2a` mappar `date-time` til Avro `int` (ikkje `long`), same som `date`. Begge vert difor korrigert frå `xs:integer`.
