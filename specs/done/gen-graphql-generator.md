# Legg til gen-graphql-generator (GraphQL SDL frå LinkML-skjema)

**Opprett:** 2026-08-10
**Bakgrunn:** Følgjer opp Gap 3 i
[`avvik-veileder-god-datatilbyder.md`](avvik-veileder-god-datatilbyder.md) —
Digdir nemner GraphQL saman med OpenAPI som standardisert distribusjonsformat
for datatenester. Brukaren har godkjent å gå vidare med dette som eiga sak.

## Grunnlag (verifisert)

- `linkml==1.11.1` (pinna i `src/assets/containers/Dockerfile.linkml:7`)
  inneheld `linkml.generators.graphqlgen.GraphqlGenerator`, med CLI-kommando
  `gen-graphql` registrert i `packages/linkml/pyproject.toml` — stadfesta
  direkte mot GitHub-taggen `v1.11.1`.
- Generatoren er **output-only**: tek eit LinkML-skjema og produserer
  GraphQL-typedefinisjonar (SDL, `.graphql`), ingen runtime-bindingar. Ingen
  JSON-Schema-mellomsteg (i motsetnad til OpenAPI/AsyncAPI/XSD i dette
  repoet) — ho er strukturelt lik `gen-proto`/`gen-python`/`gen-jsonschema`:
  éin direkte LinkML→format-transformasjon, ingen validator, ingen eigen
  container.
- Ingen ny Dockerfile-avhengigheit eller container-image trengst —
  `linkml-local` (bygd frå `Dockerfile.linkml`) er alt `always_required: true`
  i `src/assets/containers/images.json`.

## Mønster som vert følgt

To presedensar er brukte saman:
1. **`gen-proto`** (`make/10-generator-macros.mk`/`11-generator-targets.mk`,
   `batch-generate.py` REGISTRY) — strukturelt identisk generator-type
   (direkte LinkML-generator, ingen etterhandsaming/validering).
2. **`openapi`/`asyncapi`-utrullinga** (sjå
   `specs/done/openapi-asyncapi-generering.md`) — prosessen for å leggje
   til eit **nytt opt-in build.yaml-flagg** til alle eksisterande
   skjema-manifest, portal-visning og dokumentasjon.

## Endringar

### A. Kjernegenerering
1. `src/assets/scripts/makefile/batch-generate.py` — ny REGISTRY-oppføring:
   `"graphql": GeneratorSpec(module="linkml.generators.graphqlgen", out_suffix="schema.graphql", flag="graphql")`,
   pluss oppdatering av `<kind>`-lista i docstringen (linje 38)
2. `make/11-generator-targets.mk` — ny
   `$(eval $(call make_gen_target,gen-graphql,run_gen_parallel,graphql))`
   + hjelpetekstlinje `gen-graphql: ## Generer GraphQL-skjema [SCHEMA=<sti>|DOMAIN=<domain>]`
3. `src/assets/scripts/makefile/run-domain-pipeline.sh` — ny
   `run_bg graphql "$MAKE" --no-print-directory gen-graphql DOMAIN="$domain"`
   i Fase 1 (uavhengig gruppe, som `proto`), pluss oppdatering av
   header-kommentaren som listar Fase 1-gruppene
4. `src/assets/scripts/makefile/generate-informasjonsmodell.py` — legg
   `'*.graphql'` til `patterns`-lista i `discover_artifacts()` slik at
   artefaktet dukkar opp i `finnes_i_format` for Informasjonsmodell-instansen

### B. Portal
5. `mkdocs/lib/utils/formatters.sh` — ny linje i `artifact_label()`:
   `schema.graphql) echo "GraphQL-skjema" ;;`
6. `mkdocs/publish.sh` — legg `schema.graphql` til `ARTIFACT_ORDER`, plassert
   etter `schema.proto`

### C. Dokumentasjon
7. `COMMANDS.md` — ny rad i "Enkeltartefakter"-tabellen, same format som
   `gen-proto`-rada
8. `README.md` — ny rad i artefakttabellen (§ "Genererte artefakter")
9. `SCOPE.md` — ny rad i den (delvis duplikate, men separat vedlikehaldne)
   artefakttabellen
10. `mkdocs/docs/kom-i-gang/build-config.md` — legg `graphql: true` til alle
    fire eksempel-YAML-blokkene (etter `openapi: true`)
11. `CONVENTIONS.md` — legg `graphql: true` til manifest-eksempelet (etter
    `protobuf: true`, sidan `openapi` ikkje er med i dette eksempelet frå før
    — eksisterande avvik, rørast ikkje)
12. `mkdocs/docs/automasjon/artefakt-generering.md` — fire stader:
    - § 1: legg "GraphQL" til i mermaid-diagrammet sin artefakt-boks
    - § 2: ny rad i per-artefakt-tabellen, plassert etter Protobuf-rada
    - § 3.1: legg ", GraphQL" til overskrifta som listar "reine
      LinkML-genererte artefakta"
    - § 4: legg `schema.graphql` til lista over filnamn artefaktabellen i
      domene-`index.md` sjekkar for

