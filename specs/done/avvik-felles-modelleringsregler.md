# Kartlegging: Avvik mot Felles modelleringsregler for offentlig forvaltning

**Kjelde:** [digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029)  
**Utgjevar:** Digitaliseringsdirektoratet, v1.0, juni 2022  
**MCP-referanse:** `src/mcp-linkml-validator/policies/README.md` — full dekningstabell

---

## Bakgrunn

MCP-validatoren i dette repoet (`src/mcp-linkml-validator/`) implementerer allereie
sjekkar for alle 15 modelleringsreglane — anten som automatiske kontroller (bronze/silver/gold)
eller med eksplisitt dokumentasjon av kvifor regelen ikkje lar seg maskinelt evaluere.

Denne kartlegginga fokuserer difor på **to typar gap**:

1. **Etterlevingsgap** — reglar validatoren fangar som sjemaa *likevel ikkje oppfyller*
2. **Policy-gap** — reglar der automatisk kontroll ikkje er innført, og kva dette inneber i praksis

### Compliance-oversikt per skjema (before state)

| Felt | AP-NO-skjema (6) | Domenemodell-skjema (17) | Totalt |
|---|---|---|---|
| `license:` | 0/6 | 0/17 | **0/23** |
| `version:` | 5/6 ✓ | 13/17 ✓ | 18/23 |
| `annotations.status` | 6/6 ✓ | 14/17 ✓ | 20/23 |
| `annotations.utgiver` | 6/6 ✓ | 14/17 ✓ | 20/23 |
| `annotations.endringsdato` | 6/6 ✓ | (ikkje kravd for bronze) | 6/6 ✓ |
| `annotations.begrepsidentifikator` på klasser | 0/107 klasser | 39/∞ (alle TODO) | ~0 reelle |

---

## Vurdering per regel

### Regel 1 — Forståelighet ✓

> *Modellen, dens modellelementer og egenskaper skal gis forståelige navn og gode beskrivelser.*

**Bronze-sjekk:** `schema.name`, `schema.title` (error); `schema.description`, `class.description`, `slot.description` (warning)

**Status:** Alle skjema har `name`, `title` og `description` på schema-nivå ✓.  
Klasse- og slot-skildringar er gjennomgåande til stades (94 `description:`-felt i dcat-ap-no åleine) ✓.

**Gap:** Slotnamn i FINT-skjema er på engelsk og camelCase (arva frå FINT API-spec).
Desse er unntekne frå `snake_case`-sjekken i bronze-policy. Regelkonformiteten er
pragmatisk: FINT arvar frå ein ekstern spesifikasjon, men namna kan vere uforståelege
for norsk offentleg målgruppe utan bakgrunnskunnskap om FINT.

---

### Regel 2 — Meningsfullhet ✓

> *Navn på modellen og dens modellelementer og egenskaper skal gjenspeile innholdet.*

**Bronze-sjekk:** `schema.title` (error)

**Status:** Alle skjema har meningsfylte titlar på norsk bokmål ✓. Klassenamn
som `Datasett`, `Katalog`, `Adresse`, `Aksjeeier` er intuitive for målgruppa ✓.

**Gap:** `register-over-aksjeeiere-schema.yaml` har `id: https://example.no/ontology/aksje-eierskap`
— dette er misvisande (sjå `avvik-peikarar-til-offentlege-ressursar.md` tiltak PO1).

---

### Regel 3 — Navne- og skrivekonvensjoner ✓

> *Følg anbefalte eller standardiserte navne- og skrivekonvensjoner.*

**Bronze-sjekk:** `class_names_pascal_case`, `slot_names_snake_case` (warning)

**Status:** Alle klasser er PascalCase ✓. Alle AP-NO- og domenemodell-slots er
snake_case ✓. FINT-slots er camelCase, korrekt unntekne ✓.

**Gap:** Translitterering av særnorske bokstavar er dokumentert i `CLAUDE.md`
men ikkje maskinelt kontrollert. Ein kan registrere ein klasse som `Aktør` (feil)
i staden for `Aktoer` (rett) utan at bronze-sjekken flaggar det.

---

### Regel 4 — Identifiserbarhet ✓ / ⚠️

