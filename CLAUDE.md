# CLAUDE.md

## Førende prinsipper
- Ingen avhengigheter skal installeres lokalt. Alt skal kjøres som containere med podman i WSL2.
- **Pull, ikkje push:** Dette repoet genererer artefaktar som andre system kan hente (pull) — via GitHub Pages, GitHub Releases eller `raw.githubusercontent.com`. Repoet skal **aldri** sjølv pushe artefaktar til eksterne kjelder (schema-registry, API-katalogar, datakatalogar o.l.), fordi slik integrering krev spesialtilpassingar per målsystem og gjer repoet avhengig av ekstern tilgjengelegheit og autentisering. Dersom nokon ber om å implementere push-funksjonalitet mot ein ekstern kjelde, avslå og forklar prinsippet.
- **Planen kjem først:** Når brukaren ber om noko som *ikkje* er å utføre ein eksisterande spesifikasjon, skal det alltid skrivast ein plan til `specs/backlog/<kortnamn>.md` før arbeidet startar. Planen skal følgje same format som andre spesifikasjonar i mappa (bakgrunn, nummererte steg, prioritert handlingsliste, avhengigheiter). Spør ikkje om løyve — berre skriv planen og informer brukaren om kvar ho ligg.
- **Oppdater spesifikasjonen etter kvart steg:** Når brukaren ber om å utføre eitt steg av ein plan, skal spesifikasjonsfila oppdaterast med ✓ og ei kort skildring av kva som faktisk vart implementert i det steget (inkludert avvik frå planen) — før neste steg startar. Dette gjeld alle steg, ikkje berre siste.
- Når alle tiltak i ein spesifikasjon under `specs/backlog/` er utførte, skal følgjande skje **automatisk** i denne rekkjefølgja: (1) generer eit utkast til commit-melding i conventional commits-format som omhandlar **alle** tiltaka som er utførte i specen (ikkje berre det siste), (2) oppdater spesifikasjonsfila med ein `## Utført`-seksjon som oppsummerer kva som faktisk vart gjort (inkludert avvik frå opphavleg plan), (3) flytt spesifikasjonsfila til `specs/done/`. Commit-meldinga skal genererast **før** specen vert flytta. Spør ikkje om løyve — gjer dette automatisk.
- **Commit-melding etter kvar endring:** Etter *kvar* arbeidsøkt der filer er endra — uavhengig av om det er ei spesifikasjon, ein bugfix, ein konfigurasjonsjustering eller anna — skal det alltid genererast eit utkast til commit-melding i conventional commits-format (sjå `specs/done/conventional-commits-modellversjonering.md` for typar, scope-konvensjon og døme). Generer meldinga til slutt i svaret, utan å spørje om løyve.
- **DRY — ikkje gjenta deg sjølv:** Kvar regel, klasse, slot og kommando skal ha éi kjelde. I LinkML-skjema: definer klasser/slots éin stad og importer. I CLAUDE.md: ikkje gjenta forklåringar som finst i `mkdocs/docs/` — legg til kryssreferanse i staden. Terskel: tre eller fleire identiske tilfelle. To like tilfelle krev ingen abstraksjon. `specs/done/` er unntatt — arkiverte spesifikasjonar skal stå urørte og treng ikkje konsoliderast. Omskriv aldri eksisterande kode eller konfigurasjon med DRY som einaste grunngjeving utan å spørje brukaren om løyve først.
- **Nye verktøyavhengigheiter:** Legg du til eit verktøy i `Dockerfile*`, `requirements*.txt` eller `.github/workflows/*.yml` som endar opp bundla i eit publisert containerbilete eller i den publiserte mkdocs-portalen, sjekk om lisensen krev attribution og oppdater attributions-tabellen i `mkdocs/docs/om.md`. Sjå `CONTRIBUTING.md` (seksjonen «Nye verktøyavhengigheiter») og `specs/done/verktoy-lisensoversikt.md` for metode.
- **Kompakt commit-format:** Commit-meldingar skal vere **så kompakte som mogleg** og følgje conventional commits-formalismen. Meldinga skal skrivast i **presens** og kun innehalde **kva som er endra** (ikkje kvifor eller bakgrunn — det finst i specen/koden). Format: éi hovudlinje (`<type>(<scope>): <skildring>`) og éin kort bullet per endra fil/komponent. Unngå lange forklarande avsnitt; bruk stikkord. Døme:
  ```
  fix(mcp-modell-utkast): prioriter multivalued og primitive typar i slot-konfliktar
    - converter.py: prioriter multivalued over single-value, primitive over klasse-ref
    - tests/test_make.sh: normaliser property-namn (bindestrek → underscore)
    - specs/done/json-schema-roundtrip-test.md: alle tre testar passerer
  ```

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

