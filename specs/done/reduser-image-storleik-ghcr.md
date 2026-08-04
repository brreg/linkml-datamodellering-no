# Reduser container-image-storleik for å redusere total opp-/nedlasting frå GHCR

## Bakgrunn

**Mål:** Redusere total mengd bytes som vert lasta opp og ned frå GHCR av dei container-imaga
repoet byggjer og brukar, ved å (a) gjere sjølve imaga mindre og (b) unngå at image vert pulla
når dei ikkje trengst.

**Kontekst — kor mykje pullast i dag:**

`generate.yml` køyrer éin `generate`-jobb per domene (9 domene: `ap-no`, `begrepskatalog`,
`fair`, `fint`, `modellkatalog`, `ngr`, `oreg`, `referanse`, `samt`), kvar på ein fersk,
tom GitHub Actions-runner. Kvar jobb pullar minst dei fire imaga som er merkte
`always_required: true` i `src/assets/containers/images.json`, pluss eventuelle
betinga image (`avrotize-local`, `asyncapi-cli-minimal`) viss domenet har eit
`build.yaml` med tilhøyrande generator-flagg sett til `true`. `validate.yml` køyrer
tilsvarande, men berre med `linkml-local` + `mcp-linkml-validator`, og køyrer både
nattleg (cron) og på kvar PR som rører `src/linkml/**` eller `src/mcp-linkml-validator/**`.

Målte biletstorleikar (bygde lokalt med gjeldande Dockerfile via `make build-docker-*`,
verifisert 2026-08-04):

| Image | Storleik | `always_required`? | Brukt av kor mange domene |
|---|---|---|---|
| `linkml-local` | 354 MB | ja | 9/9 |
| `python-pytest` | 79 MB | ja | 9/9 |
| `plantuml` | 328 MB | ja (feil — sjå tiltak A1) | reelt behov: 7/9 |
| `mcp-linkml-validator` | 292 MB | ja | 9/9 |
| `avrotize-local` | 567 MB | nei (`xsd`-flagg) | 1/9 (`samt`) |
| `asyncapi-cli-minimal` | 299 MB | nei (`asyncapi`-flagg) | 1/9 |
| `mkdocs-local` | 190 MB | nei (berre publish-jobb) | 1× per køyring |
| `mcp-linkml-modell-utkast` | 292 MB | — | 0 (ikkje i images.json, berre release.yml) |
| `mcp-linkml-begrep-utkast` | 292 MB | — | 0 (ikkje i images.json, berre release.yml) |

Dei fire `always_required`-imaga åleine gjev **~9,5 GB** pulla data per `generate.yml`-køyring
(1053 MB × 9 domene), før betinga image er lagt til. `validate.yml` gjev **~5,8 GB** per køyring,
og køyrer langt oftare (nattleg + kvar PR). Upplastingssida er alt godt optimalisert
(sjå C1) — hovudpotensialet ligg i imagestorleik og unødvendige pull.

## Relevante filer

- `src/assets/containers/Dockerfile.*` — alle container-definisjonar
- `src/assets/containers/images.json` — autoritativ liste over image, kva make-target som byggjer
  dei, og om dei er `always_required` eller `required_if_generator_flag`
- `.github/workflows/generate.yml` — pullar image per domene (`ensure-images`- og `generate`-jobbane)
- `.github/workflows/validate.yml` — pullar `linkml-local` + `mcp-linkml-validator` per domene
- `.github/workflows/release.yml` — byggjer/pushar `linkml-local`, `mcp-linkml-validator`,
  `mcp-linkml-modell-utkast`, `mcp-linkml-begrep-utkast` ved tag-push
- `.github/actions/ensure-image/action.yml` — hash-tag-basert skip-viss-finst-logikk (alt god praksis)
- `src/assets/scripts/container/asyncapi-validate.js` — einaste bruken av `asyncapi-cli-minimal`

## Funn og foreslåtte tiltak

### Tier A — låg risiko, konkret målt gevinst

**A1. `plantuml` er feilmerkt `always_required: true` i `images.json`**

0 av `begrepskatalog` sine 2 manifest og 0 av `modellkatalog` sine 12 manifest har
`plantuml: true`, men begge domene-jobbane pullar likevel det 328 MB store `plantuml`-imaget
på kvar `generate.yml`-køyring, fordi `detect-images`-steget i `generate.yml` legg til alle
`always_required`-image uavhengig av domene. Dei andre 7 domena brukar det faktisk.

