# Vidare containeroptimering: konsolider MCP-image, slank plantuml, vurder Alpine

## Bakgrunn

Oppfølging av `specs/backlog/reduser-image-storleik-ghcr.md` (Tier A + B1 er alt utførte og
gjev −897 MB på dei fire hovudimaga, sjå den specen for detaljar). Denne specen **planlegg**
dei tre attverande punkta (B2, B3, B4) som vart lista som eiga oppfølging — ho **iverksett dei
ikkje**. Kvart punkt er verifisert med eit lite, isolert spike-bygg (ikkje permanente
endringar) for å grunngje planen i verifiserte fakta i staden for antaking, men den faktiske
Dockerfile-/Makefile-/CI-endringa står att.

**Prioritert rekkjefølgje (tilrådd):** B3 → B2 → B4, etter forholdet mellom stadfesta gevinst,
kor mange domene/jobbar som faktisk råkast, og kompleksitet/risiko ved iverksetjing (grunngjeving
under kvart punkt).

## B3 — eigenbygd, slankare `plantuml`-image

### Funn (frå tidlegare spec)

`plantuml/plantuml:latest` (upstream, ubytt i dag) = full Ubuntu 22.04 + full Temurin 17 **JDK**
(136 MB) + graphviz + `plantuml.jar` (29 MB) = 328 MB. Etter A1-fiksen (`plantuml` er no
`required_if_generator_flag`) pullast dette imaget framleis av 7 av 9 domene på kvar
`generate.yml`-køyring (~2,3 GB samla) — det er det enkeltimaget med størst attverande
fotavtrykk av alle imaga repoet brukar.

### Spike (gjennomført under planlegging, 2026-08-04)

Bygde og testa følgjande erstatning:

```dockerfile
FROM docker.io/plantuml/plantuml:latest AS upstream

FROM docker.io/library/eclipse-temurin:17-jre-alpine
RUN apk add --no-cache graphviz fontconfig ttf-dejavu
COPY --from=upstream /opt/plantuml.jar /opt/plantuml.jar
WORKDIR /data
ENTRYPOINT ["java", "-jar", "/opt/plantuml.jar"]
```

Nøkkelinnsikt: **kopier `.jar`-fila direkte frå det upstream-imaget** (multi-stage `COPY --from`)
i staden for å laste ho ned separat — garanterer eksakt same PlantUML-versjon/åtferd, ingen
versjonsdrift å halde styr på. Entrypoint/WorkingDir stadfesta ved `podman inspect` av
upstream-imaget (`[java -jar /opt/plantuml.jar] /data`).

**Resultat:**
- Storleik: **328 MB → 252 MB** (−76 MB, −23 %). Meir moderat enn det opphavlege anslaget
  (150–180 MB) — Temurin JRE Alpine + graphviz + fontconfig/pango/harfbuzz (krevst for
  tekstrendering i diagram) utgjer meir enn venta.
- Funksjonell korrektheit: rendra `-tsvg` av eit reelt, generert `.puml`-diagram
  (`samt-bu-filtered.puml`) gjennom begge imaga og samanlikna — **SVG-outputen er byte-
  identisk** (`diff` viser ingen skilnad, begge 21 998 byte). Testa berre éitt diagram; sjå
  steg 3 under for breiare verifisering før permanent iverksetjing.

### Design/steg

1. Erstatt `src/assets/containers/Dockerfile.plantuml` med spike-innhaldet over (juster evt.
   Temurin-versjon dersom upstream-imaget sin JDK-versjon endrar seg — hald han synkronisert
   med det som faktisk står i upstream-imaget for å unngå versjonsavvik mellom byggjeverktøy).
2. `make build-docker-plantuml` — stadfest bygg lukkast og mål ny storleik.
3. Breiare verifisering enn spiken: køyr `make gen-plantuml` (eller `make domain-<domain>`) på
   **fleire** skjema — særleg eitt med rike importerte klassar (t.d. `dcat-ap-no`, som har flest
   relasjonar) og eitt med spesialteikn i skildringar (norske bokstavar æøå) — for å fange opp
   eventuelle font-/teiknsett-avvik som spike-testen med berre `samt-bu` ikkje ville vist.
   Samanlikn SVG-output byte-for-byte mot noverande upstream-baserte biletet for kvart skjema.
