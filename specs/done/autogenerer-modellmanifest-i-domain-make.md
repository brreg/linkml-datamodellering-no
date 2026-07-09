# Autogenerer modellmanifest i domain-make og lenk i index.md

## Bakgrunn

`specs/done/manifest-som-modelldcat-datafil.md` dokumenterer at `metadata/modelldcat.yaml` (Informasjonsmodell-instans) skal genererast automatisk av CI som del av `make domain-*`-kommandoane. Manifestet skal også lenkast i "Generated artifacts"-tabellen i `mkdocs/docs/<domain>/<modell>/index.md`, **i første rad** i tabellen.

**Noverande tilstand:**

1. `make gen-informasjonsmodell-instance SCHEMA=<path>` genererer `metadata/modelldcat.yaml` manuelt
2. `mkdocs/publish.sh` kopierer `metadata/modelldcat.yaml` til `mkdocs/docs/<domain>/<modell>/metadata/` (tiltak 14-16 i spec)
3. `mkdocs/lib/sections/artifacts.sh` legg til manifestet som **siste rad** i artefakt-tabellen

**Ønsket tilstand:**

1. `make domain-*` køyrer automatisk `make gen-informasjonsmodell-instance` for kvart skjema
2. Artefakt-tabellen i `index.md` har manifestet som **første rad** (ikkje siste)

## Forståing

- Autogenerering skal skje i `make domain-*`-targets (t.d. `make domain-ap-no`, `make domain-ngr`, `make domain-samt`)
- Manifestet skal vere i **første rad** i "Generated artifacts"-tabellen (høgste prioritet)
- `mkdocs/lib/sections/artifacts.sh` genererer tabellen — rad-rekkjefølgja må endrast

## Tiltak

### 1. Oppdater generate-informasjonsmodell.py til å bruke <modell>-manifest.yaml

**Fil:** `src/assets/scripts/generate-informasjonsmodell.py`

**Endring:**
- Output-plassering: `src/linkml/<domain>/<modell>/metadata/<modell>-manifest.yaml` (tidlegare `modelldcat.yaml`)
- Behaldt all eksisterande logikk (6 kjelder, LangString-transformasjon, etc.)

**Pseudo-kode:**
```python
# Noverande:
output_path = schema_path.replace("-schema.yaml", "/metadata/modelldcat.yaml")

# Ønska:
# src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml
# → src/linkml/ap-no/dcat-ap-no/metadata/dcat-ap-no-manifest.yaml
output_path = schema_path.replace("-schema.yaml", "/metadata/{modell}-manifest.yaml")
# der {modell} = basename frå schema_path (t.d. "dcat-ap-no")
```

### 2. Integrer gen-informasjonsmodell-instance i make domain-*

**Fil:** `Makefile`

**Endring:** Legg til parallel køyring av `gen-informasjonsmodell-instance` i `domain-%`-target, etter alle `gen-*`-kommandoar.

**Plassering:** Etter alle artefaktar er genererte (jsonschema, shacl, owl, plantuml, docs, etc.), før `publish.sh`.

**Køyr parallelt:** Bruk same mønster som PlantUML-generering (`find | xargs -P $(PARALLEL_JOBS)`).

**Feilhandtering:** Logg feil, men hald fram (ikkje `set -e` / `|| exit 1`).

**Pseudo-kode:**
```makefile
domain-%:
	# Eksisterande generatorkall (jsonschema, shacl, owl, plantuml, docs, etc.)
	...
	
	# Generer Informasjonsmodell-instans (manifest.yaml) for kvart skjema — parallelt
	@echo "Generating Informasjonsmodell instances for domain $*..."
	@find src/linkml/$* -name "*-schema.yaml" -type f | \
		xargs -I {} -P $(PARALLEL_JOBS) $(MAKE) gen-informasjonsmodell-instance SCHEMA={} || \
		echo "Warning: Some Informasjonsmodell instances failed to generate"
	
	# Eksisterande publikasjonssteg
	...
```

**Obs:** `gen-informasjonsmodell-instance` les `generated/<domain>/<modell>/` for `finnes_i_format`, så det må køyrast **etter** alle artefaktar er genererte.

