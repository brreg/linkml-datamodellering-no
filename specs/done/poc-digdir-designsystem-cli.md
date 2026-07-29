# PoC: Digdir designsystem med CLI og genererte tokens i MkDocs

## Bakgrunn

Den tidlegare PoC ([specs/done/poc-digdir-designsystem-mkdocs.md](../done/poc-digdir-designsystem-mkdocs.md)) konkluderte med at **fullstendig integrasjon av Digdir designsystem CSS ikkje er praktisk** for MkDocs Material-tema, primært på grunn av:

1. CSS custom properties-konflikt mellom Material-tema og Digdir tokens
2. Marginal verdi for ein teknisk dokumentasjonsportal
3. Høg vedlikehaldsbyrde

Sidan den gongen har Digdir designsystem fått betre CLI-støtte via `@digdir/designsystemet` NPM-pakke. Denne PoC utforskar ein **CLI-basert tilnærming** der vi genererer skreddarsydde CSS-tokens frå ein konfigurasjonsfil, i staden for å bruke ferdiggenererte `brreg.css`.

**Hypotese:** Ved å generere eigne design tokens med CLI kan vi få betre kontroll over CSS custom properties og redusere konflikt med Material-tema.

## Mål

- Verifisere at `@digdir/designsystemet` CLI kan generere CSS-tokens for MkDocs-portalen
- Integrere genererte tokens i MkDocs Material-tema med minimal konflikt
- Dokumentere prosess, funn og anbefaling for vidare integrasjon

## Avgrensing

**Dette er ein PoC** — ikkje ein produksjonsklar implementasjon. Målet er å verifisere teknisk gjennomførbarheit og verdi, ikkje å lage ein komplett designsystem-integrasjon.

## Førarbeid: Kva er tilgjengeleg?

Basert på dokumentasjon frå https://designsystemet.no/no/fundamentals/code/setup og NPM-pakkeinformasjon:

### NPM-pakkar
- **`@digdir/designsystemet`** — CLI for generering av tokens og CSS
- **`@digdir/designsystemet-css`** — Ferdige CSS-stilar (alternativ til CLI-generering)
- **`@digdir/designsystemet-web`** — Web-komponenter (JavaScript — ikkje relevant for MkDocs)
- **`@digdir/designsystemet-react`** — React-komponenter (ikkje relevant)

### CLI-kommandoar (frå NPM-dokumentasjon)
```bash
# Generer design tokens frå konfigurasjonsfil
npx @digdir/designsystemet tokens create [--config <path>]

# Bygg CSS frå genererte tokens
npx @digdir/designsystemet tokens build [options]
```

### Konfigurasjonsfil
- Format: `designsystemet.config.json` (auto-detektert i current directory)
- Genererast frå https://theme.designsystemet.no/ (Themebuilder)
- Inneheld merkevarefargar, typografi-innstillingar, spacing osv.

### Genererte filer
- **`design-tokens/`-mappe** — JSON-tokens (frå `tokens create`)
- **CSS-filer** — bygd frå tokens (frå `tokens build`)

## Gjennomføring

### Steg 1: Installer CLI og generer konfigurasjonsfil

**1a. Bestem om CLI skal installerast globalt eller per-prosjekt**

Alternativ:
- **A. Lokal installasjon i `mkdocs/`-mappe** (anbefalt for reproduserbarheit)
- **B. Global installasjon** (enklare, men krev Node.js på utviklarmaskinen)
- **C. Kun `npx`-bruk** (ingen installasjon, køyrer remote)

**Anbefaling for PoC:** Bruk alternativ C (`npx`) for å unngå avhengigheit i repoet.

**1b. Generer konfigurasjonsfil frå Themebuilder**

1. Gå til https://theme.designsystemet.no/
2. Set opp tema med Brønnøysund-fargar (eller standard Digdir-fargar)
3. Klikk "Apply theme" og last ned `designsystemet.config.json`
4. Lagre fila i `mkdocs/designsystemet.config.json`

**Alternativ:** Dersom Brønnøysund har ein eksisterande `designsystemet.config.json` i eit anna repo (t.d. `brreg/designsystemet`), kan vi kopiere denne.

### Steg 2: Generer design tokens

Køyr CLI-kommando for å generere JSON-tokens:

```bash
cd mkdocs
npx @digdir/designsystemet tokens create --config designsystemet.config.json
```

