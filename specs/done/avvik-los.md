# Kartlegging: Avvik mot Los – Felles vokabular for klassifisering av offentlege tenester og ressursar

**Kjelde:** [digdir.no/los](https://www.digdir.no/informasjonsforvaltning/los-felles-vokabular-klassifisering-av-offentlige-tjenester-og-ressurser/2434)  
**Kanonisk namespace:** `https://psi.norge.no/los/`  
**Tilrådd bruk:** DCAT-AP-NO pkt. 8.6: `dcat:theme` skal bruke Los som primærvokabular  
**Implementasjonar i repoet:** datafiler i `src/linkml/`, `tema`-slot i `dcat-ap-no-schema.yaml` og `modelldcat-ap-no-schema.yaml`

---

## Bakgrunn

Los er eit SKOS-basert kontrollert vokabular for klassifisering av offentlege tenester og ressursar. Det inneheld:

| Bane | Formål | Døme |
|---|---|---|
| `/los/tema/[namn]` | Hovudtema og undertema | `psi.norge.no/los/tema/naring` |
| `/los/ord/[namn]` | Emneord (flatt vokabular) | `psi.norge.no/los/ord/abort` |
| `/los/hendelse/[namn]` | Livshendingar | `psi.norge.no/los/hendelse/fa-barn` |

Los har 14 hovudtema (sjå nedanfor) og eit stort tal undertema under kvart hovudtema.
Emneord (`/los/ord/`) er eit flatt komplementærvokabular — **ikkje** det same som hovud-/undertema.

> **Merk:** `/los/begrep/` finst **ikkje** i Los. Korrekte banar er `/los/tema/`, `/los/ord/` og `/los/hendelse/`.

### 14 gyldige Los-hovudtema (verifisert 2026-06)

| URI | Norsk term |
|---|---|
| `https://psi.norge.no/los/tema/arbeid` | Arbeid |
| `https://psi.norge.no/los/tema/bygg-og-eiendom` | Bygg og eiendom |
| `https://psi.norge.no/los/tema/demokrati-og-innbyggerrettigheter` | Demokrati og innbyggerrettigheter |
| `https://psi.norge.no/los/tema/familie-og-barn` | Familie og barn |
| `https://psi.norge.no/los/tema/helse-og-omsorg` | Helse og omsorg |
| `https://psi.norge.no/los/tema/kultur-idrett-og-fritid` | Kultur, idrett og fritid |
| `https://psi.norge.no/los/tema/lov-og-rett` | Lov og rett |
| `https://psi.norge.no/los/tema/naring` | Næring |
| `https://psi.norge.no/los/tema/natur-klima-og-miljo` | Natur, klima og miljø |
| `https://psi.norge.no/los/tema/samfunnssikkerhet-og-beredskap` | Samfunnssikkerhet og beredskap |
| `https://psi.norge.no/los/tema/skatt-og-avgift` | Skatt og avgift |
| `https://psi.norge.no/los/tema/skole-og-utdanning` | Skole og utdanning |
| `https://psi.norge.no/los/tema/sosiale-tjenester` | Sosiale tjenester |
| `https://psi.norge.no/los/tema/trafikk-og-transport` | Trafikk og transport |

---

## Kartlegging av avvik

### 1 — Kritisk datafeil: `naering-og-sysselsetting` er ugyldig Los-URI (404)

`src/linkml/modellkatalog/brreg-modellkatalog/data/brreg-modellkatalog/brreg-modellkatalog.yaml` (linjene 33, 46) og `brreg-modellkatalog-eksempel.yaml` (linje 31) brukar:

```yaml
tema:
  - https://psi.norge.no/los/tema/naering-og-sysselsetting
```

Dette URI-et returnerer HTTP 404. Hovudtemaet for næring i Los heiter **`naring`** (æ → a):

```
https://psi.norge.no/los/tema/naring
```

Undertemaet `Næringsliv` (`https://psi.norge.no/los/tema/naringsliv`) er gyldig, men er eit undertema under `naring`.

**Filer:**
- `src/linkml/modellkatalog/brreg-modellkatalog/data/brreg-modellkatalog/brreg-modellkatalog.yaml` (linjene 33, 46)
- `src/linkml/modellkatalog/brreg-modellkatalog/examples/brreg-modellkatalog-eksempel.yaml` (linje 31)

**Status:** ⚠️ Kritisk datafeil — returnerer 404

---

### 2 — Kritisk datafeil: `/los/begrep/`-sti er ugyldig; fleire tema-URI-ar er 404

`src/linkml/samt/samt-bu/examples/samt-bu-eksempel.yaml` brukar to typar feil Los-URI-ar:

**Feil 2a — `begrep`-bane finst ikkje i Los:**

```yaml
begrep:
  - https://psi.norge.no/los/begrep/elev       # 404
  - https://psi.norge.no/los/begrep/skole      # 404
  - https://psi.norge.no/los/begrep/kommune    # 404
  - https://psi.norge.no/los/begrep/grunnskole # 404
  - https://psi.norge.no/los/begrep/opplaering # 404
```

Los har ingen `/los/begrep/`-bane. Desse URI-ane returnerer alle 404.

`begrep`-sloten (`dct:subject`) peikar til fagomgrep i ein begrepskatalog — ikkje til Los. Viss det er Los-emneord som er meint, er korrekt bane `/los/ord/[namn]` (t.d. `los/ord/abort`). Men `/los/ord/elev` og dei andre ovanfor er heller ikkje verifiserte å eksistere. `dct:subject`-verdiar bør peike til definerte omgrep i `brreg-begrepskatalog` eller tilsvarande.

**Feil 2b — fleire tema-URI-ar er 404:**

```yaml
tema:
  - https://psi.norge.no/los/tema/skole       # 404 — ikkje eit Los-tema
  - https://psi.norge.no/los/tema/utdanning   # 404 — ikkje eit Los-tema
  - https://psi.norge.no/los/tema/elever      # 404 — ikkje eit Los-tema
  - https://psi.norge.no/los/tema/grunnskole  # ✓ gyldig undertema (verifisert)
  - https://psi.norge.no/los/tema/opplaering  # ikkje verifisert — truleg 404
```

Hovudtemaet for utdanning er `skole-og-utdanning`. Av undertema er `grunnskole` verifisert gyldig; resten er ikkje gyldige Los-URI-ar.

**Filer:**
- `src/linkml/samt/samt-bu/examples/samt-bu-eksempel.yaml` (linjene 11–22)

**Status:** ⚠️ Kritisk datafeil — fleire URI-ar returnerer 404

---

### 3 — Moderat datafeil: Undertema brukt utan hovudtema i begrepskatalog

`src/linkml/begrepskatalog/brreg-begrepskatalog/data/brreg-begrepskatalog/brreg-begrepskatalog.yaml` og tilhøyrande eksempelfil brukar:

```yaml
fagomrade:
  - https://psi.norge.no/los/tema/naringsliv
```

`naringsliv` er eit **gyldig** Los-undertema under hovudtemaet `naring`. Dette er teknisk sett korrekt bruk. DCAT-AP-NO tilrår imidlertid at hovudtemaet (`naring`) også inkluderast for at ressursen skal vere synleg under det overordna filteret i Felles datakatalog.

**Filer:**
- `src/linkml/begrepskatalog/brreg-begrepskatalog/data/brreg-begrepskatalog/brreg-begrepskatalog.yaml` (linjene 17, 36, 48)
- `src/linkml/begrepskatalog/brreg-begrepskatalog/examples/brreg-begrepskatalog-eksempel.yaml`

**Status:** ℹ️ Ikkje feil, men ufullstendig — låg prioritet

---

### 4 — Schemafeil: `tema.range: string` gjev ingen URI-validering i `dcat-ap-no`

I `src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml`:

```yaml
tema:
  slot_uri: dcat:theme
  range: string
  multivalued: true
  description: Tema frå eit kontrollert vokabular.
```

`range: string` godtek kva som helst tekststreng — inkludert feilskrivne URI-ar som `naering-og-sysselsetting` og `los/begrep/`-stiar. Avvika ovanfor vart ikkje oppdaga under validering nettopp fordi schema ikkje sjekkar at verdiane er gyldige URI-ar eller Los-konsept.

I `modelldcat-ap-no-schema.yaml` er `tema.range: Konsept`, som er meir presis — men det er `dcat-ap-no`-definisjonen som arvas av domenemodellane.

**Status:** ⚠️ Schemafeil — middels prioritet

---

### 5 — Schemafeil: Ingen `annotations` dokumenterer Los som tilrådd vokabular

Verken `tema`-sloten i `dcat-ap-no-schema.yaml` eller `modelldcat-ap-no-schema.yaml` har nokon
`description` eller annotasjon som peikar til Los som det tilrådde vokabularet for norske offentlege datasett.

Etter DCAT-AP-NO kap. 8.6 skal `dcat:theme` bruke:
1. Los (`psi.norge.no/los/tema/`) som primærvokabular
2. EuroVoc (`http://eurovoc.europa.eu/`) som sekundærvokabular

Ingen av desse er dokumentert i slotdefinisjonen.

Tilsvarende manglar `temaer`-sloten (`dcat:themeTaxonomy`) ei rettleiing om at Los-referansen
(`https://psi.norge.no/los/`) bør inkluderast i `Katalog.temaer` for å signalisere til Felles datakatalog at Los vert brukt.

**Status:** ⚠️ Manglande dokumentasjon — låg prioritet

---

### 6 — Ingen CLAUDE.md-rettleiing for korrekt Los-bruk

`CLAUDE.md` har ingen seksjon som rettleier om:
- Kva Los-bane som gjeld for `dcat:theme` (`/los/tema/`) vs. `dct:subject` (ikkje Los)
- Kva nivå som skal brukast (hovudtema vs. undertema) og om begge nivå bør inngå
- Korleis særnorske bokstavar translittererast i Los-URI-ar (æ → a, ø → o, å → a)

Mangelen på rettleiing er ein sannsynleg årsak til avvika i pkt. 1–3 ovanfor.

**Status:** ℹ️ Dokumentasjonsgap — låg prioritet

---

### 7 — Risiko: Los 4 er forventa å ikkje vere bakoverkompatibel

Los 4 var planlagt Q1 2026. Repoet inneheld hardkoda Los 3-URI-ar i fleire datafiler. Ei ikkje-bakoverkompatibel Los-oppdatering vil krevje gjennomgang av alle `tema`-verdiar i datakatalogen.

**Filer:** Alle datafiler med `psi.norge.no/los/`-URI-ar  
**Status:** ℹ️ Framtidsrisiko — følg opp ved Los 4-lansering

---

## Samandrag

| # | Avvik | Type | Prioritet |
|---|---|---|---|
| 1 | `naering-og-sysselsetting` → 404 i `brreg-modellkatalog` | Kritisk datafeil | **Kritisk** |
| 2a | `/los/begrep/`-URI-ar i `samt-bu-eksempel` → 404 | Kritisk datafeil | **Kritisk** |
| 2b | Fleire `tema`-URI-ar i `samt-bu-eksempel` → 404 | Kritisk datafeil | **Kritisk** |
| 3 | Undertema `naringsliv` utan overordna `naring` i begrepskatalog | Datafeil | Låg |
| 4 | `tema.range: string` — ingen URI-validering | Schemafeil | Middels |
| 5 | Ingen Los-dokumentasjon på `tema`- og `temaer`-slot | Dokumentasjon | Låg |
| 6 | Ingen CLAUDE.md-rettleiing for Los-bruk | Dokumentasjon | Låg |
| 7 | Los 4-risiko — ikkje bakoverkompatibel | Framtidsrisiko | Overvake |

---

## Tilrådde tiltak

### LO1 — Fiks `naering-og-sysselsetting` → `naring` i `brreg-modellkatalog` ✱ Kritisk ✓

```yaml
# Før
tema:
  - https://psi.norge.no/los/tema/naering-og-sysselsetting

# Etter
tema:
  - https://psi.norge.no/los/tema/naring
```

Gjeld:
- `src/linkml/modellkatalog/brreg-modellkatalog/data/brreg-modellkatalog/brreg-modellkatalog.yaml`
- `src/linkml/modellkatalog/brreg-modellkatalog/examples/brreg-modellkatalog-eksempel.yaml`

---

### LO2 — Fiks Los-URI-ar i `samt-bu-eksempel.yaml` ✱ Kritisk ✓

Steg 1: Fjern alle `begrep`-verdiar med `psi.norge.no`-URI-ar. `dct:subject` skal peike til
definerte fagomgrep i begrepskatalogen, ikkje til Los.

Steg 2: Erstatt ugyldige `tema`-verdiar med korrekte Los-URI-ar:

```yaml
# Før
tema:
  - https://psi.norge.no/los/tema/skole       # 404
  - https://psi.norge.no/los/tema/utdanning   # 404
  - https://psi.norge.no/los/tema/elever      # 404
  - https://psi.norge.no/los/tema/grunnskole  # ✓
  - https://psi.norge.no/los/tema/opplaering  # 404

# Etter
tema:
  - https://psi.norge.no/los/tema/skole-og-utdanning   # hovudtema
  - https://psi.norge.no/los/tema/grunnskole            # undertema (gyldig)
```

Steg 3: Erstatt `begrep`-URI-ane med referansar til definerte omgrep frå `brreg-begrepskatalog`
eller liknande, ikkje Los-URI-ar.

**Filer:** `src/linkml/samt/samt-bu/examples/samt-bu-eksempel.yaml`

---

### LO3 — Legg til Los-dokumentasjon på `tema`-sloten ✓

Legg til `description` og annotasjon i `dcat-ap-no-schema.yaml`:

```yaml
tema:
  slot_uri: dcat:theme
  range: uriorcurie
  multivalued: true
  description: >-
    Tema frå eit kontrollert vokabular. For norske offentlege datasett skal Los
    (https://psi.norge.no/los/) brukast som primærvokabular. Bruk hovudtema
    (https://psi.norge.no/los/tema/<namn>) og eventuelt undertema i tillegg.
    EuroVoc kan brukast som sekundærvokabular.
  annotations:
    gyldige_verdier: https://psi.norge.no/los/
```

Samstundes bør `range: string` endrast til `range: uriorcurie` for å signalisere at det er
URI-ar som er forventa (ikkje fritekst).

**Filer:** `src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml`

---

### LO4 — Legg til Los-rettleiing i `CLAUDE.md` ✓

Legg til ein seksjon under `Modelleringsprinsipper` i `CLAUDE.md`:

```markdown
### Los-tema i datasett og katalogar

`dcat:theme` (`tema`-sloten) skal bruke Los som primærvokabular:
- Hovudoversikt: https://psi.norge.no/los/ — alle tema: https://psi.norge.no/los/ontologi/tema.html — temastruktur: https://psi.norge.no/los/struktur.html — ord: https://psi.norge.no/los/ontologi/ord.html
- Hovudtema: `https://psi.norge.no/los/tema/<namn>`
- Undertema er lov å bruke i tillegg til hovudtemaet, ikkje i staden for det
- Særnorske bokstavar translittererast i URI: æ → a (naring), ø → o, å → a
- `/los/begrep/`-URI-ar finst ikkje — berre `/los/tema/`, `/los/ord/`, `/los/hendelse/`
- `dct:subject` (`begrep`-slot) peikar til fagomgrep i begrepskatalog — ikkje til Los
```

**Filer:** `CLAUDE.md`

---

### LO5 — Supplér `naringsliv` med `naring` i `brreg-begrepskatalog` ✓

```yaml
fagomrade:
  - https://psi.norge.no/los/tema/naring       # hovudtema
  - https://psi.norge.no/los/tema/naringsliv   # undertema
```

**Filer:**
- `src/linkml/begrepskatalog/brreg-begrepskatalog/data/brreg-begrepskatalog/brreg-begrepskatalog.yaml`
- `src/linkml/begrepskatalog/brreg-begrepskatalog/examples/brreg-begrepskatalog-eksempel.yaml`

---

## Prioritert handlingsliste

| # | Tiltak | Fil(ar) | Avhengigheit |
|---|---|---|---|
| 1 | LO1: Fiks `naering-og-sysselsetting` → `naring` | `brreg-modellkatalog.yaml`, eksempelfil | — |
| 2 | LO2: Fiks Los-URI-ar i `samt-bu-eksempel.yaml` | `samt-bu-eksempel.yaml` | — |
| 3 | LO4: Legg til Los-rettleiing i `CLAUDE.md` | `CLAUDE.md` | — |
| 4 | LO3: Los-dokumentasjon på `tema`-slot + `range: uriorcurie` | `dcat-ap-no-schema.yaml` | — |
| 5 | LO5: Supplér `naringsliv` med `naring` i begrepskatalog | begrepskatalog-datafiler | — |

---

## Avhengigheiter

- LO1 og LO2 er kritiske datafeil og bør rettast snarast — dei er uavhengige av kvarandre
- LO3 (`range: uriorcurie`) kan bryte eksisterande validering dersom andre verdiar enn URI-ar er i bruk — verifiser med `make validate-instance` etter endringa
- LO4 er dokumentasjon og har ingen tekniske avhengigheiter
- LO5 er ei suppleringsendring og er ikkje tidssensitiv

---

## Utført

Alle 5 tiltak utførte 2026-06-19.

- **LO1**: Retta ugyldig `naering-og-sysselsetting` → `naring` i `brreg-modellkatalog.yaml` og eksempelfil (2 førekomstar).
- **LO2**: Retta `samt-bu-eksempel.yaml` — erstatta 5 ugyldige `tema`-URI-ar med `skole-og-utdanning` + `grunnskole`, og fjerna heile `begrep`-seksjonen med `/los/begrep/`-URI-ar som ikkje finst i Los.
- **LO3**: Endra `tema.range` frå `string` → `uriorcurie` i `dcat-ap-no-schema.yaml` og la til Los-dokumentasjon og `gyldige_verdier`-annotasjon på `tema`- og `temaer`-slotane.
- **LO4**: La til seksjon «Los-tema i datasett og katalogar» under `Modelleringsprinsipper` i `CLAUDE.md` med lenker til hovudoversikt, temastruktur og ord.
- **LO5**: Supplerte undertema `naringsliv` med hovudtema `naring` i `fagomrade` for alle 3 begrep i `brreg-begrepskatalog` datafil og eksempelfil (6 førekomstar).
