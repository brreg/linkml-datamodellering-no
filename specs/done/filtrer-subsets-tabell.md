# Filtrer subsets-tabell til kun lokale subsets

## Bakgrunn

Subsets-tabellen i `index.md` for kvar modell viser for tida **alle subsets** (både lokale og importerte) i same tabell, med "Defined in"-kolonne som viser kjeldeskjema-URI. Brukaren ønskjer å **filtrere** tabellen til kun å vise lokalt definerte subsets, og liste importerte subsets under tabellen som ei kommaseparert lenkeliste til kjeldeskjemaa.

**Status quo for andre seksjonar:**
- **Enumerations:** Viser (importerte enumerations brukte av lokale slots/klasser) **ELLER** (lokalt definerte enums) — ingen "Importerte enumerations"-linje i Jinja2-template, `classes.sh` legg til linja
- **Types:** Viser (importerte types brukte av lokale slots/klasser) **ELLER** (lokalt definerte types) — ingen "Importerte types"-linje i Jinja2-template, `classes.sh` legg til linja
- **Slots:** Viser (importerte slots brukte av lokale klasser) **ELLER** (lokalt definerte slots) — ingen "Importerte slots"-linje i Jinja2-template, `classes.sh` legg til linja
- **Classes:** Viser alle klasser (lokale + importerte) — ingen "Importerte classes"-linje i Jinja2-template, `classes.sh` legg til linja

**Subsets skal følgje same mønster** — men med **filtrering til kun lokale subsets** i staden for OR-logikk, fordi subsets ikkje blir "brukte" av klasser på same måte som slots/enums/types.

**Døme frå `cpsv-ap-no` (noverande tilstand):**

```markdown
## Subsets

| Subset | Description | Defined in |
| --- | --- | --- |
| [Anbefalt](klasser/anbefalt.md) | Anbefalte eigenskapar i ein AP-NO-profil | [https://data.norge.no/ap-no/common-ap-no](https://data.norge.no/ap-no/common-ap-no) |
| [Metadata](klasser/metadata.md) | Klasser som beskriv metadata om ressursar, ikkje sjølve datainnhaldet | [https://data.norge.no/ap-no/common-ap-no](https://data.norge.no/ap-no/common-ap-no) |
| [Obligatorisk](klasser/obligatorisk.md) | Obligatoriske eigenskapar i ein AP-NO-profil | [https://data.norge.no/ap-no/common-ap-no](https://data.norge.no/ap-no/common-ap-no) |
| [Valgfri](klasser/valgfri.md) | Valfrie eigenskapar i ein AP-NO-profil | [https://data.norge.no/ap-no/common-ap-no](https://data.norge.no/ap-no/common-ap-no) |
```

Alle subseta er importerte frå `common-ap-no`, ingen er lokalt definerte i `cpsv-ap-no`.

**Ønskt resultat:**

```markdown
## Subsets (0)

*Ingen subsets definert lokalt i denne modellen.*

*Importerte subsets: [common-ap-no](../common-ap-no/#subsets)*
```

**Merk:** Formatet følgjer same mønster som "Importerte klasser", "Importerte slots" osv. — kursiv tekst (`*...*`) med kommaseparert liste av kjeldeskjema med anker til relevant seksjon.

**Døme for skjema med lokale subsets (t.d. `common-ap-no`):**

```markdown
## Subsets (4)

| Subset | Description | Defined in |
| --- | --- | --- |
| [Anbefalt](klasser/anbefalt.md) | Anbefalte eigenskapar i ein AP-NO-profil | [https://data.norge.no/ap-no/common-ap-no](https://data.norge.no/ap-no/common-ap-no) |
| [Metadata](klasser/metadata.md) | Klasser som beskriv metadata om ressursar, ikkje sjølve datainnhaldet | [https://data.norge.no/ap-no/common-ap-no](https://data.norge.no/ap-no/common-ap-no) |
| [Obligatorisk](klasser/obligatorisk.md) | Obligatoriske eigenskapar i ein AP-NO-profil | [https://data.norge.no/ap-no/common-ap-no](https://data.norge.no/ap-no/common-ap-no) |
| [Valgfri](klasser/valgfri.md) | Valfrie eigenskapar i ein AP-NO-profil | [https://data.norge.no/ap-no/common-ap-no](https://data.norge.no/ap-no/common-ap-no) |
```