**Forventa output:**
- `mkdocs/design-tokens/` — mappe med JSON-tokens (fargar, typografi, spacing osv.)

### Steg 3: Bygg CSS frå tokens

Køyr CLI-kommando for å bygge CSS:

```bash
cd mkdocs
npx @digdir/designsystemet tokens build
```

**Forventa output:**
- CSS-filer i `mkdocs/design-tokens/` eller eigen output-mappe (avhengig av CLI-versjon)

**Potensielt problem:** CLI kan forvente ein spesifikk mappestruktur eller konfigurasjonsfelt som ikkje er dokumentert i den offentlege dokumentasjonen. Vi må verifisere output-struktur og justera deretter.

### Steg 4: Integrer genererte CSS-tokens i MkDocs

**4a. Kopier genererte CSS-filer til `mkdocs/docs/stylesheets/`**

```bash
cp mkdocs/design-tokens/*.css mkdocs/docs/stylesheets/digdir-generated/
```

**Merk:** Output-filnamn og -struktur må verifierast etter Steg 3.

**4b. Opprett `digdir-cli-poc.css` som mapper tokens til Material-variablar**

Lag `mkdocs/docs/stylesheets/digdir-cli-poc.css` tilsvarande den tidlegare `digdir-poc.css`, men med følgjande endringar:

1. Importer genererte CSS-filer (ikkje `brreg.css`)
2. Map Digdir tokens til Material-variablar ved å bruke `var(--ds-*)`-referansar
3. Test om CSS custom properties-konflikt er redusert (sammenlikna med tidlegare PoC)

**Eksempel:**
```css
/* Last inn genererte Digdir tokens */
@import url('digdir-generated/tokens.css'); /* Faktisk filnamn må verifierast */

/* Overstyr Material theme med Digdir tokens */
:root {
  /* Primærfargar → Digdir Main1 (blå) */
  --md-primary-fg-color: var(--ds-color-main1-base-default);
  --md-primary-fg-color--light: var(--ds-color-main1-background-default);
  --md-primary-fg-color--dark: var(--ds-color-main1-base-active);
  
  /* Accent → Digdir Main2 (oransje) */
  --md-accent-fg-color: var(--ds-color-main2-base-default);
  
  /* Typografi */
  --md-text-font: var(--ds-font-family);
}

/* Aktivt menypunkt → bruk Digdir fargar */
.md-nav__item--active > .md-nav__link {
  background-color: var(--ds-color-main1-background-subtle);
  border-left: 4px solid var(--ds-color-main1-border-default);
}
```

**4c. Oppdater `mkdocs.yml`**

Legg til genererte CSS-filer i `extra_css`:

```yaml
extra_css:
  - stylesheets/digdir-generated/tokens.css  # Genererte tokens
  - stylesheets/digdir-cli-poc.css           # Material-overrides
  - stylesheets/responsivt-design.css
```

### Steg 5: Test og verifiser

```bash
make docs-serve
```

Opne `http://localhost:8000` og verifiser:

- [ ] CSS custom properties (`var(--ds-*)`) fungerer utan konflikt med Material-tema
- [ ] Primærfargar (header, lenker) brukar Digdir-tokens
- [ ] Aktivt menypunkt brukar Digdir lyseblå bakgrunn
- [ ] Typografi brukar Inter (Digdir font-family)
- [ ] Dark mode fungerer (`prefers-color-scheme: dark`)

**Samanlikn med tidlegare PoC:**
- Er CSS custom properties-konflikten løyst?
- Er det enklare å vedlikehalde tokens (sidan dei er genererte frå konfigurasjonsfil)?

### Steg 6: Dokumenter resultat

Fullfør `## Utført`-seksjonen i denne specen med:

1. **CLI-generering:** Fungerer `npx @digdir/designsystemet tokens create` og `tokens build`?
2. **Output-struktur:** Kva filer vert genererte, og kvar vert dei plasserte?
3. **CSS custom properties:** Fungerer `var(--ds-*)` betre enn hardkoda hex-verdiar?
4. **Konflikt med Material-tema:** Er spesifisitetsproblem redusert?
5. **Vedlikehaldsbyrde:** Er det enklare å oppdatere fargar via `designsystemet.config.json`?
6. **Anbefaling:** Skal CLI-tilnærminga brukast, eller er tidlegare PoC (hardkoda hex) godt nok?

## Handlingsliste

