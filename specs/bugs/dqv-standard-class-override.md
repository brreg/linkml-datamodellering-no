# Bug: Class override av importert klasse krasjar/korrumperer avhengig av generator

**ID:** BUG-6
**Status:** `workaround`
**Komponent:** `linkml` (generator-inkonsistens mellom SchemaLoader og SchemaView)
**Oppdaga:** 2026-06-20

## Symptom

`dqv-ap-no-schema.yaml` redeklarerte tidligare klassa `Standard` (definert og
importert frå `dcat-ap-no-schema.yaml`) for å «leggje til» eit DQV-spesifikt
slot via eit «class override»-mønster:

```yaml
classes:
  Standard:
    description: Ein standard eller spesifikasjon som eit datasett er i samsvar med.
    slots:
      - er_i_kvalitetsdimensjon
    slot_usage:
      er_i_kvalitetsdimensjon:
        in_subset:
          - Anbefalt
```

Dette gav to ulike, begge uønska, utfall avhengig av generator:

1. **Hard krasj** for `gen-python`, `gen-rdf`, `gen-jsonld-context` og
   `linkml-convert` (dermed òg `make roundtrip`):
   ```
   ValueError: Conflicting URIs (https://data.norge.no/ap-no/dcat-ap-no, https://data.norge.no/ap-no/dqv-ap-no) for item: Standard
   ```
   frå `linkml/utils/mergeutils.py::merge_dicts`.
2. **Silent korrupsjon** for `gen-json-schema`, `gen-shacl`, `gen-owl`: lokal
   redeklarering **erstattar** heile klassedefinisjonen i staden for å union'e
   slot-lista — `Standard` mista `id`, `tittel`, `har_referanse`, `har_merknad`
   og `versjon`, og sat berre med det nytt tillagde slottet. Dette gjorde at
   instansvalidering feila med «Additional properties are not allowed» for
   alle legitime `Standard`-felt, og at referansar til `Standard` (t.d.
   `i_samsvar_med`) blei feilaktig forventa som inline-objekt i staden for
   ein streng-URI (fordi `Standard` «mista» identifikator-slottet sitt).

Påvirka skjema: `dqv-ap-no-schema.yaml` (isolert, **utan** nedstrøms import)
og `samt-bu-schema.yaml` (transitivt, via import av `dqv-ap-no-schema.yaml`).

## Rot-årsak

LinkML har to ulike kodepatar for import-merge:

- **SchemaView-baserte generatorar** (json-schema, shacl, owl) behandlar ei
  lokal redeklarering av eit importert klassenamn som ei **fullstendig
  erstatning** — den lokale definisjonen må derfor vere sjølvstendig komplett
  (inkludere alle slot frå originalen), elles tapast dei.
- **SchemaLoader-baserte generatorar** (python, rdf, jsonld-context,
  linkml-convert) kallar `merge_schemas` → `merge_dicts`, som kastar
  `ValueError` så snart to `ClassDefinition`-objekt med samme namn har ulik
  `from_schema` — **uavhengig av** om slot-lista er komplett eller ikkje.

Verifisert empirisk (i ein isolert testkopi, ikkje i repoet): å fylle ut heile
det opphavlege slot-settet i overstyringa løyser **ikkje** krasjen i punkt 2 —
`merge_dicts` kastar uansett. Den einaste verifiserte løysinga er å ikkje
redeklarere klassa i det heile.

## Workaround

Fjern class override-mønsteret heilt. I dette tilfellet vart relasjonen
modellert omvendt i staden: `Kvalitetsdimensjon` (definert i
`dqv-core-schema.yaml`, der ho **eigentleg** høyrer heime) fekk eit nytt slot
`gjelder_standard` med `range: uriorcurie` (ikkje `range: Standard`, av
samme grunn som det eksisterande `har_maal`-slottet i samme fil brukar
`uriorcurie` — ein direkte klassereferanse til `Standard` ville krevd at
`dqv-core-schema.yaml` importerer `dcat-ap-no-schema.yaml`, som allereie
importerer `dqv-core-schema.yaml`, altså sirkulær import).

Sjå `src/linkml/ap-no/dqv-ap-no/dqv-core-schema.yaml` (`gjelder_standard`) og
`src/linkml/ap-no/dqv-ap-no/dqv-ap-no-schema.yaml` (override-blokk fjerna).

**Generell regel for resten av repoet:** unngå å redeklarere ei klasse som
er definert i eit importert skjema for å «leggje til» eit slot. Legg i
staden det nye slottet til i klassa sitt **opphavlege** skjema (krev tilgang
til klassa der ho er definert), eller modeller relasjonen omvendt (slot på
den andre klassa, med `range: uriorcurie` dersom ein direkte klassereferanse
ville skapt sirkulær import).

## Løysing

Ingen upstream-fiks venta — dette er eit avgjort designval i LinkML (klasse-
redeklarering = full erstatning, ikkje union), kombinert med ein reell
inkonsistens mellom generatorane i korleis dette handteres (krasj vs. stille
erstatning). Workaround (unngå mønsteret) er permanent løysing for dette repoet.
