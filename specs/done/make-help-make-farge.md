# Plan: Same farge på «make» som target-namnet

## Bakgrunn

I `src/assets/scripts/makefile/help.sh` sitt to-linjers format
(jf. forslag B i [[make-help-argument-og-farge]]) hadde ordet `make` i
`make <target> <argument>`-linja `CLR_DBG` (dempa), medan target-namnet
hadde `CLR_STEP` (cyan) — dvs. to ulike fargar på same kopierbare
kommandolinje. Brukaren ønskjer at `make` skal ha same farge som
target-namnet, slik at heile kommandoen (`make <target>`) framstår som éi
visuell eining, tydeleg skilt frå både argumentet (gult) og
skildringslinja under (dempa).

## Tiltak

`help.sh`: fjern `CLR_DBG`/`CLR_RST`-paret rundt `make ` og lat
`CLR_STEP` dekke `make <target>` samla (éin `CLR_RST` etter target, før
eit ev. argument-uttrykk i `CLR_WARN`).

## Handlingsliste

1. [x] Endra fargekoding i `help.sh` sine to `printf`-linjer
2. [x] Verifiser med `make help` — `make <target>` no i éin farge
   (cyan), argument gult, skildring dempa