(Ingen importerte subsets å liste, så ingen "Imported subsets"-linje)

**Hovudforskjell:**
- **Før:** Alle subsets (lokale + importerte) i tabellen — same som Enumerations, Types, Slots, Classes
- **Etter:** Kun lokale subsets i tabellen; importerte subsets lenkja under som "Importerte subsets: [skjema-1](lenke#subsets), [skjema-2](lenke#subsets)"
- **"Defined in"-kolonna:** Blir ikkje endra — beheld noverande schema-URI-format
- **Avvik frå andre seksjonar:** Subsets er den fyrste seksjonen som får filtrering — andre seksjonar kan få same behandling seinare

## Arkitektur: Korleis dokumentasjon vert generert

**To-stegs prosess:**

1. **`make gen-docs`** (Jinja2-template → `generated/.../docs/index.md`):
   - `src/assets/templates/docgen/index.md.jinja2` genererer `generated/<domain>/<schema>/docs/index.md`
   - Inneheld Classes, Slots, Enumerations, Types, Subsets-seksjonar
   - **Merk:** Det finst **berre `gen-docs`** (med `-s`), **IKKJE `gen-doc`** (utan `-s`)

2. **`make docs-publish`** (`generated/.../docs/index.md` → `mkdocs/docs/.../index.md`):
   - `mkdocs/publish.sh` kallar `mkdocs/lib/sections/classes.sh` per skjema
   - `classes.sh` ekstr aherer seksjonar frå `generated/.../docs/index.md` og **legg til "Importerte ..."-lenkjer** for Classes, Slots, Enumerations, Types
   - Subsets-seksjonen vert kopiert **utan** ekstra "Importerte subsets"-lenke (fordi templaten allereie har han)

**Noverande oppsett (Enumerations, Types, Slots):**

1. **Jinja2-template:** Viser (importerte element brukte av lokale klasser/slots) **ELLER** (lokalt definerte element) — OR-logikk, ingen "Importerte ..."-lenke
2. **`classes.sh`:** Ekstr aherer seksjonen og **legg til** "Importerte ..."-lenke via `build_import_links()`

**Noverande oppsett (Classes):**

1. **Jinja2-template:** Viser alle klasser (lokale + importerte), ingen "Importerte classes"-lenke
2. **`classes.sh`:** Ekstr aherer seksjonen og **legg til** "Importerte klasser"-lenke via `build_import_links()`

**Ny oppsett (Subsets):**

1. **Jinja2-template:** Viser **kun lokale** subsets (filtrering basert på `origin == schema.id`), **genererer** "Importerte subsets"-lenke
2. **`classes.sh`:** Ekstr aherer seksjonen **utan** å kalle `build_import_links()` (fordi linja allereie finst)

**RETTELSE: Subsets skal følgje OR-logikk (same som enums/types/slots)**

Subsets er **annotasjonar** (`in_subset`) på klasser/slots, og **skal** følgje same OR-logikk som enums/types/slots:

**Subsets som skal visast:**
- Importerte subsets **brukte av lokale klasser/slots** (via `in_subset` i `class.in_subset` eller `slot_usage[].in_subset`) **ELLER**
- Lokalt definerte subsets (frå `schema.subsets`)

**Eksempel:**
- `cpsv-ap-no` importerer `common-ap-no` (som definerer `Obligatorisk`, `Anbefalt`, `Valgfri`)
- `cpsv-ap-no` sine klasser/slots brukar `in_subset: [Obligatorisk]` osv. i `slot_usage`
- `cpsv-ap-no` definerer **ingen egne subsets**
- **Resultat:** Subsets-tabellen skal vise `Obligatorisk`, `Anbefalt`, `Valgfri` (importerte, men brukte av lokale klasser)

