# Optimalisering av Docker-image-størrelse

**Status:** ✓ Utført  
**Prioritet:** Middels  
**Estimat:** 1-2 dagar  
**Opprettet:** 2026-07-04  
**Fullført:** 2026-07-04

## Bakgrunn

Repoet byggjer 9 Docker-images for ulike formål (LinkML-generering, MCP-serverar, dokumentasjon, testing). Redusert image-størrelse gir:
- Raskare bygging lokalt og i CI
- Mindre diskbruk for utviklararar
- Raskare pull-tider frå container-registry
- Redusert nettverkstrafikk

Per no er det ikkje kartlagt kva den faktiske størrelsen på kvart image er, eller kva potensial for reduksjon som finst.

## Målsetjing

Gjennomgå alle Docker-images i repoet og implementere tiltak for å redusere størrelsen der det er hensiktsmessig, utan å kompromittere funksjonalitet eller vedlikehaldbarheit.

**Suksesskriterium:** Dokumentert gjennomgang av alle images med konkrete tiltak implementerte der gevinsten er >10% reduksjon.

## Kartlegging

### Oversikt over Docker-images

| Image | Dockerfile | Base image | Multi-stage | Formål |
|---|---|---|---|---|
| `linkml-local` | `src/assets/containers/Dockerfile.linkml` | `python:3.11-slim` | ✓ | LinkML-generatorar (gen-*, linkml-convert) |
| `mkdocs-local` | `mkdocs/Dockerfile.mkdocs` | `squidfunk/mkdocs-material:9.5` | ✗ | MkDocs Material dokumentasjonsportal |
| `python-pytest` | `src/assets/containers/Dockerfile.python` | `python:3.13-alpine` | ✗ | Python-testar (pytest, roundtrip-testar) |
| `mcp-linkml-validator` | `src/mcp-linkml-validator/Dockerfile` | `python:3.11-slim` | ✓ | MCP-server for policy-validering |
| `mcp-linkml-modell-utkast` | `src/mcp-linkml-modell-utkast/Dockerfile` | `python:3.11-slim` | ✓ | MCP-server for modell-utkast frå JSON Schema |
| `mcp-linkml-begrep-utkast` | `src/mcp-linkml-begrep-utkast/Dockerfile` | `python:3.11-slim` | ✓ | MCP-server for begreps-utkast |
| `avrotize-local` | `src/assets/containers/Dockerfile.avrotize` | `python:3.12-slim` | ✗ | XSD-generering via Avrotize |
| `asyncapi-cli-local` | `src/assets/containers/Dockerfile.asyncapi-cli` | `asyncapi/cli:latest` | ✗ | AsyncAPI CLI-validering |
| `gource-local` | `src/assets/containers/Dockerfile.gource` | `ubuntu:22.04` | ✗ | Gource-visualisering (påskeegg) |

### Typiske kjelder til bloat

1. **Unødvendige byggjeavhengigheiter** — kompilatorar, header-filer, dev-pakkar som ikkje trengst i runtime
2. **Pip/apt cache** — pakkelast-cache som ikkje vert rydda
3. **Base image-val** — `python:3.11` (920 MB) vs `python:3.11-slim` (130 MB) vs `python:3.11-alpine` (50 MB)
4. **Mange lag** — kvar `RUN`-kommando = eitt lag; konsolidering kan redusere overhead
5. **Installerte men ubrukte avhengigheiter** — transitiv dependencies som ikkje faktisk vert nytta
6. **Test-avhengigheiter i produksjon** — pytest, mypy, ruff i runtime-image
7. **Dokumentasjonsfiler** — README, CHANGELOG, eksempelfiler frå pip-pakkar

## Tiltak per image

### 1. `linkml-local` (høg prioritet — brukt i alle generatorar)

**Noverande status:**
- Multi-stage build: ✓
- Base image: `python:3.11-slim`

**Mulige tiltak:**
- [ ] **Kartlegg faktisk størrelse** med `podman images localhost/linkml-local`
- [ ] **Vurder alpine i staden for slim** — alpine er ~80 MB mindre, men kan krevje ekstra byggjeavhengigheiter (gcc, musl-dev) for visse Python-pakkar. Test at alle LinkML-generatorar fungerer.
- [ ] **Rydd apt cache** — legg til `rm -rf /var/lib/apt/lists/*` etter `apt-get install`
- [ ] **Rydd pip cache** — `pip install --no-cache-dir`
- [ ] **Konsolider RUN-kommandoar** — minimer antal lag
- [ ] **Installer berre nødvendige system-pakkar** — sjekk om alle pakkar i `apt-get install`-lista faktisk trengst
- [ ] **Vurder .dockerignore** — unngå å kopiere unødvendige filer inn i build-kontekst

**Forventa gevinst:** 10-20% reduksjon dersom alpine fungerer; 5-10% ved cache-rydding åleine.

---

### 2. `python-pytest` (middels prioritet — berre brukt i test-suite)

