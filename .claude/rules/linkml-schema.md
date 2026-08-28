---
name: linkml-schema
description: LinkML skjemakonvensjonar — slots vs attributes, lenking fremfor inlining, containerklasse-reglar, katalogstruktur, manifestformat, translitterering av norske bokstavar, slotnavn, standardprefix og silver-annotasjonar. Lastast automatisk ved arbeid med filer under src/linkml/.
paths:
  - "src/linkml/**"
---

## Modelleringsprinsipper

### Slots, ikke attributes
Alle domenemodellklasser modellerer eigenskapane sine som globale slots under `slots:` på toppnivå i skjemaet. Klasser refererer til slots via `slots:`-lista. Klassespesifikke innskrenkingar (`required`, `in_subset` o.l.) ligg i `slot_usage`.

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
Alle klasser og slots har eksplisitt `class_uri` / `slot_uri` som mapper til dei korrekte RDF-vokabulara (dcat:, dct:, foaf:, vcard: osv.). `tree_root`-containerklasser er unntatt frå kravet om `class_uri`.

**Ekstern ekvivalent er føretrekt bruk av `class_uri`.** Finst det ein etablert,
publisert ekstern ontologi-term som klassen semantisk svarar til (W3C DCAT/DCT/
FOAF/SKOS/VCard/ORG/PROV, EU sine kjernevokabular — Core Business Vocabulary
`m8g:`/`rov:`, Core Location Vocabulary `locn:`, Core Person Vocabulary — schema.org,
eller domenespesifikke standardar som ModelDCAT-AP-NO/`dcatno:`, DQV/`dqv:`,
FINT sitt API-namnerom `schema.fintlabs.no` o.l.), skal `class_uri` peike dit.
Berre når **ingen** rimeleg ekstern ekvivalent finst, brukast skjemaet sitt
eige lokale prefiks (matchar `default_prefix`) som fallback.

Grunngjeving: LinkML sin eigen metamodell-definisjon av `class_uri` seier
«The URI may come from any namespace» — lokalt prefiks er difor teknisk
gyldig, men LinkML genererer alt automatisk ein lokal URI frå `default_prefix`
når `class_uri` er utelaten. Eit eksplisitt lokalt `class_uri` gir difor
**inga ny RDF-semantikk** utover kva LinkML uansett ville generert — verdien
av å setje `class_uri` eksplisitt ligg i å *overstyre* fallback-en med ei
ekte, ekstern mapping. Sjå `specs/done/undersokelse-class-uri-kryssreferansar.md`
for grunnlaget for denne regelen.

Ynskjer du å uttrykkje ein **lausare**, ikkje-forpliktande semantisk likskap
til eit eksternt omgrep utan å gjere klassen "til" det omgrepet (t.d. når
det eksterne omgrepet er nærskyldt, men ikkje presist nok til å vere
`class_uri`), bruk `exact_mappings`/`close_mappings` i staden for — desse
to felta har ulikt føremål og skal ikkje blandast saman.

### Obligatorisk/anbefalt/valgfri
`slot_usage` med `in_subset` brukes for å markere om en egenskap er `Obligatorisk`, `Anbefalt` eller `Valgfri` i henhold til spesifikasjonen. `required: true` settes kun på obligatoriske egenskaper.

### Flerspråklige strenger
`LangString` (type `rdf:langString`) brukes for alle egenskaper som er definert som `rdf:langString` i spesifikasjonen (tittel, beskrivelse, nøkkelord osv.).

### Containerklasse
Alle toppnivå domenemodellar skal ha éin containerklasse med `tree_root: true`. Containerklassen er inngangspunktet for validering og serialisering.

Containerklassen brukar **`attributes:`** (ikkje `slots:`) for å referere til kvar klasse som kan serialiserast i tilhøyrande datafil:

```yaml
Containerklasse:
  tree_root: true
  attributes:
    datasett:          # attributtnavn i fleirtal
      range: Datasett
      multivalued: true
      inlined: true
      inlined_as_list: true
```

- Klassenavnet følgjer mønsteret **`<Domene>Container`** i PascalCase (t.d. `AdresseContainer`, `AksjeeierContainer`) — aldri berre `Containerklasse`
- Attributtnavna skrives alltid i **fleirtal** (t.d. `datasett`, `katalogar`, `aktørar`)
- `range` må peike på ein klasse definert i skjemaet eller importerte skjema
- Ingen `slot_uri` — containerattributtar er strukturelle, ikkje semantiske
- Containerklassen treng ikkje `class_uri` (unntatt frå kravet per bronze-policy)
- AP-NO-modellar og fair-modellar skal ikkje ha eigen containerklasse
- **Containerattributt skal alltid bruke `inlined`/`inlined_as_list`** — dette er ein ufravikeleg regel, også når `range`-klassen har `identifier: true`. Containerklassen sitt føremål er å vere eit sjølvstendig, komplett eksportdokument; dette gjeld ubunde av om target-klassen elles ville vore lenka (via URI) etter prinsippet "Lenking fremfor inlining" utanfor containeren. Sjå `specs/done/inlining-konvensjon.md` (R5) og `bugs/inlined-as-list-rdflib-roundtrip.md` (BUG-2) for grunngjeving og ein kjend, akseptert konsekvens av regelen.
- **`range` på eit `inlined`/`inlined_as_list`-containerattributt skal alltid vere ein konkret klasse** — aldri ei abstrakt eller mixin-klasse med fleire konkrete subklasser delt i same liste. Bruk eige containerattributt per konkret subklasse i staden for éi delt, polymorf liste. Sjå `bugs/polymorphic-inlined-list-yaml-loader.md` (BUG-8) for konsekvensen av å bryte denne regelen (krasj i `linkml-convert`/`gen-rdf`, sjølv om `make validate-instance` godkjenner instansen).

