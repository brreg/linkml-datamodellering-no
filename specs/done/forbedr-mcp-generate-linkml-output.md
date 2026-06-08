# Forbedr mcp-generate: produser gyldig LinkML-schema

## Bakgrunn

`make mcp-generate SCHEMA=./tmp/bvrinnfelles_lm_v1.schema.json` genererte
`bvrinnfelles_lm_v1.schema-schema.yaml`. `linkml-lint` rapporterte:

- **~40 `no_undeclared_ranges`-feil** — slot-range-referansar til udefinerte typar
- **Fleire `standard_naming`-åtvarsel** — camelCase-slotnamn i staden for snake_case
- **`canonical_prefixes`-åtvarsel** — `ex`-prefiks med eksempel-URL
- **Massevis av `recommended`-åtvarsel** — slots manglar `description`
- **`Containerklasse` brukar globale slots** — skal bruke `attributes:`

Rota til dei fleste feila er at generatoren behandlar alle `$defs` i JSON Schema
som klasser. Mange av dei er primitive typar (`type: string` med format/pattern)
eller enum-verdisett — og skal mappes til `types:` eller `enums:` i LinkML.

## Tiltak 1 — Korrekt mapping av primitive typar til `types:`

**Problem:** JSON Schema-definisjonar med `type: string` eller `type: integer`
(og valfri `format`, `pattern`) vert genererte som klasser. Dei er ikkje klasser
— dei er datatypar. Eksempel frå input-skjemaet:

| JSON Schema def | type | format/pattern |
|---|---|---|
| `Versjonsnummer` | string | `pattern: ^(\d+\.)?...` |
| `Dato` | string | `format: date` |
| `DatoKlokkeslett` | string | `format: date-time` |
| `Kommunenummer` | string | (ingen) |
| `URL` | string | `format: uri` |
| `Aktivitetskode` | integer | (ingen) |

Desse skal genererast som LinkML `types:`:

```yaml
types:
  Versjonsnummer:
    uri: xsd:string
    base: str
    pattern: '^(\d+\.)?(\d+\.)?(\*|\d+)$'

  Dato:
    uri: xsd:date
    base: str

  DatoKlokkeslett:
    uri: xsd:dateTime
    base: str

  URL:
    uri: xsd:anyURI
    base: str

  Aktivitetskode:
    uri: xsd:integer
    base: int
```

**Format → LinkML URI-mapping:**

| JSON Schema format | LinkML `uri` |
|---|---|
| `date` | `xsd:date` |
| `date-time` | `xsd:dateTime` |
| `uri` | `xsd:anyURI` |
| (ingen) | `xsd:string` (for string) |
| (ingen) | `xsd:integer` (for integer) |

**Regel:** Ein `$def` med `type: string` eller `type: integer` og **utan** `enum`
og **utan** `properties` skal genererast som `type:`, ikkje `class:`.

## Tiltak 2 — Korrekt mapping av enum-verdisett til `enums:`

**Problem:** JSON Schema-definisjonar med `enum:`-liste vert genererte som klasser
eller ignorerte. Dei skal mappast til LinkML `enums:`.

Eksempel:

```json
"Maalform": { "type": "string", "enum": ["nob", "nno"] }
"Rolletype": { "type": "string", "enum": ["rolletype.dagligLeder", ...] }
```

Skal gi:

```yaml
enums:
  Maalform:
    permissible_values:
      nob: {}
      nno: {}

  Rolletype:
    permissible_values:
      rolletype.dagligLeder: {}
      # ...
```

**Regel:** Ein `$def` med `enum:`-nøkkel skal alltid genererast som `enum:`,
uavhengig av om `type: string` er sett.

## Tiltak 3 — Slotnamn: camelCase → snake_case

**Problem:** Generatoren bevarer JSON Schema-eigenskapsnamn direkte som slotnamn.
CLAUDE.md krev `snake_case` for alle slotnamn i norske domenemodeller (unntaket
er FINT-skjema som arvar camelCase frå FINT API).

Eksempel på feil:
- `maalformForTilbakemelding` → `maalform_for_tilbakemelding`
- `fagsystemReferanse` → `fagsystem_referanse`
- `internasjonaltPrefiks` → `internasjonalt_prefiks`
- `internasjonalAdresse` → `internasjonal_adresse`
- `vegadresseId` → `vegadresse_id`

