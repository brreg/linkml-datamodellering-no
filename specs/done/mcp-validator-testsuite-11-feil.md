# mcp-linkml-validator: 11 føreeksisterande testfeil i test_mcp_policies.py

## Bakgrunn

Under arbeidet med `specs/done/gold-policy-oppgrader-alle-warnings.md` vart det
oppdaga at `make mcp-linkml-valider-modell-test` hadde **12 feilande testar før**
noka endring vart gjort i den økta. Éin vart løyst som eit biprodukt (fixture-fiks
i `TestGold.test_gyldig_skjema_har_ingen_feil`). Dei attverande **11** er stadfesta
**usamanhengande** med gold-policy-arbeidet (stadfesta ved å køyre testsuiten mot
den opphavlege `gold.yaml`, henta via `git show HEAD:...`, før noka endring —
same 11 feil var til stades då òg for TestBronze/TestGold/TestSilver-delane som
ikkje var rørte).

Denne specen dokumenterer fire uavhengige rotårsaker som til saman forklarer alle
11 feila.

## Relevante filer

- `src/mcp-linkml-validator/server.py` — `_fair_code()` (linje 98-100),
  sjekk-implementasjonane som brukar han, `_check_all_classes_have_concept_ref` (linje 272-291)
- `src/mcp-linkml-validator/policies/bronze.yaml` — `schema_id_is_http_uri`,
  `all_classes_have_class_uri`, `all_slots_have_slot_uri`, `all_classes_have_concept_ref`
- `src/mcp-linkml-validator/policies/gold.yaml` — `fair_checks:`-blokk (f2_title,
  f4_version, i2_standard_prefixes, r11_license, r12_provenance)
- `tests/test_mcp_policies.py` — `_BRONZE_PASS`, `_SILVER_PASS`-fixturane (linje 36-53,
  55-131), `TestGold`-testane for FAIR-sjekkar (linje ~570-745),
  `test_begrepsidentifikator_annotation_godtatt` (linje ~389)

## Rotårsaker

### Bug A — `_fair_code()` les feltnamnet `principle`, men bronze.yaml sine sjekkar set `fair_principle`

**Feil (3 testar):** `test_fair_f1_schema_id_ikkje_http_gir_feil`,
`test_fair_f3_klasse_utan_class_uri_gir_advarsel`, `test_fair_i1_slot_utan_slot_uri_gir_advarsel`

`server.py:_fair_code()`:
```python
def _fair_code(config: dict) -> str:
    p = config.get("principle")
    return ("fair_" + p.lower().replace(".", "")) if p else config.get("check", "check")
```

Sjekkane `schema_id_is_http_uri`, `all_classes_have_class_uri` og
`all_slots_have_slot_uri` i `bronze.yaml` set metadatafeltet **`fair_principle`**
(t.d. `fair_principle: F1`), ikkje `principle`. `_fair_code()` finn dermed ikkje
feltet, fell tilbake til `check`-typenamnet, og genererer kodar som
`schema_id_is_http_uri` i staden for `fair_f1`. Testane søker etter kode `fair_f1`
og finn han aldri — uavhengig av severity.

**Moglege løysingar:**
1. Endre `_fair_code()` til å også lese `fair_principle` som fallback
2. Endre feltnamnet i bronze.yaml frå `fair_principle` til `principle` for desse tre
   sjekkane (kan påverke anna kode/dokumentasjon som les `fair_principle`)
3. Endre testane til å søke etter dei faktiske kodane (`schema_id_is_http_uri`,
   `all_classes_have_class_uri`, `all_slots_have_slot_uri`) i staden for `fair_f1`/`fair_f3`/`fair_i1`

**Avgjort:** Alternativ 3 — endre testane, ikkje produksjonskoden. `_fair_code()`
og `fair_principle`-feltet i bronze.yaml rører produksjonsåtferd (faktiske
issue-kodar rapporterte til brukarar av validatoren); testane sin bruk av
`fair_f1`/`fair_f3`/`fair_i1` var berre ei feilaktig forventing om kva kode desse
tre bronze-sjekkane skulle generere. Retting: bruk `has_error`/`has_warning` med
dei faktiske kodane (`schema_id_is_http_uri`, `all_classes_have_class_uri`,
`all_slots_have_slot_uri`) i dei tre testane.

