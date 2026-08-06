# gold-policy oppgraderer ikkje alle warning-sjekker til error

## Bakgrunn

**Problem:** Ved validering av `referansemodell-goldschema.yaml` mot gold-policyen vart
desse funna rapporterte som warning, sjølv om brukaren forventa error:

1. `schema_field_present` — `schema.license` manglar (nøkkel: `schema_has_license` i bronze.yaml)
6. `class_missing_recommended_slot` — klassa `Distribusjon` manglar slot med `dct:license`
   (nøkkel: `distribusjon_lisens` i silver.yaml)

**Rotårsak:**

`gold.yaml` sin description (linje 8) seier eksplisitt:
> "Alle brot gir feil — gullstatus er krevjande å oppnå."

og kommentaren over `checks:`-blokka (linje 24) seier:
> "Oppgrader bronze-åtvarslane til feil på gullnivå."

Men merge-logikken i `server.py:_merge_policies()` (linje 42-46) gjer
`{**parent_checks, **child_checks}` — ein sjekk-nøkkel arvar `severity: warning`
frå bronze/silver med mindre **akkurat den same nøkkelen** vert redefinert i
`gold.yaml` sine `checks:`/`fair_checks:`-blokker.

`gold.yaml` redefinerer i dag berre 7 nøklar som `error`:
`all_classes_have_class_uri`, `all_slots_have_slot_uri`, `f2_title`, `f4_version`,
`i2_standard_prefixes`, `r11_license`, `r12_provenance`.

Følgjande nøklar frå bronze.yaml/silver.yaml har `severity: warning` og vert
**ikkje** oppgraderte, i strid med gold.yaml sin dokumenterte intensjon:

Frå `bronze.yaml`:
- `schema_has_license`
- `class_names_pascal_case`
- `slot_names_snake_case`
- `all_classes_have_identifier`
- `class_count_limit`
- `all_classes_have_concept_ref`
- `controlled_vocabulary_annotations`

Frå `silver.yaml`:
- `schema_has_annotation_utgiver`
- `schema_has_annotation_endringsdato`
- `schema_has_annotation_oppdateringsfrekvens`
- `schema_has_annotation_status`
- `distribusjon_lisens`
- `container_distribusjon`
- `container_datatjeneste`
- `container_kvalitetsdimensjon`
- `container_kvalitetsmerknad`

**Avklart løysing (brukarval):** Oppgrader alle desse 16 nøklane til
`severity: error` i `gold.yaml`, slik at faktisk oppførsel samsvarer med
den dokumenterte intensjonen "alle brot gir feil".

## Relevante filer

- `src/mcp-linkml-validator/policies/gold.yaml` — policyen som skal utvidast
- `src/mcp-linkml-validator/policies/bronze.yaml` — kjelde til 7 av nøklane
- `src/mcp-linkml-validator/policies/silver.yaml` — kjelde til 9 av nøklane
- `src/mcp-linkml-validator/server.py` — `_merge_policies()` (referanse, ikkje endra)
- `src/mcp-linkml-validator/policies/README.md` — sjekkliste-dokumentasjon per nivå

## Steg

### 1. Legg til dei 7 bronze-nøklane i gold.yaml sin `checks:`-blokk med `severity: error`

Behald `description`, `check`, `digdir_rule` og andre parametrar identisk med
bronze.yaml (kun `severity` endra), slik konvensjonen er for dei to allereie
oppgraderte nøklane (`all_classes_have_class_uri`, `all_slots_have_slot_uri`).

### 2. Legg til dei 9 silver-nøklane i gold.yaml sin `checks:`-blokk med `severity: error`

Same metode — kopier heile sjekk-definisjonen frå silver.yaml, endre berre
`severity: warning` → `severity: error`.

### 3. Oppdater `src/mcp-linkml-validator/policies/README.md`

Sjekk om README dokumenterer severity per nivå (bronze=warning, gold=error) og
oppdater sjekklista dersom han listar desse 16 sjekkane som "warning på gull".

### 4. Valider mot referansemodell-goldschema.yaml

```bash
make mcp-linkml-valider-modell SCHEMA=<sti-til-referansemodell-goldschema.yaml> POLICY=gold
```

Stadfest at alle 16 tidlegare warning-funn no rapporterer `severity: error`
(dersom skjemaet framleis manglar dei aktuelle felta/annotasjonane).

### 5. Kjør eksisterande testsuite for validatoren

```bash
# Identifiser og køyr relevante testar for mcp-linkml-validator
find tests -iname "*validat*"
```

