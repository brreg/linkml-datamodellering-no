# linkml-datamodellering-no

!!! warning "Proof of Concept"

    Dette repoet er ein **Proof of Concept** for LinkML-basert datamodellering i norsk offentleg sektor.
    
    **Kva det betyr:**
    
    - Modellar og verktøy er under utvikling og kan endre seg
    - Dokumentasjonen kan vere ufullstendig eller utdatert
    - Nokre funksjonar er berre delvis implementerte
    - Det finst [kjende avgrensingar og bugs](#kjende-avgrensingar)
    - Ingen garantert stabilitet eller support-SLA
    
    **For eksterne organisasjonar:** Les [for bidragsytarar](#for-bidragsytarar) for forventningar til stabilitet og ansvar.

!!! note "Målsetting"

    Dette repoet har som mål å realisere dei delane av [Rammeverk for informasjonsforvaltning](https://www.digdir.no/informasjonsforvaltning/rammeverk-informasjonsforvaltning/3626) som går på begrepsmodellering, informasjonsmodellering, metadata og publisering til felles begrepskatalog og datakatalog i henhold til nasjonale veiledere og standarder. Det er tenkt som eit felles repo for nasjonale begreps- og datamodeller inkludert felles verktøy. Både modeller og verktøy kan benyttes lokalt i andre git-repoer. 



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

---

## Avgrensingar

Repoet er i PoC-fase og har nokre kjende avgrensingar. Sjå desse dokumenta for fullstendig oversikt:

- **[SCOPE.md](https://github.com/brreg/linkml-datamodellering-no/blob/main/SCOPE.md)** — kva repoet er, kva det ikkje er, og kva som høyrer heime her
- **[BUGS.md](https://github.com/brreg/linkml-datamodellering-no/blob/main/BUGS.md)** — komplett liste over kjende bugs og workarounds

**Rapporter nye problem:** Opne eit [GitHub Issue](https://github.com/brreg/linkml-datamodellering-no/issues) med merkelappen `bug`.

---

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

Begrep vert organiserte i **begrepssamlingar** (éi fil per begrep) som automatisk aggregerast til ein **begrepskatalog** per organisasjon.

> Bytt ut **`domene`**, **`begrepssamling-namn`** og **`organisasjon`** med dine aktuelle namn.

```bash
# 1. Opprett ny begrepssamling (filstruktur for begrep)
make new-begrepssamling DOMAIN=domene NAME=begrepssamling-namn
# Døme: make new-begrepssamling DOMAIN=oreg NAME=begrepssamling-foretaksregisteret
```

Scriptet opprettar:
- `src/linkml/domene/begrepssamling-namn/begrep/` — mappe for begrepsfiler
- `src/linkml/domene/begrepssamling-namn/build.yaml` — manifest med aggregation-metadata

```bash
# 2. Fyll ut aggregation-metadata i build.yaml
#    → src/linkml/domene/begrepssamling-namn/build.yaml
#    Sett: aggregation.organization (organisasjonsnummer)
#          aggregation.catalog_name (t.d. "brreg-begrepskatalog")
```

```bash
# 3a. Generer begrep med mcp-linkml-begrep-utkast (anbefalt)
make mcp-begrep-run
# Bruk verktøyet 'skriv_begrep_fil' med:
#   - domain: domene
#   - begrepssamling: begrepssamling-namn
#   - slug: begrep-identifikator (t.d. "foretaksnavn")
#   - profil: "brreg" (eller "default")
# → skriv til src/linkml/domene/begrepssamling-namn/begrep/<slug>.yaml

# 3b. Eller skriv begrep manuelt:
#    → src/linkml/domene/begrepssamling-namn/begrep/mitt-begrep.yaml
```

```bash
# 4. Køyr gen-begrepskatalog-instance for å aggregere til begrepskatalog
make gen-begrepskatalog-instance
# → genererer src/linkml/begrepskatalog/<organisasjon>-begrepskatalog/data/<organisasjon>-begrepskatalog/<organisasjon>-begrepskatalog.yaml
```

```bash
# 5. Valider begrepskatalogen
make mcp-linkml-validate \
  SCHEMA=src/linkml/begrepskatalog/<organisasjon>-begrepskatalog/<organisasjon>-begrepskatalog-schema.yaml \
  POLICY=felles-begrepskatalog
```

```bash
# 6. Generer artefaktar og publiser til dokumentasjonsportal
make begrepskatalog && make docs-publish && make docs-serve   # → http://localhost:8000
```

**Filstruktur:**
```
src/linkml/
  oreg/
    begrepssamling-foretaksregisteret/
      build.yaml                    ← aggregation-metadata
      begrep/
        foretaksnavn.yaml          ← éin fil per begrep
        nestleder.yaml
  begrepskatalog/                   ← automatisk generert
    brreg-begrepskatalog/
      data/
        brreg-begrepskatalog/
          brreg-begrepskatalog.yaml ← aggregert frå alle brreg-begrepssamlingar
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

## Domener

<!-- BEGIN AUTO-GENERATED: DOMAIN TABLE -->
| Domene | Skildring | Dokumentasjon |
|---|---|---|
| [fair](fair/) | **FAIR**-metadataoverbygning — **F**indable, **A**ccessible, **I**nteroperable, **R**eusable. Kan importerast av alle domenemodeller. | [FAIR principles](https://www.go-fair.org/fair-principles/)
| [ap-no](ap-no/) | Norske W3C-applikasjonsprofiler — DCAT, SKOS, CPSV, DQV m.fl. Importerast av domenemodeller. | [RDF-baserte maskinlesbare ressurser](https://data.norge.no/showroom/overview)
| [referanse](referanse/) | Enkle eksempel på gyldige LinkML-modellar (referanseimplementasjonar) |
| [ngr](ngr/) | Nasjonale grunndata — adresse, eigedom, person og verksemd. | [Nasjonale grunndata](https://informasjonsforvaltning.github.io/nasjonale-grunndata/#OmNasjonaleGrunndata)
| [oreg](oreg/) | Offentlege register. |
| [fint](fint/) | FINT felleskomponent — integrasjonsmodellar for fylkeskommunal sektor. | [FINT informasjonsmodell](https://informasjonsmodell.felleskomponent.no/docs?v=v4.0.20)
| [samt](samt/) | SAMT — integrasjonsmodellar for kommunesektoren. | [SAMT-prosjektet](https://docs.samt-bu.no/om/)
| [begrepskatalog](begrepskatalog/) | Begrepskatalog etter SKOS-AP-NO-Begrep. Instansdatafiler vert automatisk konverterte til SKOS/RDF for publisering til Felles Begrepskatalog. | [SKOS-AP-NO-Begrep](https://data.norge.no/specification/skos-ap-no-begrep)
| [modellkatalog](modellkatalog/) | Modellkatalog for informasjonsmodellar etter ModelDCAT-AP-NO for publisering til Felles Datakatalog. | [ModelDCAT-AP-NO](https://data.norge.no/specification/modelldcat-ap-no)
<!-- END AUTO-GENERATED: DOMAIN TABLE -->

## Skjema

Skjema ligg under `src/linkml/<domain>/<skjema>/`

<!-- BEGIN AUTO-GENERATED: SCHEMA TABLE -->
| Domene | Skjema | Skildring | Dokumentasjon
|---|---|---|---|
| [fair](fair/) | [fair-metadata](fair/fair-metadata/) | **FAIR**-metadataoverbygning (**FAIR**-prinsippa) | [www.go-fair.org/fair-principles/](https://www.go-fair.org/fair-principles/)
| [ap-no](ap-no/) | [common-ap-no](ap-no/common-ap-no/) | Felles slot-definisjonar for alle AP-NO-profilar | 
| [ap-no](ap-no/) | [cpsv-ap-no](ap-no/cpsv-ap-no/) | Offentlege tenester og hendingar | [data.norge.no/specification/cpsv-ap-no](https://data.norge.no/specification/cpsv-ap-no)
| [ap-no](ap-no/) | [dcat-ap-no](ap-no/dcat-ap-no/) | Datakatalogar og datasett | [data.norge.no/specification/dcat-ap-no](https://data.norge.no/specification/dcat-ap-no)
| [ap-no](ap-no/) | [dqv-ap-no](ap-no/dqv-ap-no/) | Datakvalitet | [data.norge.no/specification/dqv-ap-no](https://data.norge.no/specification/dqv-ap-no)
| [ap-no](ap-no/) | [modelldcat-ap-no](ap-no/modelldcat-ap-no/) | Informasjonsmodellar | [data.norge.no/specification/modelldcat-ap-no](https://data.norge.no/specification/modelldcat-ap-no)
| [ap-no](ap-no/) | [skos-ap-no](ap-no/skos-ap-no/) | Omgrepsamlingar | [data.norge.no/specification/skos-ap-no-begrep](https://data.norge.no/specification/skos-ap-no-begrep)
| [ap-no](ap-no/) | [xkos-ap-no](ap-no/xkos-ap-no/) | Utvida klassifikasjon | [data.norge.no/specification/xkos-ap-no](https://data.norge.no/specification/xkos-ap-no)
| [referanse](referanse/) | [referanse](referanse/) | Enkel eksempelmodell for å demonstrere gyldig LinkML-struktur | 
| [ngr](ngr/) | [ngr-adresse](ngr/ngr-adresse/) | Adresse | [informasjonsforvaltning.github.io/nasjonale-grunndata/#Adresse](https://informasjonsforvaltning.github.io/nasjonale-grunndata/#Adresse)
| [ngr](ngr/) | [ngr-eiendom](ngr/ngr-eiendom/) | Fast eigedom, matrikkeleining og bygning | [informasjonsforvaltning.github.io/nasjonale-grunndata/#Temaomr%C3%A5deEiendom](https://informasjonsforvaltning.github.io/nasjonale-grunndata/#Temaomr%C3%A5deEiendom)
| [ngr](ngr/) | [ngr-person](ngr/ngr-person/) | Person, identifikasjon og familierelasjonar | [informasjonsforvaltning.github.io/nasjonale-grunndata/#Person](https://informasjonsforvaltning.github.io/nasjonale-grunndata/#Person)
| [ngr](ngr/) | [ngr-virksomhet](ngr/ngr-virksomhet/) | Verksemder, roller og organisasjonsstruktur | [informasjonsforvaltning.github.io/nasjonale-grunndata/#Virksomhet](https://informasjonsforvaltning.github.io/nasjonale-grunndata/#Virksomhet)
| [oreg](oreg/) | [enhetsregisteret-bvrinn](oreg/enhetsregisteret-bvrinn/) | Berettigede, verger, rettighetshavere i næring (BVRiNN) | 
| [oreg](oreg/) | [register-over-aksjeeiere](oreg/register-over-aksjeeiere/) | Aksjeeigarar og eigedelar | 
| [fint](fint/) | [fint-administrasjon](fint/fint-administrasjon/) | Lønn, arbeidsforhold, organisasjon | [informasjonsmodell.felleskomponent.no/docs/package_administrasjon?v=v4.0.20](https://informasjonsmodell.felleskomponent.no/docs/package_administrasjon?v=v4.0.20)
| [fint](fint/) | [fint-arkiv](fint/fint-arkiv/) | Sak, journal, dokument | [informasjonsmodell.felleskomponent.no/docs/package_arkiv?v=v4.0.20](https://informasjonsmodell.felleskomponent.no/docs/package_arkiv?v=v4.0.20)
| [fint](fint/) | [fint-common](fint/fint-common/) | Felles klassar for FINT | 
| [fint](fint/) | [fint-okonomi](fint/fint-okonomi/) | Økonomi og rekneskap | [informasjonsmodell.felleskomponent.no/docs/package_okonomi?v=v4.0.20](https://informasjonsmodell.felleskomponent.no/docs/package_okonomi?v=v4.0.20)
| [fint](fint/) | [fint-personvern](fint/fint-personvern/) | Personvernmeldingar | [informasjonsmodell.felleskomponent.no/docs/package_personvern?v=v4.0.20](https://informasjonsmodell.felleskomponent.no/docs/package_personvern?v=v4.0.20)
| [fint](fint/) | [fint-ressurs](fint/fint-ressurs/) | Ressursar | [informasjonsmodell.felleskomponent.no/docs/package_ressurs?v=v4.0.20](https://informasjonsmodell.felleskomponent.no/docs/package_ressurs?v=v4.0.20)
| [fint](fint/) | [fint-utdanning](fint/fint-utdanning/) | Utdanning og skule | [informasjonsmodell.felleskomponent.no/docs/package_utdanning?v=v4.0.20](https://informasjonsmodell.felleskomponent.no/docs/package_utdanning?v=v4.0.20)
| [samt](samt/) | [samt-bu](samt/samt-bu/) | Skular og barnehagar | [docs.samt-bu.no/om/](https://docs.samt-bu.no/om/)
<!-- END AUTO-GENERATED: SCHEMA TABLE -->

**AP-NO-profilane** og **FAIR-metadata** er skjema utan `tree_root` — dei er ikkje sjølvstendige, men meinte å importerast av domenemodeller.

## Genererte begrepskatalogar

Begrepskatalogar er automatisk genererte oversikter over begrep per organisasjon, basert på SKOS-AP-NO.

Begrepskatalogar ligg under `src/linkml/begrepskatalog/`

<!-- BEGIN AUTO-GENERATED: BEGREPSKATALOG TABLE -->
| Domene | Begrepskatalog | Organisasjon | Skildring | Generator |
|---|---|---|---|---|
| [begrepskatalog](https://brreg.github.io/linkml-datamodellering-no/begrepskatalog/) | [brreg-begrepskatalog](begrepskatalog/brreg-begrepskatalog/) | Brønnøysundregistra | Begrepskatalog for Brønnøysundregistra sine begrep | [`gen-begrepskatalog-instance`](COMMANDS.md#vedlikehald) |
<!-- END AUTO-GENERATED: BEGREPSKATALOG TABLE -->

## Genererte modellkatalogar

Modellkatalogar er automatisk genererte oversikter over informasjonsmodellar per organisasjon, basert på ModelDCAT-AP-NO.

Modellkatalogar ligg under `src/linkml/modellkatalog/`

<!-- BEGIN AUTO-GENERATED: MODELLKATALOG TABLE -->
| Domene | Modellkatalog | Organisasjon | Skildring | Generator |
|---|---|---|---|---|
| [modellkatalog](https://brreg.github.io/linkml-datamodellering-no/modellkatalog/) | [brreg-modellkatalog](modellkatalog/brreg-modellkatalog/) | Brønnøysundregistra | Modellkatalog for Brønnøysundregistra sine informasjonsmodellar | [`gen-modellkatalog-instance`](COMMANDS.md#vedlikehald) |
| [modellkatalog](https://brreg.github.io/linkml-datamodellering-no/modellkatalog/) | [digdir-modellkatalog](modellkatalog/digdir-modellkatalog/) | Digitaliseringsdirektoratet | Modellkatalog for Digitaliseringsdirektoratet sine informasjonsmodellar | [`gen-modellkatalog-instance`](COMMANDS.md#vedlikehald) |
| [modellkatalog](https://brreg.github.io/linkml-datamodellering-no/modellkatalog/) | [kartverket-modellkatalog](modellkatalog/kartverket-modellkatalog/) | Kartverket | Modellkatalog for Kartverket sine informasjonsmodellar | [`gen-modellkatalog-instance`](COMMANDS.md#vedlikehald) |
| [modellkatalog](https://brreg.github.io/linkml-datamodellering-no/modellkatalog/) | [ksdigital-modellkatalog](modellkatalog/ksdigital-modellkatalog/) | KS Digital | Modellkatalog for KS Digital sine informasjonsmodellar | [`gen-modellkatalog-instance`](COMMANDS.md#vedlikehald) |
| [modellkatalog](https://brreg.github.io/linkml-datamodellering-no/modellkatalog/) | [novari-modellkatalog](modellkatalog/novari-modellkatalog/) | Novari | Modellkatalog for Novari sine informasjonsmodellar | [`gen-modellkatalog-instance`](COMMANDS.md#vedlikehald) |
| [modellkatalog](https://brreg.github.io/linkml-datamodellering-no/modellkatalog/) | [skatteetaten-modellkatalog](modellkatalog/skatteetaten-modellkatalog/) | Skatteetaten | Modellkatalog for Skatteetaten sine informasjonsmodellar | [`gen-modellkatalog-instance`](COMMANDS.md#vedlikehald) |
<!-- END AUTO-GENERATED: MODELLKATALOG TABLE -->

## Genererte artefakter

Køyr `make <domain>` for å generere alle artefakter for eit domene. Kvar generator produserer éin fil under `generated/<domain>/<skjema>/`. Kvar modell kan slå av einskilde generatorar via `manifest.yaml` — sjå [Generatorkonfigurasjon](https://brreg.github.io/linkml-datamodellering-no/build-config/) for detaljar.

<!-- BEGIN AUTO-GENERATED: ARTIFACTS TABLE -->
| Artefakt | Fil | Brukstilfelle | W3C semantisk | manifest.yaml flag | Generator |
|---|---|---|---|---|---|
| Modellmetadata ihht ModellDCAT-AP-NO | `metadata/<skjema>-manifest.yaml` | ModelDCAT-AP-NO metadata for publisering til Felles Datakatalog | — | — | [`gen-informasjonsmodell-instance`](COMMANDS.md#vedlikehald) |
| JSON-LD kontekst | `<skjema>-context.jsonld` | Mapping frå JSON til RDF — brukast saman med API | ✓ | `jsonld_context` | [`gen-jsonld-context`](COMMANDS.md#enkeltartefakter) |
| SHACL shapes | `<skjema>-shapes.ttl` | Validering av RDF-data mot skjema i triple stores | ✓ | `shacl` | [`gen-shacl`](COMMANDS.md#enkeltartefakter) |
| OWL ontologi | `<skjema>-ontology.ttl` | Maskinlesbar ontologi for semantiske verktøy | ✓ | `owl` | [`gen-owl`](COMMANDS.md#enkeltartefakter) |
| RDF/Turtle skjema | `<skjema>-schema.ttl` | Fullstendig RDF-representasjon av skjemaet | ✓ | `rdf` | [`gen-rdf`](COMMANDS.md#enkeltartefakter) |
| Eksempel-RDF | `<skjema>-eksempel.ttl` | Konkret RDF-instans for testing og dokumentasjon | ✓ | `example_rdf` | [`convert-rdf`](COMMANDS.md#enkeltartefakter) |
| Python-klassar | `<skjema>-model.py` | Direkte bruk i Python-applikasjonar via LinkML | — | `python` | [`gen-python`](COMMANDS.md#enkeltartefakter) |
| JSON Schema | `<skjema>-schema.json` | Validering av JSON-data i applikasjonar og RESTful integrasjon | — | `json_schema` | [`gen-jsonschema`](COMMANDS.md#enkeltartefakter) |
| XSD-skjema | `<skjema>-schema.xsd` | XML Schema for XML-basert integrasjon | — | `xsd` | [`gen-xsd`](COMMANDS.md#enkeltartefakter) |
| Protobuf-skjema | `<skjema>-schema.proto` | gRPC og Protocol Buffers-integrasjon | — | `protobuf` | [`gen-proto`](COMMANDS.md#enkeltartefakter) |
| AsyncAPI-spec | `<skjema>-asyncapi.yaml` | Asynkron meldingsutveksling (event-driven API) | — | `asyncapi` | [`gen-asyncapi`](COMMANDS.md#enkeltartefakter) |
| OpenAPI-spec | `<skjema>-openapi.yaml` | RESTful API-dokumentasjon (OpenAPI 3.1) | — | `openapi` | [`gen-openapi`](COMMANDS.md#enkeltartefakter) |
| ER-diagram | `<skjema>-erdiagram.md` | Visuell oversikt over klasser og relasjonar (Mermaid) | — | `erdiagram` | [`gen-erdiagram`](COMMANDS.md#enkeltartefakter) |
| Klasse-diagram | `diagrams/<skjema>.puml` + `.svg` | Klassediagram for presentasjon og dokumentasjon (PlantUML) | — | `plantuml` | [`gen-plantuml`](COMMANDS.md#enkeltartefakter) |
| HTML-dokumentasjon | `docs/` | Menneskelesleg referansedokumentasjon basert på markdown | — | `docs` | [`gen-docs`](COMMANDS.md#enkeltartefakter) |
| DQV-målingar | `dqv-measurements.ttl` | Datakvalitetsmålingar (kun datakatalog-modellar) | ✓ | — | [`gen-dqv-measurements`](COMMANDS.md#enkeltartefakter) |
| ModelDCAT-element | `modelldcat-elements.ttl` | Modellkatalog-element (kun modellkatalog-modellar) | ✓ | — | [`gen-modelldcat-elements`](COMMANDS.md#enkeltartefakter) |
<!-- END AUTO-GENERATED: ARTIFACTS TABLE -->
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

- **[PRINCIPLES.md](https://github.com/brreg/linkml-datamodellering-no/blob/main/PRINCIPLES.md)** — designprinsipp for modellering
- **[CONVENTIONS.md](https://github.com/brreg/linkml-datamodellering-no/blob/main/CONVENTIONS.md)** — namnekonvensjonar, manifestformat og commit-meldingar
- **[GOVERNANCE.md](https://github.com/brreg/linkml-datamodellering-no/blob/main/GOVERNANCE.md)** — roller, eigarskap og RFC-prosess
- **[CONTRIBUTING.md](https://github.com/brreg/linkml-datamodellering-no/blob/main/CONTRIBUTING.md)** — korleis bidra (PR-prosess, kodegjennomgang)
- **[README-tabellgenerering](https://brreg.github.io/linkml-datamodellering-no/readme-tabellgenerering/)** — korleis README-tabellane vert genererte
