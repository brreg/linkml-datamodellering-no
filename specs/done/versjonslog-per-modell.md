# Versjonslog per modell i dokumentasjonsportalen

## Bakgrunn

Release-please genererer `CHANGELOG.md` per modell basert på conventional commits når ein release-PR vert merga. Desse changelog-filene inneheld versjonert endringshistorikk (feat, fix, refactor osv.) og vert skrivne til kvar modellmappe (`src/linkml/<domain>/<modell>/CHANGELOG.md`).

**Problem:**
CHANGELOG-filene er **ikkje synlege i dokumentasjonsportalen**. Brukarar har ingen måte å sjå endringshistorikken for ein modell utan å gå til GitHub-repoet.

**Motivasjon:**
- Brukarar treng å sjå kva som har endra seg mellom versjonar
- CHANGELOG er ein viktig del av FAIR-prinsippa (Accessible, Reusable)
- Versjonslogen bør vere tilgjengeleg same stad som resten av modelldokumentasjonen

## Foreslått løysing

### 1. Kopier CHANGELOG.md til mkdocs-struktur

`mkdocs/publish.sh` skal kopiere `CHANGELOG.md` frå kvar modellmappe til `mkdocs/docs/<domain>/<modell>/CHANGELOG.md` (saman med resten av genererte artefaktar).

### 2. Legg til Versjonslog-seksjon i index.md med kollapsa innhald

`index.md` skal få ei ny `## Versjonslog`-seksjon **før** Metadata-tabellen. Heile CHANGELOG.md-innhaldet skal inkluderast i ein kollapsa `<details>`-blokk:

```markdown
# samt-bu

Beskrivelse...

## Versjonslog

<details>
<summary>Vis full endringshistorikk</summary>

<!-- CHANGELOG.md-innhald vert injisert her -->

</details>

## Metadata
| Felt | Verdi |
| --- | --- |
| Schema URI | [...] |
| Versjon | 1.0.0 |
| Lisens | [...] |
...

## Classes
...
```

**Fordeler:**
- Endringshistorikken er synleg tidleg i dokumentet
- Heile endringshistorikken er tilgjengeleg utan å måtte navigere til ein annan side
- Kollapsa som standard — tek ikkje opp plass før brukaren klikkar
- Standard HTML `<details>`-tag — fungerer i all Markdown-renderarar

### 3. Generer CHANGELOG.md programmatisk (valfritt)

**Problem med release-please-tilnærming:**
- CHANGELOG.md vert **berre** generert når ein release-PR vert merga
- Nye modellar som ikkje har hatt ein release enno har ingen CHANGELOG.md
- Endringar etter siste release er ikkje synlege i CHANGELOG før neste release

**Alternativ tilnærming:** Generer CHANGELOG.md programmatisk frå git-historikk for **alle** modellar, ikkje berre dei som har hatt ein release.

**Verkty:**
- `git-cliff` — rask Rust-basert changelog-generator med støtte for conventional commits
- `conventional-changelog` — Node.js-basert, mykje brukt
- Eigen Python-script basert på `git log --grep`

**Fordeler:**
- Alle modellar får CHANGELOG, ikkje berre dei som har hatt release
- Endringar etter siste release er synlege (fram til HEAD)
- Konsistent format på tvers av alle modellar

**Ulemper:**
- Meir komplekst — må finne commits som påverkar kvar modell
- Kan kome i konflikt med release-please sine CHANGELOG-filer

## Implementasjon

### Alternativ A: Bruk release-please sine CHANGELOG.md (enklast)

**Steg:**

1. **Oppdater `mkdocs/publish.sh` til å kopiere CHANGELOG.md**

   Finn seksjonen der `index.md` vert generert (rundt linje 134–244) og legg til kopiering av CHANGELOG.md:

   ```bash
   # Kopier CHANGELOG.md dersom den finst
   changelog_src="$REPO_ROOT/src/linkml/$domain/$schema/CHANGELOG.md"
   changelog_dst="$DOCS/$domain/$schema/CHANGELOG.md"
   if [ -f "$changelog_src" ]; then
       cp "$changelog_src" "$changelog_dst"
   fi
   ```

