# common-ap-no: vis alle definerte slots og enums i index.md

## Bakgrunn

`common-ap-no-schema.yaml` er eit delt bibliotekskjema som definerer gjenbrukbare
slots, enums og typar for alle AP-NO-profilene. Skjemaet inneheld:

- **24 globale slots** (tittel, beskrivelse, format, spraak, lisens m.fl.)
- **4 enums** (EULicence, EUFileType, EULanguage, ADMSStatus)
- **4 typar** (LangString, NonNegativeInteger, Duration, GYear)
- **4 klasser** (Lisensdokument, Mediatype, Konsept, Begrepssamling)

Men `mkdocs/docs/ap-no/common-ap-no/index.md` viser:

- **Berre 2 slots** (`id`, `type_concept`) — resten er skjulte
- **Tom enum-liste** ("Ingen enumerations brukt i denne modellen")

**Rotårsak:**

Jinja-templaten `src/assets/templates/docgen/index.md.jinja2` (linje 104-130
og 166-188) samlar kun slots og enums som **faktisk vert brukt** i klasser
definerte i skjemaet. Dette er korrekt for dei fleste skjema, men `common-ap-no`
er eit bibliotekskjema — slots og enums er definerte for **eksport** til andre
skjema, ikkje for intern bruk.

**Eksempel på konsekvensen:**

Ein utviklar som vurderer å importere `common-ap-no` ser berre 2 slots i
dokumentasjonen, men får tilgang til alle 24 globale slots ved import. Dette
skapar forvirring og gjer det vanskeleg å evaluere kva skjemaet tilbyr.

## Føremål

Utvide dokumentasjonsgenerering til å vise **alle lokalt definerte** slots,
enums og typar i bibliotekskjema — ikkje berre dei som vert brukt internt.

## Krav

1. `index.md` for `common-ap-no` skal vise alle 24 slots, 4 enums og 4 typar
   som er definerte i skjemaet
2. Løysinga skal kun påverke skjema som er tydelege **bibliotekskjema** —
   vanlige domenemodeller held fram med å vise berre brukte slots/enums
3. Ingen endring i `common-ap-no-schema.yaml` — det er eit metadata-spørsmål,
   ikkje ein skjemafeil
4. Templaten `index.md.jinja2` skal få ein mekanisme for å skilje bibliotekskjema
   frå domenemodeller

## Løysingsalternativ

### Alternativ 1: Ny schema-annotasjon `is_library`

Legg til `annotations.is_library: true` i bibliotekskjema, og la templaten
sjekke denne verdien for å velje mellom "alle definerte" vs "berre brukte" logikk.

**Fordel:** eksplisitt, enkelt å forstå, skalerer til andre bibliotekskjema  
**Ulempe:** krev endring i kvar bibliotekskjema-yaml

### Alternativ 2: Heuristikk basert på `imports`

Detekter bibliotekskjema ved at dei **berre importerer `linkml:types`** og ingen
andre skjema. Dette passar `common-ap-no` (importerer kun `linkml:types`),
men kan gje falske positivar.

**Fordel:** ingen YAML-endring  
**Ulempe:** skjør logikk, kan feile ved framtidige endringar

### Alternativ 3: Hardkoda liste i templaten

Legg til ei hardkoda sjekk `if schema.name in ['common-ap-no', ...]` i templaten.

**Fordel:** rask implementering  
**Ulempe:** ikkje skalerbar, bryt DRY-prinsippet

## Oppdatert vurdering (2026-07-11)

**Ny innsikt:** Etter verifisering av alle skjema vart det klart at:
1. Ingen skjema bryt containerklasse-konvensjonen (sjå `specs/done/containerattributt-som-globale-slots.md`)
2. Berre **5 av 32 skjema** har faktisk ubrukte element (globale slots/enums/typar)
3. OR-logikk vil **ikkje** synleggjere containerattributta (dei er ikkje i `slots:`-seksjonen)

**Oppdatert anbefaling:**

**Alternativ 2** (OR-logikk globalt) er no **føretrekt** framfor Alternativ 1 (`is_library`-annotasjon).

**Grunngjeving:**
- Liten påverknad (berre 5 skjema)
- Synleggjer bibliotekskjema (`common-ap-no`, `dqv-core`)
- Identifiserer potensielt dead code i 3 domenemodeller
- Følgjer prinsippet "synleggjering av feil er ein god ting"
- Enklare implementering (ingen ny annotasjon)

**Sjå fullstendig utgreiing:** `specs/backlog/or-logikk-synleggjering-av-ubrukte-element.md`