> *Modellen, dens modellelementer og egenskaper skal ha en persistent identifikator.*

**Bronze-sjekk:** `schema.id` (HTTPS-URI, error); `schema.default_prefix` (HTTPS-URI + `/`, error);
`class_uri` på alle klasser (warning); `slot_uri` på alle globale slots (warning);
identifikator-slot på alle klasser (warning)

**Status:** Alle skjema har `id` og `default_prefix` som HTTPS-URI-ar ✓.
Alle AP-NO-klasser og -slots har `class_uri`/`slot_uri` ✓.

**Gap — register-over-aksjeeiere har feil schema-ID:**
```yaml
id: https://example.no/ontology/aksje-eierskap   # feil
default_prefix: https://data.norge.no/oreg/register-over-aksjeeiere/  # korrekt
```
Schema-ID bryt kravet om persistente URI-ar (sjå tiltak PO1 i `avvik-peikarar-til-offentlege-ressursar.md`).

**Gap — identifikator-slot manglar i containerklassar:** Containerklassar (`tree_root: true`)
er unntekne frå `class_uri`- og identifikator-sjekken, noko som er korrekt. Men nokre hjelpeklassar
utan `tree_root` manglar `identifier: true` — dette vert fanga av bronze-warning, og status
varierer per skjema.

---

### Regel 5 — Visualisering ⚠️

> *Modellen skal uttrykkes i et modelleringsspråk som gir en god, visuell representasjon.*

**Policy:** *Ikkje automatisk evaluert* — ER-diagram generert av `make erdiagram`, PlantUML via `make plantuml`.

**Status:** Alle 22 skjema med `manifest.yaml` genererer ER-diagram (Mermaid) og
PlantUML-diagram ✓. Desse er publisert på GitHub Pages dokumentasjonsportalen ✓.

**Gap — regelen seier UML-klassediagram, ikkje Mermaid ER-diagram:**
Digdir-regelen refererer spesifikt til UML-klassediagram som anbefalte format.
Mermaid ER-diagram og PlantUML-diagram er i UML-stil men er ikkje formelt ISO 19501
(UML 2.5) kompatible. I praksis dekkjer diagramma behovet, men dette er eit
avvik mot bokstaven i regelen.

**Gap — ingen validering av at diagram faktisk er generert:** Bronze-policy
sjekkar ikkje om `erdiagram`-artefaktet eksisterer i `generated/`. Ein kan ha
`erdiagram: false` i manifest utan å få feil.

**Tiltak:** Vurder å leggje til ein `make check-artifacts`-jobb i CI som verifiserer
at forventa artefaktar finst i `generated/` etter bygg.

---

### Regel 6 — Modularitet ⚠️

> *Antall modellelementer skal beholdes på et håndterbart nivå.*

**Policy:** *Ikkje automatisk evaluert.*

**Status:** Importhierarkiet (`common → AP-NO → domenemodell`) er eksplisitt modulært ✓.
Dei fleste skjema har handterlege klassetal.

**Gap — ingen hard grense for klassetal per skjema:**
`fint-utdanning-schema.yaml` har om lag 73 klasser — noko over ein rimeleg
«handterleg» terskel. `fint-administrasjon-schema.yaml` har om lag 35 klasser.
Ingen av dei er splitta i undermodular.

MCP-validatoren har ingen sjekk for dette, og `CLAUDE.md` gir heller ingen
rettleiing om maksimalt klassetal per skjema.

**Tiltak:** Legg til ein bronze-warning når eit skjema har fleire enn 50 klasser.
Sjå PI7 i `specs/backlog/avvik-prinsipper-informasjonsmodeller.md`.

---

### Regel 7 — Tilgjengeliggjøring ✗

> *Modellen skal være fritt tilgjengelig på internett.*

**Bronze-sjekk:** `schema.license` (warning)

**Status: Kritisk etterlevingsgap — `license:`-feltet manglar i samtlege 23 skjema:**

```yaml
# Manglar i alle skjema — bør leggjast til:
license: https://data.norge.no/nlod/no/2.0
```

Dette er bronze-warning som aldri er retta. Utan `license:` er det maskinelt
umogeleg å fastslå lisensvilkåra for skjema-gjenbruk.