2. **Legg til lenke i metadata-tabell via Jinja-template**

   **Fil:** `src/assets/templates/docgen/index.md.jinja2`

   Legg til ny rad i metadata-tabellen rett etter Versjon:

   ```jinja2
   {% if schema.version -%}
   | Versjon | {{ schema.version }} |
   | Versjonslog | [CHANGELOG.md](CHANGELOG.md) |
   {% endif -%}
   ```

   **Problem:** Jinja-templaten veit **ikkje** om CHANGELOG.md finst eller ikkje — den vil alltid generere lenka.

   **Løysing:** Post-prosesser `index.md` for å fjerne lenka dersom CHANGELOG.md ikkje finst:

   ```bash
   # Fjern Versjonslog-rad dersom CHANGELOG.md ikkje finst
   if [ ! -f "$REPO_ROOT/src/linkml/$domain/$schema/CHANGELOG.md" ]; then
       sed -i '/| Versjonslog |/d' "$out/index.md"
   fi
   ```

3. **Test med ein modell som har CHANGELOG.md**

   Køyr release-please manuelt for ein modell (eller vent til neste release), og verifiser at:
   - `CHANGELOG.md` finst i `src/linkml/<domain>/<modell>/`
   - `mkdocs/docs/<domain>/<modell>/CHANGELOG.md` finst etter `make docs-publish`
   - `index.md` har lenke til `CHANGELOG.md`

**Fordeler:**
- Enklast å implementere
- Konsistent med GitHub Releases (same CHANGELOG)
- Ingen duplikat datakilder

**Ulemper:**
- Fungerer **berre** for modellar som har hatt minst éin release
- Nye modellar eller modellar mellom releases har ingen CHANGELOG

---

### Alternativ B: Generer CHANGELOG.md programmatisk frå git-historikk

**Verkty:** `git-cliff` (anbefalt)

**Installasjon:**
```dockerfile
# Legg til i Dockerfile.linkml eller eigen Dockerfile.git-cliff
RUN curl -sSL https://github.com/orhun/git-cliff/releases/download/v2.8.1/git-cliff-2.8.1-x86_64-unknown-linux-gnu.tar.gz | \
    tar xz -C /usr/local/bin git-cliff
```

**Konfigurasjon:** `cliff.toml` i repo-rota

```toml
[changelog]
header = """
# Changelog\n
All notable changes to this project will be documented in this file.\n
"""
body = """
{% for group, commits in commits | group_by(attribute="group") %}
    ### {{ group | upper_first }}
    {% for commit in commits %}
        - {{ commit.message | split(pat="\n") | first | trim }}\
          {% if commit.scope %}({{ commit.scope }}){% endif %}\
    {% endfor %}
{% endfor %}
"""

[git]
conventional_commits = true
filter_commits = true
commit_parsers = [
  { message = "^feat", group = "Features" },
  { message = "^fix", group = "Bug Fixes" },
  { message = "^refactor", group = "Refactoring" },
  { message = "^perf", group = "Performance" },
  { message = "^docs", skip = true },
  { message = "^chore", skip = true },
  { message = "^ci", skip = true },
  { message = "^test", skip = true },
  { message = "^style", skip = true },
]
```

**Script:** `src/assets/scripts/generate-changelog.sh`

```bash
#!/usr/bin/env bash
# Generer CHANGELOG.md for ein modell basert på git-historikk.
# Bruk: generate-changelog.sh <modell-path>
set -euo pipefail

SCHEMA_PATH="${1:-}"
if [ -z "$SCHEMA_PATH" ]; then
    echo "Bruk: $0 <schema-path>" >&2
    exit 1
fi

DOMAIN=$(echo "$SCHEMA_PATH" | cut -d/ -f3)
MODEL=$(echo "$SCHEMA_PATH" | cut -d/ -f4)
MODEL_DIR="src/linkml/$DOMAIN/$MODEL"
OUTPUT="$MODEL_DIR/CHANGELOG.md"

# Finn alle commits som påverkar denne modellen
# Filtrér på commits som endrar filer i modell-mappa
git cliff \
    --config cliff.toml \
    --include-path "$MODEL_DIR/**" \
    --output "$OUTPUT"

echo "Generert $OUTPUT"
```

