# Legg til "Importerte modeller:"-lenkjer under Avhengigheiter-overskrifta

## Bakgrunn

Under "Avhengigheiter"-overskrifta i kvar modell sin `index.md`-dokumentasjonsside skal det leggjast til ei linje **"Importerte modeller:"** med lenkjer til dokumentasjonssida for alle importerte modeller. Dette følgjer same mønster som dei eksisterande "Importerte <objekt>"-lenkjene for klasser, slots, enums, typer og subsets.

## Krav

1. **Plassering:** Linja skal kome **sist** under "Avhengigheiter"-overskrifta, rett før skiljelinja `---` som avsluttar seksjonen (dvs. etter Imports-underseksjon og "Sjå Importhierarki"-lenkja)

2. **Lenkeformat:**
   - For **`linkml:types`**: lenk til GitHub (https://github.com/linkml/linkml-model/blob/main/linkml_model/model/schema/types.yaml)
   - For **andre importerte modeller** (t.d. `dcat-ap-no-schema`, `fint-common-schema`): relative lenkjer til deira dokumentasjonsside i portalen

3. **Lenketekst:** Bruk schema-namn utan `-schema`-suffiks (t.d. `dcat-ap-no`, `fint-common`)

4. **Rekkjefølgje:**
   - `linkml:types` **først** (dersom importert)
   - Andre imports i same rekkjefølgje som dei kjem i treet (dvs. same rekkjefølgje som i `get_imported_schemas`-output)

5. **Format:** Same stil som "Importerte klasser:"-linja i Classes-seksjonen:
   ```markdown
   *Importerte modeller: [linkml:types](https://github.com/linkml/linkml-model/blob/main/linkml_model/model/schema/types.yaml), [dcat-ap-no](../../ap-no/dcat-ap-no/#metadata), [common-ap-no](../../ap-no/common-ap-no/#metadata)*
   ```

6. **Anker-fragment:** Kvar lenke skal peike til `#metadata`-ankeret på målsida (første seksjon på kvar modell sin index.md)

## Steg

### 1. Oppdater `avhengigheiter.sh` til å generere "Importerte modeller:"-linja

**Fil:** `mkdocs/lib/sections/avhengigheiter.sh`

**Endring:**
- Legg til ein ny funksjon `build_imported_models_links()` som følgjer same mønster som `build_import_links()` i `classes.sh`
- Funksjonen skal:
  - Hente importerte skjema via `get_imported_schemas`
  - Spesialbehandling for `linkml:types` (GitHub-lenke)
  - For andre skjema: bygg relative lenkjer til `../../<domain>/<schema>/#metadata`
  - Output: `*Importerte modeller: <lenkjeliste>*`

- Kall funksjonen i `generate_dependencies()` **etter** "Sjå Importhierarki"-linja og **før** siste `echo ""`

### 2. Oppdater `metadata.sh` til å inkludere Metadata-anker

**Fil:** `mkdocs/lib/sections/metadata.sh`

**Endring:**
- Endre `awk`-mønster til å akseptere både `## Metadata` og `## Metadata {#metadata}` som input
- Output skal alltid vere `## Modellmetadata {#metadata}`
- Dette sikrar at alle modell-index-sider har eit stabilt `#metadata`-anker å lenke til

**Bakgrunn:** Metadata-seksjonen vert ekstrakt frå gendoc-output og overskrifta vert endra frå "Metadata" til "Modellmetadata" i `metadata.sh`, så ankeret må leggjast til der, ikkje i Jinja-templaten.

### 3. Test generert output

**Kommando:**
```bash
make docs-publish
```

**Verifiser:**
- Sjå på `mkdocs/docs/referanse/referanse/index.md` — skal ha "Importerte modeller:"-linje under Avhengigheiter-overskrifta
- Klikk på lenkjene og sjekk at dei fungerer
- Sjekk at `linkml:types` lenkar til GitHub
- Sjekk at andre imports lenkar til `#metadata`-seksjonen på respektive modell-sider

## Tiltak

- [x] Oppdater `avhengigheiter.sh` med `build_imported_models_links()`-funksjon
- [x] Legg til `{#metadata}`-anker i `metadata.sh`
- [x] Test med `make docs-publish`
- [x] Verifiser output i `mkdocs/docs/referanse/referanse/index.md`
- [x] Generer commit-melding

## Utført

Alle tiltak er fullførte. "Importerte modeller:"-lenkjer er lagt til under Avhengigheiter-overskrifta i alle modell-dokumentasjonssider, med korrekt lenking til `#metadata`-anker og GitHub for `linkml:types`.

**Verifisert output:**
- `referanse/referanse/index.md`: "Importerte modeller: linkml:types, common-ap-no, dcat-ap-no, dqv-core"
- `ap-no/dcat-ap-no/index.md`: "Importerte modeller: linkml:types, common-ap-no, dqv-core"
- Alle lenkjer peikar til `#metadata`-anker (lokale modeller) eller GitHub (linkml:types)

**Endra filer:**
- `mkdocs/lib/sections/avhengigheiter.sh` — ny funksjon `build_imported_models_links()`
- `mkdocs/lib/sections/metadata.sh` — lagt til `{#metadata}`-anker i output
- `src/assets/templates/docgen/index.md.jinja2` — lagt til `{#metadata}` i Metadata-overskrift (blir overskrive av metadata.sh, men gjer templaten konsistent)
