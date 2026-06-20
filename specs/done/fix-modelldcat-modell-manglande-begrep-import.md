# Fix: `make validate` feilar for `modelldcat-modell-schema.yaml` — manglar `begrep`-slot

## Bakgrunn

`make validate` køyrer `gen-linkml` på **alle** skjema som blir auto-oppdaga
av `SCHEMAS`-variabelen i `Makefile` (`find src/linkml -mindepth 3 -maxdepth 3
-name '*-schema.yaml' | grep -v common`) — inkludert delfiler som
`modelldcat-modell-schema.yaml`, ikkje berre dei øvste aggregator-skjemaa.
Køyring av `make validate` i dag (2026-06-20) gir:

```
→ gen-linkml  src/linkml/ap-no/modelldcat-ap-no/modelldcat-modell-schema.yaml
ValueError: No such slot begrep as an attribute of Modellelement ancestors or as a slot definition in the schema
```

Dette er den **einaste** feilen i heile `make validate`-køyringa (alle andre
~29 skjema, inkludert resten av `ap-no`-domenet, går gjennom utan feil).

### Rotårsak

`modelldcat-modell-schema.yaml` importerer berre:

```yaml
imports:
  - linkml:types
  - ../common/common-ap-no-schema
```

men tre klassar i fila (`Modellelement`, `Egenskap`, `Spesialisering` via
`har_generelt_begrep`-mønsteret) refererer til slotnamnet `begrep`, som
**ikkje** er definert lokalt og **ikkje** kjem frå `common-ap-no-schema.yaml`
— det er definert einaste staden i `dcat-ap-no-schema.yaml`.

Dette er ein direkte regresjon frå tiltak 6 i
`specs/done/fix-modellkatalog-slot-merge-konflikt.md` (BUG-7-fiksen): den
lokale `begrep`-deklarasjonen i `modelldcat-modell-schema.yaml` blei fjerna
fordi den kollapsa med `dcat-ap-no-schema.yaml` sin variant når begge blei
importerte som søsken av `modelldcat-katalog-schema.yaml`. Fiksen løyste
konflikten for **aggregatkjeda** (`modelldcat-ap-no-schema.yaml` →
`modelldcat-katalog-schema.yaml` → import av begge søsken), men gjorde
samtidig `modelldcat-modell-schema.yaml` **ugyldig som frittstående skjema**
— noko `make validate` no fangar opp fordi den køyrer `gen-linkml` på
fila isolert, ikkje berre via aggregatoren.

Verifisert: `tittel`, `identifikator_literal` og `beskrivelse` (som også
brukast av `Modellelement`/`Egenskap` utan lokal deklarasjon) er trygge,
fordi dei kjem frå `common-ap-no-schema.yaml`, som **er** importert. `begrep`
er det einaste slotnamnet i fila som manglar ei tilgjengeleg kjelde.

### Verifisert løysing (testa lokalt, reverter før denne specen blei skrive)

Legg til `../dcat-ap-no/dcat-ap-no-schema` som import i
`modelldcat-modell-schema.yaml`:

```yaml
imports:
  - linkml:types
  - ../common/common-ap-no-schema
  - ../dcat-ap-no/dcat-ap-no-schema
```

Dette er trygt fordi `modelldcat-katalog-schema.yaml` (som importerer
**begge** `modelldcat-modell-schema.yaml` og `dcat-ap-no-schema.yaml` som
søsken i dag) då importerer akkurat **det samme** `dcat-ap-no-schema.yaml`
via to stigar — eit diamant-import av identisk skjema, ikkje ein kollisjon
mellom to ulike definisjonar. BUG-6/BUG-7-mekanismen (`merge_dicts` kastar
`ValueError` kun når `from_schema` **skiljer seg** for samme namn) trigges
ikkje av diamant-import av identisk kjelde.

Verifisert empirisk:
- `podman run ... gen-linkml src/linkml/ap-no/modelldcat-ap-no/modelldcat-modell-schema.yaml` → exit 0, ingen feil
- `make lint SCHEMA=src/linkml/ap-no/modelldcat-ap-no/modelldcat-ap-no-schema.yaml` → «✓ No problems found»
- `make roundtrip SCHEMA=src/linkml/ap-no/modelldcat-ap-no/modelldcat-ap-no-schema.yaml` → 2 OK, 0 feil
- `make roundtrip SCHEMA=src/linkml/modellkatalog/brreg-modellkatalog/brreg-modellkatalog-schema.yaml` → 2 OK, 0 feil (downstream-konsument, ingen regresjon)

