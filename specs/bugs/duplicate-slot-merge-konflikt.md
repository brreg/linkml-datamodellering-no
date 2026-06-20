# Bug: Duplikat globalt slot-namn i importerte skjema krasjar (slot-variant av BUG-6)

**ID:** BUG-7
**Status:** `workaround`
**Komponent:** `linkml` (`linkml/utils/mergeutils.py::merge_dicts`)
**Oppdaga:** 2026-06-20

## Symptom

`make modellkatalog` feila i `gen-jsonld-context`-steget for
`brreg-modellkatalog-schema.yaml`:

```
ValueError: Conflicting URIs (https://data.norge.no/ap-no/dcat-ap-no, https://data.norge.no/ap-no/modelldcat-ap-no/katalog) for item: tema
```

og etter delfiks, ein ny variant for `begrep`:

```
ValueError: Conflicting URIs (https://data.norge.no/ap-no/dcat-ap-no, https://data.norge.no/ap-no/modelldcat-ap-no/modell) for item: begrep
```

## Rot-årsak

Same mekanisme som **BUG-6** (`dqv-standard-class-override.md`), men på
**slot-nivå** i staden for klasse-nivå: `merge_dicts` kastar `ValueError` så
snart eit slot-namn finst i meir enn eitt skjema i importgrafen med ulik
`from_schema` — **uavhengig av om definisjonane er identiske**. Gjeld
`gen-jsonld-context`, `gen-python`, `gen-rdf` og `linkml-convert` (alle
SchemaLoader-baserte generatorar), og dermed òg `make roundtrip`.

To variantar av mønsteret blei funne i `modelldcat-ap-no`-importkjeda:

1. **Lokal redeklarering av eit importert slot** (same form som BUG-6):
   `modelldcat-katalog-schema.yaml` definerte sin eigen `tema`, `lisens`,
   `har_del` og `erstatter` i `slots:`-blokka, samtidig som skjemaet
   importerer `dcat-ap-no-schema.yaml` som allereie definerer desse same
   slot-namna (sidan MC8-refaktoreringa, commit `4b4bad4f`).
2. **Kollisjon mellom to søsken-importerte skjema**: `begrep` var
   uavhengig definert i både `dcat-ap-no-schema.yaml` (`range: string`) og
   `modelldcat-modell-schema.yaml` (`range: Konsept`) — ingen av dei
   importerer det andre, men begge blir importerte som søsken av
   `modelldcat-katalog-schema.yaml`. Dette er strukturelt vanskelegare enn
   (1) fordi `slot_usage` på importør-nivå ikkje kan løyse ein kollisjon
   mellom to importerte skjema.

## Workaround

For variant 1: fjern den lokale slot-redeklareringa heilt, og flytt
range-overstyringa inn i `slot_usage` på dei klassane som trenger avvikande
range frå den importerte versjonen.

For variant 2: harmoniser dei to konkurrerande definisjonane til éin
kanonisk versjon (her: `dcat-ap-no-schema.yaml` sin `begrep`-range blei
endra frå `string` → `Konsept`, og duplikaten i `modelldcat-modell-schema.yaml`
blei fjerna). Dette krev ei vurdering av kva for definisjon som er den
korrekte/kanoniske, og kontroll av at ingen eksisterande instansdata brukar
den andre definisjonen sin range.

Sjå `specs/done/fix-modellkatalog-slot-merge-konflikt.md` for full analyse,
verifiseringssteg og diff.

**Generell regel (utvidar regelen frå BUG-6):** unngå å redeklarere eit
slot-namn (eller klassenamn) som allereie finst andre steder i importgrafen
til skjemaet — uavhengig av om innhaldet er identisk eller ikkje. Dette
gjeld både (a) lokal redeklarering i importøren av eit slot frå sine eigne
importar, og (b) uavhengige søsken-skjema som begge blir importerte av eit
tredje skjema og som tilfeldigvis deler eit slot-namn.

## Løysing

Ingen upstream-fiks venta — same designval i LinkML som BUG-6 (namnekollisjon
i importgrafen = hard feil for SchemaLoader-baserte generatorar, uavhengig av
innhald). Workaround (unngå duplikate namn) er permanent løysing for dette
repoet.
