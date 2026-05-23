# Generatorkonfigurasjon (generate.yaml)

## Kva er `generate.yaml`?

Kvar modell under `src/linkml/<domene>/<modell>/` kan ha ei `generate.yaml` som styrer
kva artefaktar som vert genererte og med kva flagg. Ein modell utan fila brukar
standardkonfigurasjonen: alle generatorar skrudde på, ingen ekstra flagg.

`make new-model` oppretter fila automatisk med standardkonfigen.

## Plassering

```
src/linkml/<domene>/<modell>/generate.yaml
```

## Felt

Dei boolske felta svarar 1:1 til `generate.yaml`-kolonnen i
[tabellen over genererte artefakter](https://github.com/brreg/linkml-datamodellering-no#genererte-artefakter)
i README. Alle har standardverdi `true`.

I tillegg kjem to flagg-felt for generatorar som treng ekstra parametrar:

| Felt | Type | Standard | Skildring |
|---|---|---|---|
| `shacl_flags` | streng | `""` | Ekstra flagg til `gen-shacl`, t.d. `"--exclude-imports"` |
| `owl_flags` | streng | `""` | Ekstra flagg til `gen-owl`, t.d. `"--log_level ERROR"` |

## Eksempel

**Standardkonfig** (NGR, OREG — alle generatorar på, ingen flagg):

```yaml
generators:
  jsonld_context: true
  shacl: true
  shacl_flags: ""
  python: true
  json_schema: true
  owl: true
  owl_flags: ""
  rdf: true
  protobuf: true
  erdiagram: true
  docs: true
  plantuml: true
  example_rdf: true
```

**FINT** (`rdf: false` pga. HTTP-feil ved JSON-LD-kontekstoppslag; SHACL- og OWL-flagg
for å handtere kryss-skjema klassearv; `example_rdf: false` der eksempelfila nyttar
FINT-stile CURIEs som ikkje er gyldige URI-ar):

```yaml
generators:
  jsonld_context: true
  shacl: true
  shacl_flags: "--exclude-imports"
  python: true
  json_schema: true
  owl: true
  owl_flags: "--log_level ERROR"
  rdf: false
  protobuf: true
  erdiagram: true
  docs: true
  plantuml: true
  example_rdf: false
```

**AP-NO / FAIR** (`example_rdf: false` — desse skjemaa har ingen `tree_root` og kan
ikkje konverterast til RDF av `linkml-convert`):

```yaml
generators:
  jsonld_context: true
  shacl: true
  shacl_flags: ""
  python: true
  json_schema: true
  owl: true
  owl_flags: ""
  rdf: true
  protobuf: true
  erdiagram: true
  docs: true
  plantuml: true
  example_rdf: false
```

## Korleis det fungerer

`gen-config.sh` les alle `generate.yaml`-filer og skriv `config.mk` — eit
Makefile-fragment med per-modell-variablar som Makefile-en inkluderer automatisk.
`config.mk` vert automatisk regenerert når ei `generate.yaml`-fil endrar seg. Du
kan òg regenerere manuelt:

```bash
make config.mk
```

`config.mk` er generert og skal ikkje redigerast for hand.

## Nye modellar

`make new-model NAME=... DOMAIN=...` oppretter ei standard `generate.yaml` saman med
skjemafila. Juster henne etterpå viss domenet krev det — til dømes for FINT-modellar
der `rdf` og `example_rdf` skal vera `false`.
