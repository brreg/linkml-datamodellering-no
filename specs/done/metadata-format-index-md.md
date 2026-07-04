# Juster metadata-format i index.md for enkeltmodellar

## Bakgrunn

`index.md` per skjema vert generert i `mkdocs/publish.sh` ved å kombinere:
1. `gen-doc`-output frå LinkML (brukar Jinja-template `src/assets/templates/docgen/index.md.jinja2`)
2. Postprosessering i `publish.sh` (ER-diagram, artefakt-tabell, valideringsresultat)

Metadata-tabellen i Jinja-templaten treng tre justeringar:

1. **Status** — no vert ADMS Status URI oversatt til norsk tekst (t.d. `http://purl.org/adms/status/UnderDevelopment` → "Under utarbeidelse"). Brukaren ønskjer at **URI-en vert kopiert direkte** utan oversetting, slik at konsumentar kan bruke URI-en programmatisk.

2. **Validation policy** — brukaren ønskjer at `validation_policy` **ikkje skal vere synleg i metadata-tabellen**. Dette feltet vert injisert via `src/assets/scripts/inject-validation-policy.py` (post-prosessering etter `gen-doc`). For å fjerne det, må me kommentere ut/fjerne kallet til scriptet i Makefile sitt `run_gen_doc`.

3. **Imports** — no vert alle imports skrivne på éi linje separerte med komma (`schema.imports|join(', ')`). Brukaren ønskjer **linjeskift mellom kvar import**, slik at lista vert meir lesbar.

## Påverka filer

- `src/assets/templates/docgen/index.md.jinja2` — Jinja-template for `index.md`
- `mkdocs/publish.sh` — køyrer `gen-doc` som brukar templaten (ingen endringar nødvendig her)
- `generated/*/index.md` — alle genererte index.md-filer vert oppdaterte når `make gen-docs` køyrer

## Steg

### 1. Endre Status-feltet til å vise URI direkte

**Fil:** `src/assets/templates/docgen/index.md.jinja2`

**Før:**
```jinja2
{% if schema.annotations and schema.annotations.status -%}
{%- set status_map = {
  'http://purl.org/adms/status/UnderDevelopment': 'Under utarbeidelse',
  'http://purl.org/adms/status/Completed': 'Ferdigstilt',
  'http://purl.org/adms/status/Deprecated': 'Foreldet',
  'http://purl.org/adms/status/Withdrawn': 'Trukket tilbake'
} -%}
{%- set status_uri = schema.annotations.status.value -%}
{%- set status_text = status_map.get(status_uri, status_uri) -%}
| Status | {{ status_text }} |
{% endif -%}
```

**Etter:**
```jinja2
{% if schema.annotations and schema.annotations.status -%}
| Status | {{ schema.annotations.status.value }} |
{% endif -%}
```

**Grunngjeving:** Fjern `status_map`-ordbok og vis `status.value` direkte. Dette gjer at konsumentar får ADMS Status URI som kan brukast programmatisk.

### 2. Fjern Validation policy frå metadata-tabell

`validation_policy` vert injisert i metadata-tabellen av `src/assets/scripts/inject-validation-policy.py`, som køyrer **etter** `gen-doc` i Makefile sitt `run_gen_doc`.

**Finn kallet i Makefile:**

```bash
grep -n "inject-validation-policy" Makefile
```

**Finn relevant seksjon i `run_gen_doc`:**

```makefile
define run_gen_doc
  ...
  $(LINKML_RUN) gen-doc ... && \
  $(PYTHON_RUN) python3 src/assets/scripts/inject-validation-policy.py \
    $(call schema_outdir,$(s))/docs/index.md \
    src/linkml/$(call schema_domain,$(s))/$(call schema_name,$(s))/manifest.yaml && \
  sed -i '/Container/d' $(call schema_outdir,$(s))/docs/index.md; \
  ...
endef
```

**Handling:** Kommenter ut eller fjern kallet til `inject-validation-policy.py` i `run_gen_doc`-definisjonen.

**Etter endring:**

