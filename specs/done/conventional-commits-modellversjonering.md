# Conventional commits for modellversjonering

## Bakgrunn

Versjonsfelta i skjema-YAML-filene (t.d. `version: "1.0.0"`) vert i dag oppdaterte manuelt
og utan tydeleg samanheng med endringshistorikken i git. Det er vanskeleg å sjå kva
commit som utløyste ei versjonsbump, kva type endring det var (brot, ny funksjon,
rettjing), og om versjonen stemmer med faktisk endringshistorikk.

Conventional Commits-standarden gir eit maskinlesbart og menneskevenleg format for
commit-meldingar som kan brukast til automatisk å berekne og oppdatere `version:`-feltet
i kvar modell, og generere Git-taggar per modell.

---

## Commit-format

```
<type>(<scope>): <skildring>

[valfri kropp]

[valfri footer, t.d. BREAKING CHANGE: <melding>]
```

### Typar og deira effekt på semantisk versjonering

| Type | Semver-bump | Bruksområde |
|---|---|---|
| `feat` | MINOR | Ny klasse, nytt slot, nytt obligatorisk felt (ikkje brot) |
| `fix` | PATCH | Rettjing av feil (feil range, feil URI, manglande `required`) |
| `refactor` | PATCH | Omstrukturering utan semantisk endring |
| `docs` | — | Endring i `description`-felt, `description.md`, `README.md` |
| `chore` | — | Vedlikehald av CI, skript, manifest utan modellendringar |
| `feat!` / `fix!` | MAJOR | Kvar type med `!`-suffiks = brotande endring |
| `BREAKING CHANGE:` | MAJOR | Footer i commit-kropp (alternativ til `!`) |

Brotande endringar er t.d.: sletting av klasse/slot, endring av `slot_uri`/`class_uri`,
strenge-typar som smalnar inn (LangString → string), sletting av obligatorisk slot.

### Scope = modellnamn (kebab-case)

Scope identifiserer kva modell committen gjeld. Bruk same namn som katalognamnet
under `src/linkml/`:

```
feat(ngr-adresse): legg til postnummer-slot
fix(dcat-ap-no): rett feil range på kontaktpunkt-slot
feat!(fint-administrasjon): fjern utgått AnsettelsesforholdResource-klasse
docs(samt-bu): oppdater skildringar for budsjettposter
chore(*): oppdater CI-konfigurasjon
```

Bruk `*` for endringar som ikkje tilhøyrer éin bestemt modell (CI, docs, scripts).

---

## Versjonsstrategi per modell

### Berekne ny versjon

For kvar modell: gå gjennom alle commits sidan siste versjonstagg for den modellen
(`<modell>/v<major>.<minor>.<patch>`), og vel høgaste bump-nivå blant commitane:

```
BREAKING CHANGE / <type>!  →  MAJOR
feat                        →  MINOR
fix / refactor              →  PATCH
docs / chore                →  (ingen bump)
```

Har ein periode berre `docs`- og `chore`-commits, vert ingen ny versjon laga.

### Git-tagg per modell

Kvart modell-versjon vert tagga med:

```
<modellnamn>/v<major>.<minor>.<patch>

Eksempel:
  ngr-adresse/v1.3.0
  dcat-ap-no/v2.1.0
  fint-administrasjon/v5.0.0
```

Dette gjer det mogleg å ha ulike versjonar for ulike modellar i same repo,
og å sjå endringshistorikken per modell via `git log ngr-adresse/v1.2.0..HEAD`.

---

## Handtering av kryss-modell-endringar

Nokre endringar påverkar fleire modellar, særleg:

- Endringar i `common-ap-no` eller `fint-common` påverkar alle som importerer dei
- Endringar i `dcat-ap-no` påverkar domenemodellane som importerer profilen

**Regel:** Commit-forfattar er ansvarleg for å liste *alle* påverka scopes i committen.
Fleire scopes separerast med komma:

```
feat(dcat-ap-no,ngr-adresse): …
```

Alternativt kan dette gjerast som separate commits per modell dersom endringane er
logisk åtskilde.

CI-verktøyet summar bump-nivå per scope, ikkje per commit.

---

## Automatisering (CI)

### Tilnærming: release-please (Google)

`release-please` er eit containerisert GitHub Actions-verktøy som:
1. Les conventional commits sidan siste release
2. Oppdaterer versjonsfelt i angitte filer automatisk
3. Opnar ein "Release PR" med oppdatert CHANGELOG og versjonsfelt
4. Lagar Git-taggen når Release PR vert merge

Dette passar godt fordi ingen installasjon lokalt krevst — alt køyrer i container.

#### Konfigurasjon

`release-please` støttar monorepos via `release-please-config.json`:

```json
{
  "$schema": "https://raw.githubusercontent.com/googleapis/release-please/main/schemas/config.json",
  "packages": {
    "src/linkml/ngr/ngr-adresse": {
      "component": "ngr-adresse",
      "release-type": "simple",
      "extra-files": [
        {
          "type": "yaml",
          "path": "src/linkml/ngr/ngr-adresse/ngr-adresse-schema.yaml",
          "jsonpath": "$.version"
        }
      ]
    },
    "src/linkml/ap-no/dcat-ap-no": {
      "component": "dcat-ap-no",
      "release-type": "simple",
      "extra-files": [
        {
          "type": "yaml",
          "path": "src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml",
          "jsonpath": "$.version"
        }
      ]
    }
  }
}
```

Alle modellar som har `version:`-felt i schema-YAML vert lagt til i `packages`.

#### GitHub Actions-workflow