Modellane *er* tilgjengelege på GitHub Pages og via `raw.githubusercontent.com` (open kildekode),
men dette er ikkje maskinelt deklarert i skjema-metadataen.

**Prioritet:** Høg — enkelt å rette, og er einaste augneblinkelege bronze-warning.

#### Lisensalternativ og dokumentasjonskonvensjon

Tre lisensalternativ er relevante for offentlege informasjonsmodellar i Noreg:

| Lisens | URI | Brukstilfelle |
|---|---|---|
| **NLOD 2.0** | `https://data.norge.no/nlod/no/2.0` | Standardlisens for norske forvaltningsorgan. Krev kjeldetilskrivning. Anbefalt av Digitaliseringsdirektoratet og lagt til grunn for andre data.norge.no-ressursar. |
| **CC BY 4.0** | `https://creativecommons.org/licenses/by/4.0/` | Internasjonalt anerkjend open lisens, kompatibel med NLOD. Eigna der internasjonalt samarbeid eller EU-interoperabilitet er eit mål. |
| **CC0 1.0** | `https://creativecommons.org/publicdomain/zero/1.0/` | Public domain-dediksjon utan vilkår. Eigna for basisvokabular og hjelpeskjema (t.d. `common-ap-no`) der terskelen for gjenbruk bør vere absolutt minimal. |
| **MIT** | `https://opensource.org/licenses/MIT` | Kortfatta open kjeldekode-lisens med minimal kjeldetilskrivningskrav. Eigna for skjema som primært vert konsumert som kode (t.d. Python-genererte artefaktar), men er ikkje spesifikt tilpassa offentlege data eller RDF-vokabular. |
| **Apache 2.0** | `https://www.apache.org/licenses/LICENSE-2.0` | Open kjeldekode-lisens med eksplisitt patentklausul. Eigna for skjema som distribuerast saman med programvare, men er som MIT ikkje spesifikt tilpassa offentlege data eller RDF-vokabular. |

**Tilrådd val:** NLOD 2.0 for alle skjema i dette repoet. Dette samsvarar med
Digitaliseringsdirektoratets standardvilkår for offentleg informasjon og er den
naturlege lisensen for modellane som publiserast under `data.norge.no`-domenet.

**Dokumentasjonskonvensjon** — `license:`-feltet plasserast etter `version:` i schema-seksjonen:

```yaml
name: dcat-ap-no
id: https://data.norge.no/ap-no/dcat-ap-no
version: "1.0.0"
license: https://data.norge.no/nlod/no/2.0
```

Dersom eit enkeltskjema av særlege grunnar nyttar ein annan lisens (t.d. CC0 for
basisvokabular), skal dette dokumenterast med ein kommentar i sjølve schemafila.

---

### Regel 8 — Maskinprosserbarhet ✓ / ⚠️

> *Modellen bør være tilgjengelig i et definert og åpent maskinprosesserbart format.*

**Bronze-sjekk:** `class_uri`, `slot_uri` (indirekte — sikrar at RDF-serialisering er meiningsfull)

**Status:** Dei fleste skjema genererer eit breitt spekter av maskinlesbare format ✓:

| Format | Dekning |
|---|---|
| JSON-LD kontekst | 21/22 manifest |
| SHACL | 20/22 manifest |
| JSON Schema | 22/22 manifest |
| OWL | 20/22 manifest |
| RDF/Turtle | 22/22 manifest |
| Protobuf | 20/22 manifest |

**Gap — `brreg-begrepskatalog` og `brreg-modellkatalog` manglar SHACL og OWL:**
```yaml
shacl: false   # brreg-begrepskatalog/manifest.yaml og brreg-modellkatalog/manifest.yaml
owl: false
```
Dei to produksjonskatalogane manglar maskinlesbar validering (SHACL) og ontologirepresentasjon (OWL).

**Gap — ingen content negotiation for schema-URI-ar:** `https://data.norge.no/ap-no/dcat-ap-no`
returnerer HTML, ikkje RDF (sjå `avvik-peikarar-til-offentlege-ressursar.md` avvik 4).

---

