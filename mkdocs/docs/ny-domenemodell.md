# Rettleiing: ny domenemodell

## Kom i gang

```bash
make new-model NAME=mitt-register DOMAIN=oreg
```

Dette oppretter:

- `src/linkml/oreg/mitt-register/mitt-register-schema.yaml` — skjema med stub-klasse og containerklasse
- `examples/oreg/mitt-register-eksempel.yaml` — eksempelfil med minimal instans

Skjemaet passerer `POLICY=bronze` utan manuell redigering. Nye skjema vert oppdaga automatisk — ingen endringar i Makefile nødvendig.

---

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

### 2 — Rediger skjemaet

Opne `src/linkml/<domene>/<namn>/<namn>-schema.yaml` og legg til klasser, slots og importar. Sjå [Importhierarki](#importhierarki) og [Kva importerer du?](#kva-importerer-du) nedanfor.

### 3 — Valider undervegs

```bash
make mcp-validate SCHEMA=src/linkml/<domene>/<namn>/<namn>-schema.yaml POLICY=bronze
make mcp-validate SCHEMA=src/linkml/<domene>/<namn>/<namn>-schema.yaml POLICY=silver
make mcp-validate SCHEMA=src/linkml/<domene>/<namn>/<namn>-schema.yaml POLICY=gold
```

| Policy | Sjekkar |
|---|---|
| `bronze` | `id`, `name`, `description`; alle klasser har identifikator og begrepsreferanse til felles begrepskatalog |
| `silver` | Bronze + skjemaet importerer DCAT-AP-NO og DQV-AP-NO |
| `gold` | Silver + FAIR F1–R1.3: `class_uri`, lisens, proveniens m.m. |

Validatoren bygger containerimaget automatisk første gong. Endringar i skjemaet tek effekt umiddelbart — ingen rebuild nødvendig.

### 4 — Full testsuite

```bash
make test SCHEMA=src/linkml/<domene>/<namn>/<namn>-schema.yaml
```

Lint + validering + alle generatorar for eitt skjema. Utan `SCHEMA=` køyrer testsuiten for alle skjema.

---

## Importhierarki

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

Domenemodeller importerer **AP-NO-profilane** — ikkje `common-ap-no` direkte. Dei arvar typar, subsets og slots frå AP-NO automatisk gjennom profilane.

---

## Kva importerer du?

| Du lagar … | Importer |
|---|---|
| Ein AP-NO-profil | `linkml:types` + `../common/common-ap-no-schema` |
| Ein domenemodell (NGR, o.l.) | `linkml:types` + aktuelle AP-NO-profil(ar) |
| Ein FINT-domenemodell | `linkml:types` + `../fint-common/fint-common-schema` |
| Modell med FAIR-dokumentasjon | + `../../fair/fair-metadata/fair-metadata-schema` |

---

## Kva får du frå AP-NO-profilane

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

Valider mot gold-policy:

```bash
make mcp-validate SCHEMA=src/linkml/<domene>/<namn>/<namn>-schema.yaml POLICY=gold
```

---

## Genererte artefaktar

Sjå [Genererte artefakter](https://github.com/brreg/linkml-datamodellering-no#genererte-artefakter) i README for full oversikt over kva som vert generert per skjema.

---

## Referanseskjema

`src/linkml/referanse/referanse-schema.yaml` er eit annotert eksempelskjema som viser alle hovudmønster brukte i dette repoet: containerklasse, globale slots, import frå AP-NO-profil, `class_uri`/`slot_uri`, `LangString` og `in_subset`. Bruk det som oppslagsverk når du startar eit nytt skjema.

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
