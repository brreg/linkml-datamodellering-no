# Plan: Forklar `<sti>`-konvensjon i `make help`

## Bakgrunn

Oppfølging av [[make-help-argumentkonvensjon-forklaring]]
(`specs/done/make-help-argumentkonvensjon-forklaring.md`). Brukaren ønskjer
at konvensjonsforklaringa i `make help` også skal seie kort kva `<sti>`
tyder — at det er ein filsti relativt til repo-rota, ikkje ein
filsystem-absolutt sti.

`<sti>`-plasshaldaren er ikkje unik for `SCHEMA` — same konvensjon gjeld
alle desse argumenta:

```
$ grep -ohE '[A-Z_]+=<sti[^>]*>' make/*.mk Makefile | sort -u
INPUT=<sti-til-json>
INSTANCE=<sti>
JSONSCHEMA=<sti>
MANIFEST=<sti>
SCHEMA=<sti-til-skjema>
SCHEMA=<sti>
SCHEMAS=<sti ...>
```

Forklaringa vert difor generell («`<sti>` er relativt til repo-rota»), ikkje
`SCHEMA`-spesifikk, sidan det ville vore ufullstendig/misvisande for dei
andre `<sti>`-argumenta elles i lista.

## Tiltak

Legg til éi kort, ekstra linje i `help:`-targetet i `Makefile`, rett under
den eksisterande konvensjonslinja:

```
Konvensjon: (ARG=<verdi>) = obligatorisk, [ARG=<verdi>] = valfri argument
<sti> = filsti relativt til repo-rota
```

Same fargemønster som linja over: `CLR_DBG` for forklarande tekst,
`CLR_WARN` for sjølve plasshaldaren.

## Handlingsliste

1. [x] Legg til ny forklaringslinje i `help:`-targetet i `Makefile`
2. [x] Verifiser med `make help`

## Utført

Éi ny `@echo`-linje lagt til rett under den eksisterande konvensjonslinja
i `help:`-targetet, same fargemønster (`CLR_WARN` for `<sti>`, `CLR_DBG`
for forklaringa). Verifisert med `make help`.
