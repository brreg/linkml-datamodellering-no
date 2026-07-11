# Namnekonvensjonar og format

**Formål:** Referansedokument for namnekonvensjonar, manifestformat og commit-meldingar.

---

## Fil- og mappenamn

Alle filer og katalogar nyttar **`kebab-case`**, alltid norsk eller domene-etablert forkortning:

```
src/linkml/<domain>/<modell>/<modell>-schema.yaml
src/linkml/<domain>/<modell>/examples/<modell>-eksempel.yaml
src/linkml/<domain>/<modell>/data/<datafil>/<datafil>.yaml
```

---

## Schema-metadata

| Felt | Konvensjon | Døme |
|---|---|---|
| `name` | LangString: bokmål (`nb`) og nynorsk (`nn`) i `kebab-case` | `nb: ngr-adresse`<br>`nn: ngr-adresse` |
| `id` | Absolutt HTTPS-URL utan avsluttande `/` | `https://data.norge.no/ngr/ngr-adresse` |
| `title` | LangString: bokmål (`nb`) og nynorsk (`nn`), tittelformat | `nb: "Nasjonale grunndata - Adresse"`<br>`nn: "Nasjonale grunndata - Adresse"` |
| `default_prefix` | Same som `id` med avsluttande `/` | `https://data.norge.no/ngr/ngr-adresse/` |
| `version` | Semantisk versjonering i hermeteikn | `"1.0.0"` |
| `license` | Standard: NLOD 2.0. Alltid absolutt URI. | `https://data.norge.no/nlod/no/2.0` |

**YAML-format for LangString-felt:**
```yaml
name:
  nb: ngr-adresse
  nn: ngr-adresse

title:
  nb: "Nasjonale grunndata - Adresse"
  nn: "Nasjonale grunndata - Adresse"
```

---

## URI-segment-konvensjon

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
| `referanse` | Referanseimplementasjon | `https://data.norge.no/referanse/referanse` |

URI-ar er **persistente**: `id`-feltet skal ikkje endrast etter første publisering.

---

## Klassenamn

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

---

## Slotnamn

**`snake_case`**, norsk bokmål. Unntak: FINT-skjema brukar `camelCase` (arva frå FINT-spec).

**Format:** `snake_case` tillét berre små bokstavar (`a-z`), tal (`0-9`) og understrek (`_`). 
**Bindestreker er ikkje tillate** — bruk samansette ord utan separasjon (t.d. `epost`, `epostadresse`) 
eller understrek (`mobilnummer_utgaar`).

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

---

## Standardprefiksar

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

---

## Commit-meldingar

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

**Format:** Commit-meldingar skal vere **så kompakte som mogleg**. Meldinga skal skrivast i 
**presens** og kun innehalde **kva som er endra** (ikkje kvifor eller bakgrunn — det finst i 
specen/koden). Format: éi hovudlinje (`<type>(<scope>): <skildring>`) og éin kort bullet 
per endra fil/komponent. Unngå lange forklarande avsnitt; bruk stikkord.

Døme:
```
fix(mcp-modell-utkast): prioriter multivalued og primitive typar i slot-konfliktar
  - converter.py: prioriter multivalued over single-value, primitive over klasse-ref
  - tests/test_make.sh: normaliser property-namn (bindestrek → underscore)
  - specs/done/json-schema-roundtrip-test.md: alle tre testar passerer
```

---

## Manifestformat

### Per skjema (har `generators:`-seksjon)

`build.yaml` per skjema:

```yaml
publish_external: false   # true for å publisere til ekstern katalog
validation_policy: silver # bronze / silver / gold / felles-datakatalog / felles-begrepskatalog

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

`build.yaml` per datafil:

```yaml
publish_external: true
validation_policy: felles-begrepskatalog

concepts:                   # valfri — utelat for å publisere heile datafila
  - https://begrep.brreg.no/foretaksnavn
  - https://begrep.brreg.no/nestleder
