# Pedagogisk evaluering: ny-domenemodell.md

## Overordna vurdering

Sida er teknisk korrekt men har eit strukturproblem: **referanseinnhald er blanda inn
i arbeidsflyten** i staden for å liggje samla etterpå. Ein ny brukar som les sekvensielt
møter importhierarki og AP-NO-detaljar midt i ein handlingsorientert guide, og er ikkje
klar for dette stoffet på det tidspunktet.

---

## Konkrete problem

### 1. Steg 2 ("Rediger skjemaet") er for tynt

Steg 2 seier berre «opne fila og legg til klasser, slots og importar» og peikar til
to ankerpunkt lenger nede. Det gir ikkje nok til å kome i gang. Brukaren treng minst:
- kva imports dei typisk skal velje (ein setning med beslutningsregel)
- eit minimum av kva dei skal endre i stub-klassen

Referanseskjema-bolken (lenger nede) burde vore lenka eller summert her, ikkje gøymd
til sist.

### 2. Importhierarki og "Kva importerer du?" kjem for tidleg — og er for splitta

Desse to bolkane heng tett saman og er begge referanseinnhald. Dei kjem rett etter
arbeidsflyten, men burde liggje i ein samla «Referanse»-seksjon. I tillegg er
«Importhierarki» (ASCII-tre) og «Kva importerer du?» (beslutningstabell) eigentleg
same spørsmål sett frå to vinklar — det er ikkje openbert kvifor dei er skilde.

### 3. "Kva får du frå AP-NO-profilane" kjem for seint og er lausrive

Denne bolken gir nyttig kontekst *før* ein vel kva som skal importerast, men ligg
*etter* beslutningsbolken. Rekkefølgja er baklengs.

### 4. "Referanseskjema" burde kome tidleg, ikkje sist

Referanseskjemaet er det mest konkrete hjelpemiddelet for ein ny brukar. Det vert
omtalt i steg 2 («Sjå Referanseskjema»), men sjølve bolken ligg heilt til slutt —
etter Genererte artefakter og Tilpass manifest. Ein brukar som følgjer lenka frå
steg 2 vert kasta ned til slutten av sida.

### 5. "Modelleringsprinsipp" og "Sjekkliste" høyrer saman

Prinsippa er grunnlaget for sjekklista. Dei bør liggje side om side (prinsipp → sjekkliste),
ikkje skilde av andre bolkar.

### 6. "Genererte artefakter" og "Tilpass manifest" er lausrivne frå arbeidsflyten

Desse er naturlege steg etter at skjemaet er ferdig — men i dag ligg dei mellom
«FAIR-konformitet» og «Referanseskjema» utan tydeleg samanheng.

---

## Tilrådd rekkefølgje

```
# Rettleiing: ny domenemodell

## Arbeidsflyt                        ← uendra, steg 0-4
   (steg 2 utvida med beslutningsregel for import og peikar til Referanseskjema)

## Referanseskjema                    ← flytt opp frå botnen
   (oppslagsverk — naturleg å finne tidleg)

## Kva importerer du?                 ← slå saman med Importhierarki
   Importhierarki (ASCII-tre)
   Beslutningstabell
   Kva arvar du frå AP-NO-profilene?  ← flytt inn her, ikkje eigen bolk

## FAIR-konformitet med fair-metadata ← uendra plassering, naturleg etter import-bolken

## Tilpass manifest                   ← flytt opp frå botnen
## Genererte artefakter               ← flytt opp frå botnen

## Modelleringsprinsipp               ← uendra
## Sjekkliste før innsjekking         ← uendra (avsluttande)
```

---

## Oppsummering av endringar

| Bolk | No | Tilrådd |
|---|---|---|
| Referanseskjema | Nedst | Rett etter Arbeidsflyt |
| Importhierarki + Kva importerer du? | To skilde bolkar, midt i | Slå saman til éin, etter Referanseskjema |
| Kva får du frå AP-NO | Etter beslutningsbolken | Inn i den samanslåtte import-bolken |
| Tilpass manifest | Nedst | Etter FAIR-bolken |
| Genererte artefakter | Etter FAIR-bolken | Saman med Tilpass manifest |
| Modelleringsprinsipp + Sjekkliste | Nedst | Behald — passar som avslutning |

---

## Foreslått nytt innhald