### Regel 9 — Datering ✓ / ⚠️

> *Modellen skal dateres.*

**Bronze-sjekk:** `schema.version` (warning)  
**Silver-sjekk:** `annotations.endringsdato` (warning)

**Status:** Alle skjema utanom fire har `version:`-felt:

| Skjema som manglar `version:` | Merknad |
|---|---|
| `common-ap-no-schema.yaml` | Kritisk — basislaget for alle AP-NO-profil |
| `xkos-ap-no-schema.yaml` | Sjå XK3 i `avvik-xkos-ap-no.md` |
| `enhetsregisteret-bvrinn-schema.yaml` | Registerskjema |
| `samt-bu-schema.yaml` | Samhandlingsmodell |

Alle AP-NO-skjema har `annotations.endringsdato` ✓.
Domenemodellane er ikkje underlagt silver-policy og er difor ikkje sjekka for `endringsdato`.

**Gap — `utgivelsesdato` er ikkje sjekka:** Bronze- og silver-policy sjekkar ikkje
`annotations.utgivelsesdato`. Fleire skjema har dette feltet, men det er ikkje kravd.

---

### Regel 10 — Ansvar ✓ / ⚠️

> *Ansvaret for modellen og dens innhold skal være klart og tydelig.*

**Silver-sjekk:** `annotations.utgiver` (warning)

**Status:** 20/23 skjema har `annotations.utgiver` ✓.

**Skjema som manglar `annotations.utgiver`:**
- `brreg-begrepskatalog-schema.yaml`
- `brreg-modellkatalog-schema.yaml`
- `register-over-aksjeeiere-schema.yaml`

For desse er det uklart kven som er ansvarleg utgjevar — Brreg, repoet, eller ein annan.

**Gap — `CODEOWNERS.md` koplinga ikkje reflektert i schema-metadata:**
`CODEOWNERS.md` dokumenterer at Brreg eig sine modellar, men dette er ikkje maskinlesbart
knytt til `annotations.utgiver` i skjemaet.

---

### Regel 11 — Modellstatus ✓ / ⚠️

> *Modellen skal angis med en modellstatus.*

**Silver-sjekk:** `annotations.status` (warning), gyldige ADMS-verdiar validerte

**Status:** 20/23 skjema har `annotations.status` ✓.

**Skjema som manglar `annotations.status`:**
- `brreg-begrepskatalog-schema.yaml`
- `brreg-modellkatalog-schema.yaml`
- `register-over-aksjeeiere-schema.yaml`

Alle tre er produksjonsskjema med data — status burde minst vere `Completed`.

---

### Regel 12 — Sammenhenger mellom modeller ⚠️

> *Dersom modellen har en sammenheng med én eller flere informasjonsmodeller,
> skal disse forholdene beskrives.*

**Policy:** *Ikkje automatisk evaluert* — dokumenterast manuelt via `er_profil_av`, `erstatter` o.l.

**Status:** `modelldcat-ap-no-schema.yaml` modellerer relasjonar mellom informasjonsmodellar ✓
(`er_profil_av`, `erstatter`, `gjelder_for`, `er_del_av`). Strukturen er til stades.

**Gap — `brreg-modellkatalog` dekkjer berre 2 av 23 skjema:**
Katalogen inneheld berre to `Informasjonsmodell`-instansar (`ngr-virksomhet` og
`register-over-aksjeeiere`). Dei resterande 21 skjema — inkludert alle AP-NO-profilane
— er ikkje representerte i nokon katalog.

**Gap — ingen relasjonsfelt er utfylte:**
Feltet `er_profil_av` (for profil-relasjonar) er ikkje utfylt for nokon av dei to
instansane. `dcat-ap-no-schema.yaml` er t.d. ein profil av EU sin DCAT-AP — dette
er ikkje maskinlesbart dokumentert i katalogen.

```yaml
# Manglar i brreg-modellkatalog-instansane:
informasjonsmodellar:
  - id: https://brreg.no/modellkatalogar/brreg-modellkatalog/ngr-virksomhet
    # er_profil_av: mangler
    # erstatter: mangler
```

