# Bug: `RDFGenerator`/`JSONLDGenerator` fetchar `<import>.context.jsonld` over nettverk — 404 for versjonslåste URL-importar

**ID:** BUG-17
**Status:** `workaround`
**Komponent:** `linkml` (`linkml/generators/jsonldgen.py::JSONLDGenerator.end_schema`, brukt av `linkml/generators/rdfgen.py::RDFGenerator.end_schema`)
**Oppdaga:** 2026-08-14

## Symptom

`make gen-rdf SCHEMA=<skjema med versjonslåst URL-import>` (og dermed
`make domain-<domene>` for domene som inneheld eit slikt skjema) feila med:

```
[ERROR] ::error file=src/linkml/oreg/lunchregisteret/lunchregisteret-schema.yaml
::rdf feila for oreg/lunchregisteret (3.42s) — HTTP Error 404: Not Found
```

Trigga av eit skjema (t.d. den scaffolda `src/linkml/oreg/lunchregisteret/lunchregisteret-schema.yaml`)
som importerer `dcat-ap-no-schema` via ein versjonslåst
`raw.githubusercontent.com`-URL, slik `make new-modell` set inn som
standard.

## Rot-årsak

`RDFGenerator.end_schema()` byggjer JSON-LD internt via `JSONLDGenerator`.
`JSONLDGenerator.end_schema()` legg **ubetinga** til éin `@context`-URL per
import i importgrafen — uavhengig av om eit eige `context`-argument er
gjeve (loopen ligg utanfor if/elif-kjeda som handterer det argumentet):

```python
for imp in list(self.loaded.values())[1:]:
    context.append(imp[0] + ".context.jsonld")
```

`imp[0]` er den oppløyste importstrengen. For eit versjonslåst URL-import
vert dette t.d.
`https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/dcat-ap-no-v2.14.0/src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.context.jsonld`.
`rdflib` sin JSON-LD-parser **fetchar denne URL-en over nettverk** når
grafen vert parsa i `end_schema()` (`graph.parse(data=jsonld_str, format="json-ld", ...)`).

To uavhengige grunnar til at URL-en aldri kan løyse seg for dette repoet:

1. **Plassering:** `.context.jsonld`-filer er byggoutput (`make gen-jsonld-context`),
   skrivne til `generated/`, som er heilt `.gitignore`-a — dei finst aldri
   i git-historia, verken på `main` eller på nokon versjonstag.
   `JSONLDGenerator` føreset at fila ligg **rett ved sida av** kjeldeskjemaet
   sin plassering (`src/linkml/...`), ei føresetnad som held for
   LinkML-prosjekt som publiserer byggoutput saman med kjeldekoden, men
   ikkje for dette repoet sitt skilje mellom kjeldekode og byggoutput.
2. **Namngjeving:** Sjølv om ei fil fanst der, ville filnamnet uansett ikkje
   matche — LinkML konstruerer alltid `<importnamn> + ".context.jsonld"`
   (**punktum** før "context"), medan `batch-generate.py` sin `REGISTRY`
   (out_suffix `"context.jsonld"` kombinert med skjemanamn) alltid
   produserer `<schema>-context.jsonld` (**bindestrek** før "context") —
   t.d. `generated/ap-no/dcat-ap-no/dcat-ap-no-context.jsonld`.

Feilen er **isolert til `gen-rdf`** — stadfesta empirisk mot det same
skjemaet at `gen-python`, `gen-jsonschema`, `gen-owl`, `gen-proto`,
`gen-graphql`, `gen-jsonld-context`, `gen-shacl` og `gen-plantuml` genererer
problemfritt for eit skjema med versjonslåst URL-import. `linkml-convert`
(brukt av `make roundtrip`/`convert-rdf` via `batch-convert.py`) brukar ein
heilt annan kodeveg for RDF/TTL-output (`SchemaView` +
`linkml_runtime`-dumparar, ikkje `RDFGenerator`) og er heller ikkje ramma —
sjå i staden BUG-15 for den feilen.

## Workaround

`batch-generate.py` sitt `GeneratorSpec` for `"rdf"` har feltet
`skip_if_versioned_import=True`. `main()` filtrerer skjema med minst eitt
versjonslåst import (`schema_has_versioned_import()`, sjekkar `"://"` i
`imports:`-lista) bort frå `gen-rdf`-køyringa **før** forsøk, og skriv ei
tydeleg, ikkje-stille loggline (`HOPPAR OVER rdf for <domene>/<namn> — ...`)
i staden for å telje det som ein feil. Domenet/CI feilar difor ikkje lenger
på dette — `schema.ttl` vert berre ikkje generert for slike skjema.
`mkdocs/publish.sh` sin artefakttabell (linje 436-441) sjekkar alt
`[ -f ... ]` før han listar kvar artefakttype, så eit manglande
`schema.ttl` gir ingen broten lenkje i dokumentasjonsportalen.

Scope: dette løyser berre **vår eigen lokale/CI-generering**. Ei eksterne
part som sjølv køyrer `gen-rdf` mot eit av våre publiserte skjema via den
same pinna URL-en, ville framleis treffe same 404 — vurdert og medvite lagt
utanfor scope (sjå `specs/done/fiks-ap-no-import-feil-new-modell.md`).

## Løysing

Ingen upstream-fiks venta. `JSONLDGenerator.end_schema()` sin
`.context.jsonld`-konstruksjon er eit medvite designval i LinkML (føreset
at genererte artefakt vert publisert saman med kjeldekoden), ikkje ein bug
i tradisjonell forstand — usannsynleg at upstream endrar standardåtferda.
Dersom repoet i framtida vel å committe/publisere `.context.jsonld` for
AP-NO-profilane på ein URL og med eit namn som matchar det LinkML
konstruerer, kan skip-logikken fjernast for dei aktuelle skjemaa.
