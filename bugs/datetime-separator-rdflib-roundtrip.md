# Bug: `rdflib_loader` rekonstruerer `datetime`-verdiar med mellomrom i staden for `T`-separator frå TTL

**ID:** BUG-19
**Status:** `open`
**Komponent:** `linkml-runtime` (`rdflib_loader`, sannsynleg `datetime.__str__()` brukt i staden for `.isoformat()` ved deserialisering av `xsd:dateTime`)
**Oppdaga:** 2026-08-14

## Symptom

`roundtrip-ttl (enhetsregisteret-bvrinn)` feilar:

```
ROUNDTRIP-AVVIK (yaml→ttl→yaml→json):
Forventa: {..., 'innsendingstidspunkt': '2026-07-04T10:30:00', ...}
Fekk:     {..., 'innsendingstidspunkt': '2026-07-04 10:30:00', ...}
```

`T`-separatoren (ISO 8601) i den opphavlege `datetime`-verdien vert bytt ut
med eit mellomrom etter yaml→ttl→yaml-roundtrip.

## Rot-årsak

Isolert ved å køyre dei fire konverteringsstega manuelt (utanom
`test_make.sh`, med mellomresultat bevart for inspeksjon):

| Steg | Fil | Verdi |
|---|---|---|
| 1. `eksempel.yaml → a.json` | `a.json` | `"2026-07-04T10:30:00"` |
| 2. `eksempel.yaml → b.ttl` | `b.ttl` | `"2026-07-04T10:30:00"^^xsd:dateTime` (korrekt ISO 8601 i TTL-en) |
| 3. `b.ttl → c.yaml` | `c.yaml` | `'2026-07-04 10:30:00'` (**mellomrom** — feilen oppstår her) |
| 4. `c.yaml → d.json` | `d.json` | `"2026-07-04 10:30:00"` (arvar feilen frå steg 3) |

TTL-en sjølv er korrekt typa og formatert. Feilen oppstår i steg 3:
`rdflib_loader` parsar `xsd:dateTime`-literalen til eit Python
`datetime.datetime`-objekt, og YAML-dumparen serialiserer deretter dette
objektet med Python sin standard `str(datetime_obj)`-representasjon
(mellomrom-separert, `2026-07-04 10:30:00`) i staden for
`.isoformat()` (T-separert, `2026-07-04T10:30:00`) — ein vanleg
formatteringsinkonsistens ved rundt-tur gjennom eit `datetime`-objekt.

Same familie som BUG-1 (`LangString` vert ikkje rekonstruert korrekt frå
TTL): `rdflib_loader` bevarer ikkje alltid den opphavlege
strengrepresentasjonen av ein typa literal ved deserialisering.

## Berørte skjema

Stadfesta: `enhetsregisteret-bvrinn` (einaste skjema der roundtrip-ttl når
fram til denne samanlikninga med eit populert `datetime`-felt — andre
skjema med `range: datetime`-slots, som `fint-administrasjon`/`fint-okonomi`/
`fint-personvern`/`fint-utdanning`, krasjar tidlegare i pipelinen med
BUG-3 sin `MappingError`, så det er ukjent om dei **òg** ville trigga denne
feilen dersom BUG-3 vart løyst først).

## Løysing

Ingen upstream-fiks venta — dette er del av same kategori
`rdflib_loader`-avgrensingar som BUG-1/BUG-2/BUG-3, ingen av dei har fått
ein permanent fiks (`open`/`upstream`-status). Skip-betingelse i
`tests/test_make.sh` sin `roundtrip_ttl_job()` er den pragmatiske
handteringa, same mønster som BUG-1/BUG-2.