**Tiltak:** Utvid `brreg-modellkatalog` til å inkludere alle AP-NO-profilar og
domenemodellane med korrekte relasjonsfelt. Sjå MC2 i `avvik-modelldcat-ap-no.md`.

---

### Regel 13 — Begreper ✗

> *Dokumenter modellelementer og egenskaper ved bruk av begreper.*

**Bronze-sjekk:** `annotations.begrepsidentifikator` på alle klasser (warning)

**Status: Kritisk etterlevingsgap — `begrepsidentifikator` er nær fråverande:**

| Skjema | Klasser med `begrepsidentifikator` | Merknad |
|---|---|---|
| Alle AP-NO-skjema (6) | 0 av ~107 klasser | Ingen referansar |
| `enhetsregisteret-bvrinn` | 5 av ~? klasser | Alle brukar `TODO` som UUID |
| Alle andre domenemodell-skjema | 0 | — |

Brreg har byrja å leggje inn `begrepsidentifikator` i bvrinn-skjema, men alle 5
er placeholder-verdiar som ikkje peiker på reelle omgrep:
```yaml
annotations:
  begrepsidentifikator: https://concept-catalog.fellesdatakatalog.digdir.no/collections/TODO
```

Dette bryt Digdir-regel 13 fundamentalt: modellelementa er ikkje knytte til
godkjende omgrep i Felles begrepskatalog.

**Tiltak:** Sjå PI3 i `avvik-prinsipper-informasjonsmodeller.md`.  
**Prioritet:** Middels — krev koordinering med Brreg sin begrepskatalog.

---

### Regel 14 — Gjenbruk ✓

> *Gjenbruk modellelementer og egenskaper i stedet for å definere nye.*

**Policy:** *Ikkje automatisk evaluert.*

**Status:** Gjenbruk er grundig implementert i repoet:
- `common-ap-no-schema` gir felles basisklasar/-slots til alle AP-NO-profil ✓
- `fint-common-schema` er felles for alle FINT-domenemodellane ✓
- Domenemodellane `importerer` AP-NO-profil-ar (ingen copy-paste) ✓
- `CLAUDE.md` dokumenterer importprinsippet eksplisitt ✓

**Gap — ingen validering av at gjenbruk faktisk skjer:**
Det er mogleg å definere ein klasse `Datasett` i ein domenemodell utan å importere
`dcat-ap-no-schema` — validatoren vil ikkje fange dette. Bronze-policy sjekkar
ikkje om eit skjema som bruker DCAT-konsept faktisk importerer DCAT-AP-NO.

---

### Regel 15 — Standardiserte datatyper ✓ / ⚠️

> *Bruk standardiserte eller avtalte primitive datatyper.*

**Policy:** *Ikkje automatisk evaluert* — LinkML arvar XSD-typar via `linkml:types`.

**Status:** Alle primitive datatypar i skjemaet brukar XSD-standardar via LinkML:
`string`, `integer`, `boolean`, `date`, `datetime`, `uri`, `uriorcurie` ✓.

**Gap — `tidsrom_start`/`tidsrom_slutt` i `xkos-ap-no` brukar `dct:startDate`:**
`dct:startDate` finst ikkje i DC Terms-namespacet. Korrekt URI er `dcat:startDate`
(DCAT 3). Sjå XK1 i `avvik-xkos-ap-no.md` — dette er ein konkret brot mot
standardiserte datatypar/eigenskapar.

**Gap — ingen sjekk for `range: string` på felt som burde bruke `uriorcurie`:**
Fleire slots (t.d. `tema` i `dcat-ap-no`) har `range: string` der `uriorcurie`
ville gitt betre typesikkerheit. Bronze-policy fangar ikkje dette.

---

## Samandrag: Regelstatus per skjematype

