# Plan: Tilbake til eitt-linje-format i `make help`

## Bakgrunn

Forslag B ([[make-help-argument-og-farge]]) viste kvart target som to
linjer (`make <target> <argument>` + eiga, innrykka skildringslinje).
Brukaren ønskjer i staden alt på éi linje:
`make <target> <argument-uttrykk> <skildring>`.

## Tiltak

`src/assets/scripts/makefile/help.sh`: slå saman dei to `printf`-kalla til
eitt per target, fjern `entry_first`/blank-linje-logikken mellom entries
(ikkje lenger naudsynt når kvart target berre tek éi linje). Same
fargebruk som før — `CLR_STEP` for `make <target>`, `CLR_OK`/`CLR_WARN`
per argumentgruppe, `CLR_DBG` for skildringa — no berre på same linje i
staden for to.

## Handlingsliste

1. [x] Slå saman `printf`-kalla i `help.sh`, fjern blank-linje-logikk
2. [x] Verifiser med `make help`
