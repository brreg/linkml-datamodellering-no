# Manifest som ModelDCAT-AP-NO-datafil

## Bakgrunn

Dagens `manifest.yaml`-format (t.d. `src/linkml/ap-no/dqv-ap-no/manifest.yaml`) styrer
generator- og publiseringskonfigurasjon for LinkML-skjema. Kvar modell har eit manifest
med felt som `validation_policy`, `publish_external`, `external_spec_url` og `generators:`-blokk.

ModelDCAT-AP-NO definerer ein `Informasjonsmodell`-klasse (i `modelldcat-katalog-schema.yaml`)
som beskriv metadata om informasjonsmodellar i samsvar med Digdir sin spesifikasjon.
Denne klassen dekkjer mykje av same terreng som dagens manifest-filer — tittel, beskrivelse,
versjon, lisens, utgjevar, status, kontaktpunkt, tema, osv.

Spørsmålet er om `manifest.yaml` kan migrerast til eit `Informasjonsmodell`-basert format,
og kva fordeler og svakheiter ein slik tilnærming vil ha.

## Noverande manifest-format

Typisk struktur (døme frå `dqv-ap-no/manifest.yaml`):

```yaml
publish_external: false
validation_policy: gold
external_spec_url: https://informasjonsforvaltning.github.io/dqv-ap-no/
external_spec_label: "DQV-AP-NO (Norsk applikasjonsprofil av DQV)"
submodels:
  - dqv-core

generators:
  jsonld_context: true
  shacl: true
  python: true
  json_schema: true
  owl: true
  rdf: true
  protobuf: true
  erdiagram: true
  docs: true
  plantuml: true
  example_rdf: false
  xsd: false
  openapi: true
  asyncapi: false
```

Datafil-manifest (utan `generators:`-blokk, t.d. for datafiler i `data/`-katalogar):

```yaml
publish_external: true
validation_policy: felles-begrepskatalog

concepts:
  - https://begrep.brreg.no/foretaksnavn
  - https://begrep.brreg.no/nestleder
```

## ModelDCAT-AP-NO Informasjonsmodell-klassen

`Informasjonsmodell` (frå `modelldcat-katalog-schema.yaml`) har desse slotsa (utval):

| Slot | Svarar til dagens manifest | Kommentar |
|---|---|---|
| `id` | (implisitt frå skjemanamn/plassering) | URI til modellen |
| `tittel` | (schema.yaml `title`) | Frå skjemaet, ikkje manifest |
| `beskrivelse` | (schema.yaml `description`) | Frå skjemaet, ikkje manifest |
| `versjonsnummer` | (schema.yaml `version`) | Frå skjemaet, ikkje manifest |
| `lisens` | (schema.yaml `license`) | Frå skjemaet, ikkje manifest |
| `utgiver` | (schema.yaml `annotations.utgiver`) | Frå skjemaet, ikkje manifest |
| `endringsdato` | (schema.yaml `annotations.endringsdato`) | Frå skjemaet, ikkje manifest |
| `utgivelsesdato` | (schema.yaml `annotations.utgivelsesdato`) | Frå skjemaet, ikkje manifest |
| `status` | (schema.yaml `annotations.status`) | Frå skjemaet, ikkje manifest |
| `kontaktpunkt` | **CODEOWNERS.md** | CI kan parse CODEOWNERS og generere kontaktpunkt |
| `tema` | **schema.yaml annotations** | Utvid `annotations:`-blokka med `tema:` (liste av Los-URI-ar) |
| `finnes_i_format` | **Genererte artefaktar** | CI genererer URI-liste til `.ttl`, `.json`, `.owl`, etc. i `generated/` |
| `heimeside` | `external_spec_url` | **Kan mappast frå manifest** |
| `er_profil_av` | **Kjent avvik (krev DX-PROF LinkML)** | MVP: valfri `annotations.er_profil_av`. Framtidig: `data/profil/profil.yaml` |
| `har_del` | `submodels` | **Kan mappast frå manifest** |
| `inneholder_modellelement` | **Skjemaet sine lokale klasser** | CI genererer URI-liste til klasser definerte i `classes:` (ikkje importerte) |

### Kjelde til ModelDCAT-felt

ModelDCAT-felt kjem frå ulike kjelder — nokre auto-genererte, nokre frå eksisterande filer, nokre krev ny kjeldekode-fil:

#### `tema` — frå schema.yaml annotations

**Problem:** `tema` er semantisk metadata (Los-tema, fagdomene) som ikkje passar naturleg i:
- `build.yaml` — er CI/CD-konfigurasjon, ikkje semantikk
- `CODEOWNERS.md` — er organisatorisk, ikkje fagleg
- Eigen `metadata.yaml`-fil — overkill for berre `tema:` (og kanskje `dekningsomraade`, `nokkelord`)

**Løysing:** Utvid `annotations:`-blokka i `schema.yaml` til å inkludere `tema` (og andre ModelDCAT-felt).

**Evaluering av annotations-format:**

LinkML `annotations:` støttar **både scalar-verdiar og lister**. Eksisterande bruk:
```yaml
annotations:
  utgiver: https://data.norge.no/organizations/991825827
  endringsdato: "2026-07-04"
  utgivelsesdato: "2023-01-01"
  status: http://purl.org/adms/status/Completed
```

**Utvidelse med tema:**
```yaml
# src/linkml/ap-no/dqv-ap-no/dqv-ap-no-schema.yaml
annotations:
  utgiver: https://data.norge.no/organizations/991825827
  endringsdato: "2026-07-04"
  utgivelsesdato: "2023-01-01"
  status: http://purl.org/adms/status/Completed
  
  # ModelDCAT-felt som ikkje har naturleg plass i LinkML toppnivå-felt:
  tema:
    - https://psi.norge.no/los/tema/teknologi-og-digitalisering
    - https://psi.norge.no/los/tema/styring-og-administrasjon
  
  # Valgfrie tilleggsfelt:
  # dekningsomraade: https://data.geonorge.no/administrativeEnheter/nasjon/id/173163
  
  # LangString-felt krev ALLTID både nb (bokmål) og nn (nynorsk):
  # nokkelord:
  #   nb:
  #     - datakvalitet
  #     - kvalitetsmåling
  #   nn:
  #     - datakvalitet
  #     - kvalitetsmåling
```

**Fordeler:**
- ✅ Ein fil mindre — alt i `schema.yaml`
- ✅ `annotations:` er **allereie brukt for ModelDCAT-felt** (utgiver, status, endringsdato, utgivelsesdato)
- ✅ LinkML støttar multivalued lister i annotations
- ✅ Semantisk konsistent — `tema` er metadata om modellen, akkurat som `utgiver` og `status`
- ✅ Enklare å vedlikehalde — all metadata samla i éi fil
- ✅ Mindre risiko for at metadata kjem ut av synk

**Svakheiter:**
- ⚠️ `annotations:` er fri-form nøkkel-verdi-par — ingen skjemavalidering av innhaldet
- ⚠️ Blandar Digdir-regel-metadata (utgiver, status) med Los-klassifisering (tema) — men begge er ModelDCAT-felt
- ⚠️ Blir ein relativt lang annotations-blokk dersom mange valgfrie felt vert brukt (nokkelord, dekningsomraade, osv.)

**Alternativ vurdert:**

##### Alt 1: `schema.yaml` annotations (anbefalt) ⭐
```yaml
annotations:
  utgiver: ...
  status: ...
  tema:
    - https://psi.norge.no/los/tema/...
```

**Fordeler:** Ein fil, konsistent med eksisterande praksis
**Svakheiter:** Ingen skjemavalidering av annotations-innhald

##### Alt 2: `build.yaml`
```yaml
tema:
  - https://psi.norge.no/los/tema/...
```