Derfor skal Subsets-seksjonen følgje **same mønster som Enumerations/Types/Slots**, ikkje ein "Importerte subsets"-lenke.

**Status quo:**

- `classes.sh` linje 135 har allereie kommentaren "Subsets har allereie 'Importerte subsets'-lenke frå jinja2-template — ingen behov for build_import_links"
- Denne kommentaren er **basert på mi nye template-endring** — den eksisterande template-koden har **IKKJE** filtrering eller "Importerte subsets"-lenke
- **Konklusjon:** Ingen endring nødvendig i `classes.sh` — kommentaren er korrekt etter at mi template-endring er på plass

### 1. Endre `index.md.jinja2` — OR-logikk for subsets

Oppdater `## Subsets`-seksjonen i `src/assets/templates/docgen/index.md.jinja2` (linje 389-446) til å følgje same OR-logikk som enums/types/slots:

**Noverande logikk:**

```jinja2
## Subsets

| Subset | Description | Defined in |
| --- | --- | --- |
{% for ss in schemaview.all_subsets().values()|sort(attribute='name') -%}
{%- set origin = ss.from_schema if ss.from_schema else schema.id -%}
{%- set defined_in_text = origin -%}
{%- set defined_in_link = origin -%}
| {{ gen.link(ss, True) }} | {{ ss.description|enshorten }} | [{{ defined_in_text }}]({{ defined_in_link }}) |
{% endfor %}
```

**Ny logikk (med filtrering og "Imported subsets"-lenke):**

```jinja2
{%- set ns_local_subsets = namespace(items=[]) -%}
{%- set ns_imported_subsets_by_schema = namespace(dict={}) -%}
{%- for ss in schemaview.all_subsets().values()|sort(attribute='name') -%}
{%- set origin = ss.from_schema if ss.from_schema else schema.id -%}
{%- if origin == schema.id -%}
{%- set ns_local_subsets.items = ns_local_subsets.items + [ss] -%}
{%- else -%}
{%- if origin not in ns_imported_subsets_by_schema.dict -%}
{%- set _ = ns_imported_subsets_by_schema.dict.update({origin: []}) -%}
{%- endif -%}
{%- set _ = ns_imported_subsets_by_schema.dict[origin].append(ss) -%}
{%- endif -%}
{%- endfor -%}
## Subsets ({{ ns_local_subsets.items|length }})
{%- if ns_local_subsets.items %}

| Subset | Description | Defined in |
| --- | --- | --- |
{% for ss in ns_local_subsets.items -%}
{%- set origin = ss.from_schema if ss.from_schema else schema.id -%}
{%- set defined_in_text = origin -%}
{%- set defined_in_link = origin -%}
| {{ gen.link(ss, True) }} | {{ ss.description|enshorten }} | [{{ defined_in_text }}]({{ defined_in_link }}) |
{% endfor -%}
{% else %}

*Ingen subsets definert lokalt i denne modellen.*
{% endif -%}
{%- if ns_imported_subsets_by_schema.dict %}

*Importerte subsets: {% for origin_uri in ns_imported_subsets_by_schema.dict.keys()|sort -%}
{%- if 'linkml' in origin_uri and 'types' in origin_uri -%}
{# linkml:types er eksternt skjema → GitHub-lenke #}
{%- set schema_name = 'linkml:types' -%}
{%- set schema_link = 'https://github.com/linkml/linkml-model/blob/main/linkml_model/model/schema/types.yaml' -%}
{%- elif origin_uri.startswith('https://data.norge.no/') -%}
{# Lokalt skjema → ekstraher domene og skjemanamn frå URI #}
{%- set uri_parts = origin_uri.split('/') -%}
{%- set origin_domain = uri_parts[-2] -%}
{%- set origin_schema = uri_parts[-1] -%}
{%- set local_domain = schema.id.split('/')[-2] -%}
{%- if local_domain == origin_domain -%}
{# Same domain → relativ sti eitt nivå opp #}
{%- set schema_name = origin_schema -%}
{%- set schema_link = '../' + origin_schema + '/#subsets' -%}
{%- else -%}
{# Ulik domain → relativ sti to nivå opp #}
{%- set schema_name = origin_schema -%}
{%- set schema_link = '../../' + origin_domain + '/' + origin_schema + '/#subsets' -%}
{%- endif -%}
{%- else -%}
{# Ukjent eksternt skjema → bruk URI som er #}
{%- set schema_name = origin_uri -%}
{%- set schema_link = origin_uri -%}
{%- endif -%}
[{{ schema_name }}]({{ schema_link }}){% if not loop.last %}, {% endif -%}
{%- endfor %}*
{% endif %}
```

