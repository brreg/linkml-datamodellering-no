# linkml-datamodellering-no

!!! warning "Proof of Concept"

    Dette repoet er ein **Proof of Concept** for LinkML-basert datamodellering i norsk offentleg sektor.
    
    **Kva det betyr:**
    
    - Modellar og verktøy er under utvikling og kan endre seg
    - Dokumentasjonen kan vere ufullstendig eller utdatert
    - Nokre funksjonar er berre delvis implementerte
    - Det finst [kjende avgrensingar og bugs](#avgrensingar)
    - Ingen garantert stabilitet eller support-SLA
    
    **For eksterne organisasjonar:** Les [for bidragsytarar](#for-bidragsytarar) for forventningar til stabilitet og ansvar.

## Målsetting

  Dette repoet har som mål å realisere dei delane av [Rammeverk for informasjonsforvaltning](https://www.digdir.no/informasjonsforvaltning/rammeverk-informasjonsforvaltning/3626) som går på begrepsmodellering, informasjonsmodellering, metadata og publisering til felles begrepskatalog og datakatalog i henhold til nasjonale veiledere og standarder. Det er tenkt som eit felles repo for nasjonale begreps- og datamodeller inkludert felles verktøy. Både modeller og verktøy kan benyttes lokalt i andre git-repoer. 

---

## Innhald

> [LinkML](https://linkml.io/) er eit open kjeldekode-modelleringsspråk der du skriv skjemaer i YAML som skildrar datastrukturen din, og som du kan nytte til å generere skjemaer, data, diagram og dokumentasjon i andre format ([LinkML generators](https://linkml.io/linkml/generators/index.html)). Generatorane konverterer både til tradisjonelle format (JSON Schema, Python, Protobuf) og W3C-semantiske format (RDF/Turtle, OWL, SHACL, JSON-LD) utan behov for ekstra mapping.

Dette [kodelageret](https://github.com/brreg/linkml-datamodellering-no) inneheld:

* LinkML-[modellar](https://github.com/brreg/linkml-datamodellering-no/tree/main#skjema) for norske [W3C-applikasjonsprofiler](https://data.norge.no/showroom/overview) og offentlege domenemodeller for gjenbruk.
* [mcp-linkml-modell-utkast](https://github.com/brreg/linkml-datamodellering-no/blob/main/src/mcp-linkml-modell-utkast/README.md) for å generere utkast til nye informasjonsmodellar i LinkML format ihht [Rammeverk for informasjonsforvaltning](https://www.digdir.no/informasjonsforvaltning/rammeverk-informasjonsforvaltning/3626).
* [mcp-linkml-begrep-utkast](https://github.com/brreg/linkml-datamodellering-no/blob/main/src/mcp-linkml-begrep-utkast/README.md) for å generere utkast til nye begreper i LinkML format ihht [skos-ap-no standarden](https://data.norge.no/specification/skos-ap-no-begrep).
* [mcp-linkml-validator](https://github.com/brreg/linkml-datamodellering-no/blob/main/src/mcp-linkml-validator/README.md)  for å validere LinkML-skjemaer ihht [Felles modelleringsregler for offentlig forvaltning](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029) og [FAIR prinsippa](https://www.go-fair.org/fair-principles/). Validatoren implementerer kvalitets-profilar (bronze, silver, gold), publiserings-profilar (felles begrepskatalog og felles datakatalog) og har støtte for egendefinerte profilar.
* LinkML-[generatorar](https://github.com/brreg/linkml-datamodellering-no/blob/main/README.md#genererte-artefakter) for å produsere artefakter i andre format frå LinkML-skjemaer.
* Github Actions [pipelines](https://github.com/brreg/linkml-datamodellering-no/actions) for å automatisk generere, validere og publisere artefakter frå LinkML-skjemaer.
* Guide for å publisere begreper til [felles begrepskatalog](https://brreg.github.io/linkml-datamodellering-no/publisering-begrep/) ihht [skos-ap-no standarden](https://data.norge.no/specification/skos-ap-no-begrep).
* Guide for å publisere informasjonsmodellar til [felles datakatalog](https://brreg.github.io/linkml-datamodellering-no/publisering-modell/) ihht [modeldcat-ap-no standarden](https://data.norge.no/specification/modelldcat-ap-no).
* Github Pages [dokumentasjonsportal](https://brreg.github.io/linkml-datamodellering-no/) med oversikt over alle LinkML-skjemaer og genererte artefakter med styling ihht [designsystemet.no](https://designsystemet.no/no).
* Opplegg for å [bootstrappe](https://brreg.github.io/linkml-datamodellering-no/ekstern-bruk/) eit eksternt repo for lokal LinkML modellering.

---

## Avgrensingar

> Repoet er i PoC-fase og har nokre kjende avgrensingar. Sjå desse dokumenta for fullstendig oversikt:

- **[SCOPE.md](https://github.com/brreg/linkml-datamodellering-no/blob/main/SCOPE.md)** — kva repoet er, kva det ikkje er, og kva som høyrer heime her
- **[BUGS.md](https://github.com/brreg/linkml-datamodellering-no/blob/main/BUGS.md)** — komplett liste over kjende bugs og workarounds

**Rapporter nye problem:** Opne eit [GitHub Issue](https://github.com/brreg/linkml-datamodellering-no/issues) med merkelappen `bug`.

---

## Kom i gang

> Her får du ei kjapp innføring i oppsett av lokalt miljø for å komme igang med datamodellering og begrepsarbeid.

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

> Bruk oppskrifta under for å komme igang med datamodellering.

> Bytt ut **`domene`** og **`modellnavn`** med dine aktuelle navn.

```bash
# 1. Lag eit nytt tomt LinkML-skjema (skjema + filstruktur)
make new-modell NAME=modellnavn DOMAIN=domene

# 1b. (om ønskjeleg) Generer frå eksisterande JSON Schema
# Legg JSON Schema-filen i tmp/, t.d. tmp/modellnavn.json
make mcp-linkml-modell-utkast SCHEMA=tmp/modellnavn.json
# → genererer tmp/modellnavn-schema.yaml. Kopier til src/linkml/domain/modellnavn/
```
```bash
# 2. Rediger modellfila etter behov
#    → src/linkml/domain/modellnavn/modellnavn-schema.yaml
```
```bash
# 3. Valider skjema
make mcp-linkml-valider-modell \
  SCHEMA=src/linkml/domene/modellnavn/modellnavn-schema.yaml \
  POLICY=felles-datakatalog
```
```bash
# 4. (om ønskjeleg) angi kva artefakter som skal genereres og publiseres i build.yaml
# → src/linkml/domain/modellnavn/build.yaml

# 4b. Generer artefakter og publiser til dokumentasjonsportal
make <domain> && make docs-publish && make docs-serve   # → http://localhost:8000
```

Nye skjema under `src/linkml/<domain>/<modellnavn>/` vert oppdaga automatisk.

For full rettleiing: sjå [Ny domenemodell](https://brreg.github.io/linkml-datamodellering-no/ny-domenemodell/) og [Publiser til Felles Datakatalog](https://brreg.github.io/linkml-datamodellering-no/publisering-modell/).

### Begrepsmodellering

> Bruk oppskrifta under for å komme igang med begrepsmodellering.

> Bytt ut **`domene`**, **`begrepssamling-namn`** og **`organisasjon`** med dine aktuelle namn.

```bash
# 1a. Opprett ny begrepssamling (filstruktur for begrep)
make new-begrepssamling DOMAIN=domene NAME=begrepssamling-namn

# 1b. (om ønskjeleg) Generer begrepsutkast frå eksisterande tekst
make mcp-linkml-begrep-utkast INPUT=<sti-til-tekstfil>
# → genererer begrepsutkast i tmp/ og kopier til src/linkml/domene/begrepssamling-namn/begrep/begrepnavn.yaml
```
```bash
# 2. Rediger begrep etter behov
#    → src/linkml/domene/begrepssamling-namn/begrep/<begrep-slug>.yaml
```
```bash
# 3. Aggreger til begrepskatalog
make gen-begrepskatalog-instance
```
```bash
# 4. Valider begrepskatalog
make mcp-linkml-valider-modell \
  SCHEMA=src/linkml/begrepskatalog/<organisasjon>-begrepskatalog/<organisasjon>-begrepskatalog-schema.yaml \
  POLICY=felles-begrepskatalog
```
```bash
# 5a. (om ønskjeleg) angi kva artefakter som skal genereres fra begrepskatalogen i build.yaml
#    → src/linkml/begrepskatalog/<organisasjon>-begrepskatalog/data/<organisasjon>-begrepskatalog/build.yaml

# 5b. Generer artefakter og publiser til dokumentasjonsportal
make begrepskatalog && make docs-publish && make docs-serve   # → http://localhost:8000
```

Nye begrepssamlingar under `src/linkml/<domain>/<begrepssamling>/` vert oppdaga automatisk.

For full rettleiing: sjå [Ny begrepskatalog](https://brreg.github.io/linkml-datamodellering-no/ny-begrepsmodell/) og [Publiser til Felles Begrepskatalog](https://brreg.github.io/linkml-datamodellering-no/publisering-begrep/).

Sjå [CLAUDE.md](https://github.com/brreg/linkml-datamodellering-no/blob/main/CLAUDE.md) for modelleringsprinsipp og [COMMANDS.md](https://github.com/brreg/linkml-datamodellering-no/blob/main/COMMANDS.md) for alle tilgjengelege kommandoar.

### Bruk frå eksternt repo

> Vil du bruke AP-NO-profilene i ditt eige repo utan å jobbe inni dette monorepoet?
> Bootstrap-scriptet legg til dei to filene du treng på eitt minutt:

```bash
curl -sSL https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/main/bootstrap.sh | bash
```

Importer deretter AP-NO-profilene direkte i skjemaet ditt via GitHub Raw-URL:

```yaml
imports:
  - linkml:types
  - https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/dcat-ap-no-v2.8.0/src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema
```

Validering og generering skjer via reusable GitHub Actions-workflows i dette repoet — ingen lokal installasjon er nødvendig. Sjå [Bruk frå eksternt repo](https://brreg.github.io/linkml-datamodellering-no/ekstern-bruk/) for full rettleiing.

---

## Domener

> Datamodellane er gruppert i domener.

Domena ligg under `src/linkml/<domain>/`

| Domene | Skildring | Dokumentasjon |
|---|---|---|
| [REFERANSE](referanse/) | Enkle eksempel på gyldige LinkML-modellar (referanseimplementasjonar) 
| [FAIR](fair/) | **FAIR**-metadataoverbygning — **F**indable, **A**ccessible, **I**nteroperable, **R**eusable. Kan importerast av alle domenemodeller. | [FAIR principles](https://www.go-fair.org/fair-principles/)
| [AP-NO](ap-no/) | Norske W3C-applikasjonsprofiler — DCAT, SKOS, CPSV, DQV m.fl. Importerast av domenemodeller. | [RDF-baserte maskinlesbare ressurser](https://data.norge.no/showroom/overview)
| [NGR](ngr/) | Nasjonale grunndata — adresse, eigedom, person og verksemd. | [Nasjonale grunndata](https://informasjonsforvaltning.github.io/nasjonale-grunndata/#OmNasjonaleGrunndata)
| [OREG](oreg/) | Offentlege register. |
| [FINT](fint/) | FINT felleskomponent — integrasjonsmodellar for fylkeskommunal sektor. | [FINT informasjonsmodell](https://informasjonsmodell.felleskomponent.no/docs?v=v4.0.20)
| [SAMT](samt/) | SAMT — integrasjonsmodellar for kommunesektoren. | [SAMT-prosjektet](https://docs.samt-bu.no/om/)
| [BEGREPSKATALOG](begrepskatalog/) | Begrepskatalog etter SKOS-AP-NO-Begrep. Instansdatafiler vert automatisk konverterte til SKOS/RDF for publisering til Felles Begrepskatalog. | [SKOS-AP-NO-Begrep](https://data.norge.no/specification/skos-ap-no-begrep)
| [MODELLKATALOG](modellkatalog/) | Modellkatalog for informasjonsmodellar etter ModelDCAT-AP-NO for publisering til Felles Datakatalog. | [ModelDCAT-AP-NO](https://data.norge.no/specification/modelldcat-ap-no)

---

## Skjema

> Det er eit skjema i LinkML format for kvar datamodell.

Skjema ligg under `src/linkml/<domain>/<skjema>/`

<!-- BEGIN AUTO-GENERATED: src/assets/scripts/makefile/generate-readme-tables.sh generate_schema_table -->
| Domene | Skjema | Skildring | Dokumentasjon
|---|---|---|---|
| [FAIR](fair/) | [fair-metadata](fair/fair-metadata/) | "FAIR-metadataoverbygning (FAIR-prinsippa)" | [www.go-fair.org](https://www.go-fair.org/fair-principles/)
| [AP-NO](ap-no/) | [common-ap-no](ap-no/common-ap-no/) | Felles slot-definisjonar for alle AP-NO-profilar | 
| [AP-NO](ap-no/) | [cpsv-ap-no](ap-no/cpsv-ap-no/) | Offentlege tenester og hendingar | [data.norge.no](https://data.norge.no/specification/cpsv-ap-no)
| [AP-NO](ap-no/) | [dcat-ap-no](ap-no/dcat-ap-no/) | Datakatalogar og datasett | [data.norge.no](https://data.norge.no/specification/dcat-ap-no)
| [AP-NO](ap-no/) | [dqv-ap-no](ap-no/dqv-ap-no/) | Datakvalitet | [data.norge.no](https://data.norge.no/specification/dqv-ap-no)
| [AP-NO](ap-no/) | [modelldcat-ap-no](ap-no/modelldcat-ap-no/) | Informasjonsmodellar | [data.norge.no](https://data.norge.no/specification/modelldcat-ap-no)
| [AP-NO](ap-no/) | [skos-ap-no](ap-no/skos-ap-no/) | Omgrepsamlingar | [data.norge.no](https://data.norge.no/specification/skos-ap-no-begrep)
| [AP-NO](ap-no/) | [xkos-ap-no](ap-no/xkos-ap-no/) | Utvida klassifikasjon | [data.norge.no](https://data.norge.no/specification/xkos-ap-no)
| [REFERANSE](referanse/) | [referansemodell-bronze](referanse/referansemodell-bronze/) | Viser minstekrava for å bestå bronsepolicyen: HTTP(S)-id, schema-metadata (title, version), class_uri, identifier-slot, slot_uri og begrepsidentifikator på riktig format. | 
| [REFERANSE](referanse/) | [referansemodell-gold](referanse/referansemodell-gold/) | Viser minstekrava for å bestå gullpolicyen: alle sølv-krav pluss FAIR-metadata (title, version, prefiks, lisens, proveniens). | 
| [REFERANSE](referanse/) | [referansemodell-silver](referanse/referansemodell-silver/) | Viser minstekrava for å bestå sølvpolicyen: alle bronse-krav pluss DCAT-AP-NO og DQV-AP-NO-klassar med påkravde slots og containerklasse. | 
| [REFERANSE](referanse/) | [referansemodell](referanse/referansemodell/) | Enkel eksempelmodell for å demonstrere gyldig LinkML-struktur | 
| [NGR](ngr/) | [ngr-adresse](ngr/ngr-adresse/) | Adresse | [informasjonsforvaltning.github.io](https://informasjonsforvaltning.github.io/nasjonale-grunndata/#Adresse)
| [NGR](ngr/) | [ngr-eiendom](ngr/ngr-eiendom/) | Fast eigedom, matrikkeleining og bygning | [informasjonsforvaltning.github.io](https://informasjonsforvaltning.github.io/nasjonale-grunndata/#Temaomr%C3%A5deEiendom)
| [NGR](ngr/) | [ngr-person](ngr/ngr-person/) | Person, identifikasjon og familierelasjonar | [informasjonsforvaltning.github.io](https://informasjonsforvaltning.github.io/nasjonale-grunndata/#Person)
| [NGR](ngr/) | [ngr-virksomhet](ngr/ngr-virksomhet/) | Verksemder, roller og organisasjonsstruktur | [informasjonsforvaltning.github.io](https://informasjonsforvaltning.github.io/nasjonale-grunndata/#Virksomhet)
| [OREG](oreg/) | [enhetsregisteret-bvrinn](oreg/enhetsregisteret-bvrinn/) | Berettigede, verger, rettighetshavere i næring (BVRiNN) | 
| [OREG](oreg/) | [register-over-aksjeeiere](oreg/register-over-aksjeeiere/) | Aksjeeigarar og eigedelar | 
| [FINT](fint/) | [fint-administrasjon](fint/fint-administrasjon/) | Lønn, arbeidsforhold, organisasjon | [informasjonsmodell.felleskomponent.no](https://informasjonsmodell.felleskomponent.no/docs/package_administrasjon?v=v4.0.20)
| [FINT](fint/) | [fint-arkiv](fint/fint-arkiv/) | Sak, journal, dokument | [informasjonsmodell.felleskomponent.no](https://informasjonsmodell.felleskomponent.no/docs/package_arkiv?v=v4.0.20)
| [FINT](fint/) | [fint-common](fint/fint-common/) | Felles klassar for FINT | 
| [FINT](fint/) | [fint-okonomi](fint/fint-okonomi/) | Økonomi og rekneskap | [informasjonsmodell.felleskomponent.no](https://informasjonsmodell.felleskomponent.no/docs/package_okonomi?v=v4.0.20)
| [FINT](fint/) | [fint-personvern](fint/fint-personvern/) | Personvernmeldingar | [informasjonsmodell.felleskomponent.no](https://informasjonsmodell.felleskomponent.no/docs/package_personvern?v=v4.0.20)
| [FINT](fint/) | [fint-ressurs](fint/fint-ressurs/) | Ressursar | [informasjonsmodell.felleskomponent.no](https://informasjonsmodell.felleskomponent.no/docs/package_ressurs?v=v4.0.20)
| [FINT](fint/) | [fint-utdanning](fint/fint-utdanning/) | Utdanning og skule | [informasjonsmodell.felleskomponent.no](https://informasjonsmodell.felleskomponent.no/docs/package_utdanning?v=v4.0.20)
| [SAMT](samt/) | [samt-bu](samt/samt-bu/) | Skular og barnehagar | [docs.samt-bu.no](https://docs.samt-bu.no/om/)
<!-- END AUTO-GENERATED: src/assets/scripts/makefile/generate-readme-tables.sh generate_schema_table -->

**AP-NO-profilane** og **FAIR-metadata** er skjema utan `tree_root` — dei er ikkje sjølvstendige, men meinte å importerast av domenemodeller.

---

## Genererte artefakter

> Du kan generere artefakter fra LinkML skjemaet.

Genererte artefakter ligg under `generated/<domain>/<skjema>/`.  
Køyr `make <domain>` for å generere alle artefakter for eit domene.  
Kvar modell kan slå av einskilde generatorar via `src/linkml/<domain>/<skjema>/build.yaml` — sjå [Generatorkonfigurasjon](https://brreg.github.io/linkml-datamodellering-no/build-config/) for detaljar.

| Artefakt | Fil | Brukstilfelle | W3C semantisk | build.yaml flag | Generator |
|---|---|---|---|---|---|
| Modellmetadata ihht ModellDCAT-AP-NO | `metadata/<skjema>-manifest.yaml` | ModelDCAT-AP-NO metadata for publisering til Felles Datakatalog | — | — | [`gen-informasjonsmodell-instance`](https://github.com/brreg/linkml-datamodellering-no/blob/main/COMMANDS.md#gen-informasjonsmodell-instance) |
| JSON-LD kontekst | `<skjema>-context.jsonld` | Mapping frå JSON til RDF — brukast saman med API | ✓ | `jsonld_context` | [`gen-jsonld-context`](https://github.com/brreg/linkml-datamodellering-no/blob/main/COMMANDS.md#gen-jsonld-context) |
| SHACL shapes | `<skjema>-shapes.ttl` | Validering av RDF-data mot skjema i triple stores | ✓ | `shacl` | [`gen-shacl`](https://github.com/brreg/linkml-datamodellering-no/blob/main/COMMANDS.md#gen-shacl) |
| OWL ontologi | `<skjema>-ontology.ttl` | Maskinlesbar ontologi for semantiske verktøy | ✓ | `owl` | [`gen-owl`](https://github.com/brreg/linkml-datamodellering-no/blob/main/COMMANDS.md#gen-owl) |
| RDF/Turtle skjema | `<skjema>-schema.ttl` | Fullstendig RDF-representasjon av skjemaet | ✓ | `rdf` | [`gen-rdf`](https://github.com/brreg/linkml-datamodellering-no/blob/main/COMMANDS.md#gen-rdf) |
| Eksempel-RDF | `<skjema>-eksempel.ttl` | Konkret RDF-instans for testing og dokumentasjon | ✓ | `example_rdf` | [`convert-rdf`](https://github.com/brreg/linkml-datamodellering-no/blob/main/COMMANDS.md#convert-rdf) |
| Python-klassar | `<skjema>-model.py` | Direkte bruk i Python-applikasjonar via LinkML | — | `python` | [`gen-python`](https://github.com/brreg/linkml-datamodellering-no/blob/main/COMMANDS.md#gen-python) |
| JSON Schema | `<skjema>-schema.json` | Validering av JSON-data i applikasjonar og RESTful integrasjon | — | `json_schema` | [`gen-jsonschema`](https://github.com/brreg/linkml-datamodellering-no/blob/main/COMMANDS.md#gen-jsonschema) |
| XSD-skjema | `<skjema>-schema.xsd` | XML Schema for XML-basert integrasjon | — | `xsd` | [`gen-xsd`](https://github.com/brreg/linkml-datamodellering-no/blob/main/COMMANDS.md#gen-xsd) |
| Protobuf-skjema | `<skjema>-schema.proto` | gRPC og Protocol Buffers-integrasjon | — | `protobuf` | [`gen-proto`](https://github.com/brreg/linkml-datamodellering-no/blob/main/COMMANDS.md#gen-proto) |
| AsyncAPI-spec | `<skjema>-asyncapi.yaml` | Asynkron meldingsutveksling (event-driven API) | — | `asyncapi` | [`gen-asyncapi`](https://github.com/brreg/linkml-datamodellering-no/blob/main/COMMANDS.md#gen-asyncapi) |
| OpenAPI-spec | `<skjema>-openapi.yaml` | RESTful API-dokumentasjon (OpenAPI 3.1) | — | `openapi` | [`gen-openapi`](https://github.com/brreg/linkml-datamodellering-no/blob/main/COMMANDS.md#gen-openapi) |
| ER-diagram | `<skjema>-erdiagram.md` | Visuell oversikt over klasser og relasjonar (Mermaid) | — | `erdiagram` | [`gen-erdiagram`](https://github.com/brreg/linkml-datamodellering-no/blob/main/COMMANDS.md#gen-erdiagram) |
| Klasse-diagram | `diagrams/<skjema>.puml` + `.svg` | Klassediagram for presentasjon og dokumentasjon (PlantUML) | — | `plantuml` | [`gen-plantuml`](https://github.com/brreg/linkml-datamodellering-no/blob/main/COMMANDS.md#gen-plantuml) |
| HTML-dokumentasjon | `docs/` | Menneskelesleg referansedokumentasjon basert på markdown | — | `docs` | [`gen-docs`](https://github.com/brreg/linkml-datamodellering-no/blob/main/COMMANDS.md#gen-docs) |
| DQV-målingar | `dqv-measurements.ttl` | Datakvalitetsmålingar (kun datakatalog-modellar) | ✓ | — | [`gen-dqv-measurements`](https://github.com/brreg/linkml-datamodellering-no/blob/main/COMMANDS.md#gen-dqv-measurements) |
| ModelDCAT-element | `modelldcat-elements.ttl` | Modellkatalog-element (kun modellkatalog-modellar) | ✓ | — | [`gen-modelldcat-elements`](https://github.com/brreg/linkml-datamodellering-no/blob/main/COMMANDS.md#gen-modelldcat-elements) |

**Publisering til eksterne system:** Sjå [Publiseringsflyt](https://brreg.github.io/linkml-datamodellering-no/publisering-oversikt/#kva-publiserast-til-eksterne-system) for oversikt over GitHub Pages-publisering og høsting til Felles Begrepskatalog/Datakatalog.

---

## Genererte begrepskatalogar

> Begrepskatalogar er automatisk genererte oversikter over begrep per organisasjon, basert på SKOS-AP-NO standarden.

Begrepskatalogar ligg under `src/linkml/begrepskatalog/`

<!-- BEGIN AUTO-GENERATED: src/assets/scripts/makefile/generate-readme-tables.sh generate_begrepskatalog_table -->
| Domene | Begrepskatalog | Organisasjon | Skildring | Generator |
|---|---|---|---|---|
| [begrepskatalog](https://brreg.github.io/linkml-datamodellering-no/begrepskatalog/) | [brreg-begrepskatalog](begrepskatalog/brreg-begrepskatalog/) | Registerenheten i Brønnøysund | Begrepskatalog for Registerenheten i Brønnøysund sine begrep | [`gen-begrepskatalog-instance`](https://github.com/brreg/linkml-datamodellering-no/blob/main/COMMANDS.md#gen-begrepskatalog-instance) |
<!-- END AUTO-GENERATED: src/assets/scripts/makefile/generate-readme-tables.sh generate_begrepskatalog_table -->

---

## Genererte modellkatalogar

> Modellkatalogar er automatisk genererte oversikter over informasjonsmodellar per organisasjon, basert på ModelDCAT-AP-NO standarden.

Modellkatalogar ligg under `src/linkml/modellkatalog/`

<!-- BEGIN AUTO-GENERATED: src/assets/scripts/makefile/generate-readme-tables.sh generate_modellkatalog_table -->
| Domene | Modellkatalog | Organisasjon | Skildring | Generator |
|---|---|---|---|---|
| [modellkatalog](https://brreg.github.io/linkml-datamodellering-no/modellkatalog/) | [brreg-modellkatalog](modellkatalog/brreg-modellkatalog/) | Brønnøysundregistra | Modellkatalog for Brønnøysundregistra sine informasjonsmodellar | [`gen-modellkatalog-instance`](https://github.com/brreg/linkml-datamodellering-no/blob/main/COMMANDS.md#gen-modellkatalog-instance) |
| [modellkatalog](https://brreg.github.io/linkml-datamodellering-no/modellkatalog/) | [digdir-modellkatalog](modellkatalog/digdir-modellkatalog/) | Digitaliseringsdirektoratet | Modellkatalog for Digitaliseringsdirektoratet sine informasjonsmodellar | [`gen-modellkatalog-instance`](https://github.com/brreg/linkml-datamodellering-no/blob/main/COMMANDS.md#gen-modellkatalog-instance) |
| [modellkatalog](https://brreg.github.io/linkml-datamodellering-no/modellkatalog/) | [kartverket-modellkatalog](modellkatalog/kartverket-modellkatalog/) | Kartverket | Modellkatalog for Kartverket sine informasjonsmodellar | [`gen-modellkatalog-instance`](https://github.com/brreg/linkml-datamodellering-no/blob/main/COMMANDS.md#gen-modellkatalog-instance) |
| [modellkatalog](https://brreg.github.io/linkml-datamodellering-no/modellkatalog/) | [ksdigital-modellkatalog](modellkatalog/ksdigital-modellkatalog/) | KS Digital | Modellkatalog for KS Digital sine informasjonsmodellar | [`gen-modellkatalog-instance`](https://github.com/brreg/linkml-datamodellering-no/blob/main/COMMANDS.md#gen-modellkatalog-instance) |
| [modellkatalog](https://brreg.github.io/linkml-datamodellering-no/modellkatalog/) | [novari-modellkatalog](modellkatalog/novari-modellkatalog/) | Novari IKS | Modellkatalog for Novari IKS sine informasjonsmodellar | [`gen-modellkatalog-instance`](https://github.com/brreg/linkml-datamodellering-no/blob/main/COMMANDS.md#gen-modellkatalog-instance) |
| [modellkatalog](https://brreg.github.io/linkml-datamodellering-no/modellkatalog/) | [skatteetaten-modellkatalog](modellkatalog/skatteetaten-modellkatalog/) | Skatteetaten | Modellkatalog for Skatteetaten sine informasjonsmodellar | [`gen-modellkatalog-instance`](https://github.com/brreg/linkml-datamodellering-no/blob/main/COMMANDS.md#gen-modellkatalog-instance) |
<!-- END AUTO-GENERATED: src/assets/scripts/makefile/generate-readme-tables.sh generate_modellkatalog_table -->

---

## Katalogstruktur

> Her finn du oversikt over dei mest sentrale katalogane i repoet.

```
linkml-datamodellering-no/
├── src/
│   ├── assets/                                    # Containere, skript og malar
│   ├── linkml/                                    # Kilde for LinkML modeller (og begrepsinstanser)
│   │   └── <domain>/
│   │       └── <modell>/
│   │           ├── <modell>-schema.yaml           # Datamodel
│   │           ├── build.yaml                     # Byggkonfigurasjon
│   │           ├── published-uris.lock            # Stabile URI-er for publiserte katalogar
│   │           ├── examples/                      
│   │           │   └── <modell>-eksempel.yaml     # Eksempeldatafil
│   │           └── data/                          # Kildedata for publiserte katalogar
│   │               └── <datafil-katalog>/
│   │                   ├── <datafil-katalog>.yaml # Datafil for begrepskatalog
│   │                   └── build.yaml             # Datafil-byggkonfigurasjon
│   │
│   ├── mcp-linkml-validator/                      # MCP-server: policy-basert LinkML validering
│   ├── mcp-linkml-modell-utkast/                  # MCP-server: generering av LinkML modell-utkast
│   ├── mcp-linkml-begrep-utkast/                  # MCP-server: generering av LinkML begreps-utkast
│   └── tmp/                                       # Mellombelse filer, t.d. JSON Schema-filer til mcp-linkml-modell-utkast
│
├── bootstrap.sh                                   # Bootstrap-script for eksterne repo
├── bugs/                                          # Kjente bugs
├── tests/                                         # Testar og fixtures
├── generated/                                     # Genererte artefakter (ikkje sjekka inn i git)
├── make/                                          # GNU Make filer for make kommandoar. Sjå COMMANDS.md for kommandoar.
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

> Her finn du sentrale dokumenter for bidragsytere.

Dersom du skal bidra til repoet, les desse dokumenta:

- **[PRINCIPLES.md](https://github.com/brreg/linkml-datamodellering-no/blob/main/PRINCIPLES.md)** — designprinsipp for modellering
- **[CONVENTIONS.md](https://github.com/brreg/linkml-datamodellering-no/blob/main/CONVENTIONS.md)** — namnekonvensjonar, manifestformat og commit-meldingar
- **[GOVERNANCE.md](https://github.com/brreg/linkml-datamodellering-no/blob/main/GOVERNANCE.md)** — roller, eigarskap og RFC-prosess
- **[CONTRIBUTING.md](https://github.com/brreg/linkml-datamodellering-no/blob/main/CONTRIBUTING.md)** — korleis bidra (PR-prosess, kodegjennomgang)
- **[README-tabellgenerering](https://brreg.github.io/linkml-datamodellering-no/readme-tabellgenerering/)** — korleis README-tabellane vert genererte