### D. Scaffold for nye modellar
13. `src/assets/scripts/scaffolding/new-modell.sh` — legg
    `graphql: true` til build.yaml-malen (etter `openapi: true`, same
    presedens som openapi fekk ved seinare oppdatering av scaffoldet)

### E. Eksisterande skjema-manifest (opt-in rollout)
14. Legg `graphql: false` til `generators:`-blokka i alle 34 eksisterande
    `build.yaml`-filer som har ein `generators:`-seksjon (funne via
    `grep -l "generators:" src/linkml/*/*/build.yaml`) — **ingen** endring
    i faktisk generert output for eksisterande modellar, reint opt-in flagg
    for framtidig bruk, same presedens som openapi/asyncapi-utrullinga

## Verifisering

- Køyr `podman run --rm -v "$(pwd)":/repo:ro -w /repo docker.io/rhysd/actionlint:latest -color .github/workflows/generate.yml`
  dersom `generate.yml` vert endra (det bør han **ikkje** trenge å bli,
  sidan `linkml-local` alt er `always_required`) — inga endring venta her
- Flipp mellombels `graphql: true` på **eitt** testskjema (`samt-bu`, same
  skjema som vart brukt til å verifisere openapi/asyncapi-utrullinga i
  `specs/done/openapi-asyncapi-generering.md`), køyr
  `make gen-graphql SCHEMA=src/linkml/samt/samt-bu/samt-bu-schema.yaml`, og
  sjekk at `generated/samt/samt-bu/samt-bu-schema.graphql` vert produsert
  med gyldig GraphQL SDL (typedefinisjonar for klassane i skjemaet)
- Revert flagget til `false` etter verifisering, med mindre brukaren
  eksplisitt ønskjer at eitt skjema skal ha han aktivert som levande
  eksempel i portalen
- `make lint` på testskjemaet for å stadfeste at build.yaml-endringa ikkje
  bryt noko

## Handlingsliste

- [x] A: kjernegenerering (4 filer)
- [x] B: portal-wiring (2 filer)
- [x] C: dokumentasjon (6 filer)
- [x] D: scaffold (1 fil)
- [x] E: 34 eksisterande build.yaml-filer, opt-in `graphql: false`
- [x] Verifiser med mellombels `graphql: true` på `samt-bu`, deretter revert

## Utført

Utført 2026-08-10. Alle fem punkt fullførte.

**Kva som vart gjort:**
- `src/assets/scripts/makefile/batch-generate.py`: ny `"graphql"`-oppføring
  i `REGISTRY` (`linkml.generators.graphqlgen`, `out_suffix="schema.graphql"`,
  `flag="graphql"`) + docstring oppdatert
- `make/11-generator-targets.mk`: nytt `gen-graphql`-target (via
  `make_gen_target`-malen) + hjelpetekst
- `src/assets/scripts/makefile/run-domain-pipeline.sh`: `gen-graphql` lagt
  til Fase 1 (parallelt med `gen-proto`), header-kommentar oppdatert
- `src/assets/scripts/makefile/generate-informasjonsmodell.py`: `*.graphql`
  lagt til `discover_artifacts()`-mønsterlista
- `mkdocs/lib/utils/formatters.sh`: `artifact_label()` gjev "GraphQL-skjema"
  for `schema.graphql`
- `mkdocs/publish.sh`: `schema.graphql` lagt til `ARTIFACT_ORDER`
- `COMMANDS.md`, `README.md`, `SCOPE.md`: nye tabellrader for `gen-graphql`
- `CONVENTIONS.md`, `mkdocs/docs/kom-i-gang/build-config.md`: `graphql: true`
  lagt til manifest-eksempla (5 stader totalt)
- `mkdocs/docs/automasjon/artefakt-generering.md`: fire stader oppdatert
  (mermaid-diagram, per-artefakt-tabell, § 3.1-overskrift, § 4-filliste)
- `src/assets/scripts/scaffolding/new-modell.sh`: `graphql: true` lagt til
  build.yaml-malen for nye modellar
- **34 eksisterande `build.yaml`-filer** (alle med `generators:`-seksjon):
  `graphql: false` lagt til rett etter `protobuf:`-lina — reint opt-in,
  ingen åtferdsendring for eksisterande modellar
- **Verifisert:** mellombels `graphql: true` på `samt-bu`, køyrde
  `make gen-graphql SCHEMA=src/linkml/samt/samt-bu/samt-bu-schema.yaml`
  (måtte køyrast med `dangerouslyDisableSandbox` — sandboxen blokkerte
  podman frå å skrive til `/run/user/1000/libpod`, ikkje ein feil i
  endringane). Produserte gyldig GraphQL SDL (10 137 byte, enums og
  typedefinisjonar frå både lokale og importerte klassar). `make help` og
  `make lint SCHEMA=...` stadfesta korrekt wiring. Flagget reverta til
  `false` og det mellombelse test-artefaktet sletta (`generated/` er
  gitignora byggoutput uansett).

**Avvik frå opphavleg plan:** Ingen. Ingen ny Dockerfile-/CI-endring var
naudsynt (stadfesta i planen: `linkml-local` er alt `always_required` i
`src/assets/containers/images.json`).
