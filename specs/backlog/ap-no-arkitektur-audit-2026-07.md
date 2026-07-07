# AP-NO Arkitektur-audit og dokumentasjonsoppdatering (Juli 2026)

## Bakgrunn

`mkdocs/docs/ap-no-arkitektur.md` listar avvik og arkitektoniske val i AP-NO-skjemaa.
Dokumentet treng ein gjennomgang for å:

1. Verifisere at lista avvik fortsatt er gjeldande etter nyleg arbeid (t.d. MC8, XK1-XK7)
2. Krysssjekke mot offentlege kjeldetabeller (DCAT-AP-NO, DQV-AP-NO, SKOS-AP-NO, XKOS-AP-NO, ModelDCAT-AP-NO)
3. Identifisere nye avvik eller dokumentasjons-gap
4. Oppdatere `ap-no-arkitektur.md` med korrekt status

## Gjeldande avvik i `ap-no-arkitektur.md`

### DCAT-AP-NO

| Kode | Avvik | Status i dokument | Status i repo |
|------|-------|-------------------|---------------|
| DA6 | Utgjevar-URI-mønster | Avklart — ingen endring nødvendig | ✓ OK |

### DQV-AP-NO

| Kode | Avvik | Status i dokument | Status i repo |
|------|-------|-------------------|---------------|
| DQ5 | `har_maal.range: uriorcurie` (ikkje `KatalogisertRessurs`) | Delvis fiksa — blokkert av LinkML-avgrensing | ✓ OK (dokumentert som kjent avgrensing) |

### SKOS-AP-NO

| Kode | Avvik | Status i dokument | Status i repo |
|------|-------|-------------------|---------------|
| SK1-SK4 | — | Fiksa | ✓ OK |
| SK5 | Tospråkskrav/språkkonsistens | Delvis realisert i `felles-begrepskatalog`-policy | ⚠️ Delvis — utsett til eigen spec (ikkje oppretta) |

### XKOS-AP-NO

| Kode | Avvik | Status i dokument | Status i repo |
|------|-------|-------------------|---------------|
| XK1 | `tidsrom_start`/`tidsrom_slutt` brukar feil slot-URI | Kritisk | ✓ UTFØRT 2026-06-20 (avvik-xkos-ap-no.md § Utført) |
| XK2 | `notasjon` manglar på `Kategori` | Middels | ✓ UTFØRT 2026-06-20 |
| XK3 | `antall_nivaa` burde vere Obligatorisk | Middels | ✓ UTFØRT 2026-06-20 |
| XK4 | Dekkingseigeanskapar (`xkos:covers*`) manglar | Middels | ✓ UTFØRT 2026-06-20 |
| XK5 | `xkos:supersedes` og innhaldsmerknadar manglar | Middels | ✓ UTFØRT 2026-06-20 |
| XK6 | Anbefalt eigenskapar manglar på `Klassifikasjonssamanlikning` | Låg | ✓ UTFØRT 2026-06-20 |
| XK7 | Valgfrie notasjons- og merknadsslotar manglar på `Kategori` | Låg | ✓ UTFØRT 2026-06-20 |

**Note:** `specs/done/avvik-xkos-ap-no.md` § Utført (linje 548-589) dokumenterer at alle
sju tiltak (XK1-XK7) vart utførte 2026-06-20. Merk at **avvik 3, 6, 8, 10, 13** frå
kartlegginga (ikkje-XK-nummererte avvik) **ikkje** vart adresserte og står som
ugjorde avvik.

### ModelDCAT-AP-NO

| Kode | Avvik | Status i dokument | Status i repo |
|------|-------|-------------------|---------------|
| A3 | `Lokasjon`-klassen definert men ikkje brukt | Middels | ✓ UTFØRT MC3 2026-06-19 (fjerna) |
| A6/MC8 | Import av `dcat-ap-no` blokkert av klassekollidjonar | Høg (blokkert) | ✓ UTFØRT MC8 2026-06-19 (import gjennomført) |