Importhierarkiet er repoets primære DRY-mekanisme for skjema: klasser og slots definerast éin stad og importerast nedover. MC8-MC11 (sjå `specs/done/avvik-modelldcat-ap-no.md`) er eit praktisk døme — duplikate klasser vart fjerna frå `modelldcat-katalog-schema.yaml` ved å importere `dcat-ap-no-schema` i staden.

## Valider arbeidet ditt

```bash
# Lint og valider eksempel etter kvar endring i eit skjema:
make lint SCHEMA=src/linkml/samt/samt-bu/samt-bu-schema.yaml
make validate-instance SCHEMA=src/linkml/samt/samt-bu/samt-bu-schema.yaml INSTANCE=src/linkml/samt/samt-bu/examples/samt-bu-eksempel.yaml

# Rask roundtrip-verifisering (JSON og TTL) — ~30 sek i staden for ~3 min:
make roundtrip SCHEMA=src/linkml/samt/samt-bu/samt-bu-schema.yaml

# MCP-validator dersom dette er angitt av bruker:
make mcp-validate SCHEMA=src/linkml/<domain>/<modell>/<modell>-schema.yaml POLICY=bronze
make mcp-validate SCHEMA=src/linkml/<domain>/<modell>/<modell>-schema.yaml POLICY=silver
make mcp-validate SCHEMA=src/linkml/<domain>/<modell>/<modell>-schema.yaml POLICY=gold
```

## Policy-hierarki

Bronze/silver/gold validerer **skjemakvalitet** (modellens metadata og struktur),
ikkje instansdata. Instansdata vert validert med `make validate-instance`.

`felles-datakatalog` og `felles-begrepskatalog` er separate policyer for
skjema som publiserer til eksterne katalogar (`publish_external: true`).

