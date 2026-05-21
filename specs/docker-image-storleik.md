# Reduksjon av Docker-imagestorleik

## Situasjon

Repoet har fem Docker-images:

| Image | Dockerfile | Basisbilde |
|-------|------------|------------|
| `mcp-linkml-generator` | `src/mcp-linkml-generator/Dockerfile` | `python:3.11-slim` |
| `mcp-linkml-validator` | `src/mcp-linkml-validator/Dockerfile` | `python:3.11-slim` |
| `linkml-local` | `src/assets/containers/Dockerfile.linkml` | `linkml/linkml:1.11.0` |
| `python-pytest` | `src/assets/containers/Dockerfile.python` | `python:3.11-slim` |
| `mkdocs-local` | `mkdocs/Dockerfile.mkdocs` | `squidfunk/mkdocs-material:9.5` |

---

## Analyse per image

### mcp-linkml-generator og mcp-linkml-validator (~800 MB–1 GB estimert)

Begge Dockerfiles følgjer same mønster:

```dockerfile
FROM python:3.11-slim          # ~130 MB
RUN apt-get install build-essential git  # +~280 MB
RUN pip install -r requirements.txt      # +~450 MB (linkml + avhengigheiter)
```

**Problem:** `build-essential` og `git` er installert for å kunne kompilera C-extensions under `pip install`, men dei ligg att i det ferdige imaget og utgjer om lag 280 MB overhead per image.

`git` er ikkje naudsynt ved køyretid — alle avhengigheiter i `requirements.txt` er versjonspinna PyPI-pakkar som ikkje krev `git clone`.

**Løysing — fleirsstegsbygg:**

```dockerfile
# --- builder ---
FROM python:3.11-slim AS builder
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# --- runtime ---
FROM python:3.11-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app
COPY --from=builder /install /usr/local
RUN touch server.py && useradd -m mcp
USER mcp
CMD ["python", "server.py"]
```

`build-essential` og `git` finst berre i builder-steget og følgjer ikkje med i det endelege imaget.

**Estimert innsparing:** 250–300 MB per image.

---

### linkml-local (estimert ~1,5 GB)

```dockerfile
FROM docker.io/linkml/linkml:1.11.0   # svært stort upstream-image
RUN pip install --no-cache-dir rdflib  # liten tillegg
```

Upstream-imaget `linkml/linkml` er bygd på full Debian og inkluderer Java (for ROBOT/OWL-verktøy), Node.js og fleire tyngre avhengigheiter som ikkje vert brukt her. Det er avgrensa kor mykje ein kan gjera med berre eit `RUN pip install` på toppen.

**Alternativ — bygg frå scratch:**

Erstatt `linkml/linkml`-basen med `python:3.11-slim` og installer berre det som faktisk vert brukt (`linkml`, `rdflib`). Dette krev å kartleggja nøyaktig kva `linkml`-kommandoar Makefile nyttar:

```bash
grep -oE 'linkml-[a-z-]+|gen-[a-z-]+' Makefile | sort -u
```

Typisk er berre `gen-python`, `gen-jsonld-context` og `gen-owl` i bruk — desse er alle inkludert i `linkml`-pakken på PyPI og treng ikkje Java.

Ei slik reimplementering har høg effekt (~1 GB innsparing) men krev testing for å sikra at alle generatorar framleis fungerer.

**Estimert innsparing:** 800 MB–1 GB (viss ein byter til python:3.11-slim-base).

---

### python-pytest (~200 MB estimert)

```dockerfile
FROM python:3.11-slim
RUN pip install pytest pyyaml
```

Allereie eit av dei lettaste imagene. `pytest` og `pyyaml` har ingen C-extensions som krev kompilering, og er kompatible med Alpine Linux.

**Alternativ — Alpine-base:**

```dockerfile
FROM python:3.13-alpine
RUN pip install --no-cache-dir pytest>=9.0.3 pyyaml>=6.0.3
```

`python:3.13-alpine` er om lag 55 MB mot 130 MB for `python:3.11-slim`. Ei alternativ oppdatering til `python:3.13-slim` gjer liten skilnad på storleik, men held ein på kjend libc.

**Estimert innsparing:** 80–100 MB.

---

### mkdocs-local (estimert ~300 MB)

```dockerfile
FROM squidfunk/mkdocs-material:9.5
RUN pip install mkdocs-kroki-plugin mkdocs-build-cache-plugin
```

Upstream-imaget er allereie godt optimert, og dei to pluginane legg til lite. Ingen vesentleg optimering er tilgjengeleg her utan å erstatta heile basisbiletet.

---

## Samanstilling

| Image | Hovudproblem | Tiltak | Estimert innsparing |
|-------|-------------|--------|---------------------|
| `mcp-linkml-generator` | `build-essential` + `git` i runtime | Fleirsstegsbygg | ~270 MB |
| `mcp-linkml-validator` | `build-essential` + `git` i runtime | Fleirsstegsbygg | ~270 MB |
| `linkml-local` | Tung upstream-base (Java, Node.js) | Bygg frå `python:3.11-slim` | ~800 MB–1 GB |
| `python-pytest` | `python:3.11-slim` vs Alpine | Byt til `python:3.13-alpine` | ~90 MB |
| `mkdocs-local` | Ingen vesentleg | — | — |

---

## Tilråding og prioritet

| Prioritet | Tiltak | Innsats | Effekt |
|-----------|--------|---------|--------|
| 1 | Fleirsstegsbygg for generator og validator | Låg (endra to Dockerfiles) | Høg (~540 MB total) |
| 2 | Alpine-base for python-pytest | Svært låg (ei linje) | Liten (~90 MB) |
| 3 | Rebuild linkml-local frå scratch | Høg (krev kartlegging og testing) | Svært høg (~1 GB) |

Start med **tiltak 1** — fleirsstegsbygg for generator og validator gir størst gevinst for minst innsats, og mønsteret er trygt og velprøvd. Tiltak 3 gir størst absolutt innsparing, men krev grundig testing av alle `make`-mål som bruker `linkml-local`.
