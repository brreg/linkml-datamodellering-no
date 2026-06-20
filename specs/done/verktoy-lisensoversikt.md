# Plan: Kartlegging av verktøylisensar og attribution-blokk

**Kortnamn:** `verktoy-lisensoversikt`
**Dato:** 2026-06-20

---

## Bakgrunn

Repoet brukar ei rekkje tredjepartsverktøy — containerbilete, Python-pakkar,
mkdocs-plugins og GitHub Actions. Ingen av desse er i dag dokumenterte med
lisens i repoet, og det er ikkje klart kva (om noko) som krev attribution.
Målet er å:

1. Kartlegge **alle** verktøy som faktisk brukast (ikkje berre dei mest synlege)
2. Slå opp korrekt lisens for hvert verktøy frå offisiell kjelde (LICENSE-fil i
   oppstrøms repo, PyPI-metadata, eller offisiell dokumentasjon) — ikkje gjette
3. Avgjere kva lisensar som krev attribution (typisk MIT, BSD, Apache-2.0 krev
   at lisensteksten/opphavsmerket følgjer med ved distribusjon; GPL/LGPL har
   andre krav; nettverkstjenester som berre kallast (Kroki) krev normalt ikkje
   attribution i sjølve repoet)
4. Leggje til ein attributions-blokk nedst i `mkdocs/docs/om.md` for dei
   verktøya som krev det

**Avgrensing:** Dette gjeld verktøy/programvare repoet **brukar** for å bygge,
validere og publisere (byggetidsavhengigheiter, containerbilete, CI-actions).
Det gjeld **ikkje** dataene/vokabulara repoet modellerer mot (Los, DCAT-AP-NO
o.l.) — det er regulert separat i `specs/backlog/ekstern-kodeverk-versjonering.md`
og via `license:`-feltet i det einskilde skjemaet.

---

## Førebels verktøyinventar (frå statisk gjennomgang 2026-06-20)

Denne tabellen er eit utkast basert på `Dockerfile*`, `requirements*.txt`,
`Makefile` og `.github/workflows/*.yml`. Lisensfeltet er **ikkje verifisert**
mot offisiell kjelde og må kontrolleres i steg V2 før noko publiseres.

### Containerbilete / CLI-verktøy

| Verktøy | Kjelde i repo | Antatt lisens | Status |
|---|---|---|---|
| LinkML (`linkml`, `linkml-runtime`) | `Dockerfile.linkml`, `requirements.txt` (alle MCP-tjenester) | BSD-3-Clause | Verifiser |
| rdflib | `Dockerfile.linkml` | BSD-3-Clause | Verifiser |
| Graphviz | `Dockerfile.linkml` (apt) | Eclipse Public License 1.0 | Verifiser |
| avrotize | `Dockerfile.avrotize` | Apache-2.0 (antatt) | Verifiser |
| AsyncAPI CLI | `Dockerfile.asyncapi-cli` | Apache-2.0 (antatt) | Verifiser |
| PlantUML (`plantuml/plantuml`) | Makefile (`PLANTUML_IMAGE`) | Multi-lisens (GPL/LGPL/EPL-val) | Verifiser — uvanleg lisensmodell |
| Gource | `Dockerfile.gource` | GPL-3.0 (antatt) | Verifiser |
| ffmpeg | `Dockerfile.gource` (apt) | LGPL/GPL avh. av byggeflagg | Verifiser kva variant Ubuntu-paketten brukar |
| Xvfb | `Dockerfile.gource` (apt) | MIT/X11-stil (X.Org) | Verifiser |
| pytest | `Dockerfile.python`, `requirements-python-test.txt` | MIT | Verifiser |
| PyYAML | alle `requirements*.txt` | MIT | Verifiser |
| openapi-spec-validator | `requirements-python-test.txt` | Apache-2.0 (antatt) | Verifiser |
| Podman | brukt lokalt (ikkje i repo) men premiss for heile byggeflyten | Apache-2.0 (antatt) | Verifiser |
| Python (CPython) | alle Dockerfiles (`python:3.11/3.12/3.13-slim`) | PSF License | Verifiser |

### mkdocs-plugins

