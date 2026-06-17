# Bug: `linkml lint --validate` er avvikla

**ID:** BUG-4
**Status:** `løyst`
**Komponent:** `Makefile` / `linkml-lint`
**Oppdaga:** 2026-06-17

## Symptom

`make lint` skriv ut to åtvaringslinjer ved kvar køyring:

```
DeprecationWarning: The option 'validate' is deprecated.
/usr/local/lib/python3.11/site-packages/linkml/linter/cli.py:101: DeprecationWarning: [lint-validate-flag] DEPRECATED
The --validate flag for linkml-lint is deprecated. Metamodel validation now always runs before linting.
Deprecated In: 1.11.0
Removed In: 1.13.0
Recommendation: Remove the --validate flag from your command. Metamodel validation is now automatic.
```

Flagget `--validate` vart avvikla i linkml 1.11.0 og vert fjerna i 1.13.0. Frå og med
1.11.0 køyrer metamodell-validering alltid automatisk før linting — flagget er overflødig.

## Rot-årsak

`Makefile` sitt `lint`-mål brukar `linkml lint --validate` på linje 280 og 282.
Flagget `--validate` er ikkje lenger nødvendig og vil stoppe å fungere i linkml 1.13.0.

## Workaround / Fix

Fjern `--validate` frå `linkml lint`-kallet i `Makefile`:

```makefile
# Før
$(LINKML_RUN) linkml lint --validate "$(SCHEMA)"

# Etter
$(LINKML_RUN) linkml lint "$(SCHEMA)"
```

Dette er eit enkelt søk-og-erstatt i `Makefile` linje 280 og 282. Ingen skip i testar
er nødvendig — dette er ein intern Makefile-feil, ikkje ein upstream linkml-bug.

## Løysing

Fjern `--validate` frå begge `linkml lint`-kalla i `Makefile` (linje 280 og 282).
Oppdater denne fila til `Status: løyst` etter at endringa er gjort.
