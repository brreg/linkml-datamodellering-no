# Oversikt: Avgrensingar, prinsipp, funksjonalitet og namnekonvensjonar

**Kortnamn:** `oversikt-avgrensingar-prinsipp`  
**Formål:** Autoritativt referansedokument som presiserer kva dette repoet er og gjer,
kva det ikkje er, og korleis det er organisert. Tener som utgangspunkt for diskusjonar
om scope, prioritering og bidrag.

---

## Kva er dette repoet?

`linkml-datamodellering-no` er eit **nasjonalt verktøyrepo** for informasjonsmodellering
i offentleg sektor. Det kombinerer:

- **Ferdiglagde LinkML-skjema** for norske AP-NO-profil ar og domenemodeller
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

- **AP-NO-profilar** og **fair-metadata** er berre meinte for *import*, ikkje for direkte
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

## Prinsipp

### 1. Pull, ikkje push

Repoet *genererer* artefaktar og publiserer dei til GitHub Pages og GitHub Releases.
Andre system hentar artefaktane derifrå sjølve — repoet pusher aldri til eksterne kjelder
(schema-registry, API-katalog, datakatalog o.l.).

**Grunngiving:** Push-integrasjon krev spesialtilpassingar per målsystem, knyt repoet til
ekstern tilgjengelegheit og autentisering, og gjer det vanskeleg å vedlikehalde.

### 2. Ingen lokale avhengigheiter

All verktøybruk skjer i containere (Podman, WSL2). Det skal ikkje installerast
Python-pakkar, Node-avhengigheiter eller anna verktøy direkte på vertsmaskina.

**Grunngiving:** Reproduserbarheit og portabilitet. Kvar brukar køyrer same miljø.

### 3. Modularitet via import-hierarki

Skjema importerer frå eit klart hierarki — aldri på tvers eller nedover:

```
linkml:types
    ↓
common-ap-no          ← berre AP-NO-profilene importerer denne
    ↓
dcat-ap-no / dqv-ap-no / skos-ap-no / …
    ↓
domenemodeller        ← importerer AP-NO-profilene, ikkje common-ap-no direkte
```
```
fint-common           ← berre FINT-domenemodellane importerer denne
    ↓
fint-administrasjon / fint-arkiv / …
```
```
fair-metadata         ← kan importerast av alle domenemodeller
```

**Grunngiving:** Hindrar sirkular import, gjer avhengigheitane tydelege og støttar gjenbruk.

### 4. Lenking framfor inlining

Klasser som kan opptre sjølvstendig får `identifier: true`. Referansar til andre klasser
vert modelert med URI-referanse, ikkje inlining.

**Grunngiving:** Instansar kan lenkast og delast mellom datasett utan å kopierast.

### 5. Slots, ikkje attributes (for domeneklassar)

Alle domeneklasseeigeskapar vert modellerte som globale slots. Klassespesifikke
innskrenkingar ligg i `slot_usage`. Containerklassen (`tree_root: true`) er unntaket:
der vert klassereferansar modellerte som inline `attributes`.

**Grunngiving:** Globale slots er gjenbrukbare og kan ha `slot_uri` som mapar til RDF.

### 6. Skriftspråk er domenebasert

| Domene | Språk |
|---|---|
| Modellering (klassenamn, slotnamn, skildringar i `.yaml`) | Norsk bokmål |
| Dokumentasjon (README, mkdocs-sider, spesifikasjonar i `specs/`) | Nynorsk |

---

## Funksjonalitet

### Skjema-bibliotek

Ferdige LinkML-skjema for import og gjenbruk:

| Kategori | Skjema | Merknad |
|---|---|---|
| AP-NO-profil ar | `dcat-ap-no`, `dqv-ap-no`, `skos-ap-no`, `xkos-ap-no`, `cpsv-ap-no`, `modelldcat-ap-no` | Berre for import |
| Felles basisklasar | `common-ap-no` | Berre for import av AP-NO-profilar |
| FAIR-metadata | `fair-metadata` | Kan importerast av alle domenemodeller |
| Nasjonale grunndata | `ngr-adresse`, `ngr-eiendom`, `ngr-person`, `ngr-virksomhet` | Fullstendige domenemodeller |
| FINT | `fint-common`, `fint-administrasjon`, `fint-arkiv`, `fint-okonomi`, `fint-personvern`, `fint-ressurs`, `fint-utdanning` | Arvar namgjeving frå FINT-spec |
| Offentlege register | `register-over-aksjeeiere` | Domenemodell |
| Samhandling | `samt-bu` | Skular og barnehagar |
| Begrepskatalog | `brreg-begrepskatalog` | Med produksjonsdata |
| Modellkatalog | `brreg-modellkatalog` | Med produksjonsdata |

