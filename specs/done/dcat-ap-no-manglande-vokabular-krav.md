# Spec: fiks vokabular_krav-warningar i dcat-ap-no-schema.yaml

## Bakgrunn

`make mcp-linkml-valider-modell SCHEMA=src/linkml/oreg/blomsterregisteret/blomsterregisteret-schema.yaml POLICY=bronze`
gir 5 warningar (0 errors). Ingen av dei stammar frå
`blomsterregisteret-schema.yaml` sjølv — modellen definerer ingen slots
lokalt utover `kontaktpunkt`. Alle 5 kjem frå det importerte
`dcat-ap-no-schema.yaml` (importert via versjonslåst URL til tag
`dcat-ap-no-v2.13.0`), som bronse-sjekken `slots_gyldige_verdier_krev_vokabular_krav`
(sjå `CONVENTIONS.md § Kontrollerte vokabular — annotation-konvensjon`) fangar
opp fordi `SchemaView` slår saman heile importkjeda ved validering.

Sjekken krev at eit slot med `annotations.gyldige_verdier` òg har
`annotations.vokabular_krav` (`skal`|`bør`|`kan`), og at `description`
inneheld ei tydeleg **SKAL**/**BØR**/**KAN**-formulering som matchar
`vokabular_krav`-verdien (sjå `server.py:472-503`).

Konkrete funn i `src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml`:

| Slot | Linje | Problem |
|---|---|---|
| `tema` | 1059-1069 | Har `vokabular_krav: skal`, men `description` inneheld berre small `skal`, ikkje `SKAL` |
| `policy` | 1156-1161 | Har `gyldige_verdier: odrl:Policy`, manglar `vokabular_krav` heilt |
| `eierskapshistorikk` | 1162-1171 | Har `gyldige_verdier: dct:ProvenanceStatement`, manglar `vokabular_krav` |
| `ble_generert_ved` | 1172-1179 | Har `gyldige_verdier: URI til prov:Activity`, manglar `vokabular_krav` |
| `annen_ansvarlig_aktor` | 1180-1186 | Har `gyldige_verdier: prov:Attribution`, manglar `vokabular_krav` |

## Omfang og konsekvens

`dcat-ap-no-schema.yaml` er ein delt AP-NO-profil som **alle** DCAT-baserte
domenemodellar importerer (direkte eller transitivt). Endringa rettar altså
warningane for alle slike modellar, ikkje berre blomsterregisteret.

**Viktig avgrensing:** Domenemodellar som importerer `dcat-ap-no-schema` via
**versjonslåst URL** (t.d. blomsterregisteret sin
`.../dcat-ap-no-v2.13.0/...`-import) vil **ikkje** sjå fiksen før:

1. Denne endringa er merga til `main`,
2. `release-please` cuttar ein ny `dcat-ap-no-vX.Y.Z`-tag (utløyst automatisk
   av `fix(dcat-ap-no): ...`-scope i commit-meldinga),
3. Den importerande modellen sin pinna URL vert oppdatert til å peike på den
   nye taggen.

Steg 2 og 3 skjer utanfor denne specen (CI-automatikk + separat
oppfølgingsendring per modell). Denne specen dekker berre steg 1: fiksen i
`dcat-ap-no-schema.yaml` sjølv, verifisert ved direkte validering av
`dcat-ap-no-schema.yaml` (ikkje via blomsterregisteret sin pinna import).

## Valde vokabular_krav-nivå

Ingen av dei fire manglande annotasjonane har ei formell spesifikasjon å
lene seg på (dei er ikkje del av DCAT-AP sitt kontrollerte-vokabular-regime
på same måte som `tema`/`frekvens`/`tilgangsrettigheter`, som viser til EU
sine autoritetstabellar) — nivåa er difor vurdert per felt:

| Slot | Nivå | Grunngjeving |
|---|---|---|
| `policy` | `kan` | Strukturert ODRL-policy er eit valfritt alternativ/tillegg til fritekst i `dct:rights`, ikkje eit krav |
| `eierskapshistorikk` | `bør` | Digdir sin veileder «Orden i eget hus», steg 5 — beskrive, tilrår (ikkje krev) dokumentasjon av opphav/eigarskapshistorikk |
| `ble_generert_ved` | `kan` | Valfri tilleggskontekst om genereringsaktivitet, ikkje eit krav |
| `annen_ansvarlig_aktor` | `kan` | Valfri tilleggsattributering utover primær utgivar/skapar |

## Steg

1. **`tema`** (linje 1063): kapitaliser `skal` → `SKAL` i eksisterande
   setning («For norske offentlege datasett SKAL Los ... brukast som
   primærvokabular»). Ingen annan endring.

2. **`policy`** (linje 1156-1161): legg til `annotations.vokabular_krav: kan`
   og utvid `description` med ei KAN-formulering:
   > ODRL-policy som regulerer bruk av ressursen. Verdien KAN nyttast som eit
   > strukturert alternativ til fritekst i dct:rights.

3. **`eierskapshistorikk`** (linje 1162-1171): legg til
   `annotations.vokabular_krav: bør` og kapitaliser eksisterande `Kan` →
   `BØR` i setninga («... BØR brukast til å skildre kjeldetype ...»).

4. **`ble_generert_ved`** (linje 1172-1179): legg til
   `annotations.vokabular_krav: kan` og kapitaliser innleiinga til KAN:
   > KAN brukes til å referere til en aktivitet som genererte datasettet,
   > eller som gir forretningskontekst for oppretting av det.

5. **`annen_ansvarlig_aktor`** (linje 1180-1186): legg til
   `annotations.vokabular_krav: kan` og utvid `description`:
   > Kvalifisert attributering til ansvarleg aktør. Slik attributering KAN
   > brukast for å skildre fleire aktørar med ulike roller.

6. Køyr `make lint SCHEMA=src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml`
   for å stadfeste at endringane ikkje bryt eksisterande validering.

7. Køyr
   `make mcp-linkml-valider-modell SCHEMA=src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml POLICY=bronze`
   og stadfest at dei 5 warningane er borte (validerer direkte mot fila på
   `main`, uavhengig av pinna URL-importar andre stader).

8. Køyr `make roundtrip SCHEMA=src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml`
   for rask JSON/TTL-roundtrip-verifisering.

9. **Ikkje** rediger `blomsterregisteret-schema.yaml` sin pinna import-URL i
   denne specen — det krev ein ny publisert `dcat-ap-no`-tag og høyrer heime
   i ei eiga oppfølgingsendring når taggen finst.

## Handlingsliste

- [x] Steg 1: `tema`-beskriving
- [x] Steg 2: `policy` — annotasjon + beskriving
- [x] Steg 3: `eierskapshistorikk` — annotasjon + beskriving
- [x] Steg 4: `ble_generert_ved` — annotasjon + beskriving
- [x] Steg 5: `annen_ansvarlig_aktor` — annotasjon + beskriving
- [x] Steg 6: `make lint` — 6 pre-eksisterande `canonical_prefixes`-warningar (urelatert til denne endringa)
- [x] Steg 7: `make mcp-linkml-valider-modell` (bronze) — dei 5 målwarningane er borte. 17 attverande `all_classes_have_concept_ref`-warningar er venta (AP-NO-profilklassar skal ikkje ha `begrepsidentifikator`, jf. CLAUDE.md)
- [x] Steg 8: `make roundtrip` — roundtrip-json OK, roundtrip-ttl OK
- [x] Commit-melding (`fix(dcat-ap-no): ...`) generert etter fullføring

## Utført

Alle 5 slot-warningar fiksa i `src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml`
ved å leggje til/kapitalisere SKAL/BØR/KAN-formuleringar i `description` og
leggje til manglande `annotations.vokabular_krav`. Verifisert direkte mot
skjemaet (bronse-policy: 0 av dei 5 målwarningane att). Merk: blomsterregisteret
sin pinna import (`dcat-ap-no-v2.13.0`) ser ikkje fiksen før ein ny
`dcat-ap-no`-tag er publisert og importen er oppdatert — dette er eit separat,
seinare steg (sjå «Omfang og konsekvens» over).
