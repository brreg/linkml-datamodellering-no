# Metadata-krav i bronze-policy basert på Digdir modelleringsregler

## Bakgrunn

Digdir har publisert [Felles modelleringsregler for offentlig forvaltning](https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029)
— 15 reglar for informasjonsmodellar i norsk offentleg sektor. Fleire av desse
regulerer krav til metadata på sjølve modellen.

Den noverande bronze-policyen (`src/mcp-linkml-validator/policies/bronze.yaml`)
fangar allereie nokre av desse krava, men er ufullstendig. Denne spesifikasjonen
foreslår konkrete endringar slik at bronze-policyen vert eit maskinlesbart uttrykk
for dei delane av Digdir-reglane som er direkte sjekkerbare på eit LinkML-skjema.

---

## Gjennomgang av Digdir-reglane og kopling til bronze

| # | Regel | Krav til modell | Noverande dekning | Forslag |
|---|---|---|---|---|
| 1 | **Forståelighet** | Modellen og dens elementer skal ha forståelige navn og gode beskrivelser | `description` og `title` som warning | Sjå under |
| 2 | **Meningsfullhet** | Navn skal gjenspeile innholdet | `title` som warning | Sjå under |
| 3 | **Navne- og skrivekonvensjoner** | Klasser: PascalCase; slots/attributtar: snake_case | Ikkje sjekka | Ny warning-sjekk |
| 4 | **Identifiserbarhet** | Modellen og dens elementer skal ha persistente URI-ar | `id` som error; `class_uri`/`slot_uri` som warning | Sjå under |
| 7 | **Tilgjengeliggjøring** | Modellen skal vere fritt tilgjengeleg på internett | Ikkje sjekka | Ny warning-sjekk |
| 9 | **Datering** | Angi publiserings-, endrings- og versjonsinformasjon | `version` som warning | Behold |
| 10 | **Ansvar** | Ansvar for modellen skal vere klart og tydeleg | Ikkje sjekka | Delvis via `default_prefix` |
| 11 | **Modellstatus** | Angi status (under utarbeidelse, ferdigstilt, foreldet …) | Ikkje sjekka | Utanfor scope (sjå under) |
| 13 | **Begreper** | Knytt modellelement til begrep i felles begrepskatalog | `annotations.begrepsidentifikator` som warning | Behold |

---

## Foreslåtte endringar

### 1. `schema.title` — frå warning til error

**Grunngiving:** Regel 1 (*Forståelighet*) og Regel 2 (*Meningsfullhet*) krev at
modellen har eit forståeleg namn som speglar innhaldet. Det tekniske `name`-feltet
(kebab-case) dekker ikkje dette åleine. Utan `title` er modellen vanskeleg å
identifisere i katalogvisningar og dokumentasjon.

**Endring:** Flytt `title` frå `recommended.schema` til `required.schema`.

```yaml
required:
  schema:
    - id
    - name
    - title      # ← ny
```

---

### 2. `schema.default_prefix` — ny required-sjekk (error)

**Grunngiving:** Regel 4 (*Identifiserbarhet*) krev at modellens element har
persistente URI-ar. I LinkML er `default_prefix` mekanismen som gir klasser og
slots fallback-URI viss `class_uri`/`slot_uri` manglar. Utan ein gyldig
`default_prefix` kan ikkje elementa adresserast globalt. Konvensjonen i dette
repoet krev absolutt HTTPS-URL med avsluttande `/`.

**Nye sjekkar:**

```yaml
checks:

  schema_has_default_prefix:
    severity: error
    description: >
      schema.default_prefix skal vere til stades. Utan default_prefix kan ikkje
      modellelement adresserast med persistente URI-ar (Digdir-regel 4:
      Identifiserbarhet).
    check: schema_has_default_prefix

  default_prefix_is_https_uri:
    severity: error
    description: >
      schema.default_prefix skal vere ein absolutt HTTPS-URI som sluttar med '/'.
      Sikrar at genererte element-URI-ar er globalt unike og persistente
      (Digdir-regel 4: Identifiserbarhet).
    check: default_prefix_is_https_uri
```

---

### 3. `schema.license` — ny recommended-sjekk (warning)

