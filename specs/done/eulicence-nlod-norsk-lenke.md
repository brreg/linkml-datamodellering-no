# EULicence sin NLOD_2_0-oppføring: lenke til norsk skildring, ikkje ny enum-verdi

## Bakgrunn

Etter at `schema.license`-standarden i `new-modell.sh`/`converter.py` vart
endra til `https://data.norge.no/nlod/no/2.0` (sjå
`specs/done/new-modell-genererer-gyldig-eksempel.md`), oppstod spørsmålet om
same URI burde reflekterast i `EULicence`-enumerasjonen i
`common-ap-no-schema.yaml` — anten som ein **ny, separat enum-verdi**, eller
ved å **utvide skildringa** til den eksisterande `NLOD_2_0`-verdien med ei
lenke til den norske sida.

Desse to feltas høyrer til **ulike slots med ulikt formål**, og har ikkje
noko krav om å bruke same URI-konvensjon:

| Felt | Kva det skildrar | Verdiformat |
|---|---|---|
| `schema.license` (LinkML-metadata, toppnivå) | Kva lisens **skjemaet/modell-definisjonen** er utgitt under | Fritekst-URI, ingen enum-avgrensing |
| `Distribusjon.lisens` → `Lisensdokument.id` (via `EULicence`-annotasjon) | Kva lisens **eit datadistribusjon/datasett** er utgitt under (DCAT-AP-NO) | **Skal** hentast frå EUs kontrollerte vokabular, sjå under |

### Noverande definisjon (`common-ap-no-schema.yaml`)

```yaml
# Linje 67-80
EULicence:
  description: >-
    EU Licence-vokabularet frå Publications Office.
    Kjelde: http://publications.europa.eu/resource/authority/licence/
  permissible_values:
    CC0:
      description: Creative Commons Zero 1.0 Universal
      meaning: http://publications.europa.eu/resource/authority/licence/CC0
    CC_BY_4_0:
      description: Creative Commons Attribution 4.0 International
      meaning: http://publications.europa.eu/resource/authority/licence/CC_BY_4_0
    NLOD_2_0:
      description: Norwegian Licence for Open Government Data 2.0
      meaning: http://publications.europa.eu/resource/authority/licence/NLOD_2_0
    ...

# Linje 513-524 (lisens-sloten som brukar enumen)
lisens:
  slot_uri: dct:license
  range: Lisensdokument
  description: >-
    Lisens for bruk av ressursen. Verdien SKAL veljast frå EUs kontrollerte vokabular Licence
    (http://publications.europa.eu/resource/authority/licence/).
    For norske offentlege data er CC BY 4.0 eller NLOD 2.0 anbefalt per retningslinjene.
    Enumerasjonen EULicence i common-ap-no dekkjer dei mest brukte open source/open data-lisensane.
  annotations:
    gyldige_verdier: http://publications.europa.eu/resource/authority/licence/
    vokabular_krav: skal
    enum_referanse: EULicence
```

**Kritisk detalj:** `lisens`-sloten sin dokumentasjon seier eksplisitt at
verdien **SKAL** («vokabular_krav: skal») hentast frå EU-Publications-Office-
namespacet (`http://publications.europa.eu/resource/authority/licence/`).
`EULicence` sjølv er dokumentert som *«EU Licence-vokabularet frå
Publications Office»* — altså ei speiling av éin spesifikk ekstern
autoritetstabell, ikkje eit ope, lokalt utvida vokabular.

### Verifisering mot EU sitt Publications Office (WebFetch)

Henta `http://publications.europa.eu/resource/authority/licence/NLOD_2_0`
direkte. Oppføringa deklarerer sjølv:

- **`skos:exactMatch`:** `https://data.norge.no/nlod/en/2.0/` (engelsk versjon)
- **`foaf:homepage`:** same URL
- Referanse til `europeandataportal.eu` sitt lisensoppslag

