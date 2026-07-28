# Omdøp sections-script til å matche genererte overskrifter

## Bakgrunn

Scripta i `mkdocs/lib/sections/` har filnamn som ikkje alltid matcher overskriftene dei genererer i `index.md`. Dette gjer det vanskelegare å forstå kva kvart script gjer ved å berre sjå på filnamnet.

## Mål

Omdøpe scripta slik at filnamna betre reflekterer den primære overskrifta scriptet genererer.

## Noverande vs. ønskt mapping

| Noverande filnamn | Generert hovudoverskrift | Foreslått nytt filnamn | Kommentar |
|---|---|---|---|
| `artifacts.sh` | `## Generated artifacts` | `generated_artifacts.sh` | Matchar overskrifta |
| `badges.sh` | *(ingen overskrift)* | `badges.sh` | **Beheld** — genererer badges, ikkje seksjon |
| `changelog.sh` | `## Versjonslog` | `versjonslog.sh` | Matchar overskrifta |
| `classes.sh` | `## Subsets` | `classes.sh` | **Beheld** — handterer fleire seksjoner (Classes, Slots, Enumerations, Types, Subsets) |
| `contact.sh` | `## Kontakt` | `kontakt.sh` | Matchar overskrifta |
| `datamodell.sh` | *(ingen overskrift)* | `datamodell.sh` | **Beheld** — embeddar iframe, ikkje seksjon |
| `dependencies.sh` | `## Avhengigheiter` | `avhengigheiter.sh` | Matchar overskrifta |
| `description.sh` | `## Om denne modellen` | `om_denne_modellen.sh` | Matchar overskrifta |
| `er_diagram.sh` | `## ER-diagram` | `er_diagram.sh` | **Beheld** — allereie godt namngitt |
| `example.sh` | `## Eksempeldatafil` | `eksempeldatafil.sh` | Matchar overskrifta |
| `external_reference.sh` | *(ingen overskrift)* | `external_reference.sh` | **Beheld** — genererer publiseringsboks, ikkje seksjon |
| `header.sh` | *(ingen overskrift)* | `header.sh` | **Beheld** — genererer hovudoverskrift, ikkje seksjon |
| `metadata.sh` | *(ingen overskrift)* | `metadata.sh` | **Beheld** — embeddar metadata frå gen-doc, ikkje seksjon |
| `quickstart.sh` | `## Kom i gang` | `kom_i_gang.sh` | Matchar overskrifta |
| `submodel_info.sh` | `## Delmodellar` | `delmodellar.sh` | Matchar overskrifta |
| `validation.sh` | `## Valideringsresultat` | `valideringsresultat.sh` | Matchar overskrifta |

## Namnekonvensjon

- **Snake_case** for script som genererer seksjoner med norske overskrifter (t.d. `versjonslog.sh`, `kom_i_gang.sh`)
- **Lowercase med understrek** i staden for bindestreker (snake_case, ikkje kebab-case) — konsistent med LinkML-konvensjonar
- **Engelske namn** behaldast der det er naturleg (t.d. `er_diagram.sh`, `metadata.sh`)

## Steg

### 1. Omdøp filene

```bash
cd mkdocs/lib/sections/

# Omdøp til norske namne
mv artifacts.sh generated_artifacts.sh
mv changelog.sh versjonslog.sh
mv contact.sh kontakt.sh
mv dependencies.sh avhengigheiter.sh
mv description.sh om_denne_modellen.sh
mv example.sh eksempeldatafil.sh
mv quickstart.sh kom_i_gang.sh
mv submodel_info.sh delmodellar.sh
mv validation.sh valideringsresultat.sh
```

**Behaldast uendra:**
- `badges.sh` — genererer badges, ikkje seksjon
- `classes.sh` — handterer fleire seksjoner
- `datamodell.sh` — embeddar iframe
- `er_diagram.sh` — allereie godt namngitt
- `external_reference.sh` — genererer publiseringsboks
- `header.sh` — genererer hovudoverskrift
- `metadata.sh` — embeddar metadata

### 2. Oppdater sourcing i `generate_index.sh`

`generate_index.sh` sourcar alle `.sh`-filer i `sections/`-katalogen automatisk, så ingen eksplisitte referansar må oppdaterast:

```bash
for section_file in "$SECTIONS_DIR"/*.sh; do
    source "$section_file"
done
```

Dette betyr at omdøypinga **ikkje krev endring i `generate_index.sh`** — wildcarden `*.sh` plukkar opp dei nye namna automatisk.

### 3. Verifiser at alle funksjonar framleis vert kalla