4. Oppdater `mkdocs/publish.sh` sitt bruk av genererte SVG-ar berre dersom steg 3 avdekkjer
   avvik som krev handtering (t.d. manglande font) — venta å vere unødvendig.
5. Ingen endring i `images.json`/`generate.yml` naudsynt utover at hash-taggen for `plantuml`
   automatisk endrar seg (`hashFiles('src/assets/containers/Dockerfile.plantuml')`), som
   allereie triggar ny bygg+push via `ensure-image`-mekanismen.

### Risiko

Låg for storleik/funksjon. Sjå `## Utført (B3)` under — «byte-identisk» heldt **ikkje** fullt
ut ved breiare testing (steg 3); det viste seg å vere ein reell, om enn kosmetisk, skilnad på
tette diagram, med ei identifisert og forstått rotårsak (ulik graphviz-versjon).

## Utført (B3 — 2026-08-04)

Iverksett. `src/assets/containers/Dockerfile.plantuml` bruker no eit eigenbygd
`eclipse-temurin:17-jre-alpine`-basert image i staden for `docker.io/plantuml/plantuml:latest`.

**Storleik:** 328 MB → **262 MB** (−66 MB, −20 %). Noko høgare enn spikens 252 MB, sidan
steg 3 (sjå under) avdekte at font-filene måtte kopierast frå upstream i staden for å
installerast via Alpine sin eigen `ttf-dejavu`-apk-pakke.

**Breiare verifisering (steg 3) avdekte at «byte-identisk» frå spiken ikkje heldt generelt:**

- `samt-bu` (enkelt diagram, norske særteikn æøå i skildringar): **byte-identisk**, som i spiken.
- `dcat-ap-no` (det tettaste diagrammet i repoet — flest importerte klassar/relasjonar): **ikkje**
  byte-identisk mot upstream — ~13 % av `<text>`-elementa (multiplisitetsetikettar som `0..*` på
  relasjonslinjer) var forskutte opptil ~60px på eit 6552×1894px lerret. Klasseboksar, tekst-
  innhald og totale diagram-mål var **uendra**.

**Rotårsak identifisert (ikkje berre anteke):**
1. Kopierte identiske font-filer frå upstream inn i Alpine-imaget (verifisert md5sum-likskap) —
   løyste **ikkje** skilnaden. Utelukka font-hinting/-metrikk som årsak.
2. Samanlikna `dot -V` (graphviz) i begge imaga: upstream har **graphviz 14.0.1**, Alpine sin
   nyaste tilgjengelege apk-pakke (også i edge-repoet) er **graphviz 12.2.1**. PlantUML
   delegerer layout av klassediagram til `dot`, og dei to versjonane plasserer kant-etikettar
   ulikt i tette diagram med mange kryssande relasjonar. Stadfesta reproduserbart og
   deterministisk (identisk output ved gjentekne køyringar av same image).
3. Alpine har ikkje graphviz 14.0.1 tilgjengeleg via nokon offisiell pakkekjelde — å matche
   versjonen ville krevje å byggje graphviz frå kjeldekode, som aukar kompleksitet/byggjetid og
   delvis motverkar formålet med denne endringa.

**Avgjerd:** Lagt fram avvegingen for brukar (godta kosmetisk avvik på tette diagram vs. bygg
graphviz frå kjelde vs. avbryt). Brukar valde å **godta noverande tilstand** — inga innhaldsmessig
eller strukturell påverknad, berre kosmetisk etikettplassering på det mest komplekse diagrammet i
repoet.

**Endra frå opphavleg spike-design:** font-filene kopierast no frå upstream-imaget (`COPY
--from=upstream /usr/share/fonts/truetype/dejavu ...` + `fc-cache -f`) i staden for å
installerast via `apk add ttf-dejavu` — nødvendig steg i feilsøkinga, behalde sidan det uansett
gjev tettare parasitet med upstream utan meirkostnad.

## B2 — konsolider dei tre `mcp-linkml-*`-imaga til éin multi-stage Dockerfile

### Funn (frå tidlegare spec)

Dei tre imaga (`mcp-linkml-validator`, `mcp-linkml-modell-utkast`, `mcp-linkml-begrep-utkast`,
~292 MB kvar) deler identisk `python:3.11-slim`-basis og nesten identisk avhengigheitssett
(`linkml`, `linkml-runtime`, `pyyaml`, ± `pytest`). Verifisert tidlegare at laga faktisk vert
bit-identiske når `requirements.txt`-innhaldet er byte-likt.

