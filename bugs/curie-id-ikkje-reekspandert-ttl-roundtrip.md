# Bug: `rdflib_loader` re-ekspanderer ikkje kompaktert CURIE til full URI for `uriorcurie`-identifikatorar

**ID:** BUG-18
**Status:** `workaround`
**Komponent:** `linkml-runtime` (`rdflib_loader`)
**Oppdaga:** 2026-08-14

## Symptom

`roundtrip-ttl (lunchregisteret)` feila:

```
ROUNDTRIP-AVVIK (yaml→ttl→yaml→json):
Forventa: {'@type': 'LunchregisteretContainer',
 'lunchregistereter': [{'id': 'https://data.norge.no/oreg/lunchregisteret/eksempel-1'}]}
Fekk:     {'@type': 'LunchregisteretContainer',
 'lunchregistereter': [{'id': 'lunchregisteret:eksempel-1'}]}
```

`id`-verdien kjem attende som ein kompaktert CURIE i staden for den
opphavlege fulle URI-en.

## Rot-årsak

Turtle-serialisering kompakterer alltid ein full URI til ein CURIE når
URI-en sitt navnerom matchar eit registrert skjema-prefiks (standard,
deterministisk rdflib/LinkML-åtferd). `rdflib_loader` re-ekspanderer
derimot **ikkje** ein slik kompaktert CURIE tilbake til den fulle
URI-strengen når han les TTL-en attende for eit `range: uriorcurie`-slot
med `identifier: true` — verdien blir verande som den kompakterte
CURIE-strengen.

Dette slår berre inn når identifikator-**verdien** sitt navnerom **nøyaktig
matchar** eit av skjemaet sine eigne registrerte prefiks. Stadfesta ved
samanlikning av tre `oreg`-skjema:

| Skjema | Id-verdiform i eksempelet | Eige navnerom? | Roundtrip-ttl |
|---|---|---|---|
| `lunchregisteret` (før fiks) | Full URI: `https://data.norge.no/oreg/lunchregisteret/eksempel-1` | Ja (matchar `default_prefix`) | FEIL |
| `register-over-aksjeeiere` | CURIE alt frå kjelda: `aksje:Aksjeselskap1` | Ja, men alt CURIE | OK |
| `enhetsregisteret-bvrinnfelles` | Full URI: `https://example.org/innrapportering/1` | Nei (framand plassholder-navnerom) | OK |

Same familie som BUG-1 (`LangString` vert ikkje korrekt rekonstruert frå
TTL): `rdflib_loader` bevarer ikkje alltid den opphavlege
strengrepresentasjonen av ein verdi ved deserialisering.

## Workaround

`make new-modell` sin scaffolda eksempelfil skreiv tidlegare id-verdien som
full URI (`id: $SCHEMA_ID/eksempel-1`) — garantert innanfor skjemaet sitt
eige navnerom, og dermed garantert å trigge denne avgrensinga for **kvar
einaste** nyscaffolda modell. Retta ved å skrive CURIE-form i staden
(`id: ${SCHEMA_NAME}:eksempel-1`, matchar mønsteret
`register-over-aksjeeiere` alt brukar) — sjå
`src/assets/scripts/scaffolding/new-modell.sh`.

Avgrensinga kan i prinsippet framleis ramme **handskrivne** eksempel som
uavhengig vel ein id-verdi i eige navnerom (full URI-form) — ingen generell
skip-mekanisme finst for dette, sidan det ikkje krasjar (berre gir avvik i
roundtrip-ttl-testen for det aktuelle skjemaet).

## Løysing

Ingen upstream-fiks venta — same kategori `rdflib_loader`-avgrensingar som
BUG-1/BUG-2/BUG-3. Unngå mønsteret (skriv identifikator-verdiar i eige
navnerom som CURIE, ikkje full URI) er den pragmatiske løysinga.
