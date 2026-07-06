# Feil i Imports-seksjon i samt-bu/index.md

## Bakgrunn

`mkdocs/docs/samt/samt-bu/index.md` viser feil Imports-seksjon:

```
linkml:types  # direkte import
└── common-ap-no-schema  # transitiv import
    └── dqv-ap-no-schema  # direkte import
```

Men `samt-bu-schema.yaml` importerer faktisk:
- `linkml:types` (direkte)
- `../../ap-no/dqv-ap-no/dqv-ap-no-schema` (direkte)

Og `dqv-ap-no-schema.yaml` importerer:
- `linkml:types`
- `../common/common-ap-no-schema`
- `../dcat-ap-no/dcat-ap-no-schema`

Så riktig Imports-seksjon bør vise:
- **Direkte:** `linkml:types`, `dqv-ap-no-schema`
- **Transitive:** `common-ap-no-schema`, `dcat-ap-no-schema`, `dqv-core-schema`

## Problem

`importhierarki.md` sin AP-NO-hierarki-seksjon har feil struktur og samsvarar ikkje med faktiske import-relasjonar i `.yaml`-skjemaa.

`src/assets/scripts/parse-dependency-tree.py` brukar `importhierarki.md` som kjelde for å generere Imports-seksjonar, så feil der propagerer til alle skjema-index-sider.

## Steg

### 1. Verifiser faktiske importar

Sjekk `imports:`-blokka i kvart AP-NO-skjema:

- [ ] `common-ap-no-schema.yaml`
- [ ] `dqv-core-schema.yaml`
- [ ] `dcat-ap-no-schema.yaml`
- [ ] `dqv-ap-no-schema.yaml`
- [ ] `skos-ap-no-schema.yaml`
- [ ] `modelldcat-ap-no-schema.yaml`

### 2. Teikn riktig hierarki

Basert på faktiske importar, lag ei korrekt visualisering av AP-NO-hierarkiet.
Handter "diamantproblem" (fleire skjema importerer same parent).

### 3. Oppdater `importhierarki.md`

Erstatt AP-NO-hierarki-seksjonen med riktig struktur.

### 4. Test generering

Køyr `mkdocs/publish.sh` og verifiser at `samt-bu/index.md` sin Imports-seksjon no viser riktige direkte/transitive importar.

### 5. Verifiser andre skjema

Sjekk at andre skjema sine Imports-seksjonar også ser riktige ut:
- [ ] `dcat-ap-no/index.md`
- [ ] `dqv-ap-no/index.md`
- [ ] `skos-ap-no/index.md`

## Utført

Alle steg er fullførte:

1. ✅ Verifiserte faktiske importar for alle AP-NO-skjema
2. ✅ Oppdaterte `importhierarki.md` med riktig hierarki (flytta `dqv-ap-no-schema` og `xkos-ap-no-schema` under `dcat-ap-no-schema`)
3. ✅ Fiksa `parse-dependency-tree.py` si depth-kalkulasjon til å handtere ASCII-tre med vertikale bar (`│`) riktig
4. ✅ Regenererte `mkdocs/docs/samt/samt-bu/index.md` med riktig Imports-seksjon
5. ✅ Verifiserte at output no viser riktige direkte/transitive importar

**Problem:** `parse_tree_lines()` rekna depth basert på rå antal mellomrom, ikkje faktisk tredjup. ASCII-tre brukar 4-teikns-blokkar (`"    "` eller `"│   "`) per nivå, men funksjonen tel berre leiaande mellomrom og ignorerte tree-tegn.

**Løysing:** Rekna depth ved å tel 4-teikns-blokkar i full prefix (inkl. tree-tegn), ikkje berre leiaande mellomrom.

## Notatar

- `parse-dependency-tree.py` tek inn `direct_imports_normalized` som tredje argument (normalised schema names)
- Python-scriptet filtrerer treet til kun vise path som leier til target-schemas
- Diamantproblem: fleire skjema importerer same parent (t.d. både `dcat-ap-no` og `dqv-ap-no` importerer `common-ap-no-schema`)
