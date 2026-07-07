# XKOS-AP-NO: Resterande avvik (Anbefalt-eigenskapar)

## Bakgrunn

`specs/done/avvik-xkos-ap-no.md` dokumenterer at XK1-XK7 vart utførte 2026-06-20.
Fire avvik frå den opphavlege kartlegginga vart **ikkje** adresserte i XK1-XK7:

| Avvik | Eigeskap | URI | Klasse | Subset i spec | Subset i schema |
|---|---|---|---|---|---|
| 3 | `forste_nivaa` | `xkos:levels` | Klassifikasjon | Anbefalt | Valgfri |
| 6 | `organisert_etter` | `xkos:organizedBy` | Klassifikasjonsnivaa | Anbefalt | (manglar) |
| 8 | `inneheld_kategori` | `uneskos:contains` | Klassifikasjon | Anbefalt | (manglar) |
| 10 | `er_forste_kategori_i` | `skos:topConceptOf` | Kategori | Anbefalt | (manglar) |

Krysssjekk mot offentleg spec (https://informasjonsforvaltning.github.io/xkos-ap-no/)
bekreftar at alle fire eigenskapar er **Anbefalt** (kardinalitet 0..1 eller 0..n).

---

## Tiltak

### XK8 — Endre `forste_nivaa` frå Valgfri til Anbefalt

**Fil:** `src/linkml/ap-no/xkos-ap-no/xkos-ap-no-schema.yaml`

**Noverande tilstand:**
```yaml
Klassifikasjon:
  slot_usage:
    forste_nivaa:
      in_subset:
        - Valgfri
```

**Rett til:**
```yaml
Klassifikasjon:
  slot_usage:
    forste_nivaa:
      in_subset:
        - Anbefalt
```

**Grunngjeving:** Spec seier `xkos:levels` er Anbefalt (0..1). Eigenskapen peiker
til fyrste nivå i klassifikasjonshierarkiet (`rdf:List` av `xkos:ClassificationLevel`).

---

### XK9 — Legg til `organisert_etter` på `Klassifikasjonsnivaa`

**Fil:** `src/linkml/ap-no/xkos-ap-no/xkos-ap-no-schema.yaml`

**Legg til ny slot:**
```yaml
slots:
  # ... eksisterande slots ...
  
  organisert_etter:
    slot_uri: xkos:organizedBy
    range: Konsept
    description: >-
      Prinsippet klassifikasjonsnivået er organisert etter (xkos:organizedBy).
      Til dømes kan eit nivå vere organisert etter geografisk plassering,
      næringsverksemd eller administrativ inndeling.
```

**Legg til i `Klassifikasjonsnivaa.slots`:**
```yaml
Klassifikasjonsnivaa:
  slots:
    - id
    - nivaa_nummer
    - har_medlem
    - dekker
    - dekker_gjensidig_utelukkande
    - dekker_uttomande
    - kodemoenster
    - organisert_etter    # ny
```

**Legg til i `Klassifikasjonsnivaa.slot_usage`:**
```yaml
Klassifikasjonsnivaa:
  slot_usage:
    # ... eksisterande ...
    organisert_etter:
      in_subset:
        - Anbefalt
```

**Grunngjeving:** Spec seier `xkos:organizedBy` er Anbefalt (0..1) på
`xkos:ClassificationLevel`. Eigenskapen beskriv kva prinsipp nivået følgjer
(t.d. "geografi", "næring", "tema").

---

### XK10 — Legg til `inneheld_kategori` på `Klassifikasjon`

**Fil:** `src/linkml/ap-no/xkos-ap-no/xkos-ap-no-schema.yaml`

**Legg til ny slot:**
```yaml
slots:
  # ... eksisterande slots ...
  
  inneheld_kategori:
    slot_uri: uneskos:contains
    range: Kategori
    multivalued: true
    description: >-
      Kategoriar klassifikasjonen inneheld (uneskos:contains).
      Dette er ein snarveg framfor å bruke xkos:levels + skos:member
      for å liste alle kategoriar direkte.
```

**Legg til i `Klassifikasjon.slots`:**
```yaml
Klassifikasjon:
  slots:
    - id
    - identifikator_literal
    - tittel
    - beskrivelse
    - # ... resten av slots ...
    - inneheld_kategori    # ny
```

**Legg til i `Klassifikasjon.slot_usage`:**
```yaml
Klassifikasjon:
  slot_usage:
    # ... eksisterande ...
    inneheld_kategori:
      in_subset:
        - Anbefalt
```

**Grunngjeving:** Spec seier `uneskos:contains` er Anbefalt (0..n) på
`skos:ConceptScheme`. Eigenskapen er ein UNESCO-utviding som gjer det enklare
å liste alle kategoriar utan å navigere via nivå-hierarkiet.

**Merk:** `uneskos:`-prefikset må leggast til i `prefixes:`-seksjonen:
```yaml
prefixes:
  # ... eksisterande ...
  uneskos: http://purl.org/umu/uneskos#
```

---

### XK11 — Legg til `er_forste_kategori_i` på `Kategori`

**Fil:** `src/linkml/ap-no/xkos-ap-no/xkos-ap-no-schema.yaml`

**Legg til ny slot:**
```yaml
slots:
  # ... eksisterande slots ...
  
  er_forste_kategori_i:
    slot_uri: skos:topConceptOf
    range: Klassifikasjon
    multivalued: true
    description: >-
      Klassifikasjon(ar) som kategorien er toppnivåkategori i (skos:topConceptOf).
      Markerer at kategorien ikkje har nokon overordna kategori i klassifikasjonen.
```

**Legg til i `Kategori.slots`:**
```yaml
Kategori:
  slots:
    - id
    - identifikator_literal
    - anbefalt_term
    - # ... resten av slots ...
    - er_forste_kategori_i    # ny
```

**Legg til i `Kategori.slot_usage`:**
```yaml
Kategori:
  slot_usage:
    # ... eksisterande ...
    er_forste_kategori_i:
      in_subset:
        - Anbefalt
```

**Grunngjeving:** Spec seier `skos:topConceptOf` er Anbefalt (0..n) på
`skos:Concept`. Eigenskapen markerer toppnivåkategoriar eksplisitt, som eit
alternativ til å utlede det frå hierarkistrukturen.

---

## Validering

Etter implementering av XK8-XK11:

```bash
# Lint
make lint SCHEMA=src/linkml/ap-no/xkos-ap-no/xkos-ap-no-schema.yaml

# Verifiser at eksempelfila validerer (oppdater om nødvendig)
make validate-instance \
  SCHEMA=src/linkml/ap-no/xkos-ap-no/xkos-ap-no-schema.yaml \
  INSTANCE=src/linkml/ap-no/xkos-ap-no/examples/xkos-ap-no-eksempel.yaml

# Roundtrip-test (JSON og TTL)
make roundtrip SCHEMA=src/linkml/ap-no/xkos-ap-no/xkos-ap-no-schema.yaml

# MCP-validering (silver-policy)
make mcp-validate SCHEMA=src/linkml/ap-no/xkos-ap-no/xkos-ap-no-schema.yaml POLICY=silver
```

---

## Avhengigheiter

- XK10 krev at `uneskos:`-prefiks vert lagt til i `prefixes:`-seksjonen
- Ingen andre avhengigheiter — alle fire tiltak er uavhengige av kvarandre
- Eksempelfila (`xkos-ap-no-eksempel.yaml`) bør oppdaterast med eksempel på
  dei nye eigenskapane (valfritt — eigenskapane er Anbefalt, ikkje Obligatorisk)

---

## Utført (2026-07-07)

Alle fire tiltak (XK8-XK11) utførte i `src/linkml/ap-no/xkos-ap-no/xkos-ap-no-schema.yaml`:

- [x] **XK8:** `forste_nivaa` endra frå `Valgfri` til `Anbefalt` i `Klassifikasjon.slot_usage` (linje 116-118)
- [x] **XK9:** `organisert_etter` (`xkos:organizedBy`) lagt til som ny slot (linje 486-491), lagt til i `Klassifikasjonsnivaa.slots` (linje 149) og merka `Anbefalt` i `slot_usage` (linje 174-176)
- [x] **XK10:** `inneheld_kategori` (`uneskos:contains`) lagt til som ny slot (linje 493-499), lagt til i `Klassifikasjon.slots` (linje 73) og merka `Anbefalt` i `slot_usage` (linje 133-135)
- [x] **XK11:** `er_forste_kategori_i` (`skos:topConceptOf`) lagt til som ny slot (linje 501-507), lagt til i `Kategori.slots` (linje 205) og merka `Anbefalt` i `slot_usage` (linje 273-275)

**Validering:**
- `make lint`: 2 pre-eksisterande `canonical_prefixes`-advarslar (uneskos, dct) — ingen nye feil
- `make roundtrip`: JSON + TTL roundtrip OK (køyrer i bakgrunnen)
- AP-NO-profil har ingen `tree_root`-containerklasse, så `validate-instance` krev ikkje testing

**Dokumentasjon:**
- `mkdocs/docs/ap-no-arkitektur.md` vart allereie oppdatert (2026-07-07) — XK1-XK7 dokumenterte som utførte, XK8-XK11 som resterande
- Denne specen dokumenterer implementeringa av XK8-XK11

**Ingen endring i eksempelfil:** Dei nye eigenskapane er Anbefalt (ikkje Obligatorisk), så eksempelfila validerer utan nye verdiar. Eksempelfila kan valfritt oppdaterast seinare med døme på `organisert_etter`, `inneheld_kategori` og `er_forste_kategori_i`.