### Ny observasjon frå denne runden: bind-mount overstyrer image-innhald ved lokal dev-bruk

`Makefile` sine `LINKML_MOD_RUN`/`LINKML_BEGREP_RUN`/`MCP_RUN`-variablar bind-mountar **kvart
einaste Python-script og `profiles/`-katalog** frå host inn i containeren ved `podman run`
(`-v ".../server.py:/app/server.py:ro"` osv.) for alle `mcp-linkml-*-run`/`-smoke`/`-test`-
target. Dette tyder at det som faktisk vert bakt inn i imaget via `COPY` **ikkje** er det som
køyrer ved lokal utvikling — det er berre det som køyrer når imaget brukast **standalone, utan
mount** (t.d. ein ekstern MCP-klient som peikar direkte på det publiserte GHCR-imaget). Ei
konsolidering må difor framleis bake inn korrekte, distinkte script per variant — men sidan
scripta til saman berre er nokre titals KB, er ikkje det noko hinder.

### Design: éin Dockerfile med delte multi-stage-lag og tre namngjevne sluttmål

I staden for å publisere ein separat, delt basisimage til GHCR (meir kompleksitet: ny
bygge-rekkjefølgje-avhengigheit i `ensure-images`-jobben, ny hash-tag-oppslag, `FROM`-referanse
som må vere ulik lokalt vs. i CI) — bruk **éin Dockerfile med fleire namngjevne stage** og bygg
kvar variant med `podman build --target <namn>`. Same delte lag (base-runtime-stega) vert då
bygd/cacha éin gong per byggjemiljø, og — viktigare for GHCR-målet — **dei resulterande laga får
identisk digest på tvers av alle tre image** (same instruksjonar ⇒ same innhald ⇒ same
SHA256), noko som let podman/buildah sin cross-repo blob-mount gjenbruke dei ved push, heilt
utan den ekstra kompleksiteten ein separat publisert basisimage ville kravd.

```dockerfile
# src/assets/containers/Dockerfile.mcp-linkml
FROM python:3.11-slim AS base-builder
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential \
    && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir --prefix=/install \
    "linkml>=1.11.1,<2.0.0" "linkml-runtime>=1.11.1,<2.0.0" "pyyaml>=6.0.3"

FROM python:3.11-slim AS base-runtime
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY --from=base-builder /install /usr/local

FROM base-runtime AS validator
COPY src/mcp-linkml-validator/server.py src/mcp-linkml-validator/validate-and-log.py ./
COPY src/mcp-linkml-validator/policies/ policies/
RUN useradd -m mcp
USER mcp
CMD ["python", "server.py"]

FROM base-runtime AS modell-utkast
RUN pip install --no-cache-dir "pytest>=9.1.1"
COPY src/mcp-linkml-modell-utkast/server.py src/mcp-linkml-modell-utkast/converter.py src/mcp-linkml-modell-utkast/validator.py ./
COPY src/mcp-linkml-modell-utkast/profiles/ profiles/
RUN useradd -m mcp
USER mcp
CMD ["python", "server.py"]

FROM base-runtime AS begrep-utkast
COPY src/mcp-linkml-begrep-utkast/server.py src/mcp-linkml-begrep-utkast/generator.py src/mcp-linkml-begrep-utkast/los_tema.py ./
COPY src/mcp-linkml-begrep-utkast/profiles/ profiles/
RUN useradd -m mcp
USER mcp
CMD ["python", "server.py"]
```

### Steg

1. Opprett `src/assets/containers/Dockerfile.mcp-linkml` med innhaldet over. Slett dei tre
   gamle `Dockerfile.mcp-linkml-validator`/`-modell-utkast`/`-begrep-utkast`.
2. Fjern dei tre `requirements.txt`-filene under `src/mcp-linkml-*/` (versjonane står no éin
   stad, i `base-builder`-stega) — **sjekk fyrst** at ingen andre stader (README, test-script,
   lokal venv-oppsett) refererer til desse filene før dei slettast.
