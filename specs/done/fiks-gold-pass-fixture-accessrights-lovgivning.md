# Fiks den feilande testen `TestGold.test_gyldig_skjema_har_ingen_feil`

## Bakgrunn

`make mcp-linkml-valider-modell-test` har éin kjend, pre-eksisterande
testfeil, dokumentert (men ikkje retta) i fleire tidlegare specar i denne
serien (`specs/done/gold-policy-oppgrader-alle-warnings.md`,
`specs/done/utvid-dekningsgrad-regel-5-12-14-15.md`,
`specs/done/full-gjennomgang-policy-alvorsgrad-og-overlapp.md`):

```
FAIL: test_gyldig_skjema_har_ingen_feil (__main__.TestGold.test_gyldig_skjema_har_ingen_feil)
AssertionError: 2 != 0
```

**Rotårsak — stadfesta ved direkte køyring:** `_GOLD_PASS`-testfixturen
(`tests/test_mcp_policies.py`) sin `Datasett`-klasse manglar to slots som
`gold.yaml` krev som `error` (oppgraderte frå `silver.yaml`, sjå
`datasett_tilgangsrettigheter`/`datasett_lovgivning`):

```bash
podman run --rm -v "$(pwd):/work:ro" mcp-linkml-validator python3 -c "
import sys; sys.path.insert(0, '/work/src/mcp-linkml-validator'); sys.path.insert(0, '/work/tests')
from test_mcp_policies import _GOLD_PASS
from server import validate_schema
import json; print(json.dumps(validate_schema(_GOLD_PASS, 'gold'), indent=2, ensure_ascii=False))"
```

gjev:

```json
{
  "errorCount": 2,
  "warningCount": 1,
  "issues": [
    {"severity": "error", "code": "class_missing_required_slot", "target": "class:Datasett",
     "message": "Klasse 'Datasett' manglar slot med dct:accessRights"},
    {"severity": "error", "code": "class_missing_required_slot", "target": "class:Datasett",
     "message": "Klasse 'Datasett' manglar slot med dcatap:applicableLegislation"},
    {"severity": "warning", "code": "missing_recommended_metadata", "target": "class:Container",
     "message": "Manglar anbefalt metadata: description"}
  ]
}
```

Dei to `error`-funna er kvifor testen feilar (testen assertar
`errorCount == 0`). Dei er **reelle, korrekte** funn frå validatoren —
fixturen er rett og slett ikkje eit fullstendig gull-konformt skjema enno,
ikkje ein feil i sjølve valideringslogikken. Dette skal difor **rettast i
testfixturen**, ikkje i `server.py` eller policy-YAML-filene.

Den tredje issuen (`warning` om `Container` sin manglande `description`)
påverkar **ikkje** testutfallet (testen sjekkar berre `errorCount`), men
er verdt å rette samstundes for ein reint gull-konform fixture — sjå
steg 2.

## Målbilete

`_GOLD_PASS` skal validere med `errorCount == 0` (og helst
`warningCount == 0`) mot `gold`-policyen, slik at
`test_gyldig_skjema_har_ingen_feil` faktisk testar eit gyldig gull-skjema
— føremålet testen sitt namn allereie hevdar.

## Steg

1. Legg til dei to manglande slotsa på `Datasett` i `_GOLD_PASS`
   (`tests/test_mcp_policies.py`), med same slot-/URI-namn som resten av
   repoet brukar (`dcat-ap-no-schema.yaml`, sjå `tilgangsrettigheter`/
   `gjeldende_lovgivning`):

   - Legg `tilgangsrettigheter` og `gjeldende_lovgivning` til `Datasett`
     sin `slots:`-liste.
   - Legg til to nye slot-definisjonar i skjemaet sitt globale
     `slots:`-felt:
     ```yaml
     tilgangsrettigheter:
       description: Tilgangsrettar
       slot_uri: dct:accessRights
       range: uriorcurie
     gjeldende_lovgivning:
       description: Gjeldande lovgjeving
       slot_uri: dcatap:applicableLegislation
       range: uriorcurie
     ```
   - Legg til `dcatap: http://data.europa.eu/r5r/`-prefikset i
     `_GOLD_PASS` sin `prefixes:`-blokk (manglar i dag — sjølve
     sjekken samanliknar berre `slot_uri`-strengen, så testen ville
     truleg passert utan prefikset òg, men å deklarere det er korrekt
     praksis og konsistent med korleis reelle skjema gjer det).

2. **Valfritt, lågare prioritet** (påverkar ikkje testutfallet, men gjev
   ein reint `warningCount: 0`-fixture): legg til `description:` på
   `Container`-klassen i `_GOLD_PASS`, sidan `tree_root`-klassen i dag
   **ikkje** er friteken frå det generiske `recommended: class:
   [description]`-kravet (jf. Funn B5.3 i
   `specs/done/full-gjennomgang-policy-alvorsgrad-og-overlapp.md`).

3. Køyr `make mcp-linkml-valider-modell-test` og stadfest at
   `test_gyldig_skjema_har_ingen_feil` (TestGold) no er grøn, og at ingen
   andre testar vart påverka av endringa (fixturen vert delt av fleire
   `TestGold`-testar — sjekk spesielt dei som brukar
   `_GOLD_PASS.replace(...)`, t.d. `test_lokal_type_utan_standard_uri_gir_feil`
   og `test_erdiagram_ikkje_aktivert_gir_feil`, sidan dei bygger vidare på
   denne strengen).

## Handlingsliste

- [x] Steg 1: Legg til `tilgangsrettigheter`/`gjeldende_lovgivning` på
      `Datasett` i `_GOLD_PASS`
- [x] Steg 2 (valfritt): `description` på `Container` i `_GOLD_PASS`
- [x] Steg 3: Testverifisering (full suite, ikkje berre den eine testen)

## Utført

**Dato:** 2026-08-31

Alle tre steg gjennomførte, inkludert det valfrie steg 2.

- **`tests/test_mcp_policies.py` (`_GOLD_PASS`):** lagt til
  `dcatap: http://data.europa.eu/r5r/`-prefikset; `description:` på
  `Container`; `tilgangsrettigheter`/`gjeldende_lovgivning` lagt til
  `Datasett` sin `slots:`-liste, med tilhøyrande nye slot-definisjonar
  (`slot_uri: dct:accessRights` / `dcatap:applicableLegislation`) i det
  globale `slots:`-feltet, same namnekonvensjon som
  `dcat-ap-no-schema.yaml`.
- Redigeringa trefte presist berre `_GOLD_PASS` (stadfesta med
  `grep -n "opphavar:"` — unik streng, ikkje delt med `_SILVER_PASS`).

**Verifisering:**

- Direkte køyring mot `validate_schema(_GOLD_PASS, "gold")`:
  `errorCount: 0, warningCount: 0` (var `errorCount: 2, warningCount: 1`
  før retting).
- `make mcp-linkml-valider-modell-test`: **45/45 testar grøne** — den
  tidlegare kjende, pre-eksisterande feilen
  (`TestGold.test_gyldig_skjema_har_ingen_feil`) er no retta. Ingen andre
  testar (inkl. dei to som byggjer vidare på `_GOLD_PASS` via
  `.replace()`/direkte gjenbruk) vart påverka.