```makefile
define run_gen_doc
  ...
  $(LINKML_RUN) gen-doc ... && \
  # $(PYTHON_RUN) python3 src/assets/scripts/inject-validation-policy.py ... && \
  sed -i '/Container/d' $(call schema_outdir,$(s))/docs/index.md; \
  ...
endef
```

**Resultat:** `validation_policy` vil ikkje lenger vere synleg i metadata-tabellen.

### 3. Legg til linjeskift mellom kvar import

**Fil:** `src/assets/templates/docgen/index.md.jinja2`

**Før:**
```jinja2
{% if schema.imports -%}
| Imports | {{ schema.imports|join(', ') }} |
{% endif -%}
```

**Etter:**
```jinja2
{% if schema.imports -%}
| Imports | {% for imp in schema.imports %}{{ imp }}{% if not loop.last %}<br>{% endif %}{% endfor %} |
{% endif -%}
```

**Grunngjeving:** Bruk `<br>`-tag for linjeskift i Markdown-tabell. Iterér over `schema.imports` og legg til `<br>` mellom kvart element (ikkje etter siste).

### 4. Regenerer dokumentasjon

Køyr `gen-docs` for å regenerere alle `index.md`-filer med nye metadata-format:

```bash
make gen-docs
```

Verifiser at endra skjema har korrekt format:

```bash
# Sjekk at Status no viser URI direkte
grep "Status" mkdocs/docs/samt/samt-bu/index.md

# Sjekk at Imports har linjeskift
grep -A 3 "Imports" mkdocs/docs/ap-no/dcat-ap-no/index.md
```

### 5. Publiser til mkdocs

Køyr `docs-publish` for å kopiere oppdaterte filer til `mkdocs/docs/`:

```bash
make docs-publish
```

Verifiser at endringane er synlege i portalen:

```bash
make docs-serve
# Naviger til http://localhost:8000/ap-no/dcat-ap-no/ og sjekk metadata-tabell
```

## Avhengigheiter

Ingen — endringane er isolerte til Jinja-templaten.

## Prioritet

**Middels** — forbetrar lesbarheit og maskinlesbarheit av metadata, men bryt ikkje eksisterande funksjonalitet.

## Handlingsliste

- [x] Steg 1: Endre Status-feltet til å vise URI direkte (fjern status_map i index.md.jinja2)
- [x] Steg 2: Fjern Validation policy (kommenter ut inject-validation-policy.py i Makefile)
- [x] Steg 3: Legg til linjeskift mellom kvar import (bruk `<br>` i index.md.jinja2)
- [x] Steg 4: Køyr `make gen-docs` for å regenerere index.md (testa med samt-bu)
- [ ] Steg 5: Køyr `make docs-publish` og verifiser i lokal mkdocs-server

## Utført

**Endringar gjennomførte:**

1. **Status-feltet** (`src/assets/templates/docgen/index.md.jinja2`):
   - Fjerna `status_map`-ordbok (linje 22–27)
   - Endret frå `{{ status_text }}` til `[{{ schema.annotations.status.value }}]({{ schema.annotations.status.value }})`
   - **Resultat:** Status viser no URI som **klikkbar lenke** (t.d. `[http://purl.org/adms/status/UnderDevelopment](http://...)`)

2. **Validation policy** (`Makefile`):
   - Fjerna kall til `inject-validation-policy.py` frå `run_gen_doc` (linje 102–104)
   - **Resultat:** Validation policy er ikkje lenger synleg i metadata-tabellen

3. **Imports** (`src/assets/templates/docgen/index.md.jinja2`):
   - Endra frå `{{ schema.imports|join(', ') }}` til Jinja-loop med `<br>`-separator
   - **Resultat:** Kvar import vises på eiga linje i tabellcella

**Testing:**
- samt-bu: ✅ Status = klikkbar URI, ✅ ingen Validation policy, ✅ Imports med linjeskift
- referanse: ✅ Status = klikkbar URI, ✅ ingen Validation policy, ✅ ingen Imports-rad (korrekt)

**Oppfølging:**
Status-feltet vart oppdatert til å vere klikkbar lenke (same format som Utgjevar) etter tilbakemelding frå brukaren.
