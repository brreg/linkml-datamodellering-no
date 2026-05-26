# Plan: Eksempel i generert dokumentasjon (gen-doc --example-directory)

## Mål

Vise konkrete YAML-eksempel direkte på klassesidene i den genererte
dokumentasjonsportalen — slik at utviklar kan sjå korleis ein gyldig instans ser
ut utan å søkje opp eksempelfila separat.

LinkML `gen-doc` støttar dette via `--example-directory`-flagget, og
Jinja2-malen `class.md.jinja2` har allereie støtte for det (linje 290–299):

```jinja2
{% if gen.example_object_blobs(element.name) -%}
## Examples
{% for name, blob in gen.example_object_blobs(element.name) -%}
### Example: {{ name }}
```yaml
{{ blob }}
```
{% endfor %}
{% endif %}
```

Det einaste som manglar er (a) rett namngjeve filer per klasse og (b) at
`--example-directory` vert sendt til `gen-doc`.

---

## Bakgrunn og utfordring

### Kva `--example-directory` forventar

Gen-doc forventar éi fil per klasse-instans i katalogen, med konvensjonen:

```
<KlasseNamn>-<EksempelNamn>.yaml
```

Til dømes:

```
examples/docgen/oreg/register-over-aksjeeiere/
  Aksjeselskap-001.yaml
  Aksjeselskap-002.yaml
  Aksjekapital-001.yaml
  Aksjeeier-001.yaml
```

Kvar fil inneheld berre eitt objekt av den gjeldande klassen — ikkje ein
container med lister.

### Kva vi har i dag

Eksempelfilene våre er éi stor containerstrukturfil per skjema:

```yaml
# examples/oreg/register-over-aksjeeiere-eksempel.yaml
aksjeselskaper:
  - identifikator: aksje:Aksjeselskap1
    navn: Eksempel AS
    ...
aksjekapitaler:
  - identifikator: aksje:Aksjekapital1
    ...
```

Desse kan ikkje brukast direkte med `--example-directory` — dei må splittast
til individuelle per-klasse-filer.

### Interaksjon med `--no-render-imports`

Gjeldande `gen-doc`-kommando nyttar `--no-render-imports`, som betyr at klasser
frå importerte skjema ikkje får eigne sider i det gjeldande skjemaets docs.

Konsekvensar:

| Skjema | Lokale klasser (vises) | Importerte klasser (skjult) |
|---|---|---|
| `brreg-begrep` | `BegrepContainer` | `Begrep`, `Samling`, `Definisjon`, … |
| `register-over-aksjeeiere` | `Aksjeselskap`, `Aksjekapital`, `Aksje`, … | — (alle klasser er lokale) |
| `ngr-adresse` | `Adresse`, `Veg`, … | `Organisasjon`, … |
| `samt-bu` | `Skole`, `Barnehage`, … | `Kontaktopplysning`, … |

Eksempel vil berre visast på sider for **lokalt definerte klasser**. For
`brreg-begrep` er det praktisk talt berre `BegrepContainer` — det gir avgrensa
gevinst. Skjema med mange lokale klasser (oreg, ngr, samt, fint) gagnar mest.

---

## Løysingsarkitektur

### Tilnærming: auto-ekstraksjon + generert mappe

```
examples/<domain>/<schema>-eksempel.yaml   ← kjeldefil (eksisterande)
          │
          │  gen-docgen-examples.py
          ▼
generated/<domain>/<schema>/docgen-examples/
  <ClassName>-001.yaml
  <ClassName>-002.yaml
  …
          │
          │  gen-doc --example-directory
          ▼
generated/<domain>/<schema>/docs/
  klasser/<ClassName>.md   ← inneheld ## Examples-seksjon
```

`generated/`-mappa er ikkje sjekka inn i git (allereie i `.gitignore`).
Ekstraksjonsskriptet køyrer automatisk som del av `domain-gen-doc`-steget.

### Ekstraksjonslogikk

Skriptet (`src/assets/scripts/gen-docgen-examples.py`) gjer følgjande:

1. **Les skjema-YAML** — finn klassen med `tree_root: true`, les
   `attributes:`-nøklane og deira `range:`-verdiar:
   ```python
   # aksjeselskaper → Aksjeselskap
   # aksjekapitaler → Aksjekapital
   ```

2. **Les eksempel-YAML** — itererer over kvar toppnivånøkkel som samsvarar
   med eit container-attributt

3. **Skriv per-klasse-filer** — for kvart objekt i lista:
   ```
   Aksjeselskap-001.yaml, Aksjeselskap-002.yaml, …
   ```
   Fila inneheld berre det rå objektet (ikkje ein container).

4. **Namngjeving** — sekvensielt (`001`, `002`, …) som standard.
   Valfritt: bruk siste URL-segment frå `id:`-feltet dersom det finst og er
   kortare enn 40 teikn (t.d. `Aksjeselskap-Eksempel-AS.yaml`).

5. **Berre direkte attributtar** — berre container-attributtar vert ekstraherte.
   Nestede objekt (t.d. referansar som berre eksisterer som URI-strenger i
   eksempelfila) vert ikkje ekstraherte separat.

