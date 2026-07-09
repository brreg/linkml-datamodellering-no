# Scope og avgrensingar

**Formål:** Presiserer kva dette repoet er og gjer, kva det ikkje er, og kva som høyrer heime her.

---

## Kva er dette repoet?

`linkml-datamodellering-no` er eit **nasjonalt verktøyrepo** for informasjonsmodellering
i offentleg sektor. Det kombinerer:

- **Ferdiglagde LinkML-skjema** for norske AP-NO-profilene og domenemodeller
- **Infrastruktur** for automatisk generering, validering og publisering av artefaktar
- **Verktøy** for å bootstrappe LinkML-modellering i andre repo

Repoet er tenkt som eit felles grunnlag — ein stad der norske offentlege verksemder
kan hente og gjenbruke modellar, og der aktuelle samarbeidspartnarar forvaltar
felles modellar saman.

**Status:** Proof of Concept. Strukturen er stabil, men ikkje alt er produksjonsklart.

---

## Avgrensingar

### Kva repoet IKKJE er

| Det er IKKJE… | Forklaring |
|---|---|
| Ein schema-registry | Repoet pusher ikkje skjema til Apicurio, Confluent eller andre schema-registries. Skjema vert henta frå GitHub (pull). |
| Ein datakatalog | Repoet er ikkje sjølv ein datakatalog. Det genererer maskinlesbare artefaktar (SKOS/RDF, ModelDCAT-AP-NO) som Felles datakatalog og Felles begrepskatalog *sjølv* kan sette opp pull mot frå GitHub Pages eller GitHub Releases. |
| Ein kjeldesystem for produksjonsdata | Med eitt unntak (`data/`-underkatalogar for begrepskatalog og modellkatalog) inneheld ikkje repoet produksjonsdata. Modellane *skildrar* data, dei *inneheld* det ikkje. |
| Eit API | Repoet eksponerer ikkje API-endepunkt. Artefaktar vert publisert som statiske filer på GitHub Pages og GitHub Releases. |
| Ein integrasjonsplattform | Repoet integrasjoner ikkje mot kjeldesystem, registre eller applikasjonar direkte. |
| Eit verktøy for enkeltverksemder | Repo-et er eit *delt* monorepo. Verksemder med behov for full kontroll bør vurdere å bruke bootstrap-mekanismen og halde eigne modeller i eige repo. |

### Scope-avgrensingar for innhald

- **AP-NO-profilene** og **fair-metadata** er berre meinte for *import*, ikkje for direkte
  bruk som containerklasse-baserte skjema. Dei har inga `tree_root`-klasse.
- **FINT-modellar** arvar namgjeving (camelCase, engelske attributtnamn) frå FINT API-spesifikasjonen.
  Avvik frå namnekonvensjonen i dette repoet er eit bevisst val, ikkje ein feil.
- **Produksjonsdata** kan berre liggje under `data/`-underkatalogar i skjema med
  `publish_external: true`. Eksempeldata (under `examples/`) er alltid illustrativt,
  ikkje normativt.
- **Ekstern katalog-integrasjon** er alltid pull-basert: Felles datakatalog og Felles
  begrepskatalog må sjølv sette opp henting av artefaktar frå GitHub Pages eller GitHub Releases.
  Dette repoet initierer aldri push til eksterne katalogar.

### Kva det vil seie å vere «i repoet»

Ein modell høyrer heime i dette repoet dersom han:
1. Implementerer ein norsk AP-NO-profil, eller
2. Er ein domenemodell som baserer seg på ein AP-NO-profil og skal delast nasjonalt, eller
3. Er ein felles hjelpeklasse/-skjema (common, fair-metadata)

Ein modell høyrer **ikkje** heime her dersom han:
- Berre er relevant for éi verksemd og ikkje er planlagd delt
- Baserer seg på ein proprietær standard utan norsk AP-NO-profil
- Krev kontinuerleg push til eit eksternt system som ein del av arbeidsflyten

---

## Funksjonalitet

### Skjema-bibliotek

Ferdige LinkML-skjema for import og gjenbruk:

