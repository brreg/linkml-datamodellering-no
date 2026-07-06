# Lenkjer til Classes/Slots/Enumerations/Types i importerte skjema

## Bakgrunn

Brukarar som les dokumentasjonen for eit skjema (t.d. `samt-bu`) treng ofte å sjå kva klasser, slots, enumerations og typar som er tilgjengelege frå importerte skjema (t.d. `common-ap-no`, `dcat-ap-no`, `dqv-ap-no`, `dqv-core`).

Per i dag viser index.md berre dei **lokalt definerte** klassane/slotsa/enumsa/typane. Det finst ein "Avhengigheiter"-seksjon som listar importerte skjema, men ingen direkte lenkjer til deira Classes/Slots/Enumerations/Types-seksjoner.

## Krav

Legg til ei avsluttande linje i kvar av desse seksjonane i `index.md`:

- **Classes** (## Classes)
- **Slots** (## Slots)
- **Enumerations** (## Enumerations)
- **Types** (## Types)

Linja skal innehalde lenkjer til tilsvarande seksjoner i **alle** skjema som vert importerte (direkte og transitivt) av det lokale skjemaet.

**Format:**

- **Classes:** `*Importerte klasser: [common-ap-no](../../ap-no/common-ap-no/#classes), [dcat-ap-no](../../ap-no/dcat-ap-no/#classes), ...*`
- **Slots:** `*Importerte slots: [common-ap-no](../../ap-no/common-ap-no/#slots), [dcat-ap-no](../../ap-no/dcat-ap-no/#slots), ...*`
- **Enumerations:** `*Importerte enums: [common-ap-no](../../ap-no/common-ap-no/#enumerations), [dcat-ap-no](../../ap-no/dcat-ap-no/#enumerations), ...*`
- **Types:** `*Importerte typer: [common-ap-no](../../ap-no/common-ap-no/#types), [dcat-ap-no](../../ap-no/dcat-ap-no/#types), ...*`

**Eksempel:** samt-bu sin Classes-seksjon skal ha:

```markdown
## Classes

| Class | Description |
|---|---|
| [Katalog](klasser/katalog.md) | ... |
| [Datasett](klasser/datasett.md) | ... |

*Importerte klasser: [common-ap-no](../../ap-no/common-ap-no/#classes), [dcat-ap-no](../../ap-no/dcat-ap-no/#classes), [dqv-ap-no](../../ap-no/dqv-ap-no/#classes), [dqv-core](../../ap-no/dqv-core/#classes)*
```

## Løysing

### 1. Utvid `parse-dependency-tree.py` til å returnere flat liste

`parse-dependency-tree.py` byggjer allereie eit transitivt avhengigheitstre. Utvid scriptet til å:
- Akseptere ein ny `--format flat` parameter
- Returnere ei flat liste av alle importerte skjema (i vilkårleg rekkjefølgje, evt. alfabetisk)

**Output-format (flat):**

```
common-ap-no-schema
dcat-ap-no-schema
dqv-ap-no-schema
dqv-core-schema
```

### 2. Opprett hjelpefunksjon `get_imported_schemas()`

Lag ein ny hjelpefunksjon i `mkdocs/lib/utils/` (t.d. `imported_schemas.sh`):

```bash
get_imported_schemas() {
    local domain="$1"
    local schema="$2"
    
    # Finn schema-fil
    local schema_file
    schema_file=$(find "$REPO_ROOT/src/linkml/$domain" -name "${schema}-schema.yaml" -type f 2>/dev/null | head -1)
    [ -z "$schema_file" ] && return 0
    
    # Parse direkte importar
    local imports
    imports=$(sed -n '/^imports:/,/^[a-z_]/p' "$schema_file" | grep -E "^[ ]*- " | sed 's/^[ ]*- //' | sed 's|^\.\./\.\./||' | sed 's|^\.\./||')
    [ -z "$imports" ] && return 0
    
    # Kall parse-dependency-tree.py med --format flat
    python3 "$REPO_ROOT/src/assets/scripts/parse-dependency-tree.py" --format flat "$schema" "$imports"
}
```

### 3. Utvid `generate_classes_section()` i `classes.sh`

Endre `mkdocs/lib/sections/classes.sh` til å:
- Kalle `get_imported_schemas()` etter at tabellane er genererte
- Bygge lenkjer til `../../<domain>/<imported_schema>/#classes`
- Legg til ei avsluttande linje: `*Sjå også: [schema1 Classes](...), [schema2 Classes](...)*`

**Handtering av relative stiar:**

Lenka må vere relativ til `mkdocs/docs/<domain>/<schema>/index.md`. Importerte skjema kan ligge i:
- Same domene: `../../ap-no/common-ap-no/#classes` → `../common-ap-no/#classes`
- Anna domene: `../../samt/samt-bu/index.md` → `../../fair/fair-metadata/#classes`

Bruk følgjande logikk:

```bash
# Finn domene og schema-namn for importert skjema
imported_domain=$(echo "$imported" | cut -d/ -f1)
imported_schema=$(basename "$imported" -schema.yaml | sed 's/-schema$//')

# Bygg relativ lenke
if [ "$imported_domain" = "$domain" ]; then
    link="../${imported_schema}/#classes"
else
    link="../../${imported_domain}/${imported_schema}/#classes"
fi
```

### 4. Duplikér logikk for Slots, Enumerations, Types

Same logikk som for Classes-seksjonen, men med:
- `#slots` (Slots)
- `#enumerations` (Enumerations)
- `#types` (Types)

### 5. Handter skjema utan imports

Dersom skjemaet ikkje importerer andre skjema (t.d. `linkml:types`), skal ingen lenker leggast til.

## Utført

### 1. Utvid `parse-dependency-tree.py` med `--format flat`

Endra `src/assets/scripts/parse-dependency-tree.py`:
- La til `--format flat` parameter
- Implementerte `collect_all_transitive_imports()` som samlar alle ancestors (parents) i importhierarkiet
- Returnerer flat, sortert liste av importerte skjema (inkluderer `linkml:types`)

### 2. Opprett `mkdocs/lib/utils/imported_schemas.sh`

Ny hjelpefunksjon `get_imported_schemas()`:
- Finn schema-fil dynamisk med `find`
- Parse direkte imports frå `imports:`-seksjonen
- Kall `parse-dependency-tree.py --format flat` for å hente transitive imports

### 3. Endre `mkdocs/lib/sections/classes.sh`

Implementerte `build_import_links()`:
- Hent importerte skjema via `get_imported_schemas()`
- Spesialbehandling for `linkml:types`:
  - Kun vist i Types-seksjonen (ikkje Classes/Slots/Enumerations)
  - Lenke til https://github.com/linkml/linkml-model/blob/main/linkml_model/model/schema/types.yaml
  - Plassert **først** i lenkjelista
- Finn domene for kvart importert skjema med `find`
- Bygg relative lenkjer:
  - Same domene: `../imported-schema/#section`
  - Anna domene: `../../domain/imported-schema/#section`
- Generer lenkjelinje med riktig tekst (`*Importerte klasser: ...`, osv.)

Omskriv `generate_classes_section()`:
- Ekstraher kvar seksjon separat (Classes, Slots, Enumerations, Types) med `awk`
- Legg til import-lenkjer etter kvar seksjon
- Beheld Subsets-seksjonen utan import-lenkjer

### 4. Oppdater `mkdocs/lib/generate_index.sh`

Sett miljøvariablar `CURRENT_DOMAIN` og `CURRENT_SCHEMA` før `generate_classes_section()` vert kalla, slik at `build_import_links()` har tilgang til konteksten.

### 5. Test

```bash
make docs-publish
grep "Importerte" mkdocs/docs/samt/samt-bu/index.md
# Output:
# *Importerte klasser: [common-ap-no](../../ap-no/common-ap-no/#classes), [dcat-ap-no](../../ap-no/dcat-ap-no/#classes), [dqv-ap-no](../../ap-no/dqv-ap-no/#classes), [dqv-core](../../ap-no/dqv-core/#classes)*
# *Importerte slots: [common-ap-no](../../ap-no/common-ap-no/#slots), [dcat-ap-no](../../ap-no/dcat-ap-no/#slots), [dqv-ap-no](../../ap-no/dqv-ap-no/#slots), [dqv-core](../../ap-no/dqv-core/#slots)*
# *Importerte enums: [common-ap-no](../../ap-no/common-ap-no/#enumerations), [dcat-ap-no](../../ap-no/dcat-ap-no/#enumerations), [dqv-ap-no](../../ap-no/dqv-ap-no/#enumerations), [dqv-core](../../ap-no/dqv-core/#enumerations)*
# *Importerte typer: [common-ap-no](../../ap-no/common-ap-no/#types), [dcat-ap-no](../../ap-no/dcat-ap-no/#types), [dqv-ap-no](../../ap-no/dqv-ap-no/#types), [dqv-core](../../ap-no/dqv-core/#types)*

# Same-domene lenkjer (dcat-ap-no → dqv-core):
grep "Importerte" mkdocs/docs/ap-no/dcat-ap-no/index.md | head -1
# *Importerte klasser: [common-ap-no](../common-ap-no/#classes), [dqv-core](../dqv-core/#classes)*

# Skjema utan imports (fair-metadata) har ingen lenkjer:
grep "Importerte" mkdocs/docs/fair/fair-metadata/index.md
# (ingen output)
```

## Verifisering

```bash
make docs-publish
grep "Importerte" mkdocs/docs/samt/samt-bu/index.md
# Forventa output (4 liner — éin per seksjon):
# *Importerte klasser: [common-ap-no](../../ap-no/common-ap-no/#classes), ...
# *Importerte slots: [common-ap-no](../../ap-no/common-ap-no/#slots), ...
# *Importerte enums: [common-ap-no](../../ap-no/common-ap-no/#enumerations), ...
# *Importerte typer: [common-ap-no](../../ap-no/common-ap-no/#types), ...
```

Verifiser at lenkjer er korrekte:
- Click på lenke i mkdocs-portalen → skal navigere til rett seksjon i importert skjema
- Verifiser relativ sti for same domene (t.d. `dcat-ap-no` → `dqv-ap-no`)
- Verifiser relativ sti for anna domene (t.d. `samt-bu` → `common-ap-no`)

## Merk

- `linkml:types` får lenke til https://github.com/linkml/linkml-model/blob/main/linkml_model/model/schema/types.yaml (eksternt skjema)
- `linkml:types` vises **kun** i Types-seksjonen (ikkje Classes/Slots/Enumerations)
- `linkml:types` er **først** i Types-lenkjelista
- Dersom eit importert skjema ikkje har Classes/Slots/Enumerations/Types-seksjon, skal lenka likevel inkluderast (MkDocs håndterer broken anchors gracefully)
- Rekkjefølgja på importerte skjema er alfabetisk sortert (etter `linkml:types`)

## Resultat

```markdown
*Importerte klasser: [common-ap-no](../../ap-no/common-ap-no/#classes), [dcat-ap-no](../../ap-no/dcat-ap-no/#classes), [dqv-ap-no](../../ap-no/dqv-ap-no/#classes), [dqv-core](../../ap-no/dqv-core/#classes)*

*Importerte slots: [common-ap-no](../../ap-no/common-ap-no/#slots), [dcat-ap-no](../../ap-no/dcat-ap-no/#slots), [dqv-ap-no](../../ap-no/dqv-ap-no/#slots), [dqv-core](../../ap-no/dqv-core/#slots)*

*Importerte enums: [common-ap-no](../../ap-no/common-ap-no/#enumerations), [dcat-ap-no](../../ap-no/dcat-ap-no/#enumerations), [dqv-ap-no](../../ap-no/dqv-ap-no/#enumerations), [dqv-core](../../ap-no/dqv-core/#enumerations)*

*Importerte typer: [linkml:types](https://github.com/linkml/linkml-model/blob/main/linkml_model/model/schema/types.yaml), [common-ap-no](../../ap-no/common-ap-no/#types), [dcat-ap-no](../../ap-no/dcat-ap-no/#types), [dqv-ap-no](../../ap-no/dqv-ap-no/#types), [dqv-core](../../ap-no/dqv-core/#types)*
```
