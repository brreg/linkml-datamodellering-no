# Plan: dokumenter alle kjente feil i repoet

## Bakgrunn

Kjente feil er i dag spreidde på tre ulike stader:

- **`tests/test_make.sh`** — skip-betingelser med kortfattane kommentarar
- **`specs/backlog/`** — årsaksanalyse og løysingsplan der nokon feil er nærare beskrivne
- **Ingen stad** — feil som berre er kjende av dei som har arbeidd med repoet

Det finst ingen samla oversikt som gjev ny medarbeidar eller automatiserte verktøy
éin stad å sjå kva feil som eksisterer, kva status dei har, og kva konsekvensar dei har.

## Mål

Éi `specs/bugs/`-mappe der kvar kjend feil har éi eiga fil. Mappas `README.md`
er ein indeks. Bugfilene følgjer eit fast format som gjer det enkelt å finne og
oppdatere status.

## Filstruktur

```
specs/
  bugs/
    README.md                          ← indeks over alle kjente feil
    langstring-rdflib-roundtrip.md     ← bug 1
    inlined-as-list-rdflib-roundtrip.md ← bug 2
    … (éi fil per bug)
```

## Format for kvar bugfil

```markdown
# Bug: <kort tittel>

**Status:** open | upstream | workaround | løyst
**Komponent:** linkml-runtime | linkml | intern-schema | anna
**Oppdaga:** <dato>

## Symptom

Kort skildring av kva som faktisk skjer — feilmeldinga eller åtferda ein ser.

## Berørte skjema / testar

Kva skjema, testar eller funksjonar som vert påverka. Direkte kopling til
skip-betingelser i `test_make.sh` om relevant.

## Rot-årsak

Kva er den underliggjande årsaka. Om det er ein upstream-bug, lenk til
issue dersom det finst.

## Workaround

Kva vi gjer i dag for å handsame feilen (skip i test, modellering-omveg o.l.)

## Løysing

Kva som må til for å løyse feilen permanent. Om det avheng av upstream:
kva versjon / commit vi ventar på.
```

## Kjente feil som skal dokumenterast

### Bug 1 — `rdflib_loader` rekonstruerer ikkje `LangString` frå TTL

| Felt | Verdi |
|---|---|
| Status | `upstream` |
| Komponent | `linkml-runtime` |
| Symptom | `LangString`-verdiar (`dct:title`, `skos:prefLabel` o.l.) forsvinn etter TTL→YAML i `rdflib_loader`. Om sloten har `required: true` kastar Python `ValueError: X must be supplied`. |
| Berørte skjema | `brreg-begrepskatalog`, `brreg-modellkatalog` |
| Workaround | `required: true` fjerna frå alle LangString-slots i `skos-ap-no` og `modelldcat-ap-no`; skip i `test_roundtrip_ttl` med melding `linkml-runtime LangString-bug` |
| Løysing | Upstream fix i `linkml-runtime` |

### Bug 2 — `rdflib_loader` feiler på `inlined_as_list` med `identifier: true`

| Felt | Verdi |
|---|---|
| Status | `upstream` |
| Komponent | `linkml-runtime` |
| Symptom | `TypeError: OffisiellAdresse.__init__() got an unexpected keyword argument 'X'` ved TTL→YAML for containerklassar der range-klassen har `identifier: true` og attributten er `inlined_as_list: true`. |
| Berørte skjema | `ngr-adresse`, `ngr-eiendom`, `ngr-virksomhet` |
| Workaround | Skip i `test_roundtrip_ttl` og `test_convert_rdf`; sjå `fix-roundtrip-ngr-inlined-as-list.md` for alternativ |
| Løysing | Upstream fix i `linkml-runtime`, eller endre container-design til URI-referansar (sjå backlog-spec) |

## Tiltaksliste

| # | Tiltak | Fil |
|---|---|---|
| 1 | Opprett `specs/bugs/`-mappa | — |
| 2 | Opprett `specs/bugs/README.md` med indekstabell | — |
| 3 | Skriv `specs/bugs/langstring-rdflib-roundtrip.md` for Bug 1 | — |
| 4 | Skriv `specs/bugs/inlined-as-list-rdflib-roundtrip.md` for Bug 2 | — |
| 5 | Oppdater kommentarane i `test_make.sh` til å peike på tilhøyrande bugfil | `tests/test_make.sh` |
| 6 | Legg til ein konvensjon i `CLAUDE.md`: skip-betingelser i `test_make.sh` skal alltid ha ei tilhøyrande fil i `specs/bugs/` | `CLAUDE.md` |

## Utført

Alle tiltak er gjennomførte som planlagt.

- `specs/bugs/README.md` oppretta med indekstabell og statusforklaring
- `specs/bugs/langstring-rdflib-roundtrip.md` (BUG-1) skriven med symptom, rot-årsak, workaround og løysingsplan
- `specs/bugs/inlined-as-list-rdflib-roundtrip.md` (BUG-2) skriven tilsvarande
- `tests/test_make.sh` oppdatert: skip-kommentarar refererer no til BUG-ID og tilhøyrande fil
- `CLAUDE.md` oppdatert med seksjon «Kjente feil» og konvensjon for skip-betingelser
