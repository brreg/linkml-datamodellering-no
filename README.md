# linkml-w3c-no-profiles

Modellerer norske W3C-applikasjonsprofiler og norske offentlige domenemodeller i [LinkML-format](https://linkml.io/).

**Ny domenemodell?** Sjå [docs/ny-domenemodell.md](docs/ny-domenemodell.md) for steg-for-steg-rettleiing.

## Krav

- [Podman](https://podman.io/) — alle kommandoar køyrer via container-image, ingen lokal installasjon nødvendig

## Typisk arbeidsflyt

```bash
# 1. Generer alle artefaktar for eit domene (t.d. oreg)
make oreg

# 2. Kopier artefaktar til portalen og oppdater navigasjonen
make publish

# 3. Start lokal dev-server
make docs-serve       # → http://localhost:8000
```

Nye skjema under `src/linkml/<domene>/<namn>/<namn>-schema.yaml` vert oppdaga automatisk — ingen Makefile-endring nødvendig.

## Kommandoar

### Artefakt og testar

| Kommando | Beskriving |
|---|---|
| `make test` | Lint alle skjema og valider alle eksempelfiler |
| `make validate` | Valider alle skjema mot LinkML-metaskjemaet |
| `make gen-jsonld` | Generer JSON-LD kontekst (`*-context.jsonld`) for alle skjema |
| `make gen-shacl` | Generer SHACL shapes (`*-shapes.ttl`) for alle skjema |
| `make gen-python` | Generer Python-dataklassar (`*-model.py`) for alle skjema |
| `make gen-jsonschema` | Generer JSON Schema (`*-schema.json`) for alle skjema |
| `make gen-owl` | Generer OWL/Turtle-ontologi (`*-ontology.ttl`) for alle skjema |
| `make gen-rdf` | Generer RDF/Turtle-graf av skjemaet for alle skjema |
| `make gen-erdiagram` | Generer Mermaid ER-diagram (`*-erdiagram.md`) for alle skjema |
| `make docs` | Generer HTML-klassereferanse til `generated/` for alle skjema |
| `make clean` | Slett `generated/` |

### Teste enkeltskjema/eksempel

## Linte enkeltskjema
./tests/validate_schema.bash ./src/linkml/samt/samt-bu/samt-bu-schema.yaml 

## Valider eksempelfil mot skjema direkte: 
./tests/validate_schema.bash ./src/linkml/samt/samt-bu/samt-bu-schema.yaml ./examples/samt/samt-bu-eksempel.yaml

### Domain-spesifikke targets

Kvart domene har eit eige target som køyrer alle generatorar berre for det domenet:

| Kommando | Beskriving |
|---|---|
| `make ap-no` | Valider + generer alle artefaktar for alle AP-NO-profiler |
| `make fair` | Valider + generer alle artefaktar for FAIR-metadata |
| `make ngr` | Valider + generer alle artefaktar for NGR-modellane |
| `make fint` | Valider + generer alle artefaktar for FINT-modellane |
| `make samt` | Valider + generer alle artefaktar for SAMT-modellane |
| `make oreg` | Valider + generer alle artefaktar for OREG-registera |

Nye domene vert oppdaga automatisk frå `src/linkml/` — ingen endringar i Makefile.

### Dokumentasjonsportal

Tre ulike steg — berre `publish` og `docs-serve` trengst for lokal utvikling:

| Kommando | Kva | Når |
|---|---|---|
| `make publish` | Kopier `generated/` → `mkdocs/docs/` og regenerer `mkdocs.yml` | Etter `make <domene>` eller `make docs` |
| `make docs-serve` | Start lokal dev-server på http://localhost:8000 (live reload) | Lokal utvikling |
| `make docs-build` | Bygg statisk HTML-site til `mkdocs/site/` (reint, fullstendig bygg) | Produksjon / deploy |
| `make docs-build-fast` | Same som `docs-build` men med `--dirty` — hoppar over uendra sider | Iterativ utvikling av portal-malar/CSS |

**Korleis publiseringa fungerer:**

`make publish` køyrer `mkdocs/publish.sh` som:

1. Kopier artefaktar frå `generated/<domene>/<skjema>/` til `mkdocs/docs/<domene>/<skjema>/`
2. Kopier gen-doc markdown-sider (`generated/…/docs/*.md`) til `mkdocs/docs/<domene>/<skjema>/klasser/`
3. Genererer `klasser/modell.md` per skjema — ER-diagram (Mermaid) øvst, deretter klassetabell og eigenskapar
4. Genererer ei `index.md` per skjema med artefakttabell og lenke til modell-sida
5. Genererer ei `index.md` per domene med oversikt over alle skjema og tilgjengelege artefaktar
6. Regenererer `mkdocs/mkdocs.yml` med oppdatert navigasjonsstruktur

Nye domene og skjema dukkar opp automatisk i portalen neste gong `make publish` vert køyrt — ingen manuell konfigurasjon.

Artefaktar som ikkje finst vert stillteiande utelate. `Modell`-sida i nav krev at både `make docs` (klasseliste) og `make gen-erdiagram` (diagram) er køyrde for domenet — køyr `make publish` etter begge for å synkronisere.

### Valider (lint) enkeltskjema direkte

```bash
podman run --rm -v "$(pwd):/work" -w /work -e PYTHONWARNINGS=ignore \
  docker.io/linkml/linkml:latest \
  linkml lint --ignore-warnings src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml
```

### MCP-validator

| Kommando | Beskriving |
|---|---|
| `make mcp-build` | Bygg container-bilete for MCP-serveren |
| `make mcp-test` | Køyr unit-testar for MCP-serveren |
| `make mcp-smoke` | Røyk-test med eksempel-JSON-RPC-meldingar |
| `make mcp-run` | Start MCP-serveren interaktivt (stdin/stdout) |
| `make mcp-validate SCHEMA=<sti>` | Valider eit skjema med alle importar flatta ut (standard policy) |
| `make mcp-validate SCHEMA=<sti> POLICY=ap-no-catalog` | Valider at container-klassen inkluderer DCAT-AP-NO og DQV-AP-NO |
| `make mcp-validate SCHEMA=<sti> POLICY=fair` | Valider med FAIR-policy (F1–R1.3) |

MCP-serveren les JSON-RPC-meldingar frå stdin og skriv responsar til stdout. Kvar melding er éi linje.

**Sjølvstendige skjema** (berre `linkml:types`-import) kan sendast direkte som tekst:

```bash
python3 -c "
import json
schema = open('src/linkml/fair/fair-metadata/fair-metadata-schema.yaml').read()
msgs = [
    {'jsonrpc':'2.0','id':1,'method':'initialize','params':{}},
    {'jsonrpc':'2.0','id':2,'method':'tools/call','params':{
        'name':'validate_linkml_schema',
        'arguments':{'schemaText': schema}
    }},
]
print('\n'.join(json.dumps(m) for m in msgs))
" | podman run -i --rm mcp-linkml-validator
```

**Domenemodeller med relative importar** (FINT, AP-NO) vert flatta ut automatisk med `gen-linkml --mergeimports` før validering:

```bash
make mcp-validate SCHEMA=src/linkml/fint/fint-administrasjon/fint-administrasjon-schema.yaml
```

```
→ Flattar ut src/linkml/fint/fint-administrasjon/fint-administrasjon-schema.yaml ...
→ Validerer (policy: default) ...
{
  "valid": true,
  "errorCount": 0,
  "warningCount": 0,
  "issues": []
}
```

**FAIR-validering** — sjekkar om ein domenemodell oppfyller FAIR-prinsippa (F1–R1.3):

```bash
make mcp-validate SCHEMA=src/linkml/fint/fint-administrasjon/fint-administrasjon-schema.yaml POLICY=fair
```

**AP-NO-katalog-validering** — sjekkar at container-klassen inkluderer dei obligatoriske klassane frå DCAT-AP-NO og DQV-AP-NO:

```bash
make mcp-validate SCHEMA=src/linkml/ngr/ngr-adresse/ngr-adresse-schema.yaml POLICY=ap-no-catalog
```

Valideringsresultatet inneheld `valid`, `errorCount`, `warningCount` og ei liste med `issues` (kvar med `severity`, `code`, `target` og `message`). Policy-baserte reglar konfigurerast i `src/mcp-linkml-validator/policies/`:

| Policy | Fil | Beskriving |
|---|---|---|
| `default` | `policies/default.yaml` | Obligatoriske og anbefalte metadata-felt |
| `ap-no-catalog` | `policies/ap-no-catalog.yaml` | Sjekkar at container-klassen har obligatoriske/anbefalte klasser frå DCAT-AP-NO og DQV-AP-NO |
| `fair` | `policies/fair.yaml` | FAIR-sjekkar F1–R1.3 (tittel, class_uri, lisens, proveniens m.m.) |

## Katalogstruktur

```
src/
├── linkml/
│   ├── ap-no/                          # Norske W3C-applikasjonsprofiler
│   │   ├── common/                     # Felles slot-definisjonar (delt av alle AP-NO)
│   │   ├── dcat-ap-no/                 # Datakatalogar og datasett
│   │   ├── dqv-ap-no/                  # Datakvalitet
│   │   ├── cpsv-ap-no/                 # Offentlege tenester
│   │   ├── skos-ap-no/                 # Begrepssamlingar
│   │   └── xkos-ap-no/                 # Utvidet klassifikasjon
│   ├── ngr/                            # Nasjonale grunndata (NGR)
│   │   ├── ngr-adresse/                # Offisiell adresse og geografiske inndelingar
│   │   ├── ngr-eiendom/                # Fast eiendom, matrikkelenhet og bygning
│   │   ├── ngr-person/                 # Person, identifikasjon og familierelasjonar
│   │   └── ngr-virksomhet/             # Verksemder, roller og organisasjonsstruktur
│   ├── fint/                           # FINT-domenemodeller
│   │   ├── fint-common/                # Felles typar og abstrakte klassar
│   │   ├── fint-administrasjon/        # Lønn, arbeidsforhold, organisasjon
│   │   ├── fint-arkiv/                 # Sak, journal, dokument
│   │   ├── fint-okonomi/               # Økonomi og rekneskap
│   │   ├── fint-personvern/            # Personvernmeldingar
│   │   ├── fint-ressurs/               # Ressursar
│   │   └── fint-utdanning/             # Utdanning og skole
│   └── fair/
│       └── fair-metadata/              # FAIR-metadataoverbygning (F/A/I/R-prinsippa)
├── mcp-linkml-validator/               # MCP-server for LinkML-validering
│   ├── server.py                       # JSON-RPC MCP-server
│   ├── policies/
│   │   ├── default.yaml                # Standard validering (required/recommended felt)
│   │   ├── ap-no-catalog.yaml          # Obligatoriske klasser frå DCAT-AP-NO og DQV-AP-NO
│   │   └── fair.yaml                   # FAIR-sjekkar F1–R1.3
│   ├── flatten-and-validate.bash       # Flattar ut importar og validerer via MCP
│   ├── Dockerfile
│   └── requirements.txt
└── templates/
    └── docgen/                         # Jinja2-malar for HTML-dokumentasjon

examples/
├── ap-no/                              # Eksempeldata for AP-NO-profilene
├── ngr/                                # Eksempeldata for NGR-domenemodellane
└── fair/                               # Eksempeldata for FAIR-metadata

tests/
├── fixtures/                           # Testfixturer med Container/tree_root for AP-NO og FAIR
├── ap-no-catalog-bestatt-schema.yaml   # Testskjema: container med alle DCAT/DQV-klasser (skal bestå)
├── ap-no-catalog-manglar-schema.yaml   # Testskjema: container utan obligatoriske klasser (skal feile)
├── test_schemas.sh                     # Lint og valider alle skjema og eksempel
├── test_mcp_server.py                  # Unit-testar for MCP-validator (pytest)
└── test-mcp-linkml-validator.json      # Eksempel-JSON-RPC-meldingar for røyk-test

generated/                              # Genererte artefakter (ikkje innsjekka i git)
```

## Arkitekturprinsipp

### AP-NO Profiler for RDF baserte ressurser

Skjema under `src/linkml/ap-no/` modellerer [norske applikasjonsprofiler](https://data.norge.no/showroom/overview) for RDF baserte ressurser som definert av Digitaliseringsdirektoratet. Disse skjemaene definerer klasser og slot-ar utan `Container`/`tree_root`. Dei er meint å importerast av domenemodeller og er ikkje sjølvstendige. Felles slot-ar som går att i fleire profiler ligg i `common/`.

| Skjema | Profil | Dokumentasjon |
|---|---|---|
| `cpsv-ap-no` | Spesifikasjon for tjeneste- og hendelsesbeskrivelser | [CPSV-AP-NO](https://informasjonsforvaltning.github.io/cpsv-ap-no/) |
| `dcat-ap-no` | Standard for beskrivelse av datasett, datatjenester og datakataloger | [DCAT-AP-NO](https://data.norge.no/specification/dcat-ap-no) |
| `dqv-ap-no` | Spesifikasjon for beskrivelse av kvalitet på datasett | [DQV-AP-NO](https://data.norge.no/specification/dqv-ap-no) |
| `skos-ap-no` | Forvaltningsstandard for begrepsbeskrivelser | [SKOS-AP-NO-Begrep](https://data.norge.no/specification/skos-ap-no-begrep) |
| `xskos-ap-no` | Spesifikasjon for klassifikasjonsbeskrivelser | [XKOS-AP-NO](https://data.norge.no/specification/xkos-ap-no) |

Testfixturer (`tests/fixtures/`) legg til ein `Container`-klasse med `tree_root: true` for kvar profil, slik at eksempeldata kan validerast isolert.

### FAIR-metadata

`src/linkml/fair/fair-metadata/` modellerer gapet mellom AP-NO-profilene og [FAIR-prinsippa](https://www.go-fair.org/fair-principles/) (Findable, Accessible, Interoperable, Reusable). Dei er meint å importerast av domenemodeller og er ikkje sjølvstendige. Skjemaet er eit bibliotek utan `tree_root`; testfixturen (`tests/fixtures/fair-metadata-fixture.yaml`) legg til `Container` for validering.

### NGR – Nasjonale Grunndata

Skjema under `src/linkml/ngr/` modellerer [Nasjonale grunndata](https://informasjonsforvaltning.github.io/nasjonale-grunndata/) — dei autoritative grunnlagsregistra i norsk offentleg sektor:

| Skjema | Register | Beskriving |
|---|---|---|
| `ngr-adresse` | Matrikkelen | Offisiell adresse, vegnamn, husnummer og geografiske inndelingar |
| `ngr-eiendom` | Matrikkelen / Grunnboka | Fast eiendom, matrikkelenhet (6 undertypar), bygning, eierforhold og hjemmel |
| `ngr-person` | Folkeregisteret / KRR | Person, identifikasjon, familierelasjonar, adresser og kontaktopplysningar |
| `ngr-virksomhet` | Enhetsregisteret | Verksemder (underleining/hovudeining), roller, næringskode og adresser |

Alle NGR-skjema er sjølvstendige med eigen `tree_root`-klasse og importerer berre `linkml:types`. Klasser frå andre domene (t.d. `OffisiellAdresse` i ngr-eiendom, `Person` i ngr-virksomhet) er modellerte som stub-klasser med berre `id`.

### OREG - domenemodeller
Skjema under `src/linkml/oreg/` modellerer offentlige registre.

### FINT – Felles Fylkeskommunale INTegrasjoner

Skjema under `src/linkml/fint/` modellerer [FINT-informasjonsmodellen](https://informasjonsmodell.felleskomponent.no/docs?v=v4.0.20) for integrasjon i norsk fylkeskommune sektor. Alle FINT-skjema importerer `fint-common` for felles abstrakte klassar og typar (`Aktoer`, `Enhet`, `Begrep`, `Identifikator` m.fl.) og er sjølvstendige med eigen `tree_root`-klasse.

### SAMT - Sammenhengende tjenester
Skjema under `src/linkml/samt/` modellerer [SAMT-informasjonsmodellen](https://docs.samt-bu.no/om/om-samt-bu/) for integrasjon i norsk kommune sektor.

### MCP-linkml-validator

`src/mcp-linkml-validator/` er ein [MCP-server](https://modelcontextprotocol.io/) som eksponerer LinkML-validering som eit verktøy (`validate_linkml_schema`). Serveren køyrer standard LinkML-linting og policy-baserte tilleggsreglar konfigurerbare via `policy.yaml`.

For skjema med relative importar brukar `make mcp-validate` scriptet `flatten-and-validate.bash`, som fyrst flattar ut alle importar med `gen-linkml --mergeimports` i linkml-containeren (som har tilgang til heile repoet), og deretter sender det flattened skjemaet til MCP-serveren.

Policyane støttar tre sjekktypear:

| Sjekk | Nøkkel | Beskriving |
|---|---|---|
| Metadata-felt | `required` / `recommended` | Obligatoriske og anbefalte felt på schema/class/slot |
| Fellesklasser | `common_classes.must_use` | Klasser som må finnast i skjemaet (inkl. importar) |
| Container-klasser | `container_classes.must_include` / `should_include` | Klasser som tree_root-klassen må/bør ha som `range` på attributtar |