**Grunngiving:** Regel 7 (*Tilgjengeliggjøring*) seier modellen «skal være fritt
tilgjengelig på internett». Ei open lisens er ein føresetnad for fri tilgang og
gjenbruk. I LinkML-skjema vert dette uttrykt via `license:`-feltet.

**Ny sjekk:**

```yaml
checks:

  schema_has_license:
    severity: warning
    description: >
      schema.license bør vere til stades med URI til ein open lisens
      (t.d. CC BY 4.0). Støttar Digdir-regel 7 (Tilgjengeliggjøring) om at
      modellen skal vere fritt tilgjengeleg.
    check: schema_has_license
```

---

### 4. Namnekonvensjonar — ny warning-sjekk

**Grunngiving:** Regel 3 (*Navne- og skrivekonvensjoner*) krev:
- Klasser og objekttypar: substantiv med **stor forbokstav** (PascalCase)
- Relasjonar og attributtar: **liten forbokstav** (snake_case for LinkML)

Dette er allereie reflektert i modelleringsprinsippa i CLAUDE.md, men vert ikkje
validert maskinelt.

**Nye sjekkar:**

```yaml
checks:

  class_names_pascal_case:
    severity: warning
    description: >
      Klassenamn skal starte med stor forbokstav (PascalCase). Følgjer
      Digdir-regel 3 (Navne- og skrivekonvensjoner) og gjer klasser
      skiljbare frå slot- og attributtnamn.
    check: class_names_pascal_case

  slot_names_snake_case:
    severity: warning
    description: >
      Slotnamn skal bruke liten forbokstav og understrek (snake_case). Følgjer
      Digdir-regel 3 (Navne- og skrivekonvensjoner).
    check: slot_names_snake_case
    exclude_schemas:
      - fint-administrasjon    # FINT-skjema arvar camelCase frå FINT API-spec
      - fint-arkiv
      - fint-common
      - fint-okonomi
      - fint-personvern
      - fint-ressurs
      - fint-utdanning
```

*Merk: FINT-skjema er unntatt fordi dei arvar namngjeving frå FINT API-spesifikasjonen
(camelCase-konvensjon er bevisst, ikkje ein feil).*

---

## Regel 9, 10 og 11 — realiserast via `annotations` i skjema-YAML

### Prinsipp

Regel 9, 10 og 11 handlar om livssyklus- og ansvarsmetadata for modellen.
Desse høyrer i sjølve skjema-YAML — same fil som definerer modellen.

Mekanismen er `schema.annotations` med nøkkelnamn henta direkte frå
`Informasjonsmodell`-slotsa i `modelldcat-ap-no-schema.yaml`. Dette er same
mønster som det etablerte `annotations.begrepsidentifikator`, men slotnamna
er no eksplisitt forankra i ModelDCAT-AP-NO-vokabularet:

| Regel | Digdir-krav | `Informasjonsmodell`-slot | URI | `annotations`-nøkkel |
|---|---|---|---|---|
| 10 | Ansvarleg organ | `utgiver` | `dct:publisher` | `annotations.utgiver` |
| 9 | Endringsdato | `endringsdato` | `dct:modified` | `annotations.endringsdato` |
| 9 | Publiseringsdato | `utgivelsesdato` | `dct:issued` | `annotations.utgivelsesdato` |
| 11 | Livssyklusstatus | `status` | `adms:status` | `annotations.status` |

CI les annotasjonane og genererer `Informasjonsmodell`-instansen for
modellkatalogen. Skjema-YAML er sannkjelda — ingen duplikering.

---

### Eksempel i skjema-YAML

```yaml
id: https://data.norge.no/ngr/ngr-adresse
name: ngr-adresse
title: Nasjonale grunndata - Adresse
version: "1.0.0"
annotations:
  utgiver: https://data.norge.no/organizations/974760673
  endringsdato: "2026-06-10"
  utgivelsesdato: "2024-01-15"
  status: http://purl.org/adms/status/Completed
```

---

### Silver-sjekkar

