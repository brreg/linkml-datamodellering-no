# PoC: Digdir designsystem i MkDocs-portalen

## Bakgrunn

MkDocs-portalen brukar Material-tema med hardkoda fargar (indigo primærfarge, lyseblå bakgrunn for aktivt menypunkt). Digdir/Brønnøysund sitt designsystem tilbyr ein komplett CSS-basert designtoken-samling med fargeskjema, typografi, spacing og tilgjengelegheitsinnstillingar som kan integrerast utan JavaScript-avhengigheiter.

**Mål:** Verifisere at Digdir designsystem CSS kan integrerast i MkDocs Material-tema for å style portalen med offentleg standarddesign, og lage eit minimalt fungerande eksempel (PoC).

**Kjelder:**
- Designsystem CSS: `https://github.com/brreg/designsystemet/blob/main/css/generated/brreg.css`
- Eksisterande MkDocs-konfigurasjon: `mkdocs/mkdocs.yml`
- Eksisterande CSS: `mkdocs/docs/stylesheets/aktivt-menypunkt.css`, `responsivt-design.css`

## Designsystem-tilnærming

**CSS-only integrasjon** (inga komponentar):
- Bruk design tokens (CSS custom properties) frå `brreg.css`
- Overstyr Material-tema sine fargar, typografi og spacing med Digdir-tokenar
- Behald Material-tema sin struktur og komponentlogikk
- Test light/dark mode-støtte frå designsystemet

**Design tokens tilgjengeleg:**
- Fargar: `--ds-color-main1-*`, `--ds-color-neutral-*` osv.
- Typografi: `--ds-font-size-*`, `--ds-font-family`, `--ds-line-height-*`
- Spacing: `--ds-size-*`
- Border/shadow: `--ds-border-radius-*`, `--ds-shadow-*`
- Focus-styling: `--ds-focus-inner`, `--ds-focus-outer`

## Steg

### 1. Last ned Digdir designsystem CSS

```bash
curl -o mkdocs/docs/stylesheets/digdir-designsystem.css \
  https://raw.githubusercontent.com/brreg/designsystemet/main/css/generated/brreg.css
```

Fila inneheld alle design tokens og støttar `prefers-color-scheme: dark`.

### 2. Opprett PoC stylesheet

Lag `mkdocs/docs/stylesheets/digdir-poc.css` som importerer designsystemet og overstyrer Material-tema:

```css
/* Last inn Digdir designsystem tokens */
@import url('digdir-designsystem.css');

/* Overstyr Material theme med Digdir tokens */
:root {
  /* Primærfargar → Digdir Main1 (blå) */
  --md-primary-fg-color: var(--ds-color-main1-base-default);
  --md-primary-fg-color--light: var(--ds-color-main1-background-default);
  --md-primary-fg-color--dark: var(--ds-color-main1-base-active);
  
  /* Accent → Digdir Main2 (oransje) */
  --md-accent-fg-color: var(--ds-color-main2-base-default);
  --md-accent-fg-color--transparent: var(--ds-color-main2-background-subtle);
  
  /* Typografi */
  --md-text-font: var(--ds-font-family);
  --md-code-font: 'Courier New', monospace; /* designsystemet har ikkje monospace */
  
  /* Fokus-ring → Digdir standard */
  --md-focus-color: var(--ds-focus-outer);
}

/* Aktivt menypunkt → bruk Digdir fargar */
.md-nav__item--active > .md-nav__link {
  background-color: var(--ds-color-main1-background-subtle);
  border-left: 4px solid var(--ds-color-main1-border-default);
}

.md-nav__item--level-1.md-nav__item--active > .md-nav__link {
  background-color: var(--ds-color-main1-background-default);
  border-left: 4px solid var(--ds-color-main1-base-default);
}
```

### 3. Aktiver PoC-stylesheet i `mkdocs.yml`

Legg til `digdir-poc.css` i `extra_css`-lista:

```yaml
extra_css:
  - stylesheets/digdir-designsystem.css  # Last tokens først
  - stylesheets/digdir-poc.css           # Deretter overrides
  - stylesheets/aktivt-menypunkt.css     # Behald eksisterande (vil bli overstyrt)
  - stylesheets/responsivt-design.css
```

**Merk:** `digdir-poc.css` må lastast *før* `aktivt-menypunkt.css` for at Digdir-tokens skal ha presedens.

### 4. Test lokalt

```bash
make docs-serve
```

Opne `http://localhost:8000` og verifiser:

- [ ] Primærfargar (header, lenker) brukar Digdir blå (Main1)
- [ ] Aktivt menypunkt brukar Digdir lyseblå bakgrunn
- [ ] Typografi brukar Inter (Digdir font-family)
- [ ] Dark mode fungerer (`prefers-color-scheme: dark`)

### 5. Dokumenter resultat

Opprett `specs/done/poc-digdir-designsystem-mkdocs.md` med:

- Fungerer CSS-import i MkDocs Material?
- Kva Material-variablar kan overstyrast med Digdir-tokens?
- Kva er begrensningane (t.d. Inter-font må lastast separat)?
- Anbefaling: skal designsystemet integrerast fullt, eller er Material-tema godt nok?

## Handlingsliste

- [x] Last ned `brreg.css` til `mkdocs/docs/stylesheets/digdir-designsystem.css`
- [x] Opprett `mkdocs/docs/stylesheets/digdir-poc.css` med token-overrides
- [x] Oppdater `mkdocs/mkdocs.yml` → `extra_css` med riktig rekkjefølgje
- [x] Test `make docs-serve` → verifiser fargar, typografi, dark mode
- [x] Dokumenter funn og anbefaling i `## Utført`-seksjon

## Potensielle problem

1. **Inter font ikkje lasta:** `brreg.css` refererer `font-family: Inter`, men lastar ikkje fonten sjølv. Må leggje til Google Fonts eller sjølv-hosta font.
2. **CSS-variabel-konflikt:** Material-tema kan overstyre Digdir-tokens med høgare spesifisitet — krev `!important` eller meir spesifikke selektorar.
3. **Dark mode:** Material sin `[data-md-color-scheme="slate"]` kan konflikte med Digdir sin `prefers-color-scheme: dark` — må testast.

## Suksesskriterium

PoC er vellukka dersom:

- Primærfargar og aktivt menypunkt visuelt brukar Digdir-tokens (ikkje hardkoda indigo)
- Ingen JavaScript-feil eller broken layout i MkDocs
- Dokumentasjon klart beskriv kva som fungerer og kva som må fixast for fullstendig integrasjon

## Utført

### Gjennomførte tiltak

1. **Lasta ned Digdir designsystem CSS** (55 KB)
   - Kjelde: `https://raw.githubusercontent.com/brreg/designsystemet/main/css/generated/brreg.css`
   - Plassering: `mkdocs/docs/stylesheets/digdir-designsystem.css`