**Fordeler:** Beheld dagens manifest-struktur
**Svakheiter:** `build.yaml` skal vere build/CI-konfigurasjon, ikkje semantikk — blandar concerns

##### Alt 3: Separat `metadata.yaml`
```yaml
tema:
  - https://psi.norge.no/los/tema/...
```

**Fordeler:** Klart skille mellom ulike typar metadata
**Svakheiter:** Overkill — ein heil fil berre for `tema:` (og kanskje 1-2 andre felt)

##### Konklusjon: Utvid `annotations:` (Alt 1) ⭐

`annotations:` er **allereie etablert praksis** for ModelDCAT-metadata i repoet (`utgiver`, `status`, `endringsdato`, `utgivelsesdato`). Å leggje til `tema` er ein naturleg utvidelse av same prinsipp. Dette gir:

- Éi fil å vedlikehalde (`schema.yaml`)
- Konsistent bruk av `annotations:` for alle ModelDCAT-felt
- Enklare CI-logikk (mindre filer å parse)

**Skjemavalidering av annotations:** Framtidig mogleg utviding — LinkML kunne støtte eit `annotations_schema:`-felt som validerer strukturen. Men det er ikkje nødvendig for MVP.

### LangString-krav: Både bokmål (nb) og nynorsk (nn)

**Viktig:** Alle LangString-felt i ModelDCAT-metadata må ha **både bokmål (nb) og nynorsk (nn)** målformer.

**Kvifor:** Dette sikrar tilgjengelegheit på begge offisielle norske målformer, i samsvar med Språklova og Digdir sine retningsliner for offentleg sektor.

**Gjeld for desse ModelDCAT-felta:**
- `nokkelord` (dcat:keyword) — LangString, multivalued
- Eventuelt andre LangString-felt som vert lagt til i `annotations:`

**Gjeld IKKJE for:**
- `tittel` og `beskrivelse` — desse er allereie definerte i `schema.yaml` toppnivå-felt (som scalar strings), ikkje i `annotations:`
- `tema` — URI-liste, ikkje LangString
- `dekningsomraade` — URI, ikkje LangString
- `utgiver`, `status`, `endringsdato`, `utgivelsesdato` — URI eller datoar, ikkje LangString

**Døme på korrekt LangString i annotations:**
```yaml
annotations:
  nokkelord:
    nb:
      - datakvalitet
      - kvalitetsmåling
      - DQV
    nn:
      - datakvalitet
      - kvalitetsmåling
      - DQV
```

**CI-validering:** `make validate-modelldcat` bør sjekke at alle LangString-felt i genererte `metadata/modelldcat.yaml`-filer har både `nb` og `nn` (kan vere same verdi dersom omgrepet er identisk på begge målformer).

**Obs om tittel og beskrivelse:** `title` og `description` i `schema.yaml` toppnivå er scalar strings (ikkje LangString) fordi LinkML ikkje støttar multivalued LangString i toppnivå-felt. 

**CI-transformasjon til LangString:**

1. `title` → `tittel.nb` (antatt bokmål, sidan bokmål er modelleringsspråk per CLAUDE.md)
2. `description` → `beskrivelse.nb`
3. Dersom `annotations.tittel_nn` finst → `tittel.nn`, elles `tittel.nn = tittel.nb`
4. Dersom `annotations.beskrivelse_nn` finst → `beskrivelse.nn`, elles `beskrivelse.nn = beskrivelse.nb`

**Døme:**
```yaml
# I schema.yaml
title: DQV-AP-NO
description: Norsk applikasjonsprofil av DQV...

annotations:
  # Valgfri nynorsk-oversetting (berre dersom forskjellig frå bokmål):
  tittel_nn: DQV-AP-NO
  beskrivelse_nn: Norsk applikasjonsprofil av DQV...
```

→ CI genererer i `metadata/modelldcat.yaml`:

```yaml
tittel:
  nb: "DQV-AP-NO"
  nn: "DQV-AP-NO"  # Same som nb (ingen tittel_nn i annotations)
beskrivelse:
  nb: "Norsk applikasjonsprofil av DQV..."
  nn: "Norsk applikasjonsprofil av DQV..."  # Same som nb
```

**Anbefaling til brukarar:** Berre definer `tittel_nn`/`beskrivelse_nn` i `annotations:` dersom nynorsk-versjonen er **vesentleg forskjellig** frå bokmål-versjonen. Elles la CI bruke same verdi for begge målformer.

### Auto-genererbare felt frå eksisterande kjelder

Fleire ModelDCAT-felt kan genererast automatisk av CI utan å krevje eksplisitt input:

#### `kontaktpunkt` — frå CODEOWNERS.md

`CODEOWNERS.md` inneheld ein YAML-frontmatter med organisasjonsinfo, inkludert `contact_uri` og `name`. CI matcher skjemaet sin `path` mot `path_patterns` for å finne riktig organisasjon:

```yaml
# CODEOWNERS.md (YAML-frontmatter)
organizations:
  - alias: digdir
    name: Digitaliseringsdirektoratet
    org_uri: https://data.norge.no/organizations/991825827
    contact_uri: https://www.digdir.no/om-oss/kontakt-oss/887
    path_patterns:
      - src/linkml/ap-no/**
```

→ CI finn organisasjon for `src/linkml/ap-no/dqv-ap-no/` og genererer:

```yaml
kontaktpunkt:
  har_referanse: https://www.digdir.no/om-oss/kontakt-oss/887
  har_organisasjonsnamn: Digitaliseringsdirektoratet
```

**Parsingslogikk:**
1. Les YAML-frontmatter frå `CODEOWNERS.md`
2. Match `src/linkml/<domain>/<modell>/` mot kvar organisasjon sin `path_patterns` (glob-match)
3. Dersom match: bruk `contact_uri` → `har_referanse` og `name` → `har_organisasjonsnamn`
4. Dersom ingen match: `kontaktpunkt` vert utelate frå `metadata/modelldcat.yaml` (med warning i CI-log)

**Avgrensing (første versjon):**
- Berre `contact_uri` (ikkje e-postadresse) — ModelDCAT `Kontaktopplysning` støttar både, men vi prioriterer `har_referanse` (URI til kontaktside)
- Kun éin organisasjon per skjema — dersom fleire path_patterns matcher, bruk den mest spesifikke (lengste path)

#### `finnes_i_format` — frå genererte artefaktar

CI samlar URI-ar til alle genererte artefaktar i `generated/<domain>/<modell>/`:

**Base-URL:** `https://raw.githubusercontent.com/Informasjonsforvaltning/linkml-datamodellering-no/main/generated/<domain>/<modell>/`

**Inkluderte artefaktar (kun filer som faktisk finst):**
- `<modell>-schema.ttl` (RDF Turtle serialisering)
- `<modell>-schema.json` (JSON Schema)
- `<modell>-ontology.ttl` (OWL ontology)
- `<modell>-shapes.ttl` (SHACL shapes)
- `<modell>.puml` (PlantUML diagram)
- Andre genererte filer med relevante format (`.proto`, `.openapi.yaml`, `.context.jsonld`, osv.)

**Format:** Flat URI-liste (ikkje `Distribusjon`-instansar for MVP)

**Eksempel:**
```yaml
finnes_i_format:
  - https://raw.githubusercontent.com/.../generated/ap-no/dqv-ap-no/dqv-ap-no-schema.ttl
  - https://raw.githubusercontent.com/.../generated/ap-no/dqv-ap-no/dqv-ap-no-schema.json
  - https://raw.githubusercontent.com/.../generated/ap-no/dqv-ap-no/dqv-ap-no-ontology.ttl
  - https://raw.githubusercontent.com/.../generated/ap-no/dqv-ap-no/dqv-ap-no-shapes.ttl
  - https://raw.githubusercontent.com/.../generated/ap-no/dqv-ap-no/dqv-ap-no.puml
```