### Artefaktgenerering

Frå kvart skjema kan ein generere (konfigurert via `manifest.yaml`):

| Artefakt | Format | Standard |
|---|---|---|
| JSON-LD kontekst | `.jsonld` | ✓ |
| SHACL shapes | `.ttl` | ✓ |
| OWL ontologi | `.ttl` | ✓ |
| RDF/Turtle skjema | `.ttl` | ✓ |
| JSON Schema | `.json` | ✓ |
| Python-klassar | `.py` | ✓ |
| Protobuf-skjema | `.proto` | ✓ |
| ER-diagram | `.md` (Mermaid) | ✓ |
| PlantUML klassediagram | `.puml` + `.svg` | ✓ |
| HTML-dokumentasjon | `docs/` | ✓ |
| Eksempel-RDF | `.ttl` | ✓ |

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

Import av AP-NO-profil ar skjer via HTTP-URL til ein konkret release-tag:
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

## Namnekonvensjonar

### Fil- og mappenamn

Alle filer og katalogar nyttar **`kebab-case`**, alltid norsk eller domene-etablert forkortning:

```
src/linkml/<domain>/<modell>/<modell>-schema.yaml
src/linkml/<domain>/<modell>/examples/<modell>-eksempel.yaml
src/linkml/<domain>/<modell>/data/<datafil>/<datafil>.yaml
```

### Schema-metadata

| Felt | Konvensjon | Døme |
|---|---|---|
| `name` | `kebab-case`, same som filnamnet utan `-schema.yaml` | `ngr-adresse` |
| `id` | Absolutt HTTPS-URL utan avsluttande `/` | `https://data.norge.no/ngr/ngr-adresse` |
| `title` | Norsk bokmål, tittelformat | `Nasjonale grunndata – Adresse` |
| `default_prefix` | Same som `id` med avsluttande `/` | `https://data.norge.no/ngr/ngr-adresse/` |
| `version` | Semantisk versjonering i hermeteikn | `"1.0.0"` |

### URI-segment-konvensjon

| Segment | Tydning | Døme |
|---|---|---|
| `ap-no` | AP-NO-applikasjonsprofil | `https://data.norge.no/ap-no/dcat-ap-no` |
| `oreg` | Offentleg register | `https://data.norge.no/oreg/register-over-aksjeeiere` |
| `ngr` | Nasjonale grunndata | `https://data.norge.no/ngr/ngr-adresse` |
| `fint` | FINT-domenemodell | `https://data.norge.no/fint/fint-administrasjon` |
| `samt` | Samhandlingsmodell | `https://data.norge.no/samt/samt-bu` |
| `begrepskatalog` | Begrepskatalog | `https://data.norge.no/begrepskatalog/brreg-begrepskatalog` |
| `modellkatalog` | Modellkatalog | `https://data.norge.no/modellkatalog/brreg-modellkatalog` |
| `fair` | FAIR-metadatamodell | `https://data.norge.no/fair/fair-metadata` |

URI-ar er **persistente**: `id`-feltet skal ikkje endrast etter første publisering.

### Klassenamn

**PascalCase**, norsk bokmål. Særnorske bokstavar **translittererte**:

| Bokstav | Erstatning |
|---|---|
| æ / Æ | ae / Ae |
| ø / Ø | oe / Oe |
| å / Å | aa / Aa |

```yaml
# Riktig
Aktoer          # Aktør
Tidsrom
KommunalKatalog

# Feil
Aktør           # særnorsk bokstav i identifikator
kommunalkatalog # ikkje PascalCase
```

**Containerklassenamn** følgjer mønsteret `<Domene>Container` i PascalCase
(t.d. `AdresseContainer`, `AksjeeierContainer`).

### Slotnamn