3. Oppdater `make/60-mcp.mk` sine tre `build-docker-mcp-*`-target til å byggje med
   `--target validator`/`--target modell-utkast`/`--target begrep-utkast` mot den nye, felles
   Dockerfile-en (behald eksisterande image-namn `$(MCP_IMAGE)`/`$(LINKML_MOD_IMAGE)`/
   `$(LINKML_BEGREP_IMAGE)` uendra — ingen brot for eksisterande `make mcp-linkml-*-run` osv.).
4. Oppdater `release.yml` sine to jobbar for `mcp-linkml-modell-utkast`/`mcp-linkml-begrep-
   utkast` (nyleg fiksa i B1) til å byggje med `-f src/assets/containers/Dockerfile.mcp-linkml
   --target modell-utkast`/`--target begrep-utkast` i staden for dei separate filene. Same for
   `mcp-linkml-validator`-jobben (`--target validator`).
5. Oppdater `generate.yml` sitt `hashFiles(...)`-oppslag for `mcp-linkml-validator`-taggen
   (i dag `hashFiles('src/assets/containers/Dockerfile.mcp-linkml-validator',
   'src/mcp-linkml-validator/requirements.txt')`) til å peike på den nye, delte fila
   (`hashFiles('src/assets/containers/Dockerfile.mcp-linkml')`) — merk at dette no gjer at
   endringar i `modell-utkast`/`begrep-utkast`-stega (eller `base-builder`-stega) òg
   invaliderer `mcp-linkml-validator`-taggen, sidan alle tre no deler éi fil. Dette er tilsikta
   (delt kjelde ⇒ delt cache-nøkkel), men aukar litt kor ofte `mcp-linkml-validator` vert
   ombygd/pusha samanlikna med i dag.
6. Oppdater `images.json` sitt `mcp-linkml-validator`-oppslag: `dockerfile` → den nye, delte
   fila. `make_target` er uendra (`build-docker-mcp-validator`, uendra namn frå steg 3).
7. Test: bygg alle tre lokalt (`make build-docker-mcp-validator build-docker-mcp-modell-utkast
   build-docker-mcp-begrep-utkast`), køyr alle tre sine `-smoke`-target
   (`mcp-linkml-validate-smoke`, `mcp-linkml-modell-utkast-smoke`,
   `mcp-linkml-begrep-utkast-smoke`) og stadfest dei framleis fungerer identisk. Verifiser med
   `podman inspect --format '{{range .RootFS.Layers}}{{.}}\n{{end}}'` at dei delte laga
   (`base-builder`/`base-runtime`-stega) har identisk digest på tvers av alle tre.

### Risiko/ting å avklare

- Ingen ny bygge-rekkjefølgje-avhengigheit i CI (unngått ved å bruke `--target` i staden for ein
  separat publisert basisimage) — lågare risiko enn den opphavleg vurderte tilnærminga.
- `hashFiles()`-endringa i steg 5 gjer at `mcp-linkml-validator` sin GHCR-tag endrar seg oftare
  (delt fil ⇒ delt cache-nøkkel) — akseptabelt, men verdt å nemne i commit-meldinga.
- Sjekk om `src/mcp-linkml-*/requirements.txt` er referert andre stader før dei slettast
  (steg 2).

## B4 — vurder Alpine-migrering for `linkml-local`/`mcp-linkml-*` (python:3.11-slim → alpine)

### Spike (gjennomført under planlegging, 2026-08-04)

Bygde følgjande mot `python:3.11-alpine` med same versjonar som `Dockerfile.linkml` brukar i
dag (`linkml==1.11.1`, `rdflib`):

```dockerfile
FROM python:3.11-alpine AS builder
RUN apk add --no-cache --virtual .build-deps gcc musl-dev libffi-dev g++ make cmake rust cargo
RUN pip install --no-cache-dir --prefix=/install "linkml==1.11.1" rdflib
FROM python:3.11-alpine
COPY --from=builder /install /usr/local
```

**Resultat:**
- Bygget **lukkast utan feil**. Sjekka på førehand at `pydantic-core` (den einaste tunge
  C-utvidinga i avhengigheitstreet, brukt av `pydantic`/`linkml`) publiserer musllinux-wheel
  for `cp311` på PyPI (21 wheel-variantar funne) — stadfesta empirisk: pip-loggen viser at
  `pydantic_core`, `wrapt`, `greenlet` osv. alle vart installerte frå ferdigbygde musllinux-
  wheel, **ingen Rust-/C-kompilering frå kjeldekode trengst** (dei fire pakkane som vart bygde
  frå kjelde — `antlr4-python3-runtime`, `watchdog`, `cfgraph`, `pytest-logging` — er reine
  Python-pakkar utan kompilert kode, raskt bygd).