Altså: EU-autoritetstabellen **anerkjenner sjølv** `data.norge.no` som den
offisielle heimesida/eksakte samsvaret for NLOD 2.0 — men peikar til den
**engelske** stien (`/nlod/en/2.0/`), ikkje den **norske** stien
(`/nlod/no/2.0`) som er brukt som `schema.license`-standard i denne
spec-familien. Norsk og engelsk versjon er truleg parallelle
språkvariantar av same lisens hos Digdir, men det er verdt å notere
presist kva sti EU-kjelda faktisk siterer, dersom skildringa skal vere
etterprøvbar.

## Vurdering av dei to alternativa

### Alternativ A — legg til `https://data.norge.no/nlod/no/2.0` som ny/alternativ enum-verdi eller `meaning:`

**Mot:**
- Bryt `EULicence` sin eigen dokumenterte avgrensing («EU Licence-vokabularet
  **frå Publications Office**») — vokabularet skal spegle éi ekstern
  autoritetskjelde, ikkje blandast med ein alternativ Norsk URI-form for same
  konsept.
- `lisens`-sloten sin dokumenterte «SKAL»-regel krev verdiar frå EU-
  Publications-Office-namespacet spesifikt. Ein data.norge.no-basert
  enum-verdi ville vere lett å velje ved eit uhell for `Distribusjon.lisens`,
  og ville då bryte denne regelen sjølv om lisensen semantisk er den same
  (jf. `exactMatch` over — «same lisens» er ikkje det same som «godkjend
  verdi i dette spesifikke feltet»).
- Duplikat-risiko: to enum-verdiar for konseptuelt same lisens gjer det
  vanskelegare å vite kva verdi som er «rett» å bruke i praksis, og bryt
  DRY-tankegangen i eit kontrollert vokabular (éi kjelde til sanning per
  konsept).

**For:**
- Kunne gjere det enklare å slå opp NLOD 2.0 med ein norsk-orientert
  identifikator direkte i enumen.

### Alternativ B — utvid skildringa til eksisterande `NLOD_2_0`-verdi med lenke (anbefalt)

```yaml
NLOD_2_0:
  description: >-
    Norwegian Licence for Open Government Data 2.0.
    Norsk skildring: https://data.norge.no/nlod/no/2.0
  meaning: http://publications.europa.eu/resource/authority/licence/NLOD_2_0
```

**For:**
- Rører **ikkje** `meaning:` — verdien som faktisk vert brukt i RDF-
  serialisering (`Lisensdokument.id`) er uendra, framleis EU-Publications-
  Office-forma, i tråd med «SKAL»-kravet.
- Held vokabularet reint — éi kjelde (`meaning:`), éi supplerande
  menneskeleslig lenke (`description`).
- Gir norske skjemautviklarar ei rask lenke til norsk skildring utan å
  introdusere tvitydigheit i sjølve verdien.
