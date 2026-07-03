# Bidra til linkml-datamodellering-no

## Kven kan bidra

Repoet er ope, og alle kan bidra ved å sende PR frå ein fork. Det er to typar bidragsytarar:

- **Registrerte organisasjonar** — verksemder registrert i `CODEOWNERS.md` med
  eigen modellkatalog. Sjå [GOVERNANCE.md](GOVERNANCE.md) for korleis ein org
  vert registrert.
- **Individuelle bidragsytarar** — alle som vil bidra med modellar, feilretting
  eller verktøyutvikling, anten som del av ein registrert org eller på eiga hand.

## Kom i gang

**NB: Dette er ein Proof of Concept.** Repoet er under aktiv utvikling, og modellar, verktøy og dokumentasjon kan endre seg. Sjå [GOVERNANCE.md](GOVERNANCE.md) for kva stabilitet og support du kan forvente i PoC-fasen.

Om du representerer ein ny organisasjon som ikkje er registrert i `CODEOWNERS.md` enno,
sjå [Bli modelleigar](mkdocs/docs/ny-org.md) først.

Sjå [Ny domenemodell](mkdocs/docs/ny-domenemodell.md) for fullstendig rettleiing om
føresetnader, oppsett, validering og steg-for-steg-instruksjonar for å leggje til ein modell.



## Eigarskap og kodegjennomgang

Kvar domenemodell har ein eigar-org (sjå `CODEOWNERS.md`). GitHub requestar automatisk
review frå rett team basert på `.github/CODEOWNERS`.

For din PR å bli merge-klar:
- Endringar i eigen org sine modellar: godkjenning frå éin person i same org-team
- Endringar i felles infrastruktur: godkjenning frå repo-administrator

Sjå [GOVERNANCE.md](GOVERNANCE.md) for fullstendig forklaring av roller og myndigheit.


## Scope og prinsipp

For fullstendig oversikt over kva repoet er (og ikkje er), modelleringsprinsipp og namnekonvensjonar, sjå [specs/done/oversikt-avgrensingar-prinsipp.md](specs/done/oversikt-avgrensingar-prinsipp.md).

## Modellkatalog

Kvar org skal liste **alle** sine skjema i sin modellkatalog
(`src/linkml/modellkatalog/<alias>-modellkatalog/`), også utkast som ikkje er ferdige
enno (`annotations.status: http://purl.org/adms/status/UnderDevelopment`). Sjå
[Ny organisasjon](mkdocs/docs/ny-org.md) steg 4 for korleis katalogen synkroniseres med
`make update-modellkatalog`.

## Generer artefakter lokalt

```bash
make <domain>          # t.d. make ngr, make ap-no, make fair
make docs-serve        # start lokal dokumentasjonsportal på http://localhost:8000
```

## Automatisk forvalta felt

Tre felt i kvar skjema-YAML-fil vert oppdaterte automatisk av CI — **ikkje rediger desse manuelt**:

| Felt | Forvaltingsmekanisme |
|---|---|
| `version` | release-please oppdaterer via JSONPath i release-PR |
| `annotations.endringsdato` | må oppdaterast manuelt før release |
| `annotations.utgivelsesdato` | må oppdaterast manuelt ved første release (éin gong) |

Oppdateringa av `version` skjer automatisk i release-PR. Datoannotasjonar må oppdaterast manuelt.

## Korleis utløyse ein release

Release-arbeidsflyten er todelt: **automatisk PR-oppretting** og **manuell release-publisering**.

### Steg 1: Automatisk release-PR-oppretting

Release-please opprettar automatisk ein release-PR når du pushar `feat:` eller `fix:`-commits til `main`:

1. Push ein commit med `feat:` eller `fix:` til `main`
2. `release-please.yml` workflow triggar automatisk
3. Workflow opprettar/oppdaterer ein release-PR basert på Conventional Commits sidan siste release
4. PR inneheld versjonsbump i `*-schema.yaml`, oppdatert `CHANGELOG.md` og oppdatert `.release-please-manifest.json`

**Manuell trigger** (valfritt):

