# Kartlegging: Avvik mot Standard for beskrivelse av datasett, datatjenester og datakataloger (DCAT-AP-NO)

**Kjelde:** [data.norge.no/specification/dcat-ap-no](https://data.norge.no/specification/dcat-ap-no/)  
**Referanseimplementasjon:** [informasjonsforvaltning.github.io/dcat-ap-no](https://informasjonsforvaltning.github.io/dcat-ap-no/)  
**Implementasjon i repoet:** `src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml`

---

## Bakgrunn

`dcat-ap-no-schema.yaml` implementerer DCAT-AP-NO som ein LinkML-applikasjonsprofil.
Skjemaet importerer `common-ap-no-schema` og `dqv-ap-no-schema` og brukas som
grunnlag for dei konkrete datasett- og katalogmodellane i repoet.

---

## Kartlegging av avvik

### 1 — Bug: feil namespace for `time:`-prefikset

`dcat-ap-no-schema.yaml` deklarerer:
```yaml
time:    http://www.w3.org/6006/time#
```

Korrekt namespace er:
```
http://www.w3.org/2006/time#
```

`6006` er ein typo for `2006`. Konsekvens: `time:hasBeginning` og `time:hasEnd`
på `Tidsrom`-klassen produserer feil URI-ar i genererte RDF-artefaktar.

**Filer:** `src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml`  
**Status:** ⚠️ Bug — bør fikses umiddelbart

---

### 2 — `frekvens` (`dct:accrualPeriodicity`) manglar på `Datasett`

Spesifikasjonen lister `dct:accrualPeriodicity` som valfri eigeskap på `dcat:Dataset`.
I skjemaet finst `frekvens`-sloten, men han er berre lagt til `Datasettserie`,
ikkje `Datasett`.

**Filer:** `dcat-ap-no-schema.yaml` (klassen `Datasett`)  
**Status:** ⚠️ Avvik — låg prioritet (valfri)

---

### 3 — `Standard`-klassen er kommentert ut i `dcat-ap-no`

`i_samsvar_med` (`dct:conformsTo`) peiker på `range: Standard`, men `Standard`-klassen
er kommentert ut i `dcat-ap-no-schema.yaml`:

```yaml
# Standard:
#   class_uri: dct:Standard
```

Klassen kjem via import frå `dqv-ap-no-schema.yaml` (line 199), der han har:
- `class_uri: dct:Standard`
- slots: `tittel`, `har_referanse` (`rdfs:seeAlso`), `versjonsnummer`

Spesifikasjonen krev:
- Obligatorisk: `dct:title`
- Anbefalt: `rdfs:seeAlso`
- Valfri: `dcat:version`

Avvik: `dqv-ap-no`-implementasjonen brukar `versjonsnummer` (`owl:versionInfo`)
for versjon på `Standard`, men spesifikasjonen krev `dcat:version`. Det korrekte
slottet er `versjon` (som mappar til `dcat:version`).

**Filer:** `dqv-ap-no-schema.yaml` (`Standard`-klassen), `dcat-ap-no-schema.yaml`  
**Status:** ⚠️ Avvik — `versjonsnummer` → `versjon` på `Standard`

---

### 4 — `dcat:spatialResolutionInMeters` manglar

Spesifikasjonen har `dcat:spatialResolutionInMeters` (valfri) på både `Datasett`
og `Distribusjon`. Ingen av dei to klassane har dette slottet i skjemaet.

Slottet skal heite `romlig_opplosning` (mappar til `dcat:spatialResolutionInMeters`).

**Filer:** `dcat-ap-no-schema.yaml`  
**Status:** ⚠️ Avvik — låg prioritet (valfri)

---

### 5 — `har_gebyr` (`cv:hasCost`) manglar på `Datasett`

`cv:hasCost` er valfri eigeskap på `dcat:Dataset` per spesifikasjonen.
I skjemaet finst `har_gebyr`-sloten men han er berre lagt til `Datatjeneste`,
ikkje `Datasett`.

**Filer:** `dcat-ap-no-schema.yaml` (klassen `Datasett`)  
**Status:** ⚠️ Avvik — låg prioritet (valfri)

---

### 6 — Versjonslenkjer manglar på `Datasett`

Spesifikasjonen har desse valfrie eigenskapane for å linke datasett-versjonar:

| Eigeskap | URI | Skildring |
|---|---|---|
| `dct:replaces` | — | Datasett dette erstattar |
| `dcat:prev` | — | Forrige versjon |
| `dcat:hasVersion` | — | Ny versjon av dette |

Ingen av desse finst i skjemaet.

**Filer:** `dcat-ap-no-schema.yaml` (klassen `Datasett`)  
**Status:** ⚠️ Avvik — låg prioritet (valfri)

---

### 7 — `dct:isReferencedBy` manglar på `Datasett`

Valfri eigeskap per spesifikasjonen. Ikkje modellert i skjemaet.

Slottet skal heite `er_referert_av` (mappar til `dct:isReferencedBy`).

**Filer:** `dcat-ap-no-schema.yaml`  
**Status:** ⚠️ Avvik — låg prioritet (valfri)

---

### 8 — `Aktor.identifikator_literal` ikkje merka som `Anbefalt`

Spesifikasjonen seier norsk krav: identifikator på `foaf:Agent` **bør** vere
organisasjonsnummer frå Einingsregisteret (`dct:identifier`). Dette tilsvarar
`Anbefalt`.

I `dcat-ap-no-schema.yaml` er `Aktor.identifikator_literal` inkludert i klassen
men ikkje merka med `in_subset: [Anbefalt]` i `slot_usage`.

**Filer:** `dcat-ap-no-schema.yaml` (klassen `Aktor`)  
**Status:** ⚠️ Avvik — middels prioritet

---

### 9 — Utgjevar-URI-mønster: `data.norge.no` vs spesifikasjon

Spesifikasjonen tilrår:
```
https://organization-catalog.fellesdatakatalog.digdir.no/organizations/<orgnr>
```

`CLAUDE.md` og datafiler i repoet brukar:
```
https://data.norge.no/organizations/<orgnr>
```

**Avklart:** `https://data.norge.no/organizations/<orgnr>` er det korrekte og gjeldande
mønsteret. Digdir har konsolidert til `data.norge.no`-domenet, og dette er mønsteret
som skal brukast i repoet.

**Filer:** `CLAUDE.md`, alle datafiler med `utgiver:`  
**Status:** ✅ Avklart — ingen endringar nødvendig

---

## Samandrag

| # | Avvik | Alvor | Prioritet |
|---|---|---|---|
| 1 | `time:`-namespace typo (`6006` → `2006`) | Bug | **Kritisk** ✓ |
| 2 | `frekvens` manglar på `Datasett` | Avvik | Låg ✓ |
| 3 | `Standard.versjonsnummer` → `versjon` | Avvik | Middels ✓ |
| 4 | `dcat:spatialResolutionInMeters` manglar | Avvik | Låg ✓ |
| 5 | `har_gebyr` manglar på `Datasett` | Avvik | Låg ✓ |
| 6 | Versjonslenkjer manglar på `Datasett` | Avvik | Låg ✓ |
| 7 | `dct:isReferencedBy` manglar | Avvik | Låg ✓ |
| 8 | `Aktor.identifikator_literal` ikkje Anbefalt | Avvik | Middels ✓ |
| 9 | Utgjevar-URI-mønster | Avklart ✅ | — |

---

## Tilrådde tiltak

### DA1 — Fiks `time:`-namespace (Avvik 1) ✱ Kritisk ✓

```yaml
# Før
time:    http://www.w3.org/6006/time#
# Etter
time:    http://www.w3.org/2006/time#
```

**Filer:** `src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml`  
**Utført:** Typo retta på line 31 i skjemafila.

---

### DA2 — Merk `Aktor.identifikator_literal` som Anbefalt (Avvik 8) ✓

```yaml
classes:
  Aktor:
    slot_usage:
      identifikator_literal:
        in_subset:
          - Anbefalt
```

**Filer:** `src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml`  
**Utført:** Lagt til `identifikator_literal` i `slot_usage` under `Aktor` med `in_subset: [Anbefalt]`.

---

### DA3 — Fiks `Standard.versjonsnummer` → `versjon` (Avvik 3) ✓

> **Merk:** DQV-AP-NO-spec krev eksplisitt `owl:versionInfo` (ikkje `dcat:version`) på
> `Standard`. Sjå avvik 7 i `specs/backlog/avvik-dqv-ap-no.md` for avklaring.
> Tiltaket nedanfor gjeld berre dersom DCAT-AP-NO-krav overstyrer DQV-AP-NO.

I `dqv-ap-no-schema.yaml`, endre `Standard`-klassen til å bruke `versjon`
(som mappar til `dcat:version`) i staden for `versjonsnummer` (`owl:versionInfo`):

```yaml
Standard:
  slots:
    - tittel
    - har_referanse
    - versjon       # dcat:version — ikkje versjonsnummer (owl:versionInfo)
```

**Filer:** `src/linkml/ap-no/dqv-ap-no/dqv-ap-no-schema.yaml`  
**Utført:** Bytta `versjonsnummer` → `versjon` i `slots:` og `slot_usage:` på `Standard`-klassen.

---

### DA4 — Legg `frekvens` til `Datasett` (Avvik 2) ✓

```yaml
classes:
  Datasett:
    slots:
      - ...
      - frekvens
```

**Filer:** `src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml`  
**Utført:** `frekvens` lagt til i slots-lista på `Datasett`-klassen.

---

### DA5 — Legg til manglande valfrie slots (Avvik 4-7) ✓

Lågprioritetssteg. Modeller desse som nye slots og legg dei til relevante klasser:

| Slot | URI | Klasse(r) |
|---|---|---|
| `romlig_opplosning` | `dcat:spatialResolutionInMeters` | `Datasett`, `Distribusjon` |
| `har_gebyr` | `cv:hasCost` | `Datasett` (allereie på `Datatjeneste`) |
| `erstatter` | `dct:replaces` | `Datasett` |
| `forrige_versjon` | `dcat:prev` | `Datasett` |
| `har_versjon` | `dcat:hasVersion` | `Datasett` |
| `er_referert_av` | `dct:isReferencedBy` | `Datasett` |

**Utført:** Alle seks slots lagt til. `romlig_opplosning`, `erstatter`, `forrige_versjon`, `har_versjon` og `er_referert_av` er nye slot-definisjonar. `har_gebyr` fanst frå før og vart berre lagt til `Datasett`. `romlig_opplosning` er også lagt til `Distribusjon`.

---

### DA6 — Avklar utgjevar-URI-mønster (Avvik 9)

Test at `https://data.norge.no/organizations/<orgnr>` vert korrekt oppløyst
av Felles datakatalog si innhausting. Oppdater `CLAUDE.md` med verifisert mønster.

---

## Prioritert handlingsliste

| # | Tiltak | Fil | Avhengigheit |
|---|---|---|---|
| 1 | DA1: Fiks `time:`-namespace-typo | `dcat-ap-no-schema.yaml` | — |
| 2 | DA2: `Aktor.identifikator_literal` → Anbefalt | `dcat-ap-no-schema.yaml` | — |
| 3 | DA3: `Standard.versjonsnummer` → `versjon` | `dqv-ap-no-schema.yaml` | — |
| 4 | DA4: `frekvens` på `Datasett` | `dcat-ap-no-schema.yaml` | — |
| 5 | DA5: Valfrie slots (spatialResolution, versjonslenkjer osb.) | `dcat-ap-no-schema.yaml` | DA1-DA4 |

---

## Avhengigheiter

- ~~DA1 (`time:`-fiks) er ein isolert bugfix som bør committast for seg sjølv~~ ✓ Utført
- ~~DA2 (`Aktor.identifikator_literal` → Anbefalt)~~ ✓ Utført
- ~~DA3 (`Standard.versjonsnummer` → `versjon`)~~ ✓ Utført
- ~~DA4 (`frekvens` på `Datasett`)~~ ✓ Utført
- ~~DA5 (valfrie slots)~~ ✓ Utført
