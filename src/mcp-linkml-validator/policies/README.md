# Policyer for mcp-linkml-validator

Sjekkane i bronze-, silver- og gold-policyane realiserer både
[Felles modelleringsregler for offentlig forvaltning](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029)
(Digitaliseringsdirektoratet, v1.0, juni 2022) og
[FAIR-prinsippa](https://www.go-fair.org/fair-principles/) (Findable, Accessible, Interoperable, Reusable).

---

## Digdir-reglar og FAIR-prinsipp — dekningsgrad

| # | Navn | Kort skildring | Dekt av | FAIR |
|---|---|---|---|---|
| 1 | [**Forståelighet**](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#forstelighet) | Navn og skildringar er forståelege for målgruppa | Bronze: `title` (error), `description` (warning) | [F2](https://www.go-fair.org/fair-principles/) |
| 2 | [**Meiningsfullheit**](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#meningsfullhet) | Navn speglar innhald og formål | Bronze: `title` (error) | [F2](https://www.go-fair.org/fair-principles/) |
| 3 | [**Navne- og skrivekonvensjoner**](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#navne_og_skrivekonvensjoner) | PascalCase for klasser, snake_case/camelCase for eigenskapar | Bronze: `class_names_pascal_case`, `slot_names_snake_case` (warning) | — |
| 4 | [**Identifiserbarheit**](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#identifiserbarhet) | Persistente URI-ar for modell, element og eigenskapar | Bronze: `id`, `default_prefix` (HTTPS-URI) (error); `class_uri`, `slot_uri`, identifikator-slot (warning) | [F1, F3](https://www.go-fair.org/fair-principles/) |
| 5 | [**Visualisering**](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#visualisering) | Modell tilgjengeleg med god visuell representasjon | Bronze/Gull: `schema_har_erdiagram_aktivert` (build.yaml har `generators.erdiagram: true`) — sjølve Mermaid-syntaksen i det genererte ER-diagrammet vert i tillegg validert nattleg av `mermaid-render`-jobben i `lenkje-og-mermaid-sjekk.yml` | — |
| 6 | [**Modularitet**](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#modularitet) | Handterleg mengde modellelement per modul | Bronze: `class_count_limit` — warning om skjemaet har fleire enn 50 klasser | — |
| 7 | [**Tilgjengeleggjering**](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#tilgjengeliggjring) | Modell fritt tilgjengeleg på nett med open lisens | Bronze: `license` (warning) | [R1.1](https://www.go-fair.org/fair-principles/) |
| 8 | [**Maskinprosserbarheit**](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#maskinprosserbarhet) | Modell tilgjengeleg i opne, maskinlesbare format | Bronze: `class_uri`, `slot_uri` (indirekte, via regel 4-sjekken); `no_inlined_on_primitive_range` (warning) | [I1, I2](https://www.go-fair.org/fair-principles/) |
| 9 | [**Datering**](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#datering) | Modell er datert med publiserings-, endrings- og gyldigheitsdato | Bronze: `version` (warning); Silver: `annotations.endringsdato` (warning) | [F4, R1.3](https://www.go-fair.org/fair-principles/) |
| 10 | [**Ansvar**](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#ansvar) | Eigarskap og innhaldsansvar for modellen er tydeleg | Silver: `annotations.utgiver` (warning) | [R1.2](https://www.go-fair.org/fair-principles/) |
| 11 | [**Modellstatus**](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#modellstatus) | Modellen har ein eksplisitt status (under utarbeiding, ferdig, forelda …) | Silver: `annotations.status` (warning) | [R1.3](https://www.go-fair.org/fair-principles/) |
| 12 | [**Sammenhenger mellom modeller**](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#sammenhenger_mellom_modeller) | Samanhengar med andre modellar er skildra | *Delvis evaluert* — `make analyse-modell-sammenhenger` kryssreferer LinkML sin importgraf mot `har_del`/`er_i_samsvar_med`/`er_profil_av`/`erstatter`/`er_erstattet_av` i modellkatalogen (informativ, ikkje CI-blokkerande) | [F3](https://www.go-fair.org/fair-principles/) |
| 13 | [**Begreper**](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#begreper) | Modellelement og -eigenskapar er knytte til omgrep | Bronze: `annotations.begrepsidentifikator` på alle klasser (warning) | [A2](https://www.go-fair.org/fair-principles/) |
| 14 | [**Gjenbruk**](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#gjenbruk) | Eksisterande modellelement vert gjenbrukt framfor nydefinisjoner | Sølv/Gull: `schema_importerer_dqv_ap_no` (import av dqv-ap-no-schema, warning/error). *Delvis evaluert* — `make analyse-ap-no-gjenbruk` sjekkar i tillegg gjenbruk av `common-ap-no-schema` innanfor `ap-no/*` (informativ) | [I3](https://www.go-fair.org/fair-principles/) |
| 15 | [**Standardiserte datatyper**](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#standardiserte_datatyper) | Primitive datatypar er standardiserte (XSD, RDFS) | Bronze/Gull: `local_types_have_standard_uri` — lokalt definerte typar (`types:`) skal ha `uri:` mot xsd/rdf/rdfs/owl. Typar arva frå `linkml:types` er alt garantert XSD-mappa | [I1](https://www.go-fair.org/fair-principles/) |

> **Merk:** Regel 5, 14 og 15 er dekte av policy-sjekkar (bronse/sølv/gull) for det som
> let seg validere frå sjølve skjemastrukturen. Regel 12 og delar av regel 14 (gjenbruk av
> `common-ap-no-schema`) er kryss-skjema-/kryss-katalog-analysar som ikkje passar som eit
> enkeltskjema-krav — dei vert i staden handterte som informative, ikkje CI-blokkerande
> modellanalyse-jobbar (`make analyse-modell-sammenhenger`, `make analyse-ap-no-gjenbruk`,
> køyrde vekentleg av `.github/workflows/modell-analyse.yml`). Sjå
> `specs/backlog/utvid-dekningsgrad-regel-5-12-14-15.md` for grunngjeving og avgrensingar.

---

## To typar validering

Policyfilene her er brukte til to ulike føremål:

**Skjemakvalitet (bronze / silver / gold)**  
Sjekkar at eit LinkML-skjema (`.yaml`-fila i `src/linkml/`) held eit visst
kvalitetsnivå: metadata, navngjeving, URI-ar, begrepsreferansar osv.  
Køyrast med `make mcp-linkml-valider-modell SCHEMA=... POLICY=bronze`.

**Publiseringskonformitet (felles-datakatalog / felles-begrepskatalog)**  
Sjekkar at eit skjema er i samsvar med krava til ei bestemt ekstern katalog.
Brukt for skjema der `publish_external: true` i manifest.

---

## Nivå for skjemakvalitet

| Nivå | Krav | Digdir-reglar | FAIR-prinsipp |
|---|---|---|---|
| [`bronze`](#bronze) | Grunnleggande LinkML metadata og modelleringskvalitet (dette repoets baseline) | 1, 2, 3, 4, 5, 6, 7, 8, 13, 15 | F1, F2, F3 (warning), I1 (warning), R1.1 (warning), A2 (warning) |
| [`silver`](#silver) | Bronze + AP-NO-konformitet og livssyklusmetadata | 1-5, 7-11, 13-15 | Bronze + R1.2, R1.3, I3 |
| [`gold`](#gold) | Silver + FAIR F1-R1.3: full semantisk interoperabilitet | 1-5, 7-11, 13-15 | F1-F4, I1-I3, R1.1-R1.3, A2 (alle error) |

Kvart nivå arvar krava frå nivåa under (`silver` arvar `bronze` osv., via `extends:`).

> **Merk — ikkje forveksle med data.norge.no sin kvalitetsskala:** Bronze/silver/gold
> validerer **skjemakvaliteten** (strukturen i sjølve `.yaml`-skjemaet), ikkje dei hausta
> metadataoppføringane. Data.norge.no skårar publiserte oppføringar på ein eigen
> FAIR-basert prosentskala (Utmerket ≥75 %, God 50-75 %, Tilstrekkeleg 25-50 %, Dårleg <25 %)
> — sjå [data.norge.no: Metadatakvalitet](https://data.norge.no/nb/docs/metadata-quality).
> Eit skjema som validerer på `gold` her garanterer difor ikkje automatisk "Utmerket" hos
> data.norge.no, sidan dei to skalaene måler ulike ting.

---

## Kvalitetspolicyer

### bronze

Grunnleggjande strukturkrav. Eit skjema som passerer bronse er syntaktisk korrekt og har nødvendig metadata.

| Sjekk | Alvor | Digdir-regel | FAIR | Skildring |
|---|---|---|---|---|
| `schema.id` til stades | error | [4 — Identifiserbarheit](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#identifiserbarhet) | [F1](https://www.go-fair.org/fair-principles/) | Persistent identifikator for skjemaet |
| `schema.id` er HTTP(S)-URI | error | [4 — Identifiserbarheit](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#identifiserbarhet) | [F1](https://www.go-fair.org/fair-principles/) | Sikrar at identifikatoren er ein oppløyseleg URI |
| `schema.name` til stades | error | [1 — Forståelighet](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#forstelighet) | — | Maskinlesbart navn for skjemaet |
| `schema.title` til stades | error | [1 — Forståelighet](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#forstelighet), [2 — Meiningsfullheit](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#meningsfullhet) | [F2](https://www.go-fair.org/fair-principles/) | Menneskelesbar tittel |
| `schema.default_prefix` til stades | error | [4 — Identifiserbarheit](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#identifiserbarhet) | — | Standardnavnerom for lokale identifikatorar |
| `schema.default_prefix` er absolutt HTTPS-URI med avsluttande `/` | error | [4 — Identifiserbarheit](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#identifiserbarhet) | — | Sikrar korrekt URI-konstruksjon for lokale ressursar |
| `schema.description` til stades | warning | [1 — Forståelighet](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#forstelighet) | [F2](https://www.go-fair.org/fair-principles/) | Fritekstskildring av skjemaet sitt føremål |
| `schema.version` til stades | warning | [9 — Datering](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#datering) | [F4](https://www.go-fair.org/fair-principles/) | Versjonsnummer for sporbarheit |
| `schema.license` til stades | warning | [7 — Tilgjengeleggjering](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#tilgjengeliggjring) | [R1.1](https://www.go-fair.org/fair-principles/) | Lisens for gjenbruk av skjemaet |
| Skjema har ikkje fleire enn 50 klasser (unntatt `tree_root`) | warning | [6 — Modularitet](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#modularitet) | — | Handterleg mengde modellelement per modul |
| Alle klassenavn startar med stor bokstav (PascalCase) | warning | [3 — Navne- og skrivekonvensjoner](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#navne_og_skrivekonvensjoner) | — | Konsistent navngjevingskonvensjon for klasser |
| Alle slotnavn er snake_case (berre `a-z`, `0-9`, `_` — **ikkje bindestreker**) | warning | [3 — Navne- og skrivekonvensjoner](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#navne_og_skrivekonvensjoner) | — | Konsistent navngjevingskonvensjon for eigenskapar |
| Alle klasser (unntatt `tree_root`) har `class_uri` | warning | [4 — Identifiserbarheit](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#identifiserbarhet), [8 — Maskinprosserbarheit](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#maskinprosserbarhet) | [F3, I1](https://www.go-fair.org/fair-principles/) | Mappar klassen til RDF-vokabular |
| Alle globale slots har `slot_uri` | warning | [4 — Identifiserbarheit](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#identifiserbarhet), [8 — Maskinprosserbarheit](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#maskinprosserbarhet) | [I1](https://www.go-fair.org/fair-principles/) | Mappar eigenskapen til RDF-vokabular |
| Alle klasser (unntatt `tree_root`) har identifikator-slot | warning | [4 — Identifiserbarheit](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#identifiserbarhet) | [F1](https://www.go-fair.org/fair-principles/) | Sikrar at instansar av klassen kan identifiserast unikt |
| Alle klasser (unntatt `tree_root`) har `annotations.begrepsidentifikator` | warning | [13 — Begreper](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#begreper) | [A2](https://www.go-fair.org/fair-principles/) | Koplar modellelement til fagomgrep i begrepskatalog |
| Slots med kontrollerte vokabular har korrekte annotations | warning | [8 — Maskinprosserbarheit](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#maskinprosserbarhet) | [I1](https://www.go-fair.org/fair-principles/) | Sikrar maskinlesbar dokumentasjon av vokabularkrav |
| `inlined`/`inlined_as_list` er berre sett der range er ein klasse | warning | [8 — Maskinprosserbarheit](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#maskinprosserbarhet) | [I1](https://www.go-fair.org/fair-principles/) | Fangar daud konfigurasjon — nøkkelen har ingen effekt på ein primitiv range |
| `build.yaml` har `generators.erdiagram: true` | warning | [5 — Visualisering](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#visualisering) | — | Sikrar at eit ER-diagram vert generert for skjemaet. Hoppar over dersom det ikkje finst noka `build.yaml` å lese |
| Lokalt definerte typar (`types:`) har `uri:` mot standardnamnerom (xsd/rdf/rdfs/owl) | warning | [15 — Standardiserte datatyper](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#standardiserte_datatyper) | [I1](https://www.go-fair.org/fair-principles/) | Typar arva frå `linkml:types` er alt garantert XSD-mappa og treng ingen eigen sjekk |

> **`snake_case`-format:** Slotnavn kan berre innehalde små bokstavar (`a-z`), tal (`0-9`) og understrek (`_`). **Bindestreker er ikkje tillate** — bruk samansette ord utan separasjon (t.d. `epost`, `epostadresse`) eller understrek (`mobilnummer_utgaar`).
>
> FINT-skjema er unntekne frå snake_case-sjekken — dei arvar camelCase frå FINT API-spesifikasjonen.

> **Kontrollerte vokabular:** Slots med `annotations.gyldige_verdier` skal ha `annotations.vokabular_krav` (`skal`|`bør`|`kan`) og `description` skal innehalde matchande SKAL/BØR/BØR-formulering. Sikrar konsistent og maskinlesbar dokumentasjon av vokabularkrav. Sjå [CONVENTIONS.md § Kontrollerte vokabular](../../../CONVENTIONS.md#kontrollerte-vokabular--annotation-konvensjon).

---

### silver

Arvar bronse. Legg til livssyklusmetadata og krav frå DCAT-AP-NO og DQV-AP-NO
for domenemodellar i norsk offentleg sektor, samt instanssjekkar for
kontrollerte vokabular.

| Sjekk | Alvor | Digdir-regel | FAIR | Skildring |
|---|---|---|---|---|
| `schema.annotations.utgiver` er URI på forma `https://data.norge.no/organizations/<orgnr>` | warning | [10 — Ansvar](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#ansvar) | [R1.2](https://www.go-fair.org/fair-principles/) | Identifiserer kven som har ansvar for modellen |
| `schema.annotations.endringsdato` er ISO 8601-dato | warning | [9 — Datering](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#datering) | [R1.3](https://www.go-fair.org/fair-principles/) | Datering av siste endring |
| `schema.annotations.status` er ADMS Status-URI | warning | [11 — Modellstatus](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#modellstatus) | [R1.3](https://www.go-fair.org/fair-principles/) | Eksplisitt livssyklusstatus (`UnderDevelopment`/`Completed`/`Deprecated`/`Withdrawn`) |
| Skjemaet importerer `dqv-ap-no-schema` (direkte eller transitivt) | warning | [14 — Gjenbruk](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#gjenbruk) | [I3](https://www.go-fair.org/fair-principles/) | Gjenbruk av kvalitetsvokabularet (Kvalitetsmaal, Kvalitetsmaaling m.fl.) i staden for eigne tilsvarande klassar/slots |
| `Katalog` har `dct:title` | error | [1 — Forståelighet](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#forstelighet), [2 — Meiningsfullheit](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#meningsfullhet), [10 — Ansvar](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#ansvar) | [F2, R1.2](https://www.go-fair.org/fair-principles/) | Tittel på katalogen |
| `Katalog` har `dct:description` | error | [1 — Forståelighet](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#forstelighet), [2 — Meiningsfullheit](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#meningsfullhet), [10 — Ansvar](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#ansvar) | [F2, R1.2](https://www.go-fair.org/fair-principles/) | Skildring av katalogen |
| `Katalog` har `dcat:contactPoint` | error | [1 — Forståelighet](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#forstelighet), [2 — Meiningsfullheit](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#meningsfullhet), [10 — Ansvar](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#ansvar) | [F2, R1.2](https://www.go-fair.org/fair-principles/) | Kontaktpunkt for katalogen |
| `Katalog` har `dct:publisher` | error | [1 — Forståelighet](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#forstelighet), [2 — Meiningsfullheit](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#meningsfullhet), [10 — Ansvar](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#ansvar) | [F2, R1.2](https://www.go-fair.org/fair-principles/) | Utgjevar av katalogen |
| `Katalogpost` har `dct:modified` | error | [9 — Datering](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#datering) | [R1.3](https://www.go-fair.org/fair-principles/) | Endringsdato for katalogposten |
| `Katalogpost` har `foaf:primaryTopic` | error | [9 — Datering](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#datering) | [R1.3](https://www.go-fair.org/fair-principles/) | Kopling til hovudressursen katalogposten skildrar |
| `Datasett` har `dct:title` | error | [1 — Forståelighet](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#forstelighet), [2 — Meiningsfullheit](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#meningsfullhet), [10 — Ansvar](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#ansvar) | [F2, R1.2](https://www.go-fair.org/fair-principles/) | Tittel på datasettet |
| `Datasett` har `dct:description` | error | [1 — Forståelighet](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#forstelighet), [2 — Meiningsfullheit](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#meningsfullhet), [10 — Ansvar](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#ansvar) | [F2, R1.2](https://www.go-fair.org/fair-principles/) | Skildring av datasettet |
| `Datasett` har `dcat:contactPoint` | error | [1 — Forståelighet](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#forstelighet), [2 — Meiningsfullheit](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#meningsfullhet), [10 — Ansvar](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#ansvar) | [F2, R1.2](https://www.go-fair.org/fair-principles/) | Kontaktpunkt for datasettet |
| `Datasett` har `dcat:theme` | error | [1 — Forståelighet](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#forstelighet), [2 — Meiningsfullheit](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#meningsfullhet), [10 — Ansvar](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#ansvar) | [F2, R1.2](https://www.go-fair.org/fair-principles/) | Tema/kategori for datasettet (Los) |
| `Datasett` har `dct:publisher` | error | [1 — Forståelighet](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#forstelighet), [2 — Meiningsfullheit](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#meningsfullhet), [10 — Ansvar](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#ansvar) | [F2, R1.2](https://www.go-fair.org/fair-principles/) | Utgjevar av datasettet |
| `Datasett` har `dct:accessRights` | warning | — | — | Tilgangsnivå for datasettet — svarar til trafikklyssystemet (grøn/gul/raud) i Digdir sin veileder [«Orden i eget hus», steg 4](https://www.digdir.no/informasjonsforvaltning/steg-4-vurdere-tilgangsniva/2723) |
| `Datasett` har `dcatap:applicableLegislation` | warning | — | — | Gjeldande lovgjeving (lovheimel) for tilgang til datasettet — same steg som over |
| `Distribusjon` har `dcat:accessURL` | error | — | [A1](https://www.go-fair.org/fair-principles/) | Tilgangsadresse til distribusjonen |
| `Datatjeneste` har `dcat:endpointURL` | error | [1 — Forståelighet](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#forstelighet), [2 — Meiningsfullheit](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#meningsfullhet), [10 — Ansvar](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#ansvar) | [F2, A1, R1.2](https://www.go-fair.org/fair-principles/) | Endepunkt-URL for tenesta |
| `Datatjeneste` har `dcat:contactPoint` | error | [1 — Forståelighet](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#forstelighet), [2 — Meiningsfullheit](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#meningsfullhet), [10 — Ansvar](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#ansvar) | [F2, A1, R1.2](https://www.go-fair.org/fair-principles/) | Kontaktpunkt for tenesta |
| `Datatjeneste` har `dct:title` | error | [1 — Forståelighet](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#forstelighet), [2 — Meiningsfullheit](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#meningsfullhet), [10 — Ansvar](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#ansvar) | [F2, A1, R1.2](https://www.go-fair.org/fair-principles/) | Tittel på tenesta |
| `Datatjeneste` har `dct:publisher` | error | [1 — Forståelighet](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#forstelighet), [2 — Meiningsfullheit](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#meningsfullhet), [10 — Ansvar](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#ansvar) | [F2, A1, R1.2](https://www.go-fair.org/fair-principles/) | Utgjevar av tenesta |
| `Aktør` har `foaf:name` | error | [1 — Forståelighet](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#forstelighet) | [F2](https://www.go-fair.org/fair-principles/) | Navn på aktøren |
| Containerklassen (`tree_root`) har attributt med range `Katalog`, `Datasett`, `Kvalitetsmaal`, `Kvalitetsmaaling` | error | — | — | Sikrar at hovudklassene i DCAT-AP-NO/DQV-AP-NO er kopla til containeren |
| Containerklassen har attributt med range `Distribusjon`, `Datatjeneste`, `Kvalitetsdimensjon`, `Kvalitetsmerknad` | warning | — | — | Sikrar at støtteklassene er kopla til containeren |
| Instansverdiar for slots med `vokabular_pattern` matchar regex-mønsteret **(krev `INSTANCE=`)** | error/warning/info | [8 — Maskinprosserbarheit](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#maskinprosserbarhet) | [I1](https://www.go-fair.org/fair-principles/) | Kode: `instance_slot_invalid_vocabulary_pattern`. Alvor avheng av `vokabular_krav`: **error** for `skal`, **warning** for `bør`, **info** for `kan` |
| Instansverdiar er frå korrekt vokabular-domene (`gyldige_verdier`) **(krev `INSTANCE=`)** | error/warning | [8 — Maskinprosserbarheit](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#maskinprosserbarhet) | [I1](https://www.go-fair.org/fair-principles/) | Kode: `instance_slot_invalid_vocabulary_domain`. Sjekkar at URI-ar startar med `gyldige_verdier`-domenet |

Gyldige verdiar for `annotations.status`: `http://purl.org/adms/status/UnderDevelopment`, `Completed`, `Deprecated`, `Withdrawn`.

> **Tilgangsnivå og Digdir sitt trafikklyssystem:** `dct:accessRights`-verdiane frå EU sitt
> Access Right-vokabular (`PUBLIC`/`RESTRICTED`/`NON_PUBLIC`, sjå `tilgangsrettigheter`-sloten
> i `dcat-ap-no-schema.yaml`) svarar funksjonelt til grøn/gul/raud i trafikklyssystemet frå
> Digdir sin veileder [«Orden i eget hus», steg 4 — vurdere tilgangsnivå](https://www.digdir.no/informasjonsforvaltning/steg-4-vurdere-tilgangsniva/2723).
> `dcatap:applicableLegislation` (`gjeldende_lovgivning`) svarar til lovheimel-kravet i same
> steg. Desse er sjekka via `datasett_tilgangsrettigheter` og `datasett_lovgivning`
> ovanfor.

Annotasjonsnøklane svarar til `Informasjonsmodell`-slots i `modelldcat-ap-no-schema.yaml`
(Digdir regel 10 og 8 — Maskinprosserbarheit via ModellDCAT-AP-NO).  
`make gen-informasjonsmodell-instance` genererer `Informasjonsmodell`-instansen for skjemaet frå desse annotasjonane; `make gen-modellkatalog-instance` aggregerer deretter alle slike instansar til per-org modellkatalogar.

**Døme (instanssjekk):** Dersom `spraak`-slot har `vokabular_krav: skal` og `vokabular_pattern: "^http://publications\\.europa\\.eu/resource/authority/language/[A-Z]{3}$"`, så vil verdien `"http://example.com/NOB"` gje **error** (feil domene) og `"http://publications.europa.eu/resource/authority/language/NORSK"` gje **error** (feil pattern — skal vere 3-bokstavskode).

---

### gold

Arvar sølv og bronse. Implementerer gap til FAIR-prinsippa (Findable, Accessible, Interoperable, Reusable). Alle brot gir `error` — også dei som er åtvarslane på bronse.

| Sjekk | Alvor | Digdir-regel | FAIR | Skildring |
|---|---|---|---|---|
| `schema.id` til stades | error | [4 — Identifiserbarheit](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#identifiserbarhet) | [F1](https://www.go-fair.org/fair-principles/) | Persistent identifikator for skjemaet — arva frå bronse (allereie error) |
| `schema.id` er HTTP(S)-URI | error | [4 — Identifiserbarheit](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#identifiserbarhet) | [F1](https://www.go-fair.org/fair-principles/) | Sikrar at identifikatoren er ein oppløyseleg URI — arva frå bronse (allereie error) |
| `schema.name` til stades | error | [1 — Forståelighet](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#forstelighet) | — | Maskinlesbart navn for skjemaet — arva frå bronse (allereie error) |
| `schema.title` til stades | error | [1 — Forståelighet](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#forstelighet), [2 — Meiningsfullheit](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#meningsfullhet) | [F2](https://www.go-fair.org/fair-principles/) | Tittel er del av rike metadata som gjer ressursen søkbar — arva frå bronse (allereie error) |
| `schema.default_prefix` til stades | error | [4 — Identifiserbarheit](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#identifiserbarhet) | — | Standardnavnerom for lokale identifikatorar — arva frå bronse (allereie error) |
| `schema.default_prefix` er absolutt HTTPS-URI med avsluttande `/` | error | [4 — Identifiserbarheit](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#identifiserbarhet) | — | Sikrar korrekt URI-konstruksjon — arva frå bronse (allereie error) |
| `schema.description` til stades | error | [1 — Forståelighet](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#forstelighet) | [F2](https://www.go-fair.org/fair-principles/) | Fritekstskildring av skjemaet sitt føremål — arva frå bronse, oppgradert til error |
| `schema.version` til stades | error | [9 — Datering](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#datering) | [F4](https://www.go-fair.org/fair-principles/) | Versjonering støttar katalogregistrering og sporbarheit — arva frå bronse, oppgradert til error |
| `schema.license` til stades | error | [7 — Tilgjengeleggjering](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#tilgjengeliggjring) | [R1.1](https://www.go-fair.org/fair-principles/) | Lisens for gjenbruk av skjemaet — arva frå bronse, oppgradert til error |
| Skjema har ikkje fleire enn 50 klasser (unntatt `tree_root`) | error | [6 — Modularitet](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#modularitet) | — | Handterleg mengde modellelement per modul — arva frå bronse, oppgradert til error |
| Alle klassenavn startar med stor bokstav (PascalCase) | error | [3 — Navne- og skrivekonvensjoner](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#navne_og_skrivekonvensjoner) | — | Konsistent navngjevingskonvensjon for klasser — arva frå bronse, oppgradert til error |
| Alle slotnavn er snake_case | error | [3 — Navne- og skrivekonvensjoner](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#navne_og_skrivekonvensjoner) | — | Konsistent navngjevingskonvensjon for eigenskapar — arva frå bronse, oppgradert til error |
| Alle klasser (unntatt `tree_root`) har `class_uri` | error | [4 — Identifiserbarheit](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#identifiserbarhet), [8 — Maskinprosserbarheit](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#maskinprosserbarhet) | [F3, I1](https://www.go-fair.org/fair-principles/) | Mappar klassen til RDF-vokabular — arva frå bronse, oppgradert til error |
| Alle globale slots har `slot_uri` | error | [4 — Identifiserbarheit](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#identifiserbarhet), [8 — Maskinprosserbarheit](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#maskinprosserbarhet) | [I1](https://www.go-fair.org/fair-principles/) | Mappar eigenskapen til RDF-vokabular — arva frå bronse, oppgradert til error |
| Alle klasser (unntatt `tree_root`) har identifikator-slot | error | [4 — Identifiserbarheit](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#identifiserbarhet) | [F1](https://www.go-fair.org/fair-principles/) | Sikrar at instansar av klassen kan identifiserast unikt — arva frå bronse, oppgradert til error |
| Alle klasser (unntatt `tree_root`) har `annotations.begrepsidentifikator` | error | [13 — Begreper](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#begreper) | [A2](https://www.go-fair.org/fair-principles/) | Koplar modellelement til fagomgrep i begrepskatalog — arva frå bronse, oppgradert til error |
| Slots med kontrollerte vokabular har korrekte annotations | error | [8 — Maskinprosserbarheit](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#maskinprosserbarhet) | [I1](https://www.go-fair.org/fair-principles/) | Sikrar maskinlesbar dokumentasjon av vokabularkrav — arva frå bronse, oppgradert til error |
| `build.yaml` har `generators.erdiagram: true` | error | [5 — Visualisering](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#visualisering) | — | Arva frå bronse, oppgradert til error |
| Skjemaet importerer `dqv-ap-no-schema` | error | [14 — Gjenbruk](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#gjenbruk) | [I3](https://www.go-fair.org/fair-principles/) | Arva frå sølv, oppgradert til error |
| Lokalt definerte typar (`types:`) har `uri:` mot standardnamnerom | error | [15 — Standardiserte datatyper](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#standardiserte_datatyper) | [I1](https://www.go-fair.org/fair-principles/) | Arva frå bronse, oppgradert til error |
| Skjemaet deklarerer minst eitt standard vokabularprefiks (`dct`, `dcat`, `skos`, `prov`, `rdf`, `rdfs`, `owl`, `foaf`, `xsd`) | error | [8 — Maskinprosserbarheit](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#maskinprosserbarhet) | [I2](https://www.go-fair.org/fair-principles/) | Standardvokabular sikrar interoperabilitet på tvers av system |
| Skjemaet har ein slot med `dct:license` | error | [7 — Tilgjengeleggjering](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#tilgjengeliggjring) | [R1.1](https://www.go-fair.org/fair-principles/) | Lisensinformasjon er føresetnad for gjenbruk — arva frå bronse, oppgradert til error |
| Skjemaet har ein slot for proveniens (`prov:wasAttributedTo`, `prov:wasGeneratedBy`, `dct:creator`, `dct:publisher` eller `dct:contributor`) | error | [10 — Ansvar](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#ansvar) | [R1.2](https://www.go-fair.org/fair-principles/) | Proveniens er viktig for tillit til og gjenbruk av data |
| `schema.annotations.utgiver` til stades | error | [10 — Ansvar](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#ansvar) | [R1.2](https://www.go-fair.org/fair-principles/) | URI til ansvarleg organisasjon — arva frå sølv, oppgradert til error |
| `schema.annotations.endringsdato` til stades | error | [9 — Datering](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#datering) | [R1.3](https://www.go-fair.org/fair-principles/) | ISO 8601-dato for siste endring — arva frå sølv, oppgradert til error |
| `schema.annotations.oppdateringsfrekvens` til stades | error | [9 — Datering](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#datering) | [R1.3](https://www.go-fair.org/fair-principles/) | URI frå EU sin Frequency Named Authority List — arva frå sølv, oppgradert til error |
| `schema.annotations.status` til stades | error | [11 — Modellstatus](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#modellstatus) | [R1.3](https://www.go-fair.org/fair-principles/) | ADMS Status-URI for modellstatus — arva frå sølv, oppgradert til error |
| `Distribusjon` har slot med `dct:license` | error | [7 — Tilgjengeleggjering](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029#tilgjengeliggjring) | [R1.1](https://www.go-fair.org/fair-principles/) | Lisens på distribusjonsnivå — arva frå sølv, oppgradert til error |
| `Datasett` har `dct:accessRights` | error | — | — | Tilgangsnivå (trafikklyssystemet) — arva frå sølv, oppgradert til error |
| `Datasett` har `dcatap:applicableLegislation` | error | — | — | Lovheimel for tilgang — arva frå sølv, oppgradert til error |
| Containerklassen har attributt med range `Distribusjon` | error | — | — | Arva frå sølv, oppgradert til error |
| Containerklassen har attributt med range `Datatjeneste` | error | — | — | Arva frå sølv, oppgradert til error |
| Containerklassen har attributt med range `Kvalitetsdimensjon` | error | — | — | Arva frå sølv, oppgradert til error |
| Containerklassen har attributt med range `Kvalitetsmerknad` | error | — | — | Arva frå sølv, oppgradert til error |

---

## Publiseringspolicyer

Domene-spesifikke policyer for publisering til nasjonale katalogar. Dei arvar `bronze`
og er meinte brukt i tillegg til medaljongnivåa — typisk i CI-pipelinen for skjema
som har ein tilhøyrande datafil.

| Policy | Krav | Målkatalog |
|---|---|---|
| [`felles-begrepskatalog`](#felles-begrepskatalog) | Bronse + SKOS-AP-NO-Begrep-konformitet for begrepskatalogskjema | [data.norge.no/concepts](https://data.norge.no/concepts) |
| [`felles-datakatalog`](#felles-datakatalog) | Bronse + ModelDCAT-AP-NO-konformitet for modellkatalogskjema | [data.norge.no/models](https://data.norge.no/models) |

---

### felles-begrepskatalog

For begrepskatalogskjema som publiserer til [data.norge.no/concepts](https://data.norge.no/concepts)
via SKOS-AP-NO-Begrep. Sjå [Publiser til Felles Begrepskatalog](https://brreg.github.io/linkml-datamodellering-no/publisering/publisering-begrep/) for full rettleiing.

| Kategori | Krav | Alvor | Kode | Kjelde |
|---|---|---|---|---|
| Import og prefiks | Importerer `skos-ap-no-schema` | **error** | `schema_importerer_skos_ap_no` | Repo-krav¹ |
| Import og prefiks | Deklarerer `skos:`-prefix | **error** | `schema_brukar_skos_prefix` | [Vedlegg A — Navnerom brukt i standarden](https://informasjonsforvaltning.github.io/skos-ap-no-begrep/#Navnerom-brukt-i-standarden) |
| Import og prefiks | Deklarerer `dct:`-prefix | **error** | `schema_brukar_dct_prefix` | [Vedlegg A — Navnerom brukt i standarden](https://informasjonsforvaltning.github.io/skos-ap-no-begrep/#Navnerom-brukt-i-standarden) |
| Containerklasse | Container har attributt med range `Begrep` | **error** | `container_har_begrep` | [§ Begrep](https://data.norge.no/specification/skos-ap-no-begrep#Begrep)² |
| Containerklasse | Container har attributt med range `Samling` | warning | `container_har_samling` | [§ Begrepssamling](https://data.norge.no/specification/skos-ap-no-begrep#Begrepssamling)² |
| `Begrep`-krav | `skos:prefLabel` | **error** | `begrep_har_anbefalt_term` | [§ Begrep – anbefalt term](https://data.norge.no/specification/skos-ap-no-begrep#Begrep-anbefalt-term) |
| `Begrep`-krav | `skos:definition` eller `euvoc:xlDefinition` | **error** | `begrep_har_definisjon` | [§ Begrep – definisjon, direkte angivelse](https://data.norge.no/specification/skos-ap-no-begrep#Begrep-definisjon-direkte-angivelse) / [via definisjonsobjekt](https://data.norge.no/specification/skos-ap-no-begrep#Begrep-definisjon-via-definisjonsobjekt) |
| `Begrep`-krav | `dct:identifier` | **error** | `begrep_har_identifikator` | [§ Begrep – identifikator](https://data.norge.no/specification/skos-ap-no-begrep#Begrep-identifikator) |
| `Begrep`-krav | `dct:publisher` | **error** | `begrep_har_utgjevar` | [§ Begrep – publisert av](https://data.norge.no/specification/skos-ap-no-begrep#Begrep-publisert-av) |
| `Begrep`-krav | `dcat:contactPoint` | **error** | `begrep_har_kontaktpunkt` | [§ Begrep – kontaktpunkt](https://data.norge.no/specification/skos-ap-no-begrep#Begrep-kontaktpunkt) |
| `Begrep`-krav | `dct:subject` | warning | `begrep_har_fagomrade` | [§ Begrep – fagområde](https://data.norge.no/specification/skos-ap-no-begrep#Begrep-fagområde) |
| `Begrep`-krav | `dct:creator` | warning | `begrep_har_ansvarleg_verksemd` | [§ Begrep – ansvarlig virksomhet](https://data.norge.no/specification/skos-ap-no-begrep#Begrep-ansvarlig-virksomhet) |
| `Begrep`-krav | `euvoc:startDate` | warning | `begrep_har_gyldig_fra` | [§ Begrep – dato gyldig fra og med](https://data.norge.no/specification/skos-ap-no-begrep#Begrep-dato-gyldig-fra-og-med) |
| `Begrep`-krav | `euvoc:endDate` | warning | `begrep_har_gyldig_til` | [§ Begrep – dato gyldig til og med](https://data.norge.no/specification/skos-ap-no-begrep#Begrep-dato-gyldig-til-og-med) |
| `Begrep`-krav | `dct:created` | warning | `begrep_har_opprettingsdato` | [§ Begrep – dato opprettet](https://data.norge.no/specification/skos-ap-no-begrep#Begrep-dato-opprettet) |
| `Begrep`-krav | `dct:modified` | warning | `begrep_har_endringsdato` | [§ Begrep – dato sist oppdatert](https://data.norge.no/specification/skos-ap-no-begrep#Begrep-dato-sist-oppdatert) |
| `Begrep`-krav | `skos:scopeNote` | warning | `begrep_har_merknad` | [§ Begrep – merknad](https://data.norge.no/specification/skos-ap-no-begrep#Begrep-merknad) |
| `Begrep`-krav | `skos:altLabel` | warning | `begrep_har_tillate_term` | [§ Begrep – tillatt term](https://data.norge.no/specification/skos-ap-no-begrep#Begrep-tillatt-term) |
| Tospråkskrav | `anbefalt_term` (skos:prefLabel) har range `LangString` og `multivalued: true` | warning | `begrep_anbefalt_term_er_multivalued_langstring` | [§ Begrep – anbefalt term](https://data.norge.no/specification/skos-ap-no-begrep#Begrep-anbefalt-term) (Merknad 1) |
| Tospråkskrav | `har_definisjon` har minst éi Definisjon per språk (nb, nn) | warning | `begrep_har_definisjon_pa_nb_og_nn` | [§ Begrep – anbefalt term](https://data.norge.no/specification/skos-ap-no-begrep#Begrep-anbefalt-term) (Merknad 1+2) |
| Instanssjekk | `dct:publisher`-verdi er `https://data.norge.no/organizations/<9-sifra orgnr>` og er i lista over kjende utgivarar | **error** | `utgjevar_er_kjend_org` | Repo-intern³ |

`Begrep`-krava er obligatoriske per SKOS-AP-NO-Begrep. `Definisjon`-, `AssosiativRelasjon`-,
`GeneriskRelasjon`-, `PartitivRelasjon`- og `Samling`-krav er dokumenterte i
[`policies/felles-begrepskatalog.yaml`](felles-begrepskatalog.yaml).

¹ **Repo-krav:** LinkML-teknisk føresetnad for å uttrykke vokabularet (import av
skjema, deklarasjon av prefiks) — ikkje eit eige punkt i spesifikasjonsteksten.
² **Repo-konvensjon:** containerklasse (`tree_root`)-mønsteret er repoet sin eigen
måte å eksponere klassane på, ikkje eit krav frå spesifikasjonen — lenkja peikar til
klassen sin generelle omtale i spesifikasjonen for kontekst.
³ **Repo-intern:** lista over kjende utgivar-URI-ar er halden i repoet, ikkje henta
frå spesifikasjonen.

**Om tospråkskravet (SK5, SKOS-AP-NO v.2.0.15):** `begrep_anbefalt_term_er_multivalued_langstring`
er ein schemasjekk — sikrar at skjemaet **kan** innehalde tospråkverdiar.
`begrep_har_definisjon_pa_nb_og_nn` er ein instanssjekk via ID-suffiks-konvensjon.

**Avgrensing:** Tospråkskravet for `anbefalt_term` kan **ikkje** validerast i YAML-instansar
pga. LinkML sin avgrensing (LangString bærer ikkje språk-tag per verdi i YAML — sjå
`specs/bugs/langstring-rdflib-roundtrip.md`). Bruk RDF-validering (SHACL) eller manuell
gjennomgang av `.ttl`-fila for å verifiere at både `@nb` og `@nn` er til stades.

---

### felles-datakatalog

For modellkatalogskjema som publiserer til [data.norge.no/models](https://data.norge.no/models)
via ModelDCAT-AP-NO. Sjå [Publiser til Felles Datakatalog](https://brreg.github.io/linkml-datamodellering-no/publisering/publisering-modell/) for full rettleiing.

| Kategori | Krav | Alvor | Kode | Kjelde |
|---|---|---|---|---|
| Import og prefiks | Importerer `modelldcat-ap-no-schema` | **error** | `schema_importerer_modelldcat_ap_no` | Repo-krav¹ |
| Import og prefiks | Deklarerer `dct:`-prefix | **error** | `schema_brukar_dct_prefix` | [Vedlegg A — Navnerom](https://data.norge.no/specification/modelldcat-ap-no#Navnerom) |
| Import og prefiks | Deklarerer `dcat:`-prefix | **error** | `schema_brukar_dcat_prefix` | [Vedlegg A — Navnerom](https://data.norge.no/specification/modelldcat-ap-no#Navnerom) |
| Containerklasse | Container har attributt med range `Modellkatalog` | **error** | `container_har_modellkatalog` | [§ Modellkatalog](https://data.norge.no/specification/modelldcat-ap-no#Modellkatalog)² |
| Containerklasse | Container har attributt med range `Informasjonsmodell` | **error** | `container_har_informasjonsmodell` | [§ Informasjonsmodell](https://data.norge.no/specification/modelldcat-ap-no#Informasjonsmodell)² |
| `Modellkatalog`-krav | `dct:title` | **error** | `modellkatalog_har_tittel` | [§ Modellkatalog – tittel](https://data.norge.no/specification/modelldcat-ap-no#Modellkatalog-tittel) |
| `Modellkatalog`-krav | `dct:description` | **error** | `modellkatalog_har_beskrivelse` | [§ Modellkatalog – beskrivelse](https://data.norge.no/specification/modelldcat-ap-no#Modellkatalog-beskrivelse) |
| `Modellkatalog`-krav | `dct:identifier` | warning | `modellkatalog_har_identifikator` | [§ Modellkatalog – identifikator](https://data.norge.no/specification/modelldcat-ap-no#Modellkatalog-identifikator) |
| `Modellkatalog`-krav | `dct:publisher` | **error** | `modellkatalog_har_utgjevar` | [§ Modellkatalog – utgiver](https://data.norge.no/specification/modelldcat-ap-no#Modellkatalog-utgiver) |
| `Modellkatalog`-krav | `dcat:contactPoint` | **error** | `modellkatalog_har_kontaktpunkt` | [§ Modellkatalog – kontaktpunkt](https://data.norge.no/specification/modelldcat-ap-no#Modellkatalog-kontaktpunkt) |
| `Modellkatalog`-krav | `dct:hasPart` | **error** | `modellkatalog_har_del` | [§ Modellkatalog – har del](https://data.norge.no/specification/modelldcat-ap-no#Modellkatalog-har-del) |
| `Modellkatalog`-krav | `dct:license` | warning | `modellkatalog_har_lisens` | [§ Modellkatalog – lisens](https://data.norge.no/specification/modelldcat-ap-no#Modellkatalog-lisens) |
| `Modellkatalog`-krav | `modelldcatno:model` | warning | `modellkatalog_har_modell` | [§ Modellkatalog – modell](https://data.norge.no/specification/modelldcat-ap-no#Modellkatalog-modell) |
| `Informasjonsmodell`-krav | `dct:title` | **error** | `informasjonsmodell_har_tittel` | [§ Informasjonsmodell – tittel](https://data.norge.no/specification/modelldcat-ap-no#Informasjonsmodell-tittel) |
| `Informasjonsmodell`-krav | `dct:publisher` | **error** | `informasjonsmodell_har_utgjevar` | [§ Informasjonsmodell – utgiver](https://data.norge.no/specification/modelldcat-ap-no#Informasjonsmodell-utgiver) |
| `Informasjonsmodell`-krav | `dcat:contactPoint` | **error** | `informasjonsmodell_har_kontaktpunkt` | [§ Informasjonsmodell – kontaktpunkt](https://data.norge.no/specification/modelldcat-ap-no#Informasjonsmodell-kontaktpunkt) |
| `Informasjonsmodell`-krav | `dct:description` | warning | `informasjonsmodell_har_beskrivelse` | [§ Informasjonsmodell – beskrivelse](https://data.norge.no/specification/modelldcat-ap-no#Informasjonsmodell-beskrivelse) |
| `Informasjonsmodell`-krav | `dct:identifier` | warning | `informasjonsmodell_har_identifikator` | [§ Informasjonsmodell – identifikator](https://data.norge.no/specification/modelldcat-ap-no#Informasjonsmodell-identifikator) |
| `Informasjonsmodell`-krav | `modelldcatno:informationModelIdentifier` | warning | `informasjonsmodell_har_modellidentifikator` | [§ Informasjonsmodell – informasjonsmodellidentifikator](https://data.norge.no/specification/modelldcat-ap-no#Informasjonsmodell-informasjonsmodellidentifikator) |
| `Informasjonsmodell`-krav | `dct:license` | warning | `informasjonsmodell_har_lisens` | [§ Informasjonsmodell – lisens](https://data.norge.no/specification/modelldcat-ap-no#Informasjonsmodell-lisens) |
| `Informasjonsmodell`-krav | `dcat:theme` | warning | `informasjonsmodell_har_tema` | [§ Informasjonsmodell – tema](https://data.norge.no/specification/modelldcat-ap-no#Informasjonsmodell-tema) |
| `Informasjonsmodell`-krav | `modelldcatno:containsModelElement` | warning | `informasjonsmodell_har_modellelement` | [§ Informasjonsmodell – inneholder modellelement](https://data.norge.no/specification/modelldcat-ap-no#Informasjonsmodell-inneholder-modellelement) |
| Instanssjekk | `dct:publisher`-verdi er `https://data.norge.no/organizations/<9-sifra orgnr>` og er i lista over kjende utgivarar | **error** | `utgjevar_er_kjend_org` | Repo-intern³ |

`Modellkatalog`- og `Informasjonsmodell`-krava er obligatoriske per ModelDCAT-AP-NO,
med unntak av `dct:identifier` (anbefalt — sjå eiga fotnote i kjeldetabellen for
`modellkatalog_har_identifikator`; det same gjeld transitivt for
`informasjonsmodell_har_identifikator`, som alt sto som `warning`). Merk òg at
`dcat:contactPoint` på `Informasjonsmodell` er obligatorisk (`error`), retta frå
tidlegare `warning` — sjå `specs/done/kjeldehenvisning-felles-katalog-policyar.md`
for grunngjeving og kjeldeverifisering.

¹ **Repo-krav:** LinkML-teknisk føresetnad for å uttrykke vokabularet (import av
skjema, deklarasjon av prefiks) — ikkje eit eige punkt i spesifikasjonsteksten.
² **Repo-konvensjon:** containerklasse (`tree_root`)-mønsteret er repoet sin eigen
måte å eksponere klassane på, ikkje eit krav frå spesifikasjonen — lenkja peikar til
klassen sin generelle omtale i spesifikasjonen for kontekst.
³ **Repo-intern:** lista over kjende utgivar-URI-ar er halden i repoet, ikkje henta
frå spesifikasjonen.

---

## Skiljet mellom skjema- og datavalidering

| Kva | Verktøy | Policy |
|---|---|---|
| Skjemakvalitet | `make mcp-linkml-valider-modell POLICY=bronze/silver/gold` | Policyfilene her |
| Datakvalitet (instansar) | `make validate-instance` | — |
| Publiseringskonformitet | `make mcp-linkml-valider-modell POLICY=felles-datakatalog` | `felles-datakatalog.yaml` |

`felles-begrepskatalog.yaml` har i tillegg eit eige `instance_checks:`-felt for
sjekkar som krev faktiske instansdata (gitt via `INSTANCE=` til
`make mcp-linkml-valider-modell`), t.d. `utgjevar_er_kjend_org` (kjende utgivar-URI-ar) og
`begrep_har_definisjon_pa_nb_og_nn` (tospråkskravet — sjå
`specs/done/avvik-skos-ap-no.md`, SK5 Forslag A).

---

## MCP-verktøy

| Verktøy | Skildring |
|---|---|
| `validate_linkml_schema` | Validerer eit skjema med lint + instansvalidering + policy-sjekkar. Parametrar: `schemaText` (påkravd), `policy` (standard: `bronze`), `instanceText` (valfri). |
| `validate_linkml_instance` | Validerer ein instans mot eit skjema. Tilsvarar `linkml validate --schema`. Parametrar: `schemaText`, `instanceText`, `targetClass` (valfri). |
