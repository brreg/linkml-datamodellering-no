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

Dette er eit kjend `linkml-runtime`-bug. Ei mogleg
løysing frå vår side er å fjerne `inlined: true` / `inlined_as_list: true`
frå container-attributtane og berre bruke URI-referansar. Men det vil endre
serialiseringsformatet — container vil då berre innehalde ei liste av URI-ar,
ikkje fulle objekt — og er ei semantic/design-endring som krev avklaring.

## Alternativ

### Alternativ A: Endre container til URI-lister (anbefalt om riktig for domenet)

```yaml
# Før
offisielle_adresser:
  range: OffisiellAdresse
  multivalued: true
  inlined: true
  inlined_as_list: true

# Etter
offisielle_adresser:
  range: OffisiellAdresse
  multivalued: true
  # inlined: false er default når range har identifier: true
```

Dette gjer at datafila kun inneheld URI-referansar på container-nivå, og
kvar `OffisiellAdresse` vert eige objekt med eigen URI.

### Alternativ B: Vent på upstream-fix i linkml-runtime

Hald skip-betingelsen i `test_roundtrip_ttl` inntil linkml-runtime
fiksar `rdflib_loader` for `inlined_as_list`-tilfeller.

## Prioritert tiltaksliste

| # | Tiltak | Prioritet |
|---|---|---|
| 1 | Avklar med domeneeier om container-attributtar for NGR bør bruke URI-referansar eller fulle inline-objekt | Høg |
| 2a | (Alt A) Fjern `inlined: true` og `inlined_as_list: true` frå alle container-attributtar i `ngr-adresse-schema.yaml`, `ngr-eiendom-schema.yaml`, `ngr-virksomhet-schema.yaml` | Medium |
| 2b | (Alt A) Oppdater eksempeldatafilene tilsvarande | Medium |
| 3 | (Alt A) Køyr `make test` og verifiser `roundtrip-ttl` passerer | Medium |
| 4 | (Alt A) Fjern ngr-skjemaa frå skip-lista i `test_roundtrip_ttl` og `test_convert_rdf` | Medium |
| 5 | (Alt B) Overvak linkml-runtime-issue og implementer fix når biblioteket er oppdatert | Lav |

## Referanse

Feilen er dokumentert som kjend bug i `tests/test_make.sh`:
```bash
# linkml-runtime-bug: id-only inlined_as_list-objekt
if [[ "$name" == "ngr-adresse" || ... ]]; then
    echo "Hoppar over roundtrip-ttl for $name (linkml-runtime inlined_as_list-bug)"
    return 0
fi
```
