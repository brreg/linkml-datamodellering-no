---
name: fix-codeowners-hardcoded-path
description: Fiks hardkoda sti til CODEOWNERS.md i get_contact_info() — feiler i CI (GitHub Actions)
metadata:
  type: bugfix
---

# Fiks hardkoda sti til CODEOWNERS.md i get_contact_info()

## Bakgrunn

I `mkdocs/publish.sh` har `get_contact_info()`-funksjonen ein hardkoda sti til `CODEOWNERS.md` på linje 64:

```python
with open("/mnt/c/dev/github/linkml-datamodellering-no/CODEOWNERS.md", "r") as f:
    content = f.read()
```

Denne stien fungerer berre i WSL2 (`/mnt/c/...`), **ikkje i CI** (GitHub Actions Ubuntu-runners som brukar `/home/runner/work/...`).

### Observert symptom

I CI (GitHub Actions) fell `get_contact_info()` tilbake på fallback-meldinga:

```
**Support:** [GitHub Issues](https://github.com/brreg/linkml-datamodellering-no/issues)
```

medan det lokalt (WSL2) genererer korrekt kontaktinfo:

```
**Forvaltningsansvarleg:** [KS Digital](https://data.norge.no/organizations/971032146)

**Kontakt:** [KS Digital - Kontakt](https://www.ks.no/fagomrader/digitalisering/)

**Support:** [GitHub Issues](https://github.com/brreg/linkml-datamodellering-no/issues)
```

### Rotsak

Python-scriptet i `get_contact_info()` (linje 57-92) brukar hardkoda sti i staden for `$codeowners_file`-variabelen som er definert på linje 49.

## Løysing

Erstatt hardkoda sti med `$codeowners_file`-variabelen i Python-scriptet.

## Implementasjon

### 1. Endre Python-script til å bruke $codeowners_file-variabel

**Før (linje 57-64):**
```bash
org_data=$(python3 - "$schema_path" <<'PYEOF'
import sys
import re
import yaml

schema_path = sys.argv[1]

with open("/mnt/c/dev/github/linkml-datamodellering-no/CODEOWNERS.md", "r") as f:
    content = f.read()
```

**Etter:**
```bash
org_data=$(python3 - "$schema_path" "$codeowners_file" <<'PYEOF'
import sys
import re
import yaml

schema_path = sys.argv[1]
codeowners_file = sys.argv[2]

with open(codeowners_file, "r") as f:
    content = f.read()
```

Endringar:
1. Legg til `"$codeowners_file"` som argument til `python3 -` (linje 57)
2. Legg til `codeowners_file = sys.argv[2]` i Python-scriptet (linje 63)
3. Erstatt hardkoda sti med `codeowners_file` i `open()` (linje 65)

## Teststrategi

### Lokalt (WSL2)

1. Køyr `bash mkdocs/publish.sh`
2. Sjekk `mkdocs/docs/samt/samt-bu/index.md` — verifiser at Kontakt-seksjonen inneheld:
   - `**Forvaltningsansvarleg:** [KS Digital](...)`
   - `**Kontakt:** [KS Digital - Kontakt](...)`
   - `**Support:** [GitHub Issues](...)`

### I CI (simulert)

1. Køyr scriptet frå repo-root (ikkje `/mnt/c/...`):
   ```bash
   cd /tmp
   git clone ... repo
   cd repo
   bash mkdocs/publish.sh
   ```
2. Verifiser same resultat som over

### I faktisk CI

1. Push endringane til ein branch
2. Trigger `generate.yml`-workflow
3. Sjekk publisert `samt/samt-bu/index.md` på GitHub Pages
4. Verifiser at Kontakt-seksjonen har full info (ikkje berre Support)

## Handlingsliste

- [✓] 1. Legg til `"$codeowners_file"` som argument til `python3 -` (linje 57)
- [✓] 2. Legg til `codeowners_file = sys.argv[2]` i Python-scriptet (ny linje 63)
- [✓] 3. Erstatt hardkoda sti med `codeowners_file` i `open()` (linje 65)
- [✓] 4. Test lokalt: `bash mkdocs/publish.sh`
- [ ] 5. Test i CI: push til branch og sjekk GitHub Pages

## Utført

Alle tre endringar vart implementerte i `mkdocs/publish.sh`:

1. Linje 57: Lagt til `"$codeowners_file"` som argument til `python3 -`
2. Linje 63: Lagt til `codeowners_file = sys.argv[2]` i Python-scriptet
3. Linje 65: Erstatta hardkoda sti `/mnt/c/dev/github/linkml-datamodellering-no/CODEOWNERS.md` med variabelen `codeowners_file`

**Resultat (lokalt):**
- Alle kontaktpunkt vert genererte korrekt:
  - `samt/samt-bu`: KS Digital
  - `oreg/register-over-aksjeeiere`: Brønnøysundregistra
  - `ap-no/dcat-ap-no`: Digitaliseringsdirektoratet
  - `fint/fint-administrasjon`: Novari IKS
- Ingen feilmeldingar ved køyring av `bash mkdocs/publish.sh`

**Neste steg:**
- Test i CI ved neste push til `main` eller ved å trigge `generate.yml`-workflow
- Verifiser at GitHub Pages viser full kontaktinfo (ikkje berre "Support: GitHub Issues")