```yaml
# silver.yaml — nye sjekkar

schema_has_annotation_utgiver:
  severity: warning
  description: >
    schema.annotations.utgiver bør vere til stades med URI til ansvarleg
    organisasjon. Nøkkelnamnet svarar til Informasjonsmodell.utgiver
    (dct:publisher) i ModelDCAT-AP-NO. Digdir-regel 10: Ansvar.
  check: schema_has_annotation
  annotation: utgiver
  value_pattern: "^https://data\\.norge\\.no/organizations/\\d+$"

schema_has_annotation_endringsdato:
  severity: warning
  description: >
    schema.annotations.endringsdato bør vere til stades (ISO 8601-dato).
    Svarar til Informasjonsmodell.endringsdato (dct:modified).
    Digdir-regel 9: Datering.
  check: schema_has_annotation
  annotation: endringsdato

schema_has_annotation_status:
  severity: warning
  description: >
    schema.annotations.status bør vere til stades med ein ADMS Status-URI.
    Svarar til Informasjonsmodell.status (adms:status).
    Digdir-regel 11: Modellstatus.
  check: schema_has_annotation
  annotation: status
  allowed_values:
    - http://purl.org/adms/status/UnderDevelopment
    - http://purl.org/adms/status/Completed
    - http://purl.org/adms/status/Deprecated
    - http://purl.org/adms/status/Withdrawn
```

---

### Oppdatert Digdir-regeloversikt

| # | Regel | Nivå | Felt |
|---|---|---|---|
| 1 | Forståelighet | bronze (warning) | `description`, `title` |
| 2 | Meningsfullhet | bronze (error) | `title` |
| 3 | Navnekonvensjoner | bronze (warning) | PascalCase/snake_case-sjekk |
| 4 | Identifiserbarhet | bronze (error) | `id`, `default_prefix`, `class_uri`, `slot_uri` |
| 7 | Tilgjengeliggjøring | bronze (warning) | `license` |
| 9 | Datering | **silver (warning)** | `annotations.endringsdato` / `annotations.utgivelsesdato` |
| 10 | Ansvar | **silver (warning)** | `annotations.utgiver` |
| 11 | Modellstatus | **silver (warning)** | `annotations.status` (ADMS) |
| 13 | Begreper | bronze (warning) | `annotations.begrepsidentifikator` |

---

## Oppsummering av foreslåtte endringar

```yaml
# bronze.yaml — foreslåtte endringar

required:
  schema:
    - id
    - name
    - title           # ← flytta frå recommended (Digdir-regel 1, 2)
  class: []
  slot: []

recommended:
  schema:
    - description
    - version
    # title fjerna herifrå
  class:
    - description
  slot:
    - description

checks:
  # Eksisterande
  schema_id_is_http_uri:        # uendra
  all_classes_have_class_uri:   # uendra
  all_slots_have_slot_uri:      # uendra
  all_classes_have_identifier:  # uendra
  all_classes_have_concept_ref: # uendra

  # Nye
  schema_has_default_prefix:    severity: error   (Digdir-regel 4)
  default_prefix_is_https_uri:  severity: error   (Digdir-regel 4)
  schema_has_license:           severity: warning  (Digdir-regel 7)
  class_names_pascal_case:      severity: warning  (Digdir-regel 3)
  slot_names_snake_case:        severity: warning  (Digdir-regel 3)
```

## Implementasjonsbehov i MCP-validator

Følgjande nye `check`-typar må implementerast i `src/mcp-linkml-validator/`:

| Check-nøkkel | Logikk |
|---|---|
| `schema_has_default_prefix` | `schema.default_prefix` finst og er ikkje tom |
| `default_prefix_is_https_uri` | `default_prefix` startar med `https://` og sluttar med `/` |
| `schema_has_license` | `schema.license` finst og er ikkje tom |
| `class_names_pascal_case` | alle klassenamn (unntatt tree_root) startar med stor bokstav |
| `slot_names_snake_case` | alle globale slotnamn er lowercase og inneheld berre `a-z`, `0-9`, `_` |

## Dokumentasjon av skiljet mellom modell- og datavalidering

Bronze/silver/gold validerer **skjema/modell** — ikkje instansdata. Skiljet er:

| Kva | Verktøy | Policy-type | Felt i manifest |
|---|---|---|---|
| Skjemakvalitet (modell) | `make mcp-validate` | `bronze` / `silver` / `gold` | `data_policy:` på skjema-manifest |
| Datakvalitet (instansar) | `make validate-instance` | — | — |
| Publiseringskonformitet | `make mcp-validate` | `felles-datakatalog` / `felles-begrepskatalog` | `data_policy:` på data-manifest |

