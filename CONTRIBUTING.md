# Bidra til linkml-datamodellering-no

## Kven kan bidra

Repoet er ope, og alle kan bidra ved å sende PR frå ein fork. Det er to typar bidragsytarar:

- **Registrerte organisasjonar** — verksemder registrert i `CODEOWNERS.md` med
  eigen modellkatalog. Sjå [GOVERNANCE.md](GOVERNANCE.md) for korleis ein org
  vert registrert.
- **Individuelle bidragsytarar** — alle som vil bidra med modellar, feilretting
  eller verktøyutvikling, anten som del av ein registrert org eller på eiga hand.

## Kom i gang

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
| `version` | release-please oppdaterer via JSONPath etter merge av release-PR |
| `annotations.endringsdato` | `update-schema-dates.py` set til releasedato etter kvar release |
| `annotations.utgivelsesdato` | `update-schema-dates.py` set til releasedato ved første release (éin gong) |

Oppdateringa skjer automatisk etter at ein release-PR er merge-a til `main`.
Du treng ikkje gjere noko — CI commit-ar endringane med meldinga `chore(*): oppdater datoannotasjonar etter release [skip ci]`.

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

## Pull request

1. Lag ein ny branch frå `main`
2. Gjer endringar og valider lokalt:
   - `make lint SCHEMA=...` og `make validate-instance SCHEMA=... INSTANCE=...`
   - `make mcp-validate SCHEMA=... POLICY=bronze` (minimumskrav før PR)
3. Send inn pull request mot `main` — CI køyrer validering automatisk

Rapporter sikkerheitssårbarheiter via e-post (sjå [SECURITY.md](SECURITY.md)) — ikkje som public issue.
