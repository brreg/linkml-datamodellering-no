# CLAUDE.md

## Førende prinsipper
- Ingen avhengigheter skal installeres lokalt. Alt skal kjøres som containere med podman i WSL2.

## LinkML Importhierarki

```
linkml:types
    ↓
common-ap-no          ← bare AP-NO-profilene importerer denne direkte
    ↓
dcat-ap-no / dqv-ap-no / skos-ap-no / …
    ↓
domenemodeller        ← importerer AP-NO-profilene, ikke common-ap-no direkte

fint-common           ← bare FINT-domenemodellene importerer denne
    ↓
fint-administrasjon / fint-arkiv / …

oreg-modeller         ← offentlige registre (importerer AP-NO-profil(er) etter behov)

fair-metadata         ← kan importeres av alle domenemodeller
```

## Valider arbeidet ditt

```bash
# Lint og valider eksempel etter kvar endring i eit skjema:
./tests/validate_schema.bash ./src/linkml/samt/samt-bu/samt-bu-schema.yaml ./src/linkml/samt/samt-bu/examples/samt-bu-eksempel.yaml

# MCP-validator dersom dette er angitt av bruker:
make mcp-validate SCHEMA=src/linkml/<domene>/<modell>/<modell>-schema.yaml POLICY=bronze
make mcp-validate SCHEMA=src/linkml/<domene>/<modell>/<modell>-schema.yaml POLICY=silver
make mcp-validate SCHEMA=src/linkml/<domene>/<modell>/<modell>-schema.yaml POLICY=gold
```

## Dokumentasjonsportal (mkdocs)

`mkdocs/mkdocs.yml` vert **automatisk regenerert** av `mkdocs/publish.sh` (Steg 4)
kvar gong `make publish` køyrer. Endringar gjort direkte i `mkdocs.yml` vert
overskrivne ved neste publisering.

**Sannkjelda for nav-menyen er `mkdocs/publish.sh`**, ikkje `mkdocs.yml`.

- Nye rettleiingssider (`mkdocs/docs/*.md`) må leggast til i heredoc-blokka i
  `publish.sh` (leit etter `nav:` → `- Rettleiingar:`)
- Domene og skjema vert lagt til automatisk frå `generated/`-strukturen — ikkje
  rediger desse manuelt
- Statisk innhald (`mkdocs/docs/` utanom genererte domene-katalogar) vert aldri
  sletta av `publish.sh`

## Modelleringsprinsipper

### Skriftspråk

Repoet nyttar to skriftspråk med klart skilde domene:

| Domene | Språk | Gjeld |
|---|---|---|
| Modellering | **Norsk bokmål** | Klassenamn, slotnamn, skildringar og kommentarar i `.yaml`-skjema |
| Dokumentasjon | **Nynorsk** | README-filer, mkdocs-sider, spesifikasjonar i `specs/` |

Bokmål i modellering følgjer terminologien i norske offentlege standardar (DCAT-AP-NO, SKOS-AP-NO m.fl.) som er skrivne på bokmål. Unntaket er tekniske omgrep fastsette i ein spesifikasjon (t.d. `dcat:Dataset` → `Datasett`).

### Slots, ikke attributes
Alle domenemodellklassar modellerer eigenskapane sine som globale slots under `slots:` på toppnivå i skjemaet. Klasser refererer til slots via `slots:`-lista. Klassespesifikke innskrenkingar (`required`, `in_subset` o.l.) ligg i `slot_usage`.

**Unntaket er containerklassen** (`tree_root: true`): her skal kvar klasse-referanse modellerast som eit inline `attribute` direkte under containerklassen — ikkje som ein global slot. Containerklassen er eit serialiseringsankerpunkt, ikkje ein semantisk klasse, og attributtane hennar treng ikkje `slot_uri`.

```yaml
# Riktig — domeneklasse brukar globale slots
slots:
  tittel:
    slot_uri: dct:title
    range: string

classes:
  Datasett:
    slots:
      - tittel
    slot_usage:
      tittel:
        required: true

# Riktig — containerklassen brukar attributes
classes:
  Containerklasse:
    tree_root: true
    attributes:
      datasett:
        range: Datasett
        multivalued: true
        inlined: true
        inlined_as_list: true

# Feil — domeneklasse brukar attributes
classes:
  Datasett:
    attributes:
      tittel:
        slot_uri: dct:title
        range: string

# Feil — containerklassen brukar globale slots
slots:
  datasett:
    range: Datasett
    slot_uri: ex:datasett
    multivalued: true
    inlined: true
    inlined_as_list: true
```

### Lenking fremfor inlining
Alle klasser som kan opptre selvstendig får et `id`-slot med `identifier: true` og `range: uriorcurie`. Referanser til andre klasser har **ikke** `inlined: true` (som er standard når målklassen har en identifikator). Dette sikrer at instanser refereres med URI i stedet for å bygges inn.

### Klassenavn
Norske bokmålsnavn brukes for alle klasser (f.eks. `Datasett`, `Katalog`, `Distribusjon`). Hjelpeklasser for W3C-vokabulartermer kan bruke kortere engelske navn (`Begrep`, `Spraak`, `Mediatype`).

### Slot-uri og class-uri
Alle klasser og slots har eksplisitt `class_uri` / `slot_uri` som mapper til de korrekte RDF-vokabularene (dcat:, dct:, foaf:, vcard: osv.). `tree_root`-containerklasser er unntatt fra kravet om `class_uri`.

### Obligatorisk/anbefalt/valgfri
`slot_usage` med `in_subset` brukes for å markere om en egenskap er `Obligatorisk`, `Anbefalt` eller `Valgfri` i henhold til spesifikasjonen. `required: true` settes kun på obligatoriske egenskaper.

