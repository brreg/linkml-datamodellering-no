# Fix: samt-bu TTL-namespace får ekstra kolon

## Bakgrunn

`test_roundtrip_ttl` hoppar over `samt-bu` fordi `ttl→yaml`-steget feiler:

```
linkml_runtime.DataNotFoundError: Got 0 of type <class 'test.SamtBuContainer'> from source, expected exactly 1
```

## Rot-årsak

`samt-bu` har `default_prefix: https://data.norge.no/samt/samt-bu/` (absolutt URL)
utan at denne URL-en er registrert som ein namngitt prefix-alias i `prefixes:`-blokka.
Dette fører til at rdflib konstruerer ein feil namespace i TTL-outputen:

```turtle
@prefix ns1: <https://data.norge.no/samt/samt-bu/:> .   # ← FEIL, ekstra kolon

[] a ns1:SamtBuContainer ;   # URI vert https://data.norge.no/samt/samt-bu/:SamtBuContainer
```

Riktig namespace burde vere `https://data.norge.no/samt/samt-bu/SamtBuContainer`.
Den uriktige URI-en (`https://data.norge.no/samt/samt-bu/:SamtBuContainer`) er
ikkje det same som kva `rdflib_loader` reknar ut som class-URI for `SamtBuContainer`,
og resultatet er at loader finn 0 instansar av rett type.

**Kontrast med fint-ressurs** (som fungerer): `fint-ressurs` har óg
`default_prefix: https://data.norge.no/fint/fint-ressurs/` utan namngitt alias,
men det ser ut til at interaksjonen med dei importerte AP-NO-skjemaa i `samt-bu`
forårsaker det ekstra kolonet. Rotkjelda er at `default_prefix` bør alltid
peike til ein registrert prefix-alias, ikkje ein rå URL.

## Løysing

Legg til ein namngitt prefix-alias `samtbu` og bruk denne som `default_prefix`.

### Endring i `src/linkml/samt/samt-bu/samt-bu-schema.yaml`

```yaml
# Før
prefixes:
  linkml: https://w3id.org/linkml/
  samtbuskole: https://example.no/ontology/skole#
  org:    http://www.w3.org/ns/org#

default_prefix: https://data.norge.no/samt/samt-bu/

# Etter
prefixes:
  linkml: https://w3id.org/linkml/
  samtbuskole: https://example.no/ontology/skole#
  samtbu: https://data.norge.no/samt/samt-bu/
  org:    http://www.w3.org/ns/org#

default_prefix: samtbu
```

Dette genererer korrekt TTL:
```turtle
@prefix samtbu: <https://data.norge.no/samt/samt-bu/> .

[] a samtbu:SamtBuContainer ;   # URI vert https://data.norge.no/samt/samt-bu/SamtBuContainer ✓
```

Merk: `class_uri` for domaineklassar og `slot_uri` for slots brukar framleis
`samtbuskole:`-prefixet eksplisitt og vert ikkje påverka av denne endringa.

## Prioritert tiltaksliste

| # | Tiltak | Prioritet |
|---|---|---|
| 1 | Legg til `samtbu: https://data.norge.no/samt/samt-bu/` i `prefixes:` i `samt-bu-schema.yaml` | Høg |
| 2 | Endre `default_prefix: https://data.norge.no/samt/samt-bu/` til `default_prefix: samtbu` | Høg |
| 3 | Køyr `make lint SCHEMA=...samt-bu...` og `make validate-instance SCHEMA=...samt-bu...` | Høg |
| 4 | Verifiser at gen-rdf framleis fungerer: `make gen-rdf SCHEMAS=...samt-bu...` | Høg |
| 5 | Køyr full `make test SCHEMA=...samt-bu...` og sjekk at `roundtrip-ttl` no passerer | Høg |
| 6 | Fjern `samt-bu` frå skip-lista i `test_roundtrip_ttl` i `tests/test_make.sh` | Høg |

## Sidnotat: same mønster kan affektere andre skjema

Sjekk om andre skjema med `default_prefix` som absolutt URL (ikkje namngitt alias)
har same problem ved å kjøre roundtrip-testane. Alle skjema bør bruke mønsteret
`default_prefix: <alias>` der `<alias>` er definert i `prefixes:`.

## Utført

Alle tiltak gjennomførte. `make test` passerer 17/17 for `samt-bu` inkludert
`roundtrip-ttl`.

Endringar:
- `src/linkml/samt/samt-bu/samt-bu-schema.yaml`: lagt til `samtbu: https://data.norge.no/samt/samt-bu/` i `prefixes:`, endra `default_prefix` frå absolutt URL til `samtbu`.
- `tests/test_make.sh`: fjerna `samt-bu` frå skip-lista i `test_roundtrip_ttl`.

TTL-outputen genererer no `@prefix samtbu: <https://data.norge.no/samt/samt-bu/>` (utan ekstra kolon), og `SamtBuContainer` vert korrekt funne av `rdflib_loader`.
