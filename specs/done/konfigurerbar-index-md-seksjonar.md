# Konfigurerbare seksjons-kjelder i index.md

## Bakgrunn

`mkdocs/publish.sh` genererer `index.md` for kvar modell ved å samle innhald frå fleire kjelder. Nokre av desse kjeldene er hardkoda i shellscriptet (`get_external_spec_url()`, Quickstart-logikk), medan andre er dokumenterte som eksplisitte parsingar (`generate-validation-md.py`, gen-doc-ekstraksjon).

Brukaren ønsker at alle overskrifter i `index.md` skal ha ei eksplisitt, transparent kjelde som kan endrast utan å måtte redigere shellscriptet. Dette gjer det enklare for domene-eigarar å tilpasse innhald, og gjer datakjelda tydeleg.

## Mål

1. **Dokumentere "Kontakt"-seksjonen** — klargjere i `index-md-struktur.md` at denne vert generert frå `CODEOWNERS.md`
2. **Konfigurerbar "Offisiell referanse"** — flytt hardkoda URL-ar til `manifest.yaml` (nytt valfritt felt `external_spec_url`)
3. **Konfigurerbar "Kom i gang"** — flytt hardkoda Quickstart-innhald til `src/linkml/<domain>/quickstart.md` (valfri fil per domene)
4. **Oppdatere dokumentasjonstabellen** — sørg for at `index-md-struktur.md` reflekterer dei nye kjeldene

## Løysingsval

### 1. Offisiell referanse → `manifest.yaml`

**Tilråding:** Legg til nytt valfritt felt `external_spec_url` i `manifest.yaml`.

**Grunngjeving:**
- Konsistent med eksisterande mønster (all modell-konfig ligg i `manifest.yaml`)
- Enkel Python-parsing (allereie etablert i `publish.sh`)
- Tydeleg separasjon: manifest = konfig, description.md = innhald
- Fornuftig fallback: om feltet manglar, vis ikkje seksjonen

**Eksempel (`src/linkml/ap-no/dcat-ap-no/manifest.yaml`):**
```yaml
publish_external: false
validation_policy: silver
external_spec_url: https://informasjonsforvaltning.github.io/dcat-ap-no/

generators:
  jsonld_context: true
  # ...
```

**Implementering i `publish.sh`:**
- Fjern `get_external_spec_url()`-funksjonen (linjer 30-42)
- Les `external_spec_url` frå `manifest.yaml` med Python (same mønster som `validation_policy`)
- Vis infoboks dersom feltet er sett

### 2. Kom i gang → `<domain>/quickstart.md`

**Tilråding:** Lag ny valfri fil `src/linkml/<domain>/quickstart.md` per domene.

**Grunngjeving:**
- Co-location: ligg ved sida av modellane som høyrer til domenet
- Domene-eigarar kan enkelt oppdatere innhaldet (t.d. i same PR som ein ny modell)
- Følgjer mønsteret med `description.md` (per-modell-innhald)
- Lett å oppdage og vedlikehalde

**Eksempel (`src/linkml/ap-no/quickstart.md`):**
```markdown
## Kom i gang

### Importer i LinkML-skjema

\`\`\`yaml
imports:
  - https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/main/src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema
\`\`\`

### Python-bruk

\`\`\`bash
pip install linkml-runtime pyyaml
\`\`\`

\`\`\`python
from linkml_runtime.loaders import yaml_loader
from dcat_ap_no_model import Katalog

katalog = yaml_loader.load('eksempel.yaml', target_class=Katalog)
print(katalog.tittel)
\`\`\`

### Valider data mot SHACL

\`\`\`bash
pyshacl --shacl dcat-ap-no-shapes.ttl --data-format turtle mine-data.ttl
\`\`\`
```

**Implementering i `publish.sh`:**
- Sjekk om `src/linkml/<domain>/quickstart.md` finst
- Dersom ja: inject innhaldet direkte (med variabel-substitusjon for `$schema`)
- Dersom nei: fallback til dagens hardkoda logikk (linjer 356-401)

## Steg

### Steg 1: Dokumenter "Kontakt"-seksjonen i `index-md-struktur.md`

**Oppgåve:**
- Oppdater rad 19 i tabellen "Seksjonsrekkjefølgje og kjelder"
- Endre frå: `Generert av mkdocs/publish.sh:get_contact_info() (linjer 584-589)`
- Til: `Generert av mkdocs/publish.sh:get_contact_info() frå CODEOWNERS.md (linjer 45-113). Matchdar schema-path mot path_patterns per organisasjon.`

**Verifisering:**
- Les `mkdocs/docs/index-md-struktur.md` og sjekk at tabellen er oppdatert

### Steg 2: Migrer "Offisiell referanse" til `manifest.yaml`

**Oppgåve:**