### Handskrivne overstyring

For klasser der den automatisk ekstraherte eksempelen ikkje er god nok (t.d.
for å vise fleire variasjonar eller eit pedagogisk eksempel), legg fila i:

```
src/linkml/<domain>/<schema>/examples/<ClassName>-<namn>.yaml
```

Desse vert kopierte inn i `generated/<domain>/<schema>/docgen-examples/` før
gen-doc køyrer og overstyrer auto-ekstraherte filer med same filnamn.

---

## Implementasjonsplan

### Steg 1 — Ekstraksjons-skript

**Fil:** `src/assets/scripts/gen-docgen-examples.py`

**Grensesnitt:**

```bash
python3 gen-docgen-examples.py \
  <schema.yaml>          \   # t.d. src/linkml/oreg/register-over-aksjeeiere/register-over-aksjeeiere-schema.yaml
  <eksempel.yaml>        \   # t.d. examples/oreg/register-over-aksjeeiere-eksempel.yaml
  <output-dir>               # t.d. generated/oreg/register-over-aksjeeiere/docgen-examples/
```

Skriptet nyttar berre stdlib (`yaml`, `pathlib`, `sys`) — ingen LinkML-avhengigheit.
Det køyrer difor i `$(PYTHON_IMAGE)` (allereie tilgjengeleg) utan ekstra pakkar.

**Pseudokode:**

```python
import yaml, sys
from pathlib import Path

schema_path, example_path, out_dir = sys.argv[1], sys.argv[2], Path(sys.argv[3])
out_dir.mkdir(parents=True, exist_ok=True)

schema = yaml.safe_load(open(schema_path))
example = yaml.safe_load(open(example_path))

# Finn container-attributtar → klasse-mapping
attr_to_class = {}
for cls_name, cls in (schema.get("classes") or {}).items():
    if isinstance(cls, dict) and cls.get("tree_root"):
        for attr_name, attr in (cls.get("attributes") or {}).items():
            if isinstance(attr, dict) and attr.get("range"):
                attr_to_class[attr_name] = attr["range"]

# Ekstraher per-klasse-filer
for attr_name, class_name in attr_to_class.items():
    instances = example.get(attr_name) or []
    for i, obj in enumerate(instances, start=1):
        slug = _slug(obj)  # siste URL-segment frå id: eller sekvensnr.
        filename = out_dir / f"{class_name}-{slug}.yaml"
        yaml.dump(obj, open(filename, "w"), allow_unicode=True, ...)
```

**Køyringsvilkår:** Skriptet gjer ingenting og avslutt med kode 0 dersom:
- Eksempelfila ikkje finst (schema har ingen eksempel)
- Skjemaet ikkje har ein `tree_root`-klasse med `attributes:`

### Steg 2 — Makefile: oppdater `run_gen_doc`

Gjeldande makro (linje 68–83) utvidas med eit pre-steg:

```makefile
define run_gen_doc
@$(foreach s,$(1), \
  echo "$(CLR_STEP)→ gen-docgen-examples  $(s)$(CLR_RST)" && \
  mkdir -p $(call schema_outdir,$(s))/docgen-examples && \
  $(PYTHON_RUN) python3 src/assets/scripts/gen-docgen-examples.py \
    $(s) \
    examples/$(call schema_domain,$(s))/$(call schema_name,$(s))-eksempel.yaml \
    $(call schema_outdir,$(s))/docgen-examples && \
  $(if $(wildcard src/linkml/$(call schema_domain,$(s))/$(call schema_name,$(s))/examples/*.yaml), \
    cp src/linkml/$(call schema_domain,$(s))/$(call schema_name,$(s))/examples/*.yaml \
       $(call schema_outdir,$(s))/docgen-examples/,) \
  echo "$(CLR_STEP)→ gen-doc  $(s)$(CLR_RST)" && \
  mkdir -p $(call schema_outdir,$(s))/docs && \
  $(LINKML_RUN) gen-doc \
    --template-directory src/templates/docgen \
    --no-mergeimports \
    --no-render-imports \
    --no-hierarchical-class-view \
    --diagram-type mermaid_class_diagram \
    --example-directory $(call schema_outdir,$(s))/docgen-examples \
    -d $(call schema_outdir,$(s))/docs $(s) && \
  sed -i '/Container/d' $(call schema_outdir,$(s))/docs/index.md; \
)
endef
```

`schema_domain` og `schema_name` er hjelpemakroane som allereie finst for
`schema_outdir`. Dersom dei ikkje finst, leggast dei til:

```makefile
schema_domain = $(word 3,$(subst /, ,$(1)))   # src/linkml/<domain>/...
schema_name   = $(word 4,$(subst /, ,$(1)))   # src/linkml/<domain>/<name>/...
```

**Merk:** `--example-directory` sendar ikkje feil viss mappa er tom eller ikkje
inneheld filer for gjeldande klasse — gen-doc hoppar stille over klasser utan
matchande filer.