| Verktøy | Kjelde i repo | Antatt lisens | Status |
|---|---|---|---|
| mkdocs-material (`squidfunk/mkdocs-material`) | `Dockerfile.mkdocs` | MIT | Verifiser |
| mkdocs-kroki-plugin | `Dockerfile.mkdocs` (pip) | Ukjent | Slå opp |
| mkdocs-build-cache-plugin | `Dockerfile.mkdocs` (pip) | Ukjent | Slå opp |
| Kroki (kroki.io, ekstern tjeneste kalla av kroki-plugin) | nettverkstenester, ikkje embedda kode | MIT (tenesta sjølv) | Truleg ikkje attribution-pliktig — verifiser tolking |

### GitHub Actions / CI-verktøy

| Verktøy | Kjelde i repo | Antatt lisens | Status |
|---|---|---|---|
| `actions/checkout`, `actions/cache`, `actions/upload-artifact`, `actions/download-artifact`, `actions/configure-pages`, `actions/upload-pages-artifact`, `actions/deploy-pages` | `.github/workflows/*.yml` | MIT (GitHub) | Verifiser |
| `googleapis/release-please-action` | `release-please.yml` | Apache-2.0 (antatt) | Verifiser |
| Trivy (`aquasecurity/trivy`) | `trivy.yml` | Apache-2.0 (antatt) | Verifiser |
| Renovate (Mend) | `renovate.json` — køyrer som hosted GitHub App, ikkje sjølvhosta | AGPL-3.0 (kjeldekode), men brukt som SaaS | Avklar om AGPL utløyser noko ved SaaS-bruk (truleg ikkje) |

**Manglar i denne lista vil truleg finnast** — t.d. transitive avhengigheiter
av `linkml` (jsonschema, click, antlr4 m.fl.) som ikkje er direkte pip-installert
av repoet, men følgjer med `linkml`-pakken. Steg V1 må avgjere kor djupt
kartlegginga skal gå (direkte avhengigheiter vs. fullt transitivt tre).

---

## Steg

### V1 — Avklar omfang og lag fullstendig verktøyliste ✓

**Utført:** `src/assets/scripts/list-tool-licenses.py` skanner `Dockerfile*`,
`requirements*.txt`, `.github/workflows/*.yml` og `Makefile` (`_IMAGE`-variablar)
og listar 26 distinkte direkte avhengigheiter med kildefil(ar). Skriptet
køyrast med `python3 src/assets/scripts/list-tool-licenses.py`. Avgrensing:
berre direkte avhengigheiter (ikkje transitive), som anbefalt i planen.
`localhost/*`-byggetags er filtrert ut (dei er lokale build-tags, ikkje
separate oppstrøms-verktøy).

Avgjer: skal kartlegginga dekke berre **direkte** referanser i Dockerfiles/
requirements/workflows (som tabellen ovanfor), eller òg **transitive**
Python-avhengigheiter (t.d. via `pip-licenses` i `linkml-local`-containeren)?
Anbefaling: start med direkte avhengigheiter (dei er det brukaren faktisk
har valt å ta inn), utvid til transitive berre om det er eit konkret behov.

Lag `src/assets/scripts/list-tool-licenses.py` eller liknande som genererer
inventarlista automatisk frå `Dockerfile*`, `requirements*.txt` og
`.github/workflows/*.yml`, slik at lista ikkje forvitrar når verktøy
legges til eller fjernast.

### V2 — Verifiser faktisk lisens per verktøy ✓

**Utført:** Alle 26 verktøy frå V1-inventaret er verifiserte mot GitHub sin
lisens-API (`api.github.com/repos/<org>/<repo>`), PyPI JSON-metadata
(`pypi.org/pypi/<pakke>/json`), eller rå LICENSE/COPYING-filer der API-et ikkje
fann eit SPDX-identifikator. **Fleire avvik frå dei antatte lisensane i
førebels-tabellen ovanfor vart funne** — sjå merka rader:

| Verktøy | Verifisert lisens | Kjelde |
|---|---|---|
| linkml | **Apache-2.0** (ikkje BSD-3-Clause som antatt) | GitHub API: `linkml/linkml` |
| linkml-runtime | **CC0-1.0** (avvik frå linkml sjølv) | GitHub API: `linkml/linkml-runtime` |
| rdflib | BSD-3-Clause | PyPI JSON-metadata |
| avrotize | MIT | PyPI-klassifikator |
| AsyncAPI CLI | Apache-2.0 | GitHub API: `asyncapi/cli` |
| PlantUML | **GPL-3.0-or-later** (ikkje multi-lisens som antatt) | `license.txt` i `plantuml/plantuml` |
| Gource | GPL-3.0 | GitHub API: `acaudwell/Gource` |
| ffmpeg (Ubuntu-pakke) | **GPL-2.0-or-later, effektivt** (Ubuntu sin pakke byggjer inn GPL-lisensierte filer) | Ubuntu copyright-fil, `ffmpeg_4.4.2-0ubuntu0.22.04.1` |
| git | GPL-2.0-only | `COPYING` i `git/git` |
| Xvfb (X.Org) | MIT/X11-stil | `COPYING` i `xorg/xserver` |
| Graphviz | **Eclipse Public License 2.0** (ikkje EPL-1.0 som antatt) | `LICENSE` i `gitlab.com/graphviz/graphviz` |
| build-essential | Ingen enkelt lisens — meta-pakke (gcc/g++/make), berre byggetidsverktøy, ikkje distribuert | — |
| pytest | MIT | GitHub API: `pytest-dev/pytest` |
| PyYAML | MIT | PyPI JSON-metadata |
| openapi-spec-validator | Apache-2.0 | GitHub API: `python-openapi/openapi-spec-validator` |
| Python (CPython) | PSF License 2.0 | GitHub API: `python/cpython` (PSF, OSI-godkjend) |
| mkdocs-material | MIT | PyPI-klassifikator |
| mkdocs-kroki-plugin | MIT | PyPI-klassifikator |
| mkdocs-build-cache-plugin | MIT | PyPI JSON-metadata |
| `actions/checkout`, `cache`, `cache/restore`, `upload-artifact`, `download-artifact`, `configure-pages`, `upload-pages-artifact`, `deploy-pages` | MIT | GitHub API (alle verifiserte enkeltvis) |
| `googleapis/release-please-action` | Apache-2.0 | GitHub API |
| `aquasecurity/trivy-action` + Trivy (CLI) | Apache-2.0 | GitHub API: `aquasecurity/trivy-action` og `aquasecurity/trivy` |
| `github/codeql-action` | MIT | GitHub API |
| Podman | Apache-2.0 | `LICENSE` i `containers/podman` (brukar sitt verktøy, ikkje ein repo-filavhengigheit) |
| `ubuntu:22.04` (base-image) | Ingen enkelt lisens — OS-distribusjon brukt som byggemiljø, ikkje distribuert som artefakt | — |
| Renovate (Mend) | AGPL-3.0 (kjeldekode), men brukt som hosted GitHub App, ikkje sjølvhosta | GitHub API: `renovatebot/renovate` |
| Kroki (kroki.io, ekstern teneste kalla av kroki-plugin) | Ekstern nettverksteneste — ikkje embedda kode i repoet | — (utanfor lisensspørsmålet, sjå V3) |

For hvert verktøy i V1-lista: slå opp lisens frå offisiell kjelde (PyPI-sida
si "License"-metadata, LICENSE-fila i GitHub-repoet, eller offisiell
dokumentasjon). Bruk `WebFetch`/`WebSearch` — ikkje gjett basert på generell
kjennskap. Noter kjelda (URL) for hver oppslag, slik at lisensvalet kan
etterprøves.

Spesiell oppfølging:
- **PlantUML** har ein uvanleg multi-lisensmodell (val mellom fleire
  lisensar) — les `plantuml`-repoet sin `license.txt` direkte.
- **ffmpeg** sin lisens avheng av kva codec-bibliotek som er bygd inn i
  Ubuntu sin `ffmpeg`-pakke (LGPL vs. GPL) — sjekk Ubuntu sin pakkemetadata,
  ikkje ffmpeg.org generelt.