**Integrasjon i Makefile:**

```makefile
# Generer CHANGELOG.md for alle modellar
gen-changelogs:
	@$(foreach s,$(ALL_SCHEMAS), \
	  bash src/assets/scripts/generate-changelog.sh $(s); \
	)

# Generer CHANGELOG.md for éin modell
gen-changelog:
	@test -n "$(SCHEMA)" || (echo "Bruk: make gen-changelog SCHEMA=<sti>"; exit 1)
	bash src/assets/scripts/generate-changelog.sh "$(SCHEMA)"
```

**Fordeler:**
- Alle modellar får CHANGELOG, ikkje berre dei med release
- Endringar fram til HEAD er synlege (ikkje berre til siste release)
- Kan køyrast automatisk som del av `make gen-docs`

**Ulemper:**
- Meir komplekst — ny avhengighet (`git-cliff`)
- Kan kome i konflikt med release-please sine CHANGELOG-filer
- Krev at commits følgjer conventional commits-format

---

### Alternativ C: Hybrid — bruk release-please + git-cliff for unreleased

**Strategi:**
1. Dersom `CHANGELOG.md` finst (frå release-please), bruk den
2. Dersom den **ikkje** finst, generer ein midlertidig CHANGELOG med `git-cliff`
3. Kopier til mkdocs

**Fordeler:**
- Best of both worlds — release-please for offisielle releases, git-cliff for mellomversjoner
- Alle modellar får CHANGELOG

**Ulemper:**
- Mest komplekst å implementere
- To ulike kjelder for CHANGELOG kan skape inkonsistens

---

## Anbefalt tilnærming

**Fase 1 (minimum viable):** Alternativ A — bruk release-please sine CHANGELOG.md

1. Kopier CHANGELOG.md til mkdocs i `publish.sh`
2. Legg til lenke i metadata-tabell via Jinja-template
3. Fjern lenka dersom CHANGELOG.md ikkje finst (post-prosessering)

**Fase 2 (valfri):** Alternativ B — generer CHANGELOG.md programmatisk

1. Legg til `git-cliff` i Dockerfile
2. Lag `cliff.toml`-konfigurasjon
3. Lag `generate-changelog.sh`-script
4. Integrer i `make gen-docs` eller `make gen-changelogs`

---

## Steg (Alternativ A)

### 1. Oppdater `mkdocs/publish.sh` til å kopiere CHANGELOG.md

**Fil:** `mkdocs/publish.sh`

Finn seksjonen der filer vert kopierte til `$DOCS/$domain/$schema/` (rundt linje 120–130) og legg til:

```bash
# Kopier CHANGELOG.md dersom den finst
changelog_src="$REPO_ROOT/src/linkml/$domain/$schema/CHANGELOG.md"
if [ -f "$changelog_src" ]; then
    cp "$changelog_src" "$DOCS/$domain/$schema/CHANGELOG.md"
fi
```

### 2. Legg til Versjonslog-seksjon i Jinja-template

**Fil:** `src/assets/templates/docgen/index.md.jinja2`

Legg til ny `## Versjonslog`-seksjon **før** metadata-tabellen:

```jinja2
{% if schema.description %}{{ schema.description }}{% endif %}

## Versjonslog

<details>
<summary>Vis full endringshistorikk</summary>

<!-- CHANGELOG_PLACEHOLDER -->

</details>

## Metadata

| Felt | Verdi |
| --- | --- |
{% if schema.id -%}
| Schema URI | [{{ schema.id }}]({{ schema.id }}) |
{% endif -%}
```

**Plassering:** Rett etter `{{ schema.description }}` (linje ~3–4), **før** `## Metadata` (linje ~5).

**Merk:** `<!-- CHANGELOG_PLACEHOLDER -->` vil bli erstatta med CHANGELOG.md-innhald i post-prosessering.

### 3. Post-prosesser index.md for å injisere CHANGELOG.md-innhald eller fjerne seksjonen

**Fil:** Python-script `src/assets/scripts/inject-changelog-in-index.py`