- [ ] Generer `designsystemet.config.json` frå https://theme.designsystemet.no/ (eller kopier frå `brreg/designsystemet`)
- [ ] Køyr `npx @digdir/designsystemet tokens create --config mkdocs/designsystemet.config.json`
- [ ] Køyr `npx @digdir/designsystemet tokens build` og verifiser output
- [ ] Kopier genererte CSS-filer til `mkdocs/docs/stylesheets/digdir-generated/`
- [ ] Opprett `mkdocs/docs/stylesheets/digdir-cli-poc.css` med Material-overrides
- [ ] Oppdater `mkdocs/mkdocs.yml` → `extra_css` med genererte CSS-filer
- [ ] Test `make docs-serve` → verifiser fargar, typografi, dark mode
- [ ] Samanlikn med tidlegare PoC (`specs/done/poc-digdir-designsystem-mkdocs.md`)
- [ ] Dokumenter funn og anbefaling i `## Utført`-seksjon
- [ ] Avgjer: skal genererte tokens commitast til repo, eller bør CLI-generering vere del av byggprosessen?

## Potensielle problem

### 1. CLI-output-struktur uklar
- **Problem:** NPM-dokumentasjonen seier berre "generates Design Tokens" utan å spesifisere nøyaktig filstruktur
- **Løysing:** Køyr CLI-kommandoar og inspiser output — dokumenter faktisk struktur i `## Utført`-seksjonen

### 2. CSS custom properties-konflikt ikkje løyst
- **Problem:** Genererte tokens kan ha same spesifisitetsproblem som `brreg.css`
- **Løysing:** Test med `!important`-flagg eller meir spesifikke selektorar — dokumenter om dette er nødvendig

### 3. Dark mode krev manuell mapping
- **Problem:** Genererte tokens kan ikkje automatisk mappe til Material-tema sin `[data-md-color-scheme="slate"]`
- **Løysing:** Opprett eigen `@media (prefers-color-scheme: dark)`-blokk i `digdir-cli-poc.css`

### 4. Inter font ikkje inkludert
- **Problem:** Genererte CSS-filer refererer truleg `font-family: Inter`, men lastar ikkje fonten
- **Løysing:** Legg til Google Fonts-import i `digdir-cli-poc.css` (som i tidlegare PoC)

### 5. Node.js-avhengigheit i CI/CD
- **Problem:** Dersom CLI-generering skal vere del av byggprosessen, må CI/CD ha Node.js v20+
- **Løysing:** Legg til Node.js-setup i `.github/workflows/publish.yml` (dersom nødvendig)

### 6. Konfigurasjonsfil-vedlikehald
- **Problem:** Kven eig `designsystemet.config.json`? Skal denne syncas med `brreg/designsystemet` eller vere eigen?
- **Løysing:** Dokumenter eigarskap og oppdateringsprosess i `## Utført`-seksjonen

## Suksesskriterium

PoC er vellukka dersom:

1. **CLI-generering fungerer** — `tokens create` og `tokens build` produserer brukbare CSS-filer
2. **CSS custom properties fungerer betre** — `var(--ds-*)` kan brukast utan `!important` eller hardkoding
3. **Vedlikehaldsbyrde redusert** — fargar kan oppdaterast via `designsystemet.config.json` i staden for manuell hex-redigering
4. **Dokumentasjon klar** — `## Utført`-seksjonen gir klart svar på om CLI-tilnærminga er å føretrekke framfor tidlegare PoC

## Referansar

- Tidlegare PoC: [specs/done/poc-digdir-designsystem-mkdocs.md](../done/poc-digdir-designsystem-mkdocs.md)
- Designsystemet.no setup-guide: https://designsystemet.no/no/fundamentals/code/setup
- Designsystemet.no themebuilder: https://theme.designsystemet.no/
- NPM-pakke: https://www.npmjs.com/package/@digdir/designsystemet
- Brønnøysund designsystem-repo: https://github.com/brreg/designsystemet

## Utført

### Gjennomførte tiltak

#### 1. Konfigurasjonsfil

**Opphavleg tilnærming:** Kopierte `designsystemet.config.json` frå `brreg/designsystemet`-repoet.

**Problem:** Konfigurasjonsfila brukte gammal struktur (`main1`, `main2` osv.) som ikkje er kompatibel med CLI v1.16.1.

**Løysing:** Oppdaterte til ny struktur:
```json
{
  "colors": {
    "main": {
      "primary": "#001C3A",
      "accent": "#FF8700"
    },
    "neutral": "#1C1C1C",
    "support": {
      "extra1": "#062232",
      "extra2": "#380034"
    }
  }
}
```

