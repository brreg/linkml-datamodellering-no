# Kartlegging: Avvik mot Veileder for beskrivelse av kvalitet på datasett - kvantifiserbar kvalitet

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

### KV1 — Ferdigstill `dqv-ap-no`-skjema (Avvik 2) ✓

**Utført:** Dette var allereie løyst i repoet (truleg som del av BUG-6-fiksen,
commit `49a093a1`) — kartlegginga over var forelda i forhold til faktisk
kodetilstand. `Datasett`-klassen i `dcat-ap-no-schema.yaml` har `har_kvalitetsmerknad`
og `har_kvalitetsmaaling` (Anbefalt) som peikar til `Kvalitetsmerknad`/`Kvalitetsmaaling`,
fullt definerte i `dqv-ap-no/dqv-core-schema.yaml` (importert transitivt via
`dcat-ap-no-schema.yaml`). Ingen kodeendring nødvendig for dette tiltaket.

**Filer:** `src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml`,
`src/linkml/ap-no/dqv-ap-no/dqv-core-schema.yaml` (allerede ferdigstilte)

---

### KV2 — Legg til DQV-støtte i begrepskatalog-skjema (Avvik 3) ✓

**Utført:** Lagt til `har_kvalitetsmaaling` (Anbefalt) på `Samling`-klassen i
`skos-ap-no-schema.yaml` (importerer no `dqv-core-schema.yaml`) og på
`Modellkatalog`-klassen i `modelldcat-katalog-schema.yaml` (hadde allereie
`dqv-core` i import-kjeda transitivt via `dcat-ap-no-schema.yaml`). Lagt til
`kvalitetsmaalingar`-attributt på `BegrepContainer` og `ModellkatalogContainer`
slik at `Kvalitetsmaaling`-instansar kan listast i datafilene.

**Avvik frå plan:** Eit namnekrasj dukka opp (slot-variant av BUG-7,
sjå `specs/bugs/duplicate-slot-merge-konflikt.md`) — `dqv-core-schema.yaml`
hadde sin eigen `har_definisjon`-slot (for å beskrive kvalitetsdimensjonar)
som kollapsa med `skos-ap-no-schema.yaml` sin `har_definisjon` (for omgrep)
når dei to skjemaa møttest i importgrafen. Løyst ved å gi den DQV-interne
sloten eit eige namn: `har_kvalitetsdefinisjon`.

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

### KV4 — Automatisk kvalitetsmåling i CI (Avvik 1, 3) ✓

**Utført:** Implementert før KV3 (skriptet trengtes for å generere KV3 sine
verdiar). `src/assets/scripts/gen-dqv-measurements.py` skannar alle
`data/*/manifest.yaml` med `data_policy: felles-begrepskatalog` eller
`felles-datakatalog`, reknar ut:
- **Fullstendighet** (`qm-completeness-1004`): andel einingar som manglar
  verdi for eit nøkkelfelt (`har_definisjon` for begrep, `lisens` for
  informasjonsmodellar)
- **Aktualitet** (`qm-currentness-1001`, berre felles-datakatalog): ISO 8601-
  varighet (`PxD`) frå nyaste `endringsdato` blant modellane til i dag

og skriv resultatet attende til datafila med **målretta tekstinnsetting**
(ikkje full YAML-omskriving), slik at handskrivne kommentarar og formatering
i datafila er bevart. Målings-id-ane er stabile (`.../dqv/fullstendighet`,
`.../dqv/aktualitet`), så gjentatte køyringar oppdaterer verdiane i staden
for å hope opp duplikat. Lagt til `make gen-dqv-measurements`-target og
kalla skriptet frå `update-dates`-jobben i `.github/workflows/release-please.yml`
(same mønster og commit som `update-schema-dates.py`).

**Avvik frå plan:** Først skrive med full `yaml.safe_load` + `yaml.dump`
roundtrip (som planlagt), men dette viska ut alle kommentarar og
seksjonsskiljer i `brreg-begrepskatalog.yaml` (ikkje akseptabelt for ei
gjentakande CI-handling). Omskrive til regex-basert tekstinnsetting (samme
prinsipp som `update-schema-dates.py`) — løyser oppgava utan å innføre nye
avhengigheiter (t.d. `ruamel.yaml`).