```python
#!/usr/bin/env python3
"""
Injiser CHANGELOG.md-innhald i index.md sin ## Versjonslog-seksjon.
Dersom CHANGELOG.md ikkje finst, fjern heile ## Versjonslog-seksjonen.

Usage:
    inject-changelog-in-index.py <index.md> <changelog.md>
"""
import sys
from pathlib import Path

def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <index.md> <changelog.md>", file=sys.stderr)
        sys.exit(1)

    index_path = Path(sys.argv[1])
    changelog_path = Path(sys.argv[2])

    # Les index.md
    content = index_path.read_text(encoding="utf-8")

    # Sjekk om CHANGELOG.md finst
    if changelog_path.exists():
        # Les CHANGELOG.md og injiser i placeholder
        changelog_content = changelog_path.read_text(encoding="utf-8")
        # Fjern hovudoverskrift frå CHANGELOG (# Changelog) dersom den finst
        if changelog_content.startswith("# Changelog"):
            changelog_content = "\n".join(changelog_content.split("\n")[1:]).lstrip()
        
        content = content.replace("<!-- CHANGELOG_PLACEHOLDER -->", changelog_content)
    else:
        # Fjern heile ## Versjonslog-seksjonen dersom CHANGELOG ikkje finst
        lines = content.split("\n")
        new_lines = []
        skip = False
        for line in lines:
            if line.strip() == "## Versjonslog":
                skip = True
            elif skip and line.startswith("## ") and not line.startswith("## Versjonslog"):
                skip = False
            
            if not skip:
                new_lines.append(line)
        
        content = "\n".join(new_lines)

    # Skriv tilbake
    index_path.write_text(content, encoding="utf-8")

if __name__ == "__main__":
    main()
```

**Integrasjon i Makefile (`run_gen_doc`):**

```makefile
define run_gen_doc
  ...
  $(LINKML_RUN) gen-doc ... && \
  $(PYTHON_RUN) python3 src/assets/scripts/inject-changelog-in-index.py \
    $(call schema_outdir,$(s))/docs/index.md \
    src/linkml/$(call schema_domain,$(s))/$(call schema_name,$(s))/CHANGELOG.md && \
  sed -i '/Container/d' $(call schema_outdir,$(s))/docs/index.md; \
  ...
endef
```

### 4. Test

1. Køyr release-please for ein modell (eller vent til neste release)
2. Verifiser at `src/linkml/<domain>/<modell>/CHANGELOG.md` finst
3. Køyr `make docs-publish`
4. Verifiser at `mkdocs/docs/<domain>/<modell>/CHANGELOG.md` finst
5. Verifiser at `index.md` har lenke til CHANGELOG.md
6. Verifiser at modellar **utan** CHANGELOG.md ikkje har lenka

---

## Avhengigheiter

- Release-please må ha køyrt minst éin gong for kvar modell (Alternativ A)
- `git-cliff` må installerast (Alternativ B)
- `cliff.toml`-konfigurasjon (Alternativ B)

---

## Prioritet

**Middels** — forbetrar dokumentasjon og transparency, men ikkje kritisk for kjernefunksjonalitet.

---

## Handlingsliste (Alternativ A)

- [x] Oppdater `mkdocs/publish.sh` til å kopiere CHANGELOG.md
  - [x] Legg til kopiering i schema-loop (etter artefakt-kopiering)
- [x] Legg til `## Versjonslog`-seksjon direkte i `publish.sh`
  - [x] Plasser **før** klasseliste (som inneheld `## Metadata`)
  - [x] Legg til `<details>`-blokk med CHANGELOG.md-innhald direkte
- [x] Flytt `## Valideringsresultat` til rett etter `## Versjonslog`
  - [x] Fjern duplikat Valideringsresultat-seksjon etter artefaktabell
- [x] Test med ein modell som har CHANGELOG.md (samt-bu)
- [x] Test med ein modell som **ikkje** har CHANGELOG.md (common)
- [ ] Oppdater navigasjon i `mkdocs.yml` dersom nødvendig (valfritt)

## Utført

**Endringar gjennomførte:**

1. **`mkdocs/publish.sh`** (linje 106–112):
   - Kopier CHANGELOG.md frå `src/linkml/<domain>/<schema>/` til `mkdocs/docs/<domain>/<schema>/`