### Steg 3 — `generate.yaml`-flagg (opt-out)

Legg til eit `docgen_examples`-flagg for skjema som ikkje skal ha eksempel
i dokumentasjonen:

```yaml
# generate.yaml
generators:
  ...
  example_rdf: true
docgen_examples: false    # slår av --example-directory for dette skjemaet
```

Standard: `true` (skriptet køyrer alltid, men gjer ingenting viss eksempelfila manglar).

I Makefile-makroen: sjekk flagget før `gen-docgen-examples`-steget køyrer:

```makefile
$(if $(shell grep -q '^docgen_examples: false' \
       src/linkml/$(call schema_domain,$(s))/$(call schema_name,$(s))/generate.yaml \
       2>/dev/null && echo 1),,\
  python3 src/assets/scripts/gen-docgen-examples.py ...)
```

### Steg 4 — Seksjonstittel i mal (valfri justering)

Gjeldande tittel i `class.md.jinja2` er `### Example: Aksjeselskap-001`.
Med slugging frå `id:` vert tittelen meir lesbar:
`### Example: Aksjeselskap-Eksempel-AS`.

Ingen malendring er strengt nødvendig for MVP — berre slugging-logikken i
skriptet bestemmer tittelen.

---

## Pilotskjema og prioritet

| Prioritet | Skjema | Lokale klasser | Estimert gevinst |
|---|---|---|---|
| 1 (pilot) | `oreg/register-over-aksjeeiere` | Aksjeselskap, Aksje, Aksjekapital, Aksjeeier, … | Høg — mange klasser, god eksempelfil |
| 2 | `samt/samt-bu` | Skole, Barnehage, Kontaktopplysning, … | Høg |
| 3 | `ngr/ngr-adresse` | Adresse, Vegadresse, Matrikkeladresse, … | Høg |
| 4 | `ngr/ngr-eiendom` | Eiendom, Matrikkeleining, … | Middels |
| 5 | `ngr/ngr-person` | Person, Familierelasjon, … | Middels |
| 6 | `fint/*` | Mange klasser per domene | Middels — sjå merknad |
| 7 | `begrep/brreg-begrep` | Berre `BegrepContainer` (lokalt) | Låg — avgrensa av `--no-render-imports` |

**FINT-merknad:** FINT-skjema er store og auto-ekstraksjonen vil generere mange
filer. Vurder `docgen_examples: false` som standard og hand-skrivne eksempel
for eit utval nøkkelklassar.

**`begrep`-merknad:** For å få eksempel på `Begrep`- og `Samling`-sidene i
`brreg-begrep`-dokumentasjonen, må anten (a) `--no-render-imports` fjernast for
det skjemaet, eller (b) eksempel leggjast i `skos-ap-no` sin example-directory
(lite naturleg). Dette er eit avansert steg og ikkje del av MVP.

---

## Tekniske detaljar og kanttilfelle

### Tom output-mappe

Gen-doc hoppar stille over `--example-directory` viss mappa ikkje inneheld
noka matchande fil — ingen feil. Makroen treng ikkje betre feilhandtering.

### Klasse-namntilsvar

Skriptet gjer ein enkel `schema.classes[container].attributes[attr].range`-oppslag.
Det handterer ikkje arv eller `slot_usage`-overstyring — men container-attributtane
er alltid `attributes:` (ikkje globale slots), så dette er tilstrekkeleg.

### Fleirspråklege strengar og `LangString`

YAML-instansar med `{language: nb, value: "..."}` vert skrivne as-is. Gen-doc
viser dei som rå YAML — ingen spesiell handtering nødvendig.

### AP-NO-profiler (ingen `tree_root`)

AP-NO-profilene (`dcat-ap-no`, `skos-ap-no`, …) har ingen `tree_root`-klasse.
Skriptet avslutt utan å skrive noko — ingen feil.

### Kollisjonshandtering

Dersom to instansar i same liste gir same slug (t.d. to objekt utan `id:`),
vert den andre skriven med suffiks `-b`, `-c`, osv., eller sekvensnummeret
nyttast som fallback.

---

## CI-implikasjonar

`domain-gen-doc` i `generate.yml` vil automatisk køyre ekstraksjonsskriptet som
del av gen-doc-steget. Ingen endringar i `generate.yml` er nødvendige — endring
skjer berre i `run_gen_doc`-makroen i Makefile.

Cache-nøkkelen for genererte artefakter i `generate.yml` baserer seg på
`hashFiles('src/linkml/{domain}/**')` og `examples/{domain}/**` — endringar i
eksempelfiler vil riktig nok utløyse regenerering.

---

## Referansar

- `src/templates/docgen/class.md.jinja2` linje 290–299 — eksisterande støtte
- LinkML gen-doc `--help` output:
  ```
  --example-directory TEXT  Folder in which example files are found.
                            These are used to make inline examples.
                            <ClassName>-<ExampleName>.<extension>
  ```
- `src/assets/scripts/` — plassering for skriptet
- Eksisterande eksempelfiler under `examples/<domain>/`