### Los-tema i datasett og katalogar

`dcat:theme` (`tema`-sloten) skal bruke Los som primærvokabular:
- Hovudoversikt: https://psi.norge.no/los/ — alle tema: https://psi.norge.no/los/ontologi/tema.html — temastruktur: https://psi.norge.no/los/struktur.html — ord: https://psi.norge.no/los/ontologi/ord.html
- Hovudtema: `https://psi.norge.no/los/tema/<navn>`
- Undertema er lov å bruke i tillegg til hovudtemaet, ikkje i staden for det
- Særnorske bokstavar translittererast i URI: æ → a (naring), ø → o, å → a
- `/los/begrep/`-URI-ar finst ikkje — berre `/los/tema/`, `/los/ord/`, `/los/hendelse/`
- `dct:subject` (`begrep`-slot) peikar til fagomgrep i begrepskatalog — ikkje til Los

### Ny profil eller domenemodell
Sjå `mkdocs/docs/kom-i-gang/ny-domenemodell.md` for steg-for-steg-rettleiing.

## Navngjeving

### Katalogstruktur

```
src/linkml/
  <domain>/
    <modell>/
      <modell>-schema.yaml
      build.yaml             ← publiserings- og generatorkonfig
      description.md            ← valfri portaltekst (Markdown, bokmål)
      examples/
        <modell>-eksempel.yaml
      data/                     ← berre for skjema med produksjonsdata
        <katalog>/
          <katalog>.yaml
          build.yaml         ← datafil-manifest

generated/                      ← byggoutput, ikkje kjeldekode
tests/
```

### Manifestformat

`build.yaml` per skjema (har `generators:`-seksjon):

```yaml
publish_external: false   # true for å publisere til ekstern katalog
validation_policy: silver        # bronze / silver / gold / felles-datakatalog / felles-begrepskatalog

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

`build.yaml` per datafil (manglar `generators:`):

```yaml
publish_external: true
validation_policy: felles-begrepskatalog

concepts:                   # valfri — utelat for å publisere heile datafila
  - https://begrep.brreg.no/foretaksnavn
  - https://begrep.brreg.no/nestleder
```

CI skil manifesttypen på om `generators:`-seksjonen er til stades. Datafil-underkatalogar utan `build.yaml` vert validerte automatisk med `bronze`-policy.

### Fil- og mappenavn

Alle filer nyttar **`kebab-case`**, alltid norsk eller domene-etablert forkortning:

```
src/linkml/<domain>/<modell>/<modell>-schema.yaml
src/linkml/<domain>/<modell>/examples/<modell>-eksempel.yaml
```

### Schema-metadata

| Felt | Konvensjon | Eksempel |
|---|---|---|
| `name` | `kebab-case`, same som filnavnet utan `-schema.yaml` | `ngr-adresse` |
| `id` | Absolutt HTTPS-URL | `https://data.norge.no/ngr/ngr-adresse` |
| `title` | Norsk bokmål, tittelformat | `Nasjonale grunndata - Adresse` |
| `default_prefix` | Absolutt HTTPS-URL med avsluttande `/` | `https://data.norge.no/ngr/ngr-adresse/` |
| `version` | Semantisk versjonering i hermeteikn | `"1.0.0"` |
| `license` | Standard: NLOD 2.0. Alltid absolutt URI. | `https://data.norge.no/nlod/no/2.0` |

### Norske bokstavar i identifikatorar

Særnorske bokstavar skal **translittererast** i alle identifikatorar — klassenavn, slotnavn, attributtnavn og URI-lokaldel:

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

### Slotnavn

Hovudregel: **`snake_case`**, norsk bokmål (t.d. `kommunenummer_ref`, `adressenavn_tekst`).

**Format:** `snake_case` tillét berre små bokstavar (`a-z`), tal (`0-9`) og understrek (`_`). **Bindestreker er ikkje tillate** — bruk samansette ord utan separasjon (t.d. `epost`, `epostadresse`) eller understrek (`mobilnummer_utgaar`). Dette vert håndheva av bronze-policy-sjekken `slot_names_snake_case`.

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

**AP-NO-profil-skjema skal ikkje ha `begrepsidentifikator`** på klassane sine. Klassane der (t.d. `Datasett`, `Katalog`, `Distribusjon`) er definerte av W3C/EU-standardar (DCAT, SKOS o.l.), ikkje av norske omgrep i Felles begrepskatalog. `begrepsidentifikator` er berre aktuelt for domenemodell-skjema med norskspråklege fagomgrep.

### Silver-annotasjonar (Digdir-regel 9, 10, 11)

Skjema med `validation_policy: silver` eller høgare skal ha desse annotasjonane.
Nøkkelnavna svarar til `Informasjonsmodell`-slotsa i `modelldcat-ap-no-schema.yaml`:

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

Sjå `src/mcp-linkml-validator/policies/README.md` for komplett feltliste og gyldige verdiar.
