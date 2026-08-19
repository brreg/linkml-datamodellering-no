# Plan: Forklaringslinje for argumentkonvensjon i `make help`

## Bakgrunn

Etter [[make-help-argument-og-farge]] (`specs/done/make-help-argument-og-farge.md`)
og [[domain-name-argumentrekkjefolge]] viser `make help` argumenta til kvart
target på ei eiga, farga linje — med parentes `(ARG=<verdi>)` for
obligatoriske og hakeparentes `[ARG=<verdi>]` for valfrie argument. Denne
konvensjonen er dokumentert i toppkommentaren i
`src/assets/scripts/makefile/help.sh`, men er **ikkje synleg for brukaren i
sjølve `make help`-outputen** — ein brukar som ikkje har lese kjeldekoden må
gjette seg til kva parentes vs. hakeparentes tyder.

Brukaren ønskjer éi forklarande linje i `make help`-output som gjer denne
konvensjonen eksplisitt.

## Tiltak

Legg til éi linje i `help:`-targetet i `Makefile`, rett under overskrifta
`Tilgjengelege make-target:` og før kategorilista, som forklarer
konvensjonen. Fargelegging følgjer same mønster som resten av
argumentvisinga (jf. forslag B i [[make-help-argument-og-farge]]):
- Forklarande tekst: `CLR_DBG` (dempa) — same rolle som skildringstekst elles
- Sjølve eksempel-uttrykka `(ARG=<verdi>)`/`[ARG=<verdi>]`: `CLR_WARN` (gul) —
  same farge argumenta faktisk vert vist med lenger nede, slik at legenda
  visuelt koplar seg til resten av lista

```
Tilgjengelege make-target:
Konvensjon: (ARG=<verdi>) = obligatorisk, [ARG=<verdi>] = valfri argument

Vanleg bruk:
  make roundtrip [SCHEMA=<sti>]
      Køyr roundtrip-testar (YAML→TTL→YAML)
  ...
```

## Handlingsliste

1. [x] Legg til forklaringslinje i `help:`-targetet i `Makefile`
2. [x] Verifiser med `make help` at linja vert vist korrekt, med farge

## Utført

`Makefile` `help:`-targetet: éi ny `@echo`-linje rett under
`Tilgjengelege make-target:`-overskrifta, med `CLR_DBG` for forklarande
tekst og `CLR_WARN` for eksempel-uttrykka (same farge argumenta faktisk
vert vist med i lista under). Verifisert med `make help`.