```

CI skil manifesttypen på om `generators:`-seksjonen er til stades. Datafil-underkatalogar 
utan `build.yaml` vert validerte automatisk med `bronze`-policy.

### Per begrepssamling (har `aggregation:`-seksjon)

`build.yaml` per begrepssamling:

```yaml
publish_external: false         # berre begrepskatalogen publiserer
validation_policy: bronze       # bronze / silver / gold

# Metadata for aggregering til begrepskatalog
aggregation:
  organization: "974760673"     # organisasjonsnummer (tilsv. Brønnøysundregistra)
  catalog_name: brreg-begrepskatalog

generators:
  jsonld_context: true
  shacl: true
  # osv.
```

**Filstruktur for begrepssamlingar:**

```
src/linkml/
  <domain>/
    begrepssamling-<namn>/
      build.yaml                    ← manifestfil med aggregation-metadata
      begrep/                       ← éin YAML-fil per begrep (frittstående)
        <begrep-id>.yaml
        <begrep-id>.yaml
```

**Eksempel:**

```
src/linkml/
  oreg/
    begrepssamling-foretaksregisteret/
      build.yaml
      begrep/
        foretaksnavn.yaml
        nestleder.yaml
```

Begrep-YAML-filer inneheld éin `Begrep`-instans frå `skos-ap-no-schema`:

```yaml
# foretaksnavn.yaml
id: https://begrep.brreg.no/foretaksnavn
anbefalt_term:
  - foretaksnavn
har_definisjon:
  - https://begrep.brreg.no/def/foretaksnavn-nb
identifikator_literal: "https://begrep.brreg.no/foretaksnavn"
kontaktpunkt_vcard:
  - https://begrep.brreg.no/kontakt/begrepsansvarleg
utgjevar: https://data.norge.no/organizations/974760673
fagomrade:
  - https://psi.norge.no/los/tema/naring
```

**Automatisk aggregering:**

CI-scriptet `collect-concepts.sh` samlar alle begrep frå alle begrepssamlingane til ein 
organisasjon og genererer ein begrepskatalog under `src/linkml/begrepskatalog/<organisasjon>-begrepskatalog/`.

---

## Silver-annotasjonar (Digdir-regel 9, 10, 11)

Skjema som skal bruke `validation_policy: silver` eller høgare skal ha desse annotasjonane.
Nøkkelnamna svarar til `Informasjonsmodell`-slotsa i `modelldcat-ap-no-schema.yaml`:

| Annotasjon | Svarar til | Verdiformat |
|---|---|---|
| `annotations.utgiver` | `Informasjonsmodell.utgiver` (`dct:publisher`) | `https://data.norge.no/organizations/<orgnr>` |
| `annotations.endringsdato` | `Informasjonsmodell.endringsdato` (`dct:modified`) | ISO 8601-dato, t.d. `"2026-06-10"` |
| `annotations.utgivelsesdato` | `Informasjonsmodell.utgivelsesdato` (`dct:issued`) | ISO 8601-dato |
| `annotations.status` | `Informasjonsmodell.status` (`adms:status`) | ADMS Status-URI (sjå under) |

ADMS Status-verdiar:

| Status | URI |
|---|---|
| Under utarbeidelse | `http://purl.org/adms/status/UnderDevelopment` |
| Ferdigstilt | `http://purl.org/adms/status/Completed` |
| Foreldet | `http://purl.org/adms/status/Deprecated` |
| Trukket tilbake | `http://purl.org/adms/status/Withdrawn` |

CI genererer `Informasjonsmodell`-instansar for modellkatalogen frå desse annotasjonane.

---

## Kontrollerte vokabular — annotation-konvensjon

Slots som krev bruk av kontrollerte vokabular skal ha følgjande annotations:

| Annotation | Type | Krav | Forklaring |
|---|---|---|---|
| `gyldige_verdier` | `uri` | Obligatorisk | URI til det primære kontrollerte vokabularet |
| `vokabular_krav` | `skal` \| `bør` \| `kan` | Obligatorisk | Om bruk av vokabularet er obligatorisk, anbefalt eller valfri |
| `vokabular_pattern` | `regex` | Valfri | Regex-mønster for å validere URI-format av instansverdiar |
| `enum_referanse` | `EnumName` | Valfri | Namn på enum i same/importert skjema som dekkjer (delar av) vokabularet |
| `enum_dekning` | `full` \| `delvis` | Valfri | Om `enum_referanse` dekkjer heile vokabularet eller berre vanlegaste verdiar |
| `sekundare_vokabular` | `uri` | Valfri | URI til sekundært/alternativt vokabular som kan brukast |
| `sekundare_vokabular_krav` | `skal` \| `bør` \| `kan` | Valfri | Krav for sekundært vokabular |

**Prinsipp:**
- `range` vert **ikkje** endra — behald `range: Konsept`, `range: uri`, osv.
- `description` skal innehalde tydelig SKAL/BØR/KAN-formulering
- Annotations er maskinlesbare slik at `mcp-linkml-validator` kan validere at instansar brukar korrekte vokabular

**Eksempel (obligatorisk vokabular med enum):**
```yaml
tilgangsrettigheter:
  slot_uri: dct:accessRights
  range: Konsept
  multivalued: true
  description: >-
    Tilgangsrettar til ressursen. Verdien SKAL veljast frå EUs kontrollerte
    vokabular Access Right. Gyldige verdiar: PUBLIC (ope, ingen registrering),
    RESTRICTED (avgrensa tilgang), NON_PUBLIC (ikkje offentleg).
  annotations:
    gyldige_verdier: http://publications.europa.eu/resource/authority/access-right/
    vokabular_krav: skal
    vokabular_pattern: "^http://publications\\.europa\\.eu/resource/authority/access-right/(PUBLIC|RESTRICTED|NON_PUBLIC)$"
    enum_referanse: EUAccessRight
    enum_dekning: full
```

**Eksempel (anbefalt vokabular):**
```yaml
frekvens:
  slot_uri: dct:accrualPeriodicity
  range: Konsept
  description: >-
    Oppdateringsfrekvens for ressursen. Verdien BØR veljast frå EUs kontrollerte
    vokabular Frequency. Sjå enumerasjonen DCTFrequency i common-ap-no.
  annotations:
    gyldige_verdier: http://publications.europa.eu/resource/authority/frequency/
    vokabular_krav: bør
    enum_referanse: DCTFrequency
    enum_dekning: full
```

**Eksempel (primært + sekundært vokabular):**
```yaml
tema:
  slot_uri: dcat:theme
  range: Konsept
  multivalued: true
  description: >-
    Tema frå eit kontrollert vokabular. For norske offentlege datasett skal Los
    brukast som primærvokabular. Bruk hovudtema (https://psi.norge.no/los/tema/<namn>)
    og eventuelt undertema i tillegg. EuroVoc kan brukast som sekundærvokabular.
  annotations:
    gyldige_verdier: https://psi.norge.no/los/
    vokabular_krav: skal
    vokabular_pattern: "^https://psi\\.norge\\.no/los/(tema|ord|hendelse)/[a-z-]+(/[a-z-]+)*$"
    sekundare_vokabular: http://publications.europa.eu/resource/authority/eurovoc/
    sekundare_vokabular_krav: kan
```

**Validator-støtte:**
- **Bronze-policy:** Sjekkar at alle slots med `gyldige_verdier` har `vokabular_krav` og at SKAL/BØR/KAN i description matcher `vokabular_krav`
- **Silver-policy:** Validerer instansverdiar mot `vokabular_pattern` (dersom angitt)
- **Gold-policy:** Krev at alle instansverdiar validerer mot `vokabular_pattern` og er frå korrekt domene

---

## Sjå også

- [SCOPE.md](SCOPE.md) — kva repoet er, kva det ikkje er, og kva som høyrer heime her
- [PRINCIPLES.md](PRINCIPLES.md) — designprinsipp for modellering
- [CLAUDE.md](CLAUDE.md) — detaljerte arbeidsflytinstruksjonar for AI-assistentar
- [src/mcp-linkml-validator/policies/README.md](src/mcp-linkml-validator/policies/README.md) — fullstendig sjekkliste per policy-nivå
