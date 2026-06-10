# Plan: OpenAPI / AsyncAPI-generering frå LinkML-modellskjema

## Bakgrunn

Fleire domenemodeller i dette repoet skal eksporterast til OpenAPI og/eller AsyncAPI
for bruk i REST-API-dokumentasjon, event-driven arkitektur og verktøy for kodegenerering
(f.eks. openapi-generator, AsyncAPI generator).

**Vurdering av native verktøy (utført):**
- `gen-openapi` finst ikkje i `linkml==1.11.1`
- `linkml.generators` har inga OpenAPI-modul
- avrotize 3.5.11 har `oas2s` (les OpenAPI) men ikkje `s2oas` / `j2oas` (skriv OpenAPI)

**Konklusjon: eigen Python-script er nødvendig.**
JSON Schema-generatoren (`gen-json-schema`) produserer allereie `$defs` per klasse
med alle eigenskapar og typar. OpenAPI 3.1 brukar JSON Schema direkte under
`components/schemas/`, så transformasjonen er strukturell — ikkje semantisk.

---

## Avklarte val

| # | Spørsmål | Svar |
|---|---|---|
| 1 | Omfang | Berre `components/schemas` — reint skjemabibliotek, ingen paths/channels |
| 2 | Format | Begge — `openapi: false` og `asyncapi: false` som eigne opt-in-flagg i `manifest.yaml` |
| 3 | OpenAPI-versjon | 3.1 — fullstendig JSON Schema-kompatibel |

---

## Teknisk tilnærming

Pipeline per skjema:
```
<modell>-schema.json  ($defs)
    ↓  gen-openapi.py
<modell>-openapi.yaml   (OpenAPI 3.1, validert med openapi-spec-validator)
    ↓  gen-asyncapi.py
<modell>-asyncapi.yaml  (AsyncAPI 3.0, validert med asyncapi validate)
```

`$ref`-adresser vert reindekserte: `#/$defs/X` → `#/components/schemas/X`.
Metadata (`title`, `version`, `description`, `id`) hentast frå YAML-skjemaet.

---

## Steg 1 — Verifiser JSON Schema-format ✓

JSON Schema 2019-09, 39 klasser i `$defs`, ingen `allOf`/`anyOf`/`oneOf`.
`version` er `null` i JSON Schema-outputen — hentast frå YAML.
Datofelt med `format: date/date-time` passast gjennom direkte (støtta i OpenAPI 3.1).

---

## Steg 2 — Skriv `gen-openapi.py` ✓

`src/assets/scripts/gen-openapi.py` — køyrer i `localhost/python-pytest:latest`.
Testvkøyrt: 39 klasser, 22 korrekte `#/components/schemas/`-refs, `info`-blokka korrekt.

---

## Steg 3 — Legg til validatorar ✓

- `openapi-spec-validator>=0.9.0` lagt til i `requirements-python-test.txt`, container rebuilda
- `src/assets/containers/Dockerfile.asyncapi-cli` oppretta (wrapper rundt `docker.io/asyncapi/cli:6.0.2`)
- `asyncapi-build-docker`-mål lagt til i Makefile og `.PHONY`

---

## Steg 4 — Test script manuelt på `samt-bu` ✓

| Sjekk | Resultat |
|---|---|
| `openapi-spec-validator` exit code | 0 — OK ✓ |
| `openapi:` | `3.1.0` ✓ |
| Antal klasser i `components/schemas` | 39 ✓ |
| `$ref`-adresser | 22 korrekte, 0 attståande `#/$defs/` ✓ |
| `info.title` / `info.contact.url` | Korrekt frå YAML-metadata ✓ |
| `paths` | `{}` ✓ |

---

## Steg 5 — Manifest-flagg ✓

`openapi: false` og `asyncapi: false` lagt til i alle 23 `manifest.yaml`-filer med `generators:`-seksjon.

---

## Steg 6 — Makefile-mål OpenAPI ✓

`define run_gen_openapi`-makro med manifest-sjekk, generering og validering.
Mål: `gen-openapi`, `domain-gen-openapi`, `schema-gen-openapi`. Integrert i `domain_target`.

---

## Steg 7 — AsyncAPI ✓

`src/assets/scripts/gen-asyncapi.py` oppretta (AsyncAPI 3.0-format: `channels: {}`, `operations: {}`).
`define run_gen_asyncapi`-makro og tilhøyrande mål lagt til i Makefile.
`asyncapi-cli-local` lagt til i `ensure-images`-jobben og `generate`-jobben i `generate.yml`.
`Dockerfile.asyncapi-cli` lagt til i `paths:`-trigger og cache-nøkkel.
`openapi` og `asyncapi` lagt til i artefaktgenereringsløkka.

---

## Steg 8 — Publisering i portalen ✓

`mkdocs/publish.sh`:
- `artifact_label()`: `openapi.yaml) echo "OpenAPI 3.1"` og `asyncapi.yaml) echo "AsyncAPI 3.0"`
- `ARTIFACT_ORDER`: `openapi.yaml asyncapi.yaml` etter `schema.xsd`

---

## Prioritert handlingsliste

| # | Steg | Status |
|---|---|---|
| 1 | Verifiser JSON Schema-format | ✓ |
| 2 | Skriv `gen-openapi.py` | ✓ |
| 3 | Legg til validatorar | ✓ |
| 4 | Test manuelt på `samt-bu` | ✓ |
| 5 | Manifest-flagg | ✓ |
| 6 | Makefile-mål OpenAPI | ✓ |
| 7 | AsyncAPI | ✓ |
| 8 | Publisering | ✓ |

---

## Utført

Utført 2026-06-10. Alle åtte steg er fullførte.

**Kva som vart gjort:**
- `src/assets/scripts/gen-openapi.py` og `gen-asyncapi.py` oppretta — transformerer generert JSON Schema til OpenAPI 3.1 og AsyncAPI 3.0 ved å reindeksere `$defs` til `components/schemas` og hente metadata frå YAML-skjemaet
- `openapi-spec-validator>=0.9.0` lagt til i `requirements-python-test.txt` — validering køyrer i eksisterande `python-pytest`-container
- `src/assets/containers/Dockerfile.asyncapi-cli` oppretta (wrapper rundt `docker.io/asyncapi/cli:6.0.2`)
- `openapi: false` og `asyncapi: false` lagt til i alle 23 `manifest.yaml`-filer med `generators:`-seksjon (opt-in)
- `run_gen_openapi` og `run_gen_asyncapi`-makroane med tilhøyrande bulk/domene/skjema-mål lagt til i Makefile og integrert i `domain_target`
- `asyncapi-cli-local` lagt til i `ensure-images`-jobben i `generate.yml` (cache/GHCR/bygg/last/push, same mønster som avrotize)
- `openapi` og `asyncapi` lagt til i artefaktgenereringsløkka i `generate.yml`
- `mkdocs/publish.sh` oppdatert med etikettar og plasseringsrekkjefølgje for `openapi.yaml` og `asyncapi.yaml`

**Avvik frå opphavleg plan:**
- XSD-outputfilnamn retta frå `<name>.xsd` til `<name>-schema.xsd` i Makefile — `schema.xsd`-suffikset i `ARTIFACT_ORDER` leita etter `<name>-schema.xsd`, ikkje `<name>.xsd`, så XSD-fila var aldri synleg i portalen. Retta i steg 8.
- AsyncAPI INFO-melding om v3.1.0 frå `asyncapi validate` er eit linting-tips, ikkje ein feil — akseptert, exit code 0.