Bronze/silver/gold stiller krav til at *skjemaet* er godt nok til å produsere
data av ein viss kvalitet. Dei stiller ikkje krav til kva instansdata skal innehalde.

Som del av dette tiltaket skal skiljet dokumenterast på to stader:

### Tiltak: README i `policies/`-katalogen

Opprett `src/mcp-linkml-validator/policies/README.md` med dette innhaldet:

```markdown
# Policyer for mcp-linkml-validator

## To typar validering

Policyfilene her er brukte til to ulike føremål:

**Skjemakvalitet (bronze / silver / gold)**
Sjekkar at eit LinkML-skjema (`.yaml`-fila i `src/linkml/`) held eit visst
kvalitetsnivå: metadata, namngjeving, URI-ar, begrepsreferansar osv.
Køyrast med `make mcp-validate SCHEMA=... POLICY=bronze`.

**Publiseringskonformitet (felles-datakatalog / felles-begrepskatalog)**
Sjekkar at eit skjema er i samsvar med krava til ei bestemt ekstern katalog.
Brukt for skjema der `publish_external: true` i manifest.

## Nivå for skjemakvalitet

| Nivå | Krav |
|---|---|
| `bronze` | Grunnleggande metadata og modelleringskvalitet (dette repoets baseline) |
| `silver` | AP-NO-konformitet — skjemaet implementerer norske applikasjonsprofiler korrekt |
| `gold` | Full semantisk interoperabilitet — begrepsreferansar, identifikatorar, o.l. |

Kvart nivå arvar krava frå nivåa under (`silver` arvar `bronze` osv.).
```

### Tiltak: Klargjering i `CLAUDE.md`

Legg til i `CLAUDE.md` under `## Valider arbeidet ditt`:

```markdown
## Policy-hierarki

Bronze/silver/gold validerer **skjemakvalitet** (modellens metadata og struktur),
ikkje instansdata. Instansdata vert validert med `make validate-instance`.

`felles-datakatalog` og `felles-begrepskatalog` er separate policyer for
skjema som publiserer til eksterne katalogar (`publish_external: true`).
```

---

## Dokumentasjonsstrategi

Endringane påverkar fire dokumentasjonsflater. Prinsippet er éin sannkjelde per
tema — ikkje duplisering på tvers av filer.

| Flate | Sannkjelde for | Handling |
|---|---|---|
| `policies/README.md` | Kva kvart policy-nivå sjekkar | **Ny fil** — autoritativ referanse |
| `CLAUDE.md` | Forfattarkonvensjonar (annotasjonsmønster) | Legg til silver-annotasjonar, lik `begrepsidentifikator`-seksjonen |
| `mkdocs/docs/ny-domenemodell.md` | Arbeidsflyt for nye modellar | Oppdater policy-tabellen; lenk til `policies/README.md` i staden for å duplisere sjekklista |
| `mcp-linkml-modell-utkast/README.md` | Kva verktøyet genererer | Oppdater for nye felt og silver-profil |

### `policies/README.md` — ny autoritativ referanse

Fila `src/mcp-linkml-validator/policies/README.md` vert sannkjelda for kva kvart
nivå sjekkar. `ny-domenemodell.md` og andre flater lenkar hit i staden for å
halde eigne kopiar av sjekklista.

(Innhald allereie spesifisert under *Dokumentasjon av skiljet mellom modell- og datavalidering* ovanfor.)

### `CLAUDE.md` — silver-annotasjonar

Legg til ein ny seksjon etter `### annotations.begrepsidentifikator`:

```markdown
### Silver-annotasjonar (Digdir-regel 9, 10, 11)

Skjema med `data_policy: silver` eller høgare skal ha desse annotasjonane.
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
```

### `ny-domenemodell.md` — oppdater policy-tabell og lenke

Erstattar den noverande inlinede sjekklista med ei lenke og ein oppdatert tabell som
speglar ny bronze- og silver-policy:

```markdown
| Policy | Sjekkar |
|---|---|
| `bronze` | `id`, `name`, `title` (error); `default_prefix` (https-URI, error); `description`, `version`, `license` (warning); PascalCase-klasser, snake_case-slots, `class_uri`, `slot_uri`, `begrepsidentifikator` (warning) |
| `silver` | Bronze + `annotations.utgiver`, `annotations.endringsdato`, `annotations.status` (warning) |
| `gold`   | Silver + FAIR F1-R1.3: full semantisk interoperabilitet |

Sjå [policies/README.md](../../src/mcp-linkml-validator/policies/README.md) for fullstendig sjekkliste.
```