**Tiltak:** Endre `images.json` sitt `plantuml`-oppslag frå `always_required: true` til
`required_if_generator_flag: "plantuml"`, same mønster som `avrotize-local`/`asyncapi-cli-minimal`
alt brukar. Reint konfigurasjonstiltak, ingen kodeendring.

**Gevinst:** ~656 MB mindre pulla data per `generate.yml`-køyring (2 domene × 328 MB). Risiko: ingen.

**A2. `@stoplight/spectral-cli` i `Dockerfile.asyncapi-cli-minimal` er installert, men aldri brukt**

`asyncapi-validate.js` importerer berre `@asyncapi/parser` og `js-yaml`. Verifisert med
`grep -rn spectral` mot heile `src/` og `make/` — ingen treff utanom Dockerfile-linja sjølv.
`@stoplight/spectral-cli` er den enkeltvis største pakken i imaget (66,6 MB av 299 MB totalt,
målt med `du -sh /usr/local/lib/node_modules/*`).

**Tiltak:** Fjern `@stoplight/spectral-cli@6.15.1`-linja frå `RUN npm install --global` i
`Dockerfile.asyncapi-cli-minimal`.

**Gevinst:** ~66 MB mindre (299 MB → ~233 MB), pulla av dei domena som har `asyncapi: true`
(1/9 i dag). Risiko: ingen, forutsett at ingen framtidig bruk av `spectral`-kommandoen finst.

**A3. `avrotize-local` (567 MB) drar inn tunge, ubrukte transitive avhengigheiter**

`avrotize`-containeren brukast berre til JSON Schema → Avro → XSD-konvertering (`gen-xsd`,
sjå `make/10-generator-macros.mk`) — ingen sky- eller databaseintegrasjon. Likevel installerer
`pip install avrotize` (verifisert mot PyPI sitt `requires_dist`) **ubetinga** (ikkje som
`extra`): `pyarrow` (182 MB), `pandas` (72 MB), `botocore`/`boto3` (29 MB), `azure-kusto-data`,
`azure-identity`, `pyiceberg`, `sqlalchemy`, `datapackage`, `docker`, `cddlparser`,
`json-structure` — alle knytt til format/lager avrotize støttar (Parquet, Iceberg, Kusto,
S3, SQL) som denne containeren aldri brukar.

**Tiltak (krev verifisering før iverksetjing):** Undersøk `pip install --no-deps avrotize` +
manuell installasjon av berre dei transitive pakkane den faktiske JSON→Avro→XSD-kodestien
treng (truleg eit lite subsett: `jsonschema`, `lark`, `asn1tools`, `jsonpointer`,
`jsonpath-ng`, `pyyaml`, `jinja2`, `attrs`, `bitstruct`). Må testast empirisk — avrotize
kan importere valfrie modular "eagerly" ved oppstart, noko som ville krevje anten stub-modular
eller ei anna løysing. Verifiser med full `make gen-xsd`/roundtrip på `samt-bu`-skjemaet.

**Gevinst (potensial):** 567 MB → sannsynlegvis under 150 MB. Berre 1/9 domene råka i dag.
Risiko: moderat — krev faktisk testing, ikkje berre Dockerfile-redigering.

**A4. `linkml-local` installerer `graphviz` (`dot`) — ser ut til å vere ubrukt**

Ingen make-target eller script i `make/` eller `src/assets/scripts/` kallar `dot` eller
refererer til `graphviz`. `gen-erdiagram` (einaste ER-diagram-relaterte generator i
`linkml-local`) produserer Mermaid-Markdown, ikkje graphviz-rendra output — faktisk
ER-diagram-rendering (SVG) skjer i det separate `plantuml`-imaget. `apt-get install
graphviz patch`-laget er 61,8 MB.

**Tiltak (krev verifisering før iverksetjing):** Bygg `linkml-local` utan `graphviz` i eit
mellombels forsøk, køyr full generator-pipeline (`make domain-<kvart domene>` eller minst
`make roundtrip` + `make gen-doc` + `make gen-erdiagram` på eit representativt utval skjema)
og stadfest at ingenting feilar før linja fjernast permanent. `patch` er triviell og kan
behaldast uansett (brukast til `docgen-max-chars.patch`).

**Gevinst (potensial):** opptil ~60 MB mindre per domene, alle 9 domene råka
(`linkml-local` er `always_required`) — opptil ~550 MB per `generate.yml`-køyring dersom
verifiseringa bekreftar at `graphviz` trygt kan fjernast. Risiko: låg-moderat.

### Tier B — strukturelle tiltak, høgare innsats/risiko

**B1. (Sideleg funn, ikkje del av kjerneomfanget) `release.yml` sine `mcp-linkml-modell-utkast`-
og `mcp-linkml-begrep-utkast`-jobbar er i praksis knekte**