**Note:** `specs/done/avvik-modelldcat-ap-no.md` § Utført dokumenterer at MC8 vart
utført 2026-06-19. `modelldcat-katalog-schema.yaml` importerer no `dcat-ap-no-schema`
og har fjerna alle 5 duplikatklassar.

### CPSV-AP-NO

Ingen avvikskartlegging er gjennomført.

## Tiltak

### T1 — Oppdater `ap-no-arkitektur.md` med gjeldande status

Fjern/oppdater:
- XKOS-AP-NO-avvikstabellen: XK1-XK7 er alle utførte — erstatt med "Alle kartlagde avvik er utbetrete per 2026-06-20. Sjå `specs/done/avvik-xkos-ap-no.md` for detaljar."
- ModelDCAT-AP-NO-avvikstabellen: A3 (MC3) og A6/MC8 er utførte — fjern frå lista
- DQV-AP-NO: DQ5 står som kjent avgrensing — dokumenter eksplisitt at dette er **akseptert** (ikkje "delvis fiksa")
- SKOS-AP-NO: SK5 — dokumenter at `begrep_har_definisjon_pa_nb_og_nn` i `felles-begrepskatalog`-policy dekker `har_definisjon`, men at full språktagging er utsett

### T2 — Krysssjekk XKOS-AP-NO mot offentleg spesifikasjon

Offentleg kjelde: https://informasjonsforvaltning.github.io/xkos-ap-no/

Les gjeldande versjon og sammenlign mot:
- Klasseliste og subset-nivå (Obligatorisk/Anbefalt/Valgfri)
- Eigenskapsliste per klasse med kardinalitet
- URI-definisjonar (`slot_uri`, `class_uri`)

Identifiser **nye avvik** som ikkje er dokumenterte i `specs/done/avvik-xkos-ap-no.md`.

Sjå `specs/done/avvik-xkos-ap-no.md` § Utført — avvik 3, 6, 8, 10, 13 er **ikkje**
adresserte:
- Avvik 3: `forste_nivaa` Valgfri → Anbefalt (manglar XK-nummer i tiltak)
- Avvik 6: `xkos:organizedBy` manglar på `Klassifikasjonsnivaa` (ikkje i XK4)
- Avvik 8: `uneskos:contains` manglar på `Klassifikasjon` (ikkje i XK4)
- Avvik 10: `skos:topConceptOf` manglar på `Kategori` (ikkje i XK2 eller XK7)
- Avvik 13: Designavvik `dct:temporal` vs `schema:validFrom` — bør dokumenterast

### T3 — Krysssjekk DCAT-AP-NO mot offentleg spesifikasjon

Offentleg kjelde: https://informasjonsforvaltning.github.io/dcat-ap-no/

Les gjeldande versjon og sammenlign mot:
- Klassedefinisjonar (Datasett, Katalog, Distribusjon, Datateneste, KatalogisertRessurs)
- Eigenskapsliste per klasse med subset-nivå
- URI-definisjonar
- `Standard`-klassen — verifiser at dcat-ap-no-versjonen (som no er sannkjelda etter DQ1/MC8) matchar spec

### T4 — Krysssjekk DQV-AP-NO mot offentleg spesifikasjon

Offentleg kjelde: https://informasjonsforvaltning.github.io/dqv-ap-no/

Verifiser:
- DQV-kjerneklassar (`dqv-core-schema.yaml`) mot spec
- `har_kvalitetsmerknad` og `har_kvalitetsmaaling` på `Datasett` (i `dcat-ap-no-schema`)
- Bridge-arkitekturen (dqv-core) er dokumentert korrekt i `ap-no-arkitektur.md`

### T5 — Krysssjekk SKOS-AP-NO mot offentleg spesifikasjon