| Regel | AP-NO (6 skjema) | FINT (7 skjema) | NGR (4 skjema) | Oreg/Samt (3 skjema) | Katalogar (2 skjema) |
|---|---|---|---|---|---|
| 1 Forståelighet | ✓ | ✓ | ✓ | ✓ | ✓ |
| 2 Meningsfullhet | ✓ | ✓ | ✓ | ⚠️ (oreg: example.no-ID) | ✓ |
| 3 Navnekonvensjoner | ✓ | ✓ (unntak) | ✓ | ✓ | ✓ |
| 4 Identifiserbarhet | ✓ | ✓ | ✓ | ⚠️ (feil schema-ID) | ✓ |
| 5 Visualisering | ✓ | ✓ | ✓ | ✓ | ✓ |
| 6 Modularitet | ✓ | ⚠️ (fint-utdanning: 73 kl.) | ✓ | ✓ | ✓ |
| 7 Tilgjengelighet | **✗ (ingen license)** | **✗** | **✗** | **✗** | **✗** |
| 8 Maskinprosserbarhet | ✓ | ✓ | ✓ | ✓ | ⚠️ (mangler SHACL/OWL) |
| 9 Datering | ✓ (xkos: ⚠️ versjon) | ✓ | ✓ | ✓ | ✓ |
| 10 Ansvar | ✓ | ✓ | ✓ | ⚠️ (register-aksje: mangler) | **✗ (mangler utgiver)** |
| 11 Modellstatus | ✓ | ✓ | ✓ | ⚠️ (register-aksje: mangler) | **✗ (mangler status)** |
| 12 Sammenhenger | ⚠️ (katalog dekker 2/23) | ✗ (ikkje i katalog) | ⚠️ (2 i katalog) | ✗ | N/A |
| 13 Begreper | **✗ (0 ref.)** | **✗** | **✗** | ⚠️ (TODO-placeholder) | **✗** |
| 14 Gjenbruk | ✓ | ✓ | ✓ | ✓ | ✓ |
| 15 Datatyper | ⚠️ (xkos: dct:startDate) | ✓ | ✓ | ✓ | ✓ |

---

## Prioritert tiltaksliste

| # | Tiltak | Regel | Fil(ar) | Avhengigheit |
|---|---|---|---|---|
| 1 | ✓ Lagt til `license: https://data.norge.no/nlod/no/2.0` i alle 25 skjema (23 opphavlege + `referanse-schema.yaml` + `cpsv-ap-no-schema.yaml`). Plassert etter `version:` der det finst, etter `title:` i dei 4 skjema utan `version:`. | 7 | Alle `*-schema.yaml` | — |
| 2 | ✓ Lagt til `version: "1.0.0"` i alle 4 skjema som mangla det (`common-ap-no`, `xkos-ap-no`, `bvrinn`, `samt-bu`). Plassert rett før `license:`. | 9 | common, xkos-ap-no, bvrinn, samt-bu | — |
| 3 | ✓ Lagt til `annotations.utgiver` (Brreg: `974760673`) og `annotations.status: Completed` i alle 3 skjema (`brreg-begrepskatalog`, `brreg-modellkatalog`, `register-over-aksjeeiere`). | 10, 11 | brreg-begrepskatalog, brreg-modellkatalog, register-over-aksjeeiere | — |
| 4 | ✓ Fiksa `id` frå `https://example.no/ontology/aksje-eierskap` til `https://data.norge.no/oreg/register-over-aksjeeiere`. Fiksa òg `aksje:`-prefikset frå `example.no/ontology/aksje#` til `https://data.norge.no/oreg/register-over-aksjeeiere/` (prefikset var definert men ikkje brukt i `class_uri`/`slot_uri`). | 2, 4 | `register-over-aksjeeiere-schema.yaml` | — |
| 5 | ✓ Aktivert `shacl: true` og `owl: true` i begge manifest-filer. Roundtrip-test for begrepskatalog OK. | 8 | `brreg-begrepskatalog/manifest.yaml`, `brreg-modellkatalog/manifest.yaml` | — |
| 6 | **Må utførast manuelt.** Fiks `begrepsidentifikator` TODO-plasshalderar i bvrinn: søk opp kvar kandidatklasse på `https://data.norge.no/concepts?q=<term>` og erstatt `TODO` med faktisk URI. Sjå kandidattabell i seksjonen «Begrepsidentifikator-kandidatar for bvrinn-skjema» nedanfor. | 13 | `bvrinn-schema.yaml` | Brreg begrepskatalog-avklaring |
| 7 | ~~Legg til `begrepsidentifikator` på nøkkelklasser i AP-NO~~ — **Avvist.** AP-NO-klassane (`Datasett`, `Katalog`, `Distribusjon` o.l.) er definerte av W3C/EU-standardar, ikkje norske fagomgrep. `begrepsidentifikator` er berre aktuelt for domenemodell-skjema. Regelen er dokumentert i `CLAUDE.md`. | 13 | — | — |
| 8 | ✓ Legg til `ngr-virksomhet` i `brreg-modellkatalog` — allereie til stades i katalogen. Katalogen inneheld `ngr-virksomhet` og `register-over-aksjeeiere`. `enhetsregisteret-bvrinn` er ikkje ein del av dette tiltaket. Modellar eigd av andre organisasjonar (Digdir, Kartverket, Novari o.l.) skal ikkje inngå. | 12 | `brreg-modellkatalog.yaml` | — |
| 9 | ✓ Fiksa `dct:startDate` → `dcat:startDate` og `dct:endDate` → `dcat:endDate` i `tidsrom_start`/`tidsrom_slutt`. Lagt til `dcat:`-prefiks i skjemaet. Roundtrip OK. | 15 | `xkos-ap-no-schema.yaml` | — |
| 10 | ✓ Innført `class_count_limit`-warning (>50 klasser) i `bronze.yaml` og `server.py`. Verifisert: `fint-utdanning` triggar (90 klasser inkl. importerte), `dcat-ap-no` er stille. README og Digdir-regel 6-status oppdatert. | 6 | `bronze.yaml`, `server.py`, `policies/README.md` | — |
| 11 | ✓ Fastset lisenskonvensjon: NLOD 2.0 er vald som standardlisens. Lagt til i sjekklista i `mkdocs/docs/ny-domenemodell.md`. Sjå Regel 7 — Lisensalternativ og dokumentasjonskonvensjon for grunngjeving og alternativa (CC BY 4.0, CC0 1.0, MIT, Apache 2.0). | 7 | `mkdocs/docs/ny-domenemodell.md` | Tiltak 1 (kjem før) |

