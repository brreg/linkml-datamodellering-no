# OR-logikk i index.md.jinja2: Synleggjering av ubrukte element

## Bakgrunn

Noverande logikk i `src/assets/templates/docgen/index.md.jinja2`:
- **Viser berre** slots, enums og typar som vert **brukt** i lokale klasser

Alternativ logikk (OR-logikk):
- **Viser** slots, enums og typar som vert **brukt ELLER er lokalt definerte**

## Prinsipp: Synleggjering av feil

**Grunngjeving:** Dersom eit skjema har definert slots, enums eller typar i
`slots:`, `enums:` eller `types:`-seksjonane som **aldri** vert brukt i nokon
lokal klasse, kan dette indikere:

1. **Dead code** — element som vart definerte men aldri teke i bruk
2. **Eksportslots** — legitimt definerte element for bruk i importerande skjema
   (t.d. `common-ap-no`)
3. **Framtidig bruk** — planlagde element som ikkje er implementerte enno

Ved å **synleggjere** desse i dokumentasjonen kan bidragsytarar:
- Identifisere og rydde opp i dead code
- Forstå kva eit bibliotekskjema tilbyr for import
- Sjå kva element som er tilgjengelege men ikkje obligatoriske

## Faktisk situasjon i repoet

Ny analyse med presis YAML-parsing (ekskluderer containerattributta):

### Påverka skjema: 5 av 32

| Skjema | Kategori | Ubrukte slots | Ubrukte enums | Ubrukte typar |
|---|---|---|---|---|
| **common-ap-no** | Bibliotekskjema | 18/20 | 4/4 | 4/4 |
| **dqv-core** | Bibliotekskjema | 2/17 | 0 | 0 |
| **dcat-ap-no** | AP-NO-profil | 2/79 | 0 | 0 |
| **enhetsregisteret-bvrinn** | Domenemodell | 0 | 0 | 1/31 |
| **register-over-aksjeeiere** | Domenemodell | 1/24 | 0 | 0 |

**Detaljert oversikt:**

### 1. common-ap-no (bibliotekskjema)

**Ubrukte slots (18):**
- `versjonsnummer`, `heimeside`, `utgivelsesdato`, `anbefalt_term`,
  `versjonsmerknad`, `dekningsomraade`, `lisens`, `format`, `spraak`,
  `har_referanse`, `har_merknad`, `nokkelord`, `status`, `valuta`,
  `endringsdato`, `beskrivelse`, `tittel`, `identifikator_literal`

**Ubrukte enums (4):**
- `EULicence`, `EUFileType`, `EULanguage`, `ADMSStatus`

**Ubrukte typar (4):**
- `Duration`, `LangString`, `GYear`, `NonNegativeInteger`

**Vurdering:** ✅ **Legitimt** — desse er definerte for **import** av andre
AP-NO-skjema (`dcat-ap-no`, `skos-ap-no` osv.). Synleggjering er **ønskt**.

### 2. dqv-core (bibliotekskjema)

**Ubrukte slots (2):**
- `har_kvalitetsmaaling`, `har_kvalitetsmerknad`

**Vurdering:** 🤔 **Potensielt legitimt** — kan vere definerte for bruk i
`dqv-ap-no` som importerer dette skjemaet. Men burde vere brukt i lokale klasser.

### 3. dcat-ap-no (AP-NO-profil)

**Ubrukte slots (2):**
- `tittel_literal`, `referanse`

**Vurdering:** ⚠️ **Potensielt dead code** — kvifor er desse definerte men
ikkje brukt? Kan vere:
- Feil (skulle vore brukt i ein klasse)
- Reserved for framtidig bruk
- Faktisk dead code

Synleggjering vil **identifisere** dette for gjennomgang.

### 4. enhetsregisteret-bvrinn (domenemodell)

**Ubrukt type (1):**
- `Husnummer`

**Vurdering:** ⚠️ **Sannsynlegvis dead code** — kvifor er ein type definert
men aldri brukt i nokon slot? Synleggjering vil flagge dette.

### 5. register-over-aksjeeiere (domenemodell)

**Ubrukt slot (1):**
- `antall`

**Vurdering:** ⚠️ **Sannsynlegvis dead code** — slot definert men ikkje brukt
i nokon klasse. Synleggjering vil flagge dette.

## Vurdering av OR-logikk

### Fordeler

| Fordel | Konsekvens |
|---|---|
| ✅ **Synleggjer bibliotekskjema** | `common-ap-no` og `dqv-core` får vise alle slots/enums/typar dei tilbyr for import |
| ✅ **Identifiserer dead code** | 3 skjema (`dcat-ap-no`, `enhetsregisteret-bvrinn`, `register-over-aksjeeiere`) får synleggjort potensielt ubrukte element |
| ✅ **Følgjer prinsippet** | "Synleggjering av feil er ein god ting" — gjer det mogleg å oppdage og rette |
| ✅ **Enkel implementering** | Berre utvide eksisterande Jinja2-logikk med OR i staden for AND |
| ✅ **Liten påverknad** | Berre 5 av 32 skjema vert påverka |