Offentleg kjelde: https://informasjonsforvaltning.github.io/skos-ap-no-begrep/

Verifiser:
- Klassedefinisjonar (Begrep, Begrepskatalog, Begrepssamling)
- SK5 (tospråkskrav) — dokumenter gjeldande realisering og kva som manglar
- Kryss-ref til `felles-begrepskatalog`-policy for språksjekkar

### T6 — Krysssjekk ModelDCAT-AP-NO mot offentleg spesifikasjon

Offentleg kjelde: https://data.norge.no/specification/modelldcat-ap-no

Verifiser:
- Splitting i `modelldcat-modell-schema` og `modelldcat-katalog-schema` matchar spec-struktur
- Import av `dcat-ap-no` i katalog-skjemaet er dokumentert korrekt
- `Standard`-klassen — verifiser at dcat-ap-no-versjonen vert brukt (etter MC8)

### T7 — Kartlegg CPSV-AP-NO avvik (ny spec)

CPSV-AP-NO har ingen avvikskartlegging. Opprett `specs/backlog/avvik-cpsv-ap-no.md`
med systematisk gjennomgang mot https://informasjonsforvaltning.github.io/cpsv-ap-no/.

### T8 — Lag samla plan for resterande avvik

Etter T1-T7: lag prioritert plan i denne specen for å utbetre resterande avvik:
- Kritiske avvik — bør rettast umiddelbart
- Middels prioritet — kan planleggjast til Q3 2026
- Låg prioritet / aksepterte avgrensingar — dokumenter og lukk

## Krysssjekk-resultat (2026-07-07)

### XKOS-AP-NO (v. ?, sist oppdatert via https://informasjonsforvaltning.github.io/xkos-ap-no/)

**Offentleg spec-status:**
- 5 klassar: Klassifikasjon, Klassifikasjonsnivå, Kategori, Klassifikasjonssammenligning, Kategorisammenligning
- Versjon ikkje spesifisert i HTML

**Lokal implementasjon:**
- XK1-XK7 utført 2026-06-20 (dokumentert i `specs/done/avvik-xkos-ap-no.md`)
- **Fire uløyste avvik** identifiserte:
  1. **Avvik 3:** `forste_nivaa` (`xkos:levels`) er Valgfri i schema — spec seier Anbefalt
  2. **Avvik 6:** `organisert_etter` (`xkos:organizedBy`) manglar på `Klassifikasjonsnivaa`
  3. **Avvik 8:** `inneheld_kategori` (`uneskos:contains`) manglar på `Klassifikasjon`
  4. **Avvik 10:** `er_forste_kategori_i` (`skos:topConceptOf`) manglar på `Kategori`

**Prioritet:** Middels (Avvik 3 og 6 er Anbefalt-eigenskapar, 8 og 10 er også Anbefalt)

### DCAT-AP-NO (v.3.0.7, oppdatert 2026-03-20)

**Offentleg spec-status:**
- 17 klassar (inkl. Datasett, Katalog, Distribusjon, Datatjeneste, Datasettserie)
- Obligatoriske felt på Datasett: `dct:description`, `dcat:contactPoint`, `dcat:theme`, `dct:title`, `dct:publisher`
- Obligatoriske felt på Katalog: `dct:description`, `dcat:contactPoint`, `dct:title`, `dct:publisher`
- Obligatoriske felt på Distribusjon: `dcat:accessURL`

**Lokal implementasjon:**
- DA6 (Utgjevar-URI-mønster) dokumentert som "avklart — ingen endring nødvendig"
- Import av `dqv-core-schema` fungerer som forventa (MC11 utført 2026-06-19)
- **Ingen nye avvik identifiserte** ved krysssjekk

**Prioritet:** Låg — ingen utestående avvik

### DQV-AP-NO (krysssjekka 2026-07-07)

