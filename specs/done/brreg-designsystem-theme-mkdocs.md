# Integrasjon av @brreg/designsystemet-theme i MkDocs

## Bakgrunn

Tidlegare PoC-ar ([specs/done/poc-digdir-designsystem-mkdocs.md](poc-digdir-designsystem-mkdocs.md) og [specs/done/poc-digdir-designsystem-cli.md](poc-digdir-designsystem-cli.md)) konkluderte med at **CLI-generering og manuell CSS-import ikkje er praktisk** for MkDocs Material-tema, primært på grunn av:

1. CSS spesifisitetsproblem (krev `!important` for å overstyre Material-tema)
2. Høg setup-kompleksitet (Node.js 22+, CLI-generering, config-vedlikehald)
3. Marginal verdi for ein teknisk dokumentasjonsportal

Brukaren ønskjer å bruke Brønnøysund sitt ferdigpakka tema `@brreg/designsystemet-theme`, som er ein enklare tilnærming enn CLI-generering.

## Mål

- Installere `@brreg/designsystemet-theme` NPM-pakke
- Integrere ferdig CSS i MkDocs Material-tema
- Dokumentere enklare setup samanlikna med CLI-tilnærminga

## Gjennomføring

### Steg 1: Installer NPM-pakke

Køyr i Node.js 22-container (eller lokal Node.js):

```bash
cd mkdocs
podman run --rm -v "$(pwd):/work" -w /work node:22-alpine \
  npm install @brreg/designsystemet-theme
```

**Output:**
- `mkdocs/node_modules/@brreg/designsystemet-theme/css/brreg.css` (wrapper-fil)
- `mkdocs/node_modules/@brreg/designsystemet-theme/css/generated/brreg.css` (63 KB hovedfil)

### Steg 2: Kopier CSS-filer til mkdocs/docs/stylesheets

```bash
mkdir -p mkdocs/docs/stylesheets/brreg-theme
cp -r mkdocs/node_modules/@brreg/designsystemet-theme/css/* \
  mkdocs/docs/stylesheets/brreg-theme/
```

**Filstruktur:**
```
mkdocs/docs/stylesheets/brreg-theme/
├── brreg.css              # 216 bytes wrapper med @import
└── generated/
    ├── brreg.css          # 63 KB hovedfil med tokens
    ├── colors.d.ts        # TypeScript-definisjonar
    └── types.d.ts         # TypeScript-definisjonar
```

### Steg 3: Oppdater mkdocs.yml

```yaml
extra_css:
  - stylesheets/brreg-theme/brreg.css  # Brønnøysund designsystem-tema
  - stylesheets/digdir-cli-poc.css     # Material-overrides (frå tidlegare PoC)
  - stylesheets/responsivt-design.css
```

**Merk:** `brreg.css` importerer `generated/brreg.css` via `@import`-direktiv, så heile css/-mappa må kopierast.

### Steg 4: Test

```bash
make docs-build
```

Verifiser at `site/index.html` inkluderer `stylesheets/brreg-theme/brreg.css`.

## Utført

### Gjennomførte tiltak

1. **Installert `@brreg/designsystemet-theme@0.3.3`** via NPM
   - Pakka er offentleg publisert (`publishConfig: { access: "public" }`)
   - Versjon: 0.3.3 (frå package.json)