`podman build -t ... src/mcp-linkml-modell-utkast` (og tilsvarande for `begrep-utkast`)
manglar `-f`-flagget til den faktiske Dockerfile-en (`src/assets/containers/Dockerfile.mcp-linkml-modell-utkast`).
Reprodusert lokalt: `Error: no Containerfile or Dockerfile specified or found in context
directory`. Desse to Dockerfile-ane byggjest **berre** her (ikkje i `generate.yml`/`validate.yml`,
sidan dei ikkje er i `images.json`), så feilen har truleg gått upåakta forbi sidan
`release.yml` berre køyrer ved tag-push. Dette er ein føresetnad for B2 — eit image som ikkje
kan byggjast kan heller ikkje konsoliderast. Foreslår ein liten, separat fiks
(éin linje per jobb: legg til `-f src/assets/containers/Dockerfile.mcp-linkml-<namn>`),
anten no eller som eiga oppfølging.

**B2. Dei tre `mcp-linkml-*`-imaga (validator/modell-utkast/begrep-utkast) er nesten identiske**

Alle tre er bygde frå same multi-stage `python:3.11-slim`-mønster, med tilnærma identiske
`requirements.txt` (`linkml`, `linkml-runtime`, `pyyaml`, og for éin av dei i tillegg `pytest`).
Verifisert empirisk ved å samanlikne lag-digestar (`podman inspect --format
'{{range .RootFS.Layers}}...'`): dei fire base-laga er **bit-identiske** på tvers av alle tre,
og pip-install-laget er **bit-identisk** mellom `mcp-linkml-validator` og
`mcp-linkml-begrep-utkast` (byte-identisk `requirements.txt`). Den einaste reelle skilnaden
mellom dei tre er nokre få titals KB Python-script (`server.py`, `validate-and-log.py` /
`converter.py` / `generator.py`).

Dette svarar direkte på det opphavlege spørsmålet om lag-deling i GHCR: identiske lag (same
digest) treng berre lastast opp éin gong per registry — podman/buildah nyttar automatisk
cross-repo blob-mount (OCI-distribusjonsspec) når laget alt finst andre stader i same
registry. Men det gjev **ikkje** automatisk mindre nedlasting for ein fersk CI-runner som
berre pullar eitt av dei tre imaga — den gevinsten krev anten at same jobb pullar fleire
image som deler lag (lokal gjenbruk), eller at imaga faktisk vert konsoliderte til færre
image totalt.

**Tiltak:** Etter at B1 er fiksa, vurder anten (a) eitt delt `mcp-linkml-server`-image der
kva server som køyrer vert valt via `CMD`/miljøvariabel, eller (b) behald tre image, men
sikra at det delte laget held fram med å vere byte-identisk (delt `requirements.txt`) slik
at push-sida framleis dreg nytte av blob-mount. (a) gjev størst gevinst, men er eit større
strukturelt grep som bør planleggjast som eiga oppfølging — kun `mcp-linkml-validator` er i
dag i `images.json`/faktisk pulla av CI, så den umiddelbare GHCR-nedlastingsgevinsten er
avgrensa til release- og lokalt dev-bruk inntil eventuelt fleire av dei blir pulla av CI.

### Tier C — vurdert, men utanfor omfanget av denne specen

- **C1.** Opplastingssida er alt godt optimalisert: `ensure-image`-action + hash-tag-basert
  `skopeo inspect`-sjekk (sjå `.github/actions/ensure-image/action.yml`) hoppar over bygg+push
  viss imaget alt finst i GHCR for den nøyaktige Dockerfile/requirements-hashen. Ingen tiltak.
- **C2.** `Dockerfile.gource` pullast/byggjest ikkje av nokon CI-workflow (ikkje i `images.json`,
  ingen treff i `.github/workflows/*.yml`) — påverkar ikkje GHCR-trafikk. Utanfor omfang.
- **C3.** `Dockerfile.asyncapi-cli` (ikkje `-minimal`) er alt merkt `DEPRECATED` i fila sjølv
  og brukast ingen stad i `make/`/CI. Kan vurderast sletta i eiga, uavhengig oppdurding —
  ikkje ein storleiksreduksjon i seg sjølv sidan imaget aldri vert bygt/pulla.
