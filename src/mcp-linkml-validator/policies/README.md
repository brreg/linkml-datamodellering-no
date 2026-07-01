# Policyer for mcp-linkml-validator

Sjekkane i bronze-, silver- og gold-policyane realiserer både
[Felles modelleringsregler for offentlig forvaltning](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029)
(Digitaliseringsdirektoratet, v1.0, juni 2022) og
[FAIR-prinsippa](https://www.go-fair.org/fair-principles/) (Findable, Accessible, Interoperable, Reusable).

---

## Digdir-reglar og FAIR-prinsipp — dekningsgrad

| # | Namn | Kort skildring | Dekt av | FAIR |
|---|---|---|---|---|
| 1 | **Forståelighet** | Namn og skildringar er forståelege for målgruppa | Bronze: `title` (error), `description` (warning) | F2 |
| 2 | **Meiningsfullheit** | Namn speglar innhald og formål | Bronze: `title` (error) | F2 |
| 3 | **Navne- og skrivekonvensjoner** | PascalCase for klassar, snake_case/camelCase for eigenskapar | Bronze: `class_names_pascal_case`, `slot_names_snake_case` (warning) | — |
| 4 | **Identifiserbarheit** | Persistente URI-ar for modell, element og eigenskapar | Bronze: `id`, `default_prefix` (HTTPS-URI) (error); `class_uri`, `slot_uri`, identifikator-slot (warning) | F1, F3 |
| 5 | **Visualisering** | Modell tilgjengeleg med god visuell representasjon | *Ikkje evaluert* — ER-diagram vert generert av `make erdiagram`, men ikkje validert | — |
| 6 | **Modularitet** | Handterleg mengde modellelement per modul | Bronze: `class_count_limit` — warning om skjemaet har fleire enn 50 klasser | — |
| 7 | **Tilgjengeleggjering** | Modell fritt tilgjengeleg på nett med open lisens | Bronze: `license` (warning) | R1.1 |
| 8 | **Maskinprosserbarheit** | Modell tilgjengeleg i opne, maskinlesbare format | Bronze: `class_uri`, `slot_uri` (indirekte, via regel 4-sjekken) | I1, I2 |
| 9 | **Datering** | Modell er datert med publiserings-, endrings- og gyldigheitsdato | Bronze: `version` (warning); Silver: `annotations.endringsdato` (warning) | F4, R1.3 |
| 10 | **Ansvar** | Eigarskap og innhaldsansvar for modellen er tydeleg | Silver: `annotations.utgiver` (warning) | R1.2 |
| 11 | **Modellstatus** | Modellen har ein eksplisitt status (under utarbeiding, ferdig, forelda …) | Silver: `annotations.status` (warning) | R1.3 |
| 12 | **Sammenhenger mellom modeller** | Samanhengar med andre modellar er skildra | *Ikkje evaluert* — dokumenterast manuelt via `er_profil_av`, `erstatter` o.l. i modellkatalogen | F3 |
| 13 | **Begreper** | Modellelement og -eigenskapar er knytte til omgrep | Bronze: `annotations.begrepsidentifikator` på alle klasser (warning) | A2 |
| 14 | **Gjenbruk** | Eksisterande modellelement vert gjenbrukt framfor nydefinisjoner | *Ikkje evaluert* — best practice, ikkje maskinelt sjekkbart | I3 |
| 15 | **Standardiserte datatyper** | Primitive datatypar er standardiserte (XSD, RDFS) | *Ikkje evaluert* — LinkML arvar XSD-typar via `linkml:types` | I1 |

> **Merk:** Regel 5, 12, 14 og 15 let seg ikkje automatisk validere berre frå skjemastruktur.
> Dei vert handterte gjennom verktøy (ER-diagram), konvensjonar (CLAUDE.md) og manuell gjennomgang.

---

## To typar validering

Policyfilene her er brukte til to ulike føremål:

**Skjemakvalitet (bronze / silver / gold)**  
Sjekkar at eit LinkML-skjema (`.yaml`-fila i `src/linkml/`) held eit visst
kvalitetsnivå: metadata, namngjeving, URI-ar, begrepsreferansar osv.  
Køyrast med `make mcp-validate SCHEMA=... POLICY=bronze`.

**Publiseringskonformitet (felles-datakatalog / felles-begrepskatalog)**  
Sjekkar at eit skjema er i samsvar med krava til ei bestemt ekstern katalog.
Brukt for skjema der `publish_external: true` i manifest.

---

## Nivå for skjemakvalitet

| Nivå | Krav | Digdir-reglar | FAIR-prinsipp |
|---|---|---|---|
| `bronze` | Grunnleggande metadata og modelleringskvalitet (dette repoets baseline) | 1, 2, 3, 4, 6, 7, 8, 13 | F1, F2, F3 (warning), I1 (warning), R1.1 (warning), A2 (warning) |
| `silver` | Bronze + AP-NO-konformitet og livssyklusmetadata | 1–4, 7–11, 13 | Bronze + R1.2, R1.3 |
| `gold` | Silver + FAIR F1–R1.3: full semantisk interoperabilitet | 1–4, 7–11, 13 | F1–F4, I1–I2, R1.1–R1.3, A2 (alle error) |

Kvart nivå arvar krava frå nivåa under (`silver` arvar `bronze` osv., via `extends:`).

---

## Bronze-sjekkliste

Grunnleggjande strukturkrav. Eit skjema som passerer bronse er syntaktisk korrekt og har nødvendig metadata.

| Sjekk | Alvor | Digdir-regel | FAIR |
|---|---|---|---|
| `schema.id` til stades | error | 4 — Identifiserbarheit | F1 |
| `schema.id` er HTTP(S)-URI | error | 4 — Identifiserbarheit | F1 |
| `schema.name` til stades | error | 1 — Forståelighet | — |
| `schema.title` til stades | error | 1 — Forståelighet, 2 — Meiningsfullheit | F2 |
| `schema.default_prefix` til stades | error | 4 — Identifiserbarheit | — |
| `schema.default_prefix` er absolutt HTTPS-URI med avsluttande `/` | error | 4 — Identifiserbarheit | — |
| `schema.description` til stades | warning | 1 — Forståelighet | F2 |
| `schema.version` til stades | warning | 9 — Datering | F4 |
| `schema.license` til stades | warning | 7 — Tilgjengeleggjering | R1.1 |
| Skjema har ikkje fleire enn 50 klasser (unntatt `tree_root`) | warning | 6 — Modularitet | — |
| Alle klassenamn startar med stor bokstav (PascalCase) | warning | 3 — Navne- og skrivekonvensjoner | — |
| Alle slotnamn er snake_case (berre `a-z`, `0-9`, `_` — **ikkje bindestreker**) | warning | 3 — Navne- og skrivekonvensjoner | — |
| Alle klasser (unntatt `tree_root`) har `class_uri` | warning | 4 — Identifiserbarheit, 8 — Maskinprosserbarheit | F3, I1 |
| Alle globale slots har `slot_uri` | warning | 4 — Identifiserbarheit, 8 — Maskinprosserbarheit | I1 |
| Alle klasser (unntatt `tree_root`) har identifikator-slot | warning | 4 — Identifiserbarheit | F1 |
| Alle klasser (unntatt `tree_root`) har `annotations.begrepsidentifikator` | warning | 13 — Begreper | A2 |

> **`snake_case`-format:** Slotnamn kan berre innehalde små bokstavar (`a-z`), tal (`0-9`) og understrek (`_`). **Bindestreker er ikkje tillate** — bruk samansette ord utan separasjon (t.d. `epost`, `epostadresse`) eller understrek (`mobilnummer_utgaar`).
>
> FINT-skjema er unntekne frå snake_case-sjekken — dei arvar camelCase frå FINT API-spesifikasjonen.

---

## Silver-sjekkliste (i tillegg til bronze)

Arvar bronse. Legg til livssyklusmetadata og krav frå DCAT-AP-NO og DQV-AP-NO for domenemodeller i norsk offentleg sektor.

### Livssyklusmetadata

| Sjekk | Alvor | Digdir-regel | FAIR |
|---|---|---|---|
| `schema.annotations.utgiver` — URI på forma `https://data.norge.no/organizations/<orgnr>` | warning | 10 — Ansvar | R1.2 |
| `schema.annotations.endringsdato` — ISO 8601-dato | warning | 9 — Datering | R1.3 |
| `schema.annotations.status` — ADMS Status-URI | warning | 11 — Modellstatus | R1.3 |

Gyldige verdiar for `annotations.status`: `http://purl.org/adms/status/UnderDevelopment`, `Completed`, `Deprecated`, `Withdrawn`.

Annotasjonsnøklane svarar til `Informasjonsmodell`-slots i `modelldcat-ap-no-schema.yaml`
(Digdir regel 10 og 8 — Maskinprosserbarheit via ModellDCAT-AP-NO).  
`make update-modellkatalog` genererer `Informasjonsmodell`-instansar for modellkatalogen frå desse annotasjonane.

### Klasse-slot-krav (obligatoriske per DCAT-AP-NO / DQV-AP-NO)

Alle brot gir `error`.

| Klasse | Påkravd slot (`slot_uri`) | Digdir-regel | FAIR |
|---|---|---|---|
| `Katalog` | `dct:title`, `dct:description`, `dcat:contactPoint`, `dct:publisher` | 1, 2, 10 | F2, R1.2 |
| `Katalogpost` | `dct:modified`, `foaf:primaryTopic` | 9 | R1.3 |
| `Datasett` | `dct:title`, `dct:description`, `dcat:contactPoint`, `dcat:theme`, `dct:publisher` | 1, 2, 10 | F2, R1.2 |
| `Distribusjon` | `dcat:accessURL` | — | A1 |
| `Datatjeneste` | `dcat:endpointURL`, `dcat:contactPoint`, `dct:title`, `dct:publisher` | 1, 2, 10 | F2, A1, R1.2 |
| `Aktør` | `foaf:name` | 1 | F2 |

### Containerklasse-krav

| Sjekk | Alvor | Digdir-regel | FAIR |
|---|---|---|---|
| Containerklassen (`tree_root`) har attributt med range `Katalog`, `Datasett`, `Kvalitetsmaal`, `Kvalitetsmaaling` | error | — | — |
| Containerklassen har attributt med range `Distribusjon`, `Datatjeneste`, `Kvalitetsdimensjon`, `Kvalitetsmerknad` | warning | — | — |

---

## Gold-sjekkliste (i tillegg til silver og bronze)

Arvar sølv og bronse. Implementerer FAIR-prinsippa (Findable, Accessible, Interoperable, Reusable). Alle brot gir `error` — også dei som er åtvarslane på bronse.

| Sjekk | Alvor | Digdir-regel | FAIR | Skildring |
|---|---|---|---|---|
| `schema.id` er HTTP(S)-URI | error | 4 | F1 | Persistent og globalt unik identifikator — arva frå bronse, oppgradert til error |
| `schema.title` til stades | error | 1, 2 | F2 | Tittel er del av rike metadata som gjer ressursen søkbar — arva frå bronse |
| Alle klasser (unntatt `tree_root`) har `class_uri` | error | 4, 8 | F3 | Mappar klassen til RDF-vokabular — arva frå bronse, oppgradert til error |
| `schema.version` til stades | error | 9 | F4 | Versjonering støttar katalogregistrering og sporbarheit — arva frå bronse, oppgradert til error |
| Alle globale slots har `slot_uri` | error | 4, 8 | I1 | Mappar eigenskapen til RDF-vokabular — arva frå bronse, oppgradert til error |
| Skjemaet deklarerer minst eitt standard vokabularprefiks (`dct`, `dcat`, `skos`, `prov`, `rdf`, `rdfs`, `owl`, `foaf`, `xsd`) | error | 8 | I2 | Standardvokabular sikrar interoperabilitet på tvers av system |
| Skjemaet har ein slot med `dct:license` | error | 7 | R1.1 | Lisensinformasjon er føresetnad for gjenbruk — arva frå bronse, oppgradert til error |
| Skjemaet har ein slot for proveniens (`prov:wasAttributedTo`, `prov:wasGeneratedBy`, `dct:creator`, `dct:publisher` eller `dct:contributor`) | error | 10 | R1.2 | Proveniens er viktig for tillit til og gjenbruk av data |

---

## Publiseringspolicyer

Domene-spesifikke policyer for publisering til nasjonale katalogar. Dei arvar `bronze`
og er meinte brukt i tillegg til medaljongnivåa — typisk i CI-pipelinen for skjema
som har ein tilhøyrande datafil.

---

### Felles Begrepskatalog (`felles-begrepskatalog`)

For begrepskatalogskjema som publiserer til [data.norge.no/concepts](https://data.norge.no/concepts)
via SKOS-AP-NO-Begrep. Sjå [Publiser til Felles Begrepskatalog](https://brreg.github.io/linkml-datamodellering-no/publisering-begrep/) for full rettleiing.

**Import og prefiks:**

| Alvor | Krav | Kode |
|---|---|---|
| **error** | Importerer `skos-ap-no-schema` | `schema_importerer_skos_ap_no` |
| **error** | Deklarerer `skos:`-prefix | `schema_brukar_skos_prefix` |
| **error** | Deklarerer `dct:`-prefix | `schema_brukar_dct_prefix` |

**Containerklasse:**

| Alvor | Krav | Kode |
|---|---|---|
| **error** | Container har attributt med range `Begrep` | `container_har_begrep` |
| warning | Container har attributt med range `Samling` | `container_har_samling` |

**`Begrep`-krav (obligatoriske per SKOS-AP-NO-Begrep):**

| Alvor | Krav | Kode |
|---|---|---|
| **error** | `skos:prefLabel` | `begrep_har_anbefalt_term` |
| **error** | `skos:definition` eller `euvoc:xlDefinition` | `begrep_har_definisjon` |
| **error** | `dct:identifier` | `begrep_har_identifikator` |
| **error** | `dct:publisher` | `begrep_har_utgjevar` |
| **error** | `dcat:contactPoint` | `begrep_har_kontaktpunkt` |
| warning | `dct:subject` | `begrep_har_fagomrade` |
| warning | `dct:creator` | `begrep_har_ansvarleg_verksemd` |
| warning | `euvoc:startDate` | `begrep_har_gyldig_fra` |
| warning | `euvoc:endDate` | `begrep_har_gyldig_til` |
| warning | `dct:created` | `begrep_har_opprettingsdato` |
| warning | `dct:modified` | `begrep_har_endringsdato` |
| warning | `skos:scopeNote` | `begrep_har_merknad` |
| warning | `skos:altLabel` | `begrep_har_tillate_term` |

**`Definisjon`-, `AssosiativRelasjon`-, `GeneriskRelasjon`-, `PartitivRelasjon`- og `Samling`-krav** er dokumenterte i [`policies/felles-begrepskatalog.yaml`](felles-begrepskatalog.yaml).

**Instanssjekk:**

| Alvor | Krav | Kode |
|---|---|---|
| **error** | `dct:publisher`-verdi er `https://data.norge.no/organizations/<9-sifra orgnr>` og er i lista over kjende utgivarar | `utgjevar_er_kjend_org` |

---

### Felles Datakatalog (`felles-datakatalog`)

For modellkatalogskjema som publiserer til [data.norge.no/models](https://data.norge.no/models)
via ModelDCAT-AP-NO. Sjå [Publiser til Felles Datakatalog](https://brreg.github.io/linkml-datamodellering-no/publisering-modell/) for full rettleiing.

**Import og prefiks:**

| Alvor | Krav | Kode |
|---|---|---|
| **error** | Importerer `modelldcat-ap-no-schema` | `schema_importerer_modelldcat_ap_no` |
| **error** | Deklarerer `dct:`-prefix | `schema_brukar_dct_prefix` |
| **error** | Deklarerer `dcat:`-prefix | `schema_brukar_dcat_prefix` |

**Containerklasse:**

| Alvor | Krav | Kode |
|---|---|---|
| **error** | Container har attributt med range `Modellkatalog` | `container_har_modellkatalog` |
| **error** | Container har attributt med range `Informasjonsmodell` | `container_har_informasjonsmodell` |

**`Modellkatalog`-krav (obligatoriske per ModelDCAT-AP-NO):**

| Alvor | Krav | Kode |
|---|---|---|
| **error** | `dct:title` | `modellkatalog_har_tittel` |
| **error** | `dct:description` | `modellkatalog_har_beskrivelse` |
| **error** | `dct:identifier` | `modellkatalog_har_identifikator` |
| **error** | `dct:publisher` | `modellkatalog_har_utgjevar` |
| **error** | `dcat:contactPoint` | `modellkatalog_har_kontaktpunkt` |
| **error** | `dct:hasPart` | `modellkatalog_har_del` |
| warning | `dct:license` | `modellkatalog_har_lisens` |
| warning | `modelldcatno:model` | `modellkatalog_har_modell` |

**`Informasjonsmodell`-krav (obligatoriske per ModelDCAT-AP-NO):**

| Alvor | Krav | Kode |
|---|---|---|
| **error** | `dct:title` | `informasjonsmodell_har_tittel` |
| **error** | `dct:publisher` | `informasjonsmodell_har_utgjevar` |
| warning | `dct:description` | `informasjonsmodell_har_beskrivelse` |
| warning | `dct:identifier` | `informasjonsmodell_har_identifikator` |
| warning | `modelldcatno:informationModelIdentifier` | `informasjonsmodell_har_modellidentifikator` |
| warning | `dcat:contactPoint` | `informasjonsmodell_har_kontaktpunkt` |
| warning | `dct:license` | `informasjonsmodell_har_lisens` |
| warning | `dcat:theme` | `informasjonsmodell_har_tema` |
| warning | `modelldcatno:containsModelElement` | `informasjonsmodell_har_modellelement` |

**Instanssjekk:**

| Alvor | Krav | Kode |
|---|---|---|
| **error** | `dct:publisher`-verdi er `https://data.norge.no/organizations/<9-sifra orgnr>` og er i lista over kjende utgivarar | `utgjevar_er_kjend_org` |

---

## Skiljet mellom skjema- og datavalidering

| Kva | Verktøy | Policy |
|---|---|---|
| Skjemakvalitet | `make mcp-validate POLICY=bronze/silver/gold` | Policyfilene her |
| Datakvalitet (instansar) | `make validate-instance` | — |
| Publiseringskonformitet | `make mcp-validate POLICY=felles-datakatalog` | `felles-datakatalog.yaml` |

`felles-begrepskatalog.yaml` har i tillegg eit eige `instance_checks:`-felt for
sjekkar som krev faktiske instansdata (gitt via `INSTANCE=` til
`make mcp-validate`), t.d. `utgjevar_er_kjend_org` (kjende utgivar-URI-ar) og
`begrep_har_definisjon_pa_nb_og_nn` (tospråkskravet — sjå
`specs/done/avvik-skos-ap-no.md`, SK5 Forslag A).

---

## MCP-verktøy

| Verktøy | Skildring |
|---|---|
| `validate_linkml_schema` | Validerer eit skjema med lint + instansvalidering + policy-sjekkar. Parametrar: `schemaText` (påkravd), `policy` (standard: `bronze`), `instanceText` (valfri). |
| `validate_linkml_instance` | Validerer ein instans mot eit skjema. Tilsvarar `linkml validate --schema`. Parametrar: `schemaText`, `instanceText`, `targetClass` (valfri). |
