---
name: forbetre-imports-visning
description: Vis fullt skjemanamn (inkl. -schema-suffiks) og marker direkte vs transitive importar
metadata:
  type: enhancement
---

# Forbetre Imports-visning i Avhengigheiter-seksjonen

## Bakgrunn

I Avhengigheiter-seksjonen i `index.md` (t.d. `mkdocs/docs/samt/samt-bu/index.md`) finst det to problem:

### Problem 1: Manglande -schema-suffiks

Importar viser berre `dqv-ap-no`, men den faktiske fila heiter `dqv-ap-no-schema.yaml`. Dette er misvisande fordi:

- Brukarar som vil importere skjemaet må bruke `dqv-ap-no-schema` (ikkje `dqv-ap-no`)
- Det finst to filer i `dqv-ap-no`-katalogen: `dqv-core-schema.yaml` og `dqv-ap-no-schema.yaml`

**Gjeldande visning:**
```
linkml:types
└── common-ap-no
    ├── dcat-ap-no
    └── dqv-ap-no
```

**Ønskt visning:**
```
linkml:types
└── common-ap-no-schema
    ├── dcat-ap-no-schema
    └── dqv-ap-no-schema
```

### Problem 2: Manglar markering av direkte vs transitive importar

Det er uklart kva som er **direkte importar** (frå `samt-bu-schema.yaml` sin `imports:`-seksjon) og kva som er **transitive importar** (importert via andre skjema).

**Eksempel:** `samt-bu-schema.yaml` importerer:
```yaml
imports:
  - linkml:types
  - ../../ap-no/dcat-ap-no/dcat-ap-no-schema
  - ../../ap-no/dqv-ap-no/dqv-ap-no-schema
```

Men `common-ap-no-schema` er **ikkje** i lista — den er transitiv (importert via `dcat-ap-no-schema`).

**Ønskt visning:**
```
linkml:types                   # direkte
└── common-ap-no-schema        # transitiv
    ├── dcat-ap-no-schema      # direkte
    └── dqv-ap-no-schema       # direkte
```

Eller med eksplisitte kommentarar:
```
linkml:types                             # direkte import
└── common-ap-no-schema                  # transitiv import (via dcat-ap-no-schema)
    ├── dcat-ap-no-schema                # direkte import
    └── dqv-ap-no-schema                 # direkte import
```

## Løysing

### Del 1: Behald -schema-suffiks i normalize_schema_name()

**Før (`parse-dependency-tree.py` linje 114-127):**
```python
def normalize_schema_name(name: str) -> str:
    """
    Normalize schema name from imports to match hierarchy.

    Examples:
        "ap-no/dcat-ap-no/dcat-ap-no" -> "dcat-ap-no"
        "linkml:types" -> "linkml:types"
        "../fint-common/fint-common-schema" -> "fint-common"
    """
    # Remove path components
    name = name.split('/')[-1]
    # Remove -schema suffix
    name = name.replace('-schema', '')
    return name
```

**Etter:**
```python
def normalize_schema_name(name: str) -> str:
    """
    Normalize schema name from imports.

    Examples:
        "ap-no/dcat-ap-no/dcat-ap-no-schema" -> "dcat-ap-no-schema"
        "linkml:types" -> "linkml:types"
        "../fint-common/fint-common-schema" -> "fint-common-schema"
    """
    # Remove path components
    name = name.split('/')[-1]
    # Keep -schema suffix
    return name
```

### Del 2: Oppdater importhierarki.md til å bruke -schema-suffiks

Endre alle schema-namn i `mkdocs/docs/importhierarki.md` til å inkludere `-schema`-suffiks.

**Før:**
```
linkml:types
    ↓
common-ap-no          ← bare AP-NO-profilene importerer denne direkte
    ↓
dcat-ap-no / dqv-ap-no / skos-ap-no / …
```

**Etter:**
```
linkml:types
    ↓
common-ap-no-schema   ← bare AP-NO-profilene importerer denne direkte
    ↓
dcat-ap-no-schema / dqv-ap-no-schema / skos-ap-no-schema / …
```

### Del 3: Legg til kommentarar for direkte vs transitiv

Oppdater `build_subtree()` i `parse-dependency-tree.py` til å legge til kommentar på kvar linje:

**Logikk:**
- Les `imports:`-lista frå `samt-bu-schema.yaml` (via `publish.sh`)
- Normaliser importa til skjemanamn (t.d. `../../ap-no/dcat-ap-no/dcat-ap-no-schema` → `dcat-ap-no-schema`)
- Marker kvar linje i treet:
  - `# direkte import` dersom skjemaet er i den normaliserte importlista
  - `# transitiv import` elles

**Implementasjon:**

