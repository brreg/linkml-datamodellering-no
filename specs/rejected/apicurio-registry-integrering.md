# Plan: Integrasjon mot Apicurio Registry

## Avvist

**Avvist 2026-06-10.** Denne planen er avvist fordi han bryt med eit grunnleggjande arkitekturprinsipp for dette repoet: **repoet pusher aldri artefaktar til eksterne kjelder.**

Apicurio Registry-integrasjonen ville krevje at repoet sjølv pushar genererte artefaktar til ein ekstern schema-registry. Dette er problematisk av fleire grunnar:

- **Spesialtilpassingar per målsystem** — kvar ekstern kjelde har sitt eige autentiseringsopplegg, API-konvensjonar og feilhåndteringsreglar som repoet må tilpassast til.
- **Ekstern avhengigheit** — CI-pipeline-en vert avhengig av at den eksterne tenesta er oppe og tilgjengeleg. Nedetid hjå registryen feilar publisering av modellane.
- **Ansvarsfelt** — dette repoet har ansvar for å *generere* og *gjere tilgjengeleg* artefaktar, ikkje for å *distribuere* dei til konsumentar sine system.

**Rett tilnærming:** Konsumentar som ønsker å bruke artefaktane i Apicurio Registry hentar dei sjølve via `raw.githubusercontent.com` eller GitHub Releases og importerer til sin eigen registry. Sjå prinsipp i `CLAUDE.md` og `README.md`.

---

## Bakgrunn

Apicurio Registry er ein open-source schema- og API-registry som støttar
OpenAPI, AsyncAPI, JSON Schema, Avro, XSD, Protobuf og fleire format.
Integrasjonen gjer det mogleg å publisere genererte artefaktar frå dette repoet
til ein sentral registry, slik at konsumentar kan hente skjema via API heller
enn å laste ned filer frå portalen.

**Apicurio Registry v3 REST API (base: `/apis/registry/v3`):**

| Operasjon | Endepunkt |
|---|---|
| Opprett/oppdater artefakt | `POST /groups/{groupId}/artifacts` |
| Ny versjon | `POST /groups/{groupId}/artifacts/{artifactId}/versions` |
| Hent artefaktmetadata | `GET /groups/{groupId}/artifacts/{artifactId}` |
| Liste artefaktar i gruppe | `GET /groups/{groupId}/artifacts` |

Relevante artefakttypar: `OPENAPI`, `ASYNCAPI`, `JSON`, `XSD`

Relevante request-headers:
- `X-Registry-ArtifactId` — unik ID innanfor gruppa
- `X-Registry-ArtifactType` — type (OPENAPI, ASYNCAPI, JSON, XSD)
- `X-Registry-Version` — versjonsnummer
- `X-Registry-Name` — visingsnamn
- `X-Registry-Description` — skildring
- `X-Registry-IfExists` — `UPDATE` | `FAIL` | `RETURN_OR_UPDATE`

---

## Opne spørsmål

| # | Spørsmål | Alternativ |
|---|---|---|
| 1 | **Registry-URL** | (a) Sjølvhosta (t.d. internt i infrastruktur). (b) Apicurio Cloud (`registry.apicur.io`). (c) Lokal dev-instans via `apicurio/apicurio-registry-mem`. |
| 2 | **Autentisering** | (a) API-nøkkel (header `Authorization: Bearer <token>`). (b) Basic auth. (c) Ingen (open dev-instans). |
| 3 | **Artefakttypar** | (a) OpenAPI + AsyncAPI — berre dei formata konsumentane faktisk brukar. (b) OpenAPI + AsyncAPI + JSON Schema + XSD — alle genererte format. |
| 4 | **Gruppestruktur** | (a) Éin gruppe per domene (t.d. `ngr`, `fint`, `samt`). (b) Éin gruppe per skjema (t.d. `ngr-adresse`). (c) Éin global gruppe `linkml-datamodellering-no`. |
| 5 | **Trigger** | (a) Eige `make apicurio-publish`-mål — manuelt eller frå CI etter `make docs-publish`. (b) Integrert direkte i `generate.yml` som eige jobb. |

---

## Teknisk tilnærming

### Mapping: LinkML-skjema → Apicurio-artefakt

| LinkML-felt | Apicurio-felt |
|---|---|
| `manifest.yaml` `data_policy` + `publish_external` | Avgjer om skjema skal publiserast |
| Skjemanamn (`name:` i YAML) | `artifactId` |
| `title:` | `X-Registry-Name` |
| `description:` | `X-Registry-Description` |
| `version:` | `X-Registry-Version` |
| Domene (katalognamn) | `groupId` (avheng av svar på sp. 4) |

### Publiserings-pipeline