Endringa er reversert igjen før denne specen blei skrive, slik at
implementasjonen skjer som eige steg i tråd med «Planen kjem først».

## Alternativ vurdert og forkasta

**Alternativ B:** Ekskluder delfiler som `modelldcat-modell-schema.yaml` og
`modelldcat-katalog-schema.yaml` frå `SCHEMAS`-auto-oppdaginga i `Makefile`
(t.d. med eit namnemønster eller eit `manifest.yaml`-flagg), sidan dei er
interne byggjeklossar og ikkje meint å brukast frittstående.

Forkasta for no: ville krevd ei meir invaderande endring i
schema-discovery-logikken i `Makefile` (påvirkar `make validate`, `make
<domain>`, og `tests/test_make.sh` sin auto-oppdaging for **alle** domene,
ikkje berre `modelldcat-ap-no`), og løyser ikkje det underliggande
prinsippet at eit skjema i importgrafen bør vere sjølvstendig gyldig. Kan
revurderast som eige tiltak dersom flere slike «delfil er ikkje
frittstående»-tilfelle dukker opp i framtida.

## Prioritert tiltaksliste

| # | Tiltak | Fil | Prioritet |
|---|---|---|---|
| 1 | ✓ Legg til `../dcat-ap-no/dcat-ap-no-schema` i `imports:` i `modelldcat-modell-schema.yaml` | `src/linkml/ap-no/modelldcat-ap-no/modelldcat-modell-schema.yaml` | Høg |
| 2 | ✓ Køyr `make validate` fullt ut og stadfest 0 feil (ikkje berre `ap-no`-domenet) — stadfesta: ingen `Error`/`Traceback`/`ValueError` i utdataet, `make` returnerte 0 | — | Høg |
| 3 | ✓ Køyr `make lint` og `make roundtrip` for `modelldcat-ap-no-schema.yaml` og `brreg-modellkatalog-schema.yaml` for å stadfeste ingen regresjon i nedstrøms-konsumentar — «No problems found», 2 OK/0 feil for begge | — | Høg |
| 4 | ✓ Køyr `make validate-instance` mot `brreg-modellkatalog`-eksempel og produksjonsdatafil — «No issues found» for begge | — | Medium |
| 5 | ✓ Oppdater spesifikasjonsfila med ✓ og flytt til `specs/done/` (automatisk per CLAUDE.md når alle tiltak er utførte) | `specs/backlog/fix-modelldcat-modell-manglande-begrep-import.md` | — |

## Avhengigheiter

- Ingen — fiksen er eit enkelt, isolert importtillegg utan kjende
  følgjeverknader (verifisert empirisk over).

## Referanse

- `specs/done/fix-modellkatalog-slot-merge-konflikt.md` — opphavleg
  BUG-7-fiks som (uintendert) gjorde `modelldcat-modell-schema.yaml`
  ugyldig som frittstående skjema.
- `specs/bugs/duplicate-slot-merge-konflikt.md` (BUG-7) — generell regel:
  diamant-import av **identisk** skjema er trygt, kun reelle namnekrasj
  mellom **ulike** skjema er eit problem.

## Utført

Alle 5 tiltak gjennomførte som planlagt, ingen avvik frå planen:

- `modelldcat-modell-schema.yaml`: lagt til `../dcat-ap-no/dcat-ap-no-schema`
  i `imports:`. Diamant-import av identisk skjema (allereie importert via
  `modelldcat-katalog-schema.yaml`) — utløyste ikkje BUG-6/BUG-7-mekanismen,
  som planlagt.
- `make validate` (alle ~30 skjema i repoet): 0 feil, ingen
  `Error`/`Traceback`/`ValueError` i utdataet.
- `make lint`/`make roundtrip` for `modelldcat-ap-no-schema.yaml`: «No
  problems found», 2 OK/0 feil.
- `make roundtrip` for `brreg-modellkatalog-schema.yaml` (nedstrøms-
  konsument): 2 OK/0 feil — ingen regresjon.
- `make validate-instance` mot `brreg-modellkatalog-eksempel.yaml` og
  produksjonsdatafila: «No issues found» for begge.