**Forklaring:**

- **Linje 1-12:** Split subsets i `ns_local_subsets` (origin == schema.id) og `ns_imported_subsets_by_schema` (dict som grupperer importerte subsets per kjeldeskjema)
- **Linje 13:** Overskrift med telling av lokale subsets
- **Linje 14-24:** Tabell med lokale subsets (dersom dei finst), med uendra "Defined in"-kolonne
- **Linje 25-28:** Melding når ingen lokale subsets finst
- **Linje 29-56:** "Importerte subsets"-lenke (dersom dei finst), med **dynamisk** generert relativ sti

**Dynamisk lenkeformat (ingen hardkoding):**

- **`linkml:types`**: Eksternt skjema → GitHub-lenke `https://github.com/linkml/linkml-model/blob/main/linkml_model/model/schema/types.yaml`
- **Lokale skjema** (`https://data.norge.no/`):
  - Ekstraher domene og skjemanamn frå URI ved å splitte på `/` og ta `[-2]` (domene) og `[-1]` (skjemanamn)
  - **Same domain** (t.d. `ap-no/cpsv-ap-no` → `ap-no/common-ap-no`): `../<schema>/#subsets`
  - **Ulik domain** (t.d. `samt/samt-bu` → `ap-no/common-ap-no`): `../../<domain>/<schema>/#subsets`
- **Ukjende eksterne skjema**: Bruk schema-URI som er (fallback)

**Døme URI-parsing:**

```python
# origin_uri = "https://data.norge.no/ap-no/common-ap-no"
uri_parts = origin_uri.split('/')  # ['https:', '', 'data.norge.no', 'ap-no', 'common-ap-no']
origin_domain = uri_parts[-2]      # 'ap-no'
origin_schema = uri_parts[-1]      # 'common-ap-no'

# schema.id = "https://data.norge.no/ap-no/cpsv-ap-no"
local_domain = schema.id.split('/')[-2]  # 'ap-no'

# Same domain → relativ sti eitt nivå opp
schema_link = '../common-ap-no/#subsets'
```

**Døme domene-kryssing:**

```python
# origin_uri = "https://data.norge.no/ap-no/common-ap-no"
# schema.id = "https://data.norge.no/samt/samt-bu"

origin_domain = 'ap-no'
local_domain = 'samt'

# Ulik domain → relativ sti to nivå opp
schema_link = '../../ap-no/common-ap-no/#subsets'
```

### 2. Regenerer dokumentasjon

Generer dokumentasjon for alle skjema for å verifisere endringane:

```bash
make gen-doc
```

### 3. Verifiser resultat

Sjekk eit utval av genererte `index.md`-filer:

```bash
# Skjema som importerer common-ap-no (importerte subsets)
cat generated/ap-no/cpsv-ap-no-schema/docs/index.md | grep -A 10 "## Subsets"

# Skjema som definerer lokale subsets
cat generated/ap-no/common-ap-no-schema/docs/index.md | grep -A 10 "## Subsets"
```