**Noverande status:**
- Multi-stage build: ✗
- Base image: `python:3.13-alpine`

**Mulige tiltak:**
- [ ] **Kartlegg faktisk størrelse**
- [ ] **Rydd pip cache** — `pip install --no-cache-dir`
- [ ] **Vurder multi-stage** — installer pytest i builder-stage, kopier berre runtime-avhengigheiter til final stage (men pytest *er* runtime-avhengigheit her, så gevinsten er minimal)
- [ ] **Installer berre nødvendige test-avhengigheiter** — sjekk `requirements-test.txt`

**Forventa gevinst:** 5-10% reduksjon.

---

### 3. MCP-serverar (`mcp-linkml-validator`, `mcp-linkml-modell-utkast`, `mcp-linkml-begrep-utkast`)

**Noverande status:**
- Multi-stage build: ✓ (alle tre)
- Base image: `python:3.11-slim`

**Observasjon:** Alle tre har identisk Dockerfile-struktur — dei kan bruke same optimalisering.

**Mulige tiltak:**
- [ ] **Kartlegg faktisk størrelse** for kvar
- [ ] **Konsolider Dockerfile-struktur** — lag ein felles `Dockerfile.mcp-base` dersom dei tre er tilstrekkeleg like
- [ ] **Rydd apt cache** — `rm -rf /var/lib/apt/lists/*`
- [ ] **Rydd pip cache** — `pip install --no-cache-dir`
- [ ] **Vurder alpine** — test at alle MCP-serverar fungerer med alpine (linkml-runtime kan ha native avhengigheiter)
- [ ] **Installer berre nødvendige system-pakkar** — sjekk om `git` og andre pakkar faktisk trengst i runtime-stage

**Forventa gevinst:** 10-15% reduksjon per image.

---

### 4. `mkdocs-local` (låg prioritet — eksternt vedlikehald)

**Noverande status:**
- Multi-stage build: ✗
- Base image: `squidfunk/mkdocs-material:9.5` (eksternt vedlikehald)

**Mulige tiltak:**
- [ ] **Kartlegg faktisk størrelse**
- [ ] **Vurder om ekstra pip-pakkar er nødvendige** — Dockerfile installerer `mkdocs-build-cache-plugin`; sjekk om den faktisk vert brukt
- [ ] **Rydd pip cache** — `pip install --no-cache-dir`

**Forventa gevinst:** <5% reduksjon (avgrensa kontroll over base image).

---

### 5. `avrotize-local` (låg prioritet — berre brukt for XSD-generering)

**Noverande status:**
- Multi-stage build: ✗
- Base image: `python:3.12-slim`

**Mulige tiltak:**
- [ ] **Kartlegg faktisk størrelse**
- [ ] **Rydd pip cache** — `pip install --no-cache-dir`
- [ ] **Vurder alpine**
- [ ] **Multi-stage build** — installer avrotize i builder, kopier berre runtime til final stage

**Forventa gevinst:** 10-15% reduksjon.

---

### 6. `asyncapi-cli-local` (låg prioritet — eksternt vedlikehald)

**Noverande status:**
- Multi-stage build: ✗
- Base image: `asyncapi/cli:latest` (eksternt vedlikehald)

**Mulige tiltak:**
- [ ] **Kartlegg faktisk størrelse**
- [ ] **Ingen tiltak** — Dockerfile er éi linje (`FROM asyncapi/cli:latest`), ingen kontroll over størrelse

**Forventa gevinst:** 0% (ingen kontroll).

---

### 7. `gource-local` (låg prioritet — påskeegg, berre brukt manuelt)

**Noverande status:**
- Multi-stage build: ✗
- Base image: `ubuntu:22.04`

**Mulige tiltak:**
- [ ] **Kartlegg faktisk størrelse**
- [ ] **Vurder alpine i staden for ubuntu** — gource finst i Alpine-repos (`apk add gource ffmpeg`)
- [ ] **Rydd apt cache** — `rm -rf /var/lib/apt/lists/*`

**Forventa gevinst:** 20-30% reduksjon ved bytte til alpine.

---

## Gjennomføring

### Steg 1: Kartlegging av noverande størrelse

Køyr `podman images` og dokumenter størrelse per image i ein tabell:

```bash
podman images --format "table {{.Repository}}:{{.Tag}}\t{{.Size}}" | grep -E "linkml-local|mkdocs-local|python-pytest|mcp-linkml|avrotize-local|asyncapi-cli-local|gource-local"
```

Lagre output i `specs/backlog/docker-image-storleik-baseline.md`.

### Steg 2: Implementer tiltak per image

For kvar image:
1. Implementer tiltak frå lista over
2. Bygg image på nytt
3. Dokumenter størrelse før/etter
4. Verifiser at funksjonalitet er bevart:
   - `linkml-local`: køyr `make test` for eit skjema
   - `python-pytest`: køyr `make roundtrip`
   - MCP-serverar: køyr smoke-testar (`make mcp-*-smoke`)
   - `mkdocs-local`: køyr `make docs-build`
   - `avrotize-local`: køyr `make gen-xsd` for eit skjema med XSD aktivert
   - `gource-local`: køyr `make gource-preview`