Legg også til steg 6 i "NB! Etter generering"-seksjonen:

```markdown
6. **Fyll inn silver-annotasjonar** om skjemaet har `data_policy: silver`:
   `annotations.utgiver`, `annotations.endringsdato`, `annotations.utgivelsesdato`,
   `annotations.status` — sjå [CLAUDE.md § Silver-annotasjonar](../CLAUDE.md).
```

### `mcp-linkml-modell-utkast/README.md` — oppdater for nye felt og silver-profil

To endringar:

**1. Oppdater "Kva det genererte skjemaet inneheld"-tabellen:**

| Element | Beskriving |
|---|---|
| `title` | Frå `schemaTitle`-parameteren eller `TODO: tittel` |
| `version` | `TODO: versjonsnummer` |
| `license` | `TODO: https://creativecommons.org/licenses/by/4.0/` |

**2. Legg til `silver`-profil i profil-tabellen og "NB!"-lista:**

```markdown
### Silver-profil

Bruk `PROFILE=silver` for å generere skjema med silver-annotasjonar:

make mcp-generate SCHEMA=tmp/modell.json PROFILE=silver

Det genererte skjemaet vil innehalde `annotations.utgiver`, `annotations.endringsdato`,
`annotations.utgivelsesdato` og `annotations.status` med `TODO`-stubs klare for utfylling.
```

---

## Implementasjonsbehov i `mcp-linkml-modell-utkast`

Det genererte skjemaet frå `generate_linkml` har fleire avvik frå ny bronze-policy.
Alle avvika kan rettast i `converter.py` og `profiles/default.yaml`.

### Kritiske feil (vil feile bronze)

#### 1. `default_prefix` er prefix-alias, ikkje HTTPS-URL

`converter.py` linje 274 set `schema["default_prefix"] = prefix_name` (t.d. `ngr_adresse`).
Bronze krev absolutt HTTPS-URL med avsluttande `/`.

**Fix i `converter.py`:**
```python
# Før
schema["default_prefix"] = prefix_name
# Etter
schema["default_prefix"] = schema_uri   # t.d. "https://data.norge.no/ngr/ngr-adresse/"
```

### Manglar som gir warnings (bronze)

#### 2. `title` er valfri

`title` vert berre lagt til viss `schemaTitle`-parameteren er oppgjeven. Bronze krev `title` som error.

**Fix i `converter.py`:** Legg alltid til `title`. Om `schema_title` er tom, bruk `TODO: tittel`:
```python
schema["title"] = schema_title or "TODO: tittel"
```

#### 3. `version` manglar

Bronze anbefalar `version`. Legg til ein `TODO`-stub.

**Fix i `converter.py`:**
```python
schema["version"] = "TODO: versjonsnummer"
```

#### 4. `license` manglar

Bronze anbefalar `license`. Legg til ein `TODO`-stub.

**Fix i `converter.py`:**
```python
schema["license"] = "TODO: https://creativecommons.org/licenses/by/4.0/"
```

### Silver-annotasjonar — ny profil

Silver-annotasjonane (`annotations.utgiver`, `annotations.endringsdato`,
`annotations.utgivelsesdato`, `annotations.status`) høyrer ikkje i `default`-profilen,
men bør tilbyast via ein eigen `silver`-profil i `profiles/silver.yaml`.

**Ny fil `profiles/silver.yaml`:**
```yaml
version: 1
description: >
  Utvida profil med silver-annotasjonar for Digdir-regel 9, 10 og 11.
  Arvar alle innstillingar frå default-profilen og legg til schema-annotasjonar
  med nøkkelnamn frå Informasjonsmodell i modelldcat-ap-no.

extends: default

schema_annotations:
  utgiver: "TODO: https://data.norge.no/organizations/<orgnr>"
  endringsdato: "TODO: YYYY-MM-DD"
  utgivelsesdato: "TODO: YYYY-MM-DD"
  status: "TODO: http://purl.org/adms/status/UnderDevelopment"
```