### 3. Oppdater mkdocs/lib/copy_artifacts.sh

**Fil:** `mkdocs/lib/copy_artifacts.sh`

**Endring:** Kopier `<modell>-manifest.yaml` frå `src/linkml/<domain>/<modell>/metadata/` til `mkdocs/docs/<domain>/<modell>/`

**Tidlegare:** Kopierte `metadata/modelldcat.yaml` (tiltak 14 i spec)

**Ny:**
```bash
# Kopier modellmanifest (Informasjonsmodell-instans)
manifest_file="src/linkml/$domain/$schema/metadata/$schema-manifest.yaml"
if [[ -f "$manifest_file" ]]; then
    cp "$manifest_file" "$out/$schema-manifest.yaml"
fi
```

### 4. Opprett mkdocs/lib/sections/datamodell.sh

**Fil:** `mkdocs/lib/sections/datamodell.sh` (ny fil)

**Endring:** Lag ei eiga fil som genererer "Datamodell"-seksjonen med lenke til LinkML-schema.

**Plassering i index.md:**
1. Metadata-tabell
2. Publiseringsinfo-boks
3. ER-diagram
4. **NY: Datamodell-seksjon** ← her
5. Classes-liste
6. Slots-liste
7. Enumerations-liste
8. Types-liste
9. Generated artifacts-tabell
10. Valideringsresultat
11. Versjonslog

**Ny fil: `mkdocs/lib/sections/datamodell.sh`**
```bash
#!/usr/bin/env bash
# Generer Datamodell-seksjon med lenke til LinkML-schema

set -euo pipefail

domain="$1"
schema="$2"

cat <<EOF

## Datamodell

Kjelde-datamodell i LinkML-format: [\`$schema-schema.yaml\`](../../../src/linkml/$domain/$schema/$schema-schema.yaml)

EOF
```

**Integrer i `mkdocs/publish.sh`:**
```bash
# Etter ER-diagram og før Classes-liste:
bash mkdocs/lib/sections/datamodell.sh "$domain" "$schema" >> "$index_file"
```

### 5. Oppdater mkdocs/lib/sections/artifacts.sh

**Fil:** `mkdocs/lib/sections/artifacts.sh`

**Endring:**
1. Legg til modellmanifest som **første rad** (etter tabelloverskrift)
2. **Fjern** LinkML-schema (det ligg no i eigen tabell over Classes)
3. Fjern tidlegare manifest-sjekk (som la det til som siste rad)

**Lenketekst:** "Modellmanifest ihht Modelldcat-ap-no"

**Ny struktur:**
```bash
echo "| Artifact | Link |"
echo "| --- | --- |"

# Første rad: Modellmanifest
if [[ -f "$out/$schema-manifest.yaml" ]]; then
    echo "| Modellmanifest ihht Modelldcat-ap-no | [\`$schema-manifest.yaml\`]($schema-manifest.yaml) |"
fi

# Resten: JSON Schema, SHACL, OWL, etc. (IKKJE LinkML-schema)
if [[ -f "$out/$schema-schema.json" ]]; then
    echo "| JSON Schema | [\`$schema-schema.json\`]($schema-schema.json) |"
fi
...
```

### 6. Verifiser at manifestet vert generert for alle skjema

**Test-kommandoar:**
```bash
# Generer artefaktar for ap-no-domenet
make domain-ap-no

# Sjekk at manifest-filer vart genererte
ls -l src/linkml/ap-no/*/metadata/*-manifest.yaml

# Sjekk at manifest vart kopiert til mkdocs
ls -l mkdocs/docs/ap-no/*/*.manifest.yaml

# Sjekk LinkML-schema-tabell (skal vere før Classes)
grep -B 2 -A 3 "## LinkML-schema" mkdocs/docs/ap-no/dcat-ap-no/index.md
# Forventa output:
# ## LinkML-schema
# | Schema | Link |
# | --- | --- |
# | LinkML-schema (kjeldekode) | `dcat-ap-no-schema.yaml` |

# Sjekk artefakt-tabell (første rad skal vere manifestet)
grep -A 3 "## Generated artifacts" mkdocs/docs/ap-no/dcat-ap-no/index.md | head -5
# Forventa output:
# ## Generated artifacts
# | Artifact | Link |
# | --- | --- |
# | Modellmanifest ihht Modelldcat-ap-no | `dcat-ap-no-manifest.yaml` |
```