2. **Kopierte CSS-filer til mkdocs/docs/stylesheets/brreg-theme/**
   - `brreg.css` (216 bytes) — wrapper med `@import "generated/brreg.css"`
   - `generated/brreg.css` (63 KB) — hovudfil med tokens (v1.17.0)

3. **Oppdaterte `mkdocs.yml`**
   - Lagt til `stylesheets/brreg-theme/brreg.css` i `extra_css`
   - Beheld `digdir-cli-poc.css` for Material-overrides

### Funn

#### Fordelar over CLI-tilnærminga

✅ **Enklare setup** — berre `npm install` og kopier CSS (ingen CLI-generering)
✅ **Ingen Node.js-versjonskrav** — NPM-pakka er pre-bygd
✅ **Ingen konfigurasjonsfil** — `@brreg/designsystemet-theme` er ferdigkonfigurert med Brønnøysund-fargar
✅ **Mindre vedlikehald** — oppdater pakkeversjon i staden for å køyre CLI
✅ **Same CSS-output** — `generated/brreg.css` er identisk med CLI-generert versjon

#### Utfordringar (same som tidlegare PoC-ar)

⚠️ **CSS spesifisitetsproblem ikkje løyst** — må framleis bruke `!important` i `digdir-cli-poc.css` for å overstyre Material-tema
⚠️ **NPM-avhengigheit** — må installere pakka for å få oppdateringar
⚠️ **@import-direktiv** — `brreg.css` brukar `@import "generated/brreg.css"`, så heile css/-mappa må kopierast (ikkje berre ei fil)

### Samanlikning: NPM-pakke vs CLI-generering

| Aspekt | `@brreg/designsystemet-theme` NPM | CLI-generering |
|--------|-----------------------------------|----------------|
| **Setup-kompleksitet** | Låg (npm install + kopier) | Høg (CLI i container + config) |
| **Node.js-krav** | Ingen (pre-bygd CSS) | Node.js 22+ |
| **Vedlikehald** | `npm update` | Oppdater config + køyr CLI |
| **CSS-størrelse** | 63 KB (generated/brreg.css) | 51 KB (sjølvgenerert) |
| **Spesifisitetsproblem** | ❌ Krev `!important` | ❌ Krev `!important` |
| **Konfigurasjonsfil** | ❌ Ferdigkonfigurert (kan ikkje tilpasse) | ✅ Kan tilpasse via `designsystemet.config.json` |

### Anbefaling

**`@brreg/designsystemet-theme` NPM-pakke er den **enklaste tilnærminga** for Brønnøysund-fargar i MkDocs.**

**Grunngjeving:**
1. **Enklare setup** — berre NPM install og kopier CSS (ingen CLI-generering)
2. **Mindre vedlikehald** — `npm update` i staden for CLI-køyring
3. **Same CSS-output** — identisk med CLI-generert versjon

**Begrensning:**
CSS spesifisitetsproblem er **ikkje løyst** — må framleis bruke `!important` i Material-overrides (same som CLI-tilnærminga).

**Dersom tilpassing av fargar er nødvendig** (t.d. endre primærfarge til noko anna enn Brønnøysund sine standardfargar), må ein bruke CLI-tilnærminga i staden (sjå [specs/done/poc-digdir-designsystem-cli.md](poc-digdir-designsystem-cli.md)).

### Neste steg

- [ ] Avgjer om Brønnøysund-fargar skal brukast permanent i MkDocs-portalen
- [ ] Dersom ja: commit `brreg-theme/`-mappa til repo og oppdater `CONTRIBUTING.md` med NPM-installasjonsinstruksjonar
- [ ] Dersom nei: rull tilbake til Material-tema standard (indigo) og rydd vekk Digdir/Brønnøysund CSS-filer
- [ ] Vurder om `node_modules/` skal ekskluderast frå Git (`.gitignore`) eller om CSS skal kopierast permanent

### Referansar

- NPM-pakke: `@brreg/designsystemet-theme@0.3.3`
- GitHub-repo: https://github.com/brreg/designsystemet
- Tidlegare PoC-ar:
  - [specs/done/poc-digdir-designsystem-mkdocs.md](poc-digdir-designsystem-mkdocs.md) — hardkoda hex-verdiar
  - [specs/done/poc-digdir-designsystem-cli.md](poc-digdir-designsystem-cli.md) — CLI-generering

## Handlingsliste (utført)

- [x] Installer `@brreg/designsystemet-theme` via NPM
- [x] Kopier CSS-filer til `mkdocs/docs/stylesheets/brreg-theme/`
- [x] Oppdater `mkdocs.yml` → `extra_css`
- [x] Dokumenter funn og anbefaling