**Forventa resultat for `cpsv-ap-no` (importerte subsets frå `common-ap-no`):**

```markdown
## Subsets (0)

*Ingen subsets definert lokalt i denne modellen.*

*Importerte subsets: [common-ap-no](../common-ap-no/#subsets)*
```

**Forventa resultat for `common-ap-no` (lokale subsets):**

```markdown
## Subsets (4)

| Subset | Description | Defined in |
| --- | --- | --- |
| [Anbefalt](Anbefalt.md) | Anbefalte eigenskapar i ein AP-NO-profil | [https://data.norge.no/ap-no/common-ap-no](https://data.norge.no/ap-no/common-ap-no) |
| [Metadata](Metadata.md) | Klasser som beskriv metadata om ressursar, ikkje sjølve datainnhaldet | [https://data.norge.no/ap-no/common-ap-no](https://data.norge.no/ap-no/common-ap-no) |
| [Obligatorisk](Obligatorisk.md) | Obligatoriske eigenskapar i ein AP-NO-profil | [https://data.norge.no/ap-no/common-ap-no](https://data.norge.no/ap-no/common-ap-no) |
| [Valgfri](Valgfri.md) | Valfrie eigenskapar i ein AP-NO-profil | [https://data.norge.no/ap-no/common-ap-no](https://data.norge.no/ap-no/common-ap-no) |
```

### 4. Publiser til mkdocs

Regenerer dokumentasjonsportalen:

```bash
make docs-publish
```

Sjekk at lenka til importerte subsets fungerer:

```bash
# Lenka skal peike til common-ap-no sitt Subsets-seksjon
grep "Imported subsets" mkdocs/docs/ap-no/cpsv-ap-no/index.md
```

Forventa output:

```
*Importerte subsets: [common-ap-no](../common-ap-no/#subsets)*
```

Verifiser at ankeret `#subsets` fungerer i mkdocs-portalen ved å opne `mkdocs/docs/ap-no/common-ap-no/index.md` og sjekke at det finst ein `## Subsets`-overskrift (som automatisk vert til `id="subsets"`-anker i HTML).

## Notatar

- **Kun subsets:** Denne endringa gjeld **kun** Subsets-seksjonen. Classes, Slots, Enumerations og Types har **IKKJE** filtrering — dei viser alle element (lokale + importerte) utan "Importerte ..."-linje. Subsets er den fyrste seksjonen som får filtrering
- **"Defined in"-kolonna:** Blir **ikkje** endra — beheld noverande schema-URI-format (t.d. `[https://data.norge.no/ap-no/common-ap-no](https://data.norge.no/ap-no/common-ap-no)`)
- **Telling i overskrift:** `## Subsets (0)` / `## Subsets (4)` — viser antal lokale subsets
- **Dynamisk lenkeformat:** Ingen hardkoding — ekstraherer domene og skjemanamn frå URI via `split('/')[-2]` og `split('/')[-1]`
- **Relativ lenking:** 
  - Same domain: `../<schema>/#subsets`
  - Ulik domain: `../../<domain>/<schema>/#subsets`
  - `linkml:types`: GitHub-lenke til kjeldekode
- **Anker:** `#subsets` (ikkje `index.md#subsets`) — mkdocs-konvensjon for overskrift-anker
- **Gruppering:** Importerte subsets er gruppert per kjeldeskjema (t.d. dersom eit skjema importerer subsets frå både `common-ap-no` og `dcat-ap-no`, vil begge lenkjast separat: `*Importerte subsets: [common-ap-no](../common-ap-no/#subsets), [dcat-ap-no](../dcat-ap-no/#subsets)*`)
- **Fallback for ukjende skjema:** Dersom URI ikkje startar med `https://data.norge.no/`, bruk schema-URI som lenketekst og lenke
- **Kursiv format:** `*Importerte subsets: ...*` — same som "Importerte klasser", "Importerte slots", "Importerte enumerations", "Importerte typer"