**Filer:** `src/assets/scripts/gen-dqv-measurements.py`, `Makefile`,
`.github/workflows/release-please.yml`

---

### KV3 — Legg til DQV-målingar i eksisterande datafiler (Avvik 1) ✓

**Utført:** Køyrde `gen-dqv-measurements.py` mot dei to eksisterande
datafilene. Faktiske resultat (basert på reell data per 2026-06-20):

- `brreg-begrepskatalog.yaml`: 0 av 3 begrep (0,0 %) manglar `har_definisjon`
  → `har_kvalitetsmaaling` lagt til på `samlingar[0]` (Samlinga «registerbegrep-2025»)
- `brreg-modellkatalog.yaml`: 0 av 2 informasjonsmodellar (0,0 %) manglar
  `lisens`; eldste `endringsdato` er 1 dag gammal (`P1D`) → `har_kvalitetsmaaling`
  lagt til på `modellkataloger[0]`

Validert med `make validate-instance` og `make mcp-validate POLICY=felles-begrepskatalog`/
`felles-datakatalog` — `valid: true`, `errorCount: 0` for begge.

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

---

## Utført

Alle fire tiltak (KV1-KV4) er gjennomførte:

- **KV1** var allereie løyst i repoet før denne specen blei utført (forelda
  kartlegging) — ingen kodeendring.
- **KV2**: `har_kvalitetsmaaling` lagt til på `Samling` (`skos-ap-no-schema.yaml`,
  no med import av `dqv-core-schema.yaml`) og `Modellkatalog`
  (`modelldcat-katalog-schema.yaml`). `kvalitetsmaalingar`-attributt lagt til
  på `BegrepContainer` og `ModellkatalogContainer`. Eit namnekrasj
  (`har_definisjon` i `dqv-core-schema.yaml` vs. `skos-ap-no-schema.yaml`,
  slot-variant av BUG-7) blei løyst ved å gi DQV-sloten namnet
  `har_kvalitetsdefinisjon`.
- **KV4**: nytt skript `src/assets/scripts/gen-dqv-measurements.py` reknar ut
  fullstendighet/aktualitet og skriv målingar attende til datafilene med
  målretta tekstinnsetting (ikkje full YAML-omskriving, for å bevare
  handskrivne kommentarar). Lagt til `make gen-dqv-measurements` og eit steg
  i `update-dates`-jobben i `.github/workflows/release-please.yml`.
- **KV3**: skriptet køyrt mot `brreg-begrepskatalog.yaml` og
  `brreg-modellkatalog.yaml` — begge har no reelle `dqv:hasQualityMeasurement`-
  referansar. Validert med `make validate-instance` og `make mcp-validate`
  (felles-begrepskatalog/felles-datakatalog), `errorCount: 0` for begge.

**Avvik frå opphavleg plan:**
1. KV1 var allereie ferdig — kartlegginga i specen var forelda i forhold til
   faktisk kodetilstand (truleg løyst i BUG-6-fiksen, commit `49a093a1`).
2. KV4 blei implementert før KV3 (skriptet trengtes for å generere KV3 sine
   verdiar), ikkje etter som tabellen i «Prioritert handlingsliste» antyda.
3. `gen-dqv-measurements.py` brukar regex-basert tekstinnsetting i staden for
   full YAML-dump, for å unngå å viske ut eksisterande kommentarar/formatering
   i datafilene — og for å unngå ei ny avhengigheit (`ruamel.yaml`).
4. Alle nye DQV-slots/attributtar er avgrensa til katalog-/samlingsnivå
   (`Samling`, `Modellkatalog`) — ikkje på enkelt-`Begrep`/`Informasjonsmodell`,
   sidan kvalitetsmåla i kartlegginga (avvik 1) er aggregerte katalogmål, ikkje
   per-instans-mål.
