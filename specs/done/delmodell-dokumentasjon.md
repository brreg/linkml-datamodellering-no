# Delmodell-dokumentasjon i portalen

## Bakgrunn

Repoet har no delmodell-hierarki:
- `dqv-core-schema` er ein delmodell av `dqv-ap-no-schema`
- `modelldcat-modell-schema` og `modelldcat-katalog-schema` er delmodellar av `modelldcat-ap-no-schema`

Delmodellane ligg i same kjeldekode-katalog som hovudmodellen (t.d. `src/linkml/ap-no/dqv-ap-no/`) men genererast til separate artefakt-katalogar (`generated/ap-no/dqv-core/`).

Dokumentasjonsportalen har i dag ingen mekanisme for å:
1. Vise delmodell-relasjonar i nav-menyen (hovudmodell → delmodell-hierarki)
2. Vise på `index.md` om ein modell **har** delmodellar (liste dei) eller **er** ein delmodell (peike til hovudmodellen)

## Mål

**Nav-meny:** delmodellar skal vere innrykka undermenypunkt under hovudmodellen:

```
ap-no:
  - dqv-ap-no
    - dqv-core          ← delmodell innrykka under hovudmodell
  - modelldcat-ap-no
    - modelldcat-modell ← delmodell
    - modelldcat-katalog ← delmodell
```

**index.md for hovudmodell** skal vise liste over delmodellar (dersom dei finst):

```markdown
## Delmodellar

Denne modellen er delt i fleire delmodellar:
- [dqv-core](../dqv-core/): DQV-kjerneklassar (utan DCAT-avhengigheit)
```

**index.md for delmodell** skal vise lenke til hovudmodellen:

```markdown
> **Delmodell av:** [dqv-ap-no](../dqv-ap-no/)
```

## Løysing

### 1. Legg til `submodels`-felt i manifest

Hovudmodell-manifest (`src/linkml/<domain>/<hovudmodell>/manifest.yaml`) får nytt valfritt felt:

```yaml
validation_policy: gold
submodels:
  - dqv-core

generators:
  ...
```

**Eksempel** (`src/linkml/ap-no/dqv-ap-no/manifest.yaml`):

```yaml
validation_policy: gold
submodels:
  - dqv-core

generators:
  jsonld_context: true
  ...
```

**Eksempel** (`src/linkml/ap-no/modelldcat-ap-no/manifest.yaml`):

```yaml
validation_policy: gold
submodels:
  - modelldcat-modell
  - modelldcat-katalog

generators:
  ...
```

**Namngjevingsregel:** `submodels`-verdiane skal vere `name:`-feltet frå delmodell-skjemaet (t.d. `dqv-core`, `modelldcat-modell`), **ikkje** filnamnet eller katalognamnet.

**Merk:** Delmodellane har **ikkje** eigne manifest-filer — dei ligg i same katalog som hovudmodellen og vert oppdaga automatisk av Makefile via `*-schema.yaml`-mønster.

### 2. Utvid `mkdocs/publish.sh` til å handtere delmodell-hierarki

**Steg 2 (generering per skjema):**
- Les `manifest.yaml` og ekstraher `submodel_of`-verdi (om den finst)
- Dersom delmodell: generer **delmodell-boks** i `index.md`:

```markdown
> **Delmodell av:** [<hovudmodell-title>](../<hovudmodell-schema>/)
```

Boksen plasserast **etter metadata-tabell, før publiseringsinfo-boks** (om den finst).

**Steg 3 (hovudmodell-undersøking):**
- Etter at alle skjema er prosesserte: bygg map `HOVEDMODELL_SUBMODELLER[<hovudmodell-namn>]="<delmodell1> <delmodell2> ..."`
- Legg til **Delmodellar-seksjon** i hovudmodellen sitt `index.md`:

```markdown
## Delmodellar

Denne modellen er delt i fleire delmodellar:

- [<delmodell-title>](../<delmodell-schema>/): <delmodell-description>
```

Seksjonen plasserast **etter metadata-tabell og publiseringsinfo, før ER-diagram**.

**Steg 4 (mkdocs.yml nav-generering):**
- Endre loop (linje 390-398) til å handtere delmodell-hierarki:

```bash
for schema in $schemas_str; do
    if [[ -n "${SCHEMA_SUBMODEL_OF[$schema]:-}" ]]; then
        # Delmodell — ikkje legg til her, vert lagt til under hovudmodell
        continue
    fi
    
    echo "      - '${schema}': ${domain}/${schema}/index.md"
    
    # Legg til delmodellar innrykka under hovudmodell
    submodels="${HOVEDMODELL_SUBMODELLER[$schema]:-}"
    for sub in $submodels; do
        echo "          - '${sub}': ${domain}/${sub}/index.md"
    done
done
```

### 3. Implementasjonsdetaljar

**Manifest-parsing:**
Bruk `yq`-verktøyet (allereie tilgjengeleg i CI) til å lese `submodel_of`:

```bash
submodel_of=$(yq eval '.submodel_of // ""' "$MANIFEST" 2>/dev/null || echo "")
```

**Map-struktur:**
```bash
declare -A SCHEMA_SUBMODEL_OF      # [schema-namn] -> hovudmodell-namn
declare -A HOVEDMODELL_SUBMODELLER # [hovudmodell-namn] -> "sub1 sub2 ..."
```

**Lenke-format:**
- Delmodell → hovudmodell: `[<title>](../<schema>/)`
- Hovudmodell → delmodell: `[<title>](../<schema>/): <description>`

**Fallback dersom `title`/`description` manglar:**
- Bruk `name:`-feltet frå skjemaet
- Hent via `yq eval '.title // .name' <schema>.yaml`

## Problem med dublett-katalogar

Etter implementasjon av delmodell-dokumentasjon vart det oppdaga eit **generelt problem** med repoets genererings- og publiseringsflyt:

**Makefile genererar både:**
- `generated/<domain>/<namn>/` frå `examples/<namn>-eksempel.yaml` (validerte instansdata)
- `generated/<domain>/<namn>-schema/` frå `<namn>-schema.yaml` (skjema-artefaktar)

**For domenemodeller** (NGR, OREG, SAMT) er dette riktig — dei har eigne eksempelfiler og treng separate data- og skjema-katalogar.

**For AP-NO-profilar** (som ikkje har `tree_root`-containerklasse) vert **begge** katalogane genererte frå same kjeldekatalog, men `-schema`-katalogen vert nesten tom (berre `diagrams/`). Dette skapar **dublettside**r i dokumentasjonsportalen (`dqv-ap-no` og `dqv-ap-no-schema`), der `-schema`-sida har ugyldig importveg og manglande innhald.

**Løysing:** La til filterlogikk i `mkdocs/publish.sh` som hoppar over `-schema`-katalogar dersom tilsvarande katalog **utan** `-schema`-suffiks finst i same domene. Dette filtrerer vekk dublettane utan å påverke domenemodell-katalogar.

## Utført

Implementert med følgjande endringar:

**Manifest-utvidingar:**
- La til `submodels: [dqv-core]` i `src/linkml/ap-no/dqv-ap-no/manifest.yaml`
- La til `submodels: [modelldcat-modell, modelldcat-katalog]` i `src/linkml/ap-no/modelldcat-ap-no/manifest.yaml`

**Ny seksjonsfil:**
- `mkdocs/lib/sections/submodel_info.sh` med to funksjonar:
  - `generate_submodel_box()`: genererer "Delmodell av"-boks for delmodellar
  - `generate_submodels_section()`: genererer "Delmodellar"-seksjon for hovudmodellar

**`mkdocs/lib/generate_index.sh`:**
- La til kall til `generate_submodel_box()` etter `generate_metadata()`
- La til kall til `generate_submodels_section()` før `generate_er_diagram()`

**`mkdocs/publish.sh`:**
- **Steg 1.5** (ny): bygg `SCHEMA_PARENT_MODEL` og `SCHEMA_SUBMODELS`-map frå manifest-filer
  - Brukar komma-separering i serialisering for å unngå konflikt med mellomrom i delmodell-namn
  - Serialiserer map til `SCHEMA_PARENT_MODEL_SERIALIZED` og `SCHEMA_SUBMODELS_SERIALIZED` for eksport til subshells
- **Steg 2** (schema-loop): filtrer vekk `-schema`-dublettar (hoppar over `<namn>-schema/` dersom `<namn>/` finst)
- **Steg 2** (`process_schema()`): deserialisér map og sett `PARENT_MODEL` og `SUBMODELS` miljøvariablar før `generate_schema_index()`
- **Steg 4** (nav-generering): hopp over delmodellar i hovudloop, legg dei inn innrykka under hovudmodell

**Dokumentasjon:**
- Oppdaterte `mkdocs/docs/manifest-config.md` med dokumentasjon av `submodels`-felt, inkludert brukstilfelle og døme

**Test:**
- Køyrde `bash mkdocs/publish.sh` — ingen feil
- Verifiserte nav-struktur i `mkdocs/mkdocs.yml`:
  - `dqv-core` innrykka under `dqv-ap-no` ✓
  - `modelldcat-modell` og `modelldcat-katalog` innrykka under `modelldcat-ap-no` ✓
- Verifiserte `index.md`:
  - `dqv-ap-no/index.md` viser "Delmodellar"-seksjon med lenke til `dqv-core` ✓
  - `modelldcat-ap-no/index.md` viser begge delmodellane ✓
  - `dqv-core/index.md` viser "Delmodell av"-boks med lenke til `dqv-ap-no` ✓
  - `modelldcat-katalog/index.md` viser "Delmodell av"-boks med lenke til `modelldcat-ap-no` ✓
