# Konsistente kolonnar i COMMANDS.md

## Bakgrunn

COMMANDS.md er hovudreferansen for nye brukarar. Nokre seksjonar manglar `Output`-kolonna,
nokre brukar andre kolonntitlar (`Image`, `Bruk`) og beskriving er fleire stader for snau
til at ein ny brukar forstår kva som faktisk skjer.

## Mål

Alle kommandotabellar skal ha tre kolonnar: **Kommando · Beskriving · Output**.
- `Beskriving`: kva kommandoen gjer (maks 200 teikn)
- `Output`: kva som vert produsert (fil, katalog, stdout-melding, URL, image-namn — `—` om ingen)
- Ingen seksjon skal bruke andre kolonntitlar

---

## Tiltak per seksjon

### 1. Oppsett og føresetnadar

Manglar `Output`-kolonna. Legg til:

| Kommando | Beskriving | Output |
|---|---|---|
| `make check-prereqs` | Sjekkar at Podman, GNU make, user namespace og ledig diskplass er korrekt konfigurert | Skriv OK/FEIL per føresetnad til stdout; avsluttar med kode 1 ved feil |

---

### 2. Container-image-bygging

Brukar kolonnane `Kommando · Image · Bruk`. Erstatt heile tabellen med tre standardkolonnar.
Legg òg til `mcp-begrep-build` som manglar (sjå specs/done/commands-md-stale.md).

| Kommando | Beskriving | Output |
|---|---|---|
| `make linkml-build-docker` | Byggjer container-image for artefaktgenerering og validering. Berre nødvendig ved første bruk eller etter endringar i Dockerfile. | Image `localhost/linkml-local:latest` |
| `make docs-build-docker` | Byggjer container-image for dokumentasjonsportalen. Berre nødvendig ved første bruk eller etter endringar i Dockerfile. | Image `localhost/mkdocs-local:latest` |
| `make python-build-docker` | Byggjer container-image for Python-testar. Berre nødvendig ved første bruk eller etter endringar i Dockerfile. | Image `localhost/python-pytest:latest` |
| `make mcp-mod-build` | Byggjer container-image for modell-utkast MCP-server. | Image `localhost/mcp-linkml-modell-utkast:latest` |
| `make mcp-begrep-build` | Byggjer container-image for begrepsinstans-generator MCP-server. | Image `localhost/mcp-linkml-begrep-utkast:latest` |
| `make mcp-val-build` | Byggjer container-image for validator MCP-server. | Image `localhost/mcp-linkml-validator:latest` |

---

### 3. Ny modell

Har allereie tre kolonnar, men beskriving er knapt. Oppdater:

| Kommando | Beskriving | Output |
|---|---|---|
| `make new-model NAME=<modell> DOMAIN=<domain>` | Opprettar katalogstruktur og boilerplate for ein ny LinkML-modell. Skjemaet passerer `POLICY=bronze` utan manuell redigering. | `src/linkml/<domain>/<modell>/<modell>-schema.yaml`<br>`src/linkml/<domain>/<modell>/examples/<modell>-eksempel.yaml` |

---

### 4. Validering

Manglar `Output`-kolonna på alle rader. Legg til:

| Kommando | Beskriving | Output |
|---|---|---|
| `./tests/lint_schema.bash <skjema>` | Linter eit enkelt skjema raskt utan å køyre generatorar. Nyttig for hurtigsjekk under utvikling. | OK/FEIL til stdout; avsluttar med kode 1 ved feil |
| `./tests/validate_schema.bash <skjema> <eksempel>` | Validerer éin eksempelfil mot eit skjema utan lint og generatorar. Raskaste enkeltsjekk av datainnhald. | OK/FEIL til stdout; avsluttar med kode 1 ved feil |
| `make test SCHEMA=<sti>` | Køyrer full testsuite (lint + validering + alle generatorar) for eitt skjema. | Samla testrapport til stdout; avsluttar med kode 1 ved feil |
| `make test` | Linter alle skjema og validerer alle eksempelfiler i heile repoet. | Samla testrapport til stdout; avsluttar med kode 1 ved feil |
| `make validate` | Validerer alle skjema mot LinkML-metaskjemaet (strukturvalidering, ikkje policy). | Validerings-resultat per skjema til stdout |
| `make mcp-validate SCHEMA=<sti> POLICY=bronze` | Policy-validering på bronze-nivå: obligatoriske metadata, identifikatorar og begrepsreferansar. | Pass/fail per policy-regel til stdout |
| `make mcp-validate SCHEMA=<sti> POLICY=silver` | Policy-validering på silver-nivå: bronze + krav om import av DCAT-AP-NO og DQV-AP-NO. | Pass/fail per policy-regel til stdout |
| `make mcp-validate SCHEMA=<sti> POLICY=gold` | Policy-validering på gold-nivå: silver + FAIR-sjekkar F1–R1.3 (class_uri, lisens, proveniens m.m.). | Pass/fail per policy-regel til stdout |