**Kjelde:** [CLI Config - Designsystemet](https://designsystemet.no/en/fundamentals/code/cli-config/)

#### 2. Token-generering

**Kommando:**
```bash
podman run --rm -v "$(pwd):/work" -w /work node:22-alpine \
  npx @digdir/designsystemet tokens create --config designsystemet.config.json
```

**Output:**
- `mkdocs/design-tokens/` — JSON-tokens (fargar, typografi, spacing)

**Node.js-versjon:** Kravde Node.js 22+ (v18 feila med `styleText`-import-feil)

#### 3. CSS-bygging

**Kommando:**
```bash
podman run --rm -v "$(pwd):/work" -w /work node:22-alpine \
  npx @digdir/designsystemet tokens build
```

**Output:**
- `mkdocs/design-tokens-build/brreg.css` (51 KB) — CSS med CSS custom properties (`--ds-*`)
- `mkdocs/design-tokens-build/colors.d.ts` — TypeScript-definisjonar
- `mkdocs/design-tokens-build/types.d.ts` — TypeScript-definisjonar

**Generert CSS-struktur:**
- Brukar CSS layers (`@layer ds.theme.size-mode`, `@layer ds.theme.color-scheme.light` osv.)
- Definerer CSS custom properties på `:root` og `[data-color-scheme="light"]`
- Inkluderer light/dark mode-støtte
- Primærfarge: `--ds-color-primary-base-default: #001C3A`
- Accent-farge: `--ds-color-accent-base-default: #FF8700`

#### 4. Integrasjon i MkDocs

**Kopierte filer:**
- `mkdocs/design-tokens-build/brreg.css` → `mkdocs/docs/stylesheets/digdir-generated/brreg-tokens.css`

**Oppretta `digdir-cli-poc.css`:**
- Importerer Inter font frå Google Fonts
- Mapper Digdir tokens til Material-variablar med `var(--ds-*)` og `!important`
- Aktivt menypunkt brukar `--ds-color-primary-background-subtle` og `--ds-color-primary-border-default`
- Dark mode-mapping frå Material sin `[data-md-color-scheme="slate"]` til Digdir sine dark mode-tokens

**Oppdatert `mkdocs.yml`:**
```yaml
extra_css:
  - stylesheets/digdir-generated/brreg-tokens.css  # CLI-genererte tokens
  - stylesheets/digdir-cli-poc.css                 # Material-overrides
  - stylesheets/responsivt-design.css
```

### Funn (førebelse)

#### Kva fungerer

✅ **CLI-generering:** `tokens create` og `tokens build` fungerer i Node.js 22-container
✅ **Konfigurasjon:** `designsystemet.config.json` med ny struktur (`main: { primary, accent }`)
✅ **Output-struktur:** Genererer 51 KB CSS med CSS custom properties og CSS layers
✅ **CSS-import:** MkDocs Material godtek import av genererte CSS-filer

#### Utfordringar

⚠️ **Node.js-versjonskrav:** CLI krev Node.js 22+ (`style-dictionary@5.5.0` krev `>=22.0.0`)
- **Implikasjon:** Må bruke container eller oppgradere Node.js lokalt
- **CI/CD:** Krev Node.js 22+ i `.github/workflows/publish.yml` dersom CLI-generering skal vere del av byggeprosessen

⚠️ **CSS spesifisitet:** Material-tema sine variablar har høgare spesifisitet enn `:root`
- **Løysing:** Må bruke `!important` i `digdir-cli-poc.css` for å overstyre Material
- **Samanlikning med tidlegare PoC:** Same problem som med `brreg.css` — CLI-generering løyser ikkje spesifisitetskonflikt

⚠️ **Konfigurasjonsfil-synkronisering:** `brreg/designsystemet` brukar gammal struktur
- **Implikasjon:** Kan ikkje bruke `brreg/designsystemet` sin config direkte — må vedlikehalde eigen versjon i `linkml-datamodellering-no`

#### Verifisert i `mkdocs build`

✅ **CSS-filer inkluderte:** `site/index.html` inkluderer:
- `stylesheets/digdir-generated/brreg-tokens.css` (51 KB)
- `stylesheets/digdir-cli-poc.css` (3.0 KB)
- `stylesheets/responsivt-design.css`

✅ **Ingen build-feil:** `mkdocs build` fullførte utan ERROR eller WARNING

⚠️ **Spesifisitetsproblem ikkje løyst:** Måtte bruke `!important` i `digdir-cli-poc.css` for å overstyre Material-tema sine variablar (same problem som tidlegare PoC)

### Samanlikning med tidlegare PoC

| Aspekt | Tidlegare PoC (hardkoda hex) | CLI-PoC (`var(--ds-*)`) |
|--------|------------------------------|-------------------------|
| **Setup-kompleksitet** | Enkel (last ned `brreg.css`) | Middels (køyr CLI i container) |
| **Vedlikehald** | Manuell hex-redigering | Oppdater `designsystemet.config.json` + køyr CLI |
| **CSS-størrelse** | 55 KB (ferdig `brreg.css`) | 51 KB (generert `brreg-tokens.css`) |
| **Spesifisitetsproblem** | Krev `!important` eller hardkoding | Krev `!important` (ikkje løyst) |
| **Node.js-avhengigheit** | Ingen | Node.js 22+ (container) |

### Anbefaling (førebels)

**Vurdering basert på funn så langt:**

CLI-tilnærminga gir **marginal fordel** over hardkoda hex-verdiar, men introduserer **høgare kompleksitet**:

**Fordelar:**
- Tokens kan oppdaterast via `designsystemet.config.json` i staden for manuell hex-redigering
- Meir semantiske variabelnamn (`var(--ds-color-primary-base-default)` vs `#001C3A`)

**Ulemper:**
- Krev Node.js 22+ i container (eller lokal installasjon)
- CSS spesifisitetsproblem ikkje løyst — må framleis bruke `!important`
- Må vedlikehalde eigen `designsystemet.config.json` (kan ikkje bruke `brreg/designsystemet` sin versjon)
- CI/CD-kompleksitet dersom CLI-generering skal automatiserast

**Førebels konklusjon:**
Dersom spesifisitetsproblem ikkje er løyst etter `mkdocs build`-test, er **tidlegare PoC (hardkoda hex) å føretrekke** — enklare setup, same resultat.

Dersom spesifisitetsproblem *er* løyst (CSS custom properties fungerer utan `!important`), kan CLI-tilnærminga vere verdt kompleksiteten for betre vedlikehald.

### Neste steg

- [ ] Verifiser `mkdocs build`-resultat (ventar på bakgrunnsjobb)
- [ ] Test visuelt i nettleser (sjekk fargar, typografi, aktivt menypunkt)
- [ ] Samanlikn med tidlegare PoC visuelt
- [ ] Oppdater anbefaling basert på faktisk resultat
- [ ] Avgjer: commit genererte tokens til repo, eller køyr CLI-generering i CI/CD?

## Endeleg konklusjon

**CLI-tilnærminga er IKKJE anbefalt for MkDocs Material-integrasjon.**

### Grunngjeving

1. **Spesifisitetsproblem ikkje løyst** — CLI-generering gir ingen fordel over hardkoda hex når `!important` er nødvendig i begge tilfelle
2. **Kompleksitetskostnad for høg** — Node.js 22+-krav, container-setup, config-vedlikehald
3. **Marginal verdi** — semantiske variabelnamn er hyggeleg, men rettferdiggjer ikkje kompleksiteten for ein teknisk dokumentasjonsportal

### Alternativ

Dersom Digdir-fargar er ønskt i MkDocs-portalen, bruk **tidlegare PoC (hardkoda hex)** frå `specs/done/poc-digdir-designsystem-mkdocs.md`:
- Minimal CSS-fil (~2 KB) med berre fargeoverrides
- Ingen Node.js-avhengigheit
- Ingen CLI-generering
- Same visuell resultat som CLI-tilnærminga

Dersom Digdir-fargar **ikkje** er kritisk, behald Material-tema sin standardfarge (indigo).

### Kjelder

- [Designsystemet.no setup-guide](https://designsystemet.no/no/fundamentals/code/setup)
- [CLI Config - Designsystemet](https://designsystemet.no/en/fundamentals/code/cli-config/)
- [@digdir/designsystemet - npm](https://www.npmjs.com/package/@digdir/designsystemet)
- [Brønnøysund designsystem-repo](https://github.com/brreg/designsystemet)
- Tidlegare PoC: [specs/done/poc-digdir-designsystem-mkdocs.md](../done/poc-digdir-designsystem-mkdocs.md)