**Regel:** Konverter alle slotnamn frå camelCase til snake_case ved hjelp av
standard regex (`([A-Z])` → `_\1.lower()`).

Unntak: slotnamn som alt er snake_case vert ikkje endra.

## Tiltak 4 — Slotnamn med bindestrek er ugyldige identifikatorar

**Problem:** JSON Schema-eigenskapen `e-postadresse` vert eit slotnamn med
bindestrek — ugyldig i mange samanhengar.

```
warning  Slot has name 'e-postadresse'  (standard_naming)
error    Class 'Varslingsadresse' slot 'e-postadresse' range 'E-postadresse' is not defined
```

**Regel:** Erstatt `-` med `_` i alle slotnamn.
`e-postadresse` → `e_postadresse`.

## Tiltak 5 — Containerklasse skal bruke `attributes:`, ikkje globale slots

**Problem:** Generatoren lagar containerklassen med globale slots:

```yaml
slots:
  innrapporterings:
    range: Innrapportering
    ...

classes:
  Containerklasse:
    tree_root: true
    slots:
      - innrapporterings
```

CLAUDE.md krev at containerklassen brukar `attributes:` (ikkje `slots:`):

```yaml
classes:
  GenerertContainer:
    tree_root: true
    attributes:
      innrapporterings:
        range: Innrapportering
        multivalued: true
        inlined: true
        inlined_as_list: true
```

**Regel:**
- Containerklassen heiter `<SchemaName>Container` (PascalCase, avleidd av
  `schemaName`-argumentet). Til dømes `schemaName: bvr-innfelles` →
  `BvrInnfellesContainer`.
- Containerklassen brukar `attributes:`, ikkje globale slots.
- Attributtnamna er i fleirtal (legg til `r` / `er` etter norsk morfologi, eller
  pass på at suffikset vert rett).

## Tiltak 6 — Generer stub-`description` for slots

**Problem:** Alle slots manglar `description`, noko som gjev `recommended`-åtvarsel.

**Løysing:** Generer ei stub-beskriving som minner modelleraren om å fylle inn:

```yaml
slots:
  dato:
    description: "TODO: beskriv eigenskapen"
    range: Dato
```

Dette eliminerer lint-støyen og gjer det tydeleg kva som manglar.

## Tiltak 7 — Fjern `ex:`-prefiks som placeholder

**Problem:** Generatoren brukar `ex: https://example.org/generated/` som
standardprefiks. Lint åtvarar om dette (`canonical_prefixes`).

**Løysing:** Parametriser `schemaId` og `schemaName` betre, og generer
`default_prefix` basert på `schemaId`:

```yaml
id: https://data.norge.no/bvr/bvr-innfelles
name: bvr-innfelles
default_prefix: https://data.norge.no/bvr/bvr-innfelles/
prefixes:
  bvr: https://data.norge.no/bvr/bvr-innfelles/
```

Fjern `ex:`-prefikset og bruk heller eit avleidd prefiks basert på det siste
leddet av `schemaId`.

## Gjennomføring

Endringane skal gjerast i MCP-generatoren (`src/mcp/linkml-generator/` eller
tilsvarande). Sjekk kvar generatorlogikk lever:

```bash
find src/ -name "*.py" | xargs grep -l "generate_linkml\|inputFormat\|json-schema" 2>/dev/null
```

Prioritert rekkjefølge:
1. **Tiltak 1** (types) — eliminerer ~40 feil
2. **Tiltak 2** (enums) — eliminerer fleire feil og gjev riktig modellstruktur
3. **Tiltak 3+4** (slotnamn) — eliminerer naming-åtvarsel
4. **Tiltak 5** (container) — følgjer CLAUDE.md-krav
5. **Tiltak 6** (description stub) — støy-reduksjon
6. **Tiltak 7** (prefiks) — polish

## Validering

Etter kvar endring:

```bash
make mcp-generate SCHEMA=./tmp/bvrinnfelles_lm_v1.schema.json
podman run --rm -v "$PWD:/work" -w /work -e PYTHONWARNINGS=ignore -e HOME=/tmp \
  --user root localhost/linkml-local:latest \
  linkml-lint tmp/bvrinnfelles_lm_v1.schema-schema.yaml 2>&1 | grep -c "error"
```

Målet er 0 feil og < 10 åtvarsel.