---

### 5. mcp-linkml-modell-utkast

Nokre rader manglar `Output`. Fyll inn for alle:

| Kommando | Beskriving | Output |
|---|---|---|
| `make mcp-generate SCHEMA=<sti>` | Genererer eit LinkML-skjemautkast frå ei JSON Schema-fil ved hjelp av MCP-serveren. | `<same katalog>/<skjema>-schema.yaml` |
| `make mcp-generate SCHEMA=<sti> FORMAT=json-schema PROFILE=default` | Same som over med eksplisitt format og profil. | `<same katalog>/<skjema>-schema.yaml` |
| `make mcp-mod-build` | Byggjer container-image for MCP-serveren (eingongsoperasjon). | Image `localhost/mcp-linkml-modell-utkast:latest` |
| `make mcp-mod-smoke` | Køyrer røyktest med eksempel-meldingar for å verifisere at serveren svarar korrekt. | Testresultat til stdout; avsluttar med kode 1 ved feil |
| `make mcp-mod-test` | Køyrer alle unit-testar for MCP-serveren. | Testresultat til stdout; avsluttar med kode 1 ved feil |
| `make mcp-mod-run` | Startar MCP-serveren interaktivt. Nyttig for manuell testing og feilsøking. | JSON-RPC på stdin/stdout |

---

### 6. mcp-linkml-begrep-utkast

Manglar `Output`-kolonna. Legg til:

| Kommando | Beskriving | Output |
|---|---|---|
| `make mcp-begrep-build` | Byggjer container-image for MCP-serveren (eingongsoperasjon). | Image `localhost/mcp-linkml-begrep-utkast:latest` |
| `make mcp-begrep-run` | Startar MCP-serveren interaktivt. Nyttig for manuell testing og feilsøking. | JSON-RPC på stdin/stdout |
| `make mcp-begrep-smoke` | Køyrer røyktest med eksempel-meldingar for å verifisere at serveren svarar korrekt. | Testresultat til stdout; avsluttar med kode 1 ved feil |
| `make mcp-begrep-list-profiles` | Listar alle tilgjengelege organisasjonsprofiler som kan brukast ved oppretting av begrep. | JSON-liste over profil-ID-ar til stdout |

---

### 7. LinkML-validator mcp-server (mcp-linkml-validator)

Manglar `Output`-kolonna. `make mcp-validate` er allereie dokumentert i seksjon 4 (Validering);
vurder å fjerne duplikaten her og berre behalde build/smoke/test/run.

| Kommando | Beskriving | Output |
|---|---|---|
| `make mcp-val-build` | Byggjer container-image for validator MCP-serveren (eingongsoperasjon). | Image `localhost/mcp-linkml-validator:latest` |
| `make mcp-val-smoke` | Køyrer røyktest med eksempel-meldingar for å verifisere at serveren svarar korrekt. | Testresultat til stdout; avsluttar med kode 1 ved feil |
| `make mcp-val-test` | Køyrer alle policy-testar for validator MCP-serveren. | Testresultat til stdout; avsluttar med kode 1 ved feil |
| `make mcp-val-run` | Startar validator MCP-serveren interaktivt. Nyttig for manuell testing og feilsøking. | JSON-RPC på stdin/stdout |

---

## Prioritert tiltaksliste

| # | Seksjon | Endring | Prioritet |
|---|---|---|---|
| 1 | Container-image-bygging | Erstatt `Image · Bruk` med `Beskriving · Output`; legg til `mcp-begrep-build` | Høg |
| 2 | Validering | Legg til `Output`-kolonna på alle rader | Høg |
| 3 | mcp-linkml-begrep-utkast | Legg til `Output`-kolonna | Høg |
| 4 | mcp-linkml-validator | Legg til `Output`-kolonna; fjern duplikat av `mcp-validate` | Høg |
| 5 | mcp-linkml-modell-utkast | Fyll inn `Output` for rader som manglar | Medium |
| 6 | Oppsett og føresetnadar | Legg til `Output`-kolonna | Låg |
| 7 | Ny modell | Oppdater beskriving til å nemne bronze-policy | Låg |
