# Omstrukturering av Types-tabell i gen-doc

## Bakgrunn

Den noverande Types-tabellen i gen-doc-output har denne strukturen:

| Type | LinkML-alias | Description | Defined in |
|------|--------------|-------------|------------|
| [xsd:string](http://www.w3.org/2001/XMLSchema#string) | `string` | A character string | https://w3id.org/linkml/types |

**Problem:**
- Første kolonne viser URI-en (som hovudverdi), mens type-namnet (`string`) berre står som alias
- "Defined in"-kolonna viser ein lang URI utan lenke til linkml:types

## Krav

Endre Types-tabellen til denne strukturen:

| Type | URI | Description | Defined in |
|------|-----|-------------|------------|
| string | [xsd:string](https://www.w3.org/TR/xmlschema11-2/#string) | A character string | [linkml:types](https://github.com/linkml/linkml-model/blob/main/linkml_model/model/schema/types.yaml) |
| anyURI | [xsd:anyURI](https://www.w3.org/TR/xmlschema11-2/#anyURI) | a URI or a CURIE | [linkml:types](https://github.com/linkml/linkml-model/blob/main/linkml_model/model/schema/types.yaml) |

**Endringar:**
1. **Type-kolonna** (første): Vis type-namnet (t.d. `string`, `uriorcurie`) utan lenke
2. **URI-kolonna** (ny, andre): Vis XSD-namnet (t.d. `xsd:string`) med lenke til W3C XML Schema spesifikasjonen (ikkje til URI-en direkte)
3. **LinkML-alias-kolonna**: **Fjerna** (redundant med Type-kolonna)
4. **Description-kolonna** (tredje): Beheld som før
5. **Defined in-kolonna** (fjerde): Lenke til linkml:types på GitHub når verdien er `https://w3id.org/linkml/types` eller `linkml:types`

**Lenkjelogikk for URI-kolonna:**
- Dersom URI-en startar med `http://www.w3.org/2001/XMLSchema#`, bygg lenke til W3C-dokumentasjonen:
  - Parse lokalnamnet (t.d. `string` frå `http://www.w3.org/2001/XMLSchema#string`)
  - Bygg lenke: `https://www.w3.org/TR/xmlschema11-2/#<lokalnamn>`
- Elles: bruk URI-en direkte som lenke

## Løysing

### 1. Finn Jinja-templaten for Types-tabellen

Jinja-templaten ligg i `src/assets/templates/docgen/` og heiter truleg `index.md.jinja2` eller `class.md.jinja2`.

Søk etter:
- `## Types` (seksjonsoverskrift)
- Tabelloverskrifter: `| Type |` eller `t.uri` (Jinja-variabel)

### 2. Endre tabelloverskrift

**Før:**
```jinja
| Type | LinkML-alias | Description | Defined in |
```

**Etter:**
```jinja
| Type | URI | Description | Defined in |
```

### 3. Endre tabellrad-logikk

**Før (antek):**
```jinja
| [{{ t.name }}]({{ t.uri }}) | `{{ t.alias }}` | {{ t.description }} | {{ t.from_schema }} |
```

**Etter:**
```jinja
{# URI-lenke logikk #}
{% set uri_text = t.name %}
{% set uri_link = t.uri %}
{% if t.uri and t.uri.startswith('http://www.w3.org/2001/XMLSchema#') %}
  {# XSD-type: lenk til W3C-dokumentasjon i staden for URI direkte #}
  {% set local_name = t.uri.split('#')[1] %}
  {% set uri_text = 'xsd:' + local_name %}
  {% set uri_link = 'https://www.w3.org/TR/xmlschema11-2/#' + local_name %}
{% elif t.uri %}
  {# Anna URI: bruk prefiksert form eller full URI #}
  {% set uri_text = 'xsd:' + t.name %}  {# Antek xsd-prefix som fallback #}
{% endif %}

{# Defined in-lenke logikk #}
{% set defined_in_text = t.from_schema %}
{% set defined_in_link = t.from_schema %}
{% if 'linkml/types' in t.from_schema or t.from_schema == 'https://w3id.org/linkml/types' %}
  {% set defined_in_text = 'linkml:types' %}
  {% set defined_in_link = 'https://github.com/linkml/linkml-model/blob/main/linkml_model/model/schema/types.yaml' %}
{% endif %}

| {{ t.name }} | [{{ uri_text }}]({{ uri_link }}) | {{ t.description }} | [{{ defined_in_text }}]({{ defined_in_link }}) |
```

**Forklaring:**
- `{{ t.name }}` i Type-kolonna (utan lenke)
- `[xsd:lokalnamn](https://www.w3.org/TR/xmlschema11-2/#lokalnamn)` i URI-kolonna for XSD-typar
- LinkML-alias-kolonna fjerna
- Logikk for å sjekke om URI er XSD og bygg W3C-dokumentasjonslenke
- Logikk for å sjekke om `from_schema` er linkml:types og sette riktig lenke

### 4. Handter lokale typar

Dersom ein type er definert lokalt (i same skjema), skal "Defined in"-kolonna vise skjema-URI-en (ikkje linkml:types-lenke).

### 5. Test

Generer dokumentasjon og verifiser:
- `make gen-doc SCHEMA=src/linkml/samt/samt-bu/samt-bu-schema.yaml`
- Sjå på `generated/samt/samt-bu/docs/index.md` — Types-tabellen skal ha fem kolonner
- Verifiser at linkml:types-typar (`string`, `uriorcurie`) har GitHub-lenke i "Defined in"
- Verifiser at lokale typar (dersom dei finst) ikkje får linkml:types-lenke

## Utført

### 1. Finn Jinja-templaten

Fann `src/assets/templates/docgen/index.md.jinja2`, Types-seksjonen på linje 203-240.

### 2. Endre tabelloverskrift og kolonner

Endra frå:
```jinja
| Type | LinkML-alias | Description | Defined in |
```

Til:
```jinja
| Type | URI | Description | Defined in |
```

### 3. Implementer URI-lenkelogikk

**Oppdagelse:** LinkML brukar CURIE-form (`xsd:string`) i `t.uri`, ikkje full URI (`http://www.w3.org/2001/XMLSchema#string`).

**Implementert logikk:**
```jinja
{%- if t.uri and t.uri.startswith('xsd:') %}
  {# XSD-type (CURIE-form): lenk til W3C-dokumentasjon #}
  {%- set local_name = t.uri[4:] %}  {# Skip 'xsd:' prefix #}
  {%- set uri_text = t.uri %}
  {%- set uri_link = 'https://www.w3.org/TR/xmlschema11-2/#' + local_name %}
{%- elif t.uri %}
  {# Anna URI: bruk direkte #}
  {%- set uri_text = t.uri %}
  {%- set uri_link = t.uri %}
{%- else %}
  {# Ingen URI #}
  {%- set uri_text = type_name %}
  {%- set uri_link = '#' %}
{%- endif %}
```

### 4. Implementer Defined in-lenkelogikk

```jinja
{%- set defined_in_text = origin %}
{%- set defined_in_link = origin %}
{%- if 'linkml/types' in origin or origin == 'https://w3id.org/linkml/types' %}
  {%- set defined_in_text = 'linkml:types' %}
  {%- set defined_in_link = 'https://github.com/linkml/linkml-model/blob/main/linkml_model/model/schema/types.yaml' %}
{%- endif %}
```

### 5. Fjern LinkML-alias-kolonna

Endra tabellrad frå:
```jinja
| {{ gen.link(t, True) }} | `{{ type_name }}` | {{ t.description|enshorten }} | {{ origin }} |
```

Til:
```jinja
| {{ type_name }} | [{{ uri_text }}]({{ uri_link }}) | {{ t.description|enshorten }} | [{{ defined_in_text }}]({{ defined_in_link }}) |
```

## Verifisering

```bash
make gen-doc SCHEMA=src/linkml/samt/samt-bu/samt-bu-schema.yaml
grep -A10 "^## Types$" generated/samt/samt-bu/docs/index.md

# Forventa output:
# ## Types
# 
# | Type | URI | Description | Defined in |
# | --- | --- | --- | --- |
# | string | [xsd:string](https://www.w3.org/TR/xmlschema11-2/#string) | A character string | [linkml:types](https://github.com/linkml/linkml-model/blob/main/linkml_model/model/schema/types.yaml) |
# | uriorcurie | [xsd:anyURI](https://www.w3.org/TR/xmlschema11-2/#anyURI) | a URI or a CURIE | [linkml:types](https://github.com/linkml/linkml-model/blob/main/linkml_model/model/schema/types.yaml) |

make docs-publish
# Verifiser at mkdocs/docs/samt/samt-bu/index.md har same struktur

# Verifiser at lenkjene fungerer:
# - Click på xsd:string → skal opne https://www.w3.org/TR/xmlschema11-2/#string
# - Click på linkml:types → skal opne https://github.com/linkml/linkml-model/blob/main/linkml_model/model/schema/types.yaml
```

## Merk

- LinkML-alias-kolonna er **fjerna** fordi ho er redundant med Type-kolonna (begge viste same verdi for standard-typar).
- Dersom ein lokal type ikkje har ein URI, skal URI-kolonna vise ein tom celle eller ein placeholder (t.d. `—`).
- URI-lenkjelogikken er **generisk** og basert på prefix-deteksjon:
  - `http://www.w3.org/2001/XMLSchema#*` → `https://www.w3.org/TR/xmlschema11-2/#*`
  - Andre URI-ar: bruk URI direkte som lenke
- Lokalnamn ekstraheras frå URI ved å splitte på `#` (t.d. `http://www.w3.org/2001/XMLSchema#string` → `string`)
