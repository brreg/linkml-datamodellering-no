# mcp-linkml-modell-utkast

MCP-server for generering av LinkML-skjema frå JSON Schema (eller som tomt utkast). Det genererte skjemaet følgjer modellprinsippa i dette repoet — globale slots, containerklasse, URI-mapping og begrepsreferanse-stubbar.

## Bruk

```bash
# Generer frå ein JSON Schema-fil (legg fila i tmp/ først)
make mcp-generate SCHEMA=tmp/modell.json

# Valfrie parametrar
make mcp-generate SCHEMA=tmp/modell.json FORMAT=json-schema PROFILE=default
```

Generert YAML-fil vert skriven til same katalog som inputfila (`tmp/modell-schema.yaml`).

## Konverteringspipeline

```
JSON Schema (fil)
      │
      ▼
  converter.py
  ├── Les $defs / definitions → klassar
  ├── Omset JSON-typar til LinkML-ranges (type_mapping / format_mapping)
  ├── Handterer $ref, array, anyOf (nullable)
  ├── Lagar globale slots for alle eigenskapar
  ├── Legg til id-slot (identifier: true, range: uriorcurie)
  ├── Legg til slot_usage med required og in_subset per klasse
  └── Genererer Containerklasse (tree_root: true) med attributt per klasse
      │
      ▼
  validator.py  (om validate: true)
  ├── A — Lint med linkml.linter.Linter
  └── B — Dummy-datasett-validering mot containerklassen
      │
      ▼
  Resultat: { linkmlSchema, warnings, lintIssues, dummyValidation }
```

## Kva det genererte skjemaet inneheld

| Element | Beskriving |
|---|---|
| `id`, `name`, `description` | Henta frå argumenta eller JSON Schema |
| `prefixes` | Standard vokabularprefiksar frå profilen (`dct`, `dcat`, `foaf`, `skos`, `xsd` m.fl.) + `ex:` som placeholder |
| `imports` | `linkml:types` (standard) |
| `subsets` | `Obligatorisk`, `Anbefalt`, `Valgfri` |
| `slots.id` | Global `id`-slot med `identifier: true` og `range: uriorcurie` |
| `slots.<prop>` | Ein global slot per eigeskap i JSON Schema, med `slot_uri: ex:<prop>` |
| `classes.<Klasse>` | Ein klasse per `$defs`-objekt. Har `class_uri`, `annotations.begrepsidentifikator: TODO` og `slot_usage` med `required`/`in_subset` |
| `classes.Containerklasse` | `tree_root: true`, med `multivalued`/`inlined`/`inlined_as_list`-attributt per klasse |

### Typeomsetting

| JSON Schema-type | LinkML range |
|---|---|
| `string` | `string` |
| `integer` | `integer` |
| `number` | `float` |
| `boolean` | `boolean` |
| `format: uri` | `uriorcurie` |
| `format: date` | `date` |
| `format: date-time` | `datetime` |
| array | `multivalued: true` + range frå `items` |
| `$ref: #/$defs/Foo` | `range: Foo` |
| `anyOf` (nullable) | range frå den ikkje-null-typen |

### Avgrensingar

- `anyOf` med fleire ikkje-null-typar → `range: string` + advarsel
- `oneOf` / `allOf` → `range: string` + advarsel
- Eksterne `$ref` (ikkje `#`-relative) → `range: string` + advarsel

## Validering av generert skjema

Når `validate: true` (standard) køyrer to steg automatisk etter generering:

**A — Lint:** `linkml.linter.Linter` sjekkar strukturelle feil i det genererte skjemaet.

**B — Dummy-datasett-validering:** Bygger eit minimalt datasett med plasshaldarverdiar for alle `required`-slots og `identifier`-slots, og validerer det mot containerklassen med `linkml.validator.validate`. Dette fangar opp type- og referansefeil som berre syner seg med faktiske data.

## Profiler

Profiler styrer korleis konverteringa oppfører seg. Standard profil er `default`.

```bash
make mcp-generate SCHEMA=tmp/modell.json PROFILE=default

# List tilgjengelege profiler via MCP-verktøyet list_profiles
```

Profilane ligg i `profiles/<namn>.yaml` og definerer:

| Konfig-nøkkel | Beskriving |
|---|---|
| `type_mapping` | JSON Schema-type → LinkML range |
| `format_mapping` | JSON Schema format → LinkML range (overrider type_mapping) |
| `standard_prefixes` | Prefiksar som vert lagt til i generert skjema |
| `schema_defaults.imports` | Imports-lista (standard: `[linkml:types]`) |
| `generation.add_id_slot` | Legg til `id`-slot med `identifier: true` (standard: true) |
| `generation.add_container_class` | Generer containerklasse (standard: true) |
| `generation.add_begrep_annotation` | Legg til `begrepsidentifikator: TODO`-stub (standard: true) |
| `subsets.required_maps_to` | Subset for `required`-felt (standard: `Obligatorisk`) |
| `subsets.non_required_default` | Subset for andre felt (standard: `Anbefalt`) |

## MCP-verktøy

| Verktøy | Skildring |
|---|---|
| `generate_linkml` | Genererer eit LinkML-skjema. Parametrar: `inputFormat` (`json-schema` eller `empty`), `inputContent` (JSON Schema som streng), `schemaId`, `schemaName`, `schemaTitle`, `profile`, `validate`. |
| `list_profiles` | Listar tilgjengelege konverteringsprofiler med namn og skildring. |

## NB! Etter generering — nødvendige tilpassingar

Det genererte skjemaet er eit **utkast** og krev manuell tilpassing:

1. **Erstatt `ex:`-prefiksar** med faktiske vokabular-URIar (`dct:`, `dcat:`, `skos:` o.l.)
2. **Fyll inn `begrepsidentifikator`** — finn rett begrep på [data.norge.no/concepts](https://data.norge.no/concepts) og kopier URI-en, på forma `https://concept-catalog.fellesdatakatalog.digdir.no/collections/<collection-id>/concepts/<concept-id>`
3. **Juster klassenamn** til norsk bokmål om nødvendig
4. **Importer AP-NO-profil** om skjemaet skal følgje DCAT-AP-NO, DQV-AP-NO o.l.
5. **Køyr bronze-validering** for å sjekke at grunnkrava er oppfylt:

```bash
make mcp-validate SCHEMA=src/linkml/<domene>/<modell>/<modell>-schema.yaml POLICY=bronze
```

Sjå [Ny domenemodell](https://brreg.github.io/linkml-datamodellering-no/ny-domenemodell/) for full rettleiing.
