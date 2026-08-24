---
name: mkdocs-portal
description: Korleis mkdocs/publish.sh byggjer dokumentasjonsportalen, Jinja2-template whitespace-reglar, heading-slug-fella for æ/ø/å, og relative/absolutte lenkjereglar. Lastast automatisk ved arbeid med mkdocs/publish.sh, Jinja2-templatar eller sider under mkdocs/docs/.
paths:
  - "mkdocs/**"
  - "src/assets/templates/docgen/**"
---

## Dokumentasjonsportal (mkdocs)

`mkdocs/mkdocs.yml` vert **automatisk regenerert** av `mkdocs/publish.sh` (Steg 4)
kvar gong `make docs-publish` køyrer. Endringar gjort direkte i `mkdocs.yml` vert
overskrivne ved neste publisering.

**Sannkjelda for nav-menyen er `mkdocs/publish.sh`**, ikkje `mkdocs.yml`.

- Nye rettleiingssider (`mkdocs/docs/*.md`) må leggast til i heredoc-blokka i
  `publish.sh` (leit etter `nav:` → `- Rettleiingar:`)
- Domene og skjema vert lagt til automatisk frå `generated/`-strukturen — ikkje
  rediger desse manuelt
- Statisk innhald (`mkdocs/docs/` utanom genererte domene-katalogar) vert aldri
  sletta av `publish.sh`

`mkdocs/docs/` er brukarvendt dokumentasjon og normativ kjelde for steg-for-steg-rettleiingar (t.d. `ny-domenemodell.md`). CLAUDE.md er normativ kjelde for modelleringsprinsipp og AI-instruksjonar — desse to skal ikkje duplisere kvarandre.

### Korleis `publish.sh` fungerer

`mkdocs/publish.sh` transformerer LinkML-genererte artefakter frå `generated/` til ein
publiserbar MkDocs-portal i `mkdocs/docs/`. Scriptet køyrer i fire hovudsteg:

**Steg 1: Rens tidlegare genererte domene-katalogar**
- Slettar `mkdocs/docs/<domain>/` for kvar `generated/<domain>/` som finst
- Fjernar `mkdocs/docs/<domain>/` for domene som ikkje lenger finst i `generated/`
- Beheld statisk innhald (`mkdocs/docs/*.md`, `stylesheets/`, `javascripts/`)

**Steg 2: Generer innhald per domene og skjema (parallelt)**

For kvart skjema i `generated/<domain>/<schema>/`:

1. Kopier artefaktfiler (`*.ttl`, `*.json`, `*.yaml` osv.) frå `generated/<domain>/<schema>/` til `mkdocs/docs/<domain>/<schema>/`
2. Kopier `CHANGELOG.md` frå `src/linkml/<domain>/<schema>/` dersom den finst
3. Kopier PlantUML-diagram frå `generated/<domain>/<schema>/diagrams/` til `mkdocs/docs/<domain>/<schema>/diagrams/`
4. Kopier gen-doc Markdown-filer frå `generated/<domain>/<schema>/docs/` til `mkdocs/docs/<domain>/<schema>/klasser/`
5. Generer `mkdocs/docs/<domain>/<schema>/index.md` med følgjande seksjons-rekkjefølgje:
   - Hovudoverskrift (`# <schema>`)
   - **Metadata-tabell** (`## Metadata` frå gen-doc — name, title, description, versjon, lisens, utgiver, status osv.)
   - Publiseringsinfo (boks dersom `published-uris.lock` finst)
   - **ER-diagram** (`## ER-diagram` med PlantUML SVG — zoombart, lenke til full versjon)
   - Klasseliste (`## Classes`, `## Slots`, `## Enumerations`, `## Types` frå gen-doc)
   - Artefaktabell (`## Generated artifacts` med lenkjer til `.ttl`, `.json`, `.puml` osv.)
   - **Valideringsresultat** (`## Valideringsresultat` frå `validation/<versjon>/<policy>.json`)
   - **Versjonslog** (`## Versjonslog` frå `CHANGELOG.md`)

