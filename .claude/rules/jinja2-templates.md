---
name: jinja2-templates
description: Whitespace-kontroll for Jinja2-malar (docgen) — ingen indentasjon av Jinja-blokker, {%- -%}-mønster for tabellar/variablar/if-blokkar, feilsøkingsliste. Lastast automatisk ved arbeid med filer under src/assets/templates/docgen/.
paths:
  - "src/assets/templates/docgen/**"
---

## Jinja2-template whitespace-kontroll

Når du redigerer Jinja2-templatear (t.d. `src/assets/templates/docgen/index.md.jinja2`), følg desse reglane for å unngå ekstra linjeskift og indenteringsproblem i generert output:

**HOVUDREGEL: Ingen indentasjon av Jinja-blokker**
- **ALDRI indenter Jinja-taggar (`{%`, `{{`, `{#`)** — all indentasjon vert inkludert i generert output
- `classes.sh` brukar `awk '/^## Subsets/,0'` som krev at overskrifter startar på kolonne 0
- Med indentasjon matchar ikkje `^##` (start-of-line), og seksjonen vert ikkje ekstrahert

**Hovudregel for whitespace-kontroll:** Bruk `-` i Jinja-taggar (`{%-` og `-%}`) for å strippe kvitteikn før/etter taggen:
- `{%-` strippar kvitteikn (mellomrom, tab, linjeskift) **før** taggen
- `-%}` strippar kvitteikn **etter** taggen

**Kritiske stader å unngå ekstra linjeskift:**

1. **Tabellar:** Ingen indentasjon på tabellrader, og korrekt `-`-plassering:
   ```jinja2
   | Enumeration | Description | Defined in |
   | --- | --- | --- |
   {% for enum_name in enums|sort -%}
   {%- set e = get_enum(enum_name) -%}
   {%- if e -%}
   {%- set origin = e.from_schema -%}
   | {{ e.name }} | {{ e.description }} | {{ origin }} |
   {% endif -%}
   {%- endfor -%}
   ```
   - `{% for ... -%}` (IKKJE `{%- for`) → beheld linjeskift etter header-linje
   - `{% endif -%}` (IKKJE `{%- endif`) → beheld linjeskift før endif (= linjeskift mellom tabellinjer)
   - `{%- endfor -%}` → strippar kvitteikn før og etter (hindrar ekstra linjeskift etter tabellen)
   - **Ingen indentasjon** på linjer inne i loopen — all indentasjon vert inkludert i output

2. **Variable assigningar:** Alltid bruk `{%- ... -%}` for å unngå kvitteikn:
   ```jinja2
   {%- set my_var = some_value -%}
   ```

3. **If-blokkar som IKKJE produserer synleg output:** Bruk `{%- ... -%}`:
   ```jinja2
   {%- if condition -%}
     {%- set variable = value -%}
   {%- endif -%}
   ```

4. **If-blokkar som produserer output:** Juster `-` basert på om du vil ha linjeskift:
   ```jinja2
   {%- if items %}
   ### Overskrift

   {{ items|join(', ') }}
   {% endif -%}
   ```

**Feilsøking:** Dersom generert Markdown har ekstra tomme linjer eller manglande linjeskift:
1. Sjekk om det er **indentasjon** (mellomrom/tab) på Jinja-blokker — **fjern all indentasjon**
2. Sjekk om `-` manglar på starten/slutten av taggar — legg til der kvitteikn skal strippast
3. Sjekk om `-` er **feil stad** (t.d. `{%- for` i staden for `{% for`) — juster basert på ønskt linjeskift

**Viktig:** Markdown-tabellar krev linjeskift mellom kvar rad, så **ALDRI** bruk `{%- endif -%}` direkte etter ei tabellinje — bruk `{% endif -%}` i staden.

**Verifiser alltid mot faktisk generert output** — same prinsipp som
heading-slug-fella i `.claude/rules/mkdocs-portal.md`:

```bash
make docs-build
```