`converter.py` les `schema_annotations` frå profilen og legg dei til under
`schema["annotations"]` saman med evt. eksisterande annotasjonar.

---

## Vurdering: `mcp-linkml-begrep-utkast`

`mcp-linkml-begrep-utkast` genererer **instansdata** (`BegrepContainer`-YAML) —
ikkje LinkML-skjema. Bronze/silver/gold-policyane gjeld skjema, ikkje instansdata.

Verktøyet treng difor **ingen endringar** som følgje av ny bronze-policy.

Instansane det genererer vert validerte mot `skos-ap-no-schema.yaml` via
`make validate-instance` — ein heilt separat valideringsveg.

---

## Prioritert tiltaksliste

| # | Tiltak | Avhengigheit | Prioritet |
|---|---|---|---|
| 1 | Flytt `title` til `required.schema` i `bronze.yaml` | — | Høg |
| 2 | Implementer `schema_has_default_prefix`-sjekk | — | Høg |
| 3 | Implementer `default_prefix_is_https_uri`-sjekk | Tiltak 2 | Høg |
| 4 | Legg til `schema_has_license`-sjekk | — | Medium |
| 5 | Implementer `class_names_pascal_case`-sjekk med unntaksliste | — | Medium |
| 6 | Implementer `slot_names_snake_case`-sjekk med unntaksliste | Tiltak 5 | Medium |
| 7 | Verifiser at alle eksisterande skjema passerer ny bronze (særleg `default_prefix`) | Tiltak 1-3 | Høg |
| 8 | Opprett `src/mcp-linkml-validator/policies/README.md` med skiljet dokumentert | — | Medium |
| 9 | Legg til policy-hierarki-seksjon i `CLAUDE.md` | — | Lav |
| 10 | Implementer `schema_has_annotation`-sjekk i MCP-validator | — | Medium |
| 11 | Legg `schema_has_annotation_utgiver`, `schema_has_annotation_endringsdato`, `schema_has_annotation_status` til `silver.yaml` | Tiltak 10 | Medium |
| 12 | Legg `annotations.utgiver`, `annotations.endringsdato`, `annotations.utgivelsesdato`, `annotations.status` til alle skjema med `data_policy: silver` eller høgare | Tiltak 10-11 | Medium |
| 13 | ~~Oppdater CI til å generere `Informasjonsmodell`-instansar i modellkatalogen frå skjema-annotasjonar~~ ✅ | Tiltak 12 | Lav |
| 14 | ~~**`mcp-linkml-modell-utkast`**: Fiks `default_prefix` til HTTPS-URL i `converter.py`~~ ✅ | — | Høg |
| 15 | ~~**`mcp-linkml-modell-utkast`**: Legg alltid til `title`, `version`, `license` med TODO-stubs~~ ✅ | Tiltak 14 | Høg |
| 16 | ~~**`mcp-linkml-modell-utkast`**: Gi `profiles/default.yaml` nytt namn til `profiles/bronze.yaml`; oppdater `server.py` og README med nytt standardprofilnamn~~ ✅ | — | Medium |
| 17 | ~~**`mcp-linkml-modell-utkast`**: Opprett `profiles/silver.yaml` med `schema_annotations`; `extends: bronze`~~ ✅ | Tiltak 16 | Medium |
| 18 | ~~**`mcp-linkml-modell-utkast`**: Les `schema_annotations` frå profil i `converter.py`~~ ✅ | Tiltak 17 | Medium |
| 19 | ~~**`mcp-linkml-modell-utkast/README.md`**: Oppdater tabell og legg til silver-profil-seksjon~~ ✅ | Tiltak 15-17 | Medium |
| 20 | ~~**`CLAUDE.md`**: Legg til silver-annotasjonar-seksjon etter `begrepsidentifikator`~~ ✅ (utført i tiltak 9) | — | Medium |
| 21 | ~~**`ny-domenemodell.md`**: Oppdater policy-tabell; lenk til `policies/README.md`; legg til steg 6~~ ✅ | Tiltak 8, 20 | Medium |
| 22 | ~~**Scaffold (`make new-model`)**: Sikre at generert skjema passerer ny bronze (har `title`, `version`, `default_prefix` som HTTPS-URL)~~ ✅ | Tiltak 1-3 | Høg |