```
generated/<domain>/<name>/<name>-openapi.yaml   (viss openapi: true)
generated/<domain>/<name>/<name>-asyncapi.yaml  (viss asyncapi: true)
generated/<domain>/<name>/<name>-schema.json    (viss json_schema: true)
generated/<domain>/<name>/<name>-schema.xsd     (viss xsd: true)
    ↓  publish-apicurio.py
POST /apis/registry/v3/groups/<groupId>/artifacts
    med X-Registry-IfExists: UPDATE
```

### Ny `manifest.yaml`-nøkkel

```yaml
publish_apicurio: false   # opt-in, uavhengig av publish_external
```

### Lokal testing med in-memory-instans

```bash
podman run --rm -p 8080:8080 docker.io/apicurio/apicurio-registry-mem:latest
# → http://localhost:8080/apis/registry/v3
```

---

## Steg 1 — Verifiser lokalt oppsett

Start `apicurio/apicurio-registry-mem` og test mot `/apis/registry/v3/system/info`.
Dokumenter versjon og API-basisbane.

---

## Steg 2 — Skriv `publish-apicurio.py`

`src/assets/scripts/publish-apicurio.py` — Python 3.12, køyrer i `python-pytest`-container.
Avhengigheiter: `requests` (legg til `requirements-python-test.txt`).

Argumentar:
```
publish-apicurio.py
  --registry-url <url>
  --group <groupId>
  --schema <path/to/*-schema.yaml>
  [--token <token>]
  [--dry-run]
```

Scriptet:
1. Les manifest og YAML-skjema for metadata
2. For kvar aktivert artefakttype (`openapi`, `asyncapi`, `json_schema`, `xsd`):
   - Finn generert fil i `generated/`
   - `POST` til registry med korrekte headers og `X-Registry-IfExists: UPDATE`
3. Skriv ut kva som vart publisert (URL til artefaktet i registryen)

---

## Steg 3 — Test manuelt mot lokal instans

Aktivér `publish_apicurio: true` for `samt-bu`, køyr mot lokal `apicurio-registry-mem`:

```bash
podman run --rm --entrypoint python3 -v "$(pwd):/work" localhost/python-pytest:latest \
    /work/src/assets/scripts/publish-apicurio.py \
    --registry-url http://host.containers.internal:8080 \
    --group samt \
    --schema /work/src/linkml/samt/samt-bu/samt-bu-schema.yaml \
    --dry-run
```

Verifiser via Apicurio UI (`http://localhost:8080/ui`) at artefaktane dukkar opp
med riktig type, versjon og metadata.

---

## Steg 4 — Legg til `publish_apicurio`-flagg i `manifest.yaml`-malen

Oppdater alle relevante `manifest.yaml`-filer med nytt toppnivå-flagg:

```yaml
publish_external: false
publish_apicurio: false   # ← nytt, opt-in
data_policy: silver
```

---

## Steg 5 — Legg til `apicurio-publish`-mål i `Makefile`

```makefile
apicurio-publish:
    # Krev REGISTRY_URL og REGISTRY_GROUP, valfri REGISTRY_TOKEN
    $(call run_apicurio_publish,$(SCHEMAS))

schema-apicurio-publish:
    $(call run_apicurio_publish,$(SCHEMA))
```

Makro `run_apicurio_publish` sjekkar `publish_apicurio: true` i manifest før køyring.

---

## Steg 6 — CI-integrering (valfri)

Legg til eige `apicurio-publish`-jobb i `generate.yml` som køyrer etter `publish`-jobben,
med `REGISTRY_URL` og `REGISTRY_TOKEN` som GitHub Actions secrets.

Alternativt: berre manuelt `make apicurio-publish` for no.

---

## Prioritert handlingsliste

| # | Steg | Fil | Avhengigheit |
|---|---|---|---|
| 1 | Verifiser lokal instans | — | Svar på sp. 1-2 |
| 2 | Skriv `publish-apicurio.py` | `src/assets/scripts/publish-apicurio.py` | Steg 1, svar på sp. 3-4 |
| 3 | Test manuelt | `samt-bu` mot lokal instans | Steg 2 |
| 4 | Manifest-flagg | Alle relevante `manifest.yaml` | Steg 3 |
| 5 | Makefile-mål | `Makefile` | Steg 2, 4 |
| 6 | CI-integrering (valfri) | `generate.yml` | Svar på sp. 5 |

---

## Avhengigheiter

- `requests` Python-pakke — legg til `requirements-python-test.txt`
- Apicurio Registry-instans (URL + eventuell token) — konfigurert via miljøvariablar
- `openapi: true` / `asyncapi: true` / `xsd: true` for relevante skjema (allereie aktivert for `samt-bu`)
- Ingen ny container nødvendig — scriptet køyrer i `python-pytest`-container