1. **Legg til `external_spec_url` i eksisterande AP-NO-manifest-filer:**
   - `src/linkml/ap-no/dcat-ap-no/manifest.yaml`
   - `src/linkml/ap-no/skos-ap-no/manifest.yaml`
   - `src/linkml/ap-no/modelldcat-modell/manifest.yaml`
   - `src/linkml/ap-no/modelldcat-katalog/manifest.yaml`
   - `src/linkml/ap-no/dqv-core/manifest.yaml`
   - `src/linkml/ap-no/cpsv-ap-no/manifest.yaml`
   - `src/linkml/ap-no/xkos-ap-no/manifest.yaml`

   Bruk URL-mappinga frå dagens `get_external_spec_url()` (linjer 30-42 i `publish.sh`).

2. **Oppdater `mkdocs/publish.sh`:**
   - Fjern `get_external_spec_url()`-funksjonen (linjer 30-42)
   - Oppdater `process_schema()` til å lese `external_spec_url` frå manifest.yaml (linje ~338):
     ```bash
     external_spec=""
     if [ -f "$manifest" ]; then
         external_spec=$(python3 -c "import yaml; print(yaml.safe_load(open('$manifest')).get('external_spec_url', ''))" 2>/dev/null || echo "")
     fi
     ```
   - Oppdater infoboks-logikken (linjer 338-346) til å bruke `$external_spec` i staden for `$(get_external_spec_url "$schema")`

3. **Oppdater dokumentasjon:**
   - `mkdocs/docs/index-md-struktur.md` rad 3: endre frå "`mkdocs/publish.sh:get_external_spec_url()` (kun for AP-NO-profilar)" til "`manifest.yaml` (`external_spec_url`-feltet, valfritt)"
   - `mkdocs/docs/manifest-config.md`: legg til `external_spec_url` i feltlista (under ein ny seksjon "Valfrie felt for dokumentasjon")

**Verifisering:**
- Køyr `make docs-publish` og sjekk at dcat-ap-no, skos-ap-no o.l. framleis viser infoboks med riktig URL
- Sjekk at domenemodell-skjema (t.d. samt-bu) ikkje viser infoboks (sidan dei ikkje har `external_spec_url`)

### Steg 3: Migrer "Kom i gang" til `<domain>/quickstart.md`

**Oppgåve:**

1. **Opprett `src/linkml/ap-no/quickstart.md`:**
   - Ekstraher dagens hardkoda AP-NO-Quickstart frå `publish.sh` (linjer 358-390)
   - Lagre som Markdown-fil med variabel-placeholder `{{SCHEMA}}` (skal erstattast av shellscript)
   - Fjern YAML-blokk og metadata (berre rein Markdown-innhald)

2. **Opprett `src/linkml/samt/quickstart.md`:**
   - Ekstraher dagens hardkoda domenemodell-Quickstart frå `publish.sh` (linjer 390-401)
   - Lagre som Markdown-fil med variabel-placeholder `{{SCHEMA}}`

3. **Oppdater `mkdocs/publish.sh`:**
   - Legg til ny funksjon `inject_quickstart()` som:
     - Sjekkar om `src/linkml/<domain>/quickstart.md` finst
     - Dersom ja: les fila, erstatt `{{SCHEMA}}` med `$schema`, output til stdout
     - Dersom nei: fallback til dagens hardkoda logikk
   - Erstatt linjer 356-401 med kall til `inject_quickstart "$domain" "$schema"`

4. **Oppdater dokumentasjon:**
   - `mkdocs/docs/index-md-struktur.md` rad 5: endre frå "Generert dynamisk av `mkdocs/publish.sh:process_schema()` (linjer 345-390). Skiljer mellom AP-NO og domenemodell." til "`src/linkml/<domain>/quickstart.md` (valfri, med `{{SCHEMA}}`-substitusjon). Fallback til hardkoda logikk dersom fila manglar."
   - `mkdocs/docs/ny-domenemodell.md`: legg til valfritt steg "Opprett `quickstart.md`" med døme

**Verifisering:**
- Køyr `make docs-publish` og sjekk at dcat-ap-no framleis viser AP-NO-Quickstart
- Sjekk at samt-bu framleis viser domenemodell-Quickstart
- Sjekk at ngr-adresse (som ikkje har quickstart.md) framleis viser fornuftig fallback

### Steg 4: Oppdater dokumentasjonstabellen i `index-md-struktur.md`

**Oppgåve:**
- Verifiser at alle rader i tabellen "Seksjonsrekkjefølgje og kjelder" er oppdaterte etter steg 1-3
- Oppdater "Oppdatere innhald i `index.md`"-tabellen (linje 148):
  - Rad "Quickstart-kommando": endre frå "Rediger `mkdocs/publish.sh:process_schema()` (linjer 345-390)" til "Rediger `src/linkml/<domain>/quickstart.md` (eller opprett fil dersom den manglar)"
  - Rad "Offisiell referanse": legg til ny rad → "Legg til `external_spec_url` i `manifest.yaml`"

**Verifisering:**
- Les `mkdocs/docs/index-md-struktur.md` og sjekk at alle referansar til linjenummer og kjelder er korrekte

## Suksesskriterium