Sjekk at funksjonskalla i `generate_index.sh` framleis matcher funksjonsnamna i scripta (funksjonsnamna vert **ikkje** endra, berre filnamna):

```bash
grep "^    generate_" mkdocs/lib/generate_index.sh
```

Forventa output:
```
    generate_header "$schema"
    generate_badges "$domain" "$schema" "$gendoc_index"
    generate_external_reference "$domain" "$schema"
    generate_description "$domain" "$schema"
    generate_quickstart "$domain" "$schema"
    generate_example "$domain" "$schema"
    generate_metadata "$gendoc_index"
    generate_submodel_box
    generate_dependencies "$domain" "$schema"
    generate_submodels_section
    generate_er_diagram "$schema" "$out"
    generate_datamodell "$domain" "$schema"
    generate_classes_section "$klasse_src"
    generate_artifacts_table "$out" "$schema"
    generate_validation_results "$domain" "$schema"
    generate_changelog "$domain" "$schema"
    generate_contact_info "$domain" "$schema"
```

**Viktig:** Funksjonsnamna i sjølve scripta skal **ikkje** endrast — berre filnamna. T.d.:
- `artifacts.sh` → `generated_artifacts.sh`, men funksjonen heiter framleis `generate_artifacts_table()`
- `changelog.sh` → `versjonslog.sh`, men funksjonen heiter framleis `generate_changelog()`

### 4. Test at mkdocs-publikasjon framleis fungerer

```bash
# Generer artefaktar for eit testdomene
make dcat-ap-no

# Publiser til mkdocs
make docs-publish

# Sjekk at index.md vert generert korrekt
cat mkdocs/docs/dcat-ap-no/dcat-ap-no-schema/index.md | grep "^##" | head -10
```

Forventa seksjonsoverskrifter i `index.md`:
```
## Metadata
## Avhengigheiter (X)
## ER-diagram
## Classes
## Generated artifacts (X)
## Valideringsresultat
## Versjonslog
## Kontakt
```

### 5. Oppdater dokumentasjon

Dersom `CLAUDE.md` eller andre dokument refererer eksplisitt til sections-scriptnamna (ikkje forventa), oppdater desse.

## Kriteria for ferdigstilling

- [ ] Alle 9 script er omdøypte i `mkdocs/lib/sections/`
- [ ] `make docs-publish` køyrer utan feil
- [ ] Genererte `index.md`-filer inneheld alle forventa seksjonsoverskrifter
- [ ] Ingen referansar til gamle scriptnamn finst i `mkdocs/lib/`

## Handlingsliste

- [x] Omdøp 9 script i `mkdocs/lib/sections/`
- [x] Verifiser at `generate_index.sh` sourcar alle script korrekt
- [x] Test med `make docs-publish`
- [x] Verifiser genererte `index.md`-filer

## Utført

Alle 9 sections-script er omdøypte til å matche overskriftene dei genererer:

```bash
cd mkdocs/lib/sections/ && \
mv artifacts.sh generated_artifacts.sh && \
mv changelog.sh versjonslog.sh && \
mv contact.sh kontakt.sh && \
mv dependencies.sh avhengigheiter.sh && \
mv description.sh om_denne_modellen.sh && \
mv example.sh eksempeldatafil.sh && \
mv quickstart.sh kom_i_gang.sh && \
mv submodel_info.sh delmodellar.sh && \
mv validation.sh valideringsresultat.sh
```

**Verifisert:**
- `generate_index.sh` sourcar alle script automatisk via wildcard (`*.sh`)
- `mkdocs/publish.sh` køyrer utan feil — 9 domene publiserte
- Genererte `index.md`-filer inneheld alle forventa seksjonsoverskrifter

**Testresultat (`mkdocs/docs/ap-no/dcat-ap-no/index.md`):**
```
## Om denne modellen        ← om_denne_modellen.sh
## Kom i gang                ← kom_i_gang.sh
## Eksempeldatafil           ← eksempeldatafil.sh
## Avhengigheiter (3)        ← avhengigheiter.sh
## Generated artifacts (11)  ← generated_artifacts.sh
## Valideringsresultat       ← valideringsresultat.sh
## Versjonslog               ← versjonslog.sh
## Kontakt                   ← kontakt.sh
```

**Behaldast uendra (7 script):**
- `badges.sh` — genererer badges, ikkje seksjon
- `classes.sh` — handterer fleire seksjoner (Classes, Slots, Enumerations, Types, Subsets)
- `datamodell.sh` — embeddar iframe
- `er_diagram.sh` — allereie godt namngitt
- `external_reference.sh` — genererer publiseringsboks
- `header.sh` — genererer hovudoverskrift
- `metadata.sh` — embeddar metadata