### Ulemper

| Ulempe | Konsekvens |
|---|---|
| ⚠️ **Kan forvirre for domenemodeller** | `dcat-ap-no` vil vise `tittel_literal` og `referanse` som tilgjengelege slots — men kvifor er dei ikkje brukt? |
| ⚠️ **Krever gjennomgang** | Etter implementering må dei 3 domenemodellane gjennomgåast for å verifisere om ubrukte element er feil eller legitimt |

### Alternativ: Hybrid-løysing

I staden for global OR-logikk eller `is_library`-annotasjon:

**Implementer OR-logikk globalt + legg til metadata i dokumentasjonen**

Når eit element vert vist men er **ikkje brukt** i lokale klasser, merk det i
dokumentasjonen:

```markdown
| Slot | Description | Defined in | Usage |
| --- | --- | --- | --- |
| tittel | ... | common-ap-no | ✅ Used |
| versjonsnummer | ... | common-ap-no | ⚠️ Defined but unused |
```

**Fordel:** Gjer det **eksplisitt** kva som er brukt vs definert-men-ubrukt.

## Anbefaling

**Implementer OR-logikk globalt** med **metadata om bruk**.

**Grunngjeving:**

1. **Liten påverknad:** Berre 5 av 32 skjema vert påverka
2. **Synleggjering:** Identifiserer potensielt dead code i 3 skjema
3. **Bibliotekskjema:** Gjer `common-ap-no` og `dqv-core` meir nytige
4. **Prinsipp:** Følgjer "synleggjering av feil" — gjer problem synlege

**Risiko:** Låg — dokumentasjonen kan oppdaterast dersom ubrukte element
viser seg å vere legitimt reserved for framtidig bruk.

## Gjennomføring

### Steg 1: Utvid Jinja2-template

**Fil:** `src/assets/templates/docgen/index.md.jinja2`

**Endring i slots-samling (linje ~104-130):**

```jinja2
{%- set ns_used_slots = namespace(names=[]) -%}
{# Samle alle slots brukt i klasser #}
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
{%- endfor -%}

{# OR-LOGIKK: Legg til alle lokalt DEFINERTE slots (frå slots:-seksjonen) #}
{%- for slot_name in (schema.slots or {}).keys() %}
  {%- if slot_name not in ns_used_slots.names %}
    {%- set ns_used_slots.names = ns_used_slots.names + [slot_name] %}
  {%- endif %}
{%- endfor -%}
```

**Tilsvarande for enums (linje ~166-188):**

```jinja2
{# Samle brukte enums #}
{%- set ns_used_enums = namespace(names=[]) -%}
{%- for slot_name in ns_used_slots.names %}
  ...
{%- endfor -%}

{# OR-LOGIKK: Legg til alle lokalt DEFINERTE enums #}
{%- for enum_name in (schema.enums or {}).keys() %}
  {%- if enum_name not in ns_used_enums.names %}
    {%- set ns_used_enums.names = ns_used_enums.names + [enum_name] %}
  {%- endif %}
{%- endfor -%}
```

**Tilsvarande for types (linje ~204-226):**

```jinja2
{# Samle brukte typar #}
{%- set ns_used_types = namespace(names=[]) -%}
{%- for slot_name in ns_used_slots.names %}
  ...
{%- endfor -%}

{# OR-LOGIKK: Legg til alle lokalt DEFINERTE typar #}
{%- for type_name in (schema.types or {}).keys() %}
  {%- if type_name not in ns_used_types.names %}
    {%- set ns_used_types.names = ns_used_types.names + [type_name] %}
  {%- endif %}
{%- endfor -%}
```

### Steg 2 (valfri): Legg til bruksmetadata i tabellane

**Utvid slot-tabellen med "Usage"-kolonne:**

```jinja2
{%- if ns_slots_verdiar.items %}
### Verdiar

| Slot | Description | Defined in | Usage |
| --- | --- | --- | --- |
{%- for s in ns_slots_verdiar.items|sort(attribute=sort_by) %}
  {%- set origin = s.from_schema if s.from_schema else schema.id %}
  {%- set is_used = namespace(value=false) -%}
  {%- for class_name in schemaview.all_classes() %}
    {%- set c = schemaview.get_class(class_name) %}
    {%- set c_origin = c.from_schema if c.from_schema else schema.id %}
    {%- if c and not c.tree_root and c_origin == schema.id and s.name in (c.slots or []) %}
      {%- set is_used.value = true -%}
    {%- endif %}
  {%- endfor %}
  {%- if is_used.value -%}
    {%- set usage_badge = "✅ Used" -%}
  {%- else -%}
    {%- set usage_badge = "⚠️ Defined" -%}
  {%- endif %}
| {{ gen.link(s, True) }} | {{ s.description|enshorten }} | {{ origin }} | {{ usage_badge }} |
{%- endfor %}
{% endif -%}
```