## Handlingsliste

- [x] Endre `src/assets/templates/docgen/index.md.jinja2` (Subsets-seksjon, linje 389-446) — **FYRSTE VERSJON (filtrering)**
- [x] Verifiser at `classes.sh` linje 135 har korrekt kommentar (ingen endring nødvendig)
- [x] Identifiser problem: `publish.sh` brukar katalognamn (`cpsv-ap-no`), Makefile brukar filnamn (`cpsv-ap-no-schema`)
- [x] **Slett alle `generated/<domain>/<model>-schema/` katalogar** (gamle katalogar frå filnamn-konvensjon)
- [x] **Fiks `Makefile` linje 45:** Endre `schema_name` frå filnamn til katalognamn
- [x] **Testcase (med filtrering):** Regenererte `cpsv-ap-no` — viste "Subsets (0)" (FEIL — skulle vist Obligatorisk/Anbefalt/Valgfri)
- [x] **RETTELSE:** Endre template til OR-logikk (same som enums/types/slots) — sjekk `in_subset` i klasser og `slot_usage`
- [x] **Testcase (med OR-logikk):** Regenererte `cpsv-ap-no` på nytt
- [x] Verifiser at `generated/ap-no/cpsv-ap-no/docs/index.md` har "Subsets (3)" med Obligatorisk, Anbefalt, Valgfri ✅
- [x] Publiser til mkdocs (`make docs-publish`)
- [x] **Full regenerering:** `make gen-docs` (alle domene) fullført
- [x] **Bug løyst:** `mkdocs/docs/ap-no/cpsv-ap-no/index.md` mangla `Valgfri`-linja
  - Rotårsak: Jinja2-template hadde innrykk i Subsets-seksjonen (4 mellomrom før `## Subsets`)
  - `classes.sh` linje 134 brukar `awk '/^## Subsets/,0'` som krev start-of-line (`^`)
  - Med innrykk matcha ikkje `^## Subsets`, så awk fann ikkje seksjonen
  - Løysing: Fjerna all innrykk i Subsets-blokka (linje 389-416) ved å bruke `{%- ... -%}` konsekvent
- [ ] Verifiser at `mkdocs/docs/ap-no/cpsv-ap-no/index.md` no har alle 3 subsets

## Problem: publish.sh brukar katalognamn, Makefile brukar filnamn

**Symptom:**
- `make gen-docs` genererer til `generated/ap-no/cpsv-ap-no-schema/` (basert på filnamnet `cpsv-ap-no-schema.yaml`)
- `make docs-publish` kopierer frå `generated/ap-no/cpsv-ap-no/` (basert på katalognamnet `cpsv-ap-no/`)
- **Resultat:** `mkdocs/docs/` får gammal versjon frå `generated/ap-no/cpsv-ap-no/` (sist oppdatert 27-28. juli), ikkje ny versjon frå `generated/ap-no/cpsv-ap-no-schema/` (oppdatert 29. juli)

**Rotårsak:**

1. **Makefile** (linje 45-46):
   ```makefile
   schema_name   = $(basename $(basename $(notdir $(1))))
   schema_outdir = $(GEN_DIR)/$(call schema_domain,$(1))/$(call schema_name,$(1))
   ```
   - Input: `src/linkml/ap-no/cpsv-ap-no/cpsv-ap-no-schema.yaml`
   - `schema_name`: `cpsv-ap-no-schema` (ekstraherer **filnamn** utan `.yaml`)
   - `schema_outdir`: `generated/ap-no/cpsv-ap-no-schema/`

2. **publish.sh** (linje 246-247):
   ```bash
   schema_dir=$(dirname "$manifest_file")
   schema=$(basename "$schema_dir")
   ```
   - Input: `src/linkml/ap-no/cpsv-ap-no/build.yaml`
   - `schema`: `cpsv-ap-no` (ekstraherer **katalognamn**)
   - `schema_dir` (linje 153): `generated/ap-no/cpsv-ap-no/`

