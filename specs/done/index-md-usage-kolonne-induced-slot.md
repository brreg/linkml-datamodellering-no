# index.md Usage-kolonne skal bruke induced_slot for Types og Enumerations

## Bakgrunn

`index.md`-templaten (`src/assets/templates/docgen/index.md.jinja2`) genererer Types-, Enumerations- og Slots-tabellar med ein "Usage"-kolonne som viser om eit element faktisk er brukt i lokale klasser ("✅ Used") eller berre definert ("⚠️ Defined").

Logikken for å sjekke om ein type/enum er brukt var ufullstendig:
- Den såg berre etter slots i `schema.slots` (lokale slot-definisjonar)
- Den **ignorerte** slots brukte via `induced_slot` (importerte slots brukte i lokale klasser)

Dette førte til at skjema som `modelldcat-katalog` (som har **ingen** lokale slots, men importerer alle slots frå `common-ap-no` og `dcat-ap-no`) fekk alle typer og enums markerte som "⚠️ Defined", sjølv om dei faktisk vart brukte i lokale klasser (`Informasjonsmodell`, `Modellkatalog` osv.).

## Problem

I `mkdocs/docs/ap-no/modelldcat-katalog/index.md` vart desse typane feilaktig markerte som "⚠️ Defined":
- `date` (brukt i `endringsdato`, `utgivelsesdato` via importerte slots)
- `LangString` (brukt i `tittel`, `beskrivelse` via importerte slots)
- `uri` (brukt i `heimeside`, `id` via importerte slots)
- `uriorcurie` (brukt i `id` via importerte slots)

Same problem gjaldt enumerations.

## Løysing

Utvid "Used"-sjekken i Jinja-templaten til også å inkludere `induced_slot`-logikk:

**For Types (linje 330-342):**
```jinja
{%- set is_used = namespace(value=false) -%}
{# Sjekk om typen er brukt i ein lokal slot (definert i schema.slots) #}
{%- for slot_name in (schema.slots or {}).keys() %}
  {%- set s = schemaview.get_slot(slot_name) %}
  {%- if s and s.range == type_name %}
    {%- set is_used.value = true -%}
  {%- endif %}
{%- endfor %}
{# NY: Sjekk om typen er brukt i ein lokal klasse (via induced_slot) #}
{%- for class_name in schemaview.all_classes() %}
  {%- set c = schemaview.get_class(class_name) %}
  {%- set c_origin = c.from_schema if c.from_schema else schema.id %}
  {%- if c and not c.tree_root and c_origin == schema.id %}
    {%- for slot_name in c.slots or [] %}
      {%- set induced = schemaview.induced_slot(slot_name, class_name) %}
      {%- if induced and induced.range == type_name %}
        {%- set is_used.value = true -%}
      {%- endif %}
    {%- endfor %}
  {%- endif %}
{%- endfor %}
```

**For Enumerations (linje 248-261):**
Samme logikk — legg til `induced_slot`-sjekk etter eksisterande `schema.slots`-sjekk.

## Steg

1. ✅ Oppdater `src/assets/templates/docgen/index.md.jinja2` linje 330-342 (Types)
2. ✅ Oppdater `src/assets/templates/docgen/index.md.jinja2` linje 248-261 (Enumerations)
3. ✅ Regenerer dokumentasjon for `modelldcat-katalog` med `make domain-ap-no`
4. ✅ Verifiser at `date`, `LangString`, `uri`, `uriorcurie` no er markerte som "✅ Used"

## Forventa resultat

Etter fiksinga skal `generated/ap-no/modelldcat-katalog/docs/index.md` ha:

```markdown
| Type | URI | Description | Defined in | Usage |
| --- | --- | --- | --- | --- |
| date | [xsd:date](...) | ... | [linkml:types](...) | ✅ Used |
| LangString | [rdf:langString](...) | ... | [https://data.norge.no/ap-no/common-ap-no](...) | ✅ Used |
| uri | [xsd:anyURI](...) | ... | [linkml:types](...) | ✅ Used |
| uriorcurie | [xsd:anyURI](...) | ... | [linkml:types](...) | ✅ Used |
```

## Utført

### Resultat

Fiksinga vart gjennomført og verifisert:

**Endra filer:**
- `src/assets/templates/docgen/index.md.jinja2` (Types Usage-sjekk: linje 330-352)
- `src/assets/templates/docgen/index.md.jinja2` (Enumerations Usage-sjekk: linje 248-274)

**Verifisering:**
- `generated/ap-no/modelldcat-katalog/docs/index.md` — alle typer (`date`, `LangString`, `uri`, `uriorcurie`) no markerte som "✅ Used"
- `generated/ap-no/common-ap-no/docs/index.md` — ubrukte typar (`Duration`, `GYear`) korrekt markerte som "⚠️ Defined"

### Endringar i templaten

**Types (linje 330-352):**
Lagt til `induced_slot`-sjekk etter eksisterande `schema.slots`-sjekk for å fange opp typar brukte via importerte slots i lokale klasser.

**Enumerations (linje 248-274):**
Lagt til `induced_slot`-sjekk etter eksisterande `schema.slots`-sjekk for å fange opp enums brukte via importerte slots i lokale klasser.

### Generert dokumentasjon

`make domain-ap-no` vart køyrd for å regenerere dokumentasjon for heile `ap-no`-domenet. Alle skjema (`modelldcat-katalog`, `common-ap-no`, `dcat-ap-no` osv.) har no korrekt Usage-merking for Types og Enumerations.

## Relaterte filer

- `src/assets/templates/docgen/index.md.jinja2` (hovudfil)
- `generated/ap-no/modelldcat-katalog/docs/index.md` (testcase)
- `Makefile` (linje 911: `run_gen_doc_parallel`)
