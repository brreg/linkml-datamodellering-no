# Stale `generate.yaml`-referansar etter overgang til `manifest.yaml`

## Bakgrunn

`generate.yaml` er erstatta av `manifest.yaml`. Det nye formatet er eit overbygd
konfigurasjonsfil som samlar publiseringsmetadata og generatorflaggar:

```yaml
# manifest.yaml (skjema-manifest — har generators:-seksjon)
publish_external: false
data_policy: silver

generators:
  jsonld_context: true
  shacl: true
  ...
```

```yaml
# manifest.yaml (datafil-manifest — manglar generators:-seksjon)
publish_external: true
data_policy: felles-begrepskatalog

concepts:          # valfri — utelat for å publisere heile datafila
  - https://...
```

CI skil desse to typane på om `generators:`-seksjonen er til stades.

---

## Funn per fil

### 1. `src/assets/scripts/gen-docgen-examples.py` — FUNKSJONELL FEIL

**Status:** Krev retting — kjøretidsfeil.

Linje 74–77 opnar `generate.yaml` for å lese opt-out-flagget `docgen_examples: false`.
Fila heiter no `manifest.yaml`, så opt-out-funksjonen er brot:

```python
# Feil (linje 74–77):
generate_yaml = schema_path.parent / "generate.yaml"
if generate_yaml.exists():
    ...
```

Rett:

```python
manifest_yaml = schema_path.parent / "manifest.yaml"
if manifest_yaml.exists():
    ...
```

Kommentaren på linje 11 (`docgen_examples: false is set in generate.yaml`) må òg rettast.

---

### 2. `mkdocs/docs/generate-config.md` — heile sida er utdatert

**Status:** Krev retting — brukarvendt.

Sida er fullt ut skriven for `generate.yaml` og manglar:

| Mangel | Detalj |
|---|---|
| Tittel | `# Generatorkonfigurasjon (generate.yaml)` → `(manifest.yaml)` |
| Alle `generate.yaml`-referansar (9 stk.) | Skal vera `manifest.yaml` |
| `publish_external`-feltet | Ikkje nemnt |
| `data_policy`-feltet | Ikkje nemnt |
| Skjema-manifest vs. datafil-manifest | Ikkje forklart |
| Ny `config.mk`-triggerlinje | Makefile har `$(shell find src/linkml -name 'manifest.yaml')` — teksten seier framleis `generate.yaml`-fil |

---

### 3. `mkdocs/docs/ny-domenemodell.md`

**Status:** Krev retting — brukarvendt.

| Linje | Innhald | Rett |
|---|---|---|
| 153 | `generate.yaml` ved sida av skjemafila | `manifest.yaml` |
| 157 | `rediger generate.yaml` | `rediger manifest.yaml` |
| 160 | `# regenerer Makefile-konfig frå alle generate.yaml-filer` | `manifest.yaml-filer` |

---

### 4. `mkdocs/docs/ny-begrepsmodell.md`

**Status:** Krev retting — brukarvendt.

| Linje | Innhald | Rett |
|---|---|---|
| 110 | `## 3 — Skriv \`generate.yaml\`` | `manifest.yaml` |
| 112–126 | YAML-eksempel manglar `publish_external: false` øvst | Legg til `publish_external: false` |

---

### 5. `specs/dokumentasjon-publisering-begrep.md` og `specs/generate-config.md`

**Status:** Historiske designdokument — lav prioritet. Ikkje brukarvendte.

---

## Prioritert tiltaksliste

| # | Fil | Endring | Prioritet |
|---|---|---|---|
| 1 | `src/assets/scripts/gen-docgen-examples.py` | Byt `generate.yaml` → `manifest.yaml` (linje 11, 74, 75) | **Kritisk** |
| 2 | `mkdocs/docs/generate-config.md` | Skriv om heile sida for `manifest.yaml`; legg til `publish_external`, `data_policy`, skjema- vs. datafil-manifest | Høg |
| 3 | `mkdocs/docs/ny-domenemodell.md` | Byt 3 `generate.yaml`-førekomstar → `manifest.yaml` | Høg |
| 4 | `mkdocs/docs/ny-begrepsmodell.md` | Byt seksjonstittel + legg til `publish_external: false` i YAML-eksempel | Høg |
| 5 | `specs/`-filer | Historisk kontekst — ikkje kritisk | Lav |
