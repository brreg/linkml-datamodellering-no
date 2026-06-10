# Kartlegging: Avvik mot Veileder for beskrivelse av kvalitet på datasett – kvantifiserbar kvalitet

**Kjelde:** [data.norge.no/guide/veileder-kvantifiserbar-kvalitet](https://data.norge.no/guide/veileder-kvantifiserbar-kvalitet)  
**Utgitt av:** Digitaliseringsdirektoratet (Digdir), oppdatert 2024-12-04  
**Samanheng:** DQV-AP-NO (Norsk applikasjonsprofil av DQV) og DCAT-AP-NO

---

## Bakgrunn og avgrensing

Rettleiaren forklarer korleis kvantifiserbar datakvalitet beskrives med
`dqv:hasQualityMeasurement` på `dcat:Dataset`-instansar, knytt til fire
predefinerte kvalitetsdimensjonar:

| Dimensjon | Deldimensjonar | Typiske målat |
|---|---|---|
| **Fullstendighet** | underdekning, overdekning, imputering | manglande/overflødige einingar, imputerte verdiar |
| **Aktualitet** | tidsdifferanse | samla tidsdifferanse (ISO duration) |
| **Konsistens** | konsistens innad i datasett | andel einingar med inkonsistente eigenskapar |
| **Nøyaktighet** | identifikatorriktighet, klassifikasjonsriktighet | andel feil-identifiserte/feilklassifiserte einingar |

Rettleiaren er primært meint for **instansdata** — datasett med rader og
eigenskapar (t.d. eit register over bygningar). Vurderinga nedanfor skil
difor mellom to typar output frå dette repoet:

| Type output | Relevant? | Grunngjeving |
|---|---|---|
| **Informasjonsmodellar** (LinkML-skjema) | Avgrensa | Kvalitetsdimensjonane er definerte for rader/einingar, ikkje for strukturskjema. Skjemakvalitet dekkast av bronze/silver/gold-policyen. |
| **Begrepskatalog-data** (`brreg-begrepskatalog`, m.fl.) | Ja | Faktiske SKOS-instansar publisert til Felles Begrepskatalog — fullstendighet og aktualitet er relevante. |
| **Modellkatalog-data** (`brreg-modellkatalog`, m.fl.) | Ja | DCAT-instansar publisert til Felles Datakatalog — aktualitet og fullstendighet er relevante. |

---

## Kartlegging av avvik

### 1 — `dqv:hasQualityMeasurement` manglar i alle publiserte datasett

Verken begrepskatalog- eller modellkatalog-datafiler inneheld DQV-eigenskapar:

```yaml
# brreg-begrepskatalog.yaml — noverande tilstand
begrep:
  - id: https://begrep.brreg.no/foretaksnavn
    anbefalt_term: [foretaksnavn]
    ...
    # ← ingen dqv:hasQualityMeasurement
```

Dei predefinerte kvalitetsmåla som er mest relevante for dette repoets data:

| Datasett | Dimensjon | Kvalitetsmål | Relevans |
|---|---|---|---|
| Begrepskatalog | Fullstendighet/underdekning | Andel begrep med manglande verdi for obligatorisk felt (t.d. `definisjon`) | Høg |
| Begrepskatalog | Aktualitet | Samla tidsdifferanse (kor lenge er eit begrep forelt før det vert oppdatert?) | Middels |
| Modellkatalog | Aktualitet | Samla tidsdifferanse (kor lenge frå modell er endra til katalogen er oppdatert?) | Middels |
| Modellkatalog | Fullstendighet | Andel modellar med manglande obligatoriske metadata (t.d. `dct:license`) | Høg |

**Status:** ⚠️ Avvik — ingen DQV-målingar i nokon publisert datafil.

---

### 2 — `dqv-ap-no`-skjema er ufullstendig

`src/linkml/ap-no/dqv-ap-no/dqv-ap-no-schema.yaml` finst, men
`Datasett`-klassen med `dqv:hasQualityMeasurement`-slot er kommentert ut:

```yaml
# Datasett:
#   class_uri: dcat:Dataset
#   slots:
#     - har_kvalitetsmaaling
#     ...
```

Skjemaet er aldri importert av `dcat-ap-no-schema.yaml`, `skos-ap-no-schema.yaml`
eller dei konkrete datasett-skjemaa (`brreg-begrepskatalog`, `brreg-modellkatalog`).

**Status:** ⚠️ Avvik — skjemaet er ein stub utan funksjonell bruk.

---

### 3 — Ingen mekanisme for å oppgi kvalitetsmålingar i datafiler

Datasett-datafiler (`data/<katalog>/<katalog>.yaml`) har ingen støtte for
å leggje til DQV-kvalitetsmålingar. Det finst inga:
- Slots for `dqv:hasQualityMeasurement` i begrepskatalog- eller modellkatalog-skjema
- Rettleiing til modelleigarar om korleis kvalitet skal beskrivas
- Policy-krav om kvalitetsskildring i `felles-datakatalog`- eller
  `felles-begrepskatalog`-policy

**Status:** ⚠️ Avvik — heile mekanismen manglar.

---

### 4 — Ikkje-kvantifiserbar kvalitet er heller ikkje støtta

Rettleiaren nemner `dqv:UserFeedback` og `dqv:QualityAnnotation` som alternativ
til kvantifisert kvalitet. Repoet støttar ingen av desse heller.

**Status:** ⚠️ Avvik (låg prioritet — rettleiaren prioriterer kvantifiserbar kvalitet).

---

## Samandrag

| # | Avvik | Status | Prioritet |
|---|---|---|---|
| 1 | `dqv:hasQualityMeasurement` manglar i alle publiserte datasett | ⚠️ Avvik | Middels |
| 2 | `dqv-ap-no`-skjema er ufullstendig og ubrukt | ⚠️ Avvik | Middels |
| 3 | Ingen mekanisme for å oppgi DQV i datafiler | ⚠️ Avvik | Middels |
| 4 | Ikkje-kvantifiserbar kvalitet ikkje støtta | ⚠️ Avvik | Låg |

---

## Tilrådde tiltak

### KV1 — Ferdigstill `dqv-ap-no`-skjema (Avvik 2)

Aktiver `Datasett`-klassen i `dqv-ap-no-schema.yaml` med minimum:
- `dqv:hasQualityMeasurement` → `KvalitetsMaaling`
- `KvalitetsMaaling`-klasse med `dqv:isMeasurementOf`, `dqv:value`, `rdfs:comment`

Import-kjeda bør bli:
```
dcat-ap-no-schema.yaml  →  importerer dqv-ap-no-schema.yaml
```
eller som valgfritt import i `brreg-begrepskatalog-schema.yaml` og
`brreg-modellkatalog-schema.yaml`.

**Filer:** `src/linkml/ap-no/dqv-ap-no/dqv-ap-no-schema.yaml`,
eventuelt `src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml`

---

### KV2 — Legg til DQV-støtte i begrepskatalog-skjema (Avvik 3)

Legg til valgfrie DQV-slots i `brreg-begrepskatalog-schema.yaml` (og tilsvarande
skjema for andre katalogar):

```yaml
slots:
  har_kvalitetsmaaling:
    slot_uri: dqv:hasQualityMeasurement
    range: KvalitetsMaaling
    multivalued: true
    inlined: true
    inlined_as_list: true
```

Modelleigarar kan deretter leggje til t.d.:

```yaml
katalog:
  - id: https://begrep.brreg.no/katalog
    har_kvalitetsmaaling:
      - mal_for_maaling: https://data.norge.no/vocabulary/quality-metric#qm-completeness-1004
        verdi: "0.02"
        kommentar: "2% av begrep manglar verdi for feltet 'definisjon'."
```

---

### KV3 — Legg til DQV-målingar i eksisterande datafiler (Avvik 1)

Etter KV1 og KV2: legg til faktiske kvalitetsmålingar i `brreg-begrepskatalog`
og `brreg-modellkatalog` datafiler med minimum:

- **Fullstendighet/underdekning** (`qm-completeness-1004`): andel einingar med
  manglande verdi for obligatorisk felt
- **Aktualitet** (`qm-currentness-1001`): samla tidsdifferanse mellom hendinga og
  oppdatering av katalogen

Desse verdiane kan eventuelt genereras automatisk av ein CI-skript som
analyserer datafila og reknar ut målinga.

---

### KV4 — Vurder automatisk kvalitetsmåling i CI (Avvik 1, 3)

Legg til eit skript (`src/assets/scripts/gen-dqv-measurements.py`) som for kvar
datafil med `data_policy: felles-begrepskatalog` eller `felles-datakatalog`:

1. Les datafila og tel obligatoriske felt
2. Reknar ut fullstendighetsgrad (andel einingar med manglande obligatoriske verdiar)
3. Skriv `dqv:hasQualityMeasurement`-blokker attende til datafila eller til
   ein generert sidefilledge RDF-fragment

Dette gjer at kvalitetsmålingane alltid er oppdaterte og ikkje krev manuell vedlikehald.

---

## Prioritert handlingsliste

| # | Tiltak | Fil / område | Avhengigheit |
|---|---|---|---|
| 1 | KV1: Ferdigstill `dqv-ap-no`-skjema | `dqv-ap-no-schema.yaml` | — |
| 2 | KV2: DQV-støtte i begrepskatalog-skjema | `brreg-begrepskatalog-schema.yaml` | KV1 |
| 3 | KV3: Legg til målingar i eksisterande datafiler | `brreg-begrepskatalog`, `brreg-modellkatalog` | KV1, KV2 |
| 4 | KV4: Automatisk kvalitetsmåling i CI | `src/assets/scripts/` | KV2, KV3 |

---

## Avhengigheiter

- KV1 er grunnmur for alt anna — `dqv-ap-no`-skjemaet må ha funksjonelle klasser
  og slots
- KV2 og KV3 krev at silver-policy-skjema er ferdigstilte (KV1 frå
  `avvik-veileder-apne-data.md` om lisens bør òg vere på plass)
- KV4 er eit mogleg seinare automatiseringstiltak og ikkje nødvendig for
  grunnleggjande DQV-støtte