**`snake_case`**, norsk bokmål. Unntak: FINT-skjema brukar `camelCase` (arva frå FINT-spec).

```yaml
# Riktig (AP-NO og domenemodell)
kommunenummer
adressenavn_tekst
utgjevar_id

# Riktig (FINT-unntak)
kildesystemId
rolleNavn

# `_ref`-suffiks i NGR for URI-referansar
kommune_ref
adressenavn_ref
```

### Standardprefiksar

Desse aliasa skal alltid brukast — aldri andre alias for same namespace:

| Prefix | Namespace |
|---|---|
| `dcat:` | `http://www.w3.org/ns/dcat#` |
| `dct:` | `http://purl.org/dc/terms/` |
| `foaf:` | `http://xmlns.com/foaf/0.1/` |
| `skos:` | `http://www.w3.org/2004/02/skos/core#` |
| `vcard:` | `http://www.w3.org/2006/vcard/ns#` |
| `rdf:` | `http://www.w3.org/1999/02/22-rdf-syntax-ns#` |
| `rdfs:` | `http://www.w3.org/2000/01/rdf-schema#` |
| `owl:` | `http://www.w3.org/2002/07/owl#` |
| `xsd:` | `http://www.w3.org/2001/XMLSchema#` |
| `prov:` | `http://www.w3.org/ns/prov#` |
| `linkml:` | `https://w3id.org/linkml/` |

### Commit-meldingar

Conventional Commits-format: `<type>(<scope>): <skildring>`

| Type | Bruksområde |
|---|---|
| `feat` | Ny klasse, nytt slot |
| `fix` | Rettjing av feil range, URI o.l. |
| `refactor` | Omstrukturering utan semantisk endring |
| `docs` | Skildringar, README, portalinnhald |
| `chore` | CI, skript, manifest utan modellendringar |
| `feat!` / `fix!` | Brotande endring |

**Scope** er modellnamnet i kebab-case. Bruk `*` for infrastruktur-endringar
som ikkje tilhøyrer éin modell.

---

## Manifestformat

### Per skjema (har `generators:`-seksjon)

```yaml
publish_external: false   # true for publisering til ekstern katalog
data_policy: bronze        # bronze / silver / gold / felles-datakatalog / felles-begrepskatalog

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

### Per datafil (manglar `generators:`-seksjon)

```yaml
publish_external: true
data_policy: felles-begrepskatalog

concepts:                   # valfri — utelat for å publisere heile datafila
  - https://begrep.brreg.no/foretaksnavn
```

CI skil manifesttypen på om `generators:`-seksjonen er til stades.

---

## Roller og eigarskap

| Rolle | Ansvar |
|---|---|
| Repo-administrator | Infrastruktur, CI/CD, reusable workflows, felles-skjema (common, fair) |
| Katalogeigarleiing | AP-NO-profil ar, MCP-validator, policy-oppdateringar |
| Domenemodell-eigar | Eiga org sine modellar under `src/linkml/<domain>/` |
| Bidragsytar | PR mot eiga org eller etter avtale |

Kvar domenemodell har ein eigar-org i `CODEOWNERS.md`. Brotande endringar
i delte skjema (`ap-no`, `common`) krev RFC-prosess: GitHub Issue,
14-dagars diskusjonsfrist, konsensus.

---

## Kjende avvik og unntak

| Avvik | Grunngiving |
|---|---|
| FINT-skjema brukar `camelCase` og engelske slotnamn | Arvar frå FINT API-spec |
| `brreg-modellkatalog` dekkjer berre 2 skjema | Under utvikling |
| `license:`-feltet manglar i alle skjema | Ikkje enda prioritert — sjå `avvik-felles-modelleringsregler.md` |
| `begrep.brreg.no`-URI-ar svarer ikkje | Mogleg nedlagd domene — sjå `avvik-peikarar-til-offentlege-ressursar.md` |
| `register-over-aksjeeiere` har `example.no` som schema-ID | Feil som skal rettast — sjå tiltak PO1 |
| `xkos-ap-no` brukar `dct:startDate` (finst ikkje i DC Terms) | Bug — sjå tiltak XK1 |

Sjå `specs/bugs/` for alle kjende bugs med workarounds, og `specs/backlog/avvik-*.md`
for gap-analysar mot norske standardar.
