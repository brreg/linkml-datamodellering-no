# Metadata-felt og Markdown-formatering i index.md

## Utført

Alle tiltak er implementerte:

1. ✓ **Jinja-template oppdatert** — metadata-tabell inneheld no name, title og description
2. ✓ **Seksjons-rekkjefølgje omorganisert** — metadata → ER-diagram → klasseliste → artefaktar → validering → versjonslog
3. ✓ **Details-blokkar fjerna** — valideringsresultat brukar rein Markdown med nummererte lister
4. ✓ **PlantUML SVG i staden for Mermaid** — ER-diagram er no zoombart i nettleser
5. ✓ **CLAUDE.md oppdatert** — dokumenterer nye seksjons-rekkjefølgje og rein Markdown-formatering

**Avvik frå opphavleg plan:**
- Ingen avvik — alle tiltak gjennomførte som planlagt

**Resultat:**
- Metadata-blokka viser no name, title og description
- Description er ikkje lenger vist som separat overskrift før metadata-tabellen
- ER-diagram er zoombart (PlantUML SVG)
- Versjonslog og valideringsresultat har korrekt Markdown-formatering
- Seksjons-rekkjefølgja er meir brukarvenleg: metadata og oversikt først, vedlikehald sist

## Bakgrunn

Metadata-blokka i genererte `index.md`-filer manglar name, title og description.
I tillegg vert description vist som overskrift før metadata-tabellen, noko som gir
duplisering når me legg description inn i tabellen.

Markdown-formatering i endringshistorikk (CHANGELOG.md), feil og åtvaringar vart
tidlegare vist i `<details>`-blokkar med `markdown='1'`-attributt, men dette fungerer
ikkje konsekvent på tvers av MkDocs-versjonar. Løysinga er å fjerne `<details>`-blokkar
heilt og bruke rein Markdown-tekst i staden.

## Mål

1. Legg til name, title og description som felt i metadata-tabellen
2. Fjern description som separat overskrift før metadata-tabellen
3. Bruk rein Markdown (ikkje `<details>`-blokkar) for:
   - Endringshistorikk (frå CHANGELOG.md)
   - Feil og åtvaringar (generert av `generate-validation-md.py`)
4. Omorganiser seksjons-rekkjefølgje i index.md til ein meir brukarvenleg struktur
5. Gjer ER-diagram zoombart og leseleg (erstatt innebygd Mermaid med PlantUML SVG)

## Ny seksjons-rekkjefølgje i index.md

**Tidlegare rekkjefølgje:**
1. Hovudoverskrift
2. Publiseringsinfo (boks)
3. ER-diagram
4. Valfri skjema-skildring (description.md)
5. Versjonslog
6. Valideringsresultat
7. Klasseliste
8. Artefaktabell

**Ny rekkjefølgje:**
1. Hovudoverskrift (`# <schema>`)
2. **Metadata-tabell** (name, title, description, versjon, lisens, utgjevar, status osv.)
3. Publiseringsinfo (boks dersom `published-uris.lock` finst)
4. ER-diagram
5. **Klasseliste** (`## Classes`, `## Slots`, `## Enumerations`, `## Types`)
6. **Artefaktabell** (`## Generated artifacts`)
7. **Valideringsresultat** (`## Valideringsresultat`)
8. **Versjonslog** (`## Versjonslog`)

**Rasjonale:**
- **Metadata først** — gir kontekst (kva er dette, kven eig det, kva lisens)
- **ER-diagram tidleg** — visuell oversikt over strukturen
- **Klasseliste som hovudinnhald** — dette er det brukaren primært skal forstå
- **Artefaktar rett etter** — viser kva du kan laste ned/bruke
- **Valideringsresultat og versjonslog sist** — viktig for vedlikehald, men sekundært for førstegangs brukar

## Tiltak

### 1. Oppdater Jinja-template for metadata-blokk

**Fil:** `src/assets/templates/docgen/index.md.jinja2`

- Legg til Name-felt (alltid synleg): `| Name | \`{{ schema.name }}\` |`
- Legg til Title-felt (dersom `schema.title` finst)
- Legg til Description-felt (dersom `schema.description` finst)
- Fjern `{% if schema.description %}{{ schema.description }}{% endif %}` frå toppen av templaten
- Behald hovudoverskrift: `# {% if schema.title %}{{ schema.title }}{% else %}{{ schema.name }}{% endif %}`

**Rekkjefølgje i metadata-tabell:**
1. Name
2. Title (valfri)
3. Description (valfri)
4. Schema URI
5. Versjon
6. Lisens
7. Utgjevar
8. Status
9. Endringsdato
10. Utgivelsesdato
11. Imports

### 2. Omorganiser seksjons-rekkjefølgje i publish.sh

**Fil:** `mkdocs/publish.sh`

Endre rekkjefølgja i `process_schema()`-funksjonen (linje ~142-279) til:

1. Hovudoverskrift
2. Publiseringsinfo-boks
3. ER-diagram
4. Metadata-tabell (frå gen-doc index.md — ekstrahert frå `## Metadata` til neste `##`)
5. Klasseliste (frå gen-doc index.md — frå `## Classes` til slutten)
6. Artefaktabell
7. Valideringsresultat
8. Versjonslog

**Konkret endring:**

Flytt versjonslog-blokka frå ~linje 174-187 til **etter** artefaktabell-seksjonen (~linje 270).

**Ny versjonslog-blokk (utan `<details>`):**
```bash
# Versjonslog (CHANGELOG.md som rein Markdown)
changelog_src="$REPO_ROOT/src/linkml/$domain/$schema/CHANGELOG.md"
if [ -f "$changelog_src" ]; then
    echo ""
    echo "## Versjonslog"
    echo ""
    # Fjern hovudoverskrift "# Changelog" frå CHANGELOG.md dersom den finst
    tail -n +1 "$changelog_src" | awk 'NR==1 && /^# Changelog/ { next } 1'
fi
```

**Ny metadata-ekstraksjon (etter ER-diagram, før klasseliste):**
```bash
# Metadata-tabell frå gen-doc (ekstrahert frå docs/index.md)
gendoc_index="$schema_dir/docs/index.md"
if [ -f "$gendoc_index" ]; then
    echo ""
    # Ekstraher frå "## Metadata" til (men ikkje inkludert) neste "## "-seksjon
    awk '/^## Metadata$/,/^## / { if (/^## / && !/^## Metadata$/) exit; print }' "$gendoc_index"
fi
```

### 3. Fjern details-blokk frå valideringsresultat

**Fil:** `src/assets/scripts/generate-validation-md.py`

**Tidlegare løysing (ikkje funksjonell):**
- Feil og åtvaringar vart viste i code-blokkar (````) eller `<details markdown='1'>`-blokkar
- Markdown-formatering fungerte ikkje konsekvent

**Ny løysing:**
- Fjern `<details>`-taggar heilt
- Bruk rein Markdown med nummerert liste
- Format kvar feil/åtvaring som:
  ```markdown
  1. **`<code>`** — `<target>`
     <message>
  ```

**Endring i feil-seksjon (linje ~55-70):**
```python
if errors:
    lines += [
        "",
        f"### Feil ({error_count})",
        "",
    ]
    for idx, issue in enumerate(errors, start=1):
        code = issue.get("code", "")
        target = issue.get("target", "")
        message = issue.get("message", "")
        lines.append(f"{idx}. **`{code}`** — `{target}`")
        lines.append(f"   {message}")
        lines.append("")
```

**Endring i åtvarings-seksjon (linje ~72-87):**
```python
if warnings:
    lines += [
        "",
        f"### Åtvaringar ({warning_count})",
        "",
    ]
    for idx, issue in enumerate(warnings, start=1):
        code = issue.get("code", "")
        target = issue.get("target", "")
        message = issue.get("message", "")
        lines.append(f"{idx}. **`{code}`** — `{target}`")
        lines.append(f"   {message}")
        lines.append("")
```

### 4. Gjer ER-diagram zoombart

**Problem:**
- Mermaid ER-diagram er statiske og har veldig liten tekst
- Ikkje mogleg å zoome eller interagere med diagrammet
- Uleselig på store modellar

**Løysing:**
- Erstatt Mermaid ER-diagram med PlantUML SVG-fil
- PlantUML-diagram er allereie genererte (`make gen-plantuml`)
- SVG-filer støttar zoom og pan i nettlesaren

**Fil:** `mkdocs/publish.sh`

**Gammal kode (linje ~161-165):**
```bash
# Embed oversiktsdiagram frå gen-erdiagram (berre filtrert versjon — importerte klasser visast ikkje)
erdiagram_file="$out/${schema}-erdiagram.md"
if [ -f "$erdiagram_file" ] && grep -q '{' "$erdiagram_file" 2>/dev/null; then
    awk 'NR==1 && /^# / { next } 1' "$erdiagram_file"
fi
```

**Ny kode:**
```bash
# Embed PlantUML-diagram (filtrert versjon — kun lokale klasser)
plantuml_svg="diagrams/${schema}-filtered.svg"
plantuml_full="diagrams/${schema}.svg"

# Prioriter filtrert versjon
if [ -f "$out/$plantuml_svg" ]; then
    echo ""
    echo "## ER-diagram"
    echo ""
    echo "![ER-diagram]($plantuml_svg)"
    echo ""
    echo "*Diagrammet viser kun lokale klasser. [Vis fullstendig diagram med importerte klasser]($plantuml_full).*"
elif [ -f "$out/$plantuml_full" ]; then
    echo ""
    echo "## ER-diagram"
    echo ""
    echo "![ER-diagram]($plantuml_full)"
fi
```

**Fordeler:**
- SVG-filer kan zoomast med nettleser (Ctrl+scroll eller browser zoom)
- Betre kvalitet og lesbarheit
- Kan lastast ned separat som `.puml`-kjeldekode
- Konsistent med artefakt-lenker lenger ned i dokumentet