### Bug B — Testar forventar `severity: warning` for FAIR-sjekkar som har vore `error` sidan før denne økta

**Feil (5 testar):** `test_fair_f2_schema_utan_title_gir_advarsel`,
`test_fair_f4_schema_utan_version_gir_advarsel`, `test_fair_i2_utan_standard_prefiks_gir_advarsel`,
`test_fair_r11_utan_lisensslot_gir_advarsel`, `test_fair_r12_utan_provenienssslot_gir_advarsel`

I motsetnad til Bug A genererer desse fem sjekkane (`f2_title`, `f4_version`,
`i2_standard_prefixes`, `r11_license`, `r12_provenance` — alle definerte i
`gold.yaml` sin eigen `fair_checks:`-blokk med korrekt `principle:`-felt) dei
forventa kodane (`fair_f2`, `fair_f4`, osb.) korrekt. Men `gold.yaml` sin
description (linje 8) seier eksplisitt "Alle brot gir feil", og alle fem har
`severity: error` — **dette var slik allereie før gold-policy-arbeidet i denne
økta**, stadfesta ved samanlikning mot `git show HEAD:...gold.yaml` frå før
endringane. Testane sitt namn (`..._gir_advarsel`) og assertions
(`self.assertTrue(has_warning(...))`) samsvarer ikkje med den faktiske,
dokumenterte, intenderte oppførselen.

**Løysing:** Oppdater testane til å bruke `has_error` i staden for `has_warning`,
og vurder å endre testnamn frå `..._gir_advarsel` til `..._gir_feil` for å
reflektere gold-policyen sin faktiske semantikk.

### Bug C — `_BRONZE_PASS`/`_SILVER_PASS`-fixturane er ikkje reelt gyldige

**Feil (2 testar):** `test_gyldig_skjema_har_ingen_feil` (TestBronze, TestSilver)

Begge fixturane har to reelle feil:
1. Manglar `title:` på skjemanivå — `title` er eit obligatorisk bronze-felt
   (`required.schema: [id, name, title]`), gir `missing_required_metadata`
2. `default_prefix: ex` er eit prefiksnamn, ikkje ein absolutt HTTPS-URI —
   `default_prefix_is_https_uri`-sjekken (severity: error i bronze) krev at
   `default_prefix` **sjølv** er URI-en (jf. `CLAUDE.md` sin konvensjonstabell:
   "default_prefix | Absolutt HTTPS-URL med avsluttande '/'")

Same to problem gjorde at `TestGold._GOLD_PASS` òg feila før han vart retta i
`gold-policy-oppgrader-alle-warnings.md` (der vart `default_prefix` retta til
`https://example.org/` og `title` var allereie til stades).

**Løysing:** Legg til `title:` og rett `default_prefix:` til ein absolutt
HTTPS-URI i begge fixturane, tilsvarande fiksen som alt er gjort for `_GOLD_PASS`.

### Bug D — `all_classes_have_concept_ref` sin kommentar lovar eit alias som aldri vert godteke

**Feil (1 test):** `test_begrepsidentifikator_annotation_godtatt`

`server.py:_check_all_classes_have_concept_ref` (linje 272-291):
```python
# Primærformat + bakoverkompatibelt format (data.norge.no/concepts/ er eit alias som framleis er i bruk)
accepted_prefixes = [catalog_uri.rstrip("/") + "/"]
for extra in config.get("concept_catalog_uri_also_accept", []):
    accepted_prefixes.append(extra.rstrip("/") + "/")
```

Kommentaren seier `https://data.norge.no/concepts/` er eit godteke alias, men
`concept_catalog_uri_also_accept` er **aldri sett** i `bronze.yaml` sin
`all_classes_have_concept_ref`-sjekk — så aliaset vert i praksis aldri godteke.
Testfixturen brukar nettopp dette aliaset
(`begrepsidentifikator: https://data.norge.no/concepts/2`) og feilar difor.

