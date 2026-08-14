# Fjern lokal `subsets:`-blokk frå new-modell-scaffolding (kolliderer med import)

## Bakgrunn

`make new-modell` genererer via `mcp-linkml-modell-utkast` (`converter.py`)
alltid ein lokal `subsets:`-blokk i det nye skjemaet:

```yaml
subsets:
  Obligatorisk:
    description: Obligatoriske eigenskapar.
  Anbefalt:
    description: Anbefalte eigenskapar.
  Valgfri:
    description: Valfrie eigenskapar.
```

Samstundes legg `new-modell.sh` alltid til eit `dcat-ap-no-schema`-import i
det same skjemaet. Alle AP-NO-profilar importerer (transitivt)
`common-ap-no-schema.yaml`, som **allereie** definerer subsets med same namn:

```yaml
# src/linkml/ap-no/common-ap-no/common-ap-no-schema.yaml
subsets:
  Obligatorisk:
    description: Obligatoriske eigenskapar i ein AP-NO-profil.
  Anbefalt:
    description: Anbefalte eigenskapar i ein AP-NO-profil.
  Valgfri:
    description: Valfrie eigenskapar i ein AP-NO-profil.
```

Resultatet er at **kvar einaste modell scaffolda med `make new-modell`
kolliderer med sitt eige import**, sidan namna er identiske men skildringane
avvik.

## Reprodusert

Den ferske, ikkje-committa scaffolden `src/linkml/oreg/lunchregisteret/`
reproduserer feilen direkte:

```
$ make gen-python SCHEMA=src/linkml/oreg/lunchregisteret/lunchregisteret-schema.yaml
[ERROR] python feila for oreg/lunchregisteret (1.14s) —
Conflicting URIs (https://data.norge.no/ap-no/common-ap-no, https://data.norge.no/oreg/lunchregisteret) for item: Obligatorisk
```

Same feil vil ramme alle SchemaLoader-baserte mål (`gen-python`,
`gen-jsonld-context`, `gen-rdf`, `linkml-convert`, `make roundtrip`) for
**alle** nye modellar scaffolda med `make new-modell`, uansett kva AP-NO-profil
som til slutt vert importert (dei deler alle `common-ap-no-schema.yaml`).

## Rotårsak

Dette er same mekanisme som **BUG-6** (`bugs/dqv-standard-class-override.md`,
klassenamn) og **BUG-7** (`bugs/duplicate-slot-merge-konflikt.md`, slotnamn):
LinkML sin `merge_dicts` kastar `ValueError` så snart eit namn finst meir enn
éin stad i importgrafen med ulik `from_schema` — uavhengig av om innhaldet er
identisk. `subsets` er ein tredje variant av same mønster, denne gongen på
subset-namn.

`converter.py` skriv den lokale `subsets:`-blokka ubetinga (linje 304-308),
sjølv om subset-namna alt er tilgjengelege gjennom importet så snart
scaffoldinga legg til eit AP-NO-import. `slot_usage.in_subset`-referansane
(bygde frå `subsets_cfg.required_maps_to` / `non_required_default`, linje
317-318, brukt linje 413/415) treng berre at namna **finst** i importgrafen —
dei treng ikkje at skjemaet definerer dei sjølv.

## Tiltak

| # | Tiltak | Fil |
|---|---|---|
| 1 | Fjern `schema["subsets"] = {...}`-blokka (linje 303-308) frå `convert()` | `src/mcp-linkml-modell-utkast/converter.py` |
| 2 | Behald `subsets_cfg`/`req_subset`/`def_subset`-oppslaget og `in_subset`-bruken uendra — dei refererer framleis gyldige (importerte) subset-namn | `src/mcp-linkml-modell-utkast/converter.py` |
| 3 | Oppdater `test_subsets_er_alltid_med` (linje 333-337) til å verifisere at `subsets`-nøkkelen **ikkje** finst i det genererte skjemaet, sidan namna no kjem frå import | `tests/test_mcp_linkml_generator.py` |
| 4 | Oppdater README-tabellen: rada `subsets \| Obligatorisk, Anbefalt, Valgfri` (linje 54) skal presisere at desse berre vert **referert** via `in_subset`, ikkje definerte lokalt — dei kjem frå det importerte AP-NO-skjemaet | `src/mcp-linkml-modell-utkast/README.md` |
| 5 | Oppdater `bronze.yaml`-skildringa (linje 5, «obligatorisk/anbefalt/valgfri-subsets») om ordlyden impliserer lokal definisjon | `src/mcp-linkml-modell-utkast/profiles/bronze.yaml` |
| 6 | Regenerer/rett `src/linkml/oreg/lunchregisteret/` (ikkje committa scaffold i arbeidstreet) manuelt ved å fjerne `subsets:`-blokka, eller be brukaren køyre `make new-modell` på nytt etter fiksen | `src/linkml/oreg/lunchregisteret/lunchregisteret-schema.yaml` |
| 7 | Verifiser: `make gen-python SCHEMA=src/linkml/oreg/lunchregisteret/lunchregisteret-schema.yaml` passerer utan `Conflicting URIs` | — |
| 8 | Verifiser: `make roundtrip SCHEMA=...` for eit nyscaffolda testskjema | — |

## Referanse

- `bugs/dqv-standard-class-override.md` (BUG-6) — klassenamn-variant
- `bugs/duplicate-slot-merge-konflikt.md` (BUG-7) — slotnamn-variant, inneheld
  den generelle regelen dette tiltaket følgjer: «unngå å redeklarere eit namn
  som allereie finst andre stader i importgrafen til skjemaet — uavhengig av
  om innhaldet er identisk»

## Utført

Alle 8 tiltak gjennomførte:

1. Fjerna `schema["subsets"] = {...}` frå `convert()` i `converter.py`.
2. `subsets_cfg`/`req_subset`/`def_subset`/`in_subset`-logikken uendra —
   verifisert framleis rett gjennom `test_required_property_får_obligatorisk_subset`.
3. `test_subsets_er_alltid_med` bytta ut med
   `test_subsets_vert_ikkje_lokalt_definert`, som assertar at `"subsets"`
   **ikkje** finst i det genererte skjemaet.
4. README-tabellen presiserer no at subsets berre vert referert via
   `in_subset`, ikkje definert lokalt.
5. `bronze.yaml`-skildringa presiserer «referert, ikkje lokalt definert —
   subsetnamna må finnast i importgrafen».
6. Den ikkje-committa `src/linkml/oreg/lunchregisteret/lunchregisteret-schema.yaml`
   fekk `subsets:`-blokka fjerna manuelt.
7. Verifisert: `make gen-python SCHEMA=src/linkml/oreg/lunchregisteret/lunchregisteret-schema.yaml`
   passerer no utan `Conflicting URIs`-feil.
8. `make roundtrip` for same skjema feilar framleis, men på ei **anna,
   allereie eksisterande** feilkjelde (`Unknown CURIE prefix: https` — knytt
   til kommentaren etter dei rå GitHub-URL-importane, ikkje til subsets).
   Stadfesta pre-eksisterande ved at same feiltekst dukka opp i `make lint`
   *før* subsets-fiksen vart gjort. Ute av scope for dette tiltaket — bør
   handterast i eiga spec.

I tillegg køyrde full testpakke for `mcp-linkml-modell-utkast`
(`make mcp-linkml-modell-utkast-test`): 44/44 testar passerer.