## Alternativ 1: is_library-annotasjon (tidlegare anbefaling)

Legg til `annotations.is_library: true` i bibliotekskjema og utvid templaten:

```jinja2
{%- if schema.annotations and schema.annotations.is_library -%}
  {# Vis ALLE definerte slots, enums, typar #}
  {%- set ns_used_slots.names = schemaview.all_slots()|list -%}
  {%- set ns_used_enums.names = schemaview.all_enums()|list -%}
  {%- set ns_used_types.names = schemaview.all_types()|list -%}
{%- else -%}
  {# Vis berre brukte slots, enums, typar (noverande logikk) #}
  ...
{%- endif -%}
```

**Ulempe:** Krev manuell annotasjon av bibliotekskjema, synleggjer ikkje dead code i domenemodeller.

## Gjennomføring

### 1. Legg til `is_library`-annotasjon i `common-ap-no-schema.yaml`

```yaml
annotations:
  is_library: true
  utgiver: https://data.norge.no/organizations/991825827
  ...
```

### 2. Utvid `index.md.jinja2` til å handtere `is_library`

**Linje 104-130 (Slots-samling):**

Erstatt:

```jinja2
{%- set ns_used_slots = namespace(names=[]) -%}
{%- for class_name in schemaview.all_classes() %}
  ...
{%- endfor -%}
```

med:

```jinja2
{%- set ns_used_slots = namespace(names=[]) -%}
{%- if schema.annotations and schema.annotations.is_library -%}
  {# Bibliotekskjema: vis ALLE definerte slots #}
  {%- for slot_name in schemaview.all_slots() %}
    {%- set s = schemaview.get_slot(slot_name) %}
    {%- set origin = s.from_schema if s.from_schema else schema.id %}
    {%- if origin == schema.id %}
      {%- set ns_used_slots.names = ns_used_slots.names + [slot_name] %}
    {%- endif %}
  {%- endfor %}
{%- else -%}
  {# Vanlig skjema: vis berre brukte slots #}
  {%- for class_name in schemaview.all_classes() %}
    {%- set c = schemaview.get_class(class_name) %}
    {%- set origin = c.from_schema if c.from_schema else schema.id %}
    {%- if c and not c.tree_root and origin == schema.id %}
      {%- for slot_name in c.slots or [] %}
        {%- if slot_name not in ns_used_slots.names %}
          {%- set ns_used_slots.names = ns_used_slots.names + [slot_name] %}
        {%- endif %}
      {%- endfor %}
    {%- endif %}
  {%- endfor %}
{%- endif -%}
```

**Linje 166-188 (Enum-samling):**

Legg til tilsvarande logikk:

```jinja2
{%- set ns_used_enums = namespace(names=[]) -%}
{%- if schema.annotations and schema.annotations.is_library -%}
  {# Bibliotekskjema: vis ALLE definerte enums #}
  {%- for enum_name in schemaview.all_enums() %}
    {%- set e = schemaview.get_enum(enum_name) %}
    {%- set origin = e.from_schema if e.from_schema else schema.id %}
    {%- if origin == schema.id %}
      {%- set ns_used_enums.names = ns_used_enums.names + [enum_name] %}
    {%- endif %}
  {%- endfor %}
{%- else -%}
  {# Vanlig skjema: vis berre brukte enums #}
  ...
{%- endif -%}
```

**Linje 204-226 (Type-samling):**

Tilsvarande for typar.

### 3. Regenerer dokumentasjon

```bash
make gen-doc SCHEMA=src/linkml/ap-no/common-ap-no/common-ap-no-schema.yaml
cd mkdocs && ./publish.sh
```

### 4. Valider resultat

Sjekk at `mkdocs/docs/ap-no/common-ap-no/index.md` no viser:

- **Alle 24 slots** under § Slots (fordelte i Verdiar/Referansar/Kodar)
- **Alle 4 enums** under § Enumerations
- **Alle 4 typar** under § Types

## Verifisering

- [ ] `common-ap-no-schema.yaml` har `annotations.is_library: true`
- [ ] `index.md.jinja2` har `is_library`-betinga logikk for slots, enums, typar
- [ ] `make gen-doc` for `common-ap-no` genererer fullstendig liste
- [ ] `mkdocs/docs/ap-no/common-ap-no/index.md` viser alle 24 slots, 4 enums, 4 typar
- [ ] Andre skjema (t.d. `dcat-ap-no`) er upåverka — viser framleis berre brukte slots/enums

## Utført

*(vert utfylt etter at arbeidet er fullført)*