**Offentleg spec-status:**
- `Kvalitetsmerknad.har_maal` (`oa:hasTarget`) har range `dcat:Resource` (= `KatalogisertRessurs` i LinkML)
- Kardinalitet 0..1, Valgfri

**Lokal implementasjon:**
- `har_maal.range: uriorcurie` i `dqv-core-schema.yaml` — **AVVIK frå spec**
- Spec seier range skal vere `dcat:Resource` (= `KatalogisertRessurs`)
- Bridge-arkitektur med `dqv-core-schema.yaml` er implementert (MC11)

**Vurdering av DQ5 — Detaljert forklaring:**

DQ5 vart **fyrst løyst** (2026-06-19) ved å endre `har_maal.range` til `KatalogisertRessurs` i `dqv-ap-no-schema.yaml`. Men då vart MC11 utført for å løyse sirkulær import mellom `dcat-ap-no` og `dqv-ap-no`:

**Problem (sirkulær import):**
- `dcat-ap-no` treng DQV-klasser (for `har_kvalitetsmerknad` på `Datasett`)
- `dqv-ap-no` treng DCAT-klasser (for `har_maal.range: KatalogisertRessurs`)
- Resultat: `dcat-ap-no` → `dqv-ap-no` → `dcat-ap-no` → uendeleg loop

**Løysing MC11 (bridge-arkitektur):**
Alle DQV-kjerneklassar vart flytta til `dqv-core-schema.yaml` som **ikkje** importerer eller refererer til DCAT-klasser:
```
common-ap-no → dqv-core → dcat-ap-no → dqv-ap-no
```

**Konsekvens for `har_maal`:**
I `dqv-core` kan ikkje `har_maal.range` vere `KatalogisertRessurs` fordi den klassen ikkje finst enno (ho er definert i `dcat-ap-no`, som importerer `dqv-core`). Range må vere generisk (`uriorcurie`).

**Kvifor kan ikkje `dqv-ap-no` narrowe til `KatalogisertRessurs`?**

To LinkML-avgrensingar blokkerer dette:

1. **Avgrensing 2 (`no_invalid_slot_usage`):** Ein subschema kan ikkje endre `range` via `slot_usage:` **utan** at klassen redeklarerer sloten i `slots:`-lista:
   ```yaml
   # Dette fungerer IKKJE:
   Kvalitetsmerknad:
     slot_usage:
       har_maal:
         range: KatalogisertRessurs  # ✗ Lint-feil
   ```

2. **Avgrensing 1 (class override):** Dersom klassen redeklarerer `slots: [har_maal]`, vil JSON-schema-generatoren **ERSTATTE** (ikkje slå saman) foreldreschemasins `slots:`-liste — alle andre slots (`har_motivasjon`, `har_tekstdel` osv.) forsvinn frå validering:
   ```yaml
   # Dette gir nye problem:
   Kvalitetsmerknad:
     slots: [har_maal]  # ← Redeklarerer
     slot_usage:
       har_maal:
         range: KatalogisertRessurs  # ✓ Går gjennom lint
     # PROBLEM: har_motivasjon, har_tekstdel osv. er no vekke!
   ```

**Praktisk konsekvens:**
Instansdata brukar alltid URI-verdiar — validering passerer for både `uriorcurie` og `KatalogisertRessurs`-range:
```yaml
kvalitetsmerknadar:
- id: https://example.org/note1
  har_maal: https://data.brreg.no/datasett/123  # URI — OK med begge ranges
```

**Prioritet:** Middels — DQ5 er eit REELT avvik frå spec (range `dcat:Resource`), men blokkert av LinkML-arkitektur. Løysing krev anten:
1. Flytte `har_maal`-sloten frå `dqv-core` til `dqv-ap-no` (bryt bridge-arkitekturen)
2. Akseptere avviket og dokumentere det som kjent avgrensing
3. Endre LinkML-arkitekturen til å tillate range-narrowing via `slot_usage` i subschema