**Tilsvarande for enums og types.**

### Steg 3: Regenerer dokumentasjon

```bash
# Regenerer berre dei 5 påverka skjemaa
make gen-doc SCHEMA=src/linkml/ap-no/common-ap-no/common-ap-no-schema.yaml
make gen-doc SCHEMA=src/linkml/ap-no/dqv-ap-no/dqv-core-schema.yaml
make gen-doc SCHEMA=src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml
make gen-doc SCHEMA=src/linkml/ngr/enhetsregisteret-bvrinn/enhetsregisteret-bvrinn-schema.yaml
make gen-doc SCHEMA=src/linkml/oreg/register-over-aksjeeiere/register-over-aksjeeiere-schema.yaml

# Regenerer mkdocs-portal
cd mkdocs && ./publish.sh
```

### Steg 4: Verifiser resultat

**Før (common-ap-no):**
- Slots: 2 (`id`, `type_concept`)
- Enums: 0 ("Ingen enumerations brukt i denne modellen")
- Types: 1 (`uriorcurie`)

**Etter (common-ap-no):**
- Slots: 20 (alle definerte slots)
- Enums: 4 (`EULicence`, `EUFileType`, `EULanguage`, `ADMSStatus`)
- Types: 4 (`LangString`, `NonNegativeInteger`, `Duration`, `GYear`)

**Med bruksmetadata (valfritt):**
- `id` — ✅ Used
- `type_concept` — ✅ Used
- `tittel` — ⚠️ Defined (ikkje brukt i common-ap-no sine klasser, men tilgjengeleg for import)
- ...

### Steg 5: Gjennomgå identifiserte ubrukte element

Etter implementering, gjennomgå dei 3 domenemodellane:

1. **dcat-ap-no:** `tittel_literal`, `referanse`
   - Er desse feil? Skal dei brukast i ein klasse?
   - Er dei reserved for framtidig bruk?
   - Skal dei slettast?

2. **enhetsregisteret-bvrinn:** `Husnummer` (type)
   - Kvifor er typen definert men aldri brukt?
   - Skal den brukast i ein slot?
   - Skal den slettast?

3. **register-over-aksjeeiere:** `antall` (slot)
   - Skal denne brukast i ein klasse?
   - Skal den slettast?

## Verifisering

- [ ] `index.md.jinja2` har OR-logikk for slots, enums, typar
- [ ] (Valfritt) Bruksmetadata (`✅ Used` / `⚠️ Defined`) er lagt til i tabellar
- [ ] `make gen-doc` for dei 5 påverka skjemaa genererer fullstendige lister
- [ ] `mkdocs/docs/ap-no/common-ap-no/index.md` viser alle 20 slots, 4 enums, 4 typar
- [ ] `mkdocs/docs/ap-no/dcat-ap-no/index.md` viser `tittel_literal` og `referanse`
- [ ] Ubrukte element i dei 3 domenemodellane er gjennomgått og handtert

## Utført

**Dato:** 2026-07-11

**Arbeid:**
1. ✅ Implementert OR-logikk i `index.md.jinja2` (slots, enums, types)
2. ✅ Lagt til bruksmetadata (`✅ Used` / `⚠️ Defined`) i alle tabellar
3. ✅ Regenerert dokumentasjon for dei 5 påverka skjemaa
4. ✅ Verifisert at `common-ap-no` no viser alle 20 slots, 4 enums, 4 typar
5. ✅ Generert commit-melding (utkast)

**Resultat:**

### common-ap-no (før vs etter)

**Før:**
- Slots: 2 (`id`, `type_concept`)
- Enums: 0 ("Ingen enumerations brukt i denne modellen")
- Types: 1 (`uriorcurie`)

**Etter:**
- Slots: 20 (18 med ⚠️ Defined, 2 med ✅ Used)
- Enums: 4 (alle med ⚠️ Defined)
- Types: 8 (4 lokale + 4 importerte, med bruksmetadata)

### Andre påverka skjema

- **dqv-core:** 2 ubrukte slots no synleggjort med ⚠️ Defined
- **dcat-ap-no:** 2 ubrukte slots (`tittel_literal`, `referanse`) no synleggjort
- **enhetsregisteret-bvrinn:** 1 ubrukt type (`Husnummer`) no synleggjort
- **register-over-aksjeeiere:** 1 ubrukt slot (`antall`) no synleggjort

**Neste steg:**

Gjennomgå dei 3 domenemodellane med ubrukte element for å vurdere om dei skal:
- Brukast i ein klasse (var ein feil)
- Slettast (dead code)
- Behaldast (reserved for framtidig bruk)