**Motstridande med CLAUDE.md:** `CLAUDE.md` § "annotations.begrepsidentifikator"
seier eksplisitt at `https://data.norge.no/concepts/<UUID>` er eit **anna felt**
sitt format (`see_also:`), ikkje eit gyldig alias for `begrepsidentifikator`.
Dette tyder at kommentaren i koden — ikkje testen — sannsynlegvis er den som er
feil.

**Moglege løysingar:**
1. Fjern det lovande kommentaren og legg `concept_catalog_uri_also_accept` til
   `bronze.yaml` slik at aliaset faktisk vert godteke (strir mot CLAUDE.md)
2. Fjern det ubrukte aliashandteringa i koden, og rett testfixturen til å bruke
   det primære `concept-catalog.fellesdatakatalog.digdir.no`-formatet (i tråd
   med CLAUDE.md)

**Avgjort:** Alternativ 2 — CLAUDE.md er normativ kjelde for URI-format på
`begrepsidentifikator`, og seier eksplisitt at `data.norge.no/concepts/` berre
er gyldig for `see_also`. Retting: fjern det lovande, aldri-verksame
alias-kommentaren og `concept_catalog_uri_also_accept`-handteringa i
`_check_all_classes_have_concept_ref`, og oppdater testfixturen i
`test_begrepsidentifikator_annotation_godtatt` til å bruke det primære
`https://concept-catalog.fellesdatakatalog.digdir.no/collections/...`-formatet.

## Steg

### 1. Rett Bug A — endre testane til å søke etter dei faktiske kodane

I `tests/test_mcp_policies.py`:
- `test_fair_f1_schema_id_ikkje_http_gir_feil`: `has_error(..., "fair_f1")` →
  `has_error(..., "schema_id_is_http_uri")` (severity var alt korrekt `error`)
- `test_fair_f3_klasse_utan_class_uri_gir_advarsel`: kodefiks avdekte eit **ekstra
  avvik** — `all_classes_have_class_uri` har vore `severity: error` i `gold.yaml`
  sin eigen `checks:`-blokk sidan før denne økta (ein av dei to opphavleg
  oppgraderte sjekkane). Testen forventa feilaktig `has_warning`. Retting:
  `has_warning(..., "fair_f3")` → `has_error(..., "all_classes_have_class_uri")`,
  testnamn omdøypt til `test_fair_f3_klasse_utan_class_uri_gir_feil`
- `test_fair_i1_slot_utan_slot_uri_gir_advarsel`: same avvik som f3 —
  `all_slots_have_slot_uri` er òg `severity: error` i gold.yaml frå før. Retting:
  `has_warning(..., "fair_i1")` → `has_error(..., "all_slots_have_slot_uri")`,
  testnamn omdøypt til `test_fair_i1_slot_utan_slot_uri_gir_feil`

### 2. Rett Bug D — fjern aliashandteringa i koden, oppdater testfixture

I `src/mcp-linkml-validator/server.py::_check_all_classes_have_concept_ref`:
fjern kommentaren om `data.norge.no/concepts/`-alias og
`concept_catalog_uri_also_accept`-løkka (aldri konfigurert i nokon policy).

I `tests/test_mcp_policies.py::test_begrepsidentifikator_annotation_godtatt`:
endre `begrepsidentifikator: https://data.norge.no/concepts/2` til
`https://concept-catalog.fellesdatakatalog.digdir.no/collections/1/concepts/2`.

### 3. Køyr full testsuite og stadfest 0 feil

```bash
make mcp-linkml-valider-modell-test
```

## Handlingsliste

- [x] Avgjer løysing for Bug A → alternativ 3
- [x] Avgjer løysing for Bug D → alternativ 2
- [x] Rett Bug A (endre testkodar til `schema_id_is_http_uri`, `all_classes_have_class_uri`,
      `all_slots_have_slot_uri`; retta òg severity-forventing for f3/i1, sjå Utført)
- [x] Rett Bug B (testforventingar `has_warning` → `has_error` for f2/f4/i2/r11/r12,
      testnamn omdøypt `..._gir_advarsel` → `..._gir_feil`)