---

## Begrepsidentifikator-kandidatar for bvrinn-skjema

Alle 38 klassar i `enhetsregisteret-bvrinn-schema.yaml` har `begrepsidentifikator: https://concept-catalog.fellesdatakatalog.digdir.no/collections/TODO`.
Brreg sin lokale begrepskatalog i repoet (`brreg-begrepskatalog.yaml`) inneheld berre tre omgrep
(`foretaksnavn`, `nestleder`, `aksjeklasser`) — ingen treff mot bvrinn-klassane.

Søk-URL for Felles begrepskatalog: `https://data.norge.no/concepts?q=<term>`  
Katalog-API: `https://concept-catalog.fellesdatakatalog.digdir.no`

### Klassar med truleg kandidat i Felles begrepskatalog

Desse klassane svarar til veletablerte nasjonale omgrep og bør ha treff:

| Klasse | Søketerm | Sannsynleg eigar av omgrep |
|---|---|---|
| `Virksomhet` | virksomhet | Brønnøysundregistra / Digdir |
| `VirksomhetsinformasjonHovedenhet` | hovedenhet, enhet | Brønnøysundregistra |
| `VirksomhetsinformasjonUnderenhet` | underenhet | Brønnøysundregistra |
| `Forretningsadresse` | forretningsadresse | Brønnøysundregistra |
| `Postadresse` | postadresse | Brønnøysundregistra / Posten |
| `Stedsadresse` | stedsadresse | Brønnøysundregistra |
| `Beliggenhetsadresse` | beliggenhetsadresse | Brønnøysundregistra |
| `Vegadresse` | vegadresse | Kartverket / SSB |
| `Postboksadresse` | postboksadresse | Brønnøysundregistra |
| `InternasjonalAdresse` | internasjonal adresse | Brønnøysundregistra |
| `Adressenummer` | adressenummer | Kartverket |
| `Matrikkelnummer` | matrikkelnummer | Kartverket |
| `Kontaktopplysning` | kontaktopplysning, kontaktinformasjon | Brønnøysundregistra / Digdir |
| `Telefonnummer` | telefonnummer | Digdir / Brønnøysundregistra |
| `Mobilnummer` | mobilnummer | Digdir / Brønnøysundregistra |
| `Rolle` | rolle | Brønnøysundregistra |
| `Rolleinnehaver` | rolleinnehaver | Brønnøysundregistra |
| `Rolletypegruppe` | rolletype | Brønnøysundregistra |
| `Prokura` | prokura | Brønnøysundregistra / Lovdata |
| `Prokurabestemmelse` | prokura | Brønnøysundregistra |
| `Signaturrett` | signaturrett | Brønnøysundregistra / Lovdata |
| `Signaturrettsbestemmelse` | signaturrett | Brønnøysundregistra |
| `Person` | person | Folkeregisteret / Digdir |
| `Aktivitet` | aktivitet, næringsaktivitet | Brønnøysundregistra / SSB |
| `Omdanning` | omdanning | Brønnøysundregistra |
| `Innsender` | innsender | Brønnøysundregistra |