```markdown
# Rettleiing: ny domenemodell

## Arbeidsflyt

### 0 — Sjekk føresetnader og bygg images (éin gong)

```bash
make check-prereqs
make linkml-build-docker && make python-build-docker && make mcp-val-build
```

### 1 — Scaffold

```bash
make new-model NAME=<namn> DOMAIN=<domene>
```

Dette oppretter:
```
src/linkml/<domene>/<namn>/
├── <namn>-schema.yaml       ← hovudskjema med stub-klasse og containerklasse
├── manifest.yaml            ← publiserings- og generatorkonfig
└── examples/
    └── <namn>-eksempel.yaml ← eksempelfil med minimal instans
```
Skjemaet passerer [`POLICY=bronze`](https://github.com/brreg/linkml-datamodellering-no/blob/main/src/mcp-linkml-validator/README.md#bronse) utan manuell redigering.

### 2 — Rediger skjemaet

Bruk [Referanseskjema](#referanseskjema) som oppslagsverk.

Opne `src/linkml/<domene>/<namn>/<namn>-schema.yaml` og gjer følgjande:

1. **Gi stub-klassen eit norsk PascalCase-namn** (t.d. `Grunneigedom` i staden for `mitt_register`).
2. **Vel rett import** — sjå [Kva importerer du?](#kva-importerer-du) nedanfor.
3. **Legg til slots og slot_usage** for eigenskapane i modellen.

### 3 — Valider undervegs

```bash
make mcp-validate SCHEMA=src/linkml/<domene>/<namn>/<namn>-schema.yaml POLICY=bronze
make mcp-validate SCHEMA=src/linkml/<domene>/<namn>/<namn>-schema.yaml POLICY=silver
make mcp-validate SCHEMA=src/linkml/<domene>/<namn>/<namn>-schema.yaml POLICY=gold
```

| Policy | Sjekkar |
|---|---|
| [`bronze`](https://github.com/brreg/linkml-datamodellering-no/blob/main/src/mcp-linkml-validator/README.md#bronse) | `id`, `name`, `description`; alle klasser har identifikator og begrepsreferanse til felles begrepskatalog |
| [`silver`](https://github.com/brreg/linkml-datamodellering-no/blob/main/src/mcp-linkml-validator/README.md#s%C3%B8lv) | Bronze + skjemaet inneheld obligatoriske klasser i DCAT-AP-NO og DQV-AP-NO |
| [`gold`](https://github.com/brreg/linkml-datamodellering-no/blob/main/src/mcp-linkml-validator/README.md#gull) | Silver + FAIR F1-R1.3: `class_uri`, lisens, proveniens m.m. |

### 4 — Full testsuite

```
make test SCHEMA=src/linkml/<domene>/<namn>/<namn>-schema.yaml
```

Lint + validering + alle generatorar for eitt skjema. Utan `SCHEMA=` køyrer testsuiten for alle skjema.

---

## Referanseskjema

[`src/linkml/referanse/referanse-schema.yaml`](https://github.com/brreg/linkml-datamodellering-no/blob/main/src/linkml/referanse/referanse-schema.yaml) er eit annotert eksempelskjema som viser alle hovudmønster brukte i dette repoet: containerklasse, globale slots, import frå AP-NO-profil, `class_uri`/`slot_uri`, `LangString` og `in_subset`. Bruk det som oppslagsverk når du startar eit nytt skjema.

---

## Kva importerer du?

| Du lagar … | Importer |
|---|---|
| Ein AP-NO-profil | `linkml:types` + `../common/common-ap-no-schema` |
| Ein domenemodell (NGR, o.l.) | `linkml:types` + aktuelle AP-NO-profil(ar) |
| Ein FINT-domenemodell | `linkml:types` + `../fint-common/fint-common-schema` |
| Modell med FAIR-metadata | `linkml:types` + `../../fair/fair-metadata/fair-metadata-schema` |

Domenemodeller importerer **AP-NO-profilane** — ikkje `common-ap-no` direkte. Dei arvar typar, subsets og slots frå AP-NO automatisk gjennom profilane.

### Importhierarki

```
linkml:types          (alltid)
    ↓
common-ap-no          (berre AP-NO-profilane importerer denne direkte)
    ↓
dcat-ap-no / dqv-ap-no / skos-ap-no / …   (AP-NO-profiler)
    ↓
