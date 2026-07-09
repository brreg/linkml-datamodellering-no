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

## Sjå også

- [SCOPE.md](SCOPE.md) — kva repoet er, kva det ikkje er, og kva som høyrer heime her
- [PRINCIPLES.md](PRINCIPLES.md) — designprinsipp for modellering
- [CLAUDE.md](CLAUDE.md) — detaljerte arbeidsflytinstruksjonar for AI-assistentar
- [src/mcp-linkml-validator/policies/README.md](src/mcp-linkml-validator/policies/README.md) — fullstendig sjekkliste per policy-nivå
