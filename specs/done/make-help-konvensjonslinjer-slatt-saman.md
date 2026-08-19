# Plan: Slå saman konvensjonslinjene i `make help`

## Bakgrunn

Etter [[make-help-sti-konvensjon-forklaring]] og [[make-help-obligatorisk-farge]]
viste `make help` to separate konvensjonslinjer:

```
Konvensjon: (ARG=<verdi>) = obligatorisk, [ARG=<verdi>] = valfri argument
<sti> = filsti relativt til repo-rota
```

Brukaren ønskjer dei slått saman til éi linje, med `<sti>`-forklaringa
etter `valfri argument`.

## Tiltak

`Makefile`: slå saman dei to `@echo`-linjene i `help:`-targetet til éi,
med `, ` som skiljeteikn mellom `valfri argument` og `<sti>`-forklaringa.
Same fargemønster som før (`CLR_OK` for obligatorisk-eksempelet, `CLR_WARN`
for valfri-eksempelet og `<sti>`, `CLR_DBG` for forklarande tekst).

## Handlingsliste

1. [x] Slå saman dei to `@echo`-linjene i `help:`-targetet i `Makefile`
2. [x] Verifiser med `make help`

## Utført

Éi linje i staden for to:

```
Konvensjon: (ARG=<verdi>) = obligatorisk, [ARG=<verdi>] = valfri argument, <sti> = filsti relativt til repo-rota
```

Verifisert med `make help`.
