# Bug: `rdflib_loader` kastar `MappingError` for domene-URI-ar i TTL

**ID:** BUG-3
**Status:** `open`
**Komponent:** `linkml-runtime`
**Oppdaga:** 2026-06-09

## Symptom

`ttl→yaml`-steget i TTL-roundtrip feiler med:

```
linkml_runtime.MappingError: No pred for https://data.norge.no/fint/fint-administrasjon/arbeidsforhold <class 'rdflib.term.URIRef'>
linkml_runtime.MappingError: No pred for https://data.norge.no/samt/samt-bu/id <class 'rdflib.term.URIRef'>
```

`rdflib_loader` møter ein RDF-predikat med ein URI frå domene-prefiks-namnerommet
(`default_prefix`-URI-ar) og klarer ikkje å mappa han tilbake til ein slot i skjemaet.

## Berørte skjema / testar

| Skjema | Skip i |
|---|---|
| `fint-administrasjon` | `test_roundtrip_ttl` (FEIL, ikkje skip) |
| `fint-okonomi` | `test_roundtrip_ttl` (FEIL) |
| `fint-personvern` | `test_roundtrip_ttl` (FEIL) |
| `fint-utdanning` | `test_roundtrip_ttl` (FEIL) |
| `samt-bu` | `test_roundtrip_ttl` (FEIL) |

Merk: desse skjemaa er ikkje i skip-lista — dei køyrer og feiler.

## Rot-årsak (hypotese)

`rdflib_loader` brukar `slot_uri`-mappingane til å konvertere RDF-predikatar
tilbake til slots. For slots som manglar eksplisitt `slot_uri`, genererer
LinkML ein URI basert på `default_prefix` + slotnamn. Desse URI-ane endar opp
i TTL-fila, men `rdflib_loader` klarer ikkje å slå dei opp att i slot-registeret
under deserialisering.

Dette er truleg relatert til korleis `schemaview` løyser slot-URI-oppslag for
slots utan eksplisitt `slot_uri`.

## Workaround

Ingen aktiv workaround. Desse skjemaa feiler i `test_roundtrip_ttl`.

Moglege tilnærmingar for å undersøkje:
- Sjekk om `fint-ressurs` og `fint-arkiv` (som passerer) har eksplisitt `slot_uri`
  på alle slots, i motsetnad til `fint-administrasjon` (som feiler)
- Sjekk om å leggje til eksplisitt `slot_uri` på berørte slots løyser problemet

## Løysing

Uklart om dette er ein upstream-bug i `linkml-runtime` eller ein skjema-modelleringsfeil
(manglar `slot_uri` på nokre slots). Krev nærare analyse.

Neste steg:
1. Samanlikn `fint-ressurs` (passerer) og `fint-administrasjon` (feiler) — finn
   kva slots som manglar `slot_uri` i det feilerande skjemaet
2. Test om å leggje til manglande `slot_uri` løyser roundtrip-feilen
3. Oppdater status til `workaround` eller `upstream` etter analyse