1. Oppdater `publish.sh` linje 209 til å sende normaliserte direkte importar som argument:
   ```bash
   python3 "$REPO_ROOT/src/assets/scripts/parse-dependency-tree.py" "$schema" "$imports" "$(echo "$imports" | tr ' ' '\n' | xargs -I {} basename {} | sed 's/-schema$//-schema/')"
   ```

2. Oppdater `parse-dependency-tree.py` `main()` til å ta imot tredje argument:
   ```python
   def main():
       if len(sys.argv) < 3:
           print("Usage: parse-dependency-tree.py <schema_name> <imports_list> [direct_imports]", file=sys.stderr)
           sys.exit(1)

       schema_name = sys.argv[1]
       imports = sys.argv[2].split()
       direct_imports = set(sys.argv[3].split()) if len(sys.argv) > 3 else set()

       tree = build_dependency_tree(schema_name, imports, direct_imports)
       print(tree)
   ```

3. Oppdater `build_subtree()` til å legge til kommentarar:
   ```python
   def build_subtree(
       schema: str,
       tree: Dict[str, List[str]],
       visited: Set[str],
       direct_imports: Set[str],
       indent: int = 0
   ) -> List[str]:
       # ... eksisterande logikk ...
       
       # Add current schema
       comment = ""
       if schema in direct_imports:
           comment = "  # direkte import"
       elif indent > 0:
           comment = "  # transitiv import"
       
       if indent == 0:
           lines.append(schema + comment)
       else:
           prefix = '    ' * (indent - 1) + '└── '
           lines.append(prefix + schema + comment)
   ```

**Alternativ enklare variant:** Berre marker direkte importar, lat transitive vere utan kommentar:

```
linkml:types                             # direkte
└── common-ap-no-schema
    ├── dcat-ap-no-schema                # direkte
    └── dqv-ap-no-schema                 # direkte
```

## Teststrategi

1. Oppdater `parse-dependency-tree.py` (del 1)
2. Oppdater `importhierarki.md` (del 2)
3. Køyr `bash mkdocs/publish.sh`
4. Sjekk `mkdocs/docs/samt/samt-bu/index.md` → Avhengigheiter-seksjonen
5. Verifiser:
   - Alle skjema har `-schema`-suffiks (t.d. `dcat-ap-no-schema`, ikkje `dcat-ap-no`)
   - Direkte importar er markerte med kommentar (valfritt)

## Handlingsliste

- [✓] 1. Fjern `name = name.replace('-schema', '')` i `normalize_schema_name()` (linje 127)
- [✓] 2. Oppdater `importhierarki.md` til å bruke `-schema`-suffiks på alle skjemanamn
- [✓] 3. Legg til logikk for direkte/transitiv-kommentarar i `build_subtree()`
- [✓] 4. Test: `bash mkdocs/publish.sh && grep -A15 "## Avhengigheiter" mkdocs/docs/samt/samt-bu/index.md`

## Utført

Alle tre tiltaka vart implementerte:

### 1. Behald -schema-suffiks

**Før:** `normalize_schema_name()` strippa `-schema`-suffikset → `dqv-ap-no`
**Etter:** Suffikset vert behalde → `dqv-ap-no-schema`

### 2. Oppdatert importhierarki.md

Alle skjemanamn i `mkdocs/docs/importhierarki.md` brukar no `-schema`-suffiks:
- `common-ap-no` → `common-ap-no-schema`
- `dcat-ap-no` → `dcat-ap-no-schema`
- `dqv-core` → `dqv-core-schema`
- `fint-common` → `fint-common-schema`
- `samt-bu` → `samt-bu-schema`
- osv.

### 3. Direkte vs transitiv-kommentarar

Oppdatert `build_subtree()` til å legge til kommentarar basert på normaliserte direkte importar:
- `# direkte import` — skjemaet er i den direkte importlista
- `# transitiv import` — skjemaet er importert via andre skjema

Oppdatert `publish.sh` til å:
1. Behalde `-schema`-suffiks i `imports` (fjerna `sed 's/-schema$//'`)
2. Generere `direct_imports_normalized` (basename av importa)
3. Sende `direct_imports_normalized` som tredje argument til `parse-dependency-tree.py`

**Resultat (samt-bu):**
```
linkml:types  # direkte import
└── common-ap-no-schema  # transitiv import
    ├── dcat-ap-no-schema  # direkte import
    └── dqv-ap-no-schema  # direkte import
```

**Resultat (dcat-ap-no):**
```
linkml:types  # direkte import
└── common-ap-no-schema  # direkte import
    └── dqv-core-schema  # direkte import
```

Begge problema er løyste:
- ✅ Fullt skjemanamn med `-schema`-suffiks
- ✅ Kommentarar viser direkte vs transitiv