### Klassar utan truleg nasjonal kandidat

Desse er interne tekniske eller BVINN-spesifikke klasser som truleg ikkje finst i Felles begrepskatalog:

| Klasse | Merknad |
|---|---|
| `Innrapportering` | BVINN-spesifikk innsendingsprosess |
| `Ansvarsandel` | Intern brøkrepresentasjon |
| `Broek` | Teknisk hjelpestruktur |
| `Fagsystemreferanse` | IT-systemreferanse |
| `FagsystemId` | IT-systemreferanse |
| `EierskifteAktivitet` | BVINN-spesifikk hendingstype |
| `DelerEierskifte` | BVINN-spesifikk hendingstype |
| `TypeAktivitet` | Intern kodeliste |
| `Rollesett` | Intern grupperingsstruktur |
| `SignaturberettigetEllerProkurist` | Intern kombinasjonsklasse |
| `Foretaksinformasjon` | Intern aggregeringsklasse |
| `Varslingsadresse` | Kan overlappe kontaktopplysning |
| `Gebyransvarlig` | BVINN-spesifikk part |
| `Signering` | Teknisk signeringsprosess |

### Neste steg

1. Søk opp kvar kandidatklasse i `https://data.norge.no/concepts?q=<søketerm>`
2. Verifiser at funne omgrep er frå godkjend samling i Felles begrepskatalog
3. Oppdater `begrepsidentifikator` i skjemaet med faktisk URI på forma:
   `https://concept-catalog.fellesdatakatalog.digdir.no/collections/<UUID>/concepts/<UUID>`
4. For klasser utan nasjonal kandidat: vurder om Brreg bør opprette eigne omgrep i sin begrepskatalog

---

## Merknader

### Policy-dekning er god — etterlevinga er svakare

Repoet har eit gjennomtenkt valideringssystem som eksplisitt refererer til
alle 15 Digdir-reglane. Det systematiske gapet er at fleire warning-nivå-sjekkar
(særleg `license:`, `begrepsidentifikator`) er aldri retta — dei er implementerte
som *warnings*, men dei er aldri behandla.

Ein enkel prioritering er å rette alle *warnings som ikkje krev ekstern koordinering*
(tiltak 1–5 over) i éin commit, og behandle `begrepsidentifikator` (tiltak 6–7)
som eit eige prosjekt som krev begrepskatalog-avklaring med Brreg.

### Reglar 5, 14 og 15 er reelt oppfylte

Regel 5 (Visualisering), 14 (Gjenbruk) og 15 (Datatyper) er vurdert å vere
reelt oppfylte i repoet sjølv om dei ikkje er automatisk evaluerte. Diagramma
dekkjer behovet (sjølv om dei ikkje er formell UML), gjenbruk er implementert
konsekvent, og XSD-datatypar vert brukt overalt bortsett frå éin feil i xkos-ap-no.

### Regel 12 krev strategisk prioritering

Det å registrere alle 23 skjema i modellkatalogen med korrekte relasjonsfelt
(`er_profil_av`, `erstatter`, `gjelder_for`) er eit større prosjekt. Det treng
avklaring av kva som skal vere i Brreg sin katalog vs. eventuelle andre katalogar.
Sjå MC2 i `avvik-modelldcat-ap-no.md` for bakgrunn.