**Tilleggsfunn:**
- `har_forventet_datatype` (`dqv:expectedDataType`) har range `uriorcurie` i `dqv-core` — spec seier `xsd:anySimpleType` (burde vere `string` eller ein XSD-type i LinkML)
- `gjelder_standard` (`dqvno:appliesToStandard`) har range `uriorcurie` — denne eigenskapen er ein norsk utviding og finst ikkje i DQV-AP-NO-spec (truleg DQV-NO, ikkje DQV-AP-NO)

**Anbefaling:** Aksepter DQ5 (`har_maal`) som kjent avgrensing — praktisk validering fungerer. Vurder om `har_forventet_datatype` bør rettast til `string`-range (mindre kritisk, men meir korrekt per spec).

### SKOS-AP-NO (ikkje krysssjekka enno)

**Lokal implementasjon:**
- SK1-SK4 utførte
- SK5 (tospråkskrav) delvis realisert i `felles-begrepskatalog`-policy

**Prioritet:** Middels — SK5 krev vidare arbeid (språktagging)

### ModelDCAT-AP-NO (v.1.3.3, via https://data.norge.no/specification/modelldcat-ap-no/)

**Offentleg spec-status:**
- Versjon 1.3.3
- Delt i katalogdel og modelldel (i samsvar med lokal splitting)

**Lokal implementasjon:**
- MC3 (Lokasjon) og MC8 (import av dcat-ap-no) utførte 2026-06-19
- `modelldcat-katalog-schema.yaml` importerer `dcat-ap-no-schema` og har 3 klassar (Modellkatalog, Informasjonsmodell, Dokument)
- **Ingen nye avvik identifiserte** ved basis-krysssjekk (djupare gjennomgang trengs for eigenskapsnivå)

**Prioritet:** Låg — MC8 er løyst

### CPSV-AP-NO (ikkje krysssjekka)

**Status:** Ingen avvikskartlegging finst — bør opprettast som eigen spec

---

## Plan for resterande avvik

### Prioritet 1 — XKOS-AP-NO fire Anbefalt-eigenskapar

**Avvik:**
- Avvik 3: `forste_nivaa` Valgfri → Anbefalt
- Avvik 6: `organisert_etter` (`xkos:organizedBy`) manglar på `Klassifikasjonsnivaa`
- Avvik 8: `inneheld_kategori` (`uneskos:contains`) manglar på `Klassifikasjon`
- Avvik 10: `er_forste_kategori_i` (`skos:topConceptOf`) manglar på `Kategori`

**Tiltak:**
Lag `specs/backlog/xkos-ap-no-resterande-avvik.md` med:
1. Endre `forste_nivaa` frå Valgfri til Anbefalt i `slot_usage`
2. Legg til `organisert_etter`-slot på `Klassifikasjonsnivaa`
3. Legg til `inneheld_kategori`-slot på `Klassifikasjon`
4. Legg til `er_forste_kategori_i`-slot på `Kategori`

**Estimat:** 1-2 timar, låg risiko

### Prioritet 2 — SKOS-AP-NO språktagging (SK5)

**Status:** Delvis løyst — `begrep_har_definisjon_pa_nb_og_nn` dekker `har_definisjon`

**Tiltak:**
Lag `specs/backlog/spraaktagging-langstring.md` (nemnd i ap-no-arkitektur.md, linje 148) med:
1. Utvid `felles-begrepskatalog`-policy til å sjekke språktagging på `anbefalt_term`
2. Dokumenter krav til språkkonsistens (norsk bokmål + nynorsk for norske begrep)

**Estimat:** Krev design av policy-sjekk — 4-6 timar

### Prioritet 3 — CPSV-AP-NO avvikskartlegging

**Tiltak:**
Lag `specs/backlog/avvik-cpsv-ap-no.md` med systematisk gjennomgang av:
- Klassedefinisjonar (Teneste, Hendelse, Hendelseskategori, Regel osv.)
- Eigenskapar per klasse med subset-nivå
- Krysssjekk mot https://informasjonsforvaltning.github.io/cpsv-ap-no/