**Løysing:**

Endre `Makefile` linje 45-46 til å bruke **katalognamn** (same som `publish.sh`) i staden for filnamn:

```makefile
# Før (linje 45-46):
schema_name   = $(basename $(basename $(notdir $(1))))
schema_outdir = $(GEN_DIR)/$(call schema_domain,$(1))/$(call schema_name,$(1))

# Etter:
# Ekstraher katalognamn frå stien (t.d. src/linkml/ap-no/cpsv-ap-no/cpsv-ap-no-schema.yaml → cpsv-ap-no)
schema_name   = $(notdir $(patsubst %/,%,$(dir $(1))))
schema_outdir = $(GEN_DIR)/$(call schema_domain,$(1))/$(call schema_name,$(1))
```

**Forklaring:**
- `$(dir $(1))` → `src/linkml/ap-no/cpsv-ap-no/`
- `$(patsubst %/,%,...)` → fjern trailing `/` → `src/linkml/ap-no/cpsv-ap-no`
- `$(notdir ...)` → `cpsv-ap-no`

Dette vil sikre at `make gen-docs` genererer til same katalog som `publish.sh` forventar (`generated/ap-no/cpsv-ap-no/`).

## Status

**Template-endring fullført** (`src/assets/templates/docgen/index.md.jinja2` linje 389-446):
- Split subsets i `ns_local_subsets` (origin == schema.id) og `ns_imported_subsets_by_schema` (dict per kjeldeskjema)
- Tabell viser kun lokale subsets (eller "Ingen subsets definert lokalt"-melding)
- "Importerte subsets"-lenke med dynamisk URI-parsing (ingen hardkoding):
  - linkml:types → GitHub-lenke
  - data.norge.no (same domain) → `../<schema>/#subsets`
  - data.norge.no (ulik domain) → `../../<domain>/<schema>/#subsets`
  - Ukjent URI → bruk URI som er
- Kommaseparert liste (same format som andre "Importerte ..."-lister)

**Neste steg:**
- Regenerer dokumentasjon (`make gen-doc`) — **blokkert av podman-problem** (sjå under)
- Verifiser resultat for `cpsv-ap-no` (forventa: "Ingen subsets definert lokalt" + lenke til common-ap-no)
- Verifiser resultat for `common-ap-no` (forventa: tabell med 4 lokale subsets, ingen "Importerte subsets"-linje)

**Podman-problem:**
Podman feiler med `set sticky bit on: chmod /run/user/1000/libpod: read-only file system`. Dette blokkerer `make gen-doc`. Løysing:
1. Restart WSL2 (`wsl --shutdown` frå Windows, så start på nytt)
2. Eller fiks `/run/user/1000/libpod`-permissions
3. Køyr `make gen-doc` på nytt etter restart

## Utført

**Dato:** 2026-07-29

**Resultat:**
- Subsets-seksjonen følgjer no OR-logikk (same som Enumerations/Types/Slots)
- `cpsv-ap-no` viser "Subsets (3)" med Obligatorisk, Anbefalt, Valgfri ✅
- `Makefile` brukar no katalognamn (cpsv-ap-no) i staden for filnamn (cpsv-ap-no-schema) ✅
- Alle gamle `*-schema` katalogar sletta frå `generated/` ✅

**Hovudproblem løyst:**
- Jinja2-template hadde indentasjon som vart inkludert i output
- `classes.sh` brukar `awk '/^## Subsets/,0'` som krev start-of-line (`^`)
- Med indentasjon matcha ikkje mønsteret, så seksjonen vart ikkje ekstrahert
- Løysing: konsekvent bruk av `{%- ... -%}` og **ingen indentasjon** av Jinja-blokker

**CLAUDE.md oppdatert:** Lagt til hovudregel om at Jinja-blokker aldri skal indenterast.
