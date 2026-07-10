# Fiks gen-doc Arva-tabell og reduser whitespace i class.md.jinja2

## Bakgrunn

Genererte klassedokumentasjonssider (`mkdocs/docs/<domain>/<schema>/klasser/<klasse>.md`) har to problem:

1. **Arva-tabellen renderar ikkje korrekt** — alle tabellinnganger vert festa saman på éi linje, slik at Markdown-parseren ser berre éi tabellrad i staden for fleire.
2. **Mange unødvendige tomme linjer** — Jinja2-logikkblokker (`{% set %}`, `{% for %}`, `{% if %}`) utan whitespace-kontroll renderar som tomme linjer i output.

### Eksempel frå `rektor.md`

Linje 125-128 i `mkdocs/docs/samt/samt-bu/klasser/rektor.md`:

```markdown
| Namn | Kardinalitet og domene | Beskriving | Frå |
| --- | --- | --- | --- || [id](id.md) | 1 <br/> [xsd:anyURI](...) | URI-identifikator for ressursen | [Person](person.md) |
| [navn](navn.md) | 0..1 <br/> [xsd:string](...) | Namn på ressursen | [Person](person.md) |
```

**Forventet rendering:**

```markdown
| Namn | Kardinalitet og domene | Beskriving | Frå |
| --- | --- | --- | --- |
| [id](id.md) | 1 <br/> [xsd:anyURI](...) | URI-identifikator for ressursen | [Person](person.md) |
| [navn](navn.md) | 0..1 <br/> [xsd:string](...) | Namn på ressursen | [Person](person.md) |
```

### Årsakskjede

**Arva-tabell:**

```jinja
{% if gen.get_indirect_slots(element)|length > 0 %}
### Arva

| Namn | Kardinalitet og domene | Beskriving | Frå |
| --- | --- | --- | --- |
{%- for slot in gen.get_indirect_slots(element) -%}
| {{ gen.link(slot) }} | {{ gen.cardinality(slot) }} <br/> {{ compute_range(slot) }} | {{ slot.description|enshorten }} | {{ gen.links(gen.get_slot_inherited_from(element.name, slot.name))|join(', ') }} |
{% endfor -%}
{% endif %}
```

`{%-` stripar linjeskift **før** blokka og `-%}` stripar linjeskift **etter** blokka. Linje 154 (`{%- for`) stripar linjeskiftet etter separator-rada, slik at første tabellrad vert festa til separator-rada. Linje 156 (`{% endfor -%}`) stripar linjeskiftet før `{% endif %}`, men det har ikkje synleg effekt.

**Løysing:** Fjern `-` frå linje 154 og 156 slik at linjeskift vert bevarte.

**Mange tomme linjer:**

Logikkblokker linje 107-114 og 126-138 renderar som tomme linjer fordi `{% set %}` og `{% if %}` ikkje produserer synleg innhald, men **Jinja2 renderar linjeskiftet etter kvar blokk**.

**Løysing:** Legg til `-` i blokk-sluttane (`%}` → `-%}`) for å strippe unødvendige linjeskift.

## Tiltak

1. [x] Reduser whitespace i `src/assets/templates/docgen/class.md.jinja2`:
   - Fjerna `{%-` og `-%}` frå Arva-tabell-loopen (linje 153, 155 → linje 153, 155)
   - La til `-%}` i logikkblokker for `Obligatorisk`/`Anbefalt`/`Valgfri`-loopar (linje 101, 104, 107-123)
   - La til `-%}` i logikkblokker for `Andre`-loopen (linje 126-147)
   - La til `-%}` på Arva-blokk slutt (linje 156)
2. [x] Regenerer gen-doc-output: `make gen-docs` (alle skjema)
3. [x] Verifiser at `generated/samt/samt-bu-schema/docs/Rektor.md` har:
   - Arva-tabellen med korrekt linjeskift før kvar tabellrad ✓
   - Færre tomme linjer mellom seksjonar (243 linjer vs 291 tidlegare) ✓
4. [x] Publiser docs: `make docs-publish` (manuell kopiering av samt-bu kreva pga. case-insensitive filsystem)
5. [ ] Generer commit-melding i conventional commits-format

## Rettleiing

**Jinja2 whitespace-kontroll:**

- `{%-` stripar linjeskift **før** blokka
- `-%}` stripar linjeskift **etter** blokka
- Bruk `-%}` i logikkblokker (`{% set %}`, `{% if %}`, `{% for %}`) som ikkje skal produsere tomme linjer
- **Ikkje** bruk `{%-` eller `-%}` i loopar som skal produsere fleire linjer (t.d. Arva-tabell)

**Test-strategi:**

1. Køyr `make gen-docs` (alle skjema, ikkje berre samt-bu)
2. Sjekk `generated/samt/samt-bu-schema/docs/Rektor.md` med `cat -A` for å sjå linjeskift
3. Sjekk at Arva-tabellen har `$`-symbol (linjeskift) etter kvar tabellrad
4. Publiser til mkdocs: `make docs-publish`
5. Verifiser `mkdocs/docs/samt/samt-bu/klasser/rektor.md` har same linjetal som generated-versjonen

## Utført

**Endra filer:**
- `src/assets/templates/docgen/class.md.jinja2`: La til whitespace-kontroll (`-%}`) i logikkblokker, fjerna frå Arva-tabell-loop

**Resultat:**
- Arva-tabellen renderar no korrekt med linjeskift mellom kvar rad
- Eigenskapar-seksjonen har færre tomme linjer (1 i staden for 4-7)
- Totalt linjetal redusert frå 291 til 243 for `Rektor.md`
- Alle 41 skjema regenererte med `make gen-docs`
