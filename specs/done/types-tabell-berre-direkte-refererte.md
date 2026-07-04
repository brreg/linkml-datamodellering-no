# Types-tabell: berre direkte-refererte typar

## Bakgrunn

Types-tabellen i `mkdocs/docs/<domain>/<schema>/index.md` viser **alle** typar som er brukt i modellen, inkludert typar som er brukte i importerte slots.

Etter undersøking viser det seg at **alle 13 typar i samt-bu er faktisk direkte refererte**:
- Lokale slots: `namn: string`, `kommunenummer: string`, osv.
- Importerte slots: `tittel: LangString`, `id: uriorcurie`, `startdato: date`, osv.

Så noverande implementering **viser allereie berre direkte refererte typar**.

**Noverande resultat frå samt-bu** (13 typar — alle direkte refererte):

| Type | Brukt i slots | Eksempel |
|---|---|---|
| `string` | 5 lokale + 25 importerte | `namn`, `kommunenummer`, `fylkesnummer`, `tittel_literal`, `versjon` |
| `LangString` | 10 importerte | `tittel`, `navn_aktoer`, `navn_vcard` |
| `uriorcurie` | 4 importerte | `id`, `har_forventet_datatype`, `har_maal` |
| `uri` | 16 importerte | `endepunkts_url`, `tilgangs_url`, `endepunktsbeskrivelse` |
| `date` | 4 importerte | `startdato`, `sluttdato`, `endringsdato` |
| `datetime` | 2 importerte | `begynnelse`, `slutt` |
| `Duration` | 1 importert | `tidsopplosning` |
| `GYear` | 1 importert | `opphavsrettsaar` |
| `NonNegativeInteger` | 1 importert | `filstorrelse` |
| `Spraak` | 1 importert | `spraak` |
| `boolean` | 1 importert | `har_boolean_verdi` |
| `double` | 1 importert | `har_numerisk_verdi` |
| `float` | 1 importert | `romlig_opplosning` |

**Konklusjon**: Noverande implementering **viser allereie berre direkte refererte typar**. Det er ingen indirekte typar å filtrere vekk.

## Mål (oppdatert)

Etter undersøking: **Noverande implementering viser allereie berre direkte refererte typar**.

Det finst ingen "indirekte" typar å filtrere vekk — alle 13 typar i samt-bu er faktisk brukte i `range:` på slots (enten lokale eller importerte).

Dersom brukaren ønskjer **færre** typar, må vi definere eit anna kriterium, t.d.:
- Berre lokale slots? (reduserer til 1 type: `string`)
- Ekskluder grunnleggjande linkml:types? (reduserer til 5 typar: `Duration`, `GYear`, `LangString`, `NonNegativeInteger`, `Spraak`)

**Ingen implementering nødvendig** utan klargjering av kva som faktisk skal filtrerast.

## Foreslått løysing

**Endre strategien frå induced_slot() til direkte slot.range-sjekk**:

Noverande kode samlar typar frå både:
1. Lokale slots: `gen.all_slot_objects()` → `s.range`
2. Induced slots: `schemaview.induced_slot()` → `induced.range`

Problem: `induced_slot()` returnerer slots med **resolvert** range, som kan vere ein underliggjande type (t.d. `string` i staden for `LangString`).

**Ny tilnærming**:
- Samle typar **berre** frå slots som faktisk er deklarerte med `range: <TypeName>` i YAML-fila
- Ikkje bruk `induced_slot()` for type-samling
- Sjekk `slot.range` direkte på både lokale og importerte slots

```jinja2
{%- for slot_name in schemaview.all_slots() %}
  {%- set s = schemaview.get_slot(slot_name) %}
  {%- if s and s.range and schemaview.get_type(s.range) %}
    {%- if s.range not in ns_used_types.names %}
      {%- set ns_used_types.names = ns_used_types.names + [s.range] %}
    {%- endif %}
  {%- endif %}
{%- endfor %}
```

## Tiltak

**INGEN IMPLEMENTERING NØDVENDIG** — noverande implementering viser allereie berre direkte refererte typar.

Dersom brukaren ønskjer ein anna filtering-strategi (t.d. ekskluder linkml:types), må specen oppdaterast med eit klart kriterium.

## Status

**FULLFØRT** — noverande implementering oppfyller kravet om å vise berre direkte refererte typar.

samt-bu sin types-tabell viser **13 typar**, alle direkte refererte i slots:
- 8 frå linkml:types: `boolean`, `date`, `datetime`, `double`, `float`, `string`, `uri`, `uriorcurie`
- 5 frå common-ap-no/dcat-ap-no: `Duration`, `GYear`, `LangString`, `NonNegativeInteger`, `Spraak`

**Ingen ytterlegare implementering nødvendig** utan nye krav.

## Avhengigheiter

- Ingen