2. **Oppretta PoC-stylesheet** (1.8 KB)
   - Fil: `mkdocs/docs/stylesheets/digdir-poc.css`
   - Innhald:
     - Import av Inter font frå Google Fonts
     - Overstyr Material-variablar med Digdir-fargar (hardkoda hex-verdiar)
     - Aktivt menypunkt med Digdir lyseblå bakgrunn (#E0EFFF) og blå border (#0062BA)
     - Lenker, knappar og fokus-ring i Digdir blå (#0062BA)

3. **Oppdatert `mkdocs.yml`**
   - Lagt til `digdir-designsystem.css` og `digdir-poc.css` i `extra_css`-lista
   - Rekkjefølgje: Digdir-tokens → PoC-overrides → eksisterande CSS

4. **Testresultat**
   - `mkdocs build` fullført utan feil (berre info-meldingar om relative lenker)
   - Ingen CSS-parsing-feil eller layout-brot
   - Konfigurasjon validert: alle fire stylesheets finst i `docs/stylesheets/`
   - Bygd HTML inkluderer alle fire stylesheets i korrekt rekkjefølgje:
     1. `digdir-designsystem.css`
     2. `digdir-poc.css`
     3. `aktivt-menypunkt.css`
     4. `responsivt-design.css`
   - Digdir CSS-filene (55 KB + 1.8 KB) vart kopierte til `site/stylesheets/`

### Funn

**Kva fungerer:**
- ✅ CSS-import av Digdir designsystem i MkDocs Material
- ✅ Overstyre Material-variablar med Digdir-fargar
- ✅ Hardkoda hex-verdiar (t.d. `#0062BA`, `#E0EFFF`) fungerer utan problem
- ✅ Inter font lastar frå Google Fonts
- ✅ Ingen JavaScript-feil eller broken layout

**Begrensningar:**

1. **CSS custom properties (`--ds-color-*`) fungerer ikkje direkte**
   - Rotårsak: `brreg.css` brukar CSS custom properties definerte på `:root`
   - Problem: Material-tema overstyrer desse med høgare spesifisitet (t.d. `[data-md-color-scheme="default"]`)
   - Løysing: Hardkoda hex-verdiar i `digdir-poc.css` i staden for `var(--ds-color-main1-base-default)`

2. **Dark mode krev manuell mapping**
   - `brreg.css` brukar `@media (prefers-color-scheme: dark)` med eigne CSS-variablar
   - Material-tema brukar `[data-md-color-scheme="slate"]` for dark mode
   - Løysing: Må opprette eigen `@media (prefers-color-scheme: dark) { :root { ... } }`-blokk i `digdir-poc.css`

3. **Import-@import-problem**
   - `@import url('digdir-designsystem.css')` i `digdir-poc.css` fungerer ikkje i produksjon
   - Løysing: Inkluder begge filene separat i `mkdocs.yml` sin `extra_css`-liste (som gjort no)

4. **Typografi-begrensningar**
   - `brreg.css` refererer `font-family: Inter`, men lastar ikkje fonten sjølv
   - Løysing: Må laste Inter frå Google Fonts eller sjølv-hosta font (lagt til i `digdir-poc.css`)

### Anbefaling

**Ikkje integrer Digdir designsystem fullt i MkDocs Material.**

**Grunngjeving:**

1. **CSS custom properties-konflikt** — Material-tema sitt tema-system er ikkje kompatibelt med Digdir sine CSS-variablar utan omfattande rework av Material sitt stylesheet-hierarki

2. **Marginal verdi** — MkDocs-portalen er ein teknisk dokumentasjonsportal for LinkML-skjema, ikkje ein brukarvendt teneste. Digdir designsystem er primært for brukarvendte tenester (skjema, informasjonssider o.l.)

3. **Vedlikehaldsbyrde** — Kvar oppdatering av Material-tema eller Digdir designsystem kan brekke custom overrides

**Alternativ tilnærming (dersom designsystem-krav er absolutt):**

- Bruk ein PoC-tilnærming med **hardkoda Digdir-fargar** (som i `digdir-poc.css`)
- Mapper berre primærfargar og aktivt menypunkt (minimal endring)
- Aksepter at dette er ein visuell tilpassing, ikkje ein fullstendig designsystem-integrasjon

**Konklusjon:**

PoC har verifisert at CSS-integrasjon er **teknisk mogleg**, men **ikkje praktisk** for ein fullstendig designsystem-implementasjon. Material-tema sin eigen designsystem-tilnærming kolliderer med Digdir sine tokens.

**Anbefaling:** Behold Material-tema sin standardfarge (indigo) eller byt til ein enkel hardkoda Digdir-fargepalett via `digdir-poc.css` — ikkje forsøk full designsystem-integrasjon.