- Same mønster som andre `description:`-felt i skjemaet alt brukar
  (forklarande fritekst + kjeldereferanse, jf. `EULicence` sitt eige
  `description`-felt: «Kjelde: http://publications.europa.eu/...»).

**Mot:**
- Ingen reell ulempe identifisert — `description:` er reint dokumentativt
  og påverkar ikkje validering, RDF-serialisering eller `meaning:`-oppslag.

## Anbefalt løysing

**Alternativ B** — utvid `description:` på `NLOD_2_0`-verdien i `EULicence`
med ei lenke til `https://data.norge.no/nlod/no/2.0`. Ikkje legg til nokon
ny enum-verdi, og ikkje endre `meaning:`.

## Steg

1. **Oppdater `NLOD_2_0` sin `description`** i
   `src/linkml/ap-no/common-ap-no/common-ap-no-schema.yaml` (rundt linje
   78-80) til å inkludere lenka til den norske sida, t.d.:
   ```yaml
   NLOD_2_0:
     description: >-
       Norwegian Licence for Open Government Data 2.0.
       Norsk skildring: https://data.norge.no/nlod/no/2.0
     meaning: http://publications.europa.eu/resource/authority/licence/NLOD_2_0
   ```

2. **Valider skjemaet** — `make lint SCHEMA=src/linkml/ap-no/common-ap-no/common-ap-no-schema.yaml`
   og `make mcp-linkml-valider-modell SCHEMA=src/linkml/ap-no/common-ap-no/common-ap-no-schema.yaml`
   for å stadfeste at endringa ikkje introduserer nye feil/åtvaringar
   (rein `description:`-endring på ein `permissible_value` skal ikkje
   påverke validering, men verifiser likevel).

3. **Sjekk nedstraums genererte artefakt** — køyr
   `make gen-docs SCHEMA=src/linkml/ap-no/common-ap-no/common-ap-no-schema.yaml`
   (eller tilsvarande) og stadfest at den nye lenka dukkar opp korrekt i
   den genererte `EULicence`-dokumentasjonssida
   (`https://brreg.github.io/linkml-datamodellering-no/ap-no/common-ap-no/klasser/eulicence/`
   — same side som vart brukt som referanse i `new-modell.sh` sin
   lisens-kommentar, sjå `specs/done/new-modell-genererer-gyldig-eksempel.md`).

4. **Vurder versjonsbump** — sjekk om denne endringa krev ein
   patch/minor-versjonsauke av `common-ap-no` per
   `specs/done/conventional-commits-modellversjonering.md` sine reglar
   (rein dokumentasjonsendring i eit `description:`-felt — avklar med
   brukar om dette tel som ei reell skjemaendring som treng ny versjon,
   eller om det er trivielt nok til å utelatast frå versjonering).

## Handlingsliste

- [x] 1: Oppdater `NLOD_2_0` sin `description` i `common-ap-no-schema.yaml` med lenke til norsk skildring
- [x] 2: `make lint` + `make mcp-linkml-valider-modell` for `common-ap-no-schema.yaml`
- [x] 3: Verifiser generert dokumentasjonsside for `EULicence`
- [x] 4: Avklar versjoneringsbehov med brukar
- [x] 5: Flytt spec til `specs/done/` med `## Utført`-seksjon

## Utført

**1: `description`-endring.** Oppdatert `NLOD_2_0` sin `description` i
`src/linkml/ap-no/common-ap-no/common-ap-no-schema.yaml` (linje 78-81) til
ein fleirlinje-blokk (`>-`) som legg til «Norsk skildring:
https://data.norge.no/nlod/no/2.0» etter den engelske teksten. `meaning:`
(EU-Publications-Office-URI-en) er uendra.

**2: Validering.** `make lint` gir dei same fire pre-eksisterande
`canonical_prefixes`-åtvaringane som før endringa (urelatert, gjeld
`adms`/`cv`/`dct`-prefiks). `make mcp-linkml-valider-modell` gir
`"valid": true, "errorCount": 0`, med fem pre-eksisterande åtvaringar
(`all_slots_have_slot_uri` for `id`, `all_classes_have_concept_ref` for
`Lisensdokument`/`Mediatype`/`Konsept`/`Begrepssamling`) — ingen av desse
kan ha samanheng med ei rein `description:`-tekstendring på ein
enum-verdi, og talet er identisk med før endringa.

**3: Generert dokumentasjon.** `make gen-docs SCHEMA=src/linkml/ap-no/common-ap-no/common-ap-no-schema.yaml`
verifiserer at `generated/ap-no/common-ap-no/docs/EULicence.md` viser den
nye skildringa korrekt i tabellrada for `NLOD_2_0`, med `meaning:`
uendra. `generated/` er byggoutput (`.gitignore`-a) og krev ingen
opprydding.

**4: Versjonering.** `specs/done/conventional-commits-modellversjonering.md`
linje 33 seier eksplisitt: `docs`-type → **ingen** versjonsbump for
endringar i `description`-felt. Sidan denne endringa er nøyaktig det,
skal `common-ap-no` sin `version:` **ikkje** bumpast. Commit-meldinga skal
bruke `docs`-typen.

**5: Flytting.** Denne fila vert flytta til `specs/done/` som siste steg.