**Handtering:** CI itererer gjennom `generated/<domain>/<modell>/` og inkluderer berre filer som faktisk eksisterer (generatorar kan vere slått av i `build.yaml`).

#### `er_profil_av` — kjent avvik (krev DX-PROF LinkML-implementering)

**Status:** IKKJE IMPLEMENTERT i MVP — krev at DX-PROF-standarden vert modellert i LinkML først.

**Framtidig implementering:**
DX-PROF skal modellerast i LinkML (`dx-prof-schema.yaml`) med klasser som `Profile`, `ResourceDescriptor`, osv. Skjema som er profilar kan då importere dette og inkludere ein `Profile`-instans i ei tilhøyrande datafil (t.d. `dqv-ap-no-profil.yaml`):

```yaml
# Framtidig: src/linkml/ap-no/dqv-ap-no/dqv-ap-no-schema.yaml
imports:
  - ../../w3c/dx-prof/dx-prof-schema

# Framtidig: src/linkml/ap-no/dqv-ap-no/data/profil/profil.yaml
id: https://data.norge.no/ap-no/dqv-ap-no
type: Profile
is_profile_of:
  - http://www.w3.org/ns/dqv#
has_resource:
  - artifact: https://raw.githubusercontent.com/.../dqv-ap-no-schema.ttl
    conforms_to: http://www.w3.org/2001/XMLSchema#
```

→ CI les `is_profile_of`-sloten og genererer:

```yaml
er_profil_av:
  - http://www.w3.org/ns/dqv#
```

**Midlertidig workaround (MVP):**
Dersom ein modell er ein profil og `er_profil_av` må populerast før DX-PROF er implementert, kan det leggast inn manuelt i `annotations:`:

```yaml
# I schema.yaml
annotations:
  er_profil_av:
    - http://www.w3.org/ns/dqv#
```

CI les `annotations.er_profil_av` og inkluderer det i `metadata/modelldcat.yaml`.

**Handtering i MVP:**
- Dersom verken `data/profil/profil.yaml` eller `annotations.er_profil_av` finst → `er_profil_av` vert utelate frå `metadata/modelldcat.yaml`
- **Ikkje** utlei `er_profil_av` frå `imports:` — import er ikkje det same som profil-relasjon

