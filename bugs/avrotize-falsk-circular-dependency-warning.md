# Bug: `avrotize` sin dependency-resolver rapporterer falsk sirkulær avhengigheit for containerklasser

**ID:** BUG-9
**Status:** `upstream`
**Komponent:** `avrotize` (`dependency_resolver.py`)
**Oppdaga:** 2026-08-06

## Symptom

`make gen-xsd` (via `j2a`-steget, JSON Schema → Avrotize-skjema) skriv ei
`WARNING`-linje til DEBUG-loggen for skjema med `xsd: true`:

```
WARNING: Unable to resolve circular dependency in no.norge.data.samt_bu.samt::document_wrapper with dependencies: ['no.norge.data.samt_bu.samt.Kontaktlaerer']
```

Namnet på klassen i meldinga er **ikkje deterministisk** — gjentekne køyringar
mot identisk input namngir ulike klassar (`Kontaktlaerer`, `Distribusjon`,
`Elev` er alle observerte på same skjema).

Åtvaringa påverkar **ikkje** byggresultatet: `j2a`- og `a2x`-steget lukkast,
og `fix-xsd-dates`-steget køyrer etterpå og fiksar datofelt som normalt. Ho
er reint støy i DEBUG-loggen, ikkje ein feil.

## Berørte skjema

Berre `samt-bu` har `xsd: true` i `build.yaml` per 2026-08-06 (einaste skjema
i repoet med XSD-generering aktivert). Rotårsaka gjeld generisk for **alle**
`tree_root`-containerklasser med to eller fleire `multivalued: true,
inlined_as_list: true`-attributtar — dvs. praktisk talt alle domenemodellar
i repoet ville trigga same åtvaring dersom `xsd: true` vart aktivert for dei.

## Rot-årsak (stadfesta ved kodelesing og instrumentering)

Stadfesta at dette **ikkje** er ei reell sirkulær avhengigheit:

1. Full `$ref`-avhengigheitsgraf ekstrahert frå den genererte
   `samt-bu-schema.json` og køyrd gjennom Tarjan sin SCC-algoritme — null
   sterkt samanhengande komponentar med meir enn eitt medlem, null
   sjølvreferansar.
2. Instrumentert ein kopi av `avrotize` sin `dependency_resolver.py`
   (`swap_record_dependencies`) og stadfesta at det ALLTID er akkurat éin
   attributt i containerklassen sin `document_wrapper.root`-felt som ikkje
   vert løyst — ikkje fordi klassen faktisk avheng sirkulært av containeren,
   men fordi `swap_dependency_type()` berre matchar avhengigheiter der
   `field['type']` er ein bar streng lik avhengigheitsnamnet. Multivalued
   LinkML-attributtar (`inlined_as_list: true`) kompilerer til JSON Schema
   på forma:
   ```json
   {"type": ["null", {"type": "array", "items": "no.norge.data.samt_bu.samt.Elev"}]}
   ```
   Referansen til den avhengige typen ligg her inni `items`-nøkkelen til eit
   nøsta `array`-objekt, ikkje som ein direkte streng-verdi på `field['type']`.
   `resolve_field_dependencies()`/`swap_dependency_type()` i `avrotize` går
   ikkje eitt nivå djupare inn i `items` for å matche/inline denne referansen.
   Etter éin fullstendig gjennomgang av felta er difor
   `record['dependencies']` uendra (`prior_dependencies == dependencies`),
   løkka tolkar det som ei uløyseleg sirkulær avhengigheit, og skriv
   åtvaringa — sjølv om den refererte typen (t.d. `Elev`) alt er korrekt
   definert tidlegare i utdataet, og resultatet (`.avsc`/`.xsd`) er
   strukturelt gyldig.
3. Kva klassenamn som hamnar i åtvaringsmeldinga varierer mellom køyringar
   fordi rekkjefølgja typane vert prosesserte i ikkje er deterministisk
   (truleg `PYTHONHASHSEED`-avhengig set/dict-iterasjon i `avrotize`) — eit
   ekstra teikn på at dette er eit generisk verktøy-avgrensing, ikkje eit
   modelleringsproblem knytt til éin spesifikk klasse.

## Workaround

Ingen workaround nødvendig — åtvaringa er reint informativ støy og påverkar
ikkje genererte artefakter. Ingen skip-betingelse i `tests/test_make.sh` er
lagt til sidan ingen test feiler.

## Løysing

Upstream-fix i `avrotize` sin `dependency_resolver.py` der
`resolve_field_dependencies()`/`swap_dependency_type()` også søkjer gjennom
`items`-nøkkelen til `array`-typa felt (ikkje berre `field['type']` direkte)
når han skal matche og inline avhengige typar. Ingen GitHub-issue er
identifisert pr. 2026-08-06.

Når upstream-fix er på plass: stadfest at `LOGLVL=DEBUG make gen-xsd
SCHEMA=src/linkml/samt/samt-bu/samt-bu-schema.yaml` ikkje lenger skriv
`WARNING: Unable to resolve circular dependency`, og oppdater denne fila til
`Status: løyst`.
