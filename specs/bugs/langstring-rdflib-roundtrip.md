# Bug: `rdflib_loader` rekonstruerer ikkje `LangString` frå TTL

**ID:** BUG-1
**Status:** `upstream`
**Komponent:** `linkml-runtime`
**Oppdaga:** 2026-06-09

## Symptom

`LangString`-verdiar (`rdf:langString`) forsvinn etter TTL→YAML i `rdflib_loader`.
Dersom sloten hadde `required: true` kastar Python-klassen:

```
ValueError: anbefalt_term must be supplied
ValueError: tittel must be supplied
```

Dersom `required: true` er fjerna, kjem data tilbake som eit objekt der alle
LangString-felt er `None` — det vil seie at den returnerte YAML-fila manglar
alle titlar, namn og andre språkmerkte strengar.

## Berørte skjema / testar

| Skjema | Skip i |
|---|---|
| `brreg-begrepskatalog` | `test_roundtrip_ttl` |
| `brreg-modellkatalog` | `test_roundtrip_ttl` |

Alle skjema som importerer `common-ap-no` eller `skos-ap-no` og brukar
`LangString`-slots i data vil truleg ha same problem dersom dei roundtrippar TTL.
AP-NO-skjemaa (`ap-no`-domenet) er ikkje råka i praksis fordi dei manglar
`tree_root` og vert hoppet over av `test_roundtrip_ttl` av ein annan grunn.

## Rot-årsak

`rdflib_loader` i `linkml-runtime` les RDF-literalar (`rdf:langString`) frå
ein `rdflib.Graph`, men konverterer dei ikkje korrekt til LinkML sin
`LangString`-type ved deserialisering. Resultatet er at alle
`rdf:langString`-tripplar vert ignorerte, og `LangString`-slotane i Python-objektet
forblir tomme.

Dette er ein kjend bug i `linkml-runtime`. Ingen GitHub-issue er identifisert pr.
2026-06-09.

## Workaround

To endringar vart gjort som saman demper konsekvensane:

**1. Fjerna `required: true` frå alle LangString-slots** i `skos-ap-no` og
`modelldcat-ap-no` (og deira avhengige domain-skjema).

Bakgrunn: `required: true` i LinkML er ein Python-implementasjonsmekanisme som
kastar `ValueError` ved instansiering utan feltet. Dette kolliderer med
`rdflib_loader`-buggen som returnerer `None` for LangString. `in_subset: Obligatorisk`
bevarer den semantiske annoteringen som MCP-validatoren brukar til å handheve kravet.

Berørte slots og klasser etter endringa:

| Skjema | Klasse | Slot |
|---|---|---|
| `skos-ap-no` | `Begrep` | `anbefalt_term` |
| `skos-ap-no` | `Definisjon` | `tekst` |
| `skos-ap-no` | `Samling` | `tittel` |
| `modelldcat-ap-no` | `Aktor` | `namn_aktor` |
| `modelldcat-ap-no` | `Standard` | `tittel` |
| `modelldcat-ap-no` | `Modellkatalog` | `tittel`, `beskrivelse` |
| `modelldcat-ap-no` | `Informasjonsmodell` | `tittel` |
| `modelldcat-ap-no` | `Modellelement` | `tittel` |

**2. Skip i `test_roundtrip_ttl`** for `brreg-begrepskatalog` og `brreg-modellkatalog`
med kommentar som peikar til denne fila:

```bash
# linkml-runtime-bug: rdflib_loader rekonstruerer ikkje LangString-verdiar frå TTL
# Sjå specs/bugs/langstring-rdflib-roundtrip.md
if [[ "$name" == "brreg-begrepskatalog" || "$name" == "brreg-modellkatalog" ]]; then
    echo "Hoppar over roundtrip-ttl for $name (BUG-1: linkml-runtime LangString-bug)"
    return 0
fi
```

## Løysing

Upstream fix i `linkml-runtime` der `rdflib_loader` korrekt deserialiserer
`rdf:langString`-literalar til `LangString`-objektet.

Når upstream-fix er på plass:
1. Verifiser at `make test` passerer for `brreg-begrepskatalog` og `brreg-modellkatalog`
   utan skip.
2. Fjern skip-betingelsen frå `test_make.sh`.
3. Vurder å leggje `required: true` tilbake på dei kritiske LangString-slots der det
   er semantisk korrekt (sjå tabellen over).
4. Oppdater denne fila til `Status: løyst`.