**Feilhandtering:**
- Dersom `gen-informasjonsmodell-instance` feiler for eit skjema, skal feilmeldinga loggast til stdout/stderr
- `make domain-*` skal **ikkje** stoppe (warning i staden for exit 1)
- Sjekk loggen for å finne kva skjema som feila og kvifor

### 7. Dokumenter i COMMANDS.md

**Fil:** `COMMANDS.md`

**Endring:** Oppdater dokumentasjonen for `make domain-*` for å presisere at den no køyrer `gen-informasjonsmodell-instance` automatisk.

**Legg til i seksjon `make domain-*`:**
```markdown
Genererer alle artefaktar for eit domene, inkludert:
- JSON Schema, SHACL, OWL, PlantUML, OpenAPI, Protobuf, etc.
- Modellmanifest (Informasjonsmodell-instans ihht ModelDCAT-AP-NO) — `<modell>-manifest.yaml`
- Dokumentasjon og valideringsresultat

Modellmanifestet vert generert til `src/linkml/<domain>/<modell>/metadata/<modell>-manifest.yaml` og inkludert som første rad i artefakt-tabellen i dokumentasjonsportalen. LinkML-schema vert vist i eigen tabell før Classes-lista.
```

### 8. Oppdater generate-modellkatalog.py

**Fil:** `src/assets/scripts/generate-modellkatalog.py`

**Endring:** Les `<modell>-manifest.yaml` frå `src/linkml/<domain>/<modell>/metadata/` i staden for `modelldcat.yaml`

**Tidlegare:**
```python
all_modelldcat_files = glob("src/linkml/**/metadata/modelldcat.yaml")
```

**Ny:**
```python
all_modelldcat_files = glob("src/linkml/**/metadata/*-manifest.yaml")
```

**Obs:** Dette sikrar at modellkatalogen (`generated/modellkatalog.yaml` og per-org katalogfiler) brukar dei genererte manifestfilene med riktig filnamn.

## Avklarte antakelser (2026-07-09)

1. **Plassering:** `src/linkml/<domain>/<modell>/metadata/<modell>-manifest.yaml` (generert, men commit til repo)
2. **Lenketekst:** "Modellmanifest ihht Modelldcat-ap-no"
3. **Parallellisering:** Ja, køyr parallelt på same måten som andre artefaktar i `make domain-*`
4. **Feilhandtering:** Logg feilmelding, men hald fram (ikkje stopp heile bygget)
5. **LinkML-schema plassering:** IKKJE i Generated artifacts-tabellen — skal vere i eigen tabell over "Classes"-overskrifta
6. **Artefakt-tabell rekkjefølgje:** Modellmanifest først, deretter resten (JSON Schema, SHACL, OWL, etc.)

## Handlingsliste

- [x] 1. Oppdater `generate-informasjonsmodell.py` — output til `src/linkml/<domain>/<modell>/metadata/<modell>-manifest.yaml`
- [x] 2. Integrer `gen-informasjonsmodell-instance` i `make domain-*` (Makefile) — køyr parallelt etter alle gen-*
- [x] 3. Oppdater `mkdocs/lib/copy_artifacts.sh` — kopier `<modell>-manifest.yaml` frå src/linkml/.../metadata/
- [x] 4. Opprett `mkdocs/lib/sections/datamodell.sh` — generer "Datamodell"-seksjon med lenke til LinkML-schema
- [x] 5. Integrer `datamodell.sh` i `mkdocs/lib/generate_index.sh` — plasser etter ER-diagram, før Classes
- [x] 6. Oppdater `mkdocs/lib/sections/artifacts.sh` — modellmanifest først, fjern gammal metadata-sjekk
- [x] 7. Verifiser at manifestet vert generert for alle skjema (`make domain-ap-no`) — ✓ 10 manifest genererte
- [x] 8. Dokumenter i `COMMANDS.md` — presiser at `make domain-*` genererer modellmanifest
- [x] 9. Oppdater `generate-modellkatalog.py` — les `src/linkml/**/metadata/*-manifest.yaml`

