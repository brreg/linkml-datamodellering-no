# Støtte for fleire skjema per kjeldekatalog

## Bakgrunn

CI-jobben `Generate and publish` feila fordi `publish.sh` og `make domain-*` ikkje handterte skjema der filnamnet (`dqv-core-schema.yaml`) ikkje matcher katalognamnet (`dqv-ap-no/`).

Strukturen i repoet:

```
src/linkml/ap-no/dqv-ap-no/
  ├── dqv-ap-no-schema.yaml       → generated/ap-no/dqv-ap-no/
  └── dqv-core-schema.yaml        → generated/ap-no/dqv-core/

src/linkml/ap-no/modelldcat-ap-no/
  ├── modelldcat-ap-no-schema.yaml     → generated/ap-no/modelldcat-ap-no/
  ├── modelldcat-katalog-schema.yaml   → generated/ap-no/modelldcat-katalog/
  └── modelldcat-modell-schema.yaml    → generated/ap-no/modelldcat-modell/
```

**Problemet:** Makefile sin `schema_name`-funksjon brukte katalognamnet (field 4 i stien) i staden for filnamnet, og `publish.sh`-seksjonane brukte hardkoda `src/linkml/$domain/$schema/` for å finne CHANGELOG, description.md osv.

## Løysing

### 1. Makefile: Trekk ut schema-namn frå filnamn

**Før:**
```makefile
schema_name = $(word 4,$(subst /, ,$(1)))  # dqv-ap-no (katalog)
```

**Etter:**
```makefile
schema_name = $(basename $(basename $(notdir $(1))))  # dqv-core (filnamn)
```

Dette gjer at `dqv-core-schema.yaml` genererer artefaktar til `generated/ap-no/dqv-core/`, ikkje `generated/ap-no/dqv-ap-no/`.

### 2. publish.sh-seksjonar: Dynamisk kjeldekatalog-lookup

Erstatta hardkoda `src/linkml/$domain/$schema/` med dynamisk `find`:

```bash
# Finn kjeldemappe for skjemaet (kan vere ulik $schema-namnet)
local schema_file
schema_file=$(find "$REPO_ROOT/src/linkml/$domain" -name "${schema}-schema.yaml" -type f 2>/dev/null | head -1)
local src_dir=""
[ -n "$schema_file" ] && src_dir=$(dirname "$schema_file")
```

**Endra filer:**
- `mkdocs/lib/copy_artifacts.sh` — CHANGELOG.md
- `mkdocs/lib/sections/description.sh` — description.md
- `mkdocs/lib/sections/quickstart.sh` — examples/
- `mkdocs/lib/sections/example.sh` — examples/ og GitHub-lenke
- `mkdocs/lib/sections/changelog.sh` — CHANGELOG.md
- `mkdocs/lib/sections/dependencies.sh` — imports-parsing

## Verifisering

```bash
make domain-ap-no  # Genererer dqv-core, modelldcat-katalog, modelldcat-modell
make docs-publish  # Ingen FEIL-meldingar
ls generated/ap-no/{dqv-core,modelldcat-katalog,modelldcat-modell}  # OK
ls mkdocs/docs/ap-no/{dqv-core,modelldcat-katalog,modelldcat-modell}  # OK
```

## Utført

- [x] Endre Makefile sin `schema_name`-funksjon til å bruke filnamn
- [x] Oppdatere `copy_artifacts.sh` til dynamisk kjeldekatalog
- [x] Oppdatere `description.sh`, `quickstart.sh`, `example.sh`, `changelog.sh`, `dependencies.sh`
- [x] Verifisere at `make domain-ap-no` genererer alle skjema
- [x] Verifisere at `make docs-publish` publiserer alle skjema utan feil