1. Gå til [Actions → Release Please](https://github.com/brreg/linkml-datamodellering-no/actions/workflows/release-please.yml)
2. Klikk **Run workflow** → velg branch → **Run workflow**

### Steg 2: Merge release-PR

1. Gjennomgå endringar i release-PR-en
2. Vent på at `validate.yml` passerer
3. **Godkjenn og merge PR-en manuelt**

### Steg 3: Manuell release-publisering

Etter merge må du opprette GitHub Release manuelt (krev repo-admin-tilgang).

**Alternativ A: Via GitHub UI**

1. Gå til [Releases](https://github.com/brreg/linkml-datamodellering-no/releases) → **Draft a new release**
2. **Choose a tag:** Skriv tag-namn frå release-PR (t.d. `samt-bu-v1.0.4`) → **Create new tag on publish**
3. **Release title:** `samt-bu 1.0.4` (komponent + versjon)
4. **Description:** Kopier frå `CHANGELOG.md` eller skriv manuelt
5. **Publish release**

**Alternativ B: Via GitHub CLI**

```bash
# Eksempel for samt-bu
VERSION=$(jq -r '."src/linkml/samt/samt-bu"' .release-please-manifest.json)
gh release create "samt-bu-v${VERSION}" \
  --title "samt-bu ${VERSION}" \
  --notes "Release ${VERSION} for samt-bu"
```

For fleire komponentar i same release-PR, opprett ein release per komponent.

Sjå [monitorering.md](mkdocs/docs/monitorering.md#release-arbeidsflyt) for flytdiagram og meir detaljar.

**Versjonering følgjer Conventional Commits automatisk:**
- `fix:` → patch-bump (0.0.X)
- `feat:` → minor-bump (0.X.0)
- `feat!:` eller `BREAKING CHANGE:` → major-bump (X.0.0)

## Commit-meldingar

Repoet nyttar [Conventional Commits](https://www.conventionalcommits.org/)-formatet:

```
<type>(<scope>): <skildring>
```

| Type | Semver-effekt | Bruksområde |
|---|---|---|
| `feat` | MINOR | Ny klasse, nytt slot |
| `fix` | PATCH | Rettjing av feil range, URI o.l. |
| `refactor` | PATCH | Omstrukturering utan semantisk endring |
| `docs` | — | Skildringar, README, portalinnhald |
| `chore` | — | CI, skript, manifest utan modellendringar |
| `feat!` / `fix!` | MAJOR | Brotande endring (legg til `!` eller `BREAKING CHANGE:`-footer) |

**Scope** er modellnamnet i kebab-case, same som katalognamnet under `src/linkml/`:

```
feat(ngr-adresse): legg til postnummer-slot
fix(dcat-ap-no): rett feil range på kontaktpunkt-slot
feat!(fint-administrasjon): fjern utgått klasse
docs(samt-bu): oppdater skildringar
chore(*): oppdater CI-konfigurasjon
```

Bruk `*` for endringar som ikkje tilhøyrer éin bestemt modell. CI validerer
commit-format automatisk via commitlint.

## Nye verktøyavhengigheiter

Legger du til eit nytt verktøy i `Dockerfile*`, `requirements*.txt` eller
`.github/workflows/*.yml` — vurder om verktøyet endar opp bundla i eit
containerbilete eller ein artefakt som publiseres (GHCR, GitHub Pages).
I så fall: sjekk lisensen og legg verktøyet til i attributions-tabellen i
[`mkdocs/docs/om.md`](mkdocs/docs/om.md) dersom lisensen krev det (typisk MIT,
BSD, Apache-2.0, EPL). Sjå
[`specs/done/verktoy-lisensoversikt.md`](specs/done/verktoy-lisensoversikt.md)
for metode og eksisterande klassifisering.

## Sikkerheit og personvern

**VIKTIG:** Legg aldri inn sensitive data i modellar eller datafiler.

### Kva du IKKJE skal legge inn

- ❌ **Personopplysningar:** Namn, e-postadresser, telefonnummer, fødselsnummer, personnummer
- ❌ **Konfidensielle data:** Interne forretningshemmelegheiter, ikkje-offentlege organisasjonsdata
- ❌ **Testdata med verkelege verdiar:** Bruk syntetiske/fiktive verdiar i eksempelfiler
- ❌ **Credentials:** Passord, API-nøklar, tokens (desse skal aldri vere i git)

### Kva du KAN legge inn

- ✅ **Offentlege organisasjons-URI-ar:** `https://data.norge.no/organizations/<orgnr>`
- ✅ **Offentlege Los-tema:** `https://psi.norge.no/los/tema/naring`
- ✅ **Syntetiske eksempeldata:** Fiktive namn som "Ola Nordmann", "Eksempel AS"
- ✅ **Offentlege standardar og vokabularar:** DCAT, SKOS, FOAF, osv.

### Dersom du oppdagar sensitive data

1. **Ikkje commit eller push** dersom du oppdagar sensitive data lokalt — fjern dei først
2. **Dersom allereie pusha:** Opne ein GitHub Issue med merkelappen `data-quality` og `urgent` — **ikkje inkluder dei sensitive dataa i issue-beskrivinga**
3. **Kontakt katalogeigarleiinga** for den aktuelle organisasjonen (sjå `CODEOWNERS.md`)

Sjå [SECURITY.md](SECURITY.md) for fullstendig sikkerheitspolicy.

---

## Pull request

1. Opprett ein ny branch frå `main`
2. Gjer endringar og valider lokalt:
   - `make lint SCHEMA=...` og `make validate-instance SCHEMA=... INSTANCE=...`
   - `make mcp-linkml-validate SCHEMA=...` (brukar `validation_policy` frå manifest.yaml, eller overstyr med `POLICY=bronze`)
3. **Verifiser at du ikkje har lagt inn personopplysningar eller sensitive data**
4. Opprett pull request mot `main` — CI køyrer validering automatisk

Rapporter sikkerheitssårbarheiter i infrastruktur via e-post (sjå [SECURITY.md](SECURITY.md)) — ikkje som public issue.

---

## Support og feilsøking

### PoC-status: Ingen garantert support

Dette repoet er ein **Proof of Concept** og har ingen garantert support-SLA:

- ❌ Ingen garantert responstid på GitHub Issues
- ❌ Ingen garantert feilretting innan bestemte tidsfrister
- ❌ Ingen 24/7-support eller varslingssystem
- ✅ Best-effort-support frå repo-administrator og bidragsytarar
- ✅ Community-driven feilsøking via GitHub Issues og Discussions

### Rapportering av feil

| Type problem | Rapporteringsmåte | Ansvarleg |
|---|---|---|
| **Bug i felles infrastruktur** (CI/CD, Makefile, validator, generatorar) | GitHub Issue med merkelapp `bug` | Repo-administrator |
| **Bug i domenemodell** (feil URI, ugyldig YAML, manglande metadata) | GitHub Issue med merkelapp `bug` + tag katalogeigarleiing | Katalogeigarleiing for org |
| **Datakvalitet** (TODO-verdiar, mangelfull dokumentasjon) | GitHub Issue med merkelapp `data-quality` | Katalogeigarleiing for org |
| **Sikkerheitssårbarheit** (infrastruktur, CI/CD) | **E-post til ave@brreg.no** (IKKJE public issue) | Repo-administrator |
| **Personopplysningar i data** | GitHub Issue med merkelapp `data-quality` + `urgent` | Katalogeigarleiing for org |

### Ansvarsfordeling

**Repo-administrator sitt ansvar:**
- Vedlikeheld felles infrastruktur (AP-NO-profilar, FAIR-metadata, CI/CD, validator, generatorar)
- Triagerer og prioriterer issues som gjeld felles infrastruktur
- Hjelper eksterne organisasjonar med onboarding og tekniske spørsmål

**Katalogeigarleiing sitt ansvar:**
- Vedlikeheld eigne domenemodeller og modellkatalog
- Triagerer og løyser issues som gjeld eigne modellar
- Svarar på spørsmål om eigne modellar frå andre brukarar

**Bidragsytarar sitt ansvar:**
- Rapporterer feil og forbetringsforslag via GitHub Issues
- Sender PR-ar for feilrettingar og forbetringar
- Hjelper andre brukarar i GitHub Discussions (dersom aktivert)

### Kjende avgrensingar

Sjå [specs/bugs/README.md](https://github.com/brreg/linkml-datamodellering-no/blob/main/specs/bugs/README.md) for fullstendig liste over kjende bugs og workarounds.

Kvar rettleiing har òg ein "Kjende avgrensingar"-seksjon nedst som listar opp avgrensingar spesifikke for den arbeidsflyta.

### Kva du kan forvente i PoC-fasen

**Sannsynleg responstid frå repo-administrator:**
- Kritiske sikkerheitssårbarheiter: 1 arbeidsdagdag
- Blokkerar-bugs i felles infrastruktur: 3-5 arbeidsdagar
- Feature-forespurnader: Best-effort, ingen garantert tidsramme
- Spørsmål og diskusjonar: Best-effort, når kapasitet er tilgjengeleg

**Kva du MÅ gjere sjølv:**
- Feilsøke problemer i eigne domenemodeller
- Validere data før publisering (`make mcp-linkml-validate SCHEMA=...` — brukar automatisk `validation_policy` frå manifest.yaml)
- Teste genererte artefaktar lokalt før push
- Lese dokumentasjon og eksisterande issues før du rapporterer nye problem

### Få hjelp

1. **Les dokumentasjonen først:** [brreg.github.io/linkml-datamodellering-no](https://brreg.github.io/linkml-datamodellering-no/)
2. **Søk i eksisterande issues:** Nokon andre kan ha rapportert same problemet
3. **Sjekk kjende avgrensingar:** [specs/bugs/README.md](https://github.com/brreg/linkml-datamodellering-no/blob/main/specs/bugs/README.md)
4. **Opne ein ny issue:** Med merkelapp `bug`, `question` eller `data-quality`
5. **Vær tolmodig:** Dette er ein PoC med avgrensa ressursar
