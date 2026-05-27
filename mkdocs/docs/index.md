# linkml-datamodellering-no

Norske W3C-applikasjonsprofiler og offentlege domenemodeller i [LinkML-format](https://linkml.io/).

> LinkML er eit open kjeldekode-modelleringsspråk der du skriv skjema i YAML som skildrar datastrukturen din, og som du kan nytte til å generere skjema, data, diagram og dokumentasjon i andre format ([LinkML generators](https://linkml.io/linkml/generators/index.html)). Generatorane konverterer både til tradisjonelle format (JSON Schema, Python, Protobuf) og W3C-semantiske format (RDF/Turtle, OWL, SHACL, JSON-LD) utan behov for ekstra mapping.

Dette [kodelageret](https://github.com/brreg/linkml-datamodellering-no) inneheld:

* LinkML-modellar for norske W3C-applikasjonsprofiler og offentlege domenemodeller for gjenbruk.
* mcp-linkml-modell-utkast, mcp-linkml-begrep-utkast og mcp-linkml-validator [mcp servere](https://modelcontextprotocol.io/docs/getting-started/intro) for å generere og validere LinkML-skjema (med moglegheit for KI-integrasjon).
* LinkML-generatorar for å produsere artefakter i andre format frå LinkML-skjema.
* Github Actions (pipelines) for å automatisk generere, validere og publisere artefakter frå LinkML-skjema.
* Github Pages dokumentasjonsportal med oversikt over alle LinkML-skjema og genererte artefakter.



## Kom i gang

**Føresetnader:** [Podman](https://podman.io/) (rootless), WSL2 og GNU make.

```bash
# Sjekk at alt er på plass
make check-prereqs
```
```bash
# Bygg container-images (éin gong)
make linkml-build-docker && make python-build-docker && make mcp-val-build && make mcp-mod-build && make mcp-begrep-build
```

### Datamodellering

> Bytt ut **`domene`** og **`modellnavn`** med dine aktuelle navn.

```bash
# 1. Lag eit nytt tomt LinkML-skjema (skjema + filstruktur)
make new-model NAME=modellnavn DOMAIN=domene

# 1b. (om ønskjeleg) Generer frå eksisterande JSON Schema
# Legg JSON Schema-filen i tmp/, t.d. tmp/modellnavn.json
make mcp-generate SCHEMA=tmp/modellnavn.json
# → genererer tmp/modellnavn-schema.yaml. Flytt ho til src/linkml/domene/modellnavn/
```
```bash
# 2. Rediger modellfila etter behov
#    → src/linkml/domene/modellnavn/modellnavn-schema.yaml
```
```bash
# 3. Valider skjema
make mcp-validate \
  SCHEMA=src/linkml/domene/modellnavn/modellnavn-schema.yaml \
  POLICY=felles-datakatalog
```
```bash
# 4. Generer artefakter og publiser til dokumentasjonsportal
make domene && make publish && make docs-serve   # → http://localhost:8000
```

Nye skjema under `src/linkml/<domene>/<modellnavn>/` vert oppdaga automatisk.

For full rettleiing: sjå [Ny domenemodell](https://brreg.github.io/linkml-datamodellering-no/ny-domenemodell/) og [Publiser til Felles Datakatalog](https://brreg.github.io/linkml-datamodellering-no/publisering-modell/).

### Begrepsmodellering

> Bytt ut **`katalognavn`** med ditt aktuelle navn.

```bash
# 1. Opprett ny begrepskatalog (skjema + filstruktur)
make new-model NAME=katalognavn DOMAIN=begrepskatalog
```
```bash
# 2. Rediger datafila med reelle begrep
#    → src/linkml/begrepskatalog/katalognavn/data/katalognavn/katalognavn.yaml
```
```bash
# 3. Valider skjema og datafil
make mcp-validate \
  SCHEMA=src/linkml/begrepskatalog/katalognavn/katalognavn-schema.yaml \
  POLICY=felles-begrepskatalog \
  INSTANCE=src/linkml/begrepskatalog/katalognavn/data/katalognavn/katalognavn.yaml
```
```bash
# 4. Generer og publiser til dokumentasjonsportal
make begrepskatalog && make publish && make docs-serve   # → http://localhost:8000
```

For full rettleiing: sjå [Ny begrepskatalog](https://brreg.github.io/linkml-datamodellering-no/ny-begrepsmodell/) og [Publiser til Felles Begrepskatalog](https://brreg.github.io/linkml-datamodellering-no/publisering-begrep/).


## Bruk frå eksternt repo

Vil du bruke AP-NO-profilene i ditt eige repo utan å jobbe inni dette monorepoet?
Bootstrap-scriptet legg til dei to filene du treng på eitt minutt:

```bash
curl -sSL https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/main/scripts/bootstrap.sh | bash
```

Importer deretter AP-NO-profilene direkte i skjemaet ditt via GitHub Raw-URL:

```yaml
imports:
  - linkml:types
  - https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/v1.0.0/src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema
```

Validering og generering skjer via reusable GitHub Actions-workflows i dette repoet — ingen lokal installasjon er nødvendig. Sjå [Bruk frå eksternt repo](https://brreg.github.io/linkml-datamodellering-no/ekstern-bruk/) for full rettleiing.

## Domener

| Domene | Skildring | Dokumentasjon |
|---|---|---|
| modellkatalog | Modellkatalog for Brønnøysundregistra sine informasjonsmodellar i ModelDCAT-AP-NO-format. Publisert til Felles Datakatalog. | [ModelDCAT-AP-NO](https://data.norge.no/specification/modelldcat-ap-no)
| fair | FAIR-metadataoverbygning — **F**indable, **A**ccessible, **I**nteroperable, **R**eusable. Kan importerast av alle domenemodeller. | [FAIR principles](https://www.go-fair.org/fair-principles/)
| ap-no | Norske W3C-applikasjonsprofiler — DCAT, SKOS, CPSV, DQV m.fl. Importerast av domenemodeller. | [RDF-baserte maskinlesbare ressurser](https://data.norge.no/showroom/overview)
| begrepskatalog | Begrepskatalogmodellar etter SKOS-AP-NO-Begrep. Produksjonsdatafiler vert automatisk konverterte til SKOS/RDF og publiserte til Felles Begrepskatalog via GitHub Pages-høstingsendepunkt. | [SKOS-AP-NO-Begrep](https://data.norge.no/specification/skos-ap-no-begrep)
| ngr | Nasjonale grunndata — adresse, eigedom, person og verksemd. | [Nasjonale grunndata](https://informasjonsforvaltning.github.io/nasjonale-grunndata/#OmNasjonaleGrunndata)
| oreg | Offentlege register. |
| fint | FINT felleskomponent — integrasjonsmodellar for fylkeskommunal sektor. | [FINT informasjonsmodell](https://informasjonsmodell.felleskomponent.no/docs?v=v4.0.20)
| samt | SAMT — integrasjonsmodellar for kommunesektoren. | [SAMT-prosjektet](https://docs.samt-bu.no/om/)

## Skjema

Skjema ligg under `src/linkml/<domene>/<skjema>/`

| Domene | Skjema | Skildring | Dokumentasjon
|---|---|---|---|
| begrepskatalog | brreg-begrepskatalog | Registerenheten i Brønnøysund – Begrepskatalog | [SKOS-AP-NO-Begrep](https://data.norge.no/specification/skos-ap-no-begrep)
| ap-no | common-ap-no | Felles slot-definisjonar for alle AP-NO-profilar |
| ap-no | cpsv-ap-no | Offentlege tenester og hendingar | [data.norge.no/specification/cpsv-ap-no](https://data.norge.no/specification/cpsv-ap-no)
| ap-no | dcat-ap-no | Datakatalogar og datasett | [data.norge.no/specification/dcat-ap-no](https://data.norge.no/specification/dcat-ap-no)
| ap-no | dqv-ap-no | Datakvalitet | [data.norge.no/specification/dqv-ap-no](https://data.norge.no/specification/dqv-ap-no)
| ap-no | modelldcat-ap-no | Informasjonsmodellar | [data.norge.no/specification/modelldcat-ap-no](https://data.norge.no/specification/modelldcat-ap-no)
| ap-no | skos-ap-no | Omgrepsamlingar | [data.norge.no/specification/skos-ap-no-begrep](https://data.norge.no/specification/skos-ap-no-begrep)
| ap-no | xkos-ap-no | Utvida klassifikasjon | [data.norge.no/specification/xkos-ap-no](https://data.norge.no/specification/xkos-ap-no)
| fair | fair-metadata | FAIR-metadataoverbygning (F/A/I/R-prinsippa) | [www.go-fair.org/fair-principles/](https://www.go-fair.org/fair-principles/)
| fint | fint-common | Felles klassar for FINT |
| fint | fint-administrasjon | Lønn, arbeidsforhold, organisasjon | [informasjonsmodell.felleskomponent.no/docs/package_administrasjon?v=v4.0.20](https://informasjonsmodell.felleskomponent.no/docs/package_administrasjon?v=v4.0.20)
| fint | fint-arkiv | Sak, journal, dokument | [informasjonsmodell.felleskomponent.no/docs/package_arkiv?v=v4.0.20](https://informasjonsmodell.felleskomponent.no/docs/package_arkiv?v=v4.0.20)
| fint | fint-okonomi | Økonomi og rekneskap | [informasjonsmodell.felleskomponent.no/docs/package_okonomi?v=v4.0.20](https://informasjonsmodell.felleskomponent.no/docs/package_okonomi?v=v4.0.20)
| fint | fint-personvern | Personvernmeldingar | [informasjonsmodell.felleskomponent.no/docs/package_personvern?v=v4.0.20](https://informasjonsmodell.felleskomponent.no/docs/package_personvern?v=v4.0.20)
| fint | fint-ressurs | Ressursar | [informasjonsmodell.felleskomponent.no/docs/package_ressurs?v=v4.0.20](https://informasjonsmodell.felleskomponent.no/docs/package_ressurs?v=v4.0.20)
| fint | fint-utdanning | Utdanning og skule | [informasjonsmodell.felleskomponent.no/docs/package_utdanning?v=v4.0.20](https://informasjonsmodell.felleskomponent.no/docs/package_utdanning?v=v4.0.20)
| ngr | ngr-adresse | Adresse | [informasjonsforvaltning.github.io/nasjonale-grunndata/#Adresse](https://informasjonsforvaltning.github.io/nasjonale-grunndata/#Adresse)
| ngr | ngr-eiendom | Fast eigedom, matrikkeleining og bygning | [informasjonsforvaltning.github.io/nasjonale-grunndata/#Temaomr%C3%A5deEiendom](https://informasjonsforvaltning.github.io/nasjonale-grunndata/#Temaomr%C3%A5deEiendom)
| ngr | ngr-person | Person, identifikasjon og familierelasjonar | [informasjonsforvaltning.github.io/nasjonale-grunndata/#Person](https://informasjonsforvaltning.github.io/nasjonale-grunndata/#Person)
| ngr | ngr-virksomhet | Verksemder, roller og organisasjonsstruktur | [informasjonsforvaltning.github.io/nasjonale-grunndata/#Virksomhet](https://informasjonsforvaltning.github.io/nasjonale-grunndata/#Virksomhet)
| oreg | register-over-aksjeeiere | Aksjeeigarar og eigedelar |
| samt | samt-bu | Skular og barnehagar | [docs.samt-bu.no/om/](https://docs.samt-bu.no/om/)

**AP-NO-profilane** og **FAIR-metadata** er skjema utan `tree_root` — dei er ikkje sjølvstendige, men meinte å importerast av domenemodeller.

## Genererte artefakter

Køyr `make <domene>` for å generere alle artefakter for eit domene. Kvar generator produserer éin fil under `generated/<domene>/<skjema>/`. Kvar modell kan slå av einskilde generatorar via `manifest.yaml` — sjå [Generatorkonfigurasjon](https://brreg.github.io/linkml-datamodellering-no/manifest-config/) for detaljar.

| Artefakt | Fil | Brukstilfelle | W3C semantisk | manifest.yaml flag |
|---|---|---|---|---|
| JSON-LD kontekst | `<skjema>-context.jsonld` | Mapping frå JSON til RDF — brukast saman med API-ar | ✓ | `jsonld_context` |
| SHACL shapes | `<skjema>-shapes.ttl` | Validering av RDF-data mot skjema i triple stores | ✓ | `shacl` |
| OWL ontologi | `<skjema>-ontology.ttl` | Maskinlesbar ontologi for semantiske verktøy | ✓ | `owl` |
| RDF/Turtle skjema | `<skjema>-schema.ttl` | Fullstendig RDF-representasjon av skjemaet | ✓ | `rdf` |
| Eksempel-RDF | `<skjema>-eksempel.ttl` | Konkret RDF-instans for testing og dokumentasjon | ✓ | `example_rdf` |
| Python-klassar | `<skjema>-model.py` | Direkte bruk i Python-applikasjonar via LinkML | — | `python` |
| JSON Schema | `<skjema>-schema.json` | Validering av JSON-data i applikasjonar | — | `json_schema` |
| Protobuf-skjema | `<skjema>-schema.proto` | gRPC og Protocol Buffers-integrasjon | — | `protobuf` |
| ER-diagram | `<skjema>-erdiagram.md` | Visuell oversikt over klasser og relasjonar (Mermaid) | — | `erdiagram` |
| HTML-dokumentasjon | `docs/` | Menneskelesleg referansedokumentasjon | — | `docs` |
| PlantUML-diagram | `diagrams/<skjema>.puml` + `.svg` | Klassediagram for presentasjon og dokumentasjon | — | `plantuml` |


## Katalogstruktur

```
linkml-datamodellering-no/
├── src/
│   ├── assets/                    # Containere, skript og malar
│   ├── linkml/
│   │   └── <domene>/
│   │       └── <modell>/
│   │           ├── <modell>-schema.yaml
│   │           ├── manifest.yaml           # Generator- og publiseringskonfig
│   │           ├── published-uris.lock     # Berre for publiserte katalogar
│   │           ├── examples/
│   │           │   └── <modell>-eksempel.yaml
│   │           └── data/                   # Berre for publiserte katalogar
│   │               └── <datafil-katalog>/
│   │                   ├── <datafil-katalog>.yaml
│   │                   └── manifest.yaml   # Datafil-manifest
│   ├── mcp-linkml-validator/      # MCP-server: policy-basert validering
│   ├── mcp-linkml-modell-utkast/  # MCP-server: JSON Schema → LinkML-utkast
│   ├── mcp-linkml-begrep-utkast/  # MCP-server: generering av begrepsinstansar
│   └── templates/                 # Jinja2-malar for make gen-docs
│
├── scripts/    # Bootstrap og hjelpeskript for eksterne repo
├── tests/      # Testar og fixtures
├── generated/  # Genererte artefakter (ikkje sjekka inn i git)
├── mkdocs/     # Dokumentasjonsportal (MkDocs Material)
└── tmp/        # Mellombelse filer, t.d. JSON Schema-filer til mcp-linkml-modell-utkast
```