**Sjå også:** [Kjende avvik](#kjende-avvik) for fullstendig oversikt over ikkje-implementerte felt i MVP.

#### `inneholder_modellelement` — frå skjemaet sine lokale klasser

CI itererer over `classes:`-blokka i skjemaet og genererer URI-ar til alle klasser som **ikkje** er importerte.

**Regel:** Ein klasse er **lokal** dersom den er definert i dette skjemaet sitt `classes:`-blokk.

**Inkluderer:**
- Alle klasser i `classes:`-blokka, inkludert:
  - Abstrakte klasser (`abstract: true`)
  - Klasser som arvar frå importerte klasser (`is_a: ImportedClass`)

**Ekskluderer:**
- `tree_root`-containerklassen (dersom `tree_root: true`)
- Klasser som berre er referert til (via `range:` eller `is_a:`), men ikkje definert i `classes:`

**URI-format:** `<default_prefix><ClassName>` (følgjer LinkML sin standard class_uri-oppløysing)

**Eksempel:**
```yaml
# dqv-ap-no-schema.yaml
default_prefix: https://data.norge.no/ap-no/dqv-ap-no/
classes:
  Datakvalitetsmaaling:          # lokal
    class_uri: dqv:QualityMeasurement
    is_a: Observasjon            # Observasjon er importert, men ikkje inkludert
  
  DqvApNoContainer:              # containerklasse
    tree_root: true              # ekskludert
```

→ CI genererer:

```yaml
inneholder_modellelement:
  - https://data.norge.no/ap-no/dqv-ap-no/Datakvalitetsmaaling
  # Observasjon er ikkje inkludert (importert)
  # DqvApNoContainer er ikkje inkludert (tree_root)
```

**Manifest-spesifikke felt som ikkje finst i Informasjonsmodell:**

| Manifest-felt | Føremål | Kan mappast til ModelDCAT? |
|---|---|---|
| `validation_policy` | Styrer kva policy CI skal validere mot | **Nei** — build/CI-konfigurasjon |
| `publish_external` | Om modellen skal publiserast til ekstern katalog | **Nei** — build/CI-konfigurasjon |
| `external_spec_label` | Menneskelesbar tittel for ekstern spec | **Ja** — via `heimeside` sin tittel |
| `generators.*` | Kva artefaktar som skal genererast | **Nei** — build/CI-konfigurasjon |
| `concepts` | URI-liste til begrep som skal publiserast | **Nei** — datafil-spesifikk logikk |

## Fordeler med ModelDCAT-datafil-basert manifest

### 1. Semantisk interoperabilitet
- Manifest vert ein standardisert RDF-ressurs som kan høstast og gjenbrukast eksternt
- Modellkatalogar kan automatisk aggregere metadata frå alle skjema utan eigenutvikla parsing
- Felles begrepskatalog, Felles datakatalog og andre system kan konsumere metadata direkte

### 2. DRY-prinsipp
- Eliminerer duplikasjon mellom `schema.yaml`-metadata og manifest
- Eitt sannheitskjelde for modellens metadata (anten i skjemaet eller i manifesten)
- Reduserer risiko for inkonsistens mellom tittel/versjon/lisens i schema vs. manifest

### 3. Validering og kvalitetssikring
- ModelDCAT-baserte manifestfiler kan validerast med LinkML-validatoren
- Policy-hierarki (bronze/silver/gold) kan gjelde for manifestet òg
- Tvingar gjennom Digdir sine Felles modelleringsregler (regel 9-11)

### 4. Uniformitet
- Same struktur for både skjema-metadata og datafil-metadata
- Enklare å forstå og vedlikehalde for nye bidragsytarar
- Kan gjenbruke eksisterande tooling (gen-doc, gen-plantuml, validering)

### 5. Utvidbarheit
- Kan leggje til nye ModelDCAT-felt (kontaktpunkt, tema, dekningsområde) utan å endre manifest-parsaren
- Kan lenke til eksterne ressursar (relaterte begrep, datasett, standardar) med standardisert syntax

## Svakheiter og utfordringar

### 1. Blanding av concerns
- Manifestet inneheld både **semantiske metadata** (tittel, beskrivelse, utgjevar) og **build-konfigurasjon** (`generators`, `validation_policy`)
- ModelDCAT er ikkje designa for build-konfigurasjon — det er eit CI/CD-domene, ikkje eit datamodelldomene
- Risiko for å forvirre kva som er «modellens metadata» vs. «byggprosessens konfigurasjon»

### 2. Duplikasjon med schema.yaml
- Mange ModelDCAT-felt (`tittel`, `beskrivelse`, `versjon`, `lisens`, `utgiver`, `endringsdato`, `status`) er allereie definerte i `schema.yaml` sine toppnivå-felt og `annotations:`
- Dersom manifest òg skal innehalde desse, må CI synkronisere eller validere konsistens
- Alternativ: la manifestet *berre* innehalde build-konfigurasjon, og generere ModelDCAT-instansar frå `schema.yaml` (som vert gjort i dag)

### 3. Kompleksitet for enkle skjema
- Små modeller (t.d. `fair-metadata`) treng kanskje ikkje full ModelDCAT-metadata
- Krev meir boilerplate enn dagens minimale manifest-format

### 4. Verkty-kompabilitet
- CI-scriptet (`Makefile`, `publish.sh`, `.github/workflows/*.yml`) må omskrivast for å parse ModelDCAT-YAML i staden for dagens flat struktur
- Eksisterande manifest-parsing-logikk må migrerast eller behaldast for bakoverkompatibilitet

### 5. Generator-konfigurasjon passar ikkje i ModelDCAT
- `generators:`-blokka (22 booleske flagg for ulike artefakttypar) har ingen naturleg plass i `Informasjonsmodell`-klassen
- Kunne modellerast som ein eigen hjelpeklasse (t.d. `GeneratorConfiguration`), men det bryt med ModelDCAT-AP-NO-standarden
- Alternativ: flytte generator-konfigurasjon til ei separat fil (t.d. `build.yaml`) og behalde ModelDCAT-manifesten semantisk rein

## Hybrid-tilnærming: Split av semantisk og build-konfigurasjon

**Forslag:** Skil manifestet i to filer:

### 1. `schema.yaml` annotations — utvida med ModelDCAT-felt
```yaml
# I schema.yaml
annotations:
  # Eksisterande Digdir-regel-metadata:
  utgiver: https://data.norge.no/organizations/991825827
  endringsdato: "2026-07-04"
  utgivelsesdato: "2023-01-01"
  status: http://purl.org/adms/status/Completed
  
  # Nye ModelDCAT-felt (valgfrie):
  tema:
    - https://psi.norge.no/los/tema/teknologi-og-digitalisering
    - https://psi.norge.no/los/tema/styring-og-administrasjon
  
  # Andre valgfrie ModelDCAT-felt:
  # dekningsomraade: https://data.geonorge.no/administrativeEnheter/nasjon/id/173163
  
  # LangString-felt krev ALLTID både nb (bokmål) og nn (nynorsk):
  # nokkelord:
  #   nb:
  #     - datakvalitet
  #     - kvalitetsmåling
  #   nn:
  #     - datakvalitet
  #     - kvalitetsmåling
```

**Viktig:** LangString-felt (`nokkelord`, `tittel`, `beskrivelse`) krev **alltid** både `nb` (bokmål) og `nn` (nynorsk). Dette er eit krav i repoet for å sikre tilgjengelegheit på begge målformer.

**Obs:** `annotations:` er kjeldekode i `schema.yaml`. `metadata/modelldcat.yaml` (i `metadata/`-katalogen) er den genererte Informasjonsmodell-instansen.

### 2. `build.yaml` — CI/CD-konfigurasjon (ikkje ModelDCAT)
```yaml
# Semantiske metadata (mappast til ModelDCAT):
external_spec_url: https://informasjonsforvaltning.github.io/dqv-ap-no/
submodels:
  - dqv-core

# Build/CI-konfigurasjon:
validation_policy: gold
publish_external: false

generators:
  jsonld_context: true
  shacl: true
  python: true
  json_schema: true
  owl: true
  rdf: true
  protobuf: true
  erdiagram: true
  docs: true
  plantuml: true
  example_rdf: false
  xsd: false
  openapi: true
  asyncapi: false
```

**Obs:** `external_spec_label` er fjerna — mkdocs-portalen kan bruke default-tekst "Offisiell spesifikasjon" eller hente tittel frå `external_spec_url` dersom nødvendig.

**Fordeler:**
- Klart skille mellom metadata (ModelDCAT) og build-konfigurasjon (ikkje-standardisert)
- `modelldcat.yaml` kan validerast mot `modelldcat-katalog-schema.yaml`
- `build.yaml` kan forenklas over tid (t.d. standardverdiar, konvensjon-over-konfigurasjon)
- CI kan generere ei `Modellkatalog`-datafil ved å aggregere alle `modelldcat.yaml`-filer

**Svakheiter:**
- To filer i staden for éi — meir fragmentering
- Krev omskriving av CI-scriptane for å lese to filer
- Risiko for at `modelldcat.yaml` og `schema.yaml` kjem ut av synk (krev validering)

## Alternativ 1: Auto-generering av ModelDCAT-metadata frå schema.yaml (implisitt)

**Dagens tilnærming (som vert brukt i CI):**

CI genererer `Informasjonsmodell`-instansar direkte frå `schema.yaml` sine toppnivå-felt og `annotations:`:

```python
# (Pseudo-kode — dagens CI-logikk)
informasjonsmodell_instans = {
    "id": schema["id"],
    "tittel": schema["title"],
    "beskrivelse": schema["description"],
    "versjonsnummer": schema["version"],
    "lisens": schema["license"],
    "utgiver": schema["annotations"]["utgiver"],
    "endringsdato": schema["annotations"]["endringsdato"],
    "utgivelsesdato": schema["annotations"]["utgivelsesdato"],
    "status": schema["annotations"]["status"],
    "heimeside": manifest["external_spec_url"],  # frå dagens manifest
    "har_del": [resolve_submodel_uri(s) for s in manifest.get("submodels", [])]
}
```

**Fordeler:**
- Ingen nye filer — `schema.yaml` er allereie sannheitskjelda
- DRY — ingen duplikasjon av metadata
- Enklare for modell-utviklarar — berre éi fil å vedlikehalde

**Svakheiter:**
- `schema.yaml` inneheld både LinkML-spesifikk struktur (`classes:`, `slots:`, `imports:`) og ModelDCAT-metadata
- Vanskeleg å leggje til ModelDCAT-felt som ikkje har naturleg plass i LinkML-skjema (t.d. `kontaktpunkt`, `tema`, `dekningsområde`)
- Manifestet er implisitt, ikkje eksplisitt — kan vere vanskeleg å inspisere kva metadata som faktisk vert publisert
- Krev at CI-logikk gjentar mapping-reglane kvar gong modellkatalog vert generert

## Alternativ 2: Genererte modelldcat.yaml-datafiler per skjema (eksplisitt)

**Tilnærming:** CI genererer ei `modelldcat.yaml`-datafil per skjema og lagrar den i same katalog som skjemaet. Datafila er ein fullstendig `Informasjonsmodell`-instans validert mot `modelldcat-katalog-schema.yaml`.

### Katalogstruktur
```
src/linkml/<domain>/<modell>/
  <modell>-schema.yaml           ← LinkML-skjema (kjeldekode)
  build.yaml                     ← build/CI-konfigurasjon (omdøypt frå manifest.yaml)
  description.md                 ← kjeldekode
  CHANGELOG.md                   ← kjeldekode
  examples/                      ← kjeldekode
  data/                          ← kjeldekode
  validation/                    ← genererte valideringsresultat
  metadata/                      ← genererte metadata-filer (ny katalog)
    modelldcat.yaml              ← generert Informasjonsmodell-instans
```

### Generering (CI-steg)
```bash
# Steg 1: Generer Informasjonsmodell-instans (metadata/modelldcat.yaml)
make gen-informasjonsmodell-instance SCHEMA=src/linkml/ap-no/dqv-ap-no/dqv-ap-no-schema.yaml

# Steg 2: Valider Informasjonsmodell-instans mot modelldcat-katalog-schema.yaml
make validate-informasjonsmodell SCHEMA=src/linkml/ap-no/dqv-ap-no/dqv-ap-no-schema.yaml

# Steg 3: Generer Modellkatalog-instans (samlar alle Informasjonsmodell-instansar)
make gen-modellkatalog-instance
```

### Eksempel: generert modelldcat.yaml
```yaml
# src/linkml/ap-no/dqv-ap-no/metadata/modelldcat.yaml
# Generert av CI frå dqv-ap-no-schema.yaml, build.yaml, CODEOWNERS og DX-PROF-data
# Ikkje rediger manuelt — vert overskrive ved kvar CI-køyring

id: https://data.norge.no/ap-no/dqv-ap-no
tittel:
  nb: "DQV-AP-NO"
beskrivelse:
  nb: "Norsk applikasjonsprofil for datakvalitet basert på W3C DQV."
versjonsnummer: "1.0.0"
lisens: https://data.norge.no/nlod/no/2.0
utgiver: https://data.norge.no/organizations/991825827
endringsdato: "2026-07-08"
utgivelsesdato: "2023-01-01"
status: http://purl.org/adms/status/Completed

# Frå build.yaml (tidlegare manifest.yaml)
heimeside: https://informasjonsforvaltning.github.io/dqv-ap-no/
har_del:
  - https://data.norge.no/ap-no/dqv-ap-no/dqv-core

# Frå schema.yaml annotations
tema:
  - https://psi.norge.no/los/tema/teknologi-og-digitalisering
  - https://psi.norge.no/los/tema/styring-og-administrasjon

# Frå CODEOWNERS.md
kontaktpunkt:
  har_referanse: https://www.digdir.no/om-oss/kontakt-oss/887
  har_organisasjonsnamn: Digitaliseringsdirektoratet

# Frå data/profil/profil.yaml (DX-PROF)
er_profil_av:
  - http://www.w3.org/ns/dqv#

# Frå skjemaet sine lokale klasser
inneholder_modellelement:
  - https://data.norge.no/ap-no/dqv-ap-no#Datakvalitetsmaaling
  - https://data.norge.no/ap-no/dqv-ap-no#Datakvalitetsdimensjon

# Frå genererte artefaktar i generated/ap-no/dqv-ap-no/
finnes_i_format:
  - https://raw.githubusercontent.com/.../dqv-ap-no-schema.ttl
  - https://raw.githubusercontent.com/.../dqv-ap-no-schema.json
  - https://raw.githubusercontent.com/.../dqv-ap-no-schema.owl
  - https://raw.githubusercontent.com/.../dqv-ap-no-schema.shacl.ttl
```

### Genereringslogikk (make gen-informasjonsmodell-instance)
```python
# Pseudo-kode
def generate_modelldcat_yaml(schema_path):
    schema = load_yaml(schema_path)
    build_config = load_yaml(schema_path.replace("-schema.yaml", "/build.yaml"))
    codeowners = parse_codeowners(schema_path)
    dx_prof = load_dx_prof_data(schema_path)
    local_classes = extract_local_classes(schema)
    generated_artifacts = discover_artifacts(schema_path)
    
    modelldcat = {
        # Frå schema.yaml toppnivå-felt
        "id": schema["id"],
        "tittel": schema["title"],
        "beskrivelse": schema["description"],
        "versjonsnummer": schema["version"],
        "lisens": schema["license"],
        
        # Frå schema.yaml annotations (ModelDCAT-metadata)
        "utgiver": schema["annotations"]["utgiver"],
        "endringsdato": schema["annotations"]["endringsdato"],
        "utgivelsesdato": schema["annotations"]["utgivelsesdato"],
        "status": schema["annotations"]["status"],
        "tema": schema["annotations"].get("tema", []),
        "dekningsomraade": schema["annotations"].get("dekningsomraade"),
        "nokkelord": schema["annotations"].get("nokkelord"),
        
        # Frå build.yaml (CI/CD-konfigurasjon)
        "heimeside": build_config.get("external_spec_url"),
        "har_del": resolve_submodel_uris(build_config.get("submodels", [])),
        
        # Auto-generert frå CODEOWNERS.md
        "kontaktpunkt": extract_contact_from_codeowners(codeowners, schema_path),
        # → {"har_referanse": contact_uri, "har_organisasjonsnamn": name}
        
        # Frå annotations (MVP workaround) eller DX-PROF-data (framtidig)
        "er_profil_av": schema["annotations"].get("er_profil_av", dx_prof.get("is_profile_of", [])),
        "inneholder_modellelement": [cls["class_uri"] for cls in local_classes],
        "finnes_i_format": generated_artifacts
    }
    
    # Fjern None-verdiar og tomme lister
    modelldcat = {k: v for k, v in modelldcat.items() if v}
    
    output_path = schema_path.replace("-schema.yaml", "/metadata/modelldcat.yaml")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    write_yaml(output_path, modelldcat)
```

### Modellkatalog-generering (make gen-modellkatalog-instance)

**Output:** `generated/modellkatalog.yaml` (ein `Modellkatalog`-instans)

**Struktur:**
```yaml
id: https://data.norge.no/modellkatalog
tittel:
  nb: "Felles modellkatalog for LinkML-modellar"
  nn: "Felles modellkatalog for LinkML-modellar"
beskrivelse:
  nb: "Samling av alle informasjonsmodellar i linkml-datamodellering-no-repoet."
  nn: "Samling av alle informasjonsmodellar i linkml-datamodellering-no-repoet."
utgiver: https://data.norge.no/organizations/991825827
kontaktpunkt:
  har_referanse: https://www.digdir.no/om-oss/kontakt-oss/887
  har_organisasjonsnamn: Digitaliseringsdirektoratet
modell:
  - <innhald frå src/linkml/ap-no/dcat-ap-no/metadata/modelldcat.yaml>
  - <innhald frå src/linkml/ap-no/dqv-ap-no/metadata/modelldcat.yaml>
  - ...
```

**Filter:** Inkluder alle skjema (også `publish_external: false`) — modellkatalogen er ein intern ressurs, ikkje ekstern publisering.

**Pseudo-kode:**
```python
def generate_modellkatalog():
    all_modelldcat_files = glob("src/linkml/**/metadata/modelldcat.yaml")
    
    modellkatalog = {
        "id": "https://data.norge.no/modellkatalog",
        "tittel": {
            "nb": "Felles modellkatalog for LinkML-modellar",
            "nn": "Felles modellkatalog for LinkML-modellar"
        },
        "beskrivelse": {
            "nb": "Samling av alle informasjonsmodellar i linkml-datamodellering-no-repoet.",
            "nn": "Samling av alle informasjonsmodellar i linkml-datamodellering-no-repoet."
        },
        "utgiver": "https://data.norge.no/organizations/991825827",
        "kontaktpunkt": {
            "har_referanse": "https://www.digdir.no/om-oss/kontakt-oss/887",
            "har_organisasjonsnamn": "Digitaliseringsdirektoratet"
        },
        "modell": [load_yaml(f) for f in sorted(all_modelldcat_files)]
    }
    
    write_yaml("generated/modellkatalog.yaml", modellkatalog)
```

### Fordeler

#### 1. Eksplisitt og inspiserbar
- Kvar modell har ei lesbar `modelldcat.yaml`-fil som viser **nøyaktig** kva metadata som vert publisert
- Enklare å debugge og verifisere at metadata er korrekt
- Git-diff viser endringar i ModelDCAT-metadata eksplisitt

#### 2. Enklare modellkatalog-generering
- `make gen-modellkatalog-instance` treng berre å samle eksisterande `metadata/modelldcat.yaml`-filer
- Ingen kompleks logikk for å parse `schema.yaml`, `manifest.yaml`, `CODEOWNERS`, DX-PROF, etc. — alt er allereie gjort
- Reduserer risiko for feil i modellkatalog-generering

#### 3. Validering av metadata

**Validering av `metadata/modelldcat.yaml`:**

**Policy:** Same som skjemaet sin `validation_policy` i `build.yaml` (bronze/silver/gold)

**Valideringssteg:**
1. LinkML-validering mot `modelldcat-katalog-schema.yaml`
2. Policy-validering (bronze/silver/gold-sjekkar)
3. LangString-sjekk: alle LangString-felt (`tittel`, `beskrivelse`, `nokkelord`) har både `nb` og `nn`

**Feilhandtering:**
- Validering feiler → CI blokkerer (exit 1)
- Warning-nivå feil → CI held fram, men loggar warning

**Kommando:**
```bash
make validate-informasjonsmodell SCHEMA=src/linkml/ap-no/dqv-ap-no/dqv-ap-no-schema.yaml
# Les build.yaml for å finne validation_policy
# Validerer metadata/modelldcat.yaml mot modelldcat-katalog-schema.yaml (Informasjonsmodell-klassen) med gitt policy
```

**Fordeler:**
- Fangar opp feil i metadata tidleg (før modellkatalog vert publisert)
- Sikrar at metadata oppfyller same kvalitetskrav som skjemaet
- Valider LangString-krav (både nb og nn)

#### 4. DRY — single source of truth per kjelde
- `schema.yaml` toppnivå → tittel, beskrivelse, versjon, lisens
- `schema.yaml` annotations → utgiver, status, endringsdato, utgivelsesdato, tema, dekningsomraade, nokkelord
- `build.yaml` (tidlegare `manifest.yaml`) → heimeside, har_del, validation_policy, generators
- `CODEOWNERS.md` YAML-frontmatter → kontaktpunkt (`contact_uri` → `har_referanse`, `name` → `har_organisasjonsnamn`)
- `annotations.er_profil_av` (MVP workaround) eller `data/profil/profil.yaml` (framtidig DX-PROF) → er_profil_av
- `generated/<domain>/<modell>/` → finnes_i_format
- `schema.yaml` sine `classes:` → inneholder_modellelement

Ingen duplikasjon — `metadata/modelldcat.yaml` er ein **samansett** artefakt generert frå 6 kjelder (ikkje 7 — fjerna `metadata.yaml`).

#### 5. Gjenbruk av ModelDCAT-metadata
- Andre verktøy kan lese `modelldcat.yaml` direkte utan å måtte forstå LinkML-skjemastruktur
- Ekstern harvesting av metadata vert enklare (ein fil, eitt format)
- Kan publiserast til GitHub Releases som standalone artefakt

#### 6. Konsistent med dagens artefakt-struktur
- Liknande prinsipp som `generated/<domain>/<modell>/*.ttl`, `*.json`, `*.owl`
- `modelldcat.yaml` er eit generert build-artefakt som kan reproduserast frå kjeldekode
- Passar naturleg inn i `make gen-*`-mønsteret

### Svakheiter

#### 1. Ekstra fil å generere
- CI må køyre `make gen-informasjonsmodell-instance` for kvar skjema
- Aukar byggtid (men kan køyrast parallelt, som PlantUML-generering)

#### 2. Risiko for at generert fil vert redigert manuelt

**Førebygging:**
- Tydelig kommentar i toppen av kvar generert fil: `# Generert av CI — ikkje rediger manuelt`
- CI-sjekk som validerer at `modelldcat.yaml` samsvarar med kjeldene (detekterer manuell redigering)
- `.gitattributes`: `src/linkml/**/metadata/** linguist-generated=true`

**Git-handtering:**

**Strategi:** Commit genererte `metadata/modelldcat.yaml`-filer til repo, akkurat som `validation/`-katalogar.

**Kvifor commit:**
- **Inspiserbarheit** — utviklar kan sjå endringar i metadata via git-diff
- **Reproduserbarheit** — tidlegare versjonar av metadata er tilgjengeleg i git-historikk
- **Debugging** — enklare å verifisere at metadata er korrekt utan å køyre CI lokalt

**CI-workflow:**
1. **Lokalt:** Utviklar køyrer `make gen-informasjonsmodell-instance` etter endringar i `schema.yaml`, `build.yaml` eller `annotations:`
2. **Lokalt:** Utviklar committar både kjeldekode og generert `metadata/modelldcat.yaml`
3. **CI:** Validerer at `metadata/modelldcat.yaml` samsvarar med kjeldene (detekterer manuell redigering)

**Merge-konflikt:** Sjeldan, sidan `metadata/modelldcat.yaml` er deterministisk generert — løys ved å ta `main`-versjonen og re-køyre `make gen-informasjonsmodell-instance`.

#### 3. Plassering av generert fil

Tre alternativ for plassering av `modelldcat.yaml`:

##### Alternativ A: `generated/<domain>/<modell>/modelldcat.yaml`
**Plassering:** Saman med andre genererte artefaktar (`.ttl`, `.json`, `.owl`, etc.)

**Fordeler:**
- Konsistent med resten av repoets genererte artefaktar
- Tydeleg at dette er eit build-artefakt, ikkje kjeldekode
- `generated/` vert allereie ignorert av git-diff i mange tilfelle
- Ingen risiko for at nokon tenkjer det skal redigerast manuelt

**Svakheiter:**
- Lenger unna skjemaet — vanskeleg å finne raskt når ein jobbar med `src/linkml/<domain>/<modell>/`
- Må navigere til to stader for å sjå skjema + metadata
- `generated/` vert bygt seinare i pipeline — `modelldcat.yaml` kan ikkje brukast av tidlege CI-steg

**Eigna for:** Konsistens med artefakt-filosofi, dersom `modelldcat.yaml` berre skal brukast i slutten av pipeline

##### Alternativ B: `src/linkml/<domain>/<modell>/modelldcat.yaml`
**Plassering:** Direkte i same katalog som skjemaet

**Fordeler:**
- Nær skjemaet — lett å finne og inspisere
- Kan brukast av tidlege CI-steg (før `make gen-*` køyrer)
- Liknande plassering som `manifest.yaml` (no `build.yaml`)
- Enklare å sjå samanheng mellom skjema og metadata

**Svakheiter:**
- Bryt konvensjonen om at genererte filer ligg i `generated/`
- Kan forvekslast med kjeldekode (trass i kommentar om "generert")
- Må markerast eksplisitt som generert i `.gitattributes`

**Eigna for:** Inspiserbarheit og nærleik til kjeldekode

##### Alternativ C1: `src/linkml/<domain>/<modell>/generated/modelldcat.yaml`
**Plassering:** Lokal `generated/`-underkatalog i skjemaet sin katalog

**Fordeler:**
- Tydeleg at innhaldet er generert, ikkje kjeldekode
- Konsistent med prinsippet om at genererte filer ligg i `generated/`, men lokalt i staden for globalt
- Kan brukast av tidlege CI-steg
- Opnar for andre genererte metadata-filer i framtida (t.d. `dx-prof.yaml`)
- Presedens: `validation/` er allereie ein generert underkatalog

**Svakheiter:**
- Beskriv KORLEIS innhaldet vart til, ikkje KVA det er
- Kan forvekslast med global `generated/`-katalog (trass i lokal plassering)
- Mindre semantisk presis enn `metadata/`

**Eigna for:** Konsistens med artefakt-filosofi

##### Alternativ C2: `src/linkml/<domain>/<modell>/metadata/modelldcat.yaml`
**Plassering:** Lokal `metadata/`-underkatalog i skjemaet sin katalog

**Fordeler:**
- **Semantisk presis:** Beskriv KVA innhaldet er (metadata om modellen), ikkje KORLEIS det vart til
- Tydeleg avgrensing frå global `generated/` — mindre forveksling
- Kortare og meir lesbart namn (`metadata` vs. `generated`)
- Naturleg samling av metadata-artefaktar: `modelldcat.yaml`, `dx-prof.yaml`, framtidig `prov.yaml`, `dcat-profile.yaml`, osv.
- Skil seg frå `validation/` (som er ein spesifikk type generert output) — metadata er meir overordna
- Indikerer at dette er **metadata om skjemaet**, ikkje artefaktar **frå** skjemaet (som `.ttl`, `.json`, `.owl`)

**Katalogstruktur:**
```
src/linkml/<domain>/<modell>/
  <modell>-schema.yaml           ← kjeldekode
  build.yaml                     ← build/CI-konfigurasjon
  description.md                 ← kjeldekode
  CHANGELOG.md                   ← kjeldekode
  examples/                      ← kjeldekode
  data/                          ← kjeldekode
  validation/                    ← generert (policy-resultat)
  metadata/                      ← generert (metadata om modellen)
    modelldcat.yaml              ← Informasjonsmodell-instans
    dx-prof.yaml                 ← DX-PROF-metadata (framtidig)
    prov.yaml                    ← PROV-metadata (framtidig)
```

**Svakheiter:**
- Mindre tydeleg at innhaldet er generert (treng kommentar i fila eller `.gitattributes`)
- Kan forvekslast med kjeldekode-metadata (men innhaldet er tydeleg generert når ein opnar fila)
- Ny konvensjon — ikkje brukt andre stader i repoet

**Eigna for:** Semantisk tydelege katalognamn som beskriv innhald, ikkje opphav

##### Samanlikning: `generated/` vs. `metadata/`

| Aspekt | `generated/` | `metadata/` |
|---|---|---|
| **Semantikk** | Beskriv opphav (korleis) | Beskriv innhald (kva) |
| **Tydelege som generert** | ✅ Svært tydeleg | ⚠️ Treng kommentar/`.gitattributes` |
| **Konflikt med global `generated/`** | ⚠️ Kan forvekslast (trass i lokal) | ✅ Ingen konflikt |
| **Lesbarheit** | `generated/modelldcat.yaml` | `metadata/modelldcat.yaml` ← kortare |
| **Framtidig innhald** | Alle genererte filer (også ikkje-metadata) | Berre metadata-filer |
| **Konsistens med `validation/`** | Begge er genererte katalogar | `validation/` er spesifikk, `metadata/` er overordna |
| **Presedens i repo** | Liknande global `generated/` | Ingen — ny konvensjon |

##### Anbefaling: Alternativ C2 (`src/linkml/<domain>/<modell>/metadata/modelldcat.yaml`)

`metadata/` er **semantisk meir presis** og **reduserer forveksling** med global `generated/`-katalog. Argumenta:

1. **Semantisk presisjon:** `metadata/` beskriv KVA innhaldet er (metadata om modellen), ikkje berre at det er generert
2. **Tydeleg avgrensing:** Skil lokale metadata frå globale artefaktar i `generated/<domain>/<modell>/`
3. **Framtidig-sikker:** Naturleg heim for alle metadata-artefaktar (`modelldcat.yaml`, `dx-prof.yaml`, `prov.yaml`, etc.)
4. **Kortare:** `metadata/` er enklare å lese og navigere enn `generated/`
5. **Mindre forveksling:** `generated/` kan tolkast som "lokal versjon av global `generated/`", medan `metadata/` er tydeleg forskjellig

**Handtering av "generert"-aspektet:**
- Kommentar i kvar fil: `# Generert av CI — ikkje rediger manuelt`
- `.gitattributes`: `src/linkml/**/metadata/** linguist-generated=true`

**Ekstra:** `validation/` er eit presens for domene-spesifikke genererte katalogar — `metadata/` følgjer same prinsipp, men med meir semantisk presist namn.

#### 4. Git-churn ved kvar endring
- Kvar endring i `schema.yaml`, `build.yaml`, `CODEOWNERS`, eller DX-PROF vil regenerere `modelldcat.yaml`
- Kan skape mykje git-diff dersom `endringsdato` oppdaterast ved kvar commit
- **Løysing:** `endringsdato` bør berre oppdaterast ved semantiske endringar (same som i dag)

**Obs:** Med plassering i `src/linkml/<domain>/<modell>/metadata/`, kan `metadata/`-katalogen markerast som `linguist-generated` for å redusere støy i git-diff.

### Samanlikning: Implisitt vs. Eksplisitt

| Aspekt | Implisitt (dagens) | Eksplisitt (generert modelldcat.yaml) |
|---|---|---|
| **Inspiserbarheit** | Vanskeleg — må lese CI-kode for å sjå kva som vert generert | Enkel — `modelldcat.yaml` viser eksakt innhald |
| **Validering** | Skjer berre i modellkatalog-generering | Kan skje per skjema som ein del av `make validate` |
| **Modellkatalog-generering** | Kompleks — må parse mange kjelder | Enkel — berre samle eksisterande filer |
| **Git-diff** | Ingen (metadata er implisitt) | Viser eksplisitt kva metadata som endrast |
| **DRY** | Same nivå — begge generer frå same kjelder | Same nivå — generert artefakt |
| **Feilsøking** | Vanskeleg — må rekonstruere kva CI gjorde | Enkel — kan inspisere den genererte fila |
| **Ekstra kompleksitet** | Ingen ekstra filer | Må generere og vedlikehalde ekstra fil |

### Anbefaling: Eksplisitt generering

Genererte `modelldcat.yaml`-datafiler gir **mykje betre inspiserbarheit og validering** mot moderat auka kompleksitet. Det passar godt med repoet sin filosofi om eksplisitte, validerbare artefaktar.

**Plassering:** `src/linkml/<domain>/<modell>/modelldcat.yaml` (nær skjemaet, markert som generert i `.gitattributes`)

**CI-workflow:**
1. `make gen-modelldcat` for alle skjema (parallelt, som PlantUML-generering)
2. `make validate-modelldcat` for alle genererte `modelldcat.yaml`-filer
3. `make gen-modellkatalog` samlar alle `modelldcat.yaml`-filer til `generated/modellkatalog.yaml`

## Anbefaling

### Primær anbefaling: Genererte modelldcat.yaml-datafiler (Alternativ 2)

**Split dagens `manifest.yaml` i to, og utvid schema.yaml annotations:**
1. **`build.yaml`** — CI/CD-konfigurasjon (validation_policy, generators, publish_external)
2. **`schema.yaml` annotations** — utvida med ModelDCAT-felt (tema, dekningsomraade, nokkelord)
3. **`metadata/modelldcat.yaml`** — generert `Informasjonsmodell`-instans (validert mot ModelDCAT-skjemaet)

**Katalogstruktur:**
```
src/linkml/<domain>/<modell>/
  <modell>-schema.yaml    ← kjeldekode (LinkML-struktur + annotations med ModelDCAT-felt)
  build.yaml              ← kjeldekode (CI/CD-konfigurasjon, omdøypt frå manifest.yaml)
  description.md
  CHANGELOG.md
  examples/
  data/
  validation/             ← generert (valideringsresultat)
  metadata/               ← generert (metadata-filer)
    modelldcat.yaml       ← generert Informasjonsmodell-instans
```

**CI-workflow:**
```bash
# Steg 1: Generer Informasjonsmodell-instans frå 6 kjelder
make gen-informasjonsmodell-instance SCHEMA=src/linkml/ap-no/dqv-ap-no/dqv-ap-no-schema.yaml
# Les: schema.yaml (toppnivå + annotations), build.yaml, CODEOWNERS, DX-PROF-data, lokale klasser, artefaktar
# Skriv: metadata/modelldcat.yaml (ein Informasjonsmodell-instans)

# Steg 2: Valider Informasjonsmodell-instans mot modelldcat-katalog-schema.yaml
make validate-informasjonsmodell SCHEMA=src/linkml/ap-no/dqv-ap-no/dqv-ap-no-schema.yaml

# Steg 3: Generer Modellkatalog-instans (samlar alle Informasjonsmodell-instansar)
make gen-modellkatalog-instance  # → generated/modellkatalog.yaml
```

**Kvifor dette er den beste løysinga:**
- **Eksplisitt og inspiserbar:** Kvar modell har ei lesbar `modelldcat.yaml`-fil som viser nøyaktig kva metadata som vert publisert
- **Enklare modellkatalog-generering:** `make gen-modellkatalog` treng berre å samle eksisterande filer — ingen kompleks mapping-logikk
- **Validerbar:** `modelldcat.yaml` kan validerast mot ModelDCAT-skjemaet som ein del av CI
- **DRY:** Ingen duplikasjon — data vert henta frå kjeldene (`schema.yaml`, `build.yaml`, `CODEOWNERS`, DX-PROF-data, lokale klasser, genererte artefaktar)
- **Git-diff synleg:** Endringar i ModelDCAT-metadata vert eksplisitt synlege i git-historikk
- **Konsistent med artefakt-filosofi:** Liknande prinsipp som `.ttl`, `.json`, `.owl` — generert, reproduserbar, validerbar

**Viktig:** Markerast som generert i `.gitattributes`:
```
src/linkml/**/metadata/** linguist-generated=true
```

Dette dekkjer `modelldcat.yaml` og andre framtidige genererte metadata-filer i `metadata/`-underkatalogen.

### Sekundær tilnærming: Implisitt generering (Alternativ 1)

**For tilfelle der ein ikkje ønskjer ekstra filer:**
- Behald `manifest.yaml` (omdøypt til `build.yaml`)
- CI genererer `Informasjonsmodell`-instansar direkte til `generated/modellkatalog.yaml` utan mellomsteg
- Ingen `modelldcat.yaml`-fil per skjema

**Svakheit:** Vanskeleg å inspisere kva metadata eit enkelt skjema faktisk publiserer — må rekonstruere frå CI-logikk eller sjå på den samla modellkatalogen.

### Framtidig utvidelse (langt sikt)

**Dersom `schema.yaml` skal utvidast med metadata:**
Vurder eit `metadata:`-felt i `schema.yaml` for felt som **ikkje** har naturleg plass i LinkML-skjemastruktur (tema, kontaktpunkt, dekningsområde). Dette krev anten:
- LinkML-utvidelse for å støtte arbitrary `metadata:`-blokk
- Eller bruk av `annotations:` for alle ModelDCAT-felt (mindre ryddig)

## Kjende avvik

Desse ModelDCAT-felta er ikkje implementerte i MVP, men kan leggast til seinare:

### 1. `er_profil_av` — krev DX-PROF LinkML-implementering

**Status:** Ikkje implementert i MVP — DX-PROF-standarden må først modellerast i LinkML.

**Midlertidig workaround:** Bruk `annotations.er_profil_av` for å eksplisitt deklarere profil-relasjonar:

```yaml
# I schema.yaml
annotations:
  er_profil_av:
    - http://www.w3.org/ns/dqv#
```

**Framtidig løysing:** Når `dx-prof-schema.yaml` er implementert, les `is_profile_of` frå `data/profil/profil.yaml` (DX-PROF `Profile`-instans).

**Sjå:** Seksjonen «`er_profil_av` — kjent avvik» over for detaljar.

### 2. Andre potensielle avvik (dersom dei dukkar opp under implementasjon)

Dokumenter her dersom andre ModelDCAT-felt krev funksjonalitet som ikkje finst i MVP.

---

## Konklusjon

**Manifest-filer kan i prinsippet uttrykkas som `Informasjonsmodell`-datafiler**, men ei ren 1:1-migrering vil ikkje fungere fordi dagens manifest inneheld både **semantiske metadata** (som høyrer heime i ModelDCAT) og **build-konfigurasjon** (som ikkje gjer det).

**Hovudargumentet for splitting:** Build-konfigurasjon (`generators`, `validation_policy`, `publish_external`) bør ikkje blandast med semantiske metadata (tittel, versjon, tema, utgjevar). Den fyrste er ein implementasjonsdetalj; den andre er ein del av modellens identitet og skal publiserast som RDF.

**Primær anbefaling: Genererte `modelldcat.yaml`-datafiler per skjema (Alternativ 2)**

Denne tilnærminga gir:
- **Eksplisitt inspiserbarheit** av kva metadata som vert publisert
- **Enklare modellkatalog-generering** (berre samle eksisterande filer)
- **Validering** av metadata mot ModelDCAT-skjemaet per skjema
- **DRY** ved å generere frå eksisterande kjelder (schema.yaml, build.yaml, CODEOWNERS, DX-PROF, lokale klasser, artefaktar)
- **Git-synleg historikk** over metadata-endringar

**Implementasjonssteg:**
1. Omdøp `manifest.yaml` → `build.yaml` (berre build/CI-konfigurasjon)
2. Utvid `schema.yaml` annotations med `tema:` (og eventuelt `dekningsomraade`, `nokkelord`)
3. Opprett `src/linkml/<domain>/<modell>/metadata/`-katalog for kvar modell
4. Implementer `make gen-informasjonsmodell-instance` som les 6 kjelder og genererer `metadata/modelldcat.yaml`:
   - `schema.yaml` toppnivå (tittel, beskrivelse, versjon, lisens)
   - `schema.yaml` annotations (utgiver, status, endringsdato, utgivelsesdato, tema, dekningsomraade, nokkelord)
   - `build.yaml` (heimeside, har_del)
   - `CODEOWNERS.md` (kontaktpunkt)
   - `data/profil/profil.yaml` (DX-PROF is_profile_of)
   - Skjemaet sine lokale klasser (inneholder_modellelement)
   - Genererte artefaktar (finnes_i_format)
5. Implementer `make validate-informasjonsmodell` som validerer genererte Informasjonsmodell-instansar mot `modelldcat-katalog-schema.yaml`
6. Implementer `make gen-modellkatalog-instance` som samlar alle `metadata/modelldcat.yaml`-filer til ein Modellkatalog-instans
7. Markerast `src/linkml/**/metadata/**` som `linguist-generated=true` i `.gitattributes`

## Avklarte antakelser

Alle kritiske antakelser for implementasjon er avklarte og dokumenterte i specen:

1. ✅ **CODEOWNERS.md parsing** — YAML-frontmatter med `organizations.name` → `har_organisasjonsnamn`, `contact_uri` → `har_referanse`
2. ✅ **DX-PROF** — kjent avvik (krev LinkML-implementering), MVP workaround via `annotations.er_profil_av`
3. ✅ **finnes_i_format** — GitHub raw URL, flat liste, kun eksisterande filer i `generated/<domain>/<modell>/`
4. ✅ **Lokale klasser** — definert i `classes:`, ekskluder `tree_root`, inkluder abstrakte klasser
5. ✅ **Tittel/beskrivelse LangString** — `title` → `tittel.nb`, valgfri `annotations.tittel_nn` → `tittel.nn`
6. ✅ **build.yaml struktur** — behald `external_spec_url` og `submodels`, fjern `external_spec_label`
7. ✅ **Modellkatalog** — `generated/modellkatalog.yaml` med eigen metadata, inkluder alle skjema
8. ✅ **Validering** — same policy som skjema (`build.yaml`), CI blokkerer ved feil
9. ✅ **Git-handtering** — commit `metadata/modelldcat.yaml` til repo, CI validerer mot kjelder
10. ✅ **Namnekonflikt** — løyst (ingen `metadata.yaml`-kjeldekode, berre `metadata/`-katalog)

Sjå seksjonane over for detaljert dokumentasjon av kvar avklaring.

## Tiltak

Specen er klar for implementasjon. Brukaren avgjer når implementasjonen skal starte.

## Utført

**Status:** Analyse og design fullført. Specen dokumenterer:

1. ✅ Evaluering av manifest.yaml som ModelDCAT-datafil
2. ✅ Anbefaling: Split i `build.yaml` (CI/CD) og genererte `metadata/modelldcat.yaml` (Informasjonsmodell-instansar)
3. ✅ Mapping av 6 kjelder til ModelDCAT-felt
4. ✅ LangString-krav (nb + nn)
5. ✅ CODEOWNERS.md parsing-logikk
6. ✅ DX-PROF som kjent avvik (MVP workaround via annotations)
7. ✅ Make-target-namnekonvensjon: `gen-informasjonsmodell-instance` og `gen-modellkatalog-instance`
8. ✅ Git-handtering: commit genererte filer til repo
9. ✅ Validering: same policy som skjema
10. ✅ Alle 10 antakelser avklart

**Neste steg:** Implementering av `make gen-informasjonsmodell-instance` og `make gen-modellkatalog-instance` i Makefile og Python-script.