- [x] Rett Bug C (`title:` og `default_prefix:` i `_BRONZE_PASS`/`_SILVER_PASS`)
- [x] Rett Bug D (fjern aliashandtering i `server.py`, rett testfixture til primærformat)
- [x] Køyr `make mcp-linkml-valider-modell-test` og stadfest 0 feil av 28 testar

## Utført

Alle 4 bugar retta. Testsuiten gjekk frå **11 → 0** feilande testar
(`Ran 28 tests ... OK`).

**Bug A:**
- `tests/test_mcp_policies.py::test_fair_f1_schema_id_ikkje_http_gir_feil`:
  `has_error(..., "fair_f1")` → `has_error(..., "schema_id_is_http_uri")`
- `tests/test_mcp_policies.py::test_fair_f3_klasse_utan_class_uri_gir_feil`
  (omdøypt frå `..._gir_advarsel`): `has_warning(..., "fair_f3")` →
  `has_error(..., "all_classes_have_class_uri")` — verifisering under
  implementering avdekte at severity-forventinga òg var feil, ikkje berre koden
  (`all_classes_have_class_uri` har vore `severity: error` i `gold.yaml` sin
  eigen `checks:`-blokk sidan før denne økta)
- `tests/test_mcp_policies.py::test_fair_i1_slot_utan_slot_uri_gir_feil`
  (omdøypt frå `..._gir_advarsel`): same funn — `has_warning(..., "fair_i1")` →
  `has_error(..., "all_slots_have_slot_uri")`

**Bug B:**
- `tests/test_mcp_policies.py`: `has_warning` → `has_error` for `fair_f2`, `fair_f4`,
  `fair_i2`, `fair_r11`, `fair_r12`
- Testnamn omdøypte: `test_fair_f2_schema_utan_title_gir_advarsel` →
  `test_fair_f2_schema_utan_title_gir_feil` (tilsvarande for f4, i2, r11, r12)

**Bug C:**
- `tests/test_mcp_policies.py`: la til `title: Testtittel` (`_BRONZE_PASS`) og
  `title: Sølv-testkatalog` (`_SILVER_PASS`), retta `default_prefix: ex` →
  `default_prefix: https://example.org/` i begge fixturane

**Bug D:**
- `src/mcp-linkml-validator/server.py::_check_all_classes_have_concept_ref`:
  fjerna det aldri-verksame `concept_catalog_uri_also_accept`-fallback-et og
  kommentaren som lova `data.norge.no/concepts/`-alias
- `tests/test_mcp_policies.py::test_begrepsidentifikator_annotation_godtatt`:
  `begrepsidentifikator` retta frå `https://data.norge.no/concepts/2` til
  `https://concept-catalog.fellesdatakatalog.digdir.no/collections/1/concepts/2`

**Verifisering:**
```
make mcp-linkml-valider-modell-test
# Ran 28 tests in 9.906s
# OK
```

## Utkast til commit-melding

```
test(mcp-linkml-validator): rett 11 føreeksisterande testfeil i test_mcp_policies.py
  - server.py: fjern aldri-verksam data.norge.no/concepts/-aliashandtering i
    all_classes_have_concept_ref (strid mot CLAUDE.md sin begrepsidentifikator-konvensjon)
  - tests/test_mcp_policies.py: bruk faktiske issue-kodar (schema_id_is_http_uri,
    all_classes_have_class_uri, all_slots_have_slot_uri) i staden for aldri-genererte
    fair_f1/f3/i1-kodar
  - tests/test_mcp_policies.py: has_warning → has_error for fair_f2/f3/f4/i1/i2/r11/r12
    (gold-policy har vore severity:error for desse sidan før denne økta)
  - tests/test_mcp_policies.py: omdøyp test_fair_*_gir_advarsel → test_fair_*_gir_feil
  - tests/test_mcp_policies.py: legg til title: og rett default_prefix: til absolutt
    HTTPS-URI i _BRONZE_PASS og _SILVER_PASS
  - tests/test_mcp_policies.py: rett begrepsidentifikator-format i
    test_begrepsidentifikator_annotation_godtatt til primærformatet
  - specs/done/mcp-validator-testsuite-11-feil.md: 28/28 testar grøne
```