```yaml
# .github/workflows/release-please.yml
name: Release Please

on:
  push:
    branches: [main]

jobs:
  release-please:
    runs-on: ubuntu-latest
    steps:
      - uses: googleapis/release-please-action@v4
        with:
          config-file: release-please-config.json
          manifest-file: .release-please-manifest.json
```

`.release-please-manifest.json` inneheld siste kjende versjon per modell og vert
vedlikehalde automatisk av `release-please`.

---

## Innføringsstrategi (trinnvis)

### Trinn 1 — Konvensjon og dokumentasjon

Dokumenter commit-formatet i `CONTRIBUTING.md` (ny fil) og legg til commitlint-konfig.
Ingen automatisering enno — berre einigheit om formatet.

Legg til `commitlint`-sjekk i CI:
```yaml
# Køyrer som container i eksisterande validate-workflow
- name: Lint commit messages
  run: |
    podman run --rm -v "$PWD:/repo" \
      commitlint/commitlint:latest \
      --from origin/main --to HEAD
```

### Trinn 2 — Manuell versjonsbump med verktøy

Legg til eit lokalt skript `src/assets/scripts/bump-version.sh` som:
1. Les commits sidan siste tagg for ein gjeven modell
2. Bereknar ny semver
3. Skriv ny `version:`-verdi til schema-YAML
4. Lagar Git-tagg

```bash
# Bruk:
./src/assets/scripts/bump-version.sh ngr-adresse
```

Gjer det mogleg å køyre manuelt utan full CI-automatisering.

### Trinn 3 — release-please i CI

Sett opp `release-please-config.json` og GitHub Actions-workflow som beskriven ovanfor.
Generer initial `.release-please-manifest.json` frå noverande `version:`-verdiar i alle skjema.

---

## Handtering av modellar utan `version:`-felt

Nokre modellar (t.d. `referanse-schema.yaml`) har versjonsfelt, medan andre manglar det.

**Regel:** Modellar som er publiserte eksternt (dvs. `publish_external: true` i `manifest.yaml`)
**skal** ha `version:`-felt. Andre modellar kan velje det til.

---

## LLM-arbeidsflyt: utkast til commit-melding

Kvar gong ein LLM-agent utfører ein spesifikasjon frå `specs/backlog/`, skal den
avslutte med eit utkast til commit-melding i conventional commits-format. Dette
gjer det enkelt for brukaren å velje rett type og scope utan å kjenne formatet utanåt.

Instruksjonen skal inn i `CLAUDE.md` slik at all LLM-assistert spec-gjennomføring
følgjer same mønster:

```markdown
Når alle tiltak i ein spesifikasjon er utførte, generer eit utkast til commit-melding
i conventional commits-format (sjå `specs/backlog/conventional-commits-modellversjonering.md`):

<type>(<scope>): <skildring>

Eksempel: feat(ngr-adresse): legg til postnummer-slot
```

---

## Prioritert tiltaksliste

| # | Tiltak | Avhengigheit | Prioritet |
|---|---|---|---|
| 1 | Skriv `CONTRIBUTING.md` med commit-format og scope-konvensjon | — | Høg |
| 2 | Legg til `commitlint`-sjekk i CI (container, ingen lokal installasjon) | Tiltak 1 | Høg |
| 3 | Lag `bump-version.sh` — manuelt semver-skript per modell | Tiltak 1 | Medium |
| 4 | Lag `release-please-config.json` for alle modellar med `version:` | Tiltak 3 | Medium |
| 5 | Legg til `release-please`-workflow i GitHub Actions | Tiltak 4 | Medium |
| 6 | Generer initial `.release-please-manifest.json` frå eksisterande versjonar | Tiltak 4 | Medium |
| 7 | Krev `version:` i manifest-validering for `publish_external: true`-modellar | Tiltak 5 | Lav |
| 8 | Legg til instruksjon i `CLAUDE.md` om å generere commit-meldings-utkast etter spec-gjennomføring | — | Høg |

---

## Utført

Utført 2026-06-10.

**Tiltak 1 — `CONTRIBUTING.md`:** Ny seksjon «Commit-meldingar» med tabell over typar og
semver-effekt, scope-konvensjon og døme. Lenke til Conventional Commits-standarden.

**Tiltak 2 — commitlint i CI:** Ny `commitlint`-jobb i `validate.yml`, køyrer berre på
pull requests, nyttar `node:22-alpine`-container utan lokal installasjon.

**Tiltak 3 — `bump-version.sh`:** Oppretta i `src/assets/scripts/`. Finn siste tagg per
modell, les commits, bestemmer bump-nivå (major/minor/patch/none), oppdaterer `version:`
i schema-YAML og lagar Git-tagg. Støttar `--dry-run`.

**Tiltak 4 — `release-please-config.json`:** Generert for alle 21 skjema med `version:`-felt
(inkl. dei fem NGR/oreg-skjemaa som vart lagt til i tiltak 7).

**Tiltak 5 — `release-please.yml`:** Ny GitHub Actions-workflow på push til `main`.

**Tiltak 6 — `.release-please-manifest.json`:** Generert frå eksisterande `version:`-verdiar
i alle skjema.

**Tiltak 7 — krav om `version:` for publish_external:** Fem skjema mangla `version:`
(`ngr-adresse`, `ngr-eiendom`, `ngr-person`, `ngr-virksomhet`, `register-over-aksjeeiere`) —
alle fekk `version: "1.0.0"`. Ny `check-publish-version`-jobb i `validate.yml` feilar CI
viss eit `publish_external: true`-skjema manglar `version:`.

**Avvik:** commitlint køyrer i `validate.yml` (ikkje eigen workflow) for å halde
CI-strukturen enkel. Validering av commit-format skjer berre på pull requests, ikkje på
direkte push til `main`.