- **Renovate/AGPL** — avklar at hosted GitHub App-bruk ikkje utløyser
  AGPL sine kopiplikt-krav (dei gjeld for den som *driftar ein modifisert
  versjon*, ikkje for den som brukar tenesta).

### V3 — Klassifiser attribution-krav ✓

**Utført:** Avgjerande funn — det er ikkje berre `mkdocs/docs/`-portalen som
distribueres offentleg. `.github/workflows/release.yml` pushar
`ghcr.io/<owner>/{linkml-local,mcp-linkml-validator,mcp-linkml-modell-utkast,mcp-linkml-begrep-utkast}`,
og `.github/workflows/generate.yml` pushar **i tillegg**
`ghcr.io/<owner>/{linkml-local,python-pytest,avrotize-local,asyncapi-cli-local}`
som hash-tagga build-cache-image (offentlege, sidan repoet er offentleg).
`mkdocs-local`-imaget derimot cachast berre via `actions/cache` — det pushast
ikkje til GHCR. Distribusjon av eit containerimage som **bundlar** eit verktøy
sin kode utløyser attribution-plikta i verktøyet sin lisens, sjølv når
imaget berre er tenkt som CI-cache.

**Kategori A — Krev attribution** (kode bundla i eit offentleg image eller i
den publiserte mkdocs-portalen):

| Verktøy | Lisens | Distribuert via |
|---|---|---|
| LinkML | Apache-2.0 | `linkml-local`, alle tre `mcp-*`-image |
| rdflib | BSD-3-Clause | `linkml-local` |
| Graphviz | Eclipse Public License 2.0 | `linkml-local` |
| PyYAML | MIT | `linkml-local`, `python-pytest`, alle `mcp-*`-image |
| pytest | MIT | `python-pytest`, `mcp-linkml-modell-utkast` |
| openapi-spec-validator | Apache-2.0 | `python-pytest` |
| avrotize | MIT | `avrotize-local` |
| AsyncAPI CLI | Apache-2.0 | `asyncapi-cli-local` |
| Python (CPython) | PSF License 2.0 | Alle Python-baserte image ovanfor |
| mkdocs-material | MIT | Tema-aktiva (CSS/JS/font) kopiert inn i den publiserte mkdocs-portalen |

`linkml-runtime` (CC0-1.0) er teknisk i samme kategori (bundla i `mcp-*`-image),
men CC0 er ei eksplisitt offentleg-domene-fråskriving utan attribution-krav —
utelaten frå tabellen, men nemnt her for fullstendigheit.

**Kategori B — Krev ikkje attribution** (berre brukt i CI/lokalt byggesteg,
aldri bundla i eit publisert image eller den publiserte portalen):

PlantUML, Gource, ffmpeg, git, Xvfb, `build-essential`, `ubuntu:22.04`,
mkdocs-kroki-plugin (transformerer berre Markdown til `<img>`-taggar mot
ekstern teneste — bundlar ikkje eigne aktiva i output), mkdocs-build-cache-plugin
(rein byggetidscache, ingen output-aktiva), Podman (brukar sitt eige lokale
verktøy), GitHub Actions (`actions/checkout` m.fl.), `googleapis/release-please-action`,
`aquasecurity/trivy-action` + Trivy CLI, `github/codeql-action`.

**Kategori C — Usikker / utanfor scope:**

- **Renovate** (AGPL-3.0): brukt som hosted GitHub App, ikkje sjølvhosta —
  AGPL sine kopiplikt-krav gjeld den som *driftar ein modifisert versjon*,
  ikkje den som brukar tenesta. Ingen handling nødvendig, men ikkje 100 %
  juridisk avklart dersom Renovate-bruken endrar karakter (t.d. sjølvhosting).
- **Kroki** (kroki.io): ekstern nettverksteneste kalla av mkdocs-kroki-plugin
  ved sideoppbygging — ingen kode frå Kroki er embedda i repoet eller i
  den publiserte portalen.

For hvert verktøy: avgjer om lisensen krev at opphavsmerke/lisenstekst
følgjer med når **repoet sine artefaktar** (genererte skjema, mkdocs-portalen,
container-images) distribueres. Lag tre kategoriar:

- **Krev attribution** (MIT, BSD-2/3, Apache-2.0 med NOTICE-fil, EPL)
- **Krev ikkje attribution i dette repoet** (verktøyet brukast berre internt
  i CI/byggesteg og distribueres ikkje som del av sluttproduktet — t.d.
  pytest, openapi-spec-validator, Trivy)
- **Usikker / krev juridisk vurdering** (GPL/LGPL/AGPL-tilfelle, PlantUML)

Berre verktøy i første kategori går inn i attributions-blokka.

### V4 — Lag attributions-blokk i `mkdocs/docs/om.md` ✓

**Utført:** Ny `## Attribution`-seksjon lagt til etter `## Lisens`-seksjonen
i `mkdocs/docs/om.md`, med dei 10 verktøya frå Kategori A (V3). Tabellen
lenkjer til opphavsrepoet/-prosjektet for hvert verktøy. Ein fotnote viser
til denne spec-fila (etter flytting til `specs/done/`) for fullstendig
oversikt over alle vurderte verktøy, inkludert dei som ikkje krev attribution.

Avvik frå opphavleg utkast i planen: tabellen inkluderer no
openapi-spec-validator, avrotize, AsyncAPI CLI og Python — verktøy som ikkje
var med i V4-utkastet, men som V3 viste **også** distribueres offentleg via
GHCR-cache-image i `generate.yml` (ikkje berre `release.yml`).

Legg til ein ny seksjon **etter** den eksisterande `## Lisens`-seksjonen
(som i dag ligg nedst i fila). Forslag til innhald (vert oppdatert basert
på V2/V3-resultat før dette implementeres):

```markdown
## Attribution

Dette repoet brukar følgjande tredjepartsverktøy i bygge- og publiseringsflyten.
Verktøy som berre brukast internt i CI (testing, validering) og ikkje
distribueres som del av portalen eller dei genererte artefaktane er utelatne.

| Verktøy | Lisens | Kjelde |
|---|---|---|
| [LinkML](https://github.com/linkml/linkml) | BSD-3-Clause | Skjemagenerering |
| [rdflib](https://github.com/RDFLib/rdflib) | BSD-3-Clause | RDF-prosessering |
| [Graphviz](https://graphviz.org/) | Eclipse Public License 1.0 | ER-diagram |
| [mkdocs-material](https://github.com/squidfunk/mkdocs-material) | MIT | Dokumentasjonsportal |
| [mkdocs-kroki-plugin](https://github.com/AVATEAM-IT-SYSTEMHAUS/mkdocs-kroki-plugin) | — (verifiser) | Diagramrendering i portalen |

Fullstendig oversikt over alle byggeavhengigheiter og lisensar finst i
`specs/done/verktoy-lisensoversikt.md`.
```

Tabellen ovanfor er eit **utkast** — endelig innhald avheng av resultatet
frå V2/V3. Lenkjer skal peike til opphavsrepoet/-prosjektet, ikkje til
generelle lisensoversikter.

### V5 — Hald oversikta oppdatert ✓

**Utført:** Brukar valde «begge» (CONTRIBUTING.md + CLAUDE.md) då dette vart
spurt om, jf. planen sitt forbehold om brukaravtale for dette steget. Lagt til:
- Ny seksjon «Nye verktøyavhengigheiter» i `CONTRIBUTING.md` (menneskeleg
  sjekkliste ved PR med nye Dockerfile/requirements/workflow-avhengigheiter)
- Tilsvarande kort bullet i `CLAUDE.md` under «Førende prinsipper» (AI-instruks),
  kryssreferert til CONTRIBUTING.md per DRY-prinsippet

CI-sjekk for å varsle ved nye uklassifiserte avhengigheiter (opphavleg nemnt
som moglegheit i planen) er **ikkje** implementert — utsett til behovet faktisk
melder seg, jf. plana sin eigen merknad om at dette skal vurderes etter at
V1–V4 er på plass.