Alle skjema-jobbar køyrer parallelt for å redusere byggtid.

**Steg 3: Generer `valideringsregler.md` og hovud-`index.md`**
- `valideringsregler.md` genereres frå `src/mcp-linkml-validator/policies/README.md` med GitHub-lenkjer
- Hovud-`index.md` genereres frå `README.md` (med filtrering av intern-referansar)

**Steg 4: Generer `mkdocs.yml`**
- Statisk konfigurasjon (theme, plugins, markdown_extensions) frå heredoc-blokk
- Dynamisk nav-meny: `- Rettleiingar:` (statisk) + domene-seksjonar (generert frå `generated/`-struktur)

**Viktige detaljar:**

- **Metadata-tabell** vert generert av Jinja-templaten `src/assets/templates/docgen/index.md.jinja2` og inneheld name, title, description, versjon, lisens, utgiver, status m.m.
- **ER-diagram** brukar PlantUML SVG (ikkje Mermaid) — zoombart i nettleser, med lenke til full versjon som viser importerte klasser
- **Types-lista** viser alle typar som faktisk vert brukt i modellen (frå `slots[*].range`), inkludert importerte typar frå `linkml:types` m.fl., med "Defined in"-kolonne som viser "Local" eller "Imported"
- **Enumerations-lista** viser alle enums som faktisk vert brukt i modellen (frå `slots[*].range`), inkludert importerte enums, med "Defined in"-kolonne
- **Valideringsresultat** vert generert av `mkdocs/lib/scripts/generate-validation-md.py` frå `validation/<versjon>/<policy>.json` med rein Markdown (nummererte lister, ikkje `<details>`-blokkar)
- **Versjonslog** vert kopiert direkte frå `CHANGELOG.md` som rein Markdown (ikkje kollapsa)
- **Lowercase-transformasjon** av klassefiler skjer for å unngå konflikt på case-insensitive filsystem (Windows/macOS)
- **Filtrert PlantUML-diagram** vert prioritert over full versjon i ER-diagram-seksjonen

### PlantUML-diagram

`make gen-plantuml` genererer **to versjonar** av PlantUML-diagramma:

- **`<modell>.puml/.svg`** — full versjon med alle klasser (inkl. importerte frå dcat-ap-no, dqv-ap-no osv.)
- **`<modell>-filtered.puml/.svg`** — filtrert versjon med **kun lokale klasser** frå skjemaet

Filtrering:
- Beheld alle klasser definerte i det lokale skjemaet sitt `classes:`-blokk (inkl. abstrakte klasser)
- Filtrer vekk `tree_root`-klassen (containerklassen)
- Filtrer vekk importerte klasser (frå dcat-ap-no, dqv-ap-no osv.)
- Behald relasjonar og arvestruktur mellom dei filtrerte klassane

Dokumentasjonsportalen (`mkdocs/docs/`) viser den **filtrerte versjonen** som standard, med lenke til full versjon merka "(full)".

### Jinja2-template whitespace-kontroll

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
   | Enumeration | Description | Defined in | Usage |
   | --- | --- | --- | --- |
   {% for enum_name in enums|sort -%}
   {%- set e = get_enum(enum_name) -%}
   {%- if e -%}
   {%- set origin = e.from_schema -%}
   | {{ e.name }} | {{ e.description }} | {{ origin }} | {{ usage }} |
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

### Ankerlenkjer til overskrifter (heading-slugs)

`mkdocs.yml` (heredoc-blokka i `publish.sh`) konfigurerer **ikkje** `toc`-utvidinga eksplisitt, så MkDocs/Python-Markdown brukar sin **default** slugify-funksjon (`markdown.extensions.toc.slugify`, `unicode=False`) til å generere `id`-attributtet ei overskrift får — og dermed kva `#anker` ei intern lenkje til overskrifta må bruke. Denne funksjonen er **ikkje** ei transkriberings-funksjon (ø → o, æ → ae) — han er reint ASCII-filtrerande:

1. `unicodedata.normalize('NFKD', tekst)` — dekomponerer teikn som HAR ein eiga diakritisk NFKD-form
2. `.encode('ascii', 'ignore').decode('ascii')` — **fjernar** alle attverande ikkje-ASCII-teikn (inkludert dei diakritiske merka NFKD nett skilde ut)
3. `re.sub(r'[^\w\s-]', '', ...)` — fjernar attverande teiknsetjing (parentes, spørjeteikn, skråstrek, hermeteikn)
4. Mellomrom → bindestrek, alt til små bokstavar

**Konsekvens — to heilt ulike utfall for norske bokstavar:**

| Bokstav | NFKD-dekomponerbar? | Utfall i slug | Eksempel |
|---|---|---|---|
| å, é, ö, ü m.fl. | Ja (bokstav + kombinerande merke) | Merket fjernast, **basisbokstaven står att** | `Skriftspråk` → `skriftsprak`, `éin` → `ein` |
| æ, ø, ß | **Nei** (eiga, ikkje-samansett teikn) | **Heile bokstaven forsvinn** — ingen erstatning | `høstingsendepunkt` → `hstingsendepunkt`, `Æ Ø Å` → `a` (berre Å-en si `a` står att) |

Dette er lett å gå i fella på nettopp fordi å oppfører seg annleis enn æ/ø — ei intuitiv, hand-skriven slug som transkriberer alle tre likt (t.d. `hoysting`/`hosting`) vert **feil**, og MkDocs sin lenkje-validator (`validation.links` i `mkdocs.yml`) fangar det først ved bygg, ikkje ved skriving.

**Regel:** Skriv **aldri** ein `#anker`-verdi for ei overskrift med æ/ø/å/andre diakritiske teikn frå augemål åleine. Verifiser alltid mot faktisk generert `id`:

```bash
make docs-build
grep -o 'id="[^"]*"' mkdocs/site/<sti-til-sida>/index.html
```

Gjeld berre interne lenkjer til overskrifter i **statisk** innhald i `mkdocs/docs/` (rettleiingssider) — genererte skjema-sider sine interne lenkjer (klasser, slots osv.) vert alt bygde frå faktiske `id`-ar av gen-doc-malen, ikkje handskrivne.

### Relative vs. absolutte lenkjer i portalinnhald

Lenkjer i `.md`-filer skal følgje kor målet faktisk bur:

- **Mål som er bygd inn i mkdocs-portalen** (finst under `mkdocs/docs/` etter `publish.sh` — anten statisk rettleiingsinnhald eller generert domene-/skjemainnhald) → bruk **relative lenkjer** (t.d. `../publisering/publisering-modell.md` eller `klasser/status.md`), aldri absolutte URL-ar til `brreg.github.io` eller GitHub. Relative lenkjer vert validerte av mkdocs sin eigen `validation.links` ved bygg (fangar broten interne referansar før publisering, jf. § Ankerlenkjer over) og fungerer korrekt både i lokal `mkdocs serve`-førehandsvising og på den publiserte portalen.
- **Mål som ikkje er bygd for portalen** (t.d. `BUGS.md`, `specs/`, kjeldeskjema under `src/linkml/`, andre repo-filer utanfor `mkdocs/docs/`) → bruk **absolutt lenkje** til fila i GitHub-repoet (`https://github.com/brreg/linkml-datamodellering-no/blob/main/<sti>`). Desse måla har ingen portal-relativ sti i det heile, sidan dei aldri vert kopierte inn i `mkdocs/docs/`.

Sjå `specs/done/lenkjesjekk-3817-feil-evaluering.md` for eit konkret eksempel på brotet denne regelen skal hindre: fleire rettleiingssider i `mkdocs/docs/` lenka til `specs/bugs/README.md` (ein sti som ikkje finst, og som uansett aldri ville vore ei gyldig relativ portallenkje sidan `specs/` ikkje er portalinnhald) i staden for korrekt absolutt lenkje til `BUGS.md`.
