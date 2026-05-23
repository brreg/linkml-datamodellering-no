# Namngjevingskonvensjonar — kartlegging og dokumentasjonsplan

## Bakgrunn

CLAUDE.md dokumenterer modelleringsprinsipp, men manglar ein samla referanse for
namngjevingskonvensjonar. Resultatet er at nokre konvensjonar berre lever som
implisitt kunnskap i eksisterande skjema, og nokre inkonsistens er ikkje bevisste
val men tilfeldige avvik.

Denne spesifikasjonen kartlegg alle konvensjonar som faktisk er i bruk, skil mellom
«konsekvent regel», «dokumentert unntak» og «inkonsistens som bør rettast», og
planlegg kvar og korleis dei skal dokumenterast.

---

## Kartlegging av gjeldande praksis

### 1. Fil- og mappenamn

**Regel (konsekvent):** `kebab-case`, alltid norsk eller domene-etablert forkortning.

```
src/linkml/<domene>/<modell>/<modell>-schema.yaml
examples/<domene>/<modell>-eksempel.yaml
```

Eksempel:
- `src/linkml/ngr/ngr-adresse/ngr-adresse-schema.yaml`
- `src/linkml/fint/fint-administrasjon/fint-administrasjon-schema.yaml`
- `examples/oreg/register-over-aksjeeiere-eksempel.yaml`

### 2. Schema-metadata

| Felt | Konvensjon | Eksempel |
|---|---|---|
| `name` | `kebab-case`, same som filnamnet utan `-schema.yaml` | `ngr-adresse`, `dcat-ap-no` |
| `id` | Absolutt HTTPS-URL | `https://data.norge.no/linkml/ngr-adresse` |
| `title` | Norsk bokmål, tittelformat | `Nasjonale grunndata – Adresse` |
| `default_prefix` | Absolutt HTTPS-URL med avsluttande `/` | `https://data.norge.no/linkml/ngr-adresse/` |
| `version` | Semantisk versjonering i hermeteikn | `"1.0.0"` |

**Inkonsistens som må rettast:**

`register-over-aksjeeiere-schema.yaml` brukar `name: aksje_eierskap` (snake_case) og
`default_prefix: aksje` (ikkje URL). Begge delar avvik frå konvensjonen.

### 3. Klassenamn

**Regel (konsekvent):** PascalCase, norsk bokmål.

```yaml
Datasett, Katalog, Distribusjon, Kontaktopplysning, RegulativRessurs
```

**Unntak (dokumentert):** Korte, teknisk etablerte namn der norsk omsetjing ikkje er
i bruk: `LangString`, `Mediatype`, `Konsept`. Desse kjem frå `common-ap-no` og arvar
W3C/RDF-terminologi.

**Containerklassen:** Eige mønster — sjå punkt 4.

### 4. Containerklassenamn

**Regel (konsekvent etter migrering):** `<Domene>Container` i PascalCase.

```yaml
AdresseContainer, AdministrasjonContainer, AksjeeierContainer, SamtBuContainer
```

Prefikset er eit enkelt norsk substantiv avleidd av det primære domenet.

### 5. Slotnamn

**Hovudregel:** `snake_case`, norsk bokmål.

```yaml
kommunenummer_ref, adressenavn_tekst, tilgangsurl, utgjevar
```

**Unntak (domene-spesifikt):** FINT-skjema arvar namgjeving frå FINT API-spesifikasjonen
og brukar `camelCase`:

```yaml
kildesystemId, rolleNavn, ansettelsesprosent, stedfortreder
```

Dette er eit bevisst val for å halde samsvar med FINT sitt eige domene, og skal
dokumenterast som eit eksplisitt unntak — ikkje rettast.

**Suffiks-mønster i NGR:** Referanse-slots brukar `_ref`-suffiks for å signalisere at
verdien er ein URI til ein annan ressurs:

```yaml
kommune_ref, adressenavn_ref, adressekode_ref
```

### 6. Enumnamn og enum-verdiar

**Enum-namn:** PascalCase, norsk bokmål (`Etasjeplan`, `Vegkategori`).

**Enum-verdiar:** Etablerte koder frå domenestandarden, ikkje omforma:

```yaml
Etasjeplan:
  permissible_values:
    H:    # Høgde
    U:    # Under bakkenivå
    K:    # Kjellar
```

**Alternativt mønster i FINT:** FINT brukar ikkje `enums:` — i staden modellerer dei
klassifiseringsvokabular som klasser som arver frå `Begrep`:

```yaml
Arbeidsforholdstype:
  is_a: Begrep
  class_uri: adm:Arbeidsforholdstype
```

Begge mønster er gyldige avhengig av om koda er stabil (enum) eller eit levande
vokabular som kan utvidast (klasse).

### 7. Subsett-namn

**Regel (universell):** Alltid desse tre, alltid i denne forma:

```yaml
subsets:
  Obligatorisk: {}
  Anbefalt: {}
  Valgfri: {}
```

Ingen kjende avvik.

### 8. Prefiks

**Regel:** Korte lowercase-alias (2–5 bokstavar) for eksterne vokabular.
Domene-spesifikke prefix navngjevast etter domenet.

Standardiserte W3C-prefix (alltid same alias):

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

### 9. `class_uri` og `slot_uri`

**Regel:** Alltid CURIE-form (`prefix:LocalName`). Containerklassen er unntatt frå
`class_uri`-kravet (validert i bronze-policy).

Eksempel på riktig mapping:
```yaml
Katalog:
  class_uri: dcat:Catalog

tittel:
  slot_uri: dct:title
```