- [x] Tabellen i `index-md-struktur.md` dokumenterer at "Kontakt" kjem frå `CODEOWNERS.md`
- [x] "Offisiell referanse"-infoboks vert generert frå `manifest.yaml` (`external_spec_url`), ikkje hardkoda funksjon
- [x] "Kom i gang"-seksjonen vert injektert frå `src/linkml/<domain>/quickstart.md` dersom fila finst
- [x] Alle eksisterande AP-NO-manifest-filer har `external_spec_url`-feltet
- [x] `src/linkml/ap-no/quickstart.md` og `src/linkml/samt/quickstart.md` finst og inneheld riktig innhald
- [x] `mkdocs/publish.sh` har ikkje lenger `get_external_spec_url()`-funksjonen
- [x] `make docs-publish` genererer identisk output som før (for skjema som har migrert konfig)
- [x] Dokumentasjonen i `index-md-struktur.md` og `manifest-config.md` er oppdatert

## Utført

Alle fire steg i specen er gjennomførte:

### Steg 1: Dokumenter "Kontakt"-seksjonen ✓
- Oppdaterte rad 19 i `mkdocs/docs/index-md-struktur.md` til å dokumentere at kontaktinfo vert generert frå `CODEOWNERS.md` med path-pattern-matching

### Steg 2: Migrer "Offisiell referanse" til `manifest.yaml` ✓
- La til `external_spec_url`-felt i sju AP-NO-manifest-filer:
  - `src/linkml/ap-no/dcat-ap-no/manifest.yaml`
  - `src/linkml/ap-no/skos-ap-no/manifest.yaml`
  - `src/linkml/ap-no/modelldcat-ap-no/manifest.yaml`
  - `src/linkml/ap-no/dqv-ap-no/manifest.yaml`
  - `src/linkml/ap-no/cpsv-ap-no/manifest.yaml`
  - `src/linkml/ap-no/xkos-ap-no/manifest.yaml`
- Fjerna `get_external_spec_url()`-funksjonen frå `mkdocs/publish.sh` (tidlegare linjer 29-42)
- Oppdaterte `process_schema()` til å lese `external_spec_url` frå manifest via Python-parsing
- Oppdaterte dokumentasjon i `mkdocs/docs/index-md-struktur.md` rad 3 og `mkdocs/docs/manifest-config.md`

### Steg 3: Migrer "Kom i gang" til `<domain>/quickstart.md` ✓
- Oppretta `src/linkml/ap-no/quickstart.md` med AP-NO-Quickstart-innhald og `{{SCHEMA}}`/`{{SCHEMA_UNDERSCORE}}`-substitusjon
- Oppretta `src/linkml/samt/quickstart.md` med domenemodell-Quickstart-innhald
- Oppdaterte `mkdocs/publish.sh` til å lese `quickstart.md` dersom den finst, med sed-substitusjon av variablar
- Beheld fallback-logikk for domene utan `quickstart.md`-fil
- Oppdaterte dokumentasjon i `mkdocs/docs/index-md-struktur.md` rad 5 og tabellen "Oppdatere innhald i `index.md`"

### Steg 4: Oppdater dokumentasjonstabellen ✓
- Oppdaterte "Seksjonsrekkjefølgje og kjelder"-tabellen (rad 3, 5, 19)
- Oppdaterte "Oppdatere innhald i `index.md`"-tabellen med nye kjelder for "Offisiell referanse" og "Quickstart-kommando"
- La til dokumentasjon for `external_spec_url` i `mkdocs/docs/manifest-config.md`

### Verifisering
- Køyrde `bash mkdocs/publish.sh` — alle 22 skjema vart genererte utan feil (55.5s total)
- Verifiserte at dcat-ap-no har "Offisiell referanse"-infoboks med riktig URL frå `manifest.yaml`
- Verifiserte at dcat-ap-no har "Kom i gang"-seksjon generert frå `src/linkml/ap-no/quickstart.md`
- Verifiserte at samt-bu har "Kom i gang"-seksjon generert frå `src/linkml/samt/quickstart.md`
- Verifiserte at ngr-adresse (domenemodell utan `external_spec_url`) ikkje viser infoboks

**Resultat:** Alle overskrifter i `index.md` har no tydelege, dokumenterte kjelder som kan konfigurerast utan å redigere shellscriptet.

## Bakoverkompatibilitet

- **Offisiell referanse:** Dersom `external_spec_url` manglar i `manifest.yaml`, vis ikkje infoboks (same oppførsel som for domenemodell-skjema i dag)
- **Kom i gang:** Dersom `src/linkml/<domain>/quickstart.md` manglar, fallback til dagens hardkoda logikk i `publish.sh`

Dette sikrar at gamle domene/modellar framleis fungerer utan endring.

## Relaterte filer

- `mkdocs/publish.sh` — hovudscript (linjer 30-42, 338-401 skal endrast)
- `mkdocs/docs/index-md-struktur.md` — dokumentasjon som skal oppdaterast
- `mkdocs/docs/manifest-config.md` — dokumentasjon for `manifest.yaml`-feltet
- `CODEOWNERS.md` — kjelde for kontaktinformasjon (ikkje endra)
- `src/linkml/ap-no/*/manifest.yaml` — skal få nytt `external_spec_url`-felt
