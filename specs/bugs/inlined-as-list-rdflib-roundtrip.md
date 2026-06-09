# Bug: `rdflib_loader` feiler på `inlined_as_list` med `identifier: true`

**ID:** BUG-2
**Status:** `upstream`
**Komponent:** `linkml-runtime`
**Oppdaga:** 2026-06-09

## Symptom

`TypeError` ved TTL→YAML for containerklassar der range-klassen har
`identifier: true` og container-attributten er `inlined_as_list: true`:

```
TypeError: OffisiellAdresse.__init__() got an unexpected keyword argument 'har_adressekode'
```

Feilen oppstår fordi `rdflib_loader` prøver å instansiere `OffisiellAdresse`
med feil sett av argument-namn.

I tillegg har `linkml-convert` ein relatert bug der `{id: curie}`-dicts med berre
`id`-feltet (stub-objekt) vert feilaktig prosessert: `JsonObj` vert sendt som
id-verdi i staden for ein streng. Dette berører `test_convert_rdf`.

Begge feila er spegla i `linkml-runtime/linkml_runtime/utils/yamlutils.py` i
`_normalize_inlined` / `_normalize_inlined_as_list`.

## Berørte skjema / testar

| Skjema | Skip i |
|---|---|
| `ngr-adresse` | `test_roundtrip_ttl`, `test_convert_rdf` |
| `ngr-eiendom` | `test_roundtrip_ttl`, `test_convert_rdf` |
| `ngr-virksomhet` | `test_roundtrip_ttl`, `test_convert_rdf` |

## Rot-årsak

NGR-containerklassane (`AdresseContainer`, `EiendomContainer` osv.) brukar
`inlined_as_list: true` i kombinsjon med range-klasser som har `identifier: true`:

```yaml
AdresseContainer:
  tree_root: true
  attributes:
    offisielle_adresser:
      range: OffisiellAdresse   # OffisiellAdresse har identifier: true
      multivalued: true
      inlined: true
      inlined_as_list: true
```

`rdflib_loader` handterer ikkje dette kombinasjonstilfellet korrekt — den prøver
å konstruere range-objektet med feil argument-mapping når objektet er
identifisert med `identifier: true`.

## Workaround

Skip i `test_roundtrip_ttl` og `test_convert_rdf` med kommentar som peikar til
denne fila:

```bash
# linkml-runtime-bug: id-only inlined_as_list-objekt
# Sjå specs/bugs/inlined-as-list-rdflib-roundtrip.md
if [[ "$name" == "ngr-adresse" || "$name" == "ngr-eiendom" || \
      "$name" == "ngr-virksomhet" ]]; then
    echo "Hoppar over roundtrip-ttl for $name (BUG-2: linkml-runtime inlined_as_list-bug)"
    return 0
fi
```

## Løysing

To alternativ:

**Alternativ A — endre container-design (intern fix, ingen upstream-avhengnad):**
Fjern `inlined: true` og `inlined_as_list: true` frå container-attributtane.
Container vil då innehalde URI-referansar i staden for inline-objekt.
Dette er ein semantisk endring i serialiseringsformatet — sjå
`specs/backlog/fix-roundtrip-ngr-inlined-as-list.md` for detaljert analyse.

**Alternativ B — vent på upstream-fix:**
Upstream fix i `linkml-runtime` der `rdflib_loader` korrekt handterer
`inlined_as_list`-objekt med `identifier: true`.

Når anten A eller B er på plass:
1. Fjern skip-betingelsane frå `test_make.sh`.
2. Verifiser at `make test` passerer for alle tre NGR-skjema.
3. Oppdater denne fila til `Status: løyst` (eller `workaround` for Alternativ A).