**Alternativ (dersom zoom i nettleser ikkje er nok):**

Legg til JavaScript-basert zoom via MkDocs-plugin eller custom script:

**Fil:** `mkdocs/docs/javascripts/svg-zoom.js` (ny fil)
```javascript
// Legg til zoom-funksjonalitet på alle SVG-bilete
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('img[src$=".svg"]').forEach(img => {
        img.style.cursor = 'pointer';
        img.addEventListener('click', function() {
            window.open(this.src, '_blank');
        });
        img.title = 'Klikk for å opne i nytt vindauge';
    });
});
```

**Fil:** `mkdocs/mkdocs.yml`
```yaml
extra_javascript:
  - javascripts/nav-active-fix.js
  - javascripts/svg-zoom.js  # Ny
```

Dette gjer at brukaren kan klikke på SVG-biletet for å opne det i eit nytt vindauge i full størrelse.

### 5. Oppdater CLAUDE.md-dokumentasjon

**Fil:** `CLAUDE.md`

Oppdater seksjonen "Korleis `publish.sh` fungerer" → "Steg 2" (linje ~129-137):

**Gammal seksjons-rekkjefølgje:**
```
5. Generer `mkdocs/docs/<domain>/<schema>/index.md` med følgjande seksjons-rekkjefølgje:
   - Hovudoverskrift (`# <schema>`)
   - Publiseringsinfo (boks dersom `published-uris.lock` finst)
   - ER-diagram (frå `<schema>-erdiagram.md`, utan overskrift)
   - Valfri skjema-skildring (frå `src/linkml/<domain>/<schema>/description.md`)
   - **Versjonslog** (`## Versjonslog` i kollapsa `<details>`-blokk frå `CHANGELOG.md`)
   - **Valideringsresultat** (`## Valideringsresultat` frå `validation/<versjon>/<policy>.json`, generert av `generate-validation-md.py`)
   - Klasseliste (frå `generated/<domain>/<schema>/docs/index.md`, utan duplikat-overskrift)
   - Artefaktabell (`## Generated artifacts` med lenkjer til `.ttl`, `.json`, `.puml` osv.)
```

**Ny seksjons-rekkjefølgje:**
```
5. Generer `mkdocs/docs/<domain>/<schema>/index.md` med følgjande seksjons-rekkjefølgje:
   - Hovudoverskrift (`# <schema>`)
   - **Metadata-tabell** (`## Metadata` frå gen-doc — name, title, description, versjon, lisens, utgjevar, status osv.)
   - Publiseringsinfo (boks dersom `published-uris.lock` finst)
   - **ER-diagram** (`## ER-diagram` med PlantUML SVG — zoombart, lenke til full versjon)
   - Klasseliste (`## Classes`, `## Slots`, `## Enumerations`, `## Types` frå gen-doc)
   - Artefaktabell (`## Generated artifacts` med lenkjer til `.ttl`, `.json`, `.puml` osv.)
   - **Valideringsresultat** (`## Valideringsresultat` frå `validation/<versjon>/<policy>.json`)
   - **Versjonslog** (`## Versjonslog` frå `CHANGELOG.md`)
```

Oppdater "Viktige detaljar"-lista (linje ~149-155):

- Endre: "**Versjonslog** vert kopiert direkte frå ... inn i kollapsa `<details>`-blokk"
- Til: "**Versjonslog** vert kopiert direkte frå `CHANGELOG.md` som rein Markdown (ikkje kollapsa)"
- Legg til: "**Valideringsresultat** brukar rein Markdown med nummererte lister (ikkje `<details>`-blokkar)"
- Endre: "ER-diagram (frå `<schema>-erdiagram.md`, utan overskrift)"
- Til: "**ER-diagram** (PlantUML SVG — zoombart, lenke til full versjon med importerte klasser)"

## Test

```bash
# Regenerer artefaktar med oppdatert Jinja-template
make samt

# Publiser til mkdocs/docs/
make docs-publish

# Verifiser lokalt
cd mkdocs && mkdocs serve

# Sjekk:
# 1. Metadata-tabell inneheld name, title, description
# 2. Description er ikkje vist som overskrift før metadata-tabellen
# 3. ER-diagram viser PlantUML SVG (ikkje Mermaid) og kan zoomast i nettleser
# 4. Lenke til fullstendig diagram med importerte klasser er synleg
# 5. Endringshistorikk har formaterte overskrifter, lister og lenkjer (ikkje kollapsa)
# 6. Feil og åtvaringar har nummerering og formatert kode/target/melding (ikkje kollapsa)
# 7. Ingen <details>-blokkar i genererte index.md-filer
# 8. Seksjons-rekkjefølgje: Metadata → ER-diagram → Klasseliste → Artefaktar → Validering → Versjonslog
```

## Avhengigheiter

Ingen — alle endringar er isolerte til dokumentasjonsgenerering.

## Prioritet

Medium — forbetrar lesbarheit og metadata-fullstend, men påverkar ikkje funksjonalitet.