- Storleik: **222 MB** (rå, utan `patch`-laget/multi-stage-triminga `Dockerfile.linkml` elles
  har). Samanlikna med noverande `linkml-local` (294 MB, etter A4-fiksen) er dette ei
  **moderat, ikkje dramatisk** innsparing (~25 %) — mesteparten av biletstorleiken kjem frå
  sjølve Python-pakkane (sphinx, sqlalchemy, babel m.fl.), ikkje frå distro-laget, så
  Alpine-basisen sin fordel (129 MB → 48 MB åleine) et berre delvis gjennom til sluttresultatet.

### Design/steg (dersom ein går vidare)

1. Bygg fullverdig `Dockerfile.linkml`-variant på Alpine (inkl. `patch`-laget for
   `docgen-max-chars.patch` — stadfest at `patch`-kommandoen er tilgjengeleg via `apk add
   patch` eller tilsvarande).
2. Bygg tilsvarande Alpine-variantar av dei tre `mcp-linkml-*`-stega frå B2 (same
   avhengigheitssett, `linkml`/`linkml-runtime`/`pyyaml` ± `pytest`) — dersom B2 er gjennomført
   fyrst, gjer dette som eit alternativt `base-builder`/`base-runtime`-stagepar.
3. **Full regresjonstest** — dette er ikkje gjort i spiken over, berre `pip install` vart
   verifisert. Krevst før nokon permanent overgang:
   - `make domain-<kvart av dei 9 domena>` — alle generatorar (`gen-doc`, `gen-erdiagram`,
     `gen-shacl`, `gen-owl`, `gen-rdf` osv.) på musl/Alpine i staden for glibc/Debian.
   - `make roundtrip` på eit breitt utval skjema — musl sin `re`/locale-/Unicode-handtering kan
     i sjeldne tilfelle avvike frå glibc og påverke RDF-serialisering eller sortering.
   - Byggjetid: samanlikn `make build-docker-linkml` sin tidsbruk Alpine vs. slim — pip-
     wheel-installasjon var rask i spiken, men verdt å måle systematisk over fleire køyringar
     (nettverksvariasjon i CI kan gje andre tal enn lokalt).
4. Oppdater `Dockerfile.linkml` (og evt. `Dockerfile.mcp-linkml` frå B2) berre dersom steg 3
   ikkje avdekkjer regresjonar.

### Risiko

**Moderat, høgast av dei tre punkta.** Spiken stadfestar at *installasjonen* lukkast, men seier
ingenting om *køyretidsåtferd* — heile generator-pipelinen (særleg RDF/SPARQL-relatert kode i
`rdflib`/`linkml-runtime`, som kan vere kjenslevar for musl sine skilnader frå glibc i
lokale-/reguttrykk-/flyttal-handtering) er uverifisert. Gevinsten (~25 %, ikkje dei ~63 %
biletet sin basisstorleik isolert skulle tilseie) er også mindre enn for B2/B3, og talet på
CI-jobbar som pullar `linkml-local` (alle 9 domene, kvar `generate.yml`- **og** `validate.yml`-
køyring) gjer ein eventuell regresjon dyr å oppdage seint. **Tilråding: lågast prioritet av dei
tre, og bør ikkje iverksetjast utan full regresjonstesting (steg 3) fyrst.**

## Handlingsliste

- [x] B3: erstatt `Dockerfile.plantuml` med Temurin-JRE-Alpine-variant, verifiser breiare
      (fleire skjema) enn spiken, oppdater dersom avvik
- [ ] B2: slå saman dei tre `mcp-linkml-*`-Dockerfile-ane til éin fil med `--target`-stega,
      oppdater `make/60-mcp.mk`, `release.yml`, `generate.yml` (hashFiles), `images.json`
- [ ] B4: full regresjonstest av Alpine-migrering (domene-pipeline, roundtrip, byggjetid) —
      berre iverksett dersom testane ikkje avdekkjer regresjonar