domenemodell          (importerer éin eller fleire AP-NO-profiler)

fint-common           (berre FINT-domenemodellane importerer denne)
    ↓
fint-administrasjon / fint-arkiv / …

fair-metadata         (kan importerast av alle domenemodeller)
```

### Kva arvar du frå AP-NO-profilane?

Ved å importere ein AP-NO-profil arvar du automatisk alt frå `common-ap-no` — du treng ikkje importere `common-ap-no` direkte.

**Typar frå `common-ap-no`**

| Namn | RDF-type | Bruk |
|---|---|---|
| `LangString` | `rdf:langString` | Fleirspråklege strenger (tittel, skildring …) |
| `Duration` | `xsd:duration` | Varigheit, t.d. `PT15M` |
| `GYear` | `xsd:gYear` | Årstal, t.d. `2024` |
| `NonNegativeInteger` | `xsd:nonNegativeInteger` | Telling, storleik |

**Gjenbrukbare slots (døme)**

```yaml
classes:
  MittObjekt:
    slots:
      - id          # identifier: true, range: uriorcurie
      - tittel      # slot_uri: dct:title, range: LangString
      - beskrivelse # slot_uri: dct:description, range: LangString
      - utgiver     # slot_uri: dct:publisher, range: uriorcurie
      - lisens      # slot_uri: dct:license, range: uriorcurie
```

Sjå `src/linkml/ap-no/common/common-ap-no-schema.yaml` for full liste.

---

## FAIR-konformitet med fair-metadata

For å dokumentere at ein ressurs er FAIR-konform, importer `fair-metadata`:

```yaml
imports:
  - linkml:types
  - ../../ap-no/dcat-ap-no/dcat-ap-no-schema
  - ../../fair/fair-metadata/fair-metadata-schema
```

Valider mot gold-policy (gold-policy validerer spesifikt FAIR konformitet):

```bash
make mcp-validate SCHEMA=src/linkml/<domene>/<namn>/<namn>-schema.yaml POLICY=gold
```

---

## Tilpass manifest for generering og publisering

Kvar modell har ei `manifest.yaml` ved sida av skjemafila som styrer kva artefaktar
som vert genererte. `make new-model` oppretter standardkonfigen automatisk — alle
generatorar på, ingen ekstra flagg.

For å slå av ein generator eller leggje til flagg, rediger `manifest.yaml` og køyr:

```bash
make config.mk   # regenerer Makefile-konfig frå alle manifest.yaml-filer
```

Sjå [Modellmanifest](manifest-config.md) for feltliste og eksempel per
domenetype (standard, FINT, AP-NO/FAIR).

## Genererte artefakter

Sjå [Genererte artefakter](https://github.com/brreg/linkml-datamodellering-no#genererte-artefakter) i README for full oversikt over kva som vert generert per skjema.

---

## Modelleringsprinsipp

**Norsk bokmål** — alle klassenamn, slotnamn og skildringar skrivast på bokmål. Unntak: tekniske omgrep fastsett i ein spesifikasjon (t.d. `dcat:Dataset` → `Datasett`).

**Slots, ikkje attributes** — alle eigenskapar definerast som globale `slots:` på toppnivå, aldri som `attributes:` inne i ein klasse.

**Lenking framfor inlining** — klasser som kan opptre sjølvstendig får `id`-slot med `identifier: true`. Referansar til slike klasser skal *ikkje* ha `inlined: true`.

**Eksplisitte URI-ar** — alle klasser skal ha `class_uri` (unntatt `tree_root`-containerklassar). Alle slots skal ha `slot_uri`.

**`slot_usage` for klassespesifikke innskrenkingar** — `required: true` og `in_subset:` setjast i `slot_usage` på klassen, ikkje i den globale slotdefinisjonen.

---

## Sjekkliste før innsjekking

```
[ ] id er ein HTTPS-URI
[ ] title og description er sett på skjemanivå
[ ] version er sett (t.d. "1.0.0")
[ ] Importerer AP-NO-profil(ar) — ikkje common-ap-no direkte
[ ] Klasse- og slotnamn er på norsk bokmål
[ ] Alle klasser (unntatt tree_root) har class_uri
[ ] Alle globale slots har slot_uri
[ ] make mcp-validate POLICY=bronze gir 0 feil
[ ] make test køyrer utan feil
```
```
