# linkml-datamodellering-no

!!! warning "Proof of Concept"

    Dette repoet er ein **Proof of Concept** for LinkML-basert datamodellering i norsk offentleg sektor.
    
    **Kva det betyr:**
    
    - Modellar og verktøy er under utvikling og kan endre seg
    - Dokumentasjonen kan vere ufullstendig eller utdatert
    - Nokre funksjonar er berre delvis implementerte
    - Det finst [kjende avgrensingar og bugs](#kjende-avgrensingar)
    - Ingen garantert stabilitet eller support-SLA
    
    **For eksterne organisasjonar:** Les [GOVERNANCE.md](#for-bidragsytarar) for forventningar til stabilitet og ansvar.

!!! note "Målsetting"

    Dette repoet har som mål å realisere dei delane av [Rammeverk for informasjonsforvaltning](https://www.digdir.no/informasjonsforvaltning/rammeverk-informasjonsforvaltning/3626) som går på begrepsmodellering, informasjonsmodellering, metadata og publisering til felles begrepskatalog og datakatalog. Det er tenkt som eit felles repo for nasjonale begreps- og datamodeller inkludert felles verktøy. Både modeller og verktøy kan benyttes lokalt i andre git-repoer. 



> [LinkML](https://linkml.io/) er eit open kjeldekode-modelleringsspråk der du skriv skjema i YAML som skildrar datastrukturen din, og som du kan nytte til å generere skjema, data, diagram og dokumentasjon i andre format ([LinkML generators](https://linkml.io/linkml/generators/index.html)). Generatorane konverterer både til tradisjonelle format (JSON Schema, Python, Protobuf) og W3C-semantiske format (RDF/Turtle, OWL, SHACL, JSON-LD) utan behov for ekstra mapping.

Dette [kodelageret](https://github.com/brreg/linkml-datamodellering-no) inneheld:

* LinkML-[modellar](https://github.com/brreg/linkml-datamodellering-no/tree/main#skjema) for norske W3C-applikasjonsprofiler og offentlege domenemodeller for gjenbruk.
* [mcp-linkml-modell-utkast](https://github.com/brreg/linkml-datamodellering-no/blob/main/src/mcp-linkml-modell-utkast/README.md), [mcp-linkml-begrep-utkast](https://github.com/brreg/linkml-datamodellering-no/blob/main/src/mcp-linkml-begrep-utkast/README.md) og [mcp-linkml-validator](https://github.com/brreg/linkml-datamodellering-no/blob/main/src/mcp-linkml-validator/README.md) ([mcp servere](https://modelcontextprotocol.io/docs/getting-started/intro)) for å generere og validere LinkML-skjema (med moglegheit for KI-integrasjon).
* LinkML-[generatorar](https://github.com/brreg/linkml-datamodellering-no/blob/main/README.md#genererte-artefakter) for å produsere artefakter i andre format frå LinkML-skjema.
* Github Actions [pipelines](https://github.com/brreg/linkml-datamodellering-no/actions) for å automatisk generere, validere og publisere artefakter frå LinkML-skjema.
* Guide for å publisere begreper til [felles begrepskatalog](https://brreg.github.io/linkml-datamodellering-no/publisering-begrep/)
* Guide for å publisere informasjonsmodeller til [felles datakatalog](https://brreg.github.io/linkml-datamodellering-no/publisering-modell/)
* Github Pages [dokumentasjonsportal](https://brreg.github.io/linkml-datamodellering-no/) med oversikt over alle LinkML-skjema og genererte artefakter.
* Opplegg for å [bootstrappe](https://brreg.github.io/linkml-datamodellering-no/ekstern-bruk/) eit eksternt repo for lokal LinkML modellering.


## Kom i gang

**Føresetnader:** linux eller windows med  WSL2, [Podman](https://podman.io/) (rootless) og GNU make.

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
make mcp-linkml-modell-utkast SCHEMA=tmp/modellnavn.json
# → genererer tmp/modellnavn-schema.yaml. Flytt ho til src/linkml/domain/modellnavn/
```
```bash
# 2. Rediger modellfila etter behov
#    → src/linkml/domain/modellnavn/modellnavn-schema.yaml
```
```bash
# 3. Valider skjema
make mcp-linkml-validate \
  SCHEMA=src/linkml/domene/modellnavn/modellnavn-schema.yaml \
  POLICY=felles-datakatalog
```
```bash
# 4. Generer artefakter og publiser til dokumentasjonsportal
make <domain> && make docs-publish && make docs-serve   # → http://localhost:8000
```

Nye skjema under `src/linkml/<domain>/<modellnavn>/` vert oppdaga automatisk.

For full rettleiing: sjå [Ny domenemodell](https://brreg.github.io/linkml-datamodellering-no/ny-domenemodell/) og [Publiser til Felles Datakatalog](https://brreg.github.io/linkml-datamodellering-no/publisering-modell/).

### Begrepsmodellering

> Bytt ut **`katalognavn`** med ditt aktuelle navn.

```bash
# 1. Opprett ny begrepskatalog (skjema + filstruktur)
make new-begrepskatalog NAME=katalognavn
```
```bash
# 1b. (om ønskjeleg) Generer utkast til begrep
# Legg argumenta i tmp/mitt-begrep.json (sjå ny-begrepsmodell.md for format)
make mcp-linkml-begrep-utkast INPUT=tmp/mitt-begrep.json
# → lim YAML-output inn i examples/katalognavn-eksempel.yaml
```
```bash
# 2. Rediger datafila med reelle begrep
#    → src/linkml/begrepskatalog/katalognavn/data/katalognavn/katalognavn.yaml
```
```bash
# 3. Valider skjema og datafil
make mcp-linkml-validate \
  SCHEMA=src/linkml/begrepskatalog/katalognavn/katalognavn-schema.yaml \
  POLICY=felles-begrepskatalog \
  INSTANCE=src/linkml/begrepskatalog/katalognavn/data/katalognavn/katalognavn.yaml
```
```bash
# 4. Generer og publiser til dokumentasjonsportal
make begrepskatalog && make docs-publish && make docs-serve   # → http://localhost:8000
```

For full rettleiing: sjå [Ny begrepskatalog](https://brreg.github.io/linkml-datamodellering-no/ny-begrepsmodell/) og [Publiser til Felles Begrepskatalog](https://brreg.github.io/linkml-datamodellering-no/publisering-begrep/).

Sjå [CLAUDE.md](CLAUDE.md) for modelleringsprinsipp og [COMMANDS.md](COMMANDS.md) for alle tilgjengelege kommandoar.

### Bruk frå eksternt repo

Vil du bruke AP-NO-profilene i ditt eige repo utan å jobbe inni dette monorepoet?
Bootstrap-scriptet legg til dei to filene du treng på eitt minutt:

```bash
curl -sSL https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/main/bootstrap.sh | bash
```

Importer deretter AP-NO-profilene direkte i skjemaet ditt via GitHub Raw-URL:

```yaml
imports:
  - linkml:types
  - https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/v1.0.0/src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema
```

Validering og generering skjer via reusable GitHub Actions-workflows i dette repoet — ingen lokal installasjon er nødvendig. Sjå [Bruk frå eksternt repo](https://brreg.github.io/linkml-datamodellering-no/ekstern-bruk/) for full rettleiing.

---

## Kjende avgrensingar

Repoet er i PoC-fase og har nokre kjende avgrensingar. Sjå desse dokumenta for fullstendig oversikt:

- **[SCOPE.md](SCOPE.md)** — kva repoet er, kva det ikkje er, og kva som høyrer heime her
- **[BUGS.md](BUGS.md)** — komplett liste over kjende bugs og workarounds

**Rapporter nye problem:** Opne eit [GitHub Issue](https://github.com/brreg/linkml-datamodellering-no/issues) med merkelappen `bug`.

---

## Domener

<!-- BEGIN AUTO-GENERATED: DOMAIN TABLE -->
| Domene | Skildring | Dokumentasjon |
|---|---|---|
| fair | **FAIR**-metadataoverbygning — **F**indable, **A**ccessible, **I**nteroperable, **R**eusable. Kan importerast av alle domenemodeller. | [FAIR principles](https://www.go-fair.org/fair-principles/)
| ap-no | Norske W3C-applikasjonsprofiler — DCAT, SKOS, CPSV, DQV m.fl. Importerast av domenemodeller. | [RDF-baserte maskinlesbare ressurser](https://data.norge.no/showroom/overview)
| ngr | Nasjonale grunndata — adresse, eigedom, person og verksemd. | [Nasjonale grunndata](https://informasjonsforvaltning.github.io/nasjonale-grunndata/#OmNasjonaleGrunndata)
| oreg | Offentlege register. |
| fint | FINT felleskomponent — integrasjonsmodellar for fylkeskommunal sektor. | [FINT informasjonsmodell](https://informasjonsmodell.felleskomponent.no/docs?v=v4.0.20)
| samt | SAMT — integrasjonsmodellar for kommunesektoren. | [SAMT-prosjektet](https://docs.samt-bu.no/om/)
| begrepskatalog | Begrepskatalog etter SKOS-AP-NO-Begrep. Instansdatafiler vert automatisk konverterte til SKOS/RDF for publisering til Felles Begrepskatalog. | [SKOS-AP-NO-Begrep](https://data.norge.no/specification/skos-ap-no-begrep)
| modellkatalog | Modellkatalog for informasjonsmodellar etter ModelDCAT-AP-NO for publisering til Felles Datakatalog. | [ModelDCAT-AP-NO](https://data.norge.no/specification/modelldcat-ap-no)
| referanse | Enkle eksempel på gyldige LinkML-modellar (referanseimplementasjonar) |
<!-- END AUTO-GENERATED: DOMAIN TABLE -->

## Skjema

Skjema ligg under `src/linkml/<domain>/<skjema>/`

<!-- BEGIN AUTO-GENERATED: SCHEMA TABLE -->
| Domene | Skjema | Skildring | Dokumentasjon
|---|---|---|---|
| fair | [fair-metadata](src/linkml/fair/fair-metadata/) | **FAIR**-metadataoverbygning (**FAIR**-prinsippa) | [www.go-fair.org/fair-principles/](https://www.go-fair.org/fair-principles/)
| ap-no | [common-ap-no](src/linkml/ap-no/common-ap-no/) | Felles slot-definisjonar for alle AP-NO-profilar | 
| ap-no | [cpsv-ap-no](src/linkml/ap-no/cpsv-ap-no/) | Offentlege tenester og hendingar | [data.norge.no/specification/cpsv-ap-no](https://data.norge.no/specification/cpsv-ap-no)
| ap-no | [dcat-ap-no](src/linkml/ap-no/dcat-ap-no/) | Datakatalogar og datasett | [data.norge.no/specification/dcat-ap-no](https://data.norge.no/specification/dcat-ap-no)
| ap-no | [dqv-ap-no](src/linkml/ap-no/dqv-ap-no/) | Datakvalitet | [data.norge.no/specification/dqv-ap-no](https://data.norge.no/specification/dqv-ap-no)
| ap-no | [modelldcat-ap-no](src/linkml/ap-no/modelldcat-ap-no/) | Informasjonsmodellar | [data.norge.no/specification/modelldcat-ap-no](https://data.norge.no/specification/modelldcat-ap-no)
| ap-no | [skos-ap-no](src/linkml/ap-no/skos-ap-no/) | Omgrepsamlingar | [data.norge.no/specification/skos-ap-no-begrep](https://data.norge.no/specification/skos-ap-no-begrep)
| ap-no | [xkos-ap-no](src/linkml/ap-no/xkos-ap-no/) | Utvida klassifikasjon | [data.norge.no/specification/xkos-ap-no](https://data.norge.no/specification/xkos-ap-no)
| ngr | [ngr-adresse](src/linkml/ngr/ngr-adresse/) | Adresse | [informasjonsforvaltning.github.io/nasjonale-grunndata/#Adresse](https://informasjonsforvaltning.github.io/nasjonale-grunndata/#Adresse)
| ngr | [ngr-eiendom](src/linkml/ngr/ngr-eiendom/) | Fast eigedom, matrikkeleining og bygning | [informasjonsforvaltning.github.io/nasjonale-grunndata/#Temaomr%C3%A5deEiendom](https://informasjonsforvaltning.github.io/nasjonale-grunndata/#Temaomr%C3%A5deEiendom)
| ngr | [ngr-person](src/linkml/ngr/ngr-person/) | Person, identifikasjon og familierelasjonar | [informasjonsforvaltning.github.io/nasjonale-grunndata/#Person](https://informasjonsforvaltning.github.io/nasjonale-grunndata/#Person)
| ngr | [ngr-virksomhet](src/linkml/ngr/ngr-virksomhet/) | Verksemder, roller og organisasjonsstruktur | [informasjonsforvaltning.github.io/nasjonale-grunndata/#Virksomhet](https://informasjonsforvaltning.github.io/nasjonale-grunndata/#Virksomhet)
| oreg | [enhetsregisteret-bvrinn](src/linkml/oreg/enhetsregisteret-bvrinn/) | Berettigede, verger, rettighetshavere i næring (BVRiNN) | 
| oreg | [register-over-aksjeeiere](src/linkml/oreg/register-over-aksjeeiere/) | Aksjeeigarar og eigedelar | 
| fint | [fint-administrasjon](src/linkml/fint/fint-administrasjon/) | Lønn, arbeidsforhold, organisasjon | [informasjonsmodell.felleskomponent.no/docs/package_administrasjon?v=v4.0.20](https://informasjonsmodell.felleskomponent.no/docs/package_administrasjon?v=v4.0.20)
| fint | [fint-arkiv](src/linkml/fint/fint-arkiv/) | Sak, journal, dokument | [informasjonsmodell.felleskomponent.no/docs/package_arkiv?v=v4.0.20](https://informasjonsmodell.felleskomponent.no/docs/package_arkiv?v=v4.0.20)
| fint | [fint-common](src/linkml/fint/fint-common/) | Felles klassar for FINT | 
| fint | [fint-okonomi](src/linkml/fint/fint-okonomi/) | Økonomi og rekneskap | [informasjonsmodell.felleskomponent.no/docs/package_okonomi?v=v4.0.20](https://informasjonsmodell.felleskomponent.no/docs/package_okonomi?v=v4.0.20)
| fint | [fint-personvern](src/linkml/fint/fint-personvern/) | Personvernmeldingar | [informasjonsmodell.felleskomponent.no/docs/package_personvern?v=v4.0.20](https://informasjonsmodell.felleskomponent.no/docs/package_personvern?v=v4.0.20)
| fint | [fint-ressurs](src/linkml/fint/fint-ressurs/) | Ressursar | [informasjonsmodell.felleskomponent.no/docs/package_ressurs?v=v4.0.20](https://informasjonsmodell.felleskomponent.no/docs/package_ressurs?v=v4.0.20)
| fint | [fint-utdanning](src/linkml/fint/fint-utdanning/) | Utdanning og skule | [informasjonsmodell.felleskomponent.no/docs/package_utdanning?v=v4.0.20](https://informasjonsmodell.felleskomponent.no/docs/package_utdanning?v=v4.0.20)
| samt | [samt-bu](src/linkml/samt/samt-bu/) | Skular og barnehagar | [docs.samt-bu.no/om/](https://docs.samt-bu.no/om/)
| begrepskatalog | [brreg-begrepskatalog](src/linkml/begrepskatalog/brreg-begrepskatalog/) | Begrepskatalog for Brønnøysundregistrene | 
| referanse | [referanse](src/linkml/referanse/) | Enkel eksempelmodell for å demonstrere gyldig LinkML-struktur | 
<!-- END AUTO-GENERATED: SCHEMA TABLE -->

**AP-NO-profilane** og **FAIR-metadata** er skjema utan `tree_root` — dei er ikkje sjølvstendige, men meinte å importerast av domenemodeller.

## Genererte modellkatalogar

Modellkatalogar er automatisk genererte oversikter over informasjonsmodellar per organisasjon, basert på ModelDCAT-AP-NO.

<!-- BEGIN AUTO-GENERATED: MODELLKATALOG TABLE -->
| Modellkatalog | Organisasjon | Skildring |
|---|---|---|
| [brreg-modellkatalog](src/linkml/modellkatalog/brreg-modellkatalog/) | Brønnøysundregistra | Modellkatalog for Brønnøysundregistra sine informasjonsmodellar |
| [digdir-modellkatalog](src/linkml/modellkatalog/digdir-modellkatalog/) | Digitaliseringsdirektoratet | Modellkatalog for Digitaliseringsdirektoratet sine informasjonsmodellar |
| [kartverket-modellkatalog](src/linkml/modellkatalog/kartverket-modellkatalog/) | Kartverket | Modellkatalog for Kartverket sine informasjonsmodellar |
| [ksdigital-modellkatalog](src/linkml/modellkatalog/ksdigital-modellkatalog/) | KS Digital | Modellkatalog for KS Digital sine informasjonsmodellar |
| [novari-modellkatalog](src/linkml/modellkatalog/novari-modellkatalog/) | Novari | Modellkatalog for Novari sine informasjonsmodellar |
| [skatteetaten-modellkatalog](src/linkml/modellkatalog/skatteetaten-modellkatalog/) | Skatteetaten | Modellkatalog for Skatteetaten sine informasjonsmodellar |
<!-- END AUTO-GENERATED: MODELLKATALOG TABLE -->

## Genererte artefakter

Køyr `make <domain>` for å generere alle artefakter for eit domene. Kvar generator produserer éin fil under `generated/<domain>/<skjema>/`. Kvar modell kan slå av einskilde generatorar via `manifest.yaml` — sjå [Generatorkonfigurasjon](https://brreg.github.io/linkml-datamodellering-no/manifest-config/) for detaljar.

| Artefakt | Fil | Brukstilfelle | W3C semantisk | manifest.yaml flag |
|---|---|---|---|---|
| JSON-LD kontekst | `<skjema>-context.jsonld` | Mapping frå JSON til RDF — brukast saman med API | ✓ | `jsonld_context` |
| SHACL shapes | `<skjema>-shapes.ttl` | Validering av RDF-data mot skjema i triple stores | ✓ | `shacl` |
| OWL ontologi | `<skjema>-ontology.ttl` | Maskinlesbar ontologi for semantiske verktøy | ✓ | `owl` |
| RDF/Turtle skjema | `<skjema>-schema.ttl` | Fullstendig RDF-representasjon av skjemaet | ✓ | `rdf` |
| Eksempel-RDF | `<skjema>-eksempel.ttl` | Konkret RDF-instans for testing og dokumentasjon | ✓ | `example_rdf` |
| Python-klassar | `<skjema>-model.py` | Direkte bruk i Python-applikasjonar via LinkML | — | `python` |
| JSON Schema | `<skjema>-schema.json` | Validering av JSON-data i applikasjonar og RESTful integrasjon | — | `json_schema` |
| XSD-skjema | `<skjema>-schema.xsd` | XML Schema for XML-basert integrasjon | — | `xsd` |
| Protobuf-skjema | `<skjema>-schema.proto` | gRPC og Protocol Buffers-integrasjon | — | `protobuf` |
| AsyncAPI-spec | `<skjema>-asyncapi.yaml` | Asynkron meldingsutveksling (event-driven API) | — | `asyncapi` |
| OpenAPI-spec | `<skjema>-openapi.yaml` | RESTful API-dokumentasjon (OpenAPI 3.1) | — | `openapi` |
| ER-diagram | `<skjema>-erdiagram.md` | Visuell oversikt over klasser og relasjonar (Mermaid) | — | `erdiagram` |
| Klasse-diagram | `diagrams/<skjema>.puml` + `.svg` | Klassediagram for presentasjon og dokumentasjon (PlantUML) | — | `plantuml` |
| HTML-dokumentasjon | `docs/` | Menneskelesleg referansedokumentasjon basert på markdown | — | `docs` |
| DQV-målingar | `dqv-measurements.ttl` | Datakvalitetsmålingar (kun datakatalog-modellar) | ✓ | — |
| ModelDCAT-element | `modelldcat-elements.ttl` | Modellkatalog-element (kun modellkatalog-modellar) | ✓ | — |

**Publisering til eksterne system:** Sjå [Publiseringsflyt](https://brreg.github.io/linkml-datamodellering-no/publisering-oversikt/#kva-publiserast-til-eksterne-system) for oversikt over GitHub Pages-publisering og høsting til Felles Begrepskatalog/Datakatalog.

## Katalogstruktur

```
linkml-datamodellering-no/
├── src/
│   ├── assets/                                    # Containere, skript og malar
│   ├── linkml/                                    # Kilde for LinkML modeller (og begrepsinstanser)
│   │   └── <domain>/
│   │       └── <modell>/
│   │           ├── <modell>-schema.yaml           # Datamodel
│   │           ├── manifest.yaml                  # Modell-manifest
│   │           ├── published-uris.lock            # Stabile URI-er for publiserte katalogar
│   │           ├── examples/                      
│   │           │   └── <modell>-eksempel.yaml     # Eksempeldatafil
│   │           └── data/                          # Kildedata for publiserte katalogar
│   │               └── <datafil-katalog>/
│   │                   ├── <datafil-katalog>.yaml # Datafil for begrepskatalog
│   │                   └── manifest.yaml          # Datafil-manifest
│   │
│   ├── mcp-linkml-validator/                      # MCP-server: policy-basert LinkML validering
│   ├── mcp-linkml-modell-utkast/                  # MCP-server: generering av LinkML modell-utkast
│   ├── mcp-linkml-begrep-utkast/                  # MCP-server: generering av LinkML begreps-utkast
│   └── tmp/                                       # Mellombelse filer, t.d. JSON Schema-filer til mcp-linkml-modell-utkast
│
├── bootstrap.sh                                   # Bootstrap-script for eksterne repo
├── tests/                                         # Testar og fixtures
├── generated/                                     # Genererte artefakter (ikkje sjekka inn i git)
├── mkdocs/                                        # Dokumentasjonsportal (MkDocs Material)
│   └── docs/                                      # Den publiserte dokumentasjonsportalen
│       └── <domain>/
│          └── <modell>/
│               └── index.md                       # Hoveddokumentasjon for kvar datamodell (generert av publish.sh)
└── specs/
    ├── backlog/                                   # Planer for endringar og nye features
    ├── done/                                      # Utførte planer
    └── bugs/                                      # Kjente bugs

```

---

## For bidragsytarar

Dersom du skal bidra til repoet, les desse dokumenta:

- **[PRINCIPLES.md](PRINCIPLES.md)** — designprinsipp for modellering
- **[CONVENTIONS.md](CONVENTIONS.md)** — namnekonvensjonar, manifestformat og commit-meldingar
- **[CONTRIBUTING.md](CONTRIBUTING.md)** — korleis bidra (PR-prosess, kodegjennomgang)
- **[GOVERNANCE.md](GOVERNANCE.md)** — roller, eigarskap og RFC-prosess