2. **`mkdocs/publish.sh`** (linje 174–187):
   - Legg til `## Versjonslog`-seksjon med kollapsa `<details>`-blokk
   - Inkluder heile CHANGELOG.md-innhald direkte (ikkje placeholder)
   - Fjern hovudoverskrift (`# Changelog`) frå CHANGELOG
   - Seksjon vert **ikkje** lagt til dersom CHANGELOG.md manglar

3. **`mkdocs/publish.sh`** (linje 189–221):
   - Flytta `## Valideringsresultat` til rett etter `## Versjonslog`
   - Fjerna duplikat Valideringsresultat-seksjon (tidlegare linje 256–285)

**Resulterande struktur i `index.md`:**

```markdown
# samt-bu

Ontodia-vennlig LinkML-modell for skoler

<ER-diagram>

## Versjonslog

<details>
<summary>Vis full endringshistorikk</summary>

## [1.0.4](...) (2026-07-02)
...

</details>

## Valideringsresultat

*Siste validering: 2026-07-03 — v1.0.0 — policy: silver*
...

## Metadata

| Felt | Verdi |
| --- | --- |
| Schema URI | https://data.norge.no/samt/samt-bu |
...

## Classes
...
```

**Testing:**
- ✅ `samt-bu`: Har CHANGELOG.md → `## Versjonslog` vises med kollapsa innhald
- ✅ `common`: Har **ikkje** CHANGELOG.md → `## Versjonslog` vises **ikkje**
- ✅ Rekkjefølgje: Versjonslog → Valideringsresultat → Metadata → Classes

---

## Visuell struktur

Slik vil `index.md` sjå ut med `## Versjonslog` **før** `## Metadata`:

```markdown
# samt-bu

Ontodia-vennlig LinkML-modell for skoler

## Versjonslog

<details>
<summary>Vis full endringshistorikk</summary>

## [1.0.4](https://github.com/.../compare/samt-bu-v1.0.3...samt-bu-v1.0.4) (2026-06-10)

### Bug Fixes

* **samt-bu:** rette feil i Kontaktlaerer-klasse ([abc1234](...))

## [1.0.3](https://github.com/.../compare/samt-bu-v1.0.2...samt-bu-v1.0.3) (2026-05-15)

### Features

* **samt-bu:** legg til Fylke-klasse ([def5678](...))

</details>

## Metadata

| Felt | Verdi |
| --- | --- |
| Schema URI | https://data.norge.no/samt/samt-bu |
| Versjon | 1.0.4 |
| Lisens | https://data.norge.no/nlod/no/2.0 |
...

## Classes
...
```

**Fordeler:**
- Heile endringshistorikken er tilgjengeleg utan å måtte navigere til ein annan side
- Kollapsa som standard — tek ikkje opp plass før brukaren klikkar
- Standard HTML `<details>`-tag — fungerer i mkdocs og all Markdown-renderarar
- Release-lenker og commit-hashar er klikkbare

**Ulemper:**
- Kan bli stor for modellar med mange versjonar (men kollapsa som standard)
- Meir prosessering nødvendig (men berre éin gong per `make gen-docs`)

---

## Eksempel: CHANGELOG.md frå release-please

```markdown
# Changelog

## [1.0.4](https://github.com/brreg/linkml-datamodellering-no/compare/samt-bu-v1.0.3...samt-bu-v1.0.4) (2026-06-10)

### Bug Fixes

* **samt-bu:** rette feil i Kontaktlaerer-klasse ([abc1234](https://github.com/brreg/linkml-datamodellering-no/commit/abc1234))

## [1.0.3](https://github.com/brreg/linkml-datamodellering-no/compare/samt-bu-v1.0.2...samt-bu-v1.0.3) (2026-05-15)

### Features

* **samt-bu:** legg til Fylke-klasse ([def5678](https://github.com/brreg/linkml-datamodellering-no/commit/def5678))
```

---

## Neste steg

Etter implementering:
1. Vurder om CHANGELOG.md også skal inkluderast i GitHub Releases-artefaktar
2. Vurder om CHANGELOG.md skal visast i navigasjonsmenyen i mkdocs
3. Evaluer om Alternativ B (git-cliff) gir meirverdi for modellar mellom releases