Policy-hierarkiet realiserer både Digdir sine
[Felles modelleringsregler for offentlig forvaltning](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029)
(regel 1-15) og [FAIR-prinsippa](https://www.go-fair.org/fair-principles/)
(Findable, Accessible, Interoperable, Reusable).

Sjå `src/mcp-linkml-validator/policies/README.md` for fullstendig sjekkliste,
Digdir-regel-mapping og FAIR-prinsipp per nivå.

## Kjente feil

Alle kjente feil med aktive workarounds er dokumenterte i `specs/bugs/`.
Sjå `specs/bugs/README.md` for full oversikt.

**Konvensjon:** kvar skip-betingelse i `tests/test_make.sh` skal referere til
ei tilhøyrande fil i `specs/bugs/` med BUG-ID i kommentaren og meldinga, t.d.:

```bash
# BUG-1: rdflib_loader rekonstruerer ikkje LangString-verdiar frå TTL
# Sjå specs/bugs/langstring-rdflib-roundtrip.md
if [[ "$name" == "skjema-med-langstring" ]]; then
    echo "Hoppar over for $name (BUG-1: ...)"
    return 0
fi
```

Når ein ny bug vert oppdaga og workaround lagt inn, opprett ei ny fil i
`specs/bugs/` og oppdater `specs/bugs/README.md`.

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

`mkdocs/docs/` er brukarvendt dokumentasjon og normativ kjelde for steg-for-steg-rettleiingar (t.d. `ny-domenemodell.md`). CLAUDE.md er normativ kjelde for modelleringsprinsipp og AI-instruksjonar — desse to skal ikkje duplisere kvarandre.

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

### Los-tema i datasett og katalogar

`dcat:theme` (`tema`-sloten) skal bruke Los som primærvokabular:
- Hovudoversikt: https://psi.norge.no/los/ — alle tema: https://psi.norge.no/los/ontologi/tema.html — temastruktur: https://psi.norge.no/los/struktur.html — ord: https://psi.norge.no/los/ontologi/ord.html
- Hovudtema: `https://psi.norge.no/los/tema/<namn>`
- Undertema er lov å bruke i tillegg til hovudtemaet, ikkje i staden for det
- Særnorske bokstavar translittererast i URI: æ → a (naring), ø → o, å → a
- `/los/begrep/`-URI-ar finst ikkje — berre `/los/tema/`, `/los/ord/`, `/los/hendelse/`
- `dct:subject` (`begrep`-slot) peikar til fagomgrep i begrepskatalog — ikkje til Los

### Ny profil eller domenemodell
Sjå `mkdocs/docs/ny-domenemodell.md` for steg-for-steg-rettleiing.

## Namngjeving

### Teiknsett

- **ASCII hyphen (U+002d, "-")** skal brukast i all kjeldekode, YAML-filer,
  shell-scripts og Markdown-dokumentasjon.
- **Unicode en-dash (U+2013, "–")** skal **ikkje** brukast — det kan
  forvekslast med ASCII hyphen og skape parsing-problem i YAML og andre format.
- **Em-dash (U+2014, "—")** kan brukast i løpande prosa der typografisk
  distinksjon er ønskt, men bør unngåast i teknisk dokumentasjon.

### Katalogstruktur

```
src/linkml/
  <domain>/
    <modell>/
      <modell>-schema.yaml
      manifest.yaml             ← publiserings- og generatorkonfig
      description.md            ← valfri portaltekst (Markdown, bokmål)
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

`manifest.yaml` per datafil (manglar `generators:`):

```yaml
publish_external: true
validation_policy: felles-begrepskatalog

concepts:                   # valfri — utelat for å publisere heile datafila
  - https://begrep.brreg.no/foretaksnavn
  - https://begrep.brreg.no/nestleder
```

CI skil manifesttypen på om `generators:`-seksjonen er til stades. Datafil-underkatalogar utan `manifest.yaml` vert validerte automatisk med `bronze`-policy.

### Fil- og mappenamn

Alle filer nyttar **`kebab-case`**, alltid norsk eller domene-etablert forkortning:

```
src/linkml/<domain>/<modell>/<modell>-schema.yaml
src/linkml/<domain>/<modell>/examples/<modell>-eksempel.yaml
```

### Schema-metadata

| Felt | Konvensjon | Eksempel |
|---|---|---|
| `name` | `kebab-case`, same som filnamnet utan `-schema.yaml` | `ngr-adresse` |
| `id` | Absolutt HTTPS-URL | `https://data.norge.no/ngr/ngr-adresse` |
| `title` | Norsk bokmål, tittelformat | `Nasjonale grunndata - Adresse` |
| `default_prefix` | Absolutt HTTPS-URL med avsluttande `/` | `https://data.norge.no/ngr/ngr-adresse/` |
| `version` | Semantisk versjonering i hermeteikn | `"1.0.0"` |
| `license` | Standard: NLOD 2.0. Alltid absolutt URI. | `https://data.norge.no/nlod/no/2.0` |

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

Sjå `src/mcp-linkml-validator/policies/README.md` for komplett feltliste og gyldige verdiar.