### Steg 3: Oppdater dokumentasjon

- Legg til `.dockerignore`-filer der det manglar
- Dokumenter eventuelle avvik (t.d. dersom alpine ikkje fungerer for linkml-local)
- Oppdater `COMMANDS.md` dersom nye bygg-flagg vert lagt til

### Steg 4: Samanlikn før/etter

| Image | Før | Etter | Reduksjon | % | Tiltak |
|---|---|---|---|---|---|
| linkml-local | 352 MB | 352 MB | 0 MB | 0% | Allereie optimalisert (multi-stage, --no-cache-dir, apt cleanup) |
| python-pytest | 79.2 MB | 79.2 MB | 0 MB | 0% | Allereie optimalisert (alpine, --no-cache-dir) |
| mcp-linkml-validator | 290 MB | 290 MB | 0 MB | 0% | Allereie optimalisert (multi-stage, --no-cache-dir, apt cleanup) |
| mcp-linkml-modell-utkast | 292 MB | 292 MB | 0 MB | 0% | Allereie optimalisert (multi-stage, --no-cache-dir, apt cleanup) |
| mcp-linkml-begrep-utkast | 290 MB | 290 MB | 0 MB | 0% | Allereie optimalisert (multi-stage, --no-cache-dir, apt cleanup) |
| mkdocs-local | 200 MB | 200 MB | 0 MB | 0% | Allereie optimalisert (--no-cache-dir); base image eksternt vedlikehald |
| avrotize-local | 603 MB | 552 MB | 51 MB | 8% | Bytta til alpine, multi-stage build, apk del .build-deps |
| asyncapi-cli-local | 4.43 GB | 4.43 GB | 0 GB | 0% | Eksternt vedlikehald (asyncapi/cli:latest). Docker Hub viser 1.4 GB (komprimert), Podman viser 4.43 GB (ukomprimert). |
| gource-local | 559 MB | 322 MB | 237 MB | 42% | Bytta frå ubuntu:22.04 til alpine:3.19 |
| **Totalt** | **6.98 GB** | **6.69 GB** | **288 MB** | **4%** | |

**Total reduksjon:** 288 MB (4% av total størrelse)  
**Største gevinst:** gource-local (237 MB / 42% reduksjon)  
**Største blocker:** asyncapi-cli-local (4.43 GB ukomprimert, 1.4 GB komprimert på Docker Hub — eksternt vedlikehald, ingen kontroll)

**Merknad om image-størrelse:** Podman viser ukomprimert størrelse (sum av alle lag), medan Docker Hub viser komprimert størrelse (brukt ved pull). Dette forklarer skilnaden mellom 4.43 GB (Podman) og 1.4 GB (Docker Hub) for asyncapi-cli-local.

---

## Referansar

- [Docker best practices for Python](https://docs.docker.com/language/python/containerize/)
- [Smaller Python Docker images](https://pythonspeed.com/articles/base-image-python-docker-images/)
- [Multi-stage builds](https://docs.docker.com/build/building/multi-stage/)
- [Alpine vs slim vs full Python images](https://pythonspeed.com/articles/alpine-docker-python/)

---

## Avhengigheiter

Ingen.

## Risiko

**Låg risiko** — alle endringar kan testast lokalt før commit. Einaste risiko er at alpine-baserte images kan krevje ekstra native dependencies for visse Python-pakkar (rdflib, pydantic osv.), men dette kan testast og reverterast.

## Utført

**Dato:** 2026-07-04

**Resultat:**
- ✓ Kartlagt alle 9 Docker-images med noverande størrelse
- ✓ Implementert optimalisering for `gource-local` (ubuntu → alpine): 237 MB reduksjon (42%)
- ✓ Implementert optimalisering for `avrotize-local` (alpine + multi-stage): 51 MB reduksjon (8%)
- ✓ Verifisert at alle andre images allereie var godt optimaliserte
- ✓ Testa funksjonalitet for avrotize-local og gource-local

**Konklusjon:**
Dei fleste images var allereie godt optimaliserte med multi-stage builds, `--no-cache-dir` og apt cleanup. Største gevinsten kom frå å byte `ubuntu:22.04` → `alpine:3.19` for gource-local. asyncapi-cli-local (4.43 GB ukomprimert / 1.4 GB komprimert) er eksternt vedlikehald og kan ikkje optimiserast — størrelsen er normal for eit Node.js-basert CLI-verktøy med mange avhengigheiter.

**Vidare arbeid (valfritt):**
- Vurder om asyncapi-cli kan bytast ut med ein mindre alternativ eller kjørast som GitHub Action i staden for lokal container
- Analyser om alle avrotize-avhengigheiter faktisk trengst (avrotize installerer 80+ Python-pakkar)
