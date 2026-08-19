# Plan: `<katalognavn>` → `<katalog>` i mkdocs-rettleiingane sine stiillustrasjonar

## Bakgrunn

Oppfølging av [[harmoniser-alle-argument-help-commands]], tiltak F. Der
vart `NAME=<katalognavn>` retta til `NAME=<katalog>` (og
`NAME=<begrepssamling-navn>` til `NAME=<begrepssamling>`) i `make/*.mk`,
`COMMANDS.md` og `mkdocs/docs/kom-i-gang/kommandoar.md` — sjølve
argument-plasshaldaren til `new-begrepskatalog`/`new-begrepssamling`.

Den specen avgrensa seg medvite til desse to overflatene og let følgjande
stå urørt:

> **Utanfor omfang (medvite, ikkje del av tiltak F):** `<katalognavn>` og
> `<begrepssamling-navn>` opptrer òg som stiillustrasjonar i lengre
> mkdocs-rettleiingar (`ny-begrepsmodell.md`, `publisering-begrep.md`,
> `README.md` m.fl.), t.d.
> `src/linkml/begrepskatalog/<katalognavn>/<katalognavn>-schema.yaml`.
> Desse skildrar filstruktur, ikkje sjølve `NAME=`-argumentet, og er eit
> vesentleg større, separat sveip (fleire rettleiingssider, mange
> førekomstar per side) enn resten av denne specen sitt konsekvent
> avgrensa omfang (`make/*.mk` + `COMMANDS.md`, med
> `mkdocs/kommandoar.md` berre der han speglar ei `COMMANDS.md`-rad). Tek
> dette som eiga oppfølgings-spec dersom ønskt.

Denne specen er den oppfølginga.

## Kartlegging

Full repo-søk (utanom `specs/done/`, som er arkivert og urørt per
CLAUDE.md, og `generated/`, som er byggoutput):

### Bracketa stiillustrasjon `<katalognavn>` (reell målgruppe for sveipet)

| Fil | Førekomstar | Døme |
|---|---|---|
| `mkdocs/docs/kom-i-gang/ny-begrepsmodell.md` | 11 | `src/linkml/begrepskatalog/<katalognavn>/<katalognavn>-schema.yaml` |
| `mkdocs/docs/publisering/publisering-begrep.md` | 5 | same mønster, publiseringssteg 3 |
| `src/mcp-linkml-begrep-utkast/README.md` | 1 | `SCHEMA=src/linkml/begrepskatalog/<katalognavn>/<katalognavn>-schema.yaml POLICY=bronze` |

**17 førekomstar totalt**, alle i konsistent bruk som stiillustrasjon —
same mønster som `NAME=`-argumentet no produserer (`<katalog>`), berre at
katalognamnet gjentakast i sjølve filstien/URI-en (t.d.
`<katalognavn>-schema.yaml`, `data.norge.no/linkml/<katalognavn>`).

### `<begrepssamling-navn>` (bracketa form) — ingen levande førekomstar

Ingen fil utanom `specs/done/` og denne/den føregåande specen bruker
`<begrepssamling-navn>` i bracketa form. `README.md` sitt
`new-begrepssamling`-eksempel (linje 115, 119, 123) brukar det **usette**
ordet `begrepssamling-navn` (utan `<>`) som ein konkret eksempelverdi — same
kategori som `PROFILE=bronze`/`FORMAT=json-schema` andre stader (eit
konkret, ikkje eit generisk, eksempel) — og er difor **ikkje** i same
kategori som stiillustrasjonane under. Ingen tiltak naudsynt for
`begrepssamling`-sida av denne oppfølginga.

### Reine prosaordbruk (IKKJE i scope — ikkje ein plasshaldar i det heile)

`CODEOWNERS.md:111`, `CONTRIBUTING.md:143`,
`mkdocs/docs/automasjon/index-md-struktur.md:21`,
`mkdocs/docs/automasjon/readme-tabellgenerering.md:43,250` brukar
«katalognavn»/«katalognamn» som eit vanleg substantiv i laupande tekst
(«…organisasjonsnivå-metadata (katalognavn, kontaktpunkt…)»), ikkje som
ein `<...>`-plasshaldar. Desse er korrekt norsk prosa og skal **ikkje**
endrast.

## Plan

Erstatt alle 17 `<katalognavn>`-førekomstar i dei tre fillista med
`<katalog>`, konsekvent med fasiten frå
[[harmoniser-alle-argument-help-commands]] tiltak F. Reint
søk-og-erstatt — ingen semantiske vurderingar naudsynte, sidan alle
førekomstane er same type stiillustrasjon.

Eksempel på transformasjon (frå `ny-begrepsmodell.md`):

```diff
-src/linkml/begrepskatalog/<katalognavn>/
-├── <katalognavn>-schema.yaml  ← skjema med BegrepContainer og import av skos-ap-no
+src/linkml/begrepskatalog/<katalog>/
+├── <katalog>-schema.yaml  ← skjema med BegrepContainer og import av skos-ap-no
```

## Filer som vert påverka

- `mkdocs/docs/kom-i-gang/ny-begrepsmodell.md` (11 førekomstar)
- `mkdocs/docs/publisering/publisering-begrep.md` (5 førekomstar)
- `src/mcp-linkml-begrep-utkast/README.md` (1 førekomst)

## Handlingsliste

1. [x] Erstatt `<katalognavn>` → `<katalog>` i alle 17 førekomstar i dei
   tre fillista over
2. [x] Verifiser med `grep -rn "<katalognavn>"` (utanom `specs/done/`) at
   ingen bracketa førekomstar står att
3. [x] Stikkprøve: les gjennom `ny-begrepsmodell.md` i samanheng for å
   stadfeste at ingen linjer vart brotne av søk-og-erstattet (spesielt
   URI-ar og fil-tre-illustrasjonar med fleire `<katalognavn>` per linje)

## Utført

`replace_all` av `<katalognavn>` → `<katalog>` i alle tre filer. Ingen
semantiske vurderingar naudsynte — reint søk-og-erstatt, som planlagt.

Overraskande funn under verifiseringa: `mkdocs/docs/publisering/publisering-begrep.md`
hadde alt to `<katalog>`-førekomstar (linje 5, 35) **før** denne endringa,
side om side med dei 5 `<katalognavn>`-linjene — eit teikn på at fila alt
var i ferd med å drive mot `<katalog>` som den reelle konvensjonen. Denne
oppfølginga gjer no heile fila (og dei to andre) fullt konsistente.

**Verifisert:** Ingen bracketa `<katalognavn>` står att i nokon levande
fil (utanfor `specs/done/` og denne specen sjølv, som medvite dokumenterer
før-tilstanden). Alle tre filer lest gjennom i samanheng — ingen brotne
linjer, korrekt `<katalog>/<katalog>-schema.yaml`-mønster gjennomgåande.