### Flerspråklige strenger
`LangString` (type `rdf:langString`) brukes for alle egenskaper som er definert som `rdf:langString` i spesifikasjonen (tittel, beskrivelse, nøkkelord osv.).

### Containerklasse
Alle toppnivå domenemodeller skal ha éin containerklasse med `tree_root: true`. Containerklassen er inngangspunktet for validering og serialisering.

Containerklassen brukar **`attributes:`** (ikkje `slots:`) for å referere til kvar klasse som kan serialiserast i tilhøyrande datafil:

```yaml
Containerklasse:
  tree_root: true
  attributes:
    datasett:          # attributtnamn i fleirtal
      range: Datasett
      multivalued: true
      inlined: true
      inlined_as_list: true
```

- Klassenamnet følgjer mønsteret **`<Domene>Container`** i PascalCase (t.d. `AdresseContainer`, `AksjeeierContainer`) — aldri berre `Containerklasse`
- Attributtnamna skrives alltid i **fleirtal** (t.d. `datasett`, `katalogar`, `aktørar`)
- `range` må peike på ein klasse definert i skjemaet eller importerte skjema
- Ingen `slot_uri` — containerattributtar er strukturelle, ikkje semantiske
- Containerklassen treng ikkje `class_uri` (unntatt frå kravet per bronze-policy)
- AP-NO-modellar og fair-modellar skal ikkje ha eigen containerklasse

### Endringer i koderepoet
Forsøk alltid å utføre minimale endringer som kun løser den spesifikke oppgava.

### Ny profil eller domenemodell
Sjå `mkdocs/docs/ny-domenemodell.md` for steg-for-steg-rettleiing.

## Namngjeving

### Katalogstruktur

```
src/linkml/
  <domene>/
    <modell>/
      <modell>-schema.yaml
      manifest.yaml             ← publiserings- og generatorkonfig
      examples/
        <modell>-eksempel.yaml
      data/                     ← berre for skjema med produksjonsdata
        <katalog>/
          <katalog>.yaml
          manifest.yaml         ← datafil-manifest

generated/                      ← byggoutput, ikkje kjeldekode
tests/
```

### Manifestformat

`manifest.yaml` per skjema (har `generators:`-seksjon):

```yaml
publish_external: false   # true for å publisere til ekstern katalog
data_policy: silver        # bronze / silver / gold / felles-datakatalog / felles-begrepskatalog

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

`manifest.yaml` per datafil (manglar `generators:`):

```yaml
publish_external: true
data_policy: felles-begrepskatalog

concepts:                   # valfri — utelat for å publisere heile datafila
  - https://begrep.brreg.no/foretaksnavn
  - https://begrep.brreg.no/nestleder
```

CI skil manifesttypen på om `generators:`-seksjonen er til stades. Datafil-underkatalogar utan `manifest.yaml` vert validerte automatisk med `bronze`-policy.

### Fil- og mappenamn

Alle filer nyttar **`kebab-case`**, alltid norsk eller domene-etablert forkortning:

```
src/linkml/<domene>/<modell>/<modell>-schema.yaml
src/linkml/<domene>/<modell>/examples/<modell>-eksempel.yaml
```

### Schema-metadata

| Felt | Konvensjon | Eksempel |
|---|---|---|
| `name` | `kebab-case`, same som filnamnet utan `-schema.yaml` | `ngr-adresse` |
| `id` | Absolutt HTTPS-URL | `https://data.norge.no/ngr/ngr-adresse` |
| `title` | Norsk bokmål, tittelformat | `Nasjonale grunndata – Adresse` |
| `default_prefix` | Absolutt HTTPS-URL med avsluttande `/` | `https://data.norge.no/ngr/ngr-adresse/` |
| `version` | Semantisk versjonering i hermeteikn | `"1.0.0"` |

### Norske bokstavar i identifikatorar

Særnorske bokstavar skal **translittererast** i alle identifikatorar — klassenamn, slotnamn, attributtnamn og URI-lokaldel:

| Bokstav | Erstatning |
|---|---|
| æ / Æ | ae / Ae |
| ø / Ø | oe / Oe |
| å / Å | aa / Aa |

Dette gjeld i `.yaml`-skjema og datafiler. `title`, `description` og andre fritekstfelt er unntatt — der er norske bokstavar tillate.

```yaml
# Riktig
classes:
  Aktoer:          # Aktør → Aktoer
    class_uri: ex:Aktoer
slots:
  utgjevar_id:     # ingen særnorske her — OK som det er

# Feil
classes:
  Aktør:
    class_uri: ex:Aktør
```

### Slotnamn

Hovudregel: **`snake_case`**, norsk bokmål (t.d. `kommunenummer_ref`, `adressenavn_tekst`).

**Unntak — FINT-skjema:** arvar namgjeving frå FINT API-spesifikasjonen og brukar `camelCase`
(t.d. `kildesystemId`, `rolleNavn`). Dette er eit bevisst val, ikkje ein feil.

**`_ref`-suffiks i NGR:** referanse-slots som held ein URI til ein annan ressurs nyttar `_ref`-suffiks
(t.d. `kommune_ref`, `adressenavn_ref`).

### Standardprefix

Desse W3C-aliasa skal alltid brukast slik — aldri andre alias for same namespace:

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

### `annotations.begrepsidentifikator`

URI til begrepsdefinisjon i Felles begrepskatalog:

```
https://concept-catalog.fellesdatakatalog.digdir.no/collections/<UUID>/concepts/<UUID>
```

(`see_also:` nyttar legitimt `https://data.norge.no/concepts/<UUID>` — det er eit anna felt.)