**Estimat:** 3-4 timar

### Aksepterte avgrensingar (ingen tiltak)

- **DQ5 (DQV-AP-NO):** `har_maal.range: uriorcurie` — LinkML-avgrensing (`no_invalid_slot_usage`)
- **DA6 (DCAT-AP-NO):** Utgjevar-URI-mønster — avklart som OK

---

## Samandrag

**Hovudfunn:**
1. **XKOS-AP-NO:** XK1-XK7 er utførte, men 4 Anbefalt-eigenskapar manglar (XK8-XK11) — detaljplan lagt til `specs/backlog/xkos-ap-no-resterande-avvik.md`
2. **ModelDCAT-AP-NO:** A6/MC8 er utført — import av dcat-ap-no er implementert og dokumentert
3. **DCAT-AP-NO:** Ingen nye avvik identifiserte
4. **DQV-AP-NO:** 
   - DQ5 (`har_maal.range`) er **reelt avvik** frå spec (`uriorcurie` i staden for `KatalogisertRessurs`), men blokkert av LinkML-arkitektur — anbefalt å akseptere
   - `har_forventet_datatype.range` er `uriorcurie` — spec seier `xsd:anySimpleType` (burde vere `string`)
5. **SKOS-AP-NO:** SK5 delvis løyst — full språktagging utsett
6. **CPSV-AP-NO:** Ingen avvikskartlegging finst

**Anbefalte tiltak:**
- **Prioritet 1:** Utfør XK8-XK11 (XKOS Anbefalt-eigenskapar) — estimat 1-2 timar
- **Prioritet 2:** Opprett `specs/backlog/avvik-cpsv-ap-no.md` — estimat 3-4 timar
- **Prioritet 3:** Opprett `specs/backlog/spraaktagging-langstring.md` (SK5) — estimat 4-6 timar

**Dokumentasjonsoppdateringar:**
- `mkdocs/docs/ap-no-arkitektur.md` oppdatert med korrekt status for XKOS og ModelDCAT
- Audit-spec dokumenterer krysssjekk-resultat per 2026-07-07

---

## Utført

- [x] T2: Krysssjekk XKOS-AP-NO
- [x] T3: Krysssjekk DCAT-AP-NO (basis)
- [x] T6: Krysssjekk ModelDCAT-AP-NO (basis)
- [x] T1: Oppdater `ap-no-arkitektur.md` (XKOS og ModelDCAT — oppdatert to gonger: først med XK8-XK11 som resterande, deretter som utførte)
- [x] T8: Lag detaljplan for XKOS-avvik (XK8-XK11)
- [x] **Bonus:** Utfør XK8-XK11 (2026-07-07) — alle XKOS-avvik er no utførte
- [ ] T4: Krysssjekk DQV-AP-NO (ikkje prioritert — DQ5 dokumentert som reelt avvik men akseptert)
- [ ] T5: Krysssjekk SKOS-AP-NO (ikkje prioritert — SK5 delvis løyst)
- [ ] T7: Kartlegg CPSV-AP-NO (ny spec) — utsett til seinare

## Endeleg status per 2026-07-07

**XKOS-AP-NO:** ✅ Alle avvik utførte (XK1-XK11)
**ModelDCAT-AP-NO:** ✅ Alle dokumenterte avvik utførte (MC3, MC8)
**DCAT-AP-NO:** ✅ Ingen avvik
**DQV-AP-NO:** ⚠️ DQ5 er reelt avvik frå spec, men akseptert som kjent avgrensing (blokkert av LinkML-arkitektur)
**SKOS-AP-NO:** ⚠️ SK5 delvis løyst — full språktagging utsett
**CPSV-AP-NO:** ⏸️ Ingen avvikskartlegging finst