| Kategori | Skjema | Merknad |
|---|---|---|
| AP-NO-profilene | `dcat-ap-no`, `dqv-ap-no`, `skos-ap-no`, `xkos-ap-no`, `cpsv-ap-no`, `modelldcat-ap-no` | Berre for import |
| Felles basisklasar | `common-ap-no` | Berre for import av AP-NO-profilar |
| FAIR-metadata | `fair-metadata` | Kan importerast av alle domenemodeller |
| Nasjonale grunndata | `ngr-adresse`, `ngr-eiendom`, `ngr-person`, `ngr-virksomhet` | Fullstendige domenemodeller |
| FINT | `fint-common`, `fint-administrasjon`, `fint-arkiv`, `fint-okonomi`, `fint-personvern`, `fint-ressurs`, `fint-utdanning` | Arvar namgjeving frå FINT-spec |
| Offentlege register | `enhetsregisteret-bvrinn`, `register-over-aksjeeiere` | Domenemodeller |
| Samhandling | `samt-bu` | Skular og barnehagar |
| Begrepskatalog | `brreg-begrepskatalog` | Med produksjonsdata |
| Modellkatalog | `brreg-modellkatalog`, `digdir-modellkatalog`, `kartverket-modellkatalog`, `ksdigital-modellkatalog`, `novari-modellkatalog`, `skatteetaten-modellkatalog` | Med produksjonsdata |
| Referanse | `referanse` | Enkle eksempel på gyldige LinkML-modellar |

### Artefaktgenerering

Køyr `make <domain>` for å generere alle artefakter for eit domene. Kvar generator produserer éin fil under `generated/<domain>/<skjema>/`. Kvar modell kan slå av einskilde generatorar via `build.yaml`.

| Artefakt | Fil | Brukstilfelle | W3C semantisk | build.yaml flag |
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

### Validering

MCP-validator (`src/mcp-linkml-validator/`) med medaljong policy-nivå og publiseringssjekkar:

| Policy | Krav | Brukstilfelle |
|---|---|---|
| `bronze` | Schema-ID, prefix, klassenamn, slotnamn, identifikatorar | Minimum for alle skjema |
| `silver` | Bronze + utgjevar, status, endringsdato; DCAT-AP-NO-struktur | Skjema klare for publisering |
| `gold` | Silver + begrepsbeskrivingar på alle klassar | Full semantisk kvalitet |
| `felles-datakatalog` | Publiseringssjekkar for ModelDCAT-AP-NO | Skjema klare for at Felles datakatalog kan hente dei |
| `felles-begrepskatalog` | Publiseringssjekkar for SKOS-AP-NO | Omgrep klare for at Felles begrepskatalog kan hente dei |

### CI/CD-pipelines

| Pipeline | Utløysar | Kva det gjer |
|---|---|---|
| `validate.yml` | Push, PR | Linter og validerer alle skjema med MCP-validator |
| `generate.yml` | Push til main | Genererer alle artefaktar, publiserer til GitHub Pages |
| `reusable-validate.yml` | Kall frå eksterne repo | Validering av eitt skjema med éin policy |
| `release-please.yml` | Push til main | Oppretter release-PR ved nye commits |

### Bootstrap-mekanisme

`bootstrap.sh` set opp eit eksternt repo for LinkML-modellering på under eitt minutt:
- Oppretter `linkml-datamodellering.yaml` (pinnar versjon)
- Oppretter `.github/workflows/linkml.yml` (brukar reusable workflow)

Import av AP-NO-profilene skjer via HTTP-URL til ein konkret release-tag:
```yaml
imports:
  - linkml:types
  - https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/v2.0.0/src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema
```

### MCP-tenarar

| Tenar | Funksjon |
|---|---|
| `mcp-linkml-validator` | Policy-basert skjema- og instansvalidering med forklaring |
| `mcp-linkml-modell-utkast` | Genererer LinkML-skjemautkast frå skildring eller JSON Schema |
| `mcp-linkml-begrep-utkast` | Genererer SKOS-AP-NO-begrepsinstansar frå skildring |

### Dokumentasjonsportal

GitHub Pages (`mkdocs/`) med oversikt over alle skjema, genererte artefaktar,
ER-diagram og HTML-dokumentasjon. Vert automatisk oppdatert ved push til `main`.

---

## Sjå også

- [PRINCIPLES.md](PRINCIPLES.md) — designprinsipp for modellering
- [CONVENTIONS.md](CONVENTIONS.md) — namnekonvensjonar og manifestformat
- [GOVERNANCE.md](GOVERNANCE.md) — roller, eigarskap og bidragsprosess
- [BUGS.md](BUGS.md) — kjende bugs og workarounds
