# Fix: NGR inlined_as_list TTL-roundtrip-bug

## Bakgrunn

`test_roundtrip_ttl` hoppar over `ngr-adresse`, `ngr-eiendom` og
`ngr-virksomhet` grunna ein kjend linkml-runtime-bug:

```
TypeError: OffisiellAdresse.__init__() got an unexpected keyword argument 'har_adressekode'
```

## Rot-årsak

NGR-containerklassane (`AdresseContainer`, `EiendomContainer`, osv.) brukar
`inlined_as_list: true` for container-attributtar som peikar til klasser
med `id: identifier: true`:

```yaml
# ngr-adresse-schema.yaml
AdresseContainer:
  tree_root: true
  attributes:
    offisielle_adresser:
      range: OffisiellAdresse
      multivalued: true
      inlined: true
      inlined_as_list: true      # ← kombinert med identifier: true på OffisiellAdresse
```

Når `linkml-convert` les TTL-fila tilbake til YAML, prøver `rdflib_loader`
å konstruere `OffisiellAdresse`-objekt, men TTL-triplane inneheld predikatar
(`har_adressekode`, osv.) som ikkje korresponderer til konstruktøren. Dette
er ein feil i `linkml-runtime`-biblioteket der loader ikkje handterer
`inlined_as_list`-objekt med `identifier: true` korrekt.

## Status for upstream-fix

Dette er eit kjend `linkml-runtime`-bug.

**Avgjerd (2026-08-20, jf. `specs/done/inlining-konvensjon.md` R5):**
containerklassen (`tree_root: true`) sitt bruk av `inlined`/`inlined_as_list`
på attributta sine er ein **ufravikeleg regel** — containerattributt skal
alltid inline sine attributt, uavhengig av om range-klassen har
`identifier: true`. Containerklassen sitt føremål er nettopp å vere eit
sjølvstendig, komplett eksportdokument, og det gjeld også for NGR. **Alternativ A
er difor avvist:** container-attributtane i `ngr-adresse-schema.yaml`,
`ngr-eiendom-schema.yaml` og `ngr-virksomhet-schema.yaml` skal **ikkje**
endrast til URI-lister. **Alternativ B** (vente på ein upstream-fix i
`linkml-runtime`) er den standande, endelege løysinga.

## Alternativ

### Alternativ A: Endre container til URI-lister — AVVIST

```yaml
# Vurdert, men avvist:
offisielle_adresser:
  range: OffisiellAdresse
  multivalued: true
  # inlined: false er default når range har identifier: true
```

Dette vart vurdert fordi det ville løyst BUG-2 direkte, men bryt regelen om
at containerattributt alltid skal inline sine attributt (sjå
`specs/done/inlining-konvensjon.md` R5). Container ville då berre
innehalde URI-referansar, ikkje eit sjølvstendig, komplett eksportdokument —
det motseier heile føremålet med `tree_root`-containerklassen.

### Alternativ B: Vent på upstream-fix i linkml-runtime — VALT LØYSING

Hald skip-betingelsen i `test_roundtrip_ttl`/`test_convert_rdf` inntil
linkml-runtime fiksar `rdflib_loader` for `inlined_as_list`-tilfeller med
`identifier: true`. Tapet av roundtrip-testdekning for `ngr-adresse`,
`ngr-eiendom` og `ngr-virksomhet` er akseptert som ein kjend, permanent
grense i verktøykjeda inntil då.

## Prioritert tiltaksliste

| # | Tiltak | Prioritet | Status |
|---|---|---|---|
| 1 | Overvak linkml-runtime-issue og implementer fix når biblioteket er oppdatert | Lav | Open |
| 2 | Behald skip-betingelsane i `test_roundtrip_ttl`/`test_convert_rdf` og referansen til `bugs/inlined-as-list-rdflib-roundtrip.md` uendra | — | Utført (ingen kodeendring nødvendig — dette var alt gjeldande tilstand) |

## Referanse

Feilen er dokumentert som kjend bug i `tests/test_make.sh`:
```bash
# linkml-runtime-bug: id-only inlined_as_list-objekt
if [[ "$name" == "ngr-adresse" || ... ]]; then
    echo "Hoppar over roundtrip-ttl for $name (linkml-runtime inlined_as_list-bug)"
    return 0
fi
```
