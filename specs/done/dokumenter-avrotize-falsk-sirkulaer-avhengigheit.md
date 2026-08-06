# Dokumenter avrotize sin falske "circular dependency"-åtvaring

## Bakgrunn

`make gen-xsd` for `samt-bu` skreiv ei DEBUG-åtvaring:

```
WARNING: Unable to resolve circular dependency in no.norge.data.samt_bu.samt::document_wrapper with dependencies: ['no.norge.data.samt_bu.samt.Kontaktlaerer']
```

Brukaren bad om å finne rotårsaka. Undersøkinga (Tarjan SCC-analyse av
`$ref`-grafen i den genererte `samt-bu-schema.json`, instrumentering av
`avrotize` sin `dependency_resolver.py`) stadfesta at det **ikkje** finst
nokon reell sirkulær avhengigheit i skjemaet — sjå full analyse i
`bugs/avrotize-falsk-circular-dependency-warning.md` (BUG-9). Feilen er ein
falsk positiv i tredjepartsverktøyet `avrotize` sin dependency-resolver, som
ikkje søkjer gjennom `items`-nøkkelen til `array`-typa JSON Schema-felt
(nøyaktig forma multivalued `inlined_as_list`-attributtar kompilerer til) når
han skal matche/inline avhengige typar.

Ingen endring i vårt eige skjema kan fjerne åtvaringa — ho krev ein upstream-
fiks i `avrotize`. Brukaren bad om å dokumentere funnet i `bugs/`, i tråd med
repoet sin konvensjon for kjende feil med ekstern rotårsak.

## Steg

1. **Opprett** `bugs/avrotize-falsk-circular-dependency-warning.md` (BUG-9)
   med symptom, berørte skjema, rotårsak (stadfesta via SCC-analyse og
   instrumentering) og løysingssti, etter malen i eksisterande `bugs/*.md`.
2. **Oppdater** `BUGS.md`: legg til BUG-9 i indekstabellen og nemn han i
   "Generatorar"-seksjonen av PoC-status-oversikta.
3. Ingen skip-betingelse i `tests/test_make.sh` er nødvendig — ingen test
   feilar, åtvaringa er reint informativ støy.

## Handlingsliste

- [x] Opprett `bugs/avrotize-falsk-circular-dependency-warning.md` (BUG-9)
- [x] Legg til BUG-9 i `BUGS.md` sin indekstabell og PoC-status-oversikt

## Utført

Oppretta `bugs/avrotize-falsk-circular-dependency-warning.md` (BUG-9, status
`upstream`, komponent `avrotize`) med full rotårsaksanalyse: Tarjan SCC-
analyse av `$ref`-grafen (null reelle syklusar), instrumentert
`dependency_resolver.py` som stadfestar at `swap_dependency_type()` ikkje
søkjer inn i `items`-nøkkelen til `array`-typa union-medlemmar, og
observasjonen at klassenamnet i åtvaringa varierer mellom identiske
køyringar (ikkje-deterministisk set/dict-iterasjon i `avrotize`).

Oppdatert `BUGS.md`: BUG-9 lagt til i indekstabellen og i
"Generatorar"-seksjonen av PoC-status-oversikta.

Ingen kodeendring i eige skjema — feilen er reint informativ og krev
upstream-fiks i `avrotize`.