## Handlingsliste

- [x] Legg til 7 bronze-nøklar i gold.yaml med severity: error
- [x] Legg til 9 silver-nøklar i gold.yaml med severity: error
- [x] Oppdater policies/README.md — la til manglande rader for dei 9 silver-nøklane
- [x] Valider mot referansemodell-gold-schema.yaml
- [x] Køyr testsuite for validatoren

## Utført

**Endringar:**
- `policies/gold.yaml`: 16 nøklar (`schema_has_license`, `class_names_pascal_case`,
  `slot_names_snake_case`, `all_classes_have_identifier`, `class_count_limit`,
  `all_classes_have_concept_ref`, `controlled_vocabulary_annotations`,
  `schema_has_annotation_utgiver/endringsdato/oppdateringsfrekvens/status`,
  `distribusjon_lisens`, `container_distribusjon/datatjeneste/kvalitetsdimensjon/kvalitetsmerknad`)
  lagt til med `severity: error`, elles identisk kopi av bronze/silver-definisjonane.
  Merga gold-policy har no 47 sjekkar, alle `error` — verifisert programmatisk.
- `policies/README.md`: la til 9 tabellrader i gull-seksjonen for dei silver-nøklane
  som no er oppgraderte (var udokumenterte i gull-tabellen frå før).
- `tests/test_mcp_policies.py`: `_GOLD_PASS`-fixturen i `TestGold` var ikkje reelt
  gull-kompatibel (mangla `schema.license`, dei fire `schema.annotations.*`-felta,
  korrekt `begrepsidentifikator`-URI-format og fire container-attributt). Oppdatert
  fixturen slik at `test_gyldig_skjema_har_ingen_feil` faktisk testar eit gyldig
  gull-skjema.

**Validering mot referansemodell-gold-schema.yaml:**
```
make mcp-linkml-valider-modell SCHEMA=src/linkml/referanse/referansemodell-gold/referansemodell-gold-schema.yaml POLICY=gold
```
Alle 6 funn (inkl. `schema.license` og `Distribusjon` manglar `dct:license`) rapporterer
no `"severity": "error"`, `"warningCount": 0` — stadfesta av brukaren sitt opphavlege
avvik.

**Testsuite:** `make mcp-linkml-valider-modell-test` — 28 testar, 11 feilar (var 12 før
denne endringa). Éin test vart løyst av denne endringa (`TestGold.test_gyldig_skjema_har_ingen_feil`,
via fixture-oppdateringa). Dei attverande 11 feila er stadfesta **føreeksisterande** og
**usamanhengande** med denne endringa (verifisert ved å køyre testsuiten mot original
`gold.yaml` via `git show HEAD:...` før noka endring vart gjort):
- `TestBronze` (2 feil): `bronze.yaml` vart ikkje endra i det heile — feila kjem frå
  eit fixture-avvik i `all_classes_have_concept_ref`-mønsteret og ein eksisterande
  `errorCount != 0`-fixture.
- `TestGold` (8 feil): `_fair_code()` i `server.py` les feltet `principle`, men
  bronze.yaml sine sjekkar (t.d. `all_classes_have_class_uri`) set feltet
  `fair_principle` — eit namneavvik som gjer at kodane `fair_f1`/`fair_f3`/`fair_i1`
  aldri vert generert. I tillegg venta fleire testar `severity: warning` for sjekkar
  (`f2_title`, `f4_version`, `i2_standard_prefixes`, `r11_license`, `r12_provenance`)
  som **allereie var `severity: error`** i gold.yaml før denne økta — ikkje noko eg endra.
- `TestSilver` (1 feil): `silver.yaml` vart ikkje endra i det heile.

Desse 11 er reelle, men eksisterande, avvik i testsuiten som ligg utanfor omfanget til
denne specen. Anbefaler eiga spec for å rette `_fair_code()`-namneavviket og dei to
andre fixture-feila.

## Utkast til commit-melding

```
fix(mcp-linkml-validator): oppgrader alle bronze/silver-warnings til error i gold-policy
  - policies/gold.yaml: legg til 16 nøklar (schema_has_license, distribusjon_lisens,
    schema_has_annotation_*, container_*, m.fl.) med severity: error
  - policies/README.md: dokumenter dei 9 nyleg oppgraderte silver-nøklane i gull-tabellen
  - tests/test_mcp_policies.py: oppdater _GOLD_PASS-fixture til å vere reelt gull-kompatibel
  - specs/done/gold-policy-oppgrader-alle-warnings.md: dokumenter avvik og løysing
```
