# Plan: rett bokmålsforma "domenemodeller" til nynorsk "domenemodellar"

## Bakgrunn og motivasjon

`CLAUDE.md` § «Skriftspråk» slår fast at dokumentasjon (README, mkdocs-sider,
spesifikasjonar) skal skrivast på nynorsk, medan sjølve modelleringa
(klassenamn, slotnamn, skildringar i `.yaml`-skjema) skal vere bokmål.

Ordet **"domenemodeller"** (ubunden fleirtal, bokmålsform) er brukt konsekvent
i nynorsk løpetekst gjennom repoet, der den korrekte nynorske forma er
**"domenemodellar"**. Dette er same type retting som `890867af` gjorde for
"applikasjonsprofiler" → "applikasjonsprofilar".

Relaterte ord som **ikkje** skal endrast fordi dei alt er korrekte/upåverka:
- `domenemodell` (eintal, ubunden) — same form i bokmål og nynorsk
- `domenemodellen` (eintal, bunden) — same form i bokmål og nynorsk (hankjønnsord)
- `domenemodellane` (fleirtal, bunden) — alt korrekt nynorsk
- `domenemodellering`, `domenemodellklassar` — andre ord/samansetjingar, upåverka

## Omfang

39 førekomstar av `domenemodeller`/`Domenemodeller` i 17 kjeldefiler.
`specs/done/` er eksplisitt utelate (arkiverte specs skal stå urørte, jf.
CLAUDE.md § DRY-prinsipp).

**Genererte filer er utelatne** (gitignora, regenererte automatisk av
`make docs-publish` frå kjeldefilene under): `mkdocs/site/**`,
`mkdocs/mkdocs.yml`, `mkdocs/docs/index.md` (generert frå `README.md`),
`mkdocs/docs/arkitektur/valideringsregler.md` (generert frå
`src/mcp-linkml-validator/policies/README.md`).

### Filer og tal på førekomstar

| Fil | Tal |
|---|---|
| `README.md` | 4 |
| `CLAUDE.md` | 1 |
| `GOVERNANCE.md` | 7 |
| `CONTRIBUTING.md` | 2 |
| `SECURITY.md` | 1 |
| `SCOPE.md` | 3 |
| `.github/CODEOWNERS` | 1 |
| `mkdocs/publish.sh` | 2 |
| `mkdocs/docs/arkitektur/arkitektur-oversikt.md` | 1 |
| `mkdocs/docs/arkitektur/importhierarki.md` | 4 |
| `mkdocs/docs/kom-i-gang/kommandoar.md` | 1 |
| `mkdocs/docs/kom-i-gang/ny-org.md` | 3 |
| `mkdocs/docs/kom-i-gang/ny-domenemodell.md` | 1 |
| `specs/backlog/dx-prof-linkml-modell.md` | 1 |
| `specs/backlog/ekstern-kodeverk-versjonering.md` | 6 |
| `specs/backlog/nasjonal-datamesh-arkitektur.md` | 5 |
| `src/mcp-linkml-validator/policies/README.md` | 1 |

Ingen av førekomstane inngår i lenkje-ankrar (`#...domenemodeller...`) som
andre filer refererer til — verifisert ved søk etter kryssreferansar til
overskrifter som inneheld ordet.

## Steg

1. Erstatt `domenemodeller` → `domenemodellar` og `Domenemodeller` →
   `Domenemodellar` i dei 17 kjeldefilene over, med presis ordgrense (ikkje
   ramm `domenemodellane`, `domenemodellering`, `domenemodellklassar`).
2. Verifiser at ingen attverande bokmålsform finst utanfor `specs/done/`:
   `grep -rn "domenemodeller\b" --include='*' . | grep -v specs/done | grep -v mkdocs/site`
3. Køyr `bash tests/test_make.sh` for å stadfeste at ingen skript/testar er
   avhengige av den eksakte strengen "domenemodeller".
4. Generer commit-melding (kompakt format, jf. CLAUDE.md).

## Risikopunkt

| Risiko | Tiltak |
|---|---|
| Overskriftsendring bryt ankerlenkjer | Verifisert ingen kryssreferansar finst før endring |
| Skript/tekst-matching på eksakt streng "domenemodeller" | Steg 3 køyrer full testsuite |
| Generert innhald hamnar ute av synk til neste `make docs-publish` | Akseptabelt — same mønster som anna dokumentasjonsendring; genererte filer er ikkje versjonskontrollerte |

## Utført

Alle fire steg gjennomførte:

1. Erstatta `domenemodeller`/`Domenemodeller` → `domenemodellar`/`Domenemodellar` i
   alle 17 kjeldefilene, med ordgrense-sikker `sed`-regex
   (`\bdomenemodeller\b`/`\bDomenemodeller\b`). Stikkprøver stadfesta at
   `domenemodellklassar`, `domenemodellering` og `domenemodellane` er upåverka.
2. Verifisert: ingen attverande `\bdomenemodeller\b` utanfor `specs/done/` og
   genererte filer — berre denne specen sjølv (som dokumenterer endringa historisk).
3. `bash tests/test_make.sh` køyrd: **536 OK, 42 feil**. Dei 42 feila er
   roundtrip-ttl-feil (`MappingError: No pred for ...`) i `fint-utdanning`,
   `enhetsregisteret-bvrinn`, `samt-bu` m.fl. — kjende, pre-eksisterande
   RDF/LangString-roundtrip-avvik (jf. BUG-1-mønsteret i `bugs/`), heilt
   urelatert til tekstendringane i denne specen. Ingen skript/testar var
   avhengige av den eksakte strengen "domenemodeller".
4. Commit-melding generert (sjå under).

### Commit-melding

```
docs: rett "domenemodeller" til nynorsk "domenemodellar"
  - README.md, CLAUDE.md, GOVERNANCE.md, CONTRIBUTING.md, SECURITY.md, SCOPE.md: 4/1/7/2/1/3 førekomstar
  - .github/CODEOWNERS, mkdocs/publish.sh: 1/2 førekomstar
  - mkdocs/docs/arkitektur/{arkitektur-oversikt,importhierarki}.md: 1/4 førekomstar
  - mkdocs/docs/kom-i-gang/{kommandoar,ny-org,ny-domenemodell}.md: 1/3/1 førekomstar
  - specs/backlog/{dx-prof-linkml-modell,ekstern-kodeverk-versjonering,nasjonal-datamesh-arkitektur}.md: 1/6/5 førekomstar
  - src/mcp-linkml-validator/policies/README.md: 1 førekomst
```