- **B3 (valfritt, større innsats).** `plantuml`-imaget er upstream `plantuml/plantuml:latest`
  = full Ubuntu 22.04 + full Temurin 17 JDK (136 MB) + graphviz + `plantuml.jar` (29 MB) =
  328 MB totalt (målt). Eit eigebygd image på t.d. `eclipse-temurin:17-jre-alpine` + graphviz
  + `plantuml.jar` kunne truleg kome ned mot 150–180 MB. Sidan `plantuml` (etter A1-fiksen)
  framleis pullast av 7/9 domene (~2,3 GB per `generate.yml`-køyring), er dette det
  enkeltimaget med størst attverande fotavtrykk og høgast potensial — men krev eiga
  verifiseringsrunde (JRE i staden for JDK, Alpine/musl i staden for Ubuntu/glibc, stadfeste
  at ER-diagram-generering framleis fungerer korrekt). Foreslått som eiga, seinare spec.
- **B4 (valfritt, avslått i denne omgang).** Migrering frå `python:3.11-slim` til
  `python:3.11-alpine` for `linkml-local`/`mcp-*`. Base åleine 129 MB → ~48 MB, men
  `linkml-runtime`/`rdflib`/`pydantic-core` har C-utvidingar som krev musl-kompatible wheel
  eller bygg-frå-kjelde (tregare bygg, høgare risiko for runtime-avvik). Eiga, seinare spec
  med eigen testrunde.

## Steg (foreslått rekkjefølgje ved iverksetjing)

1. **A1** — endre `images.json`: `plantuml.always_required` → `false`,
   legg til `required_if_generator_flag: "plantuml"`. Test: kjør `generate.yml` (eller
   simuler `detect-images`-steget lokalt) og stadfest at `begrepskatalog`/`modellkatalog`
   ikkje lenger pullar `plantuml`, medan dei 7 andre domena framleis gjer det.
2. **A2** — fjern `@stoplight/spectral-cli`-linja i `Dockerfile.asyncapi-cli-minimal`.
   Test: `make build-docker-asyncapi`, deretter køyr `gen-asyncapi`-pipelinen på eit
   AsyncAPI-skjema og stadfest at validering framleis fungerer.
3. **A4** — verifiser om `graphviz` kan fjernast frå `Dockerfile.linkml`. Bygg ei
   testutgåve utan, køyr full generator-suite, fjern permanent viss alt går gjennom.
4. **A3** — undersøk `pip install --no-deps avrotize` + minimal transitiv avhengigheitsliste.
   Verifiser med full `gen-xsd`-roundtrip på `samt-bu`. Berre iverksett viss verifiseringa
   lukkast utan å måtte vedlikehalde ei skjør, hardkoda avhengigheitsliste som lett kan
   knekkje ved neste `avrotize`-oppgradering.
5. **B1** — fiks manglande `-f`-flagg i `release.yml` for `mcp-linkml-modell-utkast`/
   `mcp-linkml-begrep-utkast` (føresetnad for B2, men uavhengig verdifullt åleine).
6. **B2** — (eiga oppfølging, større omfang) vurder konsolidering av dei tre `mcp-linkml-*`-imaga.

## Utført (Tier A — 2026-08-04)

Alle fire Tier A-tiltak er iverksette og verifiserte lokalt (bygde med `make build-docker-*`,
testa mot faktisk generator-pipeline via `make gen-asyncapi`/`make gen-xsd`/`make gen-docs`/
`make domain-samt`):

- **A1**: `images.json` — `plantuml.always_required` → `false`,
  `required_if_generator_flag: "plantuml"`. Verifisert ved å simulere `detect-images`-bash-
  logikken frå `generate.yml` lokalt: `begrepskatalog`/`modellkatalog` pullar no ikkje lenger
  `plantuml`, dei 7 andre domena gjer det framleis.
- **A2**: Fjerna `@stoplight/spectral-cli@6.15.1` frå `Dockerfile.asyncapi-cli-minimal`.
  **299 MB → 234 MB** (−65 MB). Verifisert med full `make gen-jsonschema` → `make gen-asyncapi`
  på `samt-bu` — validering køyrer og returnerer korrekt resultat via den nye containeren.
- **A4**: Fjerna `graphviz` frå `Dockerfile.linkml`. **354 MB → 294 MB** (−60 MB). Verifisert med
  full `make domain-samt` (alle generatorar, inkl. `gen-doc`/`gen-erdiagram`/`gen-plantuml`) og
  `make gen-docs` på `dcat-ap-no` (større, meir kompleks skjema) — begge fullførte utan feil.
  `roundtrip-ttl (samt-bu)` feilar framleis (`Unknown CURIE prefix: @base` i
  `samt-bu-eksempel.yaml`), men A/B-testa mot uendra image via `git stash` og stadfesta at
  feilen er **føreeksisterande og heilt urelatert** til graphviz-fjerninga (rein
  RDF/CURIE-namnerom-feil i rdflib-serialisering, ikkje diagram-rendering). Ikkje ein del av
  denne specen — kan meldast som eiga sak viss ønskt.