## Utført (2026-07-09)

Alle tiltak er fullførte og verifiserte:

1. ✅ `generate-informasjonsmodell.py` — output til `<modell>-manifest.yaml`
2. ✅ `Makefile` — parallell køyring av `gen-informasjonsmodell-instance` i `domain-%`-target
3. ✅ `mkdocs/lib/copy_artifacts.sh` — kopier manifest frå `src/linkml/.../metadata/`
4. ✅ `mkdocs/lib/sections/datamodell.sh` (NY) — "Datamodell"-seksjon med lenke til LinkML-schema
5. ✅ `mkdocs/lib/generate_index.sh` — integrerte `generate_datamodell()` etter ER-diagram
6. ✅ `mkdocs/lib/sections/artifacts.sh` — manifest først i Generated artifacts-tabell
7. ✅ `generate-modellkatalog.py` — les `*-manifest.yaml` i staden for `modelldcat.yaml`
8. ✅ `COMMANDS.md` — dokumentert modellmanifest-generering

**Verifisering:**
- `make domain-ap-no PARALLEL=1` — ✓ Alle 10 skjema fekk generert manifest
- Manifest-filer ligg i `src/linkml/<domain>/<modell>/metadata/<modell>-manifest.yaml`
- Filnamn følgjer mønsteret `<modell>-manifest.yaml` (t.d. `dcat-ap-no-manifest.yaml`, `dqv-core-manifest.yaml`)

## Viktige implementasjonsdetaljar

### Plassering
- **Generert artefakt:** `src/linkml/<domain>/<modell>/metadata/<modell>-manifest.yaml`
- **Kopiert til mkdocs:** `mkdocs/docs/<domain>/<modell>/<modell>-manifest.yaml`
- **Tidlegare filnamn:** `modelldcat.yaml` → **nytt filnamn:** `<modell>-manifest.yaml`

### Seksjonar i index.md (rekkjefølgje)
1. Metadata-tabell
2. Publiseringsinfo-boks
3. ER-diagram
4. **NY: Datamodell-seksjon** (paragraf + lenke til LinkML-schema)
5. Classes-liste
6. Slots-liste
7. Enumerations-liste
8. Types-liste
9. Generated artifacts-tabell (modellmanifest først, IKKJE LinkML-schema)
10. Valideringsresultat
11. Versjonslog

### Generated artifacts-tabell rekkjefølgje
1. Modellmanifest ihht Modelldcat-ap-no (`<modell>-manifest.yaml`)
2. JSON Schema (`<modell>-schema.json`)
3. SHACL Shapes (`<modell>-shapes.ttl`)
4. ... (resten som før)

**Viktig:** LinkML-schema skal IKKJE vere i Generated artifacts — det har eigen tabell før Classes.

### Parallell køyring
- Same mønster som PlantUML: `find | xargs -P $(PARALLEL_JOBS) make gen-informasjonsmodell-instance`
- Feilhandtering: `|| echo "Warning: Some Informasjonsmodell instances failed to generate"`
- Feil vert logga, men byggeprosessen stoppar ikkje

### Påverkna filer
1. `src/assets/scripts/generate-informasjonsmodell.py` — output-path-logikk (`<modell>-manifest.yaml`)
2. `Makefile` — `domain-%`-target (legg til gen-informasjonsmodell-instance)
3. `mkdocs/lib/copy_artifacts.sh` — kopier `<modell>-manifest.yaml` frå src/linkml/.../metadata/
4. `mkdocs/lib/sections/datamodell.sh` (NY FIL) — generer Datamodell-seksjon med lenke til LinkML-schema
5. `mkdocs/publish.sh` — integrer datamodell.sh før Classes-lista
6. `mkdocs/lib/sections/artifacts.sh` — artefakt-tabell (manifest først, IKKJE LinkML-schema)
7. `src/assets/scripts/generate-modellkatalog.py` — les `src/linkml/**/metadata/*-manifest.yaml`
8. `COMMANDS.md` — dokumentasjon av `make domain-*`