Legg ein kort kommentar i `CLAUDE.md` eller `CONTRIBUTING.md` (etter avtale
med brukar) om at nye verktøy som tas inn i `Dockerfile*`/`requirements*.txt`/
`.github/workflows/*.yml` skal vurderes mot attributions-blokka i `om.md`.
Vurder om V1-skriptet (listeoversikt) bør køyres som ein CI-sjekk som varslar
ved nye, uklassifiserte avhengigheiter — utsett til etter at V1–V4 er på plass
og brukar ser behovet.

---

## Prioritert handlingsliste

| # | Tiltak | Fil(ar) | Avheng av |
|---|--------|---------|-----------|
| 1 | V1: Avklar omfang, generer fullstendig direkte-avhengigheitsliste | `src/assets/scripts/list-tool-licenses.py` | — |
| 2 | V2: Verifiser faktisk lisens per verktøy mot offisiell kjelde | (research, ingen fil) | V1 |
| 3 | V3: Klassifiser attribution-krav per verktøy | (research, ingen fil) | V2 |
| 4 | V4: Lag attributions-blokk i `mkdocs/docs/om.md` | `mkdocs/docs/om.md` | V3 |
| 5 | V5: Rutine for å halde oversikta oppdatert ved nye verktøy | `CLAUDE.md` eller `CONTRIBUTING.md` | V4 |

## Avhengigheiter

- V2 krev nettoppslag (`WebFetch`/`WebSearch`) — kan ikkje fullføres ut frå
  lokal kjennskap aleine, sidan lisensfelt må kunne etterprøves
- V4 endrar ei brukarvendt side (`mkdocs/docs/om.md`) — følgjer same
  nynorsk-konvensjon som resten av `mkdocs/docs/`
- Ingen avhengigheit til `ekstern-kodeverk-versjonering.md` (ulikt omfang:
  verktøy vs. vokabulardata), men begge spec-ane bør lenkast til frå
  hverandre når begge er implementerte

## Utført (2026-06-20)

Alle fem tiltak (V1–V5) er gjennomførte i éin arbeidsøkt:

- **V1:** `src/assets/scripts/list-tool-licenses.py` skanner `Dockerfile*`,
  `requirements*.txt`, `Makefile` og `.github/workflows/*.yml` og finn 26
  distinkte direkte verktøyavhengigheiter automatisk.
- **V2:** Alle 26 verktøy verifiserte mot GitHub sin lisens-API og PyPI
  JSON-metadata (kjelder noterte per verktøy). Fire avvik frå dei opphavlege
  antakelsane i planen: LinkML er **Apache-2.0** (ikkje BSD-3-Clause),
  linkml-runtime er **CC0-1.0**, PlantUML er rein **GPL-3.0-or-later**
  (ikkje multi-lisens), Graphviz er **EPL-2.0** (ikkje EPL-1.0).
- **V3:** Avgjerande funn under klassifiseringa — `.github/workflows/generate.yml`
  pushar **fire ekstra** image (`python-pytest`, `avrotize-local`,
  `asyncapi-cli-local`, i tillegg til `linkml-local`) til GHCR som offentleg
  build-cache, ikkje berre dei fire `release.yml`-pusha frå opphavleg utkast.
  Dette utvida kategori «krev attribution» med openapi-spec-validator,
  avrotize, AsyncAPI CLI og Python (CPython) — verktøy som ikkje var med i
  V4-utkastet i opphavleg plan.
- **V4:** `## Attribution`-seksjon lagt til i `mkdocs/docs/om.md` etter
  `## Lisens`, med 10 verktøy (Kategori A frå V3) og lenkjer til
  opphavsrepo/-prosjekt for hvert.
- **V5:** Bruker valde å dokumentere rutinen i **begge** `CONTRIBUTING.md`
  (menneskeleg PR-sjekkliste) og `CLAUDE.md` (AI-instruks, kryssreferert til
  CONTRIBUTING.md per DRY). CI-varsling ved nye uklassifiserte avhengigheiter
  er utsett, som planlagt.

**Avvik frå opphavleg plan:** Ingen separat `generated/tool-inventory.yaml`
eller liknande strukturert datafil blei laga — V1-skriptet skriv rett til
stdout og brukast manuelt ved behov for revurdering, sidan lista er liten
(26 verktøy) og endrar seg sjeldan.