- **A3**: `Dockerfile.avrotize` bruker no `pip install --no-deps avrotize` + eksplisitt minimal
  avhengigheitsliste (`jsonpointer requests jsoncomparison jinja2`), i staden for å la
  ubetinga `pyproject.toml`-avhengigheiter (pyarrow, pandas, azure-*, pyiceberg, sqlalchemy,
  botocore m.fl.) følgje med. **567 MB → 61,9 MB** (−505 MB, langt over det opphavleg anslåtte
  potensialet på <150 MB). Verifisert ved kjeldekodeanalyse (avrotize sin `__init__.py`/CLI
  brukar lazy-import og dispatchar `j2a`/`a2x` direkte til `avrotize.jsonstoavro`/
  `avrotize.avrotoxsd`, som til saman berre importerer dei fire pakkane over + stdlib) **og**
  empirisk: full `make gen-xsd` på `samt-bu` gjev **byte-identisk** `.xsd`-output samanlikna med
  det uendra imaget (verifisert med `diff`).

**Total målt reduksjon (dei fire imaga åleine, absolutt storleik):** 1548 MB → 651,8 MB
(−897 MB, −58 %). I tillegg kjem A1 sin effekt på *kor mange gonger* `plantuml` vert pulla
(2 av 9 domene treng han ikkje lenger i det heile).

**Ikkje iverksett i denne omgangen** (står att i backlog, sjå Tier B over):

- [x] A1: `plantuml` → `required_if_generator_flag` i `images.json`
- [x] A2: fjern `@stoplight/spectral-cli` frå `Dockerfile.asyncapi-cli-minimal`
- [x] A4: verifiser og evt. fjern `graphviz` frå `Dockerfile.linkml`
- [x] A3: undersøk minimal-avhengigheit-installasjon for `avrotize-local`
- [x] B1: fiks `-f`-flagg i `release.yml` for dei to `mcp-linkml-*-utkast`-jobbane
- [x] B2: vurder/planlegg konsolidering av `mcp-linkml-*`-imaga (eiga oppfølging) — utført,
      sjå `specs/done/videre-containeroptimering-mcp-plantuml-alpine.md` (som òg tok B3
      og B4, dei to Tier C-punkta som opphavleg var utanfor omfanget her)

## Utført (B1 — 2026-08-04)

`release.yml` sine `mcp-linkml-modell-utkast`- og `mcp-linkml-begrep-utkast`-jobbar bygde i
praksis feil: `podman build -t ... src/mcp-linkml-modell-utkast` (utan `-f`) leita etter ein
bar `Dockerfile` i den katalogen, som ikkje finst — reelle Dockerfile ligg i
`src/assets/containers/`, og desse Dockerfile-ane har `COPY`-stiar (t.d.
`COPY src/mcp-linkml-modell-utkast/requirements.txt .`) som føreset byggjekontekst = repo-rota,
ikkje underkatalogen som vart brukt som kontekst.

**Fiks:** endra begge jobbane til å byggje med `-f src/assets/containers/Dockerfile.mcp-linkml-
<namn>` og kontekst `.` (repo-rota), pluss `--format docker` — same mønster som
`make/60-mcp.mk` sine `build-docker-mcp-modell-utkast`/`build-docker-mcp-begrep-utkast`-target
og som `mcp-linkml-validator`-jobben lenger oppe i same fil alt brukar.

**Verifisert:**
- Begge `podman build`-kommandoane (nøyaktig slik dei no står i `release.yml`) køyrde og
  fullførte utan feil lokalt, mot dei faktiske Dockerfile-ane og repo-rota som kontekst.
- `actionlint` mot `.github/workflows/release.yml` — ingen funn.

## Utkast til commit-melding

```
perf(containers): reduser image-storleik for avrotize/asyncapi/linkml, fiks plantuml-pull

  - Dockerfile.avrotize: --no-deps + minimal avhengigheitsliste (567MB→62MB)
  - Dockerfile.asyncapi-cli-minimal: fjern ubrukt @stoplight/spectral-cli (299MB→234MB)
  - Dockerfile.linkml: fjern ubrukt graphviz (354MB→294MB)
  - images.json: plantuml → required_if_generator_flag (unngår unødvendig pull for
    begrepskatalog/modellkatalog)
  - specs/backlog/reduser-image-storleik-ghcr.md: full gjennomgang, funn og verifisering
```