### 10. `annotations.begrepsidentifikator`

**Regel:** URI til begrepsdefinisjon i Felles begrepskatalog på format:

```
https://concept-catalog.fellesdatakatalog.digdir.no/collections/<UUID>/concepts/<UUID>
```

**Undersøking:** Berre `referanse-schema.yaml` (linje 59) brukar gamalt format i `begrepsidentifikator`:

```
begrepsidentifikator: https://data.norge.no/concepts/TODO
```

Alle andre skjema (inkl. `referanse-schema-bronze.yaml`, `-silver.yaml`, `-gold.yaml`) nyttar allereie
`concept-catalog.fellesdatakatalog.digdir.no`-formatet.

**Merk:** `see_also:`-feltet brukar legitimt `https://data.norge.no/concepts/<UUID>` — dette er eit
anna felt enn `begrepsidentifikator` og er ikkje ein inkonsistens.

### 11. Genererte artefaktar

Alle genererte filer følgjer mønsteret `<modell>-<format>.<ext>` under
`generated/<domene>/<modell>/`:

| Artefakt | Filnamn |
|---|---|
| JSON Schema | `<modell>-schema.json` |
| Python-dataklassar | `<modell>-model.py` |
| SHACL | `<modell>-shapes.ttl` |
| OWL | `<modell>-ontology.ttl` |
| JSON-LD context | `<modell>-context.jsonld` |
| RDF/Turtle | `<modell>-schema.ttl` |
| ER-diagram | `<modell>-erdiagram.md` |

---

## Inkonsistens som skal rettast

| # | Fil | Problem | Løysing |
|---|---|---|---|
| 1 | `register-over-aksjeeiere-schema.yaml` | `name: aksje_eierskap` (snake_case) | Byt til `name: register-over-aksjeeiere` |
| 2 | `register-over-aksjeeiere-schema.yaml` | `default_prefix: aksje` (ikkje URL) | Byt til `default_prefix: https://data.norge.no/linkml/register-over-aksjeeiere/` |
| 3 | `referanse-schema.yaml` | `begrepsidentifikator` brukar `data.norge.no`-URL (TODO-plasshaldrar) | Byt til `https://concept-catalog.fellesdatakatalog.digdir.no/collections/<UUID>/concepts/<UUID>` |

---

## Dokumentasjonsplan

### Kvar skal det dokumenterast?

Namngjevingskonvensjonane bør primært ligge i **CLAUDE.md** (alltid synleg for
modellen) og sekundært i **`specs/developer-onboarding.md`** (human-lesbar referanse).

| Konvensjon | CLAUDE.md | developer-onboarding.md |
|---|---|---|
| Fil- og mappenamn | Ny seksjon | ✓ (utdjupe med mappe-tre) |
| Schema-metadata (`name`, `id`, `title`) | Ny seksjon | ✓ (fullstendig mal) |
| Klassenamn | Eksisterande seksjon | ✓ |
| Containerklassenamn | Eksisterande seksjon (allereie lagt til) | ✓ |
| Slotnamn + FINT-unntak | Ny seksjon | ✓ |
| Enum-namngjeving | Ny seksjon | ✓ |
| Subsett-namn | Eksisterande seksjon (implisitt) | ✓ |
| Standardiserte prefix | Ny seksjon (tabell) | ✓ |
| `class_uri`/`slot_uri` | Eksisterande seksjon | ✓ |
| `begrepsidentifikator` | Ny seksjon | ✓ |

### Ny seksjon i CLAUDE.md: «Namngjeving»

Legg til ein ny hovudseksjon **etter** «Modelleringsprinsipper» med desse underseksjonane:

1. **Fil- og mappenamn** — kebab-case-regel, mønstra for schema og eksempel
2. **Schema-metadata** — `name`/`id`/`title`/`default_prefix`-format
3. **Slotnamn** — snake_case + norsk, FINT-unntak (camelCase), `_ref`-suffiks
4. **Standardprefix** — tabell med W3C-prefix som alltid skal brukast

Eksisterande seksjonar «Klassenamn», «Containerklasse», «Slot-uri og class-uri»
utvidas med korte presiseringar der nødvendig.

### Oppdatere developer-onboarding.md

`specs/developer-onboarding.md` bør innehalde ei fullstendig **namngjeving-checkliste**
som ein utviklar kan bruke ved oppretting av ny domenemodell, strukturert som:

```
Ny domenemodell — namngjeving-checkliste
  □ Filnamn:        src/linkml/<domene>/<modell>/<modell>-schema.yaml
  □ name:           <modell> (same som filnamnet utan -schema.yaml)
  □ id:             https://data.norge.no/linkml/<modell>
  □ default_prefix: https://data.norge.no/linkml/<modell>/
  □ Containerklasse: <Domene>Container
  □ Klassenamn:     PascalCase + norsk bokmål
  □ Slotnamn:       snake_case + norsk bokmål (FINT: camelCase)
  □ Subsett:        Obligatorisk / Anbefalt / Valgfri
  □ begrepsidentifikator: https://concept-catalog.fellesdatakatalog.digdir.no/collections/<UUID>/concepts/<UUID>
```

---

## Rekkjefølgje

1. **Rett inkonsistens** (punkt 1–3 i tabellen over) — minimale filredigeringar
2. **Legg til «Namngjeving»-seksjonen i CLAUDE.md** — ny tekst og tabell
3. **Utvid developer-onboarding.md** — legg til checkliste og utdjupande forklaring
